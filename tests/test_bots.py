"""Bots com estilo (Fase 2): perfis, leitura do Radar, blefe, contestação e cada estilo."""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Sequence
from typing import Any

import numpy as np
import pytest
from conftest import RAIZ, jogar, montar
from hypothesis import given, settings
from hypothesis import strategies as st

from critical_failure.bots.base import Decisao
from critical_failure.bots.estimativas import chance_de_nao_ter, copias_nao_vistas
from critical_failure.bots.estimativas import teste_mais_provavel as mais_provavel
from critical_failure.bots.estrategicos import (
    BotCacador,
    BotConstrutor,
    BotEstrategico,
    BotHeuristico,
    exp_deterministico,
)
from critical_failure.bots.fabrica import criar_bot, perfis, resolver
from critical_failure.bots.mesa import MesaPublica, mesa_do_motor
from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.observacao import Observacao, observar
from critical_failure.partida import jogar_partida
from critical_failure.regras.v2 import acoes as A
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.acoes import Acao
from critical_failure.regras.v2.estado import Evento, Pendente
from critical_failure.regras.v2.motor import MotorV2

EXPERIENTE = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}


class Gravador:
    """Envolve um bot e guarda cada observação e decisão, para os testes conferirem o estilo."""

    def __init__(self, bot: Any) -> None:
        self.bot = bot
        self.tipo = bot.tipo
        self.decisoes: list[tuple[Observacao, list[Acao], Decisao]] = []

    def parametros(self) -> dict[str, Any]:
        return dict(self.bot.parametros())

    def iniciar(self, semente: int, partida: int, assento: int, mesa: MesaPublica | None = None) -> None:
        self.bot.iniciar(semente, partida, assento, mesa)

    def decidir(self, observacao: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        decisao: Decisao = self.bot.decidir(observacao, opcoes)
        self.decisoes.append((observacao, list(opcoes), decisao))
        return decisao


def mesa_mista(blefe: str = "metade", contestacao: str = "limiar") -> list[Gravador]:
    comum = {"conhecimento": "experiente", "blefe": blefe, "contestacao": contestacao}
    return [
        Gravador(criar_bot("construtor", comum)),
        Gravador(criar_bot("cacador", {**comum, "alvo": "lider"})),
        Gravador(criar_bot("heuristico", comum)),
        Gravador(criar_bot("cacador", {**comum, "alvo": "mais_fraco"})),
    ]


def jogar_gravando(
    motor: MotorV2, bots: list[Gravador], semente: int, partida: int
) -> tuple[list[Gravador], list[Evento]]:
    eventos: list[Evento] = []
    jogar_partida(
        motor, bots, semente, partida, conferir_invariantes=True, ouvinte=lambda evento, d: eventos.append(evento)
    )
    return bots, eventos


def decisoes_do_tipo(gravador: Gravador, tipo: str) -> list[tuple[Observacao, list[Acao], Decisao]]:
    return [registro for registro in gravador.decisoes if registro[0].decisao_pedida == tipo]


# ---------------------------------------------------------------- perfis e fábrica


def test_perfis_aprovados_pelo_autor() -> None:
    tabela = perfis()
    assert tabela["conhecimento"]["iniciante"] == {
        "explicacao_correta": 0.5, "diagnostico_certo": 0.4, "secundaria_no_erro": 0.5, "precisao_auditor": 0.75,
    }  # fmt: skip
    assert tabela["conhecimento"]["experiente"] == {
        "explicacao_correta": 0.85, "diagnostico_certo": 0.8, "secundaria_no_erro": 0.5, "precisao_auditor": 0.95,
    }  # fmt: skip
    assert tabela["blefe"] == {"nunca": 0.0, "metade": 0.5, "sempre": 1.0}
    assert tabela["contestacao"] == ["nunca", "sempre", "limiar"]
    assert tabela["heuristico"]["temperatura"] == 0.5


def test_fabrica_resolve_os_nomes_de_perfil_e_o_registro_guarda_os_valores() -> None:
    bot = criar_bot("heuristico", EXPERIENTE)
    parametros = bot.parametros()
    assert parametros["conhecimento"]["diagnostico_certo"] == 0.8 and parametros["blefe"] == 0.5
    assert parametros["temperatura"] == 0.5 and parametros["desconto_do_futuro"] == 0.8
    # Recriar com os valores gravados dá o mesmo bot: é o que o replay faz.
    assert criar_bot("heuristico", parametros).parametros() == parametros
    assert resolver("aleatorio", {"explicacao_correta": 0.5}) == {"explicacao_correta": 0.5}


@pytest.mark.parametrize(
    "tipo, parametros",
    [
        ("construtor", {**EXPERIENTE, "conhecimento": "genio"}),
        ("construtor", {**EXPERIENTE, "blefe": "as_vezes"}),
        ("construtor", {**EXPERIENTE, "blefe": 1.5}),
        ("construtor", {**EXPERIENTE, "contestacao": "talvez"}),
        ("construtor", {"blefe": 0.5, "contestacao": "limiar"}),
        ("construtor", {**EXPERIENTE, "conhecimento": {"explicacao_correta": 0.5}}),
        ("cacador", EXPERIENTE),  # falta a política de alvo
        ("cacador", {**EXPERIENTE, "alvo": "vizinho"}),
        ("heuristico", {**EXPERIENTE, "temperatura": -1}),
        ("robo", {}),
    ],
)
def test_parametros_invalidos_geram_erro_controlado(tipo: str, parametros: dict[str, Any]) -> None:
    with pytest.raises(ConfiguracaoInvalida):
        criar_bot(tipo, parametros)


def test_bot_com_estilo_precisa_da_mesa() -> None:
    with pytest.raises(ValueError):
        criar_bot("construtor", EXPERIENTE).iniciar(1, 0, 0, None)


# ---------------------------------------------------------------- softmax determinístico


def test_exp_deterministico_bate_com_a_exponencial() -> None:
    for x in [0.0, -1e-9, -0.1, -0.5, -0.7, -1.0, -2.5, -7.3, -20.0, -45.0]:
        assert exp_deterministico(x) == pytest.approx(math.exp(x), rel=1e-12, abs=1e-300)
    assert exp_deterministico(-100.0) == 0.0
    with pytest.raises(ValueError):
        exp_deterministico(0.1)


def test_softmax_com_temperatura_baixa_escolhe_o_maior_valor(motor: MotorV2) -> None:
    bot = criar_bot("heuristico", {**EXPERIENTE, "temperatura": 0.01})
    bot.iniciar(1, 0, 0, mesa_do_motor(motor))
    assert isinstance(bot, BotHeuristico)
    valores = [(Acao(A.PASSAR), 0.0), (Acao(A.ENCERRAR), 1.0), (Acao(A.RECUSAR), 0.5)]
    escolhas = Counter(bot._escolher(valores, "teste").acao.tipo for _ in range(200))
    assert escolhas == {A.ENCERRAR: 200}


def test_softmax_segue_a_temperatura(motor: MotorV2) -> None:
    bot = criar_bot("heuristico", EXPERIENTE)  # temperatura 0,5
    bot.iniciar(1, 0, 0, mesa_do_motor(motor))
    assert isinstance(bot, BotHeuristico)
    valores = [(Acao(A.PASSAR), 0.0), (Acao(A.ENCERRAR), 0.5)]
    escolhas = Counter(bot._escolher(valores, "teste").acao.tipo for _ in range(4000))
    # Com T = 0,5 e diferença de 0,5: P(encerrar) = e / (1 + e), cerca de 0,731.
    assert 0.70 < escolhas[A.ENCERRAR] / 4000 < 0.76


# ---------------------------------------------------------------- leitura do Radar (MOD-03, MOD-04)


def _leituras(motor: MotorV2, numero: str, certo: int, secundaria: int, vezes: int = 3000) -> Counter[str]:
    leitor = mesa_do_motor(motor).leitor
    rng = np.random.default_rng(2026)
    return Counter(leitor.ler(numero, certo, secundaria, rng).categoria for _ in range(vezes))


def test_leitura_com_acerto_certo_ou_nulo(motor: MotorV2) -> None:
    assert _leituras(motor, "07", 1000, 500) == {"Confiabilidade": 3000}
    assert "Confiabilidade" not in _leituras(motor, "07", 0, 500)


def test_ao_errar_metade_cai_na_secundaria_e_o_resto_nas_vizinhas(motor: MotorV2) -> None:
    # 13 | Campanha viral: chave Flexibilidade, secundária Desempenho. O teste-chave (Escalabilidade) só é
    # confundido com Carga e Pico, de Desempenho: sem outra vizinha, o resto do erro vai para as demais categorias.
    leituras = _leituras(motor, "13", 0, 500)
    assert 0.45 < leituras["Desempenho"] / 3000 < 0.55
    assert "Flexibilidade" not in leituras and len(leituras) == 6
    # 04 | Nova política de segurança da TI: chave Compatibilidade, sem secundária. Coexistência é confundida
    # com Adaptabilidade (Flexibilidade): todo erro vai para Flexibilidade.
    assert _leituras(motor, "04", 0, 500) == {"Flexibilidade": 3000}


def test_a_leitura_e_a_mesma_em_qualquer_estilo_e_vale_o_jogo_todo(motor: MotorV2) -> None:
    mesa = mesa_do_motor(motor)
    bots: list[BotEstrategico] = [
        BotConstrutor(perfis()["conhecimento"]["iniciante"], 0.5, "limiar"),
        BotHeuristico(perfis()["conhecimento"]["iniciante"], 0.0, "nunca", 0.5, 0.8),
    ]
    for bot in bots:
        bot.iniciar(9, 4, 2, mesa)
    for numero in motor.catalogo.incidentes:
        assert bots[0].leitura(numero) == bots[1].leitura(numero) == bots[0].leitura(numero)


def test_o_diagnostico_e_a_leitura_usada_no_planejamento(motor: MotorV2) -> None:
    bots, eventos = jogar_gravando(motor, mesa_mista(), semente=3, partida=11)
    for assento, gravador in enumerate(bots):
        bot = gravador.bot
        for obs, _, decisao in decisoes_do_tipo(gravador, E.DIAGNOSTICAR):
            assert obs.radar_agora is not None
            assert decisao.acao.categoria == bot.leitura(obs.radar_agora.numero).categoria
        escolhas = [
            ev.oculto["categoria"] for ev in eventos if ev.tipo == "diagnostico_escolhido" and ev.ator == assento
        ]
        assert len(escolhas) == 3


# ---------------------------------------------------------------- estimativas com informação pública


def test_chance_de_nao_ter(motor: MotorV2) -> None:
    mesa = mesa_do_motor(motor)
    estado = montar(motor, sistemas=[[], ["Carga", "Regressão"], [], []], maos=[["Pico"], [], [], []])
    obs = observar(estado, 0, motor.catalogo)
    # Sistema vazio: certeza de não ter.
    assert chance_de_nao_ter(obs, mesa, 2, ["Carga"]) == 1.0
    # Bruno tem 2 cartas escondidas. Ana viu só a própria Pico: 62 cartas não vistas, 3 delas Carga.
    assert chance_de_nao_ter(obs, mesa, 1, ["Carga"]) == pytest.approx((59 / 62) * (58 / 61))
    desempenho = mesa.testes_por_categoria["Desempenho"]  # 9 cartas, menos a Pico de Ana
    assert chance_de_nao_ter(obs, mesa, 1, desempenho) == pytest.approx((54 / 62) * (53 / 61))
    # Depois que a Carga de Bruno é revelada numa contestação, a chance é 0.
    estado, _ = jogar(motor, estado, "testar:Pico:1", "defender:Carga", "confere", "contestar")
    obs = observar(estado, 2, motor.catalogo)
    assert chance_de_nao_ter(obs, mesa, 1, ["Carga"]) == 0.0
    assert copias_nao_vistas(obs, mesa)["Carga"] == 2  # a revelada já foi vista
    assert copias_nao_vistas(obs, mesa)["Pico"] == 1  # a de Ana foi para o descarte


def test_o_blefe_nomeia_o_teste_mais_provavel(motor: MotorV2) -> None:
    mesa = mesa_do_motor(motor)
    estado = montar(motor, maos=[["Carga", "Carga", "Pico"], [], [], []], backlog=["Estresse"])
    obs = observar(estado, 0, motor.catalogo)
    # Ana viu 2 das 3 Cargas, 1 das 2 Picos e 1 das 2 Estresses: a que mais falta ver é Resistência (2).
    assert mais_provavel(obs, mesa, "Desempenho") == "Resistência"
    # Sem nenhuma carta vista, ganha a de mais cópias: Carga (3).
    assert mais_provavel(observar(montar(motor), 0, motor.catalogo), mesa, "Desempenho") == "Carga"


# ---------------------------------------------------------------- blefe e contestação


@pytest.mark.parametrize("blefe", ["nunca", "sempre"])
def test_perfil_de_blefe(motor: MotorV2, blefe: str) -> None:
    defesas = 0
    for partida in range(6):
        bots, eventos = jogar_gravando(motor, mesa_mista(blefe=blefe), semente=8, partida=partida)
        for gravador in bots:
            for obs, _, decisao in decisoes_do_tipo(gravador, E.RESPONDER):
                assert obs.disputa is not None
                tem = any(mesa_do_motor(motor).categoria(t) == obs.disputa.categoria for t in obs.sistema)
                defesas += 1
                if tem:  # com a carta, sempre defende com a verdade
                    assert decisao.acao.tipo == A.DEFENDER and decisao.acao.teste in obs.sistema
                elif blefe == "nunca":
                    assert decisao.acao.tipo == A.ADMITIR
                else:
                    assert decisao.acao.tipo == A.DEFENDER and decisao.acao.teste not in obs.sistema
    assert defesas > 20


@pytest.mark.parametrize("contestacao", ["nunca", "sempre", "limiar"])
def test_perfil_de_contestacao(motor: MotorV2, contestacao: str) -> None:
    vistas = Counter[str]()
    for partida in range(6):
        bots, _ = jogar_gravando(motor, mesa_mista(contestacao=contestacao), semente=4, partida=partida)
        for gravador in bots:
            for obs, _, decisao in decisoes_do_tipo(gravador, E.CONTESTAR):
                vistas[decisao.acao.tipo] += 1
                if contestacao == "limiar":
                    assert obs.disputa is not None and obs.disputa.teste_nomeado is not None
                    chance = chance_de_nao_ter(
                        obs, mesa_do_motor(motor), obs.disputa.defensor, [obs.disputa.teste_nomeado]
                    )
                    assert (decisao.acao.tipo == A.CONTESTAR) == (chance >= 1 / 3)
    if contestacao == "nunca":
        assert set(vistas) == {A.ACEITAR}
    elif contestacao == "sempre":
        assert set(vistas) == {A.CONTESTAR}
    else:
        assert set(vistas) == {A.ACEITAR, A.CONTESTAR}


def test_o_limiar_vem_das_regras_em_uso() -> None:
    from conftest import criar_motor

    for punicao, esperado in ((1, "1/3"), (2, "1/4"), (0, "1/2")):
        motor = criar_motor(**{"disputa.contestacao_blefe.defensor_paga": punicao})
        bot = criar_bot("construtor", EXPERIENTE)
        bot.iniciar(1, 0, 0, mesa_do_motor(motor))
        assert isinstance(bot, BotEstrategico)
        assert str(bot.limiar_de_contestacao()) == esperado


def test_o_auditor_segue_a_precisao(motor: MotorV2) -> None:
    perfeito = {"explicacao_correta": 0.5, "diagnostico_certo": 0.5, "secundaria_no_erro": 0.5, "precisao_auditor": 1.0}
    bot = BotConstrutor(perfeito, 0.5, "limiar")
    bot.iniciar(1, 0, 3, mesa_do_motor(motor))
    estado = montar(motor, maos=[["Carga"], [], [], []])
    for correta, esperado in ((True, A.CONFERE), (False, A.NAO_CONFERE)):
        depois, _ = jogar(motor, estado, "testar:Carga:1", Acao(A.DEFENDER, teste="Pico", explicacao_correta=correta))
        assert depois.pendente == Pendente(E.CONFERIR, 3)
        decisao = bot.decidir(observar(depois, 3, motor.catalogo), motor.acoes_legais(depois))
        assert decisao.acao.tipo == esperado


# ---------------------------------------------------------------- os estilos


def test_construtor_enche_o_sistema_e_so_testa_com_sobras(motor: MotorV2) -> None:
    teto = motor.teto
    testes = 0
    for partida in range(8):
        bots, _ = jogar_gravando(motor, mesa_mista(), semente=12, partida=partida)
        construtor = bots[0]
        bot = construtor.bot
        assert isinstance(bot, BotConstrutor)
        for obs, _, decisao in decisoes_do_tipo(construtor, E.AGIR):
            if decisao.acao.tipo == A.TESTAR:
                testes += 1
                teste = decisao.acao.teste or ""
                assert len(obs.sistema) == teto or bot._prioridade(obs, teste, obs.sistema) is None
        for obs, _, decisao in decisoes_do_tipo(construtor, E.COLOCAR):
            if decisao.acao.tipo == A.ENCERRAR:
                assert all(bot._prioridade(obs, teste, obs.sistema) is None for teste in obs.mao)
        # Fim do Planejamento do ciclo 1: o Construtor já colocou tudo o que melhora o sistema.
        # Na Homologação do ciclo 1 (se ele chegou a ter vez), já colocou tudo o que melhora o sistema.
        primeira = next((obs for obs, _, _ in decisoes_do_tipo(construtor, E.AGIR) if obs.ciclo == 1), None)
        if primeira is not None and len(primeira.sistema) < teto:
            assert all(bot._prioridade(primeira, t, primeira.sistema) is None for t in primeira.mao)
    assert testes > 0


def test_cacador_coloca_no_maximo_uma_carta_por_ciclo_e_da_categoria_do_agora(motor: MotorV2) -> None:
    for partida in range(8):
        bots, _ = jogar_gravando(motor, mesa_mista(), semente=13, partida=partida)
        for gravador in (bots[1], bots[3]):
            bot = gravador.bot
            assert isinstance(bot, BotCacador)
            colocadas = Counter[int]()
            for obs, _, decisao in decisoes_do_tipo(gravador, E.COLOCAR):
                if decisao.acao.tipo == A.COLOCAR:
                    colocadas[obs.ciclo] += 1
                    assert mesa_do_motor(motor).categoria(decisao.acao.teste or "") == bot.categoria_do_agora(obs)
            assert all(vezes <= 1 for vezes in colocadas.values())


@pytest.mark.parametrize("politica, extremo", [("lider", max), ("mais_fraco", min)])
def test_cacador_escolhe_o_alvo_pela_politica(motor: MotorV2, politica: str, extremo: Any) -> None:
    testes = 0
    for partida in range(6):
        comum = {**EXPERIENTE, "alvo": politica}
        bots = [Gravador(criar_bot("cacador", comum)) for _ in range(4)]
        jogar_gravando(motor, bots, semente=21, partida=partida)
        for gravador in bots:
            for obs, opcoes, decisao in decisoes_do_tipo(gravador, E.AGIR):
                if decisao.acao.tipo != A.TESTAR:
                    continue
                testes += 1
                alvos = [o.alvo for o in opcoes if o.tipo == A.TESTAR and o.teste == decisao.acao.teste]
                fichas = [obs.jogadores[alvo].fichas for alvo in alvos if alvo is not None]
                assert obs.jogadores[decisao.acao.alvo or 0].fichas == extremo(fichas)
    assert testes > 20


def test_os_estilos_jogam_diferente(motor: MotorV2) -> None:
    tamanhos: dict[str, list[int]] = {"construtor": [], "cacador": [], "heuristico": []}
    for partida in range(20):
        bots, eventos = jogar_gravando(motor, mesa_mista(), semente=31, partida=partida)
        final = eventos[-1].estado
        for assento, gravador in enumerate(bots[:3]):
            tamanhos[gravador.tipo].append(len(final.jogadores[assento].sistema))
    media = {estilo: sum(valores) / len(valores) for estilo, valores in tamanhos.items()}
    assert media["construtor"] > media["cacador"] + 1


@settings(max_examples=30, deadline=None)
@given(
    semente=st.integers(0, 2**32 - 1),
    partida=st.integers(0, 10**6),
    estilos=st.lists(st.sampled_from(["construtor", "cacador", "heuristico", "aleatorio"]), min_size=4, max_size=5),
    conhecimento=st.sampled_from(["iniciante", "experiente"]),
    blefe=st.sampled_from(["nunca", "metade", "sempre"]),
    contestacao=st.sampled_from(["nunca", "sempre", "limiar"]),
    alvo=st.sampled_from(["lider", "mais_fraco", "aleatorio"]),
)
def test_qualquer_mesa_de_bots_termina_sem_violar_invariantes(
    motor: MotorV2,
    semente: int,
    partida: int,
    estilos: list[str],
    conhecimento: str,
    blefe: str,
    contestacao: str,
    alvo: str,
) -> None:
    def novo(estilo: str) -> Any:
        if estilo == "aleatorio":
            return criar_bot("aleatorio", {})
        parametros: dict[str, Any] = {"conhecimento": conhecimento, "blefe": blefe, "contestacao": contestacao}
        if estilo == "cacador":
            parametros["alvo"] = alvo
        return criar_bot(estilo, parametros)

    primeira = jogar_partida(motor, [novo(e) for e in estilos], semente, partida, conferir_invariantes=True)
    segunda = jogar_partida(motor, [novo(e) for e in estilos], semente, partida)
    assert primeira.estado_final.fase == E.FIM
    assert segunda == primeira


def test_o_codigo_dos_bots_nao_consulta_o_gabarito() -> None:
    """Os bots só leem o relato pelo Leitor. Nenhum outro módulo de bots toca no catálogo de incidentes."""
    for nome in ("estrategicos.py", "estimativas.py", "fabrica.py", "aleatorio.py", "base.py"):
        codigo = (RAIZ / "src" / "critical_failure" / "bots" / nome).read_text(encoding="utf-8")
        assert not re.search(r"\.incidentes\b|__gabaritos|_Leitor__|\bCatalogo\b|\bcatalogo\b", codigo), nome

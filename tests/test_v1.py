"""Regras da v1 (docs/especificacao_v1.md): um ou mais testes por regra, e os bots da v1."""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence
from dataclasses import replace
from typing import Any

import pytest
from conftest import CONFIGS, criar_motor, ler_yaml
from hypothesis import given, settings
from hypothesis import strategies as st

from critical_failure.auditoria import registro, replay
from critical_failure.auditoria.narrar import narrar
from critical_failure.bots.fabrica import criar_bot
from critical_failure.bots.mesa import mesa_para
from critical_failure.nucleo.erros import AcaoIlegal, ConfiguracaoInvalida
from critical_failure.partida import jogar_partida
from critical_failure.regras.familias import carregar_motor, motor_de
from critical_failure.regras.v1 import acoes as A
from critical_failure.regras.v1 import estado as E
from critical_failure.regras.v1.acoes import AcaoV1, acao_v1_de_dict
from critical_failure.regras.v1.config import ler_regras_v1
from critical_failure.regras.v1.estado import EstadoV1, EventoV1, JogadorV1, Pendente
from critical_failure.regras.v1.motor import MotorV1
from critical_failure.regras.v1.pontuacao import pontuar

LOAD = "Load (Eficiência de Desempenho)"
STRESS = "Stress (Eficiência de Desempenho)"
SCALABILITY = "Scalability (Eficiência de Desempenho)"
STRESS_USABILIDADE = "Stress (Usabilidade)"
COEXISTENCE = "Coexistence (Compatibilidade)"
RECOVERY = "Recovery (Confiabilidade)"
AUTHENTICATION = "Authentication (Segurança)"
ADAPTABILITY = "Adaptability (Portabilidade)"
AB = "A/B (Usabilidade)"
CF = "Critical Failure"
REGRAS_V1 = CONFIGS / "regras_v1.yaml"
EXPERIENTE = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}


@pytest.fixture(scope="module")
def motor() -> MotorV1:
    motor = carregar_motor(REGRAS_V1)
    assert isinstance(motor, MotorV1)
    return motor


def montar_v1(
    motor: MotorV1,
    *,
    n: int = 4,
    sistemas: Sequence[Sequence[str]] | None = None,
    maos: Sequence[Sequence[str]] | None = None,
    vez: int = 0,
    pendente: Pendente | None = None,
) -> EstadoV1:
    """Um estado na fase de testes; o que não foi pedido fica no baralho."""
    livres: dict[str, list[int]] = {}
    for carta, nome in enumerate(motor.catalogo.cartas):
        livres.setdefault(nome, []).append(carta)

    def pegar(nomes: Sequence[str]) -> tuple[int, ...]:
        return tuple(livres[nome].pop(0) for nome in nomes)

    vazio: list[list[str]] = [[] for _ in range(n)]
    cartas_do_sistema = [pegar(nomes) for nomes in (sistemas or vazio)]
    cartas_da_mao = [pegar(nomes) for nomes in (maos or vazio)]
    jogadores = tuple(
        JogadorV1(
            mao=cartas_da_mao[j],
            sistema=cartas_do_sistema[j],
            reveladas=(),
            testes_feitos=motor.cartas_de_teste - len(cartas_da_mao[j]),
            pontos=0,
        )
        for j in range(n)
    )
    return EstadoV1(
        semente=5,
        partida=0,
        contador_rng=10,
        jogadores=jogadores,
        baralho=tuple(sorted(c for resto in livres.values() for c in resto)),
        descarte=(),
        fase=E.TESTES,
        vez=vez,
        pendente=pendente or Pendente(E.TESTAR, vez),
        disputa=None,
        historico=(),
        vencedores=(),
    )


def jogar(motor: MotorV1, estado: EstadoV1, *passos: AcaoV1) -> tuple[EstadoV1, list[EventoV1]]:
    eventos: list[EventoV1] = []
    for passo in passos:
        estado, novos = motor.aplicar(estado, passo)
        eventos += novos
    return estado, eventos


def ataque(carta: str, alvo: int) -> AcaoV1:
    return AcaoV1(A.TESTAR, cartas=(carta,), alvo=alvo)


TEM = AcaoV1(A.DECLARAR, tem=True, explicacao_correta=True)
NAO_TEM = AcaoV1(A.DECLARAR, tem=False)
ACEITAR = AcaoV1(A.ACEITAR)
DUVIDAR = AcaoV1(A.DUVIDAR)
CONTESTAR = AcaoV1(A.CONTESTAR)


def tipos(eventos: list[EventoV1]) -> list[str]:
    return [evento.tipo for evento in eventos]


def nomes(motor: MotorV1, cartas: tuple[int, ...]) -> list[str]:
    return motor.catalogo.nomes(cartas)


# ---------------------------------------------------------------- componentes e configuração


@pytest.mark.regra("V1-T2.1", "V1-4.1.1", "V1-4.2.1")
def test_baralho_da_tabela_3(motor: MotorV1) -> None:
    contagem = Counter(motor.catalogo.atributo_da(carta) for carta in range(len(motor.catalogo.cartas)))
    assert len(motor.catalogo.cartas) == 54
    assert contagem == {
        "Eficiência de Desempenho": 9,
        "Compatibilidade": 6,
        "Confiabilidade": 9,
        "Segurança": 9,
        "Portabilidade": 9,
        "Usabilidade": 9,
        "Especial": 3,
    }
    assert len(motor.catalogo.atributos) == 6 and "Especial" not in motor.catalogo.atributos
    # AMB-26: o teste é o par atributo e nome. Os dois "Stress" são testes diferentes.
    assert motor.catalogo.atributo[STRESS] != motor.catalogo.atributo[STRESS_USABILIDADE]
    assert motor.catalogo.especiais == {CF}


def test_todo_parametro_da_especificacao_da_v1_esta_no_yaml(motor: MotorV1) -> None:
    import re

    from conftest import RAIZ

    especificacao = (RAIZ / "docs" / "especificacao_v1.md").read_text(encoding="utf-8")
    declarados = motor.regras.parametros()
    achados = dict(re.findall(r"`v1\.([a-z0-9_.]+)=([^`]+)`", especificacao))
    assert achados, "a especificação da v1 deveria declarar parâmetros"
    for chave, valor in achados.items():
        assert chave in declarados, f"v1.{chave} está na especificação e falta em configs/regras_v1.yaml"
        assert str(declarados[chave][0]) == valor, chave
    for chave, (_, regra) in declarados.items():
        if not chave.startswith("interpretacoes."):
            assert chave in achados, f"{chave} está no YAML da v1 e falta na especificação"
            linha = next(linha for linha in especificacao.splitlines() if linha.startswith(f"| {regra} |"))
            assert f"`v1.{chave}=" in linha, f"{chave} cita {regra}, que não declara o parâmetro"


@pytest.mark.parametrize(
    "caminho, valor",
    [
        ("baralho.cartas.valor", 55),
        ("atributos.valor", 7),
        ("sistema_inicial.valor", 4),
        ("jogadores.maximo.valor", 10),
        ("interpretacoes.pontuacao_combinacoes.valor", "todas"),
        ("familia", "v2"),
    ],
)
def test_configuracao_da_v1_malformada_gera_erro_controlado(caminho: str, valor: Any) -> None:
    import copy

    dados = copy.deepcopy(ler_yaml(REGRAS_V1))
    no = dados
    *partes, ultima = caminho.split(".")
    for parte in partes:
        no = no[parte]
    no[ultima] = valor
    with pytest.raises(ConfiguracaoInvalida):
        ler_regras_v1(dados)


def test_familia_desconhecida() -> None:
    with pytest.raises(ConfiguracaoInvalida):
        motor_de({"familia": "v3"}, CONFIGS)
    with pytest.raises(ConfiguracaoInvalida):
        motor_de(None, CONFIGS)


# ---------------------------------------------------------------- preparação e montagem


@pytest.mark.regra("V1-T2.2")
def test_numero_de_jogadores(motor: MotorV1) -> None:
    for n in (3, 8):
        estado, _ = motor.preparar(n, 1, 0)
        assert estado.n == n
    for n in (2, 9):
        with pytest.raises(ConfiguracaoInvalida, match="V1-T2.2"):
            motor.preparar(n, 1, 0)


@pytest.mark.regra("V1-4.3.1", "V1-4.3.2")
def test_cada_jogador_compra_seis_cartas_e_ha_ordem_de_jogo(motor: MotorV1) -> None:
    estado, eventos = motor.preparar(5, 3, 1)
    assert [len(jogador.mao) for jogador in estado.jogadores] == [6] * 5
    assert len(estado.baralho) == 54 - 30
    assert [ev.ator for ev in eventos if ev.tipo == "mao_inicial"] == [0, 1, 2, 3, 4]
    mao = next(ev for ev in eventos if ev.tipo == "mao_inicial")
    assert mao.oculto["mao"] and mao.visivel_para == {"mao": [0]}
    assert next(ev for ev in eventos if ev.tipo == "ordem_de_jogo").publico == {"ordem": [0, 1, 2, 3, 4]}
    assert estado.fase == E.MONTAGEM and estado.pendente == Pendente(E.MONTAR, 0)


@pytest.mark.regra("V1-4.3.3", "V1-4.2.2")
def test_montagem_do_sistema(motor: MotorV1) -> None:
    estado, _ = motor.preparar(3, 7, 0)
    opcoes = motor.acoes_legais(estado)
    assert opcoes and all(len(acao.cartas) == 3 and CF not in acao.cartas for acao in opcoes)
    estado, eventos = jogar(motor, estado, opcoes[0])
    jogador = estado.jogadores[0]
    assert len(jogador.sistema) == 3 and len(jogador.mao) == 3
    assert sorted(nomes(motor, jogador.sistema)) == sorted(opcoes[0].cartas)
    montado = next(ev for ev in eventos if ev.tipo == "sistema_montado")
    assert montado.publico == {"cartas": 3} and montado.visivel_para == {"sistema": [0]}
    assert estado.pendente == Pendente(E.MONTAR, 1)
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, AcaoV1(A.MONTAR, cartas=(LOAD, LOAD, LOAD)))


@pytest.mark.regra("V1-4.2.2", "V1-4.3.3")
def test_critical_failure_fica_obrigatoriamente_na_mao(motor: MotorV1) -> None:
    """AMB-28: com 3 Critical Failure na mão, só há um jeito de montar o sistema."""
    estado = montar_v1(motor, n=3)
    livres = list(estado.baralho)
    mao = tuple(c for c in livres if motor.catalogo.cartas[c] == CF)[:3]
    mao += tuple(c for c in livres if motor.catalogo.cartas[c] == LOAD)[:3]
    jogadores = (replace(estado.jogadores[0], mao=mao, testes_feitos=0), *estado.jogadores[1:])
    estado = replace(
        estado,
        jogadores=jogadores,
        baralho=tuple(c for c in livres if c not in mao),
        fase=E.MONTAGEM,
        pendente=Pendente(E.MONTAR, 0),
    )
    assert motor.acoes_legais(estado) == (AcaoV1(A.MONTAR, cartas=(LOAD, LOAD, LOAD)),)


# ---------------------------------------------------------------- fase de testes


@pytest.mark.regra("V1-4.3.4", "V1-4.3.4a", "V1-4.3.13")
def test_cada_um_testa_na_sua_vez_ate_usar_as_tres_cartas(motor: MotorV1) -> None:
    bots = [criar_bot("construtor", EXPERIENTE, "v1") for _ in range(4)]
    eventos: list[Any] = []
    jogar_partida(motor, bots, 3, 3, ouvinte=lambda ev, d: eventos.append(ev), conferir_invariantes=True)
    atacantes = [ev.publico["atacante"] for ev in eventos if ev.tipo == "teste"]
    assert atacantes == [0, 1, 2, 3] * 3
    assert tipos(eventos).count("fim_da_rodada") == 1


@pytest.mark.regra("V1-4.3.5")
def test_testa_qualquer_adversario_com_qualquer_carta_da_mao(motor: MotorV1) -> None:
    estado = montar_v1(motor, sistemas=[[LOAD], [], [COEXISTENCE], [AB]], maos=[[RECOVERY, CF], [], [], []])
    opcoes = [acao.texto() for acao in motor.acoes_legais(estado)]
    assert opcoes == [f"testar:{RECOVERY}:{alvo}" for alvo in (1, 2, 3)] + [f"testar:{CF}:{alvo}" for alvo in (1, 2, 3)]
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, ataque(RECOVERY, 0))
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, ataque(LOAD, 1))


@pytest.mark.regra("V1-4.3.6")
def test_declarar_que_nao_tem_e_falha_encontrada(motor: MotorV1) -> None:
    estado = montar_v1(motor, sistemas=[[LOAD], [COEXISTENCE], [], []], maos=[[RECOVERY], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(RECOVERY, 1), NAO_TEM)
    assert "falha_encontrada" in tipos(eventos)
    # O atacante tira a carta do sistema do defensor; a carta de ataque vai para o descarte (AMB-23).
    assert nomes(motor, estado.jogadores[0].sistema) == [LOAD, COEXISTENCE]
    assert estado.jogadores[1].sistema == ()
    assert nomes(motor, estado.descarte) == [RECOVERY]
    tomada = next(ev for ev in eventos if ev.tipo == "carta_tomada")
    assert tomada.oculto == {"carta": COEXISTENCE} and tomada.visivel_para == {"carta": [0, 1]}


@pytest.mark.regra("V1-4.3.7", "V1-4.3.8", "V1-4.3.10a")
def test_declaracao_aceita_e_defesa_bem_sucedida(motor: MotorV1) -> None:
    estado = montar_v1(motor, sistemas=[[], [RECOVERY], [], []], maos=[[LOAD], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(LOAD, 1))
    assert estado.pendente == Pendente(E.DECLARAR, 1)
    assert motor.acoes_legais(estado) == (AcaoV1(A.DECLARAR, tem=True), AcaoV1(A.DECLARAR, tem=False))
    estado, eventos = jogar(motor, estado, TEM)
    declaracao = next(ev for ev in eventos if ev.tipo == "declaracao")
    assert declaracao.publico == {"tem": True}
    assert declaracao.oculto == {"tem_a_cor": False, "blefe": True}
    assert estado.pendente == Pendente(E.DUVIDAR, 0)
    estado, eventos = jogar(motor, estado, ACEITAR)
    # AMB-20: vale a declaração. Mesmo blefando, o defensor fica com a carta de ataque.
    assert nomes(motor, estado.jogadores[1].sistema) == [RECOVERY, LOAD]
    assert estado.descarte == () and estado.jogadores[0].sistema == ()


@pytest.mark.regra("V1-4.3.10a")
def test_blefe_aceito_pela_verdade_se_a_configuracao_pedir() -> None:
    dados = ler_yaml(REGRAS_V1)
    dados["interpretacoes"]["blefe_aceito"]["valor"] = "verdade"
    motor = MotorV1(ler_regras_v1(dados))
    estado = montar_v1(motor, sistemas=[[], [RECOVERY], [], []], maos=[[LOAD], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(LOAD, 1), TEM, ACEITAR)
    assert "falha_encontrada" in tipos(eventos)
    assert nomes(motor, estado.jogadores[0].sistema) == [RECOVERY]


@pytest.mark.regra("V1-4.3.9", "V1-4.3.10")
def test_duvida_pede_a_definicao_e_o_atacante_decide(motor: MotorV1) -> None:
    estado = montar_v1(motor, sistemas=[[], [STRESS], [], []], maos=[[LOAD], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(LOAD, 1), TEM)
    assert motor.acoes_legais(estado) == (ACEITAR, DUVIDAR)
    estado, eventos = jogar(motor, estado, DUVIDAR)
    assert tipos(eventos) == ["duvida", "definicao"]
    definicao = eventos[1]
    assert definicao.oculto == {"explicacao_correta": True} and definicao.visivel_para == {"explicacao_correta": [1]}
    assert estado.pendente == Pendente(E.CONTESTAR, 0)
    assert motor.acoes_legais(estado) == (ACEITAR, CONTESTAR)
    estado, _ = jogar(motor, estado, ACEITAR)
    assert nomes(motor, estado.jogadores[1].sistema) == [STRESS, LOAD]


@pytest.mark.regra("V1-4.3.10b", "V1-4.3.11")
def test_contestou_e_era_verdade(motor: MotorV1) -> None:
    estado = montar_v1(motor, sistemas=[[AUTHENTICATION], [STRESS], [], []], maos=[[LOAD], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(LOAD, 1), TEM, DUVIDAR, CONTESTAR)
    contestacao = next(ev for ev in eventos if ev.tipo == "contestacao")
    assert contestacao.publico == {"tinha_a_cor": True, "carta_revelada": STRESS}
    # Defesa bem-sucedida (fica com a carta de ataque) e, de punição, tira uma carta do atacante.
    assert sorted(nomes(motor, estado.jogadores[1].sistema)) == sorted([STRESS, LOAD, AUTHENTICATION])
    assert estado.jogadores[0].sistema == () and estado.descarte == ()
    assert estado.historico[-1].resultado == E.CONTESTOU_VERDADE


@pytest.mark.regra("V1-4.3.12")
def test_contestou_e_era_blefe(motor: MotorV1) -> None:
    estado = montar_v1(motor, sistemas=[[], [RECOVERY, AB, COEXISTENCE], [], []], maos=[[LOAD], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(LOAD, 1), TEM, DUVIDAR, CONTESTAR)
    assert next(ev for ev in eventos if ev.tipo == "contestacao").publico == {"tinha_a_cor": False}
    # Falha encontrada mais a recompensa: duas cartas tiradas do defensor; a carta de ataque é descartada.
    assert len(estado.jogadores[0].sistema) == 2 and len(estado.jogadores[1].sistema) == 1
    assert [ev.tipo for ev in eventos].count("carta_tomada") == 2
    assert nomes(motor, estado.descarte) == [LOAD]


@pytest.mark.regra("V1-4.2.3")
def test_critical_failure_e_falha_automatica(motor: MotorV1) -> None:
    estado = montar_v1(motor, sistemas=[[], [STRESS], [], []], maos=[[CF], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(CF, 1))
    assert "falha_automatica" in tipos(eventos) and "declaracao" not in tipos(eventos)
    assert nomes(motor, estado.jogadores[0].sistema) == [STRESS]
    assert nomes(motor, estado.descarte) == [CF]


def test_alvo_com_sistema_vazio(motor: MotorV1) -> None:
    """AMB-25: pode ser alvo; a falha não tira nada, e a carta de ataque é gasta."""
    estado = montar_v1(motor, sistemas=[[LOAD], [], [], []], maos=[[RECOVERY], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(RECOVERY, 1), NAO_TEM)
    assert next(ev for ev in eventos if ev.tipo == "nada_a_tomar").amb == "AMB-25"
    assert nomes(motor, estado.descarte) == [RECOVERY] and nomes(motor, estado.jogadores[0].sistema) == [LOAD]


# ---------------------------------------------------------------- pontuação


@pytest.mark.regra("V1-4.3.15", "V1-4.3.16", "V1-4.3.17", "V1-4.3.18")
@pytest.mark.parametrize(
    "sistema, pontos, pares, trios",
    [
        ([], 0, 0, 0),
        ([LOAD], 1, 0, 0),
        ([LOAD, LOAD], 2, 0, 0),  # mesmo teste não forma par
        ([LOAD, STRESS], 4, 1, 0),
        ([LOAD, STRESS_USABILIDADE], 2, 0, 0),  # atributos diferentes, sem terceira carta
        ([LOAD, RECOVERY, AUTHENTICATION], 5, 0, 1),
        # AMB-24: cada carta numa combinação só, na melhor divisão.
        ([LOAD, STRESS, RECOVERY, AUTHENTICATION], 6, 1, 0),
        # V1-4.3.18: mais de um par do mesmo atributo.
        ([LOAD, LOAD, STRESS, SCALABILITY], 8, 2, 0),
        ([LOAD, STRESS, RECOVERY, AUTHENTICATION, COEXISTENCE], 9, 1, 1),
    ],
)
def test_pontuacao_pela_melhor_divisao(motor: MotorV1, sistema: list[str], pontos: int, pares: int, trios: int) -> None:
    resultado = pontuar([(motor.catalogo.atributo[nome], nome) for nome in sistema], motor.tabela)
    assert (resultado.total, resultado.pares, resultado.trios) == (pontos, pares, trios)


@pytest.mark.regra("V1-4.3.14", "V1-4.3.19")
def test_revelacao_pontuacao_e_vencedor(motor: MotorV1) -> None:
    sistemas = [[LOAD, STRESS], [RECOVERY, AUTHENTICATION, COEXISTENCE, ADAPTABILITY], [AB], [LOAD, LOAD]]
    estado = montar_v1(motor, sistemas=sistemas, maos=[[RECOVERY], [], [], []])
    estado, eventos = jogar(motor, estado, ataque(RECOVERY, 2), NAO_TEM)
    finais = {ev.ator: ev.publico for ev in eventos if ev.tipo == "pontuacao_final"}
    # Ana: Load, Stress e a A/B que tirou de Carla: um par e uma carta solta, 5 pontos.
    # Bruno: quatro atributos diferentes: um trio e uma carta solta, 6 pontos.
    assert finais[0]["pontos"] == 5 and finais[1]["pontos"] == 6 and finais[1]["trios"] == 1
    fim = next(ev for ev in eventos if ev.tipo == "fim_de_jogo")
    assert fim.publico["vencedores"] == [1] and fim.publico["criterio"] == "pontos"
    assert estado.fase == E.FIM and all(set(j.reveladas) == set(j.sistema) for j in estado.jogadores)


def test_empate_divide_a_vitoria(motor: MotorV1) -> None:
    """AMB-29."""
    estado = montar_v1(motor, sistemas=[[LOAD], [AB], [], []], maos=[[], [], [], [RECOVERY]], vez=3)
    estado, eventos = jogar(motor, estado, ataque(RECOVERY, 2), NAO_TEM)
    fim = next(ev for ev in eventos if ev.tipo == "fim_de_jogo")
    assert fim.publico["vencedores"] == [0, 1] and fim.publico["criterio"] == "dividida" and fim.amb == "AMB-29"


# ---------------------------------------------------------------- registro, replay e observação


def test_registro_da_v1_refeito_nos_dois_modos(motor: MotorV1) -> None:
    bots = [
        criar_bot(t, p, "v1")
        for t, p in [
            ("aleatorio", {}),
            ("construtor", EXPERIENTE),
            ("cacador", {**EXPERIENTE, "alvo": "lider"}),
            ("heuristico", EXPERIENTE),
        ]
    ]
    linhas, resultado = registro.gerar_linhas(motor, "configs/regras_v1.yaml", bots, 4, 2, "2026-11-10T00:00:00+00:00")
    assert linhas[0]["regras"]["familia"] == "v1" and linhas[-1]["placar"]["final"] == list(resultado.placar)
    assert linhas[-1]["duracao_estimada_s"] is None
    for modo in replay.MODOS:
        assert replay.refazer(linhas, modo).eventos == len(linhas) - 2
    texto = narrar(linhas, motor.catalogo)
    assert "== Rodada 3 de testes ==" in texto and "Placar final:" in texto
    with pytest.raises(ConfiguracaoInvalida):
        from critical_failure.auditoria import folha

        folha.extrair(linhas)


def test_acao_da_v1_vinda_do_registro() -> None:
    acao = AcaoV1(A.MONTAR, cartas=(LOAD, AB, CF))
    assert acao_v1_de_dict(acao.para_dict()) == acao
    for ruim in ({"tipo": "voar"}, {"tipo": "testar", "alvo": "x"}, {"tipo": "declarar", "tem": "sim"}, [], None):
        with pytest.raises(AcaoIlegal):
            acao_v1_de_dict(ruim)


def test_a_observacao_esconde_maos_e_sistemas_dos_outros(motor: MotorV1) -> None:
    estado = montar_v1(motor, sistemas=[[LOAD], [AUTHENTICATION], [], []], maos=[[RECOVERY], [AB], [], []])
    ana = motor.observar(estado, 0)
    assert ana.mao == (RECOVERY,) and ana.sistema == (LOAD,)
    texto = repr(ana)
    assert AUTHENTICATION not in texto and AB not in texto
    assert ana.jogadores[1].cartas_no_sistema == 1 and ana.jogadores[1].cartas_na_mao == 1


def test_carta_recebida_numa_defesa_fica_conhecida_ate_uma_retirada(motor: MotorV1) -> None:
    estado = montar_v1(
        motor, sistemas=[[], [RECOVERY], [], [AB]], maos=[[LOAD, ADAPTABILITY], [], [], [STRESS_USABILIDADE]]
    )
    estado, _ = jogar(motor, estado, ataque(LOAD, 1), TEM, ACEITAR)
    assert motor.observar(estado, 2).jogadores[1].reveladas == (LOAD,)
    estado = replace(estado, vez=3, pendente=Pendente(E.TESTAR, 3))
    estado, _ = jogar(motor, estado, ataque(STRESS_USABILIDADE, 1), NAO_TEM)
    # Depois de uma carta tirada ao acaso, a mesa não sabe mais o que ficou.
    assert motor.observar(estado, 2).jogadores[1].reveladas == ()


def test_ponto_de_corte_quando_todos_fizeram_o_primeiro_teste(motor: MotorV1) -> None:
    bots = [criar_bot("cacador", {**EXPERIENTE, "alvo": "mais_fraco"}, "v1") for _ in range(5)]
    eventos: list[Any] = []
    resultado = jogar_partida(motor, bots, 8, 1, ouvinte=lambda ev, d: eventos.append(ev))
    indice = next(
        i
        for i, ev in enumerate(eventos)
        if ev.tipo == "fim_da_disputa" and [j.testes_feitos for j in ev.estado.jogadores] == [1] * 5
    )
    esperado = tuple(len(j.sistema) for j in eventos[indice].estado.jogadores)
    assert resultado.placar_no_corte == esperado


# ---------------------------------------------------------------- bots da v1


def _jogos_gravados(motor: MotorV1, parametros: dict[str, Any], partidas: int) -> list[tuple[Any, Any, Any]]:
    from test_bots import Gravador

    registros: list[tuple[Any, Any, Any]] = []
    for partida in range(partidas):
        bots = [
            Gravador(criar_bot(estilo, {**parametros, **extra}, "v1"))
            for estilo, extra in [
                ("construtor", {}),
                ("cacador", {"alvo": "lider"}),
                ("heuristico", {}),
                ("cacador", {"alvo": "mais_fraco"}),
            ]
        ]
        jogar_partida(motor, bots, 6, partida, conferir_invariantes=True)
        for gravador in bots:
            registros += gravador.decisoes
    return registros


@pytest.mark.parametrize("blefe", ["nunca", "sempre"])
def test_bots_da_v1_declaram_conforme_o_perfil(motor: MotorV1, blefe: str) -> None:
    declaracoes = 0
    for obs, _, decisao in _jogos_gravados(motor, {**EXPERIENTE, "blefe": blefe}, 8):
        if obs.decisao_pedida != E.DECLARAR:
            continue
        declaracoes += 1
        tem = any(motor.catalogo.atributo[nome] == obs.disputa.atributo for nome in obs.sistema)
        if tem:
            assert decisao.acao.tem is True
        else:
            assert decisao.acao.tem is (blefe == "sempre")
    assert declaracoes > 10


def test_bots_da_v1_montam_o_sistema_que_mais_pontua(motor: MotorV1) -> None:
    for obs, opcoes, decisao in _jogos_gravados(motor, EXPERIENTE, 3):
        if obs.decisao_pedida != E.MONTAR:
            continue

        def pontos(acao: AcaoV1) -> int:
            return pontuar([(motor.catalogo.atributo[n], n) for n in acao.cartas], motor.tabela).total

        assert pontos(decisao.acao) == max(pontos(acao) for acao in opcoes)


@pytest.mark.parametrize("politica, extremo", [("lider", max), ("mais_fraco", min)])
def test_cacador_da_v1_escolhe_o_alvo_pelo_tamanho_do_sistema(motor: MotorV1, politica: str, extremo: Any) -> None:
    from test_bots import Gravador

    testes = 0
    for partida in range(5):
        bots = [Gravador(criar_bot("cacador", {**EXPERIENTE, "alvo": politica}, "v1")) for _ in range(5)]
        jogar_partida(motor, bots, 12, partida)
        for gravador in bots:
            for obs, opcoes, decisao in gravador.decisoes:
                if obs.decisao_pedida != E.TESTAR:
                    continue
                testes += 1
                tamanhos = [obs.jogadores[a].cartas_no_sistema for a in {o.alvo for o in opcoes}]
                assert obs.jogadores[decisao.acao.alvo].cartas_no_sistema == extremo(tamanhos)
    assert testes == 5 * 5 * 3


def test_v1_e_v2_usam_bots_diferentes_com_o_mesmo_nome() -> None:
    v1, v2 = criar_bot("construtor", EXPERIENTE, "v1"), criar_bot("construtor", EXPERIENTE, "v2")
    assert v1.tipo == v2.tipo == "construtor" and type(v1) is not type(v2)
    assert v1.parametros() == v2.parametros()
    with pytest.raises(ConfiguracaoInvalida):
        criar_bot("construtor", EXPERIENTE, "v9")
    with pytest.raises(ValueError):
        criar_bot("construtor", EXPERIENTE, "v1").iniciar(1, 0, 0, mesa_para(criar_motor()))


# ---------------------------------------------------------------- propriedades


@settings(max_examples=40, deadline=None)
@given(
    semente=st.integers(0, 2**32 - 1),
    partida=st.integers(0, 10**6),
    estilos=st.lists(st.sampled_from(["construtor", "cacador", "heuristico", "aleatorio"]), min_size=3, max_size=8),
    blefe=st.sampled_from(["nunca", "metade", "sempre"]),
    contestacao=st.sampled_from(["nunca", "sempre", "limiar"]),
)
def test_qualquer_partida_da_v1_respeita_os_invariantes(
    motor: MotorV1, semente: int, partida: int, estilos: list[str], blefe: str, contestacao: str
) -> None:
    def novo(estilo: str) -> Any:
        if estilo == "aleatorio":
            return criar_bot("aleatorio", {}, "v1")
        extra = {"alvo": "aleatorio"} if estilo == "cacador" else {}
        return criar_bot(estilo, {**EXPERIENTE, "blefe": blefe, "contestacao": contestacao, **extra}, "v1")

    primeira = jogar_partida(motor, [novo(e) for e in estilos], semente, partida, conferir_invariantes=True)
    final = primeira.estado_final
    em_jogo = [*final.baralho, *final.descarte]
    for jogador in final.jogadores:
        em_jogo += [*jogador.mao, *jogador.sistema]
        assert jogador.mao == () and jogador.testes_feitos == 3
    assert sorted(em_jogo) == list(range(54))
    assert primeira.vezes("teste") == 3 * len(estilos)
    assert jogar_partida(motor, [novo(e) for e in estilos], semente, partida) == primeira


# ---------------------------------------------------------------- conta direta contra busca exaustiva


def _por_busca(cartas: tuple[tuple[str, str], ...], tabela: Any) -> tuple[int, int, int]:
    """Oráculo: tenta todas as divisões (o cálculo antigo, por busca). (bônus, pares, trios)."""
    from itertools import combinations

    if not cartas:
        return (0, 0, 0)
    primeira, outras = cartas[0], cartas[1:]
    opcoes = [_por_busca(outras, tabela)]
    for tamanho, e_par, bonus_do_grupo in (
        (tabela.cartas_no_par, True, tabela.por_par),
        (tabela.cartas_no_trio, False, tabela.por_trio),
    ):
        for indices in combinations(range(len(outras)), tamanho - 1):
            grupo = (primeira, *(outras[i] for i in indices))
            atributos = {atributo for atributo, _ in grupo}
            valido = (len(atributos) == 1 and len(set(grupo)) == len(grupo)) if e_par else len(atributos) == len(grupo)
            if valido:
                sobra = tuple(carta for k, carta in enumerate(outras) if k not in indices)
                bonus, pares, trios = _por_busca(sobra, tabela)
                opcoes.append((bonus + bonus_do_grupo, pares + e_par, trios + (not e_par)))
    return max(opcoes)


@settings(max_examples=300, deadline=None)
@given(
    cartas=st.lists(
        st.tuples(st.sampled_from(["A", "B", "C", "D", "E"]), st.sampled_from(["x", "y", "z"])), max_size=9
    ),
    por_par=st.integers(0, 4),
    por_trio=st.integers(0, 4),
)
def test_conta_direta_igual_a_busca_exaustiva(cartas: list[tuple[str, str]], por_par: int, por_trio: int) -> None:
    from critical_failure.regras.v1.pontuacao import TabelaDePontos

    tabela = TabelaDePontos(por_carta=1, por_par=por_par, por_trio=por_trio, cartas_no_par=2, cartas_no_trio=3)
    direto = pontuar(cartas, tabela)
    bonus, pares, trios = _por_busca(tuple(sorted(cartas)), tabela)
    assert direto.total == len(cartas) + bonus
    assert (direto.pares, direto.trios) == (pares, trios)


def test_pontuacao_de_sistema_grande_e_rapida(motor: MotorV1) -> None:
    """A busca antiga explodia com sistemas grandes; a conta direta não."""
    import time

    nomes_v1 = sorted(set(motor.catalogo.cartas) - motor.catalogo.especiais)
    sistema = [(motor.catalogo.atributo[nome], nome) for nome in (nomes_v1 * 3)[:40]]
    inicio = time.perf_counter()
    resultado = pontuar(sistema, motor.tabela)
    assert time.perf_counter() - inicio < 1.0
    assert resultado.cartas == 40 and resultado.total > 40

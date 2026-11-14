"""Variantes de playtest (VAR-02 a VAR-06) e o coletor de medidas por partida."""

from __future__ import annotations

import copy
from collections import Counter
from dataclasses import replace
from typing import Any

import pytest
import yaml
from conftest import RAIZ

from critical_failure.bots.fabrica import criar_bot
from critical_failure.experimentos.config import aplicar_mudancas
from critical_failure.nucleo.canonico import como_dict
from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.partida import jogar_partida
from critical_failure.regras.familias import motor_de
from critical_failure.regras.v2.estado import Disputa
from critical_failure.regras.v2.motor import MotorV2

BLOCO = {
    "custo_extra_da_explicacao": {"valor": 0, "regra": "VAR-02"},
    "auditor_externo": {"valor": False, "regra": "VAR-03"},
    "auditor_externo_acertos": {"valor": 95, "regra": "MOD-02"},
    "auditor_externo_julgamentos": {"valor": 100, "regra": "MOD-02"},
    "vizinhos_designados": {"valor": [], "regra": "VAR-04"},
    "limite_de_testes_recebidos": {"valor": 0, "regra": "VAR-05"},
    "palpite_da_plateia": {"valor": False, "regra": "VAR-06"},
    "premio_do_palpite": {"valor": 1, "regra": "VAR-06"},
}
PERFIL = {"conhecimento": "iniciante", "blefe": "metade", "contestacao": "limiar"}


def regras_base() -> dict[str, Any]:
    dados: dict[str, Any] = yaml.safe_load((RAIZ / "configs" / "regras_v2_2_1.yaml").read_text(encoding="utf-8"))
    return dados


def motor_com(**troca: Any) -> MotorV2:
    bloco = copy.deepcopy(BLOCO)
    for chave, valor in troca.items():
        bloco[chave]["valor"] = valor
    motor = motor_de(aplicar_mudancas(regras_base(), {"variantes": bloco}), RAIZ / "configs")
    assert isinstance(motor, MotorV2)
    return motor


class Gravador:
    """Ouvinte que guarda os eventos e as decisões dos bots."""

    def __init__(self) -> None:
        self.eventos: list[Any] = []
        self.decisoes: list[dict[str, Any]] = []

    def __call__(self, evento: Any, decisao: dict[str, Any] | None) -> None:
        self.eventos.append(evento)
        if decisao is not None:
            self.decisoes.append(decisao)


def jogar_gravando(motor: MotorV2, partidas: int = 12, n: int = 4) -> list[Gravador]:
    """Partidas com Heurísticos iniciantes e um Aleatório, invariantes conferidos."""
    todas = []
    for partida in range(partidas):
        gravador = Gravador()
        bots = [criar_bot("heuristico", PERFIL) for _ in range(n - 1)] + [criar_bot("aleatorio", {})]
        jogar_partida(motor, bots, 7, partida, ouvinte=gravador, conferir_invariantes=True)
        todas.append(gravador)
    return todas


def jogar(motor: MotorV2, partidas: int = 12, n: int = 4) -> list[list[Any]]:
    return [gravador.eventos for gravador in jogar_gravando(motor, partidas, n)]


# ---------------------------------------------------------------- configuração


def test_sem_bloco_de_variantes_o_hash_das_regras_nao_muda() -> None:
    motor = motor_de(regras_base(), RAIZ / "configs")
    assert "variantes" not in motor.regras.resolvida()
    com_bloco = motor_com()
    assert com_bloco.regras.resolvida()["variantes"]["palpite_da_plateia"]["valor"] is False
    assert com_bloco.regras.hash() != motor.regras.hash()


def test_variantes_incoerentes_sao_recusadas() -> None:
    with pytest.raises(ConfiguracaoInvalida):
        motor_com(auditor_externo_acertos=101)
    with pytest.raises(ConfiguracaoInvalida):
        motor_com(auditor_externo=True, palpite_da_plateia=True)
    with pytest.raises(ConfiguracaoInvalida):
        motor_com(vizinhos_designados=["acima"])


def test_campo_de_variante_fica_fora_do_hash_enquanto_vazio() -> None:
    disputa = Disputa(0, 1, 2, 5, "Desempenho", "contestar")
    assert "palpites" not in como_dict(disputa)
    assert como_dict(Disputa(0, 1, 2, 5, "Desempenho", "contestar", palpites=((3, True),)))["palpites"] == ((3, True),)


# ---------------------------------------------------------------- variantes


def test_var02_custo_extra_da_explicacao() -> None:
    custos = 0
    for eventos in jogar(motor_com(custo_extra_da_explicacao=1)):
        for anterior, evento in zip(eventos, eventos[1:], strict=False):
            if evento.tipo == "custo_da_explicacao":
                custos += 1
                assert anterior.tipo == "conferencia" and anterior.publico["veredito"] == "nao_confere"
                defensor = evento.ator
                perdeu = anterior.estado.jogadores[defensor].fichas - evento.estado.jogadores[defensor].fichas
                assert perdeu == -evento.publico["fichas"][str(defensor)] in (0, 1)
    assert custos > 0


def test_var03_auditor_externo_julga_sem_jogador() -> None:
    conferencias = 0
    for gravador in jogar_gravando(motor_com(auditor_externo=True, auditor_externo_acertos=100)):
        # Nenhum bot é chamado a julgar: o motor resolve a conferência no mesmo passo da defesa.
        assert not any(d["acao"]["tipo"] in ("confere", "nao_confere") for d in gravador.decisoes)
        explicacao = None
        for evento in gravador.eventos:
            if evento.tipo == "defesa" and "explicacao_correta" in evento.oculto:
                explicacao = evento.oculto["explicacao_correta"]
                assert evento.visivel_para["explicacao_correta"] == []
            if evento.tipo == "conferencia":
                conferencias += 1
                assert evento.ator is None and evento.regra == "VAR-03"
                # Com 100 acertos em 100, o veredito segue a explicação.
                assert evento.publico["veredito"] == ("confere" if explicacao else "nao_confere")
    assert conferencias > 0


def test_var04_vizinho_designado() -> None:
    testes = 0
    for eventos in jogar(motor_com(vizinhos_designados=["esquerda", "direita", "esquerda"]), n=5):
        for evento in eventos:
            if evento.tipo == "teste":
                testes += 1
                atacante, defensor = evento.publico["atacante"], evento.publico["defensor"]
                esperado = (atacante + 1) % 5 if evento.ciclo in (1, 3) else (atacante - 1) % 5
                assert defensor == esperado
    assert testes > 0


def test_var05_limite_de_testes_recebidos() -> None:
    maximo = 0
    for eventos in jogar(motor_com(limite_de_testes_recebidos=2)):
        por_ciclo = Counter((e.ciclo, e.publico["defensor"]) for e in eventos if e.tipo == "teste")
        maximo = max(maximo, *por_ciclo.values())
    assert maximo == 2


def test_var06_palpite_da_plateia() -> None:
    premios = 0
    for eventos in jogar(motor_com(palpite_da_plateia=True), n=5):
        votos: dict[int, bool] = {}
        for evento in eventos:
            e = evento.estado
            if evento.tipo == "palpite":
                d = e.disputa
                assert evento.ator not in (d.atacante, d.defensor, d.auditor)  # AMB-30
                assert evento.publico == {} and evento.visivel_para == {"blefe": [evento.ator]}
                votos[evento.ator] = evento.oculto["blefe"]
            if evento.tipo == "palpites_revelados":
                assert len(votos) == 2  # com 5 jogadores, votam 2
                assert e.pendente is not None and e.pendente.tipo == "contestar"
            if evento.tipo == "contestacao":
                era_blefe = not evento.publico["tinha_carta"]
                certos = {str(v) for v, b in votos.items() if b == era_blefe}
            if evento.tipo == "premio_do_palpite":
                premios += 1
                assert set(evento.publico["fichas"]) == certos and evento.amb == "AMB-31"
            if evento.tipo == "fim_da_disputa":
                votos = {}
    assert premios > 0


# ---------------------------------------------------------------- coletor de medidas


def test_coletor_confere_com_os_eventos() -> None:
    from critical_failure.duracao import Cronometro, carregar_duracao

    motor = motor_de(regras_base(), RAIZ / "configs")
    assert isinstance(motor, MotorV2)
    modelo = carregar_duracao(RAIZ / "configs" / "duracao.yaml")
    cronometro = Cronometro(modelo)
    for partida in range(6):
        gravador = Gravador()
        eventos = gravador.eventos
        bots = [criar_bot("heuristico", PERFIL) for _ in range(4)]
        resultado = jogar_partida(motor, bots, 3, partida, ouvinte=gravador, duracao=modelo)
        medidas = resultado.medidas
        recebidos = Counter(e.publico["defensor"] for e in eventos if e.tipo == "teste")
        assert medidas["testes_recebidos"] == [recebidos[k] for k in range(4)]
        assert sum(medidas["testes_recebidos"]) == resultado.vezes("teste")
        # Ninguém fica parado mais que o tempo inteiro do ciclo, e na Produção ninguém fica parado.
        for ciclo in (1, 2, 3):
            total = sum(
                cronometro.tempo(e)
                for e in eventos
                if e.ciclo == ciclo and e.fase != "producao" and e.fase in ("planejamento", "homologacao")
            )
            parados = medidas["parado_s"][(ciclo - 1) * 4 : ciclo * 4]
            assert all(0 <= p <= total for p in parados) and sum(parados) > 0
        inicio = next(e for e in eventos if e.tipo == "inicio_da_fase" and e.publico["fase"] == "planejamento")
        chave = motor.incidente_atual(inicio.estado).chave
        cobre = [any(motor.catalogo.categoria(c) == chave for c in j.sistema) for j in inicio.estado.jogadores]
        assert medidas["cobre_incidente_1"] == cobre
        dano = sum(abs(v) for e in eventos if e.publico.get("fonte") == "dano" for v in e.publico["fichas"].values())
        assert medidas["fichas_de_dano"] == dano <= medidas["fichas_movimentadas"]
        acertos = [e for e in eventos if e.tipo == "diagnostico_pontuado" and e.publico.get("fichas")]
        diagnostico = sum(v for e in acertos for v in e.publico["fichas"].values())
        assert medidas["fichas_de_diagnostico"] == diagnostico > 0
        assert dano + diagnostico <= medidas["fichas_movimentadas"]


# ---------------------------------------------------------------- ablações (Experimento 3) e tempos por cenário


def motor_com_ablacao(bug: bool = False, testes: int = 0) -> MotorV2:
    bloco = {
        "bug_duplicado_permitido": {"valor": bug, "regra": "VAR-10"},
        "testes_por_ciclo": {"valor": testes, "regra": "VAR-11"},
    }
    motor = motor_de(aplicar_mudancas(regras_base(), {"ablacoes": bloco}), RAIZ / "configs")
    assert isinstance(motor, MotorV2)
    return motor


def ataques_em_categoria_com_alerta(eventos: list[Any]) -> int:
    return sum(
        1
        for e in eventos
        if e.tipo == "teste" and e.publico["categoria"] in e.estado.jogadores[e.publico["defensor"]].alertas
    )


def test_var10_bug_duplicado_permitido() -> None:
    base = motor_de(regras_base(), RAIZ / "configs")
    assert isinstance(base, MotorV2)
    assert sum(ataques_em_categoria_com_alerta(eventos) for eventos in jogar(base)) == 0
    com_ablacao = jogar(motor_com_ablacao(bug=True), partidas=20)
    assert sum(ataques_em_categoria_com_alerta(eventos) for eventos in com_ablacao) > 0
    # O cubo não se repete: no máximo 1 Alerta por categoria (os invariantes já conferem a cada evento).
    assert "ablacoes" in motor_com_ablacao(bug=True).regras.resolvida()
    assert "ablacoes" not in base.regras.resolvida()


def test_var11_um_teste_por_ciclo() -> None:
    for eventos in jogar(motor_com_ablacao(testes=1), n=5):
        por_atacante = Counter((e.ciclo, e.publico["atacante"]) for e in eventos if e.tipo == "teste")
        assert por_atacante and max(por_atacante.values()) == 1


def test_var11_dois_testes_por_ciclo() -> None:
    """Experimento 7: o meio-termo de 2 testes por ciclo usa o mesmo parâmetro do VAR-11."""
    maximos = []
    for eventos in jogar(motor_com_ablacao(testes=2), n=5):
        por_atacante = Counter((e.ciclo, e.publico["atacante"]) for e in eventos if e.tipo == "teste")
        maximos.append(max(por_atacante.values()))
    assert max(maximos) == 2


# ---------------------------------------------------------------- VAR-12: custo do teste (proposta)


def motor_com_custo(custo: int = 1, a_partir_do: int = 2) -> MotorV2:
    bloco = {
        "custo_do_teste": {"valor": custo, "regra": "VAR-12"},
        "teste_pago_a_partir_do": {"valor": a_partir_do, "regra": "VAR-12"},
    }
    motor = motor_de(aplicar_mudancas(regras_base(), {"propostas": bloco}), RAIZ / "configs")
    assert isinstance(motor, MotorV2)
    return motor


def test_var12_do_segundo_teste_do_ciclo_em_diante_cada_teste_custa_1_ficha() -> None:
    pagos = gratis = 0
    for eventos in jogar(motor_com_custo(), partidas=12, n=4):
        feitos: Counter[tuple[int, int]] = Counter()
        for posicao, evento in enumerate(eventos):
            if evento.tipo != "teste":
                continue
            atacante = evento.publico["atacante"]
            feitos[(evento.ciclo, atacante)] += 1
            seguinte = eventos[posicao + 1]
            if feitos[(evento.ciclo, atacante)] >= 2:
                assert seguinte.tipo == "custo_do_teste" and seguinte.regra == "VAR-12" and seguinte.amb == "AMB-32"
                assert seguinte.publico["fichas"] == {str(atacante): -1}
                assert seguinte.estado.jogadores[atacante].fichas == evento.estado.jogadores[atacante].fichas - 1
                pagos += 1
            else:
                assert seguinte.tipo != "custo_do_teste"
                gratis += 1
    assert pagos and gratis


def test_var12_sem_ficha_para_pagar_nao_faz_o_teste_pago() -> None:
    """AMB-32 (autor, 2026-11-11): com 0 ficha, só o teste de graça do ciclo é possível."""
    motor = motor_com_custo()
    conferidos = 0
    for eventos in jogar(motor, partidas=6, n=4):
        for evento in eventos:
            e = evento.estado
            if e.pendente is None or e.pendente.tipo != "agir":
                continue
            j = e.pendente.jogador
            if not any(d.ciclo == e.ciclo and d.atacante == j for d in e.historico):
                continue
            com_ficha = replace(
                e, jogadores=tuple(replace(x, fichas=1) if k == j else x for k, x in enumerate(e.jogadores))
            )
            sem_ficha = replace(
                e, jogadores=tuple(replace(x, fichas=0) if k == j else x for k, x in enumerate(e.jogadores))
            )
            testes_com = [a for a in motor.acoes_legais(com_ficha) if a.tipo == "testar"]
            testes_sem = [a for a in motor.acoes_legais(sem_ficha) if a.tipo == "testar"]
            assert testes_sem == []
            conferidos += bool(testes_com)
    assert conferidos


def test_var12_configuracao() -> None:
    base = motor_de(regras_base(), RAIZ / "configs")
    assert "propostas" not in base.regras.resolvida()
    assert motor_com_custo().regras.resolvida()["propostas"]["custo_do_teste"]["valor"] == 1
    with pytest.raises(ConfiguracaoInvalida, match="teste_pago_a_partir_do"):
        motor_com_custo(custo=1, a_partir_do=0)
    # Sem custo, o bloco não muda o jogo.
    sem_custo = motor_com_custo(custo=0)
    assert [len(eventos) for eventos in jogar(sem_custo, partidas=3)] == [
        len(eventos) for eventos in jogar(base, partidas=3)
    ]


def test_modelo_de_duracao_por_cenario(tmp_path: Any) -> None:
    from critical_failure.experimentos import executor
    from critical_failure.experimentos.config import ler_experimento

    def cenario(nome: str, **extra: Any) -> dict[str, Any]:
        bots = [{"tipo": "heuristico", "parametros": PERFIL}]
        return {
            "nome": nome,
            "regras": "configs/regras_v2_2_1.yaml",
            "jogadores": 4,
            "partidas": 4,
            "bots": bots,
            **extra,
        }

    dados = {
        "esquema": "cf-experimento/1",
        "nome": "tempos",
        "descricao": "Tempos por cenário.",
        "semente_mestre": 5,
        "duracao": "configs/duracao.yaml",
        "registros_completos_um_a_cada": 100,
        "cenarios": [cenario("normal"), cenario("lento", duracao="configs/duracao_mais_25.yaml")],
    }
    arquivo = tmp_path / "tempos.yaml"
    arquivo.write_text(yaml.safe_dump(dados), encoding="utf-8")
    execucao = executor.executar(ler_experimento(dados), arquivo, saida=tmp_path / "saida")
    normal = [linha for linha in execucao.linhas if linha["cenario"] == "normal"]
    lento = [linha for linha in execucao.linhas if linha["cenario"] == "lento"]
    # Os tempos não mudam o jogo, só a medida.
    assert [linha["placar"] for linha in normal] == [linha["placar"] for linha in lento]
    assert all(b["duracao_s"] > a["duracao_s"] for a, b in zip(normal, lento, strict=True))
    resumo = {c["nome"]: c for c in execucao.manifest["cenarios"]}
    assert resumo["lento"]["duracao"]["arquivo"] == "configs/duracao_mais_25.yaml" and "duracao" not in resumo["normal"]


def test_experimentos_3_e_4_sao_validos() -> None:
    from critical_failure.experimentos.config import carregar_experimento

    ablacao = carregar_experimento(RAIZ / "experimentos" / "fase4_exp3_ablacao.yaml")
    assert len(ablacao.cenarios) == 18 and sum(c.partidas for c in ablacao.cenarios) == 36_000
    sensibilidade = carregar_experimento(RAIZ / "experimentos" / "fase4_exp4_sensibilidade.yaml")
    assert len(sensibilidade.cenarios) == 44 and sum(c.partidas for c in sensibilidade.cenarios) == 88_000
    combinacoes = carregar_experimento(RAIZ / "experimentos" / "fase4_exp4b_combinacoes.yaml")
    assert len(combinacoes.cenarios) == 16 and sum(c.partidas for c in combinacoes.cenarios) == 32_000
    assert {tuple(sorted(c.mudancas.items())) for c in combinacoes.cenarios} == {
        (("dano.incidente.sem_cobertura", d), ("fichas.iniciais", f)) for f in (5, 6) for d in (2, 3)
    }
    assert {c.duracao for c in sensibilidade.cenarios} == {
        None,
        "configs/duracao_menos_25.yaml",
        "configs/duracao_mais_25.yaml",
    }

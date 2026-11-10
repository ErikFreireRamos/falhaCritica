"""Seção 9 da especificação: Critical Failure, pontuação final e vencedor."""

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest
from conftest import avancar, criar_motor, fichas, jogar, montar, tipos, todos, um

from critical_failure.nucleo.rng import FLUXO_JOGO, gerador
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.estado import Estado, Evento, Pendente
from critical_failure.regras.v2.motor import MotorV2


def com_o_dado(motor: MotorV2, estado: Estado, categoria: str | None, primeira_face: int | None = None) -> Estado:
    """Ajusta o contador de aleatoriedade para o dado dar a categoria pedida na 1ª rolagem.

    Com ``primeira_face``, procura um contador em que a primeira rolagem dê essa face.
    """
    for contador in range(5000):
        face = int(gerador(estado.semente, estado.partida, FLUXO_JOGO, contador).integers(1, motor.faces + 1))
        if primeira_face is not None:
            if face == primeira_face:
                return replace(estado, contador_rng=contador)
        elif motor.catalogo.categoria_da_face(face) == categoria:
            return replace(estado, contador_rng=contador)
    raise AssertionError("não achei um contador para o dado pedido")


def fim(
    motor: MotorV2, categoria: str = "Desempenho", n: int = 4, acertos: list[int] | None = None, **mesa: Any
) -> tuple[Estado, list[Evento]]:
    """Leva a partida do fim da Produção do ciclo 3 até o fim, com o dado na categoria pedida.

    O incidente do ciclo é o 04 (Compatibilidade) e ninguém leva dano dele aqui:
    a partida já está na Lição aprendida, e o jogador recusa.
    """
    estado = montar(
        motor,
        n=n,
        fase=E.PRODUCAO,
        ciclo=3,
        agora="04",
        proximo=None,
        linha_do_tempo=(),
        pendente=Pendente(E.LICAO, 0),
        **mesa,
    )
    jogadores = tuple(replace(jogador, acertos=(acertos or [0] * n)[j]) for j, jogador in enumerate(estado.jogadores))
    estado = replace(estado, jogadores=jogadores, diagnosticos=("Compatibilidade",) * n, fila_da_licao=(0,))
    return jogar(motor, com_o_dado(motor, estado, categoria), "recusar")


def dano_cf(eventos: list[Evento], assento: int) -> dict[str, int]:
    (evento,) = [ev for ev in todos(eventos, "dano_critical_failure") if ev.ator == assento]
    return dict(evento.publico["itens"])


# ---------------------------------------------------------------- estrutura


@pytest.mark.regra("R-9.0.1", "R-4.2", "R-3.2a", "R-2.0.3", "R-1.3", "R-3.2b")
def test_depois_do_terceiro_ciclo_vem_o_critical_failure_e_a_pontuacao(motor: MotorV2) -> None:
    estado, eventos = motor.preparar(4, semente=2, partida=5)
    sorteados = um(eventos, "linha_do_tempo").oculto["incidentes"]
    while estado.pendente is not None:
        estado, novos = avancar(motor, estado, E.FIM)
        eventos += novos
    ordem = tipos(eventos)
    # 3 ciclos, cada um com o seu incidente, e só os 3 sorteados aparecem.
    assert [ev.publico["incidente"] for ev in todos(eventos, "gabarito_revelado")] == sorteados
    assert len(todos(eventos, "fim_do_ciclo")) == 2
    # O Critical Failure vem uma vez só, depois da última limpeza e antes da pontuação final.
    assert ordem.count("critical_failure") == 1
    ultima_limpeza = len(ordem) - 1 - ordem[::-1].index("limpeza")
    assert ultima_limpeza < ordem.index("critical_failure") < ordem.index("pontuacao_final")
    assert ordem[-1] == "fim_de_jogo" and estado.fase == E.FIM
    assert um(eventos, "critical_failure").ciclo == 3


@pytest.mark.regra("R-9.1.2")
def test_no_critical_failure_nao_ha_diagnostico(motor: MotorV2) -> None:
    estado, eventos = fim(motor)
    assert estado.pendente is None and estado.fase == E.FIM
    depois = tipos(eventos)[tipos(eventos).index("critical_failure") :]
    assert not any(tipo.startswith("diagnostico") or tipo == "gabarito_revelado" for tipo in depois)


# ---------------------------------------------------------------- o dado


@pytest.mark.regra("R-9.1.1", "R-2.0.16")
def test_o_dado_sorteia_a_categoria_e_o_oito_e_rolado_de_novo(motor: MotorV2) -> None:
    for categoria in motor.catalogo.categorias:
        _, eventos = fim(motor, categoria)
        assert um(eventos, "critical_failure").publico == {
            "rolagens": [motor.catalogo.categorias.index(categoria) + 1],
            "categoria": categoria,
        }
    # Sem o módulo, a face 8 não vale: rola-se de novo até sair uma categoria do jogo.
    estado = montar(
        motor, fase=E.PRODUCAO, ciclo=3, agora="04", proximo=None, linha_do_tempo=(), pendente=Pendente(E.LICAO, 0)
    )
    estado = replace(estado, diagnosticos=("Compatibilidade",) * 4, fila_da_licao=(0,))
    _, eventos = jogar(motor, com_o_dado(motor, estado, None, primeira_face=8), "recusar")
    sorteio = um(eventos, "critical_failure").publico
    assert sorteio["rolagens"][0] == 8 and len(sorteio["rolagens"]) >= 2
    assert sorteio["rolagens"][-1] != 8 and sorteio["categoria"] in motor.catalogo.categorias


@pytest.mark.regra("R-11.5")
def test_com_o_modulo_a_face_oito_vale(motor_com_modulo: MotorV2) -> None:
    _, eventos = fim(motor_com_modulo, "Segurança Operacional")
    assert um(eventos, "critical_failure").publico == {"rolagens": [8], "categoria": "Segurança Operacional"}


def test_o_dado_e_uniforme_entre_as_categorias_do_jogo(motor: MotorV2) -> None:
    contagem: dict[str, int] = dict.fromkeys(motor.catalogo.categorias, 0)
    for partida in range(700):
        estado = replace(
            montar(
                motor,
                fase=E.PRODUCAO,
                ciclo=3,
                agora="04",
                proximo=None,
                linha_do_tempo=(),
                pendente=Pendente(E.LICAO, 0),
            ),
            partida=partida,
            diagnosticos=("Compatibilidade",) * 4,
            fila_da_licao=(0,),
        )
        _, eventos = jogar(motor, estado, "recusar")
        contagem[um(eventos, "critical_failure").publico["categoria"]] += 1
    # 700 sorteios em 7 categorias: 100 esperados em cada; a folga é larga de propósito.
    assert all(60 <= vezes <= 140 for vezes in contagem.values()), contagem


# ---------------------------------------------------------------- dano do Critical Failure


@pytest.mark.regra("R-9.1.3", "R-9.1.4", "R-9.1.5", "R-9.1.6", "R-9.1.7", "R-9.2.3a")
@pytest.mark.parametrize(
    "sistema, alertas, itens",
    [
        # R-9.1.8: 1 com cobertura profunda, 2 com cobertura simples, 4 sem cobertura, mais 1 com Alerta.
        (["Carga", "Pico"], [], {"sempre": 1}),
        (["Carga"], [], {"sempre": 1, "sem_cobertura_profunda": 1}),
        (["Carga", "Carga"], [], {"sempre": 1, "sem_cobertura_profunda": 1}),  # mesmo teste não é profunda
        ([], [], {"sempre": 1, "sem_cobertura_profunda": 1, "sem_cobertura": 2}),
        (["Regressão", "Recuperação"], [], {"sempre": 1, "sem_cobertura_profunda": 1, "sem_cobertura": 2}),
        (["Carga", "Pico"], ["Desempenho"], {"sempre": 1, "alerta": 1}),
        ([], ["Desempenho"], {"sempre": 1, "sem_cobertura_profunda": 1, "sem_cobertura": 2, "alerta": 1}),
        ([], ["Interação"], {"sempre": 1, "sem_cobertura_profunda": 1, "sem_cobertura": 2}),
    ],
)
def test_itens_de_dano_do_critical_failure(
    motor: MotorV2, sistema: list[str], alertas: list[str], itens: dict[str, int]
) -> None:
    estado, eventos = fim(
        motor, "Desempenho", sistemas=[sistema, [], [], []], alertas=[alertas, [], [], []], fichas=[20] * 4
    )
    (evento,) = [ev for ev in todos(eventos, "dano_critical_failure") if ev.ator == 0]
    assert evento.publico["itens"] == itens
    assert evento.publico["fichas"] == {"0": -sum(itens.values())}


@pytest.mark.regra("R-9.1.6", "R-9.2.4")
def test_o_alerta_nao_sai_depois_do_critical_failure(motor: MotorV2) -> None:
    """AMB-12: o cubo custa 1 no Critical Failure e mais 1 na pontuação final."""
    estado, eventos = fim(motor, "Desempenho", alertas=[["Desempenho"], [], [], []], fichas=[20] * 4)
    assert dano_cf(eventos, 0)["alerta"] == 1
    assert estado.jogadores[0].alertas == ("Desempenho",)
    final = [ev for ev in todos(eventos, "pontuacao_final") if ev.ator == 0][0]
    assert final.publico["alertas_ativos"] == 1 and final.publico["perda"] == 1
    assert fichas(estado)[0] == 20 - 5 - 1

    limpa = criar_motor(**{"interpretacoes.critical_failure_limpa_alertas": True})
    estado, eventos = fim(limpa, "Desempenho", alertas=[["Desempenho"], [], [], []], fichas=[20] * 4)
    assert um(eventos, "limpeza_critical_failure").publico["alertas_removidos"] == [0]
    assert fichas(estado)[0] == 20 - 5


# ---------------------------------------------------------------- pontuação final


@pytest.mark.regra("R-9.2.1", "R-9.2.2", "R-9.2.3", "R-9.2.4", "R-9.2.5")
@pytest.mark.parametrize(
    "sistema, alertas, categorias, profundas, ganho, perda",
    [
        ([], [], 0, 0, 0, 0),
        (["Carga"], [], 1, 0, 1, 0),
        (["Carga", "Carga"], [], 1, 0, 1, 0),  # carta repetida do mesmo teste não soma
        (["Carga", "Pico"], [], 1, 1, 2, 0),
        (["Carga", "Regressão", "Recuperação", "Autenticação", "Coexistência"], [], 5, 0, 5, 0),
        (["Carga", "Pico", "Regressão", "Análise estática", "Recuperação"], [], 3, 2, 5, 0),
        (["Carga", "Pico", "Estresse", "Resistência", "Regressão"], [], 2, 1, 3, 0),
        (["Carga", "Regressão"], ["Interação", "Flexibilidade"], 2, 0, 2, 2),
    ],
)
def test_pontuacao_final(
    motor: MotorV2, sistema: list[str], alertas: list[str], categorias: int, profundas: int, ganho: int, perda: int
) -> None:
    estado, eventos = fim(
        motor, "Manutenibilidade", sistemas=[sistema, [], [], []], alertas=[alertas, [], [], []], fichas=[20] * 4
    )
    (final,) = [ev for ev in todos(eventos, "pontuacao_final") if ev.ator == 0]
    assert final.publico["sistema"] == sistema  # todos viram o sistema inteiro para cima
    assert (final.publico["categorias_distintas"], final.publico["coberturas_profundas"]) == (categorias, profundas)
    assert (final.publico["ganho"], final.publico["perda"]) == (ganho, perda)
    assert final.publico["fichas"] == {"0": ganho - perda}
    assert final.publico["ganho"] <= motor.teto, "o sistema vale no máximo 5 fichas (R-9.2.6)"
    assert set(estado.jogadores[0].reveladas) == set(estado.jogadores[0].sistema)


@pytest.mark.regra("R-5.2", "R-9.2.1")
def test_pontuacao_final_com_poucas_fichas_usa_o_saldo(motor: MotorV2) -> None:
    """AMB-13: 0 fichas, +3 de amplitude e 1 Alerta. Saldo único dá 2; perdas antes dos ganhos, 3."""
    mesa: dict[str, Any] = {
        "sistemas": [["Carga", "Regressão", "Recuperação"], [], [], []],
        "alertas": [["Interação"], [], [], []],
        "fichas": [2, 5, 5, 5],  # o Critical Failure de Desempenho tira 2 e deixa 0
    }
    estado, eventos = fim(motor, "Desempenho", **mesa)
    assert dano_cf(eventos, 0) == {"sempre": 1, "sem_cobertura_profunda": 1}
    assert fichas(estado)[0] == 2

    perdas_primeiro = criar_motor(**{"interpretacoes.final_ordem": "perdas_primeiro"})
    estado, _ = fim(perdas_primeiro, "Desempenho", **mesa)
    assert fichas(estado)[0] == 3


# ---------------------------------------------------------------- vencedor


@pytest.mark.regra("R-1.1")
def test_vence_quem_tem_mais_fichas(motor: MotorV2) -> None:
    estado, eventos = fim(motor, fichas=[10, 12, 9, 11])
    resultado = um(eventos, "fim_de_jogo").publico
    # Sem cartas nem Alertas, todos perdem 4 no Critical Failure e nada muda na pontuação final.
    assert resultado == {"placar": [6, 8, 5, 7], "vencedores": [1], "criterio": "fichas"}
    assert estado.vencedores == (1,)


@pytest.mark.regra("R-9.2.7")
def test_desempate_por_menos_alertas_ativos(motor: MotorV2) -> None:
    # Ana chega com 1 ficha a mais e 1 Alerta fora da categoria do dado: empata em fichas com Bruno.
    estado, eventos = fim(motor, fichas=[11, 10, 5, 5], alertas=[["Interação"], [], [], []])
    resultado = um(eventos, "fim_de_jogo").publico
    assert resultado["placar"][:2] == [6, 6]
    assert resultado["vencedores"] == [1] and resultado["criterio"] == "alertas"


@pytest.mark.regra("R-9.2.8")
def test_desempate_por_mais_diagnosticos_certos(motor: MotorV2) -> None:
    estado, eventos = fim(motor, fichas=[10, 10, 5, 5], acertos=[1, 2, 3, 0])
    resultado = um(eventos, "fim_de_jogo").publico
    # Carla tem mais acertos, mas não está empatada em fichas: o critério só vale entre os empatados.
    assert resultado["vencedores"] == [1] and resultado["criterio"] == "diagnosticos"


def test_empate_que_persiste_divide_a_vitoria(motor: MotorV2) -> None:
    """AMB-14."""
    estado, eventos = fim(motor, fichas=[10, 10, 5, 10], acertos=[2, 2, 3, 1])
    fim_de_jogo = um(eventos, "fim_de_jogo")
    assert fim_de_jogo.publico["vencedores"] == [0, 1] and fim_de_jogo.publico["criterio"] == "dividida"
    assert fim_de_jogo.amb == "AMB-14"
    assert estado.vencedores == (0, 1)

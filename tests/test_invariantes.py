"""As invariantes acusam cada violação (testes negativos, autor em 2026-11-14).

Os outros testes só conferem que estados válidos passam. Aqui cada teste entrega um estado com
uma violação de propósito e confere a mensagem exata, e que ``conferir`` levanta o erro. Achado do
teste de mutação: sem estes testes, até desligar a conferência inteira passava despercebido.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import replace
from typing import Any

import pytest
from conftest import jogar, montar
from test_v1 import CF, LOAD, RECOVERY, ataque, montar_v1

from critical_failure.nucleo.erros import ViolacaoDeInvariante
from critical_failure.regras.v1 import estado as E1
from critical_failure.regras.v1 import invariantes as I1
from critical_failure.regras.v1.motor import MotorV1
from critical_failure.regras.v2 import estado as E2
from critical_failure.regras.v2 import invariantes as I2
from critical_failure.regras.v2.motor import MotorV2


def trocar_jogador(estado: Any, assento: int, **campos: Any) -> Any:
    jogadores = list(estado.jogadores)
    jogadores[assento] = replace(jogadores[assento], **campos)
    return replace(estado, jogadores=tuple(jogadores))


# ---------------------------------------------------------------- v2


def violacoes_v2(motor: MotorV2, estado: Any, em_repouso: bool = True) -> list[str]:
    return I2.violacoes(estado, motor.regras, motor.catalogo, em_repouso)


def test_v2_estado_valido_nao_tem_violacao(motor: MotorV2) -> None:
    estado = montar(motor, sistemas=[["Carga"], [], [], []])
    assert violacoes_v2(motor, estado) == []
    I2.conferir(estado, motor.regras, motor.catalogo)  # não levanta


CORROMPIDOS_V2: list[tuple[str, Callable[[MotorV2, Any], Any], str]] = [
    (
        "carta_duplicada",
        lambda m, e: replace(e, descarte=(*e.descarte, e.baralho[0])),
        "cartas não se conservam: 64 em jogo, 63 no catálogo",
    ),
    (
        "backlog_grande",
        lambda m, e: replace(e, backlog=e.baralho[:6], baralho=e.baralho[6:]),
        "Backlog com 6 cartas",
    ),
    (
        "sistema_acima_do_teto",
        lambda m, e: replace(trocar_jogador(e, 0, sistema=e.baralho[:6]), baralho=e.baralho[6:]),
        "assento 0: sistema com 6 cartas (teto 5)",
    ),
    ("fichas_negativas", lambda m, e: trocar_jogador(e, 1, fichas=-1), "assento 1: -1 fichas (mínimo 0)"),
    (
        "alerta_repetido",
        lambda m, e: trocar_jogador(e, 2, alertas=("Desempenho", "Desempenho")),
        "assento 2: mais de um Alerta na mesma categoria",
    ),
    (
        "alerta_fora_do_jogo",
        lambda m, e: trocar_jogador(e, 3, alertas=("Inexistente",)),
        "assento 3: Alerta em categoria fora do jogo",
    ),
    (
        "revelada_fora_do_sistema",
        lambda m, e: trocar_jogador(e, 0, reveladas=(e.baralho[0],)),
        "assento 0: carta revelada que não está no sistema",
    ),
    (
        "pega_do_backlog_sumiu",
        lambda m, e: trocar_jogador(e, 0, pegas_do_backlog=(e.baralho[0],)),
        "assento 0: carta pega do Backlog que o jogador não tem mais",
    ),
    (
        "acertos_demais",
        lambda m, e: trocar_jogador(e, 1, acertos=e.ciclo + 1),
        "assento 1: mais acertos do que incidentes já diagnosticados",
    ),
    ("primeiro_fora_da_mesa", lambda m, e: replace(e, primeiro=e.n), "marcadores fora da mesa"),
    ("auditor_fora_da_mesa", lambda m, e: replace(e, auditor=-1), "marcadores fora da mesa"),
    (
        "auditor_fora_de_lugar",
        lambda m, e: replace(e, auditor=(e.auditor + 1) % e.n),
        "o Auditor não é o último da ordem de jogo (R-4.9a)",
    ),
    (
        "fim_com_decisao_pendente",
        lambda m, e: replace(e, fase=E2.FIM, vencedores=(0,)),
        "partida encerrada com decisão pendente ou sem vencedor",
    ),
    (
        "fim_sem_vencedor",
        lambda m, e: replace(e, fase=E2.FIM, pendente=None, vencedores=()),
        "partida encerrada com decisão pendente ou sem vencedor",
    ),
    (
        "andamento_sem_decisao",
        lambda m, e: replace(e, pendente=None),
        "partida em andamento (homologacao) sem decisão pendente",
    ),
]


@pytest.mark.parametrize(
    ("corromper", "mensagem"), [(c, m) for _, c, m in CORROMPIDOS_V2], ids=[n for n, _, _ in CORROMPIDOS_V2]
)
def test_v2_cada_violacao_e_acusada(motor: MotorV2, corromper: Callable[[MotorV2, Any], Any], mensagem: str) -> None:
    estado = corromper(motor, montar(motor))
    assert violacoes_v2(motor, estado) == [mensagem]
    with pytest.raises(ViolacaoDeInvariante, match=f"^{re.escape(mensagem)}$"):
        I2.conferir(estado, motor.regras, motor.catalogo)


def test_v2_fora_de_repouso_nao_exige_decisao_pendente(motor: MotorV2) -> None:
    estado = replace(montar(motor), pendente=None)
    assert violacoes_v2(motor, estado, em_repouso=False) == []
    I2.conferir(estado, motor.regras, motor.catalogo, em_repouso=False)
    with pytest.raises(ViolacaoDeInvariante):  # em repouso, o padrão
        I2.conferir(estado, motor.regras, motor.catalogo)


def test_v2_disputa_fora_da_homologacao(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga"], [], [], []])
    estado, _ = jogar(motor, estado, "testar:Carga:1")
    assert estado.disputa is not None and violacoes_v2(motor, estado) == []
    assert violacoes_v2(motor, replace(estado, fase=E2.PLANEJAMENTO)) == ["disputa aberta fora da Homologação"]


def test_v2_varias_violacoes_vao_juntas_na_mensagem(motor: MotorV2) -> None:
    estado = trocar_jogador(montar(motor), 1, fichas=-1, acertos=5)
    with pytest.raises(ViolacaoDeInvariante) as erro:
        I2.conferir(estado, motor.regras, motor.catalogo)
    assert str(erro.value) == (
        "assento 1: -1 fichas (mínimo 0); assento 1: mais acertos do que incidentes já diagnosticados"
    )


def test_v2_na_preparacao_nada_e_conferido(motor: MotorV2) -> None:
    estado = replace(montar(motor), fase=E2.PREPARACAO, descarte=(0,), pendente=None)
    assert violacoes_v2(motor, estado) == []


# ---------------------------------------------------------------- v1


@pytest.fixture(scope="module")
def motor_v1() -> MotorV1:
    from conftest import CONFIGS

    from critical_failure.regras.familias import carregar_motor

    motor = carregar_motor(CONFIGS / "regras_v1.yaml")
    assert isinstance(motor, MotorV1)
    return motor


def violacoes_v1(motor: MotorV1, estado: Any, em_repouso: bool = True) -> list[str]:
    return I1.violacoes(estado, motor.regras, motor.catalogo, em_repouso)


def base_v1(motor: MotorV1) -> Any:
    return montar_v1(motor, sistemas=[[RECOVERY], [], [], []], maos=[[LOAD], [], [], []])


def test_v1_estado_valido_nao_tem_violacao(motor_v1: MotorV1) -> None:
    estado = base_v1(motor_v1)
    assert violacoes_v1(motor_v1, estado) == []
    I1.conferir(estado, motor_v1.regras, motor_v1.catalogo)  # não levanta


def cf_no_sistema(m: MotorV1, e: Any) -> Any:
    cf = next(carta for carta in e.baralho if m.catalogo.cartas[carta] == CF)
    return replace(trocar_jogador(e, 1, sistema=(cf,)), baralho=tuple(c for c in e.baralho if c != cf))


def sem_baralho(e: Any) -> Any:
    """Baralho todo no descarte: válido nos testes, mas a preparação sem baralho não é conferida."""
    return replace(e, baralho=(), descarte=e.baralho)


CORROMPIDOS_V1: list[tuple[str, Callable[[MotorV1, Any], Any], list[str]]] = [
    (
        "carta_duplicada",
        lambda m, e: replace(e, descarte=(e.baralho[0],)),
        ["cartas não se conservam: 55 em jogo, 54 no baralho"],
    ),
    ("critical_failure_no_sistema", cf_no_sistema, ["assento 1: carta Critical Failure no sistema (V1-4.2.2)"]),
    (
        "mao_grande",
        lambda m, e: replace(trocar_jogador(e, 2, mao=e.baralho[:7], testes_feitos=0), baralho=e.baralho[7:]),
        [
            "assento 2: mão com 7 cartas",
            "assento 2: cartas de teste na mão e testes feitos não somam o esperado",
        ],
    ),
    (
        "testes_demais",
        lambda m, e: trocar_jogador(e, 2, testes_feitos=4),
        [
            "assento 2: 4 testes, mais que as cartas de teste",
            "assento 2: cartas de teste na mão e testes feitos não somam o esperado",
        ],
    ),
    (
        "revelada_fora_do_sistema",
        lambda m, e: trocar_jogador(e, 0, reveladas=(e.baralho[0],)),
        ["assento 0: carta revelada que não está no sistema"],
    ),
    (
        "soma_da_mao_errada",
        lambda m, e: trocar_jogador(e, 3, testes_feitos=2),
        ["assento 3: cartas de teste na mão e testes feitos não somam o esperado"],
    ),
    (
        "fim_com_decisao_pendente",
        lambda m, e: replace(e, fase=E1.FIM, vencedores=(0,)),
        ["partida encerrada com decisão pendente ou sem vencedor"],
    ),
    (
        "fim_sem_vencedor",
        lambda m, e: replace(e, fase=E1.FIM, pendente=None, vencedores=()),
        ["partida encerrada com decisão pendente ou sem vencedor"],
    ),
    (
        "andamento_sem_decisao",
        lambda m, e: replace(e, pendente=None),
        ["partida em andamento (testes) sem decisão pendente"],
    ),
    (
        "baralho_vazio_nos_testes",
        lambda m, e: sem_baralho(cf_no_sistema(m, e)),
        ["assento 1: carta Critical Failure no sistema (V1-4.2.2)"],
    ),
]


@pytest.mark.parametrize(
    ("corromper", "mensagens"), [(c, m) for _, c, m in CORROMPIDOS_V1], ids=[n for n, _, _ in CORROMPIDOS_V1]
)
def test_v1_cada_violacao_e_acusada(
    motor_v1: MotorV1, corromper: Callable[[MotorV1, Any], Any], mensagens: list[str]
) -> None:
    estado = corromper(motor_v1, base_v1(motor_v1))
    assert violacoes_v1(motor_v1, estado) == mensagens
    with pytest.raises(ViolacaoDeInvariante) as erro:
        I1.conferir(estado, motor_v1.regras, motor_v1.catalogo)
    assert str(erro.value) == "; ".join(mensagens)


def test_v1_fora_de_repouso_nao_exige_decisao_pendente(motor_v1: MotorV1) -> None:
    estado = replace(base_v1(motor_v1), pendente=None)
    assert violacoes_v1(motor_v1, estado, em_repouso=False) == []
    I1.conferir(estado, motor_v1.regras, motor_v1.catalogo, em_repouso=False)
    with pytest.raises(ViolacaoDeInvariante):  # em repouso, o padrão
        I1.conferir(estado, motor_v1.regras, motor_v1.catalogo)


def test_v1_disputa_fora_da_fase_de_testes(motor_v1: MotorV1) -> None:
    from test_v1 import jogar as jogar_v1

    estado, _ = jogar_v1(motor_v1, base_v1(motor_v1), ataque(LOAD, 1))
    assert estado.disputa is not None and violacoes_v1(motor_v1, estado) == []
    assert violacoes_v1(motor_v1, replace(estado, fase=E1.MONTAGEM)) == ["disputa aberta fora da fase de testes"]


def test_v1_na_preparacao_sem_baralho_nada_e_conferido(motor_v1: MotorV1) -> None:
    estado = replace(base_v1(motor_v1), fase=E1.PREPARACAO, baralho=(), pendente=None)
    assert violacoes_v1(motor_v1, estado) == []
    # Com baralho, a preparação já é conferida.
    com_baralho = replace(base_v1(motor_v1), fase=E1.PREPARACAO, descarte=(base_v1(motor_v1).baralho[0],))
    assert violacoes_v1(motor_v1, com_baralho) == ["cartas não se conservam: 55 em jogo, 54 no baralho"]

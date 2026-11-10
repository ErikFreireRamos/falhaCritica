"""Seção 3 da especificação: preparação da partida."""

from __future__ import annotations

import pytest
from conftest import todos, um

from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.estado import Pendente
from critical_failure.regras.v2.motor import MotorV2


@pytest.mark.regra("R-3.1", "R-3.4", "R-3.4c", "R-3.5", "R-3.6", "R-3.6a", "R-2.0.11")
@pytest.mark.parametrize("n", [4, 5])
def test_estado_depois_da_preparacao(motor: MotorV2, n: int) -> None:
    estado, eventos = motor.preparar(n, semente=1, partida=0)
    assert [jogador.fichas for jogador in estado.jogadores] == [5] * n
    assert [len(jogador.sistema) for jogador in estado.jogadores] == [2] * n
    assert all(jogador.mao == () for jogador in estado.jogadores)
    assert len(estado.backlog) == 5
    # R-3.8: a preparação usa 2 cartas por jogador e 5 no Backlog.
    assert len(estado.baralho) == 63 - 2 * n - 5
    assert estado.primeiro == 0  # AMB-08
    assert estado.auditor == n - 1  # à direita do primeiro jogador
    assert um(eventos, "marcadores").publico == {"primeiro": 0, "auditor": n - 1}
    assert estado.ciclo == 1 and estado.fase == E.PLANEJAMENTO
    assert estado.pendente == Pendente(E.COMPRAR, 0)


@pytest.mark.regra("R-3.2", "R-3.2b", "R-3.3", "R-4.11")
def test_linha_do_tempo_e_radar(motor: MotorV2) -> None:
    estado, eventos = motor.preparar(4, semente=1, partida=0)
    sorteados = um(eventos, "linha_do_tempo").oculto["incidentes"]
    assert len(sorteados) == len(set(sorteados)) == 3
    assert set(sorteados) <= set(motor.catalogo.incidentes)
    assert (estado.agora, estado.proximo, estado.linha_do_tempo) == (sorteados[0], sorteados[1], (sorteados[2],))
    assert um(eventos, "radar").publico == {"agora": sorteados[0], "proximo": sorteados[1]}
    # O sorteio fica em "oculto": ninguém vê a Linha do Tempo.
    assert um(eventos, "linha_do_tempo").publico == {} and um(eventos, "linha_do_tempo").visivel_para == {}


@pytest.mark.regra("R-1.2")
def test_numero_de_jogadores_fora_do_intervalo(motor: MotorV2, motor_impresso: MotorV2) -> None:
    for n in (0, 1, 3, 6, 7):
        with pytest.raises(ConfiguracaoInvalida, match="R-1.2"):
            motor.preparar(n, semente=1, partida=0)
    # COR-01: a regra impressa aceitava 6.
    estado, _ = motor_impresso.preparar(6, semente=1, partida=0)
    assert estado.n == 6


@pytest.mark.regra("R-3.4b")
def test_carta_repetida_e_trocada_e_vai_para_o_fundo(motor: MotorV2) -> None:
    cat = motor.catalogo
    com_troca = 0
    for partida in range(300):
        estado, eventos = motor.preparar(5, semente=11, partida=partida)
        for jogador in estado.jogadores:
            nomes = cat.nomes(jogador.sistema)
            assert len(set(nomes)) == len(nomes), "sistema inicial com duas cartas do mesmo teste"
        trocas = todos(eventos, "carta_trocada")
        if len(trocas) == 1:
            com_troca += 1
            # AMB-07: a carta trocada vai para o fundo do baralho.
            assert cat.teste(estado.baralho[-1]) == trocas[0].oculto["saiu"]
            assert trocas[0].amb == "AMB-07"
            assert trocas[0].oculto["entrou"] in cat.nomes(estado.jogadores[trocas[0].ator].sistema)
    assert com_troca > 0, "nenhuma preparação com carta repetida em 300 partidas"


def test_preparacao_e_deterministica(motor: MotorV2) -> None:
    assert motor.preparar(4, semente=5, partida=3)[0] == motor.preparar(4, semente=5, partida=3)[0]
    assert motor.preparar(4, semente=5, partida=3)[0] != motor.preparar(4, semente=5, partida=4)[0]
    assert motor.preparar(4, semente=5, partida=3)[0] != motor.preparar(4, semente=6, partida=3)[0]


def test_baralho_nao_depende_do_numero_de_jogadores_nem_dos_bots(motor: MotorV2) -> None:
    """Números aleatórios comuns: a mesma semente dá o mesmo embaralhamento em mesas diferentes."""
    com_4 = um(motor.preparar(4, semente=9, partida=2)[1], "baralho_embaralhado").oculto["ordem"]
    com_5 = um(motor.preparar(5, semente=9, partida=2)[1], "baralho_embaralhado").oculto["ordem"]
    assert com_4 == com_5 and sorted(com_4) == list(range(63))

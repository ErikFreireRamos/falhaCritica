"""Modelo de duração (MOD-05): soma de tempos por ação, lidos de configs/duracao.yaml."""

from __future__ import annotations

import copy
from collections import Counter
from typing import Any

import pytest
from conftest import CONFIGS, ler_yaml

from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.duracao import carregar_duracao, ler_duracao
from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.partida import jogar_partida
from critical_failure.regras.v2.estado import Evento
from critical_failure.regras.v2.motor import MotorV2

DURACAO = CONFIGS / "duracao.yaml"


def test_os_tempos_do_pdf_estao_no_modelo() -> None:
    modelo = carregar_duracao(DURACAO)
    assert modelo.preparacao.valor == 180  # p. 4: cerca de 3 minutos
    assert modelo.turno_de_planejamento.valor == 30  # R-6.7
    assert modelo.teste_com_defesa.valor == 60  # p. 34: cada defesa leva até 1 minuto
    assert all(tempo["fonte"] for nome, tempo in modelo.resolvido().items() if nome != "esquema")


def test_a_duracao_e_a_soma_dos_tempos_de_cada_acao(motor: MotorV2) -> None:
    modelo = carregar_duracao(DURACAO)
    eventos: list[Evento] = []
    resultado = jogar_partida(
        motor,
        [BotAleatorio() for _ in range(4)],
        semente=3,
        partida=8,
        duracao=modelo,
        ouvinte=lambda evento, decisao: eventos.append(evento),
    )
    vezes = Counter(evento.tipo for evento in eventos)
    defesas_conferidas = vezes["conferencia"]
    esperado = (
        modelo.preparacao.valor
        + vezes["fim_do_turno"] * modelo.turno_de_planejamento.valor
        + (vezes["teste"] - defesas_conferidas) * modelo.teste_admitido.valor
        + defesas_conferidas * modelo.teste_com_defesa.valor
        + vezes["contestacao"] * modelo.contestacao.valor
        + vezes["passou"] * modelo.passar.valor
        + 3 * modelo.producao.valor
        + modelo.fim_de_jogo.valor
    )
    assert resultado.duracao_s == esperado
    assert vezes["fim_do_turno"] == 4 * 3  # cada jogador faz um turno por ciclo
    assert resultado.vezes("teste") == vezes["teste"]


def test_sem_modelo_a_duracao_fica_vazia(motor: MotorV2) -> None:
    resultado = jogar_partida(motor, [BotAleatorio() for _ in range(4)], semente=3, partida=8)
    assert resultado.duracao_s is None


def test_mudar_um_tempo_muda_o_hash_do_modelo() -> None:
    modelo = carregar_duracao(DURACAO)
    dados = ler_yaml(DURACAO)
    dados["passar"]["valor"] = 6
    assert ler_duracao(dados).hash() != modelo.hash()


@pytest.mark.parametrize(
    "estrago",
    [
        {"passar": {"valor": -5, "fonte": "x"}},
        {"passar": {"valor": "cinco", "fonte": "x"}},
        {"passar": None},
        {"tempo_que_nao_existe": {"valor": 1, "fonte": "x"}},
        {"esquema": "cf-duracao/9"},
    ],
)
def test_modelo_malformado_gera_erro_controlado(estrago: dict[str, Any]) -> None:
    dados = copy.deepcopy(ler_yaml(DURACAO))
    for chave, valor in estrago.items():
        if valor is None:
            del dados[chave]
        else:
            dados[chave] = valor
    with pytest.raises(ConfiguracaoInvalida):
        ler_duracao(dados)

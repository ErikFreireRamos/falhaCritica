"""Intervalos de confiança e veredito dos requisitos."""

from __future__ import annotations

import numpy as np
import pytest

from critical_failure.metricas.estatistica import (
    FALHA,
    INCONCLUSIVO,
    PASSA,
    intervalo_de_wilson,
    intervalo_por_bootstrap,
    pior,
    veredito,
)


@pytest.mark.parametrize(
    "sucessos, n, esperado",
    [
        # Valores de referência do intervalo de Wilson com 95% de confiança.
        (50, 100, (0.4038, 0.5962)),
        (4, 6, (0.3000, 0.9032)),  # as 4 de 6 partidas desequilibradas do artigo
        (0, 10, (0.0000, 0.2775)),
        (10, 10, (0.7225, 1.0000)),
    ],
)
def test_intervalo_de_wilson(sucessos: int, n: int, esperado: tuple[float, float]) -> None:
    baixo, alto = intervalo_de_wilson(sucessos, n)
    assert baixo == pytest.approx(esperado[0], abs=1e-4)
    assert alto == pytest.approx(esperado[1], abs=1e-4)


@pytest.mark.parametrize("sucessos, n", [(1, 0), (-1, 10), (11, 10)])
def test_wilson_recusa_contagem_invalida(sucessos: int, n: int) -> None:
    with pytest.raises(ValueError):
        intervalo_de_wilson(sucessos, n)


def test_bootstrap_e_deterministico_e_contem_a_estimativa() -> None:
    valores = np.random.default_rng(1).normal(45.0, 5.0, size=2000)

    def intervalo(estatistica: str) -> tuple[float, float]:
        return intervalo_por_bootstrap(valores, estatistica, np.random.default_rng(7), reamostras=400)

    media, mediana = intervalo("media"), intervalo("mediana")
    assert media == intervalo("media")
    assert media[0] < float(np.mean(valores)) < media[1]
    assert mediana[0] < float(np.median(valores)) < mediana[1]
    # O erro padrão da média é 5 / sqrt(2000), cerca de 0,11: o intervalo de 95% tem perto de 0,44 de largura.
    assert 0.3 < media[1] - media[0] < 0.6


def test_bootstrap_recusa_entrada_invalida() -> None:
    with pytest.raises(ValueError):
        intervalo_por_bootstrap(np.array([]), "media", np.random.default_rng(1))
    with pytest.raises(ValueError):
        intervalo_por_bootstrap(np.array([1.0, 2.0]), "moda", np.random.default_rng(1))


@pytest.mark.parametrize(
    "intervalo, esperado",
    [
        ((0.24, 0.26), PASSA),
        ((0.23, 0.27), PASSA),  # encostar na borda ainda é estar dentro
        ((0.22, 0.24), INCONCLUSIVO),
        ((0.26, 0.28), INCONCLUSIVO),
        ((0.20, 0.30), INCONCLUSIVO),
        ((0.10, 0.20), FALHA),
        ((0.28, 0.40), FALHA),
    ],
)
def test_veredito_compara_o_intervalo_inteiro_com_a_zona(intervalo: tuple[float, float], esperado: str) -> None:
    assert veredito(intervalo, (0.23, 0.27)) == esperado


def test_o_veredito_do_requisito_e_o_pior_das_medidas() -> None:
    assert pior([PASSA, PASSA]) == PASSA
    assert pior([PASSA, INCONCLUSIVO]) == INCONCLUSIVO
    assert pior([INCONCLUSIVO, FALHA, PASSA]) == FALHA
    assert pior([]) == INCONCLUSIVO

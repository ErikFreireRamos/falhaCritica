"""Intervalos de confiança e veredito.

Wilson para proporções e bootstrap para o resto, como definido em
``configs/requisitos.yaml``. O veredito compara o intervalo inteiro com a zona
de aceite, que é fixada antes de o experimento rodar:

- ``passa``: o intervalo inteiro está dentro da zona;
- ``falha``: o intervalo inteiro está fora da zona;
- ``inconclusivo``: o intervalo cruza a borda da zona.
"""

from __future__ import annotations

import math
from statistics import NormalDist

import numpy as np
from numpy.typing import NDArray

PASSA = "passa"
FALHA = "falha"
INCONCLUSIVO = "inconclusivo"
GRAVIDADE = {PASSA: 0, INCONCLUSIVO: 1, FALHA: 2}

Intervalo = tuple[float, float]


def intervalo_de_wilson(sucessos: int, n: int, confianca: float = 0.95) -> Intervalo:
    """Intervalo de Wilson para uma proporção."""
    if n <= 0 or not 0 <= sucessos <= n:
        raise ValueError(f"contagem inválida: {sucessos} sucessos em {n}")
    z = NormalDist().inv_cdf(0.5 + confianca / 2)
    p = sucessos / n
    denominador = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / denominador
    meia_largura = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denominador
    return max(0.0, centro - meia_largura), min(1.0, centro + meia_largura)


def intervalo_por_bootstrap(
    valores: NDArray[np.float64],
    estatistica: str,
    rng: np.random.Generator,
    reamostras: int = 1000,
    confianca: float = 0.95,
    lote: int = 50,
) -> Intervalo:
    """Intervalo percentil por bootstrap para a média ou a mediana."""
    if valores.size == 0:
        raise ValueError("não há valores para o bootstrap")
    if estatistica not in ("media", "mediana"):
        raise ValueError(f"estatística desconhecida: {estatistica}")
    estimativas: list[float] = []
    while len(estimativas) < reamostras:
        quantas = min(lote, reamostras - len(estimativas))
        indices = rng.integers(0, valores.size, size=(quantas, valores.size))
        amostras = valores[indices]
        resumo = np.mean(amostras, axis=1) if estatistica == "media" else np.median(amostras, axis=1)
        estimativas.extend(float(x) for x in resumo)
    cauda = (1 - confianca) / 2
    baixo, alto = np.quantile(np.array(estimativas), [cauda, 1 - cauda])
    return float(baixo), float(alto)


def intervalo_da_diferenca(
    a: NDArray[np.float64],
    b: NDArray[np.float64],
    rng: np.random.Generator,
    reamostras: int = 1000,
    confianca: float = 0.95,
) -> Intervalo:
    """Intervalo percentil por bootstrap para média(a) - média(b), com as duas amostras independentes."""
    if a.size == 0 or b.size == 0:
        raise ValueError("não há valores para o bootstrap")
    diferencas = [
        float(np.mean(a[rng.integers(0, a.size, a.size)]) - np.mean(b[rng.integers(0, b.size, b.size)]))
        for _ in range(reamostras)
    ]
    cauda = (1 - confianca) / 2
    baixo, alto = np.quantile(np.array(diferencas), [cauda, 1 - cauda])
    return float(baixo), float(alto)


def intervalo_da_razao(
    numeradores: NDArray[np.float64],
    denominadores: NDArray[np.float64],
    rng: np.random.Generator,
    reamostras: int = 1000,
    confianca: float = 0.95,
) -> Intervalo:
    """Intervalo percentil por bootstrap para soma(numeradores) / soma(denominadores), reamostrando as partidas."""
    if numeradores.size == 0 or numeradores.size != denominadores.size or float(denominadores.sum()) <= 0:
        raise ValueError("não há valores para o bootstrap da razão")
    razoes: list[float] = []
    while len(razoes) < reamostras:
        indices = rng.integers(0, numeradores.size, numeradores.size)
        abaixo = float(denominadores[indices].sum())
        if abaixo > 0:
            razoes.append(float(numeradores[indices].sum()) / abaixo)
    cauda = (1 - confianca) / 2
    baixo, alto = np.quantile(np.array(razoes), [cauda, 1 - cauda])
    return float(baixo), float(alto)


def veredito(intervalo: Intervalo, zona: Intervalo) -> str:
    """Compara o intervalo de confiança com a zona de aceite."""
    baixo, alto = intervalo
    minimo, maximo = zona
    if baixo >= minimo and alto <= maximo:
        return PASSA
    if alto < minimo or baixo > maximo:
        return FALHA
    return INCONCLUSIVO


def pior(vereditos: list[str]) -> str:
    """O veredito de um requisito é o pior entre as suas medidas."""
    return max(vereditos, key=lambda v: GRAVIDADE[v]) if vereditos else INCONCLUSIVO

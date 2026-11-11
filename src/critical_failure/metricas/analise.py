"""Toda a análise de uma execução: requisitos, descrição, estilos, desequilíbrio e matrizes.

O executor e o ``cf relatorio`` chamam a mesma função, então o relatório refeito
a partir do manifest e da tabela é igual ao original.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from critical_failure.experimentos.config import Experimento
from critical_failure.metricas.matrizes import (
    BLEFES,
    DOMINANCIA,
    MatrizDeEstilos,
    medidas_de_blefe,
    medidas_de_dominancia,
    montar_matrizes,
)
from critical_failure.metricas.requisitos import (
    Medida,
    avaliar,
    criterio_confirmado,
    descrever,
    desequilibrio,
    equilibrio_interno,
    vitorias_por_bot,
)


@dataclass(frozen=True)
class Analise:
    medidas: list[Medida]
    descricoes: list[dict[str, Any]]
    estilos: list[dict[str, Any]]
    desequilibrio: list[dict[str, Any]]
    matrizes: list[MatrizDeEstilos]
    interno: list[dict[str, Any]]


def analisar(linhas: list[dict[str, Any]], experimento: Experimento, requisitos: dict[str, dict[str, Any]]) -> Analise:
    criterio = criterio_confirmado(requisitos, DOMINANCIA)
    matrizes = montar_matrizes(linhas, experimento, float(criterio["diferenca_minima"]) if criterio else 0.0)
    medidas = avaliar(linhas, experimento, requisitos)
    if criterio is not None:
        medidas += medidas_de_dominancia(matrizes, criterio)
    criterio_dos_blefes = criterio_confirmado(requisitos, BLEFES)
    if criterio_dos_blefes is not None:
        medidas += medidas_de_blefe(matrizes, criterio_dos_blefes)
    return Analise(
        medidas=medidas,
        descricoes=descrever(linhas, experimento),
        estilos=vitorias_por_bot(linhas, experimento),
        desequilibrio=desequilibrio(linhas, experimento, requisitos),
        matrizes=matrizes,
        interno=equilibrio_interno(linhas, experimento),
    )

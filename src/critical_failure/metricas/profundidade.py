"""Profundidade do jogo (Experimento 7, autor em 2026-11-11): números sem critério de aceite.

Servem para comparar regras lado a lado. Cada medida vem com o intervalo de confiança de 95%,
reamostrando as partidas:

- **MET-08, escolhas:** decisões com 2 ou mais opções legais, por jogador e por partida (todas as
  fases); e, entre as decisões que o Heurístico avalia por valor (compra, colocação e ação na
  Homologação), a fração apertada: a segunda melhor opção a menos do limiar da melhor;
- **MET-09, viradas:** trocas de líder isolado por partida, conferidas a cada mudança de placar; e a
  recuperação: nas partidas com líder isolado no fim do ciclo 1, a fração da vitória que ficou com
  outro jogador (vitória dividida conta pela fatia);
- **MET-10, habilidade em degraus:** a taxa de vitória do bot foco (Heurístico normal) dividida por
  1/N, numa mesa de Heurísticos mais descuidados (temperatura maior). 1 é jogar tão bem quanto eles.

As defesas por jogador e por partida (testes por partida divididos por N: cada teste é uma defesa)
vão junto em todo cenário que pede alguma dessas medidas.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from critical_failure.experimentos.config import Experimento
from critical_failure.metricas.estatistica import Intervalo, intervalo_da_razao, intervalo_por_bootstrap
from critical_failure.metricas.requisitos import (
    _validas_do_grupo,
    amostra_do_foco,
    amostra_do_lider,
    grupos,
    rng_da_analise,
)

ESCOLHAS = "MET-08"
VIRADAS = "MET-09"
DEGRAUS = "MET-10"
MEDIDAS_DE_PROFUNDIDADE = (ESCOLHAS, VIRADAS, DEGRAUS)
FLUXO_DA_PROFUNDIDADE = 40_000
"""Base da chave do gerador do bootstrap destas medidas (cada grupo e cada medida tem a sua)."""


def _media(valores: np.ndarray[Any, np.dtype[np.float64]], rng: np.random.Generator) -> dict[str, Any]:
    return {"valor": float(valores.mean()), "intervalo": intervalo_por_bootstrap(valores, "media", rng)}


def _escalado(medida: dict[str, Any], fator: float) -> dict[str, Any]:
    baixo, alto = medida["intervalo"]
    return {"valor": medida["valor"] * fator, "intervalo": (baixo * fator, alto * fator)}


def _complemento(medida: dict[str, Any]) -> dict[str, Any]:
    baixo, alto = medida["intervalo"]
    intervalo: Intervalo = (1 - alto, 1 - baixo)
    return {"valor": 1 - medida["valor"], "intervalo": intervalo}


def profundidade(linhas: list[dict[str, Any]], experimento: Experimento) -> list[dict[str, Any]]:
    """Uma linha por grupo de cenários que pede MET-08, MET-09 ou MET-10."""
    resultado: list[dict[str, Any]] = []
    for indice, (nome, cenarios) in enumerate(grupos(experimento).items()):
        pedidas = set(cenarios[0].requisitos) & set(MEDIDAS_DE_PROFUNDIDADE)
        validas = _validas_do_grupo(linhas, cenarios)
        if not pedidas or not validas:
            continue
        n = cenarios[0].jogadores

        def rng(medida: int, grupo: int = indice) -> np.random.Generator:
            return rng_da_analise(experimento.semente_mestre, FLUXO_DA_PROFUNDIDADE + grupo, medida)

        linha: dict[str, Any] = {
            "cenario": nome,
            "jogadores": n,
            "partidas": len(validas),
            "defesas_por_jogador": _media(np.array([v["testes"] / n for v in validas], dtype=np.float64), rng(0)),
        }
        if ESCOLHAS in pedidas and all(v.get("decisoes_com_escolha") is not None for v in validas):
            linha["decisoes_com_escolha"] = _media(
                np.array([sum(v["decisoes_com_escolha"]) / n for v in validas], dtype=np.float64), rng(1)
            )
            avaliadas = np.array([sum(v["decisoes_avaliadas"]) for v in validas], dtype=np.float64)
            if all(v.get("decisoes_apertadas") is not None for v in validas) and avaliadas.sum() > 0:
                apertadas = np.array([sum(v["decisoes_apertadas"]) for v in validas], dtype=np.float64)
                linha["escolhas_apertadas"] = {
                    "valor": float(apertadas.sum() / avaliadas.sum()),
                    "intervalo": intervalo_da_razao(apertadas, avaliadas, rng(2)),
                }
        if VIRADAS in pedidas and all(v.get("trocas_de_lider") is not None for v in validas):
            linha["trocas_de_lider"] = _media(
                np.array([v["trocas_de_lider"] for v in validas], dtype=np.float64), rng(3)
            )
            lider = amostra_do_lider(validas)
            if lider.size:
                linha["recuperacao"] = _complemento(_media(lider, rng(4)))
        if DEGRAUS in pedidas and any(bot.rotulo == "foco" for bot in cenarios[0].bots):
            foco = amostra_do_foco(linhas, cenarios)
            if foco.size:
                linha["foco_sobre_1_n"] = _escalado(_media(foco, rng(5)), n)
        resultado.append(linha)
    return resultado

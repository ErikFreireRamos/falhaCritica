"""Aleatoriedade derivada por contador.

Cada sorteio usa um gerador novo, derivado de (semente mestre, índice da
partida, fluxo, contador). Consequências:

- o resultado de uma partida não depende de quantas rodaram antes nem em que
  processo (o paralelismo não muda nada);
- o fluxo do jogo (baralhos, dado) é separado do fluxo de cada bot, então trocar
  um bot não muda a ordem das cartas;
- o contador do fluxo do jogo fica dentro do estado da partida, o que mantém
  ``aplicar`` como função pura e permite refazer a partida a partir de qualquer
  evento.
"""

from __future__ import annotations

import numpy as np

FLUXO_JOGO = 0


def fluxo_do_bot(assento: int) -> int:
    """Fluxo de aleatoriedade do bot sentado em ``assento``."""
    return assento + 1


def gerador(semente: int, partida: int, fluxo: int, contador: int = 0) -> np.random.Generator:
    """Gerador determinístico para um sorteio (ou para a vida de um bot)."""
    sequencia = np.random.SeedSequence(entropy=semente, spawn_key=(partida, fluxo, contador))
    return np.random.Generator(np.random.PCG64(sequencia))


def chance_por_mil(probabilidade: float) -> int:
    """Converte uma probabilidade em inteiro de 0 a 1000.

    Os sorteios dos bots comparam inteiros, nunca ponto flutuante, para o
    resultado ser idêntico em qualquer plataforma.
    """
    if not 0.0 <= probabilidade <= 1.0:
        raise ValueError(f"probabilidade fora de [0, 1]: {probabilidade}")
    return round(probabilidade * 1000)

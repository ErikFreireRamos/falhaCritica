"""Bot Aleatório: escolhe uniformemente entre as ações legais.

Dois pontos não são escolha entre ações e dependem de hipóteses de modelo:

- MOD-01: se a explicação dada numa defesa está correta. É sorteado com a
  probabilidade ``explicacao_correta``.
- MOD-02: o julgamento como Auditor. O bot vê se a explicação está correta e
  acerta o veredito com a probabilidade ``precisao_auditor``.

Os valores da Fase 1 foram decididos pelo autor em 2026-11-09 e são provisórios:
explicação correta em 50% das defesas e Auditor que sempre julga certo.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import numpy as np

from critical_failure.bots.base import Decisao
from critical_failure.nucleo.rng import chance_por_mil, fluxo_do_bot, gerador
from critical_failure.observacao import Observacao
from critical_failure.regras.v2 import acoes as A
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.acoes import Acao

MIL = 1000


class BotAleatorio:
    tipo = "aleatorio"

    def __init__(self, explicacao_correta: float = 0.5, precisao_auditor: float = 1.0) -> None:
        self._explicacao = explicacao_correta
        self._precisao = precisao_auditor
        self._explicacao_por_mil = chance_por_mil(explicacao_correta)
        self._precisao_por_mil = chance_por_mil(precisao_auditor)
        self._rng: np.random.Generator | None = None

    def parametros(self) -> dict[str, Any]:
        return {"explicacao_correta": self._explicacao, "precisao_auditor": self._precisao}

    def iniciar(self, semente: int, partida: int, assento: int) -> None:
        self._rng = gerador(semente, partida, fluxo_do_bot(assento))

    def _sortear(self, limite: int) -> int:
        if self._rng is None:
            raise RuntimeError("o bot precisa de iniciar() antes de decidir")
        return int(self._rng.integers(limite))

    def decidir(self, observacao: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        if observacao.decisao_pedida == E.CONFERIR:
            return self._julgar(observacao)
        indice = self._sortear(len(opcoes))
        acao = opcoes[indice]
        motivo = f"aleatório: opção {indice + 1} de {len(opcoes)}"
        if acao.tipo == A.DEFENDER:
            sorteio = self._sortear(MIL)
            correta = sorteio < self._explicacao_por_mil
            acao = acao.com_explicacao(correta)
            motivo += (
                f"; explicação {'correta' if correta else 'incorreta'}"
                f" (p={self._explicacao_por_mil}/{MIL}, sorteio={sorteio})"
            )
        return Decisao(acao, motivo)

    def _julgar(self, observacao: Observacao) -> Decisao:
        disputa = observacao.disputa
        if disputa is None or disputa.explicacao_percebida is None:
            raise RuntimeError("pedido de conferência sem explicação para julgar")
        sorteio = self._sortear(MIL)
        acertou = sorteio < self._precisao_por_mil
        confere = disputa.explicacao_percebida if acertou else not disputa.explicacao_percebida
        motivo = (
            f"Auditor: a explicação estava {'correta' if disputa.explicacao_percebida else 'incorreta'}; "
            f"julgou {'certo' if acertou else 'errado'} (precisão={self._precisao_por_mil}/{MIL}, sorteio={sorteio})"
        )
        return Decisao(Acao(A.CONFERE if confere else A.NAO_CONFERE), motivo)

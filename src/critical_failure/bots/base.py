"""Contrato dos bots.

Um bot recebe a ``Observacao`` do seu assento e a lista de ações legais, e
devolve a ação escolhida com o motivo. Ele nunca vê nem altera o estado da
partida.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Protocol

from critical_failure.observacao import Observacao
from critical_failure.regras.v2.acoes import Acao

if TYPE_CHECKING:
    from critical_failure.bots.mesa import MesaPublica


@dataclass(frozen=True, slots=True)
class Decisao:
    acao: Acao
    motivo: str
    """Explicação curta da escolha, gravada no registro de auditoria."""


class Bot(Protocol):
    tipo: str

    def parametros(self) -> dict[str, Any]:
        """Parâmetros do bot, gravados no cabeçalho do registro."""
        ...

    def iniciar(self, semente: int, partida: int, assento: int, mesa: MesaPublica | None = None) -> None:
        """Prepara o bot para uma partida, com o seu próprio fluxo de aleatoriedade.

        ``mesa`` traz o que um jogador sabe antes de jogar: regras, Cartão de
        Referência e composição do baralho. Nunca traz o estado da partida.
        """
        ...

    def decidir(self, observacao: Observacao, opcoes: Sequence[Acao]) -> Decisao: ...

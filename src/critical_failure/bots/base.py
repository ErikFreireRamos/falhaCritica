"""Contrato dos bots.

Um bot recebe a ``Observacao`` do seu assento e a lista de ações legais, e
devolve a ação escolhida com o motivo. Ele nunca vê nem altera o estado da
partida.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Protocol

from critical_failure.regras.v1.acoes import AcaoV1
from critical_failure.regras.v2.acoes import Acao

if TYPE_CHECKING:
    from critical_failure.bots.mesa import MesaPublica, MesaPublicaV1


@dataclass(frozen=True, slots=True)
class Decisao:
    acao: Acao | AcaoV1
    motivo: str
    """Explicação curta da escolha, gravada no registro de auditoria."""


class Bot(Protocol):
    tipo: str

    def parametros(self) -> dict[str, Any]:
        """Parâmetros do bot, gravados no cabeçalho do registro."""
        ...

    def iniciar(
        self, semente: int, partida: int, assento: int, mesa: MesaPublica | MesaPublicaV1 | None = None
    ) -> None:
        """Prepara o bot para uma partida, com o seu próprio fluxo de aleatoriedade.

        ``mesa`` traz o que um jogador sabe antes de jogar: regras, Cartão de
        Referência e composição do baralho. Nunca traz o estado da partida.
        """
        ...

    def decidir(self, observacao: Any, opcoes: Sequence[Any]) -> Decisao:
        """Recebe a observação da família do motor (``Observacao`` ou ``ObservacaoV1``) e as ações legais."""
        ...

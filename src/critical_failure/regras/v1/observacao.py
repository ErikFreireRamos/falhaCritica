"""O que um jogador da v1 vê.

Público: quantas cartas cada um tem na mão e no sistema, as cartas que a mesa
sabe estarem num sistema (reveladas numa contestação ou recebidas numa defesa,
até a próxima retirada ao acaso daquele sistema), o descarte, o andamento da
disputa e o histórico dos testes. Privado: a própria mão e o próprio sistema.
Oculto de todos: a ordem do baralho.
"""

from __future__ import annotations

from dataclasses import dataclass

from critical_failure.regras.v1.config import CatalogoV1
from critical_failure.regras.v1.estado import DisputaEncerradaV1, EstadoV1


@dataclass(frozen=True, slots=True)
class JogadorVistoV1:
    assento: int
    cartas_na_mao: int
    cartas_no_sistema: int
    reveladas: tuple[str, ...]
    testes_feitos: int


@dataclass(frozen=True, slots=True)
class DisputaVistaV1:
    atacante: int
    defensor: int
    carta: str
    atributo: str
    etapa: str
    declarou_tem: bool | None
    duvidou: bool


@dataclass(frozen=True, slots=True)
class ObservacaoV1:
    assento: int
    n_jogadores: int
    fase: str
    vez: int
    decisao_pedida: str | None
    mao: tuple[str, ...]
    sistema: tuple[str, ...]
    jogadores: tuple[JogadorVistoV1, ...]
    descarte: tuple[str, ...]
    cartas_no_baralho: int
    disputa: DisputaVistaV1 | None
    historico: tuple[DisputaEncerradaV1, ...]


def observar_v1(estado: EstadoV1, assento: int, catalogo: CatalogoV1) -> ObservacaoV1:
    eu = estado.jogadores[assento]
    d = estado.disputa
    disputa = None
    if d is not None:
        disputa = DisputaVistaV1(
            d.atacante, d.defensor, catalogo.cartas[d.carta], d.atributo, d.etapa, d.declarou_tem, d.duvidou
        )
    pendente = estado.pendente
    return ObservacaoV1(
        assento=assento,
        n_jogadores=estado.n,
        fase=estado.fase,
        vez=estado.vez,
        decisao_pedida=pendente.tipo if pendente is not None and pendente.jogador == assento else None,
        mao=tuple(catalogo.nomes(eu.mao)),
        sistema=tuple(catalogo.nomes(eu.sistema)),
        jogadores=tuple(
            JogadorVistoV1(
                assento=j,
                cartas_na_mao=len(jogador.mao),
                cartas_no_sistema=len(jogador.sistema),
                reveladas=tuple(sorted(catalogo.nomes(jogador.reveladas))),
                testes_feitos=jogador.testes_feitos,
            )
            for j, jogador in enumerate(estado.jogadores)
        ),
        descarte=tuple(catalogo.nomes(estado.descarte)),
        cartas_no_baralho=len(estado.baralho),
        disputa=disputa,
        historico=estado.historico,
    )

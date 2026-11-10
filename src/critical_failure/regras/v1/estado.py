"""Estado de uma partida da v1. Imutável, como na família v2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from critical_failure.regras.v2.estado import Pendente

# Fases
PREPARACAO = "preparacao"
MONTAGEM = "montagem"
TESTES = "testes"
FIM = "fim"

# Decisões que o motor pode pedir
MONTAR = "montar"
TESTAR = "testar"
DECLARAR = "declarar"
DUVIDAR = "duvidar"
CONTESTAR = "contestar"

# Resultados de um teste
FALHA = "falha_encontrada"
DEFESA = "defesa_bem_sucedida"
CRITICAL_FAILURE = "critical_failure"
CONTESTOU_VERDADE = "contestou_verdade"
CONTESTOU_BLEFE = "contestou_blefe"

__all__ = ["Pendente"]


@dataclass(frozen=True, slots=True)
class JogadorV1:
    mao: tuple[int, ...]
    sistema: tuple[int, ...]
    reveladas: tuple[int, ...]
    """Cartas do sistema que a mesa sabe com certeza que estão lá."""
    testes_feitos: int
    pontos: int


@dataclass(frozen=True, slots=True)
class DisputaV1:
    atacante: int
    defensor: int
    carta: int
    atributo: str
    etapa: str
    declarou_tem: bool | None = None
    explicacao_correta: bool | None = None
    duvidou: bool = False
    carta_entregue: bool = False
    """A carta de ataque já foi para o sistema do defensor (defesa bem-sucedida)."""


@dataclass(frozen=True, slots=True)
class DisputaEncerradaV1:
    """O que a mesa viu de um teste já resolvido."""

    atacante: int
    defensor: int
    teste_do_ataque: str
    atributo: str
    declarou_tem: bool | None
    duvidou: bool
    contestou: bool
    resultado: str


@dataclass(frozen=True, slots=True)
class EstadoV1:
    semente: int
    partida: int
    contador_rng: int
    jogadores: tuple[JogadorV1, ...]
    baralho: tuple[int, ...]
    descarte: tuple[int, ...]
    fase: str
    vez: int
    pendente: Pendente | None
    disputa: DisputaV1 | None
    historico: tuple[DisputaEncerradaV1, ...]
    vencedores: tuple[int, ...]

    @property
    def n(self) -> int:
        return len(self.jogadores)

    @property
    def rodada(self) -> int:
        """Rodada de testes em andamento: 1 até todos terem testado uma vez, e assim por diante."""
        if self.fase in (PREPARACAO, MONTAGEM):
            return 0
        return min(jogador.testes_feitos for jogador in self.jogadores) + 1


@dataclass(frozen=True, slots=True)
class EventoV1:
    """Um fato da partida, com o estado logo depois dele. Mesmos campos do evento da família v2."""

    tipo: str
    regra: str
    ciclo: int
    """Na v1 não há ciclos: aqui vai a rodada de testes (0 na preparação)."""
    fase: str
    ator: int | None
    publico: dict[str, Any]
    oculto: dict[str, Any]
    visivel_para: dict[str, list[int]]
    amb: str | None
    estado: EstadoV1

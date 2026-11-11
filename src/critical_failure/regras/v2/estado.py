"""Estado de uma partida da família v2.

Tudo é imutável. Cartas são números (posição no catálogo); categorias e testes
são nomes. O estado contém também o contador de aleatoriedade do jogo, para que
``aplicar`` seja uma função pura.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from critical_failure.nucleo.canonico import OMITIR_SE_PADRAO

# Fases
PREPARACAO = "preparacao"
PLANEJAMENTO = "planejamento"
HOMOLOGACAO = "homologacao"
PRODUCAO = "producao"
CRITICAL_FAILURE = "critical_failure"
FIM = "fim"

# Decisões que o motor pode pedir a um jogador
COMPRAR = "comprar"
COLOCAR = "colocar"
AGIR = "agir"
RESPONDER = "responder"
CONFERIR = "conferir"
CONTESTAR = "contestar"
PALPITAR = "palpitar"
DIAGNOSTICAR = "diagnosticar"
LICAO = "licao"

# Resultados de uma disputa (R-7.3.1 a R-7.3.4)
FALHOU = "falhou"
ACEITA = "aceita"
CONTESTOU_VERDADE = "contestou_verdade"
CONTESTOU_BLEFE = "contestou_blefe"


@dataclass(frozen=True, slots=True)
class Jogador:
    fichas: int
    mao: tuple[int, ...]
    sistema: tuple[int, ...]
    alertas: tuple[str, ...]
    """Categorias com cubo de Alerta, na ordem do catálogo."""
    reveladas: tuple[int, ...]
    """Cartas do sistema que a mesa já viu (contestação ou Produção)."""
    pegas_do_backlog: tuple[int, ...]
    """Cartas que a mesa viu o jogador pegar do Backlog e que ele ainda tem."""
    passou: bool
    acertos: int
    """Diagnósticos certos, pela categoria-chave (R-8.0.8)."""


@dataclass(frozen=True, slots=True)
class Disputa:
    atacante: int
    defensor: int
    auditor: int
    carta: int
    categoria: str
    etapa: str
    teste_nomeado: str | None = None
    explicacao_correta: bool | None = None
    veredito: str | None = None
    palpites: tuple[tuple[int, bool], ...] = field(default=(), metadata={OMITIR_SE_PADRAO: True})
    """VAR-06: (votante, votou blefe) do palpite da plateia. Fica fora do hash enquanto vazio."""


@dataclass(frozen=True, slots=True)
class DisputaEncerrada:
    """O que a mesa viu de uma disputa já resolvida."""

    ciclo: int
    atacante: int
    defensor: int
    auditor: int
    categoria: str
    teste_do_ataque: str
    teste_nomeado: str | None
    veredito: str | None
    contestou: bool
    resultado: str


@dataclass(frozen=True, slots=True)
class Pendente:
    tipo: str
    jogador: int


@dataclass(frozen=True, slots=True)
class Estado:
    semente: int
    partida: int
    contador_rng: int
    jogadores: tuple[Jogador, ...]
    baralho: tuple[int, ...]
    """O topo é a posição 0."""
    descarte: tuple[int, ...]
    backlog: tuple[int, ...]
    linha_do_tempo: tuple[str, ...]
    """Incidentes que ainda não entraram no Radar. Depois deles vem o Critical Failure."""
    agora: str | None
    proximo: str | None
    """``None`` na vaga Próximo significa Critical Failure (R-4.13)."""
    resolvidos: tuple[str, ...]
    ciclo: int
    fase: str
    primeiro: int
    auditor: int
    pendente: Pendente | None
    compras_restantes: int
    disputa: Disputa | None
    diagnosticos: tuple[str | None, ...]
    fila_da_licao: tuple[int, ...]
    historico: tuple[DisputaEncerrada, ...]
    vencedores: tuple[int, ...]

    @property
    def n(self) -> int:
        return len(self.jogadores)


@dataclass(frozen=True, slots=True)
class Evento:
    """Um fato da partida, com o estado logo depois dele."""

    tipo: str
    regra: str
    ciclo: int
    fase: str
    ator: int | None
    publico: dict[str, Any]
    oculto: dict[str, Any]
    visivel_para: dict[str, list[int]]
    """Para cada campo de ``oculto``, quem pode vê-lo. Campo ausente: ninguém."""
    amb: str | None
    estado: Estado

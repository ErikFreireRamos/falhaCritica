"""Laço de uma partida: motor, bots e, se pedido, um ouvinte de eventos.

O ouvinte recebe cada evento na ordem, com a decisão do bot que o causou. É
assim que o registro de auditoria é escrito, sem que o motor saiba dele.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Any

from critical_failure.bots.base import Bot
from critical_failure.nucleo.erros import ErroCF
from critical_failure.observacao import observar
from critical_failure.regras.v2 import invariantes
from critical_failure.regras.v2.estado import Estado, Evento
from critical_failure.regras.v2.motor import FONTES, MotorV2

LIMITE_DE_PASSOS = 100_000
"""Guarda do simulador contra laço infinito. Não é número de regra."""

Ouvinte = Callable[[Evento, dict[str, Any] | None], None]


class PartidaSemFim(ErroCF):
    """A partida passou do limite de passos sem terminar."""


@dataclass(frozen=True, slots=True)
class ResultadoPartida:
    n_jogadores: int
    placar: tuple[int, ...]
    vencedores: tuple[int, ...]
    criterio: str
    """Como o vencedor foi definido: fichas, alertas, diagnosticos ou dividida."""
    fontes: tuple[dict[str, int], ...]
    """Para cada assento, o saldo de fichas por fonte."""
    eventos: int
    estado_final: Estado


def somar_fontes(fontes: list[dict[str, int]], evento: Evento) -> None:
    fichas = evento.publico.get("fichas")
    if fichas:
        fonte = evento.publico["fonte"]
        for assento, variacao in fichas.items():
            fontes[int(assento)][fonte] += variacao


def jogar_partida(
    motor: MotorV2,
    bots: Sequence[Bot],
    semente: int,
    partida: int,
    ouvinte: Ouvinte | None = None,
    conferir_invariantes: bool = False,
) -> ResultadoPartida:
    n = len(bots)
    for assento, bot in enumerate(bots):
        bot.iniciar(semente, partida, assento)
    fontes: list[dict[str, int]] = [dict.fromkeys(FONTES, 0) for _ in range(n)]
    total = 0
    criterio = ""

    def entregar(eventos: list[Evento], decisao: dict[str, Any] | None) -> None:
        nonlocal total, criterio
        for posicao, evento in enumerate(eventos):
            if conferir_invariantes:
                ultimo = posicao == len(eventos) - 1
                invariantes.conferir(evento.estado, motor.regras, motor.catalogo, em_repouso=ultimo)
            somar_fontes(fontes, evento)
            if evento.tipo == "fim_de_jogo":
                criterio = evento.publico["criterio"]
            if ouvinte is not None:
                ouvinte(evento, decisao if posicao == 0 else None)
        total += len(eventos)

    estado, eventos = motor.preparar(n, semente, partida)
    entregar(eventos, None)
    for _ in range(LIMITE_DE_PASSOS):
        pendente = estado.pendente
        if pendente is None:
            break
        opcoes = motor.acoes_legais(estado)
        decisao = bots[pendente.jogador].decidir(observar(estado, pendente.jogador, motor.catalogo), opcoes)
        estado, eventos = motor.aplicar(estado, decisao.acao)
        entregar(
            eventos,
            {
                "opcoes": [opcao.texto() for opcao in opcoes],
                "escolha": decisao.acao.texto(),
                "acao": decisao.acao.para_dict(),
                "motivo": decisao.motivo,
            },
        )
    else:
        raise PartidaSemFim(f"partida {partida} não terminou em {LIMITE_DE_PASSOS} passos")

    return ResultadoPartida(
        n_jogadores=n,
        placar=tuple(jogador.fichas for jogador in estado.jogadores),
        vencedores=estado.vencedores,
        criterio=criterio,
        fontes=tuple(fontes),
        eventos=total,
        estado_final=estado,
    )

"""Cria bots a partir do tipo e dos parâmetros gravados num registro ou num experimento."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.bots.base import Bot
from critical_failure.nucleo.erros import ConfiguracaoInvalida

TIPOS: dict[str, Callable[..., Bot]] = {BotAleatorio.tipo: BotAleatorio}
"""Tipos de bot conhecidos. Os próximos entram aqui na Fase 2."""


def criar_bot(tipo: str, parametros: dict[str, Any] | None = None) -> Bot:
    if tipo not in TIPOS:
        raise ConfiguracaoInvalida(f"tipo de bot desconhecido: {tipo!r}. Conhecidos: {sorted(TIPOS)}")
    try:
        return TIPOS[tipo](**(parametros or {}))
    except (TypeError, ValueError) as erro:
        raise ConfiguracaoInvalida(f"parâmetros inválidos para o bot {tipo!r}: {erro}") from erro

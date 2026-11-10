"""Cria bots a partir do tipo e dos parâmetros gravados num registro ou num experimento.

Num experimento, os perfis podem vir pelo nome (``conhecimento: experiente``,
``blefe: metade``); a fábrica troca o nome pelos valores de
``configs/perfis.yaml``. O bot criado guarda só os valores resolvidos, e é isso
que o registro de auditoria grava: a partida pode ser refeita mesmo que o
arquivo de perfis mude depois.
"""

from __future__ import annotations

from collections.abc import Callable
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.bots.base import Bot
from critical_failure.bots.estrategicos import BotCacador, BotConstrutor, BotHeuristico
from critical_failure.nucleo.erros import ConfiguracaoInvalida

PERFIS = Path(__file__).resolve().parents[3] / "configs" / "perfis.yaml"

TIPOS: dict[str, Callable[..., Bot]] = {
    BotAleatorio.tipo: BotAleatorio,
    BotConstrutor.tipo: BotConstrutor,
    BotCacador.tipo: BotCacador,
    BotHeuristico.tipo: BotHeuristico,
}
ESTILOS = (BotConstrutor.tipo, BotCacador.tipo, BotHeuristico.tipo)


@lru_cache(maxsize=1)
def perfis() -> dict[str, Any]:
    try:
        dados = yaml.safe_load(PERFIS.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as erro:
        raise ConfiguracaoInvalida(f"não foi possível ler {PERFIS}: {erro}") from erro
    if not isinstance(dados, dict) or dados.get("esquema") != "cf-perfis/1":
        raise ConfiguracaoInvalida(f"{PERFIS} não é um arquivo cf-perfis/1")
    return dados


def resolver(tipo: str, parametros: dict[str, Any] | None) -> dict[str, Any]:
    """Troca os nomes de perfil pelos valores. Valores já resolvidos passam direto."""
    resolvidos = dict(parametros or {})
    if tipo not in ESTILOS:
        return resolvidos
    tabela = perfis()
    for campo in ("conhecimento", "blefe"):
        valor = resolvidos.get(campo)
        if isinstance(valor, str):
            if valor not in tabela[campo]:
                raise ConfiguracaoInvalida(f"perfil de {campo} desconhecido: {valor!r}. Há: {sorted(tabela[campo])}")
            perfil = tabela[campo][valor]
            resolvidos[campo] = dict(perfil) if isinstance(perfil, dict) else perfil
    if tipo == BotHeuristico.tipo:
        for campo, valor in tabela["heuristico"].items():
            resolvidos.setdefault(campo, valor)
    return resolvidos


def criar_bot(tipo: str, parametros: dict[str, Any] | None = None) -> Bot:
    if tipo not in TIPOS:
        raise ConfiguracaoInvalida(f"tipo de bot desconhecido: {tipo!r}. Conhecidos: {sorted(TIPOS)}")
    resolvidos = resolver(tipo, parametros)
    try:
        return TIPOS[tipo](**resolvidos)
    except (TypeError, ValueError) as erro:
        raise ConfiguracaoInvalida(f"parâmetros inválidos para o bot {tipo!r}: {erro}") from erro


def rotulo(tipo: str, parametros: dict[str, Any] | None) -> str:
    """Nome curto de um bot para os relatórios, como ``cacador (lider)``."""
    parametros = parametros or {}
    if tipo == BotCacador.tipo and "alvo" in parametros:
        return f"{tipo} ({parametros['alvo']})"
    return tipo

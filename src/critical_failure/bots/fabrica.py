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
from critical_failure.bots.v1 import BotAleatorioV1, BotCacadorV1, BotConstrutorV1, BotHeuristicoV1
from critical_failure.nucleo.erros import ConfiguracaoInvalida

PERFIS = Path(__file__).resolve().parents[3] / "configs" / "perfis.yaml"

TIPOS: dict[str, Callable[..., Bot]] = {
    BotAleatorio.tipo: BotAleatorio,
    BotConstrutor.tipo: BotConstrutor,
    BotCacador.tipo: BotCacador,
    BotHeuristico.tipo: BotHeuristico,
}
TIPOS_V1: dict[str, Callable[..., Bot]] = {
    BotAleatorioV1.tipo: BotAleatorioV1,
    BotConstrutorV1.tipo: BotConstrutorV1,
    BotCacadorV1.tipo: BotCacadorV1,
    BotHeuristicoV1.tipo: BotHeuristicoV1,
}
"""Os mesmos estilos, traduzidos para a v1 (decisão do autor em 2026-11-10)."""
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


def criar_bot(tipo: str, parametros: dict[str, Any] | None = None, familia: str = "v2") -> Bot:
    """Cria o bot do tipo pedido para a família de regras (``v2`` ou ``v1``)."""
    tabela = {"v2": TIPOS, "v1": TIPOS_V1}.get(familia)
    if tabela is None:
        raise ConfiguracaoInvalida(f"família de regras desconhecida: {familia!r}")
    if tipo not in tabela:
        raise ConfiguracaoInvalida(f"tipo de bot desconhecido na {familia}: {tipo!r}. Conhecidos: {sorted(tabela)}")
    resolvidos = resolver(tipo, parametros)
    try:
        return tabela[tipo](**resolvidos)
    except (TypeError, ValueError) as erro:
        raise ConfiguracaoInvalida(f"parâmetros inválidos para o bot {tipo!r}: {erro}") from erro


def rotulo(tipo: str, parametros: dict[str, Any] | None) -> str:
    """Nome curto de um bot para os relatórios, como ``cacador (lider)``."""
    parametros = parametros or {}
    if tipo == BotCacador.tipo and "alvo" in parametros:
        return f"{tipo} ({parametros['alvo']})"
    return tipo

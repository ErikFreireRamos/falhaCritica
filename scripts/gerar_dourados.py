"""Gera os registros de referência ("dourados") e as narrações de exemplo.

Uso:
    uv run python scripts/gerar_dourados.py

Os dourados ficam em tests/dourados/. Um teste refaz cada partida e exige os
mesmos bytes, no Windows e no Linux: é a prova de que o simulador é
determinístico entre plataformas. Só gere de novo quando uma mudança de regra
ou de formato for intencional, e registre o motivo no diário.

As narrações de docs/exemplos/ saem dos mesmos registros.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from critical_failure.auditoria import registro
from critical_failure.auditoria.narrar import narrar
from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.bots.fabrica import criar_bot
from critical_failure.duracao import carregar_duracao
from critical_failure.regras.familias import Motor, carregar_motor

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "tests" / "dourados"
EXEMPLOS = RAIZ / "docs" / "exemplos"
DATA = "2026-11-09T00:00:00+00:00"
SEMENTE = 2026

# nome, arquivo de regras, jogadores, partida, tem narração de exemplo
CASOS: list[tuple[str, str, int, int, bool]] = [
    ("v2_2_1_com_4_jogadores", "regras_v2_2_1.yaml", 4, 0, True),
    ("v2_2_1_com_5_jogadores", "regras_v2_2_1.yaml", 5, 1, True),
    ("v2_2_impressa_com_6_jogadores", "regras_v2_2.yaml", 6, 2, False),
    ("v2_2_1_estilos_mistos", "regras_v2_2_1.yaml", 4, 3, True),
    ("v1_estilos_mistos_6_jogadores", "regras_v1.yaml", 6, 4, True),
]

_COMUM = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}
BOTS_DO_CASO: dict[str, list[tuple[str, dict[str, Any]]]] = {
    "v2_2_1_estilos_mistos": [
        ("construtor", _COMUM),
        ("cacador", {**_COMUM, "alvo": "lider"}),
        ("heuristico", _COMUM),
        ("aleatorio", {"explicacao_correta": 0.85, "precisao_auditor": 0.95}),
    ],
    "v1_estilos_mistos_6_jogadores": [
        ("aleatorio", {"explicacao_correta": 0.85, "precisao_auditor": 0.95}),
        ("construtor", _COMUM),
        ("cacador", {**_COMUM, "alvo": "lider"}),
        ("cacador", {**_COMUM, "alvo": "mais_fraco"}),
        ("cacador", {**_COMUM, "alvo": "aleatorio"}),
        ("heuristico", _COMUM),
    ],
}
"""Casos com bots de estilo. Os outros usam o bot Aleatório com os parâmetros da Fase 1."""


def linhas_do_caso(arquivo: str, jogadores: int, partida: int, nome: str = "") -> tuple[list[dict[str, Any]], Motor]:
    motor = carregar_motor(RAIZ / "configs" / arquivo)
    if nome in BOTS_DO_CASO:
        bots: list[Any] = [criar_bot(tipo, parametros, motor.familia) for tipo, parametros in BOTS_DO_CASO[nome]]
    else:
        bots = [BotAleatorio() for _ in range(jogadores)]
    # O modelo de duração (MOD-05) só existe para a família v2.
    duracao = carregar_duracao(RAIZ / "configs" / "duracao.yaml") if motor.familia == "v2" else None
    linhas, _ = registro.gerar_linhas(
        motor, f"configs/{arquivo}", bots, SEMENTE, partida, data_hora=DATA, duracao=duracao
    )
    # O commit muda a cada versão do código; o dourado não pode depender dele.
    linhas[0]["git"] = {"commit": None, "sujo": None}
    return linhas, motor


def narracao_do_caso(arquivo: str, jogadores: int, partida: int, nome: str = "") -> str:
    linhas, motor = linhas_do_caso(arquivo, jogadores, partida, nome)
    return narrar(linhas, motor.catalogo, mostrar_oculto=True, citar_regras=False)


def main() -> int:
    for nome, arquivo, jogadores, partida, com_narracao in CASOS:
        linhas, _ = linhas_do_caso(arquivo, jogadores, partida, nome)
        registro.escrever(PASTA / f"{nome}.jsonl", linhas)
        print(f"escrito tests/dourados/{nome}.jsonl ({len(linhas) - 2} eventos)")
        if com_narracao:
            EXEMPLOS.mkdir(parents=True, exist_ok=True)
            destino = EXEMPLOS / f"narracao_{nome}.txt"
            destino.write_text(narracao_do_caso(arquivo, jogadores, partida, nome), encoding="utf-8", newline="\n")
            print(f"escrito docs/exemplos/{destino.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

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
from critical_failure.duracao import carregar_duracao
from critical_failure.regras.config import carregar_jogo
from critical_failure.regras.v2.motor import MotorV2

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
]


def linhas_do_caso(arquivo: str, jogadores: int, partida: int) -> tuple[list[dict[str, Any]], MotorV2]:
    regras, catalogo = carregar_jogo(RAIZ / "configs" / arquivo)
    motor = MotorV2(regras, catalogo)
    bots = [BotAleatorio() for _ in range(jogadores)]
    duracao = carregar_duracao(RAIZ / "configs" / "duracao.yaml")
    linhas, _ = registro.gerar_linhas(
        motor, f"configs/{arquivo}", bots, SEMENTE, partida, data_hora=DATA, duracao=duracao
    )
    # O commit muda a cada versão do código; o dourado não pode depender dele.
    linhas[0]["git"] = {"commit": None, "sujo": None}
    return linhas, motor


def narracao_do_caso(arquivo: str, jogadores: int, partida: int) -> str:
    linhas, motor = linhas_do_caso(arquivo, jogadores, partida)
    return narrar(linhas, motor.catalogo, mostrar_oculto=True, citar_regras=False)


def main() -> int:
    for nome, arquivo, jogadores, partida, com_narracao in CASOS:
        linhas, _ = linhas_do_caso(arquivo, jogadores, partida)
        registro.escrever(PASTA / f"{nome}.jsonl", linhas)
        print(f"escrito tests/dourados/{nome}.jsonl ({len(linhas) - 2} eventos)")
        if com_narracao:
            EXEMPLOS.mkdir(parents=True, exist_ok=True)
            destino = EXEMPLOS / f"narracao_{nome}.txt"
            destino.write_text(narracao_do_caso(arquivo, jogadores, partida), encoding="utf-8", newline="\n")
            print(f"escrito docs/exemplos/{destino.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

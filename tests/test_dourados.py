"""Registros de referência: a mesma partida precisa gerar os mesmos bytes em qualquer plataforma."""

from __future__ import annotations

import gerar_dourados
import pytest

from critical_failure.auditoria import registro, replay
from critical_failure.nucleo.canonico import json_canonico

CASOS = [pytest.param(*caso, id=caso[0]) for caso in gerar_dourados.CASOS]


@pytest.mark.parametrize("nome, arquivo, jogadores, partida, com_narracao", CASOS)
def test_partida_refeita_bate_byte_a_byte_com_o_dourado(
    nome: str, arquivo: str, jogadores: int, partida: int, com_narracao: bool
) -> None:
    caminho = gerar_dourados.PASTA / f"{nome}.jsonl"
    gravado = caminho.read_bytes()
    assert b"\r" not in gravado, "o dourado precisa ter fim de linha LF"
    linhas, _ = gerar_dourados.linhas_do_caso(arquivo, jogadores, partida)
    refeito = "".join(json_canonico(linha) + "\n" for linha in linhas).encode("utf-8")
    assert refeito == gravado, (
        f"a partida {nome} não gera mais o mesmo registro. Se a mudança foi intencional, "
        "rode scripts/gerar_dourados.py e registre o motivo no diário."
    )


@pytest.mark.parametrize("nome, arquivo, jogadores, partida, com_narracao", CASOS)
@pytest.mark.parametrize("modo", replay.MODOS)
def test_replay_do_dourado(
    nome: str, arquivo: str, jogadores: int, partida: int, com_narracao: bool, modo: str
) -> None:
    linhas = registro.ler(gerar_dourados.PASTA / f"{nome}.jsonl")
    assert linhas[0]["jogadores"] == jogadores
    assert replay.refazer(linhas, modo).eventos == linhas[-1]["eventos"]


@pytest.mark.parametrize("nome, arquivo, jogadores, partida, com_narracao", CASOS)
def test_narracao_de_exemplo_esta_em_dia(
    nome: str, arquivo: str, jogadores: int, partida: int, com_narracao: bool
) -> None:
    if not com_narracao:
        pytest.skip("caso sem narração de exemplo")
    caminho = gerar_dourados.EXEMPLOS / f"narracao_{nome}.txt"
    assert caminho.read_text(encoding="utf-8") == gerar_dourados.narracao_do_caso(arquivo, jogadores, partida)

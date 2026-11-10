"""Registro de auditoria de uma partida (esquema ``cf-audit/1``).

Um arquivo JSONL por partida:

- 1ª linha, ``cabecalho``: tudo o que é preciso para refazer a partida (versão
  do motor, commit, regras resolvidas e o seu hash, semente, bots).
- uma linha ``evento`` por evento, com ``publico`` e ``oculto`` separados, a
  regra que o justificou e o hash do estado depois dele.
- última linha, ``fim``: placar por fonte, vencedor e critério de desempate.

Toda linha é JSON canônico, então a mesma partida gera os mesmos bytes em
qualquer plataforma. Só ``data_hora`` e ``git`` do cabeçalho variam.
"""

from __future__ import annotations

import subprocess
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import critical_failure
from critical_failure.bots.base import Bot
from critical_failure.duracao import ModeloDeDuracao
from critical_failure.nucleo.canonico import como_dict, json_canonico, sha256
from critical_failure.nucleo.erros import ErroCF, RegistroDivergente
from critical_failure.partida import ResultadoPartida, jogar_partida
from critical_failure.regras.familias import Motor

ESQUEMA = "cf-audit/1"
RAIZ = Path(__file__).resolve().parents[3]
PASTA_CONFIGS = RAIZ / "configs"

CABECALHO = "cabecalho"
EVENTO = "evento"
FIM = "fim"

Linha = dict[str, Any]


def info_git() -> dict[str, Any]:
    """Commit atual e se há alteração não commitada. ``None`` fora de um repositório."""
    try:
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=RAIZ, capture_output=True, text=True, check=True
        ).stdout.strip()
        estado = subprocess.run(
            ["git", "status", "--porcelain"], cwd=RAIZ, capture_output=True, text=True, check=True
        ).stdout
        return {"commit": commit, "sujo": bool(estado.strip())}
    except (OSError, subprocess.CalledProcessError):
        return {"commit": None, "sujo": None}


def montar_cabecalho(
    motor: Motor,
    arquivo_de_regras: str,
    bots: Sequence[Bot],
    semente: int,
    partida: int,
    data_hora: str,
    duracao: ModeloDeDuracao | None = None,
) -> Linha:
    regras = motor.regras
    return {
        "registro": CABECALHO,
        "esquema": ESQUEMA,
        "motor": critical_failure.__version__,
        "git": info_git(),
        "regras": {
            "versao": regras.versao,
            "familia": regras.familia,
            "correcoes": list(regras.correcoes),
            "arquivo": arquivo_de_regras,
            "texto": regras.texto,
        },
        "config": regras.resolvida(),
        "config_hash": regras.hash(),
        "catalogo_hash": motor.catalogo.hash,
        "semente_mestre": semente,
        "partida": partida,
        "jogadores": len(bots),
        "bots": [
            {"assento": assento, "tipo": bot.tipo, "parametros": bot.parametros()} for assento, bot in enumerate(bots)
        ],
        # Hipóteses de modelo que não são regra do jogo (MOD-05).
        "modelos": {"duracao": duracao.resolvido() if duracao is not None else None},
        "data_hora": data_hora,
    }


def linha_do_evento(seq: int, evento: Any, decisao: dict[str, Any] | None) -> Linha:
    oculto = dict(evento.oculto)
    if oculto:
        oculto["visivel_para"] = evento.visivel_para
    linha: Linha = {
        "registro": EVENTO,
        "seq": seq,
        "ciclo": evento.ciclo,
        "fase": evento.fase,
        "tipo": evento.tipo,
        "ator": evento.ator,
        "regra": evento.regra,
        "publico": evento.publico,
        "oculto": oculto,
        "estado_hash": sha256(como_dict(evento.estado)),
    }
    if evento.amb is not None:
        linha["amb"] = evento.amb
    if decisao is not None:
        linha["decisao"] = decisao
    return linha


def linha_do_fim(resultado: ResultadoPartida) -> Linha:
    return {
        "registro": FIM,
        "placar": {"final": list(resultado.placar), "por_fonte": list(resultado.fontes)},
        "vencedores": list(resultado.vencedores),
        "criterio_de_desempate": resultado.criterio,
        "invariantes": "ok",
        "eventos": resultado.eventos,
        "duracao_estimada_s": resultado.duracao_s,  # MOD-05; None quando a partida roda sem modelo de duração
        "estado_hash_final": sha256(como_dict(resultado.estado_final)),
    }


def linha_de_falha(erro: Exception, eventos: int) -> Linha:
    return {
        "registro": FIM,
        "placar": None,
        "vencedores": [],
        "criterio_de_desempate": None,
        "invariantes": f"falha: {type(erro).__name__}: {erro}",
        "eventos": eventos,
        "duracao_estimada_s": None,
        "estado_hash_final": None,
    }


def gerar_linhas(
    motor: Motor,
    arquivo_de_regras: str,
    bots: Sequence[Bot],
    semente: int,
    partida: int,
    data_hora: str | None = None,
    duracao: ModeloDeDuracao | None = None,
) -> tuple[list[Linha], ResultadoPartida]:
    """Joga a partida no modo auditado e devolve todas as linhas do registro.

    Se a partida falhar, a exceção sai com as linhas já geradas no atributo
    ``linhas``, terminadas por um ``fim`` que descreve a falha.
    """
    momento = data_hora or datetime.now(UTC).isoformat(timespec="seconds")
    linhas: list[Linha] = [montar_cabecalho(motor, arquivo_de_regras, bots, semente, partida, momento, duracao)]

    def ouvinte(evento: Any, decisao: dict[str, Any] | None) -> None:
        linhas.append(linha_do_evento(len(linhas) - 1, evento, decisao))

    try:
        resultado = jogar_partida(
            motor, bots, semente, partida, ouvinte=ouvinte, conferir_invariantes=True, duracao=duracao
        )
    except ErroCF as erro:
        linhas.append(linha_de_falha(erro, len(linhas) - 1))
        erro.linhas = linhas  # type: ignore[attr-defined]
        raise
    linhas.append(linha_do_fim(resultado))
    return linhas, resultado


def escrever(caminho: Path, linhas: Sequence[Linha]) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8", newline="\n") as arquivo:
        for linha in linhas:
            arquivo.write(json_canonico(linha) + "\n")


def gravar_partida(
    caminho: Path,
    motor: Motor,
    arquivo_de_regras: str,
    bots: Sequence[Bot],
    semente: int,
    partida: int,
    data_hora: str | None = None,
    duracao: ModeloDeDuracao | None = None,
) -> ResultadoPartida:
    """Joga e grava. Partida que falha também é gravada, e a exceção segue adiante."""
    try:
        linhas, resultado = gerar_linhas(motor, arquivo_de_regras, bots, semente, partida, data_hora, duracao)
    except ErroCF as erro:
        escrever(caminho, getattr(erro, "linhas", []))
        raise
    escrever(caminho, linhas)
    return resultado


def ler(caminho: Path) -> list[Linha]:
    import json

    try:
        texto = caminho.read_text(encoding="utf-8")
        linhas = [json.loads(bruta) for bruta in texto.splitlines() if bruta.strip()]
    except (OSError, ValueError) as erro:
        raise RegistroDivergente(f"não foi possível ler o registro {caminho}: {erro}") from erro
    formato_ok = (
        len(linhas) >= len((CABECALHO, FIM))
        and all(isinstance(linha, dict) for linha in linhas)
        and linhas[0].get("registro") == CABECALHO
        and linhas[0].get("esquema") == ESQUEMA
        and linhas[-1].get("registro") == FIM
    )
    if not formato_ok:
        raise RegistroDivergente(f"{caminho} não é um registro {ESQUEMA} completo")
    return linhas

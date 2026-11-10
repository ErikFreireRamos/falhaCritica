"""Exporta a Folha de registro de uma partida (R-REG.1 a R-REG.3).

São os campos que o observador anota em sala, para que partidas simuladas e
reais sejam comparadas com o mesmo esquema. Três arquivos CSV, um por bloco da
Folha (decisão do autor em 2026-11-09):

- ``diagnosticos.csv``: o diagnóstico de cada jogador em cada incidente;
- ``defesas.csv``: cada defesa na Homologação;
- ``fichas.csv``: as fichas finais de cada jogador.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from critical_failure.auditoria.narrar import nome
from critical_failure.auditoria.registro import EVENTO, Linha

COLUNAS_DIAGNOSTICOS = [
    "ciclo",
    "incidente",
    "assento",
    "jogador",
    "era_auditor",
    "categoria_escolhida",
    "classificacao",
    "acertou",
]
COLUNAS_DEFESAS = [
    "ciclo",
    "ordem",
    "atacante",
    "defensor",
    "auditor",
    "categoria_atacada",
    "teste_do_ataque",
    "resposta",
    "teste_nomeado",
    "era_blefe",
    "decisao_do_auditor",
    "houve_contestacao",
    "resultado",
]
COLUNAS_FICHAS = ["assento", "jogador", "fichas_finais", "venceu"]

SIM, NAO = "sim", "nao"


def _sim_nao(valor: bool) -> str:
    return SIM if valor else NAO


def extrair(linhas: list[Linha]) -> dict[str, list[dict[str, Any]]]:
    """Monta as três tabelas da Folha a partir das linhas do registro."""
    diagnosticos: list[dict[str, Any]] = []
    defesas: list[dict[str, Any]] = []
    auditor_do_ciclo: int | None = None
    incidente = ""
    disputa: dict[str, Any] = {}

    for ev in linhas:
        if ev.get("registro") != EVENTO:
            continue
        tipo, p, o = ev["tipo"], ev["publico"], ev["oculto"]
        if tipo == "relato_lido":
            auditor_do_ciclo, incidente = ev["ator"], p["incidente"]
        elif tipo == "diagnostico_pontuado":
            diagnosticos.append(
                {
                    "ciclo": ev["ciclo"],
                    "incidente": incidente,
                    "assento": ev["ator"],
                    "jogador": nome(ev["ator"]),
                    "era_auditor": _sim_nao(ev["ator"] == auditor_do_ciclo),
                    "categoria_escolhida": p["escolha"],
                    "classificacao": p["classificacao"],
                    "acertou": _sim_nao(p["classificacao"] == "chave"),
                }
            )
        elif tipo == "teste":
            disputa = {
                "ciclo": ev["ciclo"],
                "ordem": len(defesas) + 1,
                "atacante": nome(p["atacante"]),
                "defensor": nome(p["defensor"]),
                "auditor": nome(p["auditor_da_disputa"]),
                "categoria_atacada": p["categoria"],
                "teste_do_ataque": p["teste"],
                "resposta": "",
                "teste_nomeado": "",
                "era_blefe": "",
                "decisao_do_auditor": "",
                "houve_contestacao": NAO,
                "resultado": "",
            }
        elif tipo == "defesa":
            disputa["resposta"] = p["resposta"]
            disputa["teste_nomeado"] = p.get("teste_nomeado", "")
            if "blefe" in o:
                disputa["era_blefe"] = _sim_nao(o["blefe"])
        elif tipo == "conferencia":
            disputa["decisao_do_auditor"] = p["veredito"]
        elif tipo == "contestacao":
            disputa["houve_contestacao"] = SIM
        elif tipo == "fim_da_disputa":
            disputa["resultado"] = p["resultado"]
            defesas.append(disputa)
            disputa = {}

    fim = linhas[-1]
    placar = (fim.get("placar") or {}).get("final") or []
    fichas = [
        {
            "assento": assento,
            "jogador": nome(assento),
            "fichas_finais": total,
            "venceu": _sim_nao(assento in fim.get("vencedores", [])),
        }
        for assento, total in enumerate(placar)
    ]
    return {"diagnosticos": diagnosticos, "defesas": defesas, "fichas": fichas}


def exportar(linhas: list[Linha], pasta: Path, prefixo: str) -> list[Path]:
    """Escreve os três CSVs em ``pasta`` e devolve os caminhos."""
    tabelas = extrair(linhas)
    colunas = {"diagnosticos": COLUNAS_DIAGNOSTICOS, "defesas": COLUNAS_DEFESAS, "fichas": COLUNAS_FICHAS}
    pasta.mkdir(parents=True, exist_ok=True)
    escritos: list[Path] = []
    for tabela, registros in tabelas.items():
        caminho = pasta / f"{prefixo}_{tabela}.csv"
        with caminho.open("w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas[tabela], lineterminator="\n")
            escritor.writeheader()
            escritor.writerows(registros)
        escritos.append(caminho)
    return escritos

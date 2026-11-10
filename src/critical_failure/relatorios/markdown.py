"""Relatório de um experimento em Markdown.

O relatório é refeito a partir do manifest e da tabela de partidas (``cf
relatorio``), então todo número dele é rastreável até a execução que o gerou.
"""

from __future__ import annotations

from typing import Any

from critical_failure.metricas.estatistica import pior
from critical_failure.metricas.requisitos import Medida


def _num(valor: float, casas: int = 3) -> str:
    return f"{valor:.{casas}f}".replace(".", ",")


def _faixa(faixa: tuple[float, float] | None, casas: int = 3) -> str:
    if faixa is None:
        return "—"
    return f"{_num(faixa[0], casas)} a {_num(faixa[1], casas)}"


def _pct(valor: float) -> str:
    return f"{100 * valor:.1f}%".replace(".", ",")


def renderizar(manifest: dict[str, Any], medidas: list[Medida], descricoes: list[dict[str, Any]]) -> str:
    experimento = manifest["experimento"]["conteudo"]
    git = manifest["git"]
    commit = (git["commit"] or "sem git")[:7]
    estado_do_git = "árvore limpa" if git["sujo"] is False else "COM ALTERAÇÕES NÃO COMMITADAS"
    linhas = [
        f"# Relatório do experimento `{experimento['nome']}`",
        "",
        experimento["descricao"].strip(),
        "",
        "| Item | Valor |",
        "|---|---|",
        f"| Arquivo | `{manifest['experimento']['arquivo']}` |",
        f"| Commit | `{commit}` ({estado_do_git}) |",
        f"| Execução oficial | {'sim' if manifest['oficial'] else 'não'} |",
        f"| Semente mestre | {manifest['semente_mestre']} |",
        f"| Partidas | {manifest['partidas']} |",
        f"| Falhas | {manifest['falhas']} |",
        f"| Registros completos gravados | {manifest['registros_completos']} |",
        f"| Início | {manifest['inicio']} |",
        "",
        "## Requisitos",
        "",
        "Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; "
        "**falha** se está inteiro fora; **inconclusivo** se cruza a borda. "
        "As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.",
        "",
    ]
    if not medidas:
        linhas += ["Nenhum requisito confirmado foi medido neste experimento.", ""]
    for requisito in sorted({medida.requisito for medida in medidas}):
        do_requisito = [medida for medida in medidas if medida.requisito == requisito]
        casas = 1 if requisito == "REQ-08" else 3
        linhas += [
            f"### {requisito}: {pior([medida.veredito for medida in do_requisito])}",
            "",
            "| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |",
            "|---|---|---|---|---|---|---|",
        ]
        for medida in do_requisito:
            valor = str(int(medida.valor)) if medida.intervalo is None else _num(medida.valor, casas)
            linhas.append(
                f"| {medida.cenario} | {medida.o_que} | {valor} | {_faixa(medida.intervalo, casas)} | "
                f"{_faixa(medida.zona, casas)} | {medida.partidas} | {medida.veredito} |"
            )
        notas = sorted({medida.nota for medida in do_requisito if medida.nota})
        linhas += ["", *[f"Nota: {nota}." for nota in notas], ""] if notas else [""]

    linhas += [
        "## Descrição das partidas",
        "",
        "Números sem critério de aceite. Dependem de como os bots jogam.",
        "",
        "| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | "
        "Partidas com reembaralhamento | Partidas em que faltou carta | Fichas do vencedor | Fichas médias | "
        "Duração p10 / mediana / p90 (min) |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for d in descricoes:
        if "testes_por_partida" not in d:
            linhas.append(f"| {d['cenario']} | {d['partidas']} | {d['falhas']} | — | — | — | — | — | — | — | — |")
            continue
        linhas.append(
            f"| {d['cenario']} | {d['partidas']} | {d['falhas']} | {_num(d['testes_por_partida'], 1)} | "
            f"{_num(d['contestacoes_por_partida'], 1)} | {_pct(d['vitorias_divididas'])} | "
            f"{_pct(d['partidas_com_reembaralhamento'])} | {_pct(d['partidas_com_compra_impossivel'])} | "
            f"{_num(d['fichas_do_vencedor'], 1)} | {_num(d['fichas_medias'], 1)} | "
            f"{_num(d['duracao_p10'], 1)} / {_num(d['duracao_mediana'], 1)} / {_num(d['duracao_p90'], 1)} |"
        )
    linhas += [
        "",
        "## Cenários",
        "",
        "| Cenário | Regras | Jogadores | Bots | Hash da configuração |",
        "|---|---|---|---|---|",
    ]
    for cenario in manifest["cenarios"]:
        bots = sorted({f"{bot['tipo']} {bot['parametros']}" for bot in cenario["bots"]})
        mudancas = f" com {cenario['mudancas']}" if cenario["mudancas"] else ""
        linhas.append(
            f"| {cenario['nome']} | {cenario['versao']}{mudancas} | {cenario['jogadores']} | {'; '.join(bots)} | "
            f"`{cenario['config_hash'][:19]}` |"
        )
    linhas += [
        "",
        "## Como refazer",
        "",
        f"No commit `{commit}`: `{manifest['comando'] or 'cf experimento ' + manifest['experimento']['arquivo']}`. "
        "O resultado não depende do número de processos.",
        "",
    ]
    return "\n".join(linhas)

"""Relatório de um experimento em Markdown.

O relatório é refeito a partir do manifest e da tabela de partidas (``cf
relatorio``), então todo número dele é rastreável até a execução que o gerou.
"""

from __future__ import annotations

import math
from typing import Any

from critical_failure.metricas.analise import Analise
from critical_failure.metricas.estatistica import pior
from critical_failure.metricas.matrizes import MatrizDeEstilos


def _num(valor: float, casas: int = 3) -> str:
    return f"{valor:.{casas}f}".replace(".", ",")


def _faixa(faixa: tuple[float, float] | None, casas: int = 3) -> str:
    if faixa is None:
        return "—"
    return f"{_num(faixa[0], casas)} a {_num(faixa[1], casas)}"


def _pct(valor: float) -> str:
    return f"{100 * valor:.1f}%".replace(".", ",")


def _blefes(descricao: dict[str, Any]) -> str:
    por_partida = descricao.get("blefes_por_partida")
    if por_partida is None:
        return "—"
    sucesso = descricao.get("blefes_bem_sucedidos")
    return f"{_num(por_partida, 2)} ({'—' if sucesso is None else _pct(sucesso)})"


def _matriz_de_alvos(manifest: dict[str, Any], estilos: list[dict[str, Any]]) -> list[str]:
    """MET-02: a taxa de vitória do bot "foco" em cada célula (política do foco x política dos outros)."""
    celulas = {
        cenario["grupo"]: cenario["celula"]
        for cenario in manifest["cenarios"]
        if cenario.get("celula") is not None and not cenario.get("matriz")
    }
    if not celulas:
        return []
    do_foco = {e["grupo"]: e for e in estilos if e["bot"] == "foco" and e["grupo"] in celulas}
    linhas_da_matriz = list(dict.fromkeys(celula[0] for celula in celulas.values()))
    colunas = list(dict.fromkeys(celula[1] for celula in celulas.values()))
    saida = [
        "## Política de alvo (MET-02)",
        "",
        "Sem veredito. Taxa de vitória de 1 bot (o foco) que usa a política da linha, numa mesa em que todos os "
        "outros usam a política da coluna. Rodízio de assentos. Referência de quem não leva vantagem: 1/N.",
        "",
        "| Foco \\ Outros | " + " | ".join(colunas) + " |",
        "|---|" + "---|" * len(colunas),
    ]
    for linha in linhas_da_matriz:
        celulas_da_linha = []
        for coluna in colunas:
            grupo = next((g for g, c in celulas.items() if c == [linha, coluna]), None)
            estilo = do_foco.get(grupo or "")
            celulas_da_linha.append(
                "—" if estilo is None else f"{_num(estilo['taxa'])} ({_faixa(estilo['intervalo'])})"
            )
        saida.append(f"| {linha} | " + " | ".join(celulas_da_linha) + " |")
    referencias = sorted({e["referencia"] for e in do_foco.values()})
    saida += ["", "Referência 1/N: " + ", ".join(_num(r) for r in referencias) + ".", ""]
    return saida


def _matrizes_de_estilos(matrizes: list[MatrizDeEstilos]) -> list[str]:
    """MET-07 e REQ-04: a matriz de cada tamanho de mesa, as melhores respostas e a dinâmica do replicador."""
    if not matrizes:
        return []
    saida = [
        "## Matrizes de ganhos entre estilos ou perfis (MET-07 e REQ-04)",
        "",
        "Taxa de vitória de 1 bot do estilo ou perfil da linha (o foco) numa mesa em que os outros N-1 são do da "
        "coluna, com rodízio de assentos. Na diagonal o foco joga contra bots iguais a ele e vence exatamente 1/N. "
        "Em negrito, as melhores respostas a cada mesa: as linhas que nenhuma outra supera com clareza (intervalo "
        "de 95% da diferença inteiro acima da diferença mínima do REQ-04).",
        "",
    ]
    for matriz in matrizes:
        saida += [
            f"### {matriz.nome} ({matriz.jogadores} jogadores, referência 1/N = {_num(1 / matriz.jogadores)})",
            "",
            "| Foco \\ Mesa | " + " | ".join(matriz.estilos) + " |",
            "|---|" + "---|" * len(matriz.estilos),
        ]
        for foco in matriz.estilos:
            celulas = []
            for mesa in matriz.estilos:
                celula = matriz.celulas.get((foco, mesa))
                if celula is None:
                    texto = "não rodada"
                elif celula.intervalo is None:
                    texto = f"{_num(celula.taxa)} (1/N)"
                else:
                    texto = f"{_num(celula.taxa)} ({_faixa(celula.intervalo)})"
                if foco in matriz.melhores_respostas.get(mesa, ()):
                    texto = f"**{texto}**"
                celulas.append(texto)
            saida.append(f"| {foco} | " + " | ".join(celulas) + " |")
        if not matriz.completa:
            saida += ["", "Matriz incompleta: sem análise de dominância nem dinâmica do replicador.", ""]
            continue
        saida += ["", "| Estilo | Situação (REQ-04) | Por quê |", "|---|---|---|"]
        saida += [f"| {e} | {matriz.situacao[e]} | {matriz.motivo[e]} |" for e in matriz.estilos]
        mistura = ", ".join(
            f"{estilo} {_num(proporcao)}"
            for estilo, proporcao in sorted(matriz.replicador.items(), key=lambda item: (-item[1], item[0]))
            if proporcao >= 0.0005
        )
        parada = (
            "é um equilíbrio: ali nenhuma linha se sai melhor que a média"
            if matriz.replicador_convergiu
            else "não é um equilíbrio: a dinâmica não parou ou parou num ponto que outra linha invade"
        )
        saida += [
            "",
            "Dinâmica do replicador (sem veredito; aproximação linear, tempo contínuo com passo pequeno, a partir "
            f"da população uniforme): {mistura} ({parada}).",
            "",
        ]
        if matriz.populacoes:
            saida += [
                "Mesas de perfis iguais (REQ-05: blefes bem-sucedidos divididos por blefes tentados).",
                "",
                "| Perfil | Partidas | Blefes por partida | Bem-sucedidos | IC 95% |",
                "|---|---|---|---|---|",
            ]
            for populacao in matriz.populacoes:
                taxa = "—" if populacao.taxa_de_sucesso is None else _num(populacao.taxa_de_sucesso)
                saida.append(
                    f"| {populacao.estilo} | {populacao.partidas} | {_num(populacao.blefes_por_partida, 2)} | "
                    f"{taxa} | {_faixa(populacao.intervalo)} |"
                )
            saida.append("")
    return saida


def renderizar(manifest: dict[str, Any], analise: Analise) -> str:
    medidas = analise.medidas
    descricoes = analise.descricoes
    estilos = analise.estilos
    desequilibrio = analise.desequilibrio
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
        *(
            [
                f"| Relatório refeito | com o código do commit `{(refeito['commit'] or 'sem git')[:7]}`"
                f"{' (com alterações não commitadas)' if refeito['sujo'] else ''} em {refeito['data']}; "
                "a execução e a tabela de partidas são as do commit acima |"
            ]
            if (refeito := manifest.get("relatorio_refeito"))
            else []
        ),
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
        casas = 1 if requisito in ("REQ-08", "REQ-10") else 3
        linhas += [
            f"### {requisito}: {pior([medida.veredito for medida in do_requisito])}",
            "",
            "| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |",
            "|---|---|---|---|---|---|---|",
        ]
        for medida in do_requisito:
            if math.isnan(medida.valor):
                valor = "—"
            else:
                valor = str(int(medida.valor)) if medida.intervalo is None else _num(medida.valor, casas)
            linhas.append(
                f"| {medida.cenario} | {medida.o_que} | {valor} | {_faixa(medida.intervalo, casas)} | "
                f"{_faixa(medida.zona, casas)} | {medida.partidas} | {medida.veredito} |"
            )
        notas = sorted({medida.nota for medida in do_requisito if medida.nota})
        linhas += ["", *[f"Nota: {nota}." for nota in notas], ""] if notas else [""]

    if estilos:
        linhas += [
            "## Taxa de vitória por bot (MET-07)",
            "",
            "Sem veredito. Cada assento conta 1 na vitória, 1/k numa "
            "vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. "
            "As rotações do rodízio estão somadas.",
            "",
            "| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |",
            "|---|---|---|---|---|---|---|",
        ]
        for estilo in sorted(estilos, key=lambda e: (e["grupo"], -e["taxa"])):
            linhas.append(
                f"| {estilo['grupo']} | {estilo['bot']} | {estilo['jogadores']} | {estilo['assentos_jogados']} | "
                f"{_num(estilo['taxa'])} | {_faixa(estilo['intervalo'])} | {_num(estilo['referencia'])} |"
            )
        linhas.append("")

    matriz = _matriz_de_alvos(manifest, estilos or [])
    if matriz:
        linhas += matriz
    linhas += _matrizes_de_estilos(analise.matrizes)

    if desequilibrio:
        linhas += [
            "## Partidas desequilibradas (MET-01)",
            "",
            "Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. "
            "O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são "
            "análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903). "
            "Na v2 é só descrição: o placar em fichas não está na mesma escala dos pontos da v1, e a comparação "
            "entre as versões é feita pelo REQ-02 (autor, 2026-11-10).",
            "",
            "| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |",
            "|---|---|---|---|---|---|---|",
        ]
        for d in desequilibrio:
            fator = f"**{_num(d['fator'], 2)}**" if d["principal"] else _num(d["fator"], 2)
            linhas.append(
                f"| {d['grupo']} | {d['familia']} | {d['jogadores']} | {d['partidas']} | {fator} | "
                f"{_num(d['proporcao'])} | {_faixa(d['intervalo'])} |"
            )
        linhas.append("")

    linhas += [
        "## Descrição das partidas",
        "",
        "Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em "
        "fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.",
        "",
        "| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | "
        "Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | "
        "Placar médio | Sistema cheio no 1º Planejamento | Blefes por partida (bem-sucedidos) | "
        "Duração p10 / mediana / p90 (min) |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for d in descricoes:
        if "testes_por_partida" not in d:
            linhas.append(
                f"| {d['cenario']} | {d['partidas']} | {d['falhas']} | — | — | — | — | — | — | — | — | — | — | — |"
            )
            continue
        cheios = d.get("sistemas_cheios_no_planejamento_1")
        linhas.append(
            f"| {d['cenario']} | {d['partidas']} | {d['falhas']} | {_num(d['testes_por_partida'], 1)} | "
            f"{_num(d['contestacoes_por_partida'], 1)} | {_pct(d['vitorias_divididas'])} | "
            f"{_pct(d['partidas_com_reembaralhamento'])} | {_pct(d['partidas_com_compra_impossivel'])} | "
            f"{'—' if d['vantagem_do_lider'] is None else _num(d['vantagem_do_lider'])} | "
            f"{_num(d['fichas_do_vencedor'], 1)} | {_num(d['fichas_medias'], 1)} | "
            f"{'—' if cheios is None else _pct(cheios)} | {_blefes(d)} | "
            + (
                "— |"
                if d["duracao_mediana"] is None
                else f"{_num(d['duracao_p10'], 1)} / {_num(d['duracao_mediana'], 1)} / {_num(d['duracao_p90'], 1)} |"
            )
        )
    if analise.interno:

        def talvez(valor: float | None, casas: int = 3) -> str:
            return "—" if valor is None else _num(valor, casas)

        linhas += [
            "",
            "## Equilíbrio dentro da partida (descrição)",
            "",
            "Números sem critério de aceite; os vereditos, quando pedidos, estão na seção de requisitos. Razão de "
            "testes: máximo sobre a média de testes recebidos na partida (REQ-06a). Contra o menor: fração dos "
            "testes contra quem tinha o menor placar (REQ-06b). Zeradas: partidas com alguém em 0 ficha antes do "
            "último ciclo (REQ-07). Parado: percentil 90 do tempo parado por jogador e ciclo, pelos tempos "
            "provisórios do MOD-05 (REQ-10). Peso do dano: dano de incidente sobre as fichas movimentadas "
            "(REQ-13). Dispersão: placar do primeiro menos o do último no fim (REQ-14).",
            "",
            "| Cenário | Razão de testes | Contra o menor | Zeradas | Parado p90 (min) | Peso do dano | Dispersão |",
            "|---|---|---|---|---|---|---|",
        ]
        for d in analise.interno:
            linhas.append(
                f"| {d['cenario']} | {talvez(d['razao_de_testes'], 2)} | {talvez(d['contra_o_menor'])} | "
                f"{_pct(d['zeradas'])} | {talvez(d['parado_p90_min'], 1)} | {talvez(d['peso_do_dano'])} | "
                f"{_num(d['dispersao_final'], 1)} |"
            )
    linhas += [
        "",
        "## Cenários",
        "",
        "| Cenário | Regras | Jogadores | Bots | Hash da configuração |",
        "|---|---|---|---|---|",
    ]
    ja_listados: set[str] = set()
    for cenario in manifest["cenarios"]:
        nome = cenario["nome"]
        if cenario.get("matriz"):  # as rotações de uma célula de matriz aparecem numa linha só
            nome = cenario["grupo"]
            if nome in ja_listados:
                continue
            ja_listados.add(nome)
            nome = f"{nome} (rotações somadas)"
        bots = sorted({f"{bot['tipo']} {bot['parametros']}" for bot in cenario["bots"]})
        if cenario.get("pesos"):
            bots = [
                f"{bot['rotulo']} (peso {peso}): {bot['tipo']} {bot['parametros']}"
                for bot, peso in zip(cenario["bots"], cenario["pesos"], strict=True)
            ]
        mudancas = f" com {cenario['mudancas']}" if cenario["mudancas"] else ""
        linhas.append(
            f"| {nome} | {cenario['versao']}{mudancas} | {cenario['jogadores']} | {'; '.join(bots)} | "
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

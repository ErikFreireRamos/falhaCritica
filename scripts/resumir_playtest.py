"""Resumo agregado do questionário do playtest da v2.2 (com o módulo de Segurança Operacional).

O CSV fica só na máquina do autor (decisão de 2026-11-14): não vai para o git, e o TCC traz apenas
contagens agregadas, como o artigo do SBQS 2025. Este script refaz essas contagens.

Uso:
    uv run python scripts/resumir_playtest.py [caminho do CSV] [--latex]

Sem caminho, lê ``docs/Avaliação do jogo Critical Failure.csv``. Com ``--latex``, imprime também as
linhas da tabela de itens em formato LaTeX.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PADRAO = RAIZ / "docs" / "Avaliação do jogo Critical Failure.csv"

ESCALA = ("Discordo totalmente", "Discordo", "Nem concordo nem discordo", "Concordo", "Concordo totalmente")
"""Likert de 5 pontos, do menor para o maior."""
GRUPOS_LIKERT = ("Sobre o jogo [", "O jogo contribuiu para eu... [", "Sobre as regras do jogo [")
PERFIL = (
    "Qual é o seu curso?",
    "Em qual período você está?",
    "Você tem experiência profissional com teste de software (estágio ou trabalho)?",
    "Com que frequência você joga jogos de tabuleiro ou de cartas?",
    "Antes de jogar, como era o seu conhecimento sobre testes não funcionais?",
)
ESCOLHA_UNICA = ("A duração da partida foi:", "Qual parte das regras foi mais confusa?")
ESCOLHA_MULTIPLA = "Sobre a sua experiência com o jogo, marque todas as opções que se aplicam:"
ABERTAS = (
    "Qual teste ou categoria você mais confundiu durante a partida? Com qual outro?",
    "Cite até três pontos fortes do jogo.",
    "O que você mudaria no jogo?",
)


def ler(caminho: Path) -> list[dict[str, str]]:
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        return [{k.strip(): (v or "").strip() for k, v in linha.items()} for linha in csv.DictReader(arquivo)]


def item_curto(coluna: str) -> str:
    """O texto entre colchetes da pergunta Likert."""
    return coluna[coluna.index("[") + 1 : coluna.rindex("]")]


def resumo_likert(respostas: list[str]) -> dict[str, float | int]:
    contagem = Counter(respostas)
    validas = [r for r in respostas if r in ESCALA]
    notas = sorted(ESCALA.index(r) + 1 for r in validas)
    n = len(notas)
    mediana = (notas[(n - 1) // 2] + notas[n // 2]) / 2 if n else float("nan")
    return {
        **{rotulo: contagem.get(rotulo, 0) for rotulo in ESCALA},
        "n": n,
        "concordam": contagem.get("Concordo", 0) + contagem.get("Concordo totalmente", 0),
        "mediana": mediana,
    }


def main(argv: list[str]) -> int:
    latex = "--latex" in argv
    caminhos = [a for a in argv if not a.startswith("--")]
    caminho = Path(caminhos[0]) if caminhos else PADRAO
    if not caminho.exists():
        print(f"CSV não encontrado: {caminho}", file=sys.stderr)
        return 1
    linhas = ler(caminho)
    print(f"Respostas: {len(linhas)}")
    print(f"Consentimento: {dict(Counter(linha['Consentimento'] for linha in linhas))}")

    print("\n== Perfil")
    for pergunta in PERFIL:
        print(f"- {pergunta} {dict(sorted(Counter(linha[pergunta] for linha in linhas).items()))}")

    print("\n== Itens de 5 pontos (DT, D, N, C, CT; concordam; mediana de 1 a 5)")
    tabela_latex = []
    for coluna in linhas[0]:
        if not coluna.startswith(GRUPOS_LIKERT):
            continue
        r = resumo_likert([linha[coluna] for linha in linhas])
        contagens = " ".join(str(r[rotulo]) for rotulo in ESCALA)
        print(f"- {item_curto(coluna)} | {contagens} | {r['concordam']}/{r['n']} | {r['mediana']:.1f}")
        celulas = " & ".join(str(r[rotulo]) for rotulo in ESCALA)
        tabela_latex.append(f"{item_curto(coluna)} & {celulas} & {r['concordam']}/{r['n']} \\\\")

    print("\n== Escolha única")
    for pergunta in ESCOLHA_UNICA:
        print(f"- {pergunta} {dict(Counter(linha[pergunta] for linha in linhas).most_common())}")

    print("\n== Experiência (marque todas)")
    marcadas = Counter(op for linha in linhas for op in linha[ESCOLHA_MULTIPLA].split(";") if op.strip())
    for opcao, vezes in marcadas.most_common():
        print(f"- {opcao}: {vezes}")

    print("\n== Respostas abertas (para análise do autor; não publicar o CSV)")
    for pergunta in ABERTAS:
        textos = [
            " / ".join(parte.strip() for parte in linha[pergunta].splitlines() if parte.strip())
            for linha in linhas
            if linha[pergunta]
        ]
        print(f"- {pergunta} ({len(textos)} respostas)")
        for texto in textos:
            print(f"    * {texto}")

    if latex:
        print("\n== Linhas LaTeX")
        print("\n".join(tabela_latex))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

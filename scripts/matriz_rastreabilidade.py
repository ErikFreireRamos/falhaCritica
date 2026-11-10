"""Matriz de rastreabilidade: regra da especificação -> código -> testes.

Uso:
    uv run python scripts/matriz_rastreabilidade.py            # escreve docs/MATRIZ_RASTREABILIDADE.md
    uv run python scripts/matriz_rastreabilidade.py --conferir # só lista as regras sem teste

Para cada item da especificação da v2.2, lista onde o código o cita (eventos,
comentários e docstrings em src/) e quais testes estão marcados com
``@pytest.mark.regra("R-x.y")``. Itens dos tipos regra, definicao, componente e
revogada precisam de pelo menos um teste; sai com código 1 se algum não tiver.
"""

from __future__ import annotations

import ast
import re
import sys
from collections import defaultdict

from verificar_especificacao import ESPEC_V2, PADRAO_R, RAIZ, ler_tabelas

DESTINO = RAIZ / "docs" / "MATRIZ_RASTREABILIDADE.md"
TIPOS_COM_TESTE = {"regra", "definicao", "componente", "revogada"}
RE_REGRA = re.compile(rf"(?<![\w-])({PADRAO_R})(?![\w])")


def itens_da_especificacao() -> dict[str, tuple[str, str]]:
    """``{id: (tipo, texto)}`` de todas as tabelas de regras da especificação da v2.2."""
    itens: dict[str, tuple[str, str]] = {}
    for cabecalho, linhas in ler_tabelas(ESPEC_V2):
        if "ID" in cabecalho and "Tipo" in cabecalho and "Regra" in cabecalho:
            for linha in linhas:
                itens[linha["ID"]] = (linha["Tipo"], linha["Regra"])
    return itens


def testes_por_regra() -> dict[str, list[str]]:
    """Lê os decoradores ``@pytest.mark.regra(...)`` dos arquivos de teste."""
    achados: dict[str, list[str]] = defaultdict(list)
    for arquivo in sorted((RAIZ / "tests").glob("test_*.py")):
        arvore = ast.parse(arquivo.read_text(encoding="utf-8"))
        for no in ast.walk(arvore):
            if not isinstance(no, ast.FunctionDef) or not no.name.startswith("test_"):
                continue
            for decorador in no.decorator_list:
                if (
                    isinstance(decorador, ast.Call)
                    and isinstance(decorador.func, ast.Attribute)
                    and decorador.func.attr == "regra"
                ):
                    for argumento in decorador.args:
                        if isinstance(argumento, ast.Constant) and isinstance(argumento.value, str):
                            achados[argumento.value].append(f"{arquivo.name}::{no.name}")
    return achados


def codigo_por_regra() -> dict[str, list[str]]:
    """Onde cada regra é citada em src/ (arquivo:linha)."""
    achados: dict[str, list[str]] = defaultdict(list)
    for arquivo in sorted((RAIZ / "src").rglob("*.py")):
        relativo = arquivo.relative_to(RAIZ / "src" / "critical_failure").as_posix()
        for numero, linha in enumerate(arquivo.read_text(encoding="utf-8").splitlines(), start=1):
            for regra in RE_REGRA.findall(linha):
                achados[regra].append(f"{relativo}:{numero}")
    return achados


def sem_teste() -> list[str]:
    testes = testes_por_regra()
    return [
        ident
        for ident, (tipo, _) in itens_da_especificacao().items()
        if tipo in TIPOS_COM_TESTE and not testes.get(ident)
    ]


def marcas_desconhecidas() -> list[str]:
    """Regras citadas em testes que não existem na especificação."""
    itens = itens_da_especificacao()
    return sorted(regra for regra in testes_por_regra() if regra not in itens)


def _resumir(itens: list[str], limite: int) -> str:
    if not itens:
        return "—"
    mostrados = ", ".join(f"`{item}`" for item in itens[:limite])
    return mostrados + (f" e mais {len(itens) - limite}" if len(itens) > limite else "")


def renderizar() -> str:
    itens, testes, codigo = itens_da_especificacao(), testes_por_regra(), codigo_por_regra()
    exigem = [ident for ident, (tipo, _) in itens.items() if tipo in TIPOS_COM_TESTE]
    cobertos = [ident for ident in exigem if testes.get(ident)]
    linhas = [
        "# Matriz de rastreabilidade — v2.2.1",
        "",
        "Gerada por `scripts/matriz_rastreabilidade.py`. Não edite à mão.",
        "",
        "Para cada item de `docs/especificacao_v2_2.md`: onde o código o cita e quais testes o cobrem. "
        "Itens dos tipos `regra`, `definicao`, `componente` e `revogada` precisam de pelo menos um teste "
        "marcado com `@pytest.mark.regra`. Itens `mesa` e `nota` não são mecânica do motor.",
        "",
        f"**Cobertura:** {len(cobertos)} de {len(exigem)} itens que exigem teste têm pelo menos um.",
        "",
        "| ID | Tipo | Código | Testes | Situação |",
        "|---|---|---|---|---|",
    ]
    for ident, (tipo, _) in itens.items():
        nomes = sorted({nome.split("::")[1] for nome in testes.get(ident, [])})
        situacao = "coberta" if nomes else "**SEM TESTE**"
        if tipo not in TIPOS_COM_TESTE:
            situacao = "não exige teste"
        linhas.append(
            f"| {ident} | {tipo} | {_resumir(codigo.get(ident, []), 3)} | {_resumir(nomes, 2)} | {situacao} |"
        )
    return "\n".join(linhas) + "\n"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    faltam, desconhecidas = sem_teste(), marcas_desconhecidas()
    if "--conferir" not in sys.argv:
        DESTINO.write_text(renderizar(), encoding="utf-8", newline="\n")
        print(f"escrito {DESTINO.relative_to(RAIZ)}")
    exigem = [i for i, (tipo, _) in itens_da_especificacao().items() if tipo in TIPOS_COM_TESTE]
    print(f"{len(exigem) - len(faltam)} de {len(exigem)} itens que exigem teste estão cobertos")
    for ident in faltam:
        print(f"SEM TESTE: {ident}")
    for regra in desconhecidas:
        print(f"MARCA DESCONHECIDA num teste: {regra}")
    return 1 if faltam or desconhecidas else 0


if __name__ == "__main__":
    sys.exit(main())

"""Gera configs/catalogo_v2.yaml a partir das tabelas de docs/especificacao_v2_2.md.

Uso:
    uv run python scripts/gerar_catalogo.py            # escreve o arquivo
    uv run python scripts/gerar_catalogo.py --conferir # só confere se está em dia

A especificação é a fonte única das cartas de Teste e dos incidentes. O catálogo
YAML é derivado dela, para que o motor não dependa de ler Markdown. Um teste
automático roda este script com --conferir.
"""

from __future__ import annotations

import re
import sys

import yaml
from verificar_especificacao import ESPEC_V2, RAIZ, ler_tabelas

DESTINO = RAIZ / "configs" / "catalogo_v2.yaml"
CABECALHO = (
    "# Catálogo de cartas de Teste e de incidentes da família v2.\n"
    "# GERADO por scripts/gerar_catalogo.py a partir de docs/especificacao_v2_2.md.\n"
    "# Não edite à mão: mude a especificação e gere de novo.\n"
)


def _linha_da_regra(ident: str) -> dict[str, str]:
    for cabecalho, linhas in ler_tabelas(ESPEC_V2):
        if "ID" in cabecalho and "Regra" in cabecalho:
            for linha in linhas:
                if linha["ID"] == ident:
                    return linha
    raise SystemExit(f"regra {ident} não encontrada na especificação")


def montar() -> dict[str, object]:
    cartas: list[dict[str, str]] = []
    incidentes: list[dict[str, str]] = []
    relatos: dict[str, str] = {}
    for cabecalho, linhas in ler_tabelas(ESPEC_V2):
        if "Teste" in cabecalho and "Cópias" in cabecalho:
            cartas = linhas
        elif "Categoria-chave" in cabecalho:
            incidentes = linhas
        elif "Relato" in cabecalho:
            relatos = {linha["Incidente"]: linha["Relato"] for linha in linhas}

    # Faces do dado (R-2.0.15): "1 Desempenho; 2 Compatibilidade; ..."
    faces = re.findall(r"(\d) ([^;.]+)", _linha_da_regra("R-2.0.15")["Regra"].split(":", 1)[1])
    conjunto_da_categoria = {c["Categoria"]: c["Conjunto"] for c in cartas}
    categorias = [
        {"nome": nome.strip(), "face_do_dado": int(face), "conjunto": conjunto_da_categoria[nome.strip()]}
        for face, nome in faces
    ]

    testes = [
        {
            "regra": c["ID"],
            "nome": c["Teste"],
            "categoria": c["Categoria"],
            "copias": int(c["Cópias"]),
            "conjunto": c["Conjunto"],
            "nao_confundir": [n.strip() for n in c["Não confundir com"].split(";")],
            "descricao": c["Descrição"],
        }
        for c in cartas
    ]
    lista_incidentes = [
        {
            "regra": i["ID"],
            "numero": i["ID"].split(".")[1],
            "nome": i["Nome"],
            "chave": i["Categoria-chave"],
            "secundaria": None if i["Secundária"] == "—" else i["Secundária"],
            "testes_chave": [t.strip() for t in i["Testes-chave"].split(";")],
            "severo": i["Severo"] == "sim",
            "conjunto": i["Conjunto"],
            "relato": relatos[i["ID"].split(".")[1]],
        }
        for i in incidentes
    ]
    return {
        "esquema": "cf-catalogo/1",
        "familia": "v2",
        "categorias": categorias,
        "testes": testes,
        "incidentes": lista_incidentes,
    }


def renderizar() -> str:
    corpo = yaml.safe_dump(montar(), allow_unicode=True, sort_keys=False, width=100)
    return CABECALHO + corpo


def main() -> int:
    texto = renderizar()
    if "--conferir" in sys.argv:
        atual = DESTINO.read_text(encoding="utf-8") if DESTINO.exists() else ""
        if atual != texto:
            print("configs/catalogo_v2.yaml está diferente da especificação; gere de novo")
            return 1
        print("configs/catalogo_v2.yaml está em dia com a especificação")
        return 0
    DESTINO.write_text(texto, encoding="utf-8", newline="\n")
    dados = montar()
    print(f"escrito {DESTINO.relative_to(RAIZ)}: {len(dados['testes'])} testes, {len(dados['incidentes'])} incidentes")  # type: ignore[arg-type]
    return 0


if __name__ == "__main__":
    sys.exit(main())

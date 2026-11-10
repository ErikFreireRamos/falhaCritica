"""Confere a consistência interna dos documentos de especificação.

Uso:
    py -3.12 scripts/verificar_especificacao.py

Lê docs/especificacao_v2_2.md, docs/especificacao_v1.md, docs/AMBIGUIDADES.md e
configs/requisitos.yaml. Usa só a biblioteca padrão. Sai com código 1 se
encontrar algum erro.

O que é conferido:
  - identificadores bem formados e únicos;
  - toda regra com tipo válido e página dentro do documento de origem;
  - um mesmo parâmetro com o mesmo valor em todo lugar em que aparece;
  - catálogo de cartas: 63 cartas e 29 testes no jogo base, 9 por categoria,
    72 e 33 com o módulo, e os "não confundir com" apontando para testes reais;
  - catálogo de incidentes: 14 no jogo base, 2 por categoria, severos corretos,
    testes-chave da categoria-chave, um relato por incidente;
  - baralho da v1: 54 cartas, como na Tabela 3 do artigo;
  - cada ambiguidade com todos os campos e o resumo coerente com as entradas;
  - cada requisito com métrica, zona e estado;
  - toda referência cruzada apontando para um identificador que existe.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESPEC_V2 = RAIZ / "docs" / "especificacao_v2_2.md"
ESPEC_V1 = RAIZ / "docs" / "especificacao_v1.md"
AMBIGUIDADES = RAIZ / "docs" / "AMBIGUIDADES.md"
REQUISITOS = RAIZ / "configs" / "requisitos.yaml"

PADRAO_R = r"R-(?:\d+|[BC]|REG)(?:\.\d+){1,2}[a-z]?"
PADRAO_V1 = r"V1-(?:\d\.\d|T\d)\.\d+[a-z]?"
PADRAO_OUTROS = r"(?:AMB|REQ|MET|MOD|VAR|COR)-\d{2}"
RE_ID_R = re.compile(rf"^{PADRAO_R}$")
RE_ID_V1 = re.compile(rf"^{PADRAO_V1}$")
# O (?!\.<) evita casar com as formas genéricas da convenção, como R-B.0.<n>.
RE_REFERENCIA = re.compile(rf"(?<![\w-])({PADRAO_R}|{PADRAO_V1}|{PADRAO_OUTROS})(?![\w])(?!\.<)")
RE_PARAMETRO = re.compile(r"`([a-z0-9_.]+)=([^`]+)`")

TIPOS = {"regra", "definicao", "componente", "mesa", "nota", "evidencia", "revogada"}
PAGINAS = {"v2.2": 35, "v1": 9}

CATEGORIAS_BASE = [
    "Desempenho",
    "Compatibilidade",
    "Interação",
    "Confiabilidade",
    "Segurança da Informação",
    "Manutenibilidade",
    "Flexibilidade",
]
CATEGORIA_MODULO = "Segurança Operacional"
SEVEROS_ESPERADOS = {"R-C.07", "R-C.09", "R-C.13", "R-C.15"}
ATRIBUTOS_V1 = {
    "Eficiência de Desempenho": 9,
    "Compatibilidade": 6,
    "Confiabilidade": 9,
    "Segurança": 9,
    "Portabilidade": 9,
    "Usabilidade": 9,
    "Especial": 3,
}
CAMPOS_AMB = ["Regras", "Trecho", "Interpretações", "Sugestão", "Configuração", "Impacto", "Estado"]
CAMPOS_REQ = ["nome", "tipo", "fonte", "metrica", "zona", "estado"]
CAMPOS_MET = ["nome", "fonte", "metrica", "estado"]

erros: list[str] = []
avisos: list[str] = []


def erro(mensagem: str) -> None:
    erros.append(mensagem)


def ler_tabelas(caminho: Path) -> list[tuple[list[str], list[dict[str, str]]]]:
    """Devolve as tabelas Markdown do arquivo como (cabeçalho, linhas)."""
    tabelas: list[tuple[list[str], list[dict[str, str]]]] = []
    cabecalho: list[str] | None = None
    linhas: list[dict[str, str]] = []
    for numero, bruta in enumerate(caminho.read_text(encoding="utf-8").splitlines(), start=1):
        linha = bruta.strip()
        if not linha.startswith("|"):
            if cabecalho is not None:
                tabelas.append((cabecalho, linhas))
            cabecalho, linhas = None, []
            continue
        celulas = [c.strip() for c in linha.strip("|").split("|")]
        if cabecalho is None:
            cabecalho = celulas
            continue
        if all(set(c) <= set("-: ") for c in celulas):
            continue
        if len(celulas) != len(cabecalho):
            erro(f"{caminho.name}:{numero}: linha com {len(celulas)} colunas, esperado {len(cabecalho)}")
            continue
        linhas.append(dict(zip(cabecalho, celulas, strict=True)))
    if cabecalho is not None:
        tabelas.append((cabecalho, linhas))
    return tabelas


def conferir_regras(
    caminho: Path, versao: str, re_id: re.Pattern[str]
) -> tuple[dict[str, dict[str, str]], dict[str, set[str]]]:
    """Confere as tabelas de regras e devolve (regras por ID, valores por parâmetro)."""
    regras: dict[str, dict[str, str]] = {}
    parametros: dict[str, set[str]] = defaultdict(set)
    for cabecalho, linhas in ler_tabelas(caminho):
        if "Tipo" not in cabecalho or "Regra" not in cabecalho:
            continue
        for linha in linhas:
            ident = linha["ID"]
            if not re_id.match(ident):
                erro(f"{caminho.name}: identificador mal formado: {ident!r}")
            if ident in regras:
                erro(f"{caminho.name}: identificador repetido: {ident}")
            regras[ident] = linha
            if linha["Tipo"] not in TIPOS:
                erro(f"{caminho.name}: {ident} tem tipo desconhecido {linha['Tipo']!r}")
            if not linha["Regra"]:
                erro(f"{caminho.name}: {ident} está sem texto")
            pagina = linha["Pág."]
            if not pagina.isdigit() or not 1 <= int(pagina) <= PAGINAS[versao]:
                erro(f"{caminho.name}: {ident} tem página inválida {pagina!r}")
            for chave, valor in RE_PARAMETRO.findall(linha["Parâmetros"]):
                parametros[chave].add(valor)
    return regras, parametros


def conferir_parametros(parametros: dict[str, set[str]]) -> dict[str, str]:
    valores: dict[str, str] = {}
    for chave, vistos in sorted(parametros.items()):
        if len(vistos) > 1:
            erro(f"parâmetro {chave} aparece com valores diferentes: {sorted(vistos)}")
        valores[chave] = next(iter(vistos))
    return valores


def esperar(valores: dict[str, str], chave: str, calculado: int) -> None:
    declarado = valores.get(chave)
    if declarado is None:
        erro(f"parâmetro {chave} não foi declarado em nenhuma regra")
    elif declarado != str(calculado):
        erro(f"parâmetro {chave}={declarado}, mas o catálogo dá {calculado}")


def conferir_cartas(valores: dict[str, str]) -> dict[str, str]:
    """Confere o catálogo de cartas da v2.2 e devolve {teste: categoria}."""
    cartas: list[dict[str, str]] = []
    for cabecalho, linhas in ler_tabelas(ESPEC_V2):
        if "Teste" in cabecalho and "Cópias" in cabecalho:
            cartas = linhas
    if not cartas:
        erro("catálogo de cartas da v2.2 não encontrado")
        return {}

    categoria_de: dict[str, str] = {}
    copias_base: Counter[str] = Counter()
    copias_modulo: Counter[str] = Counter()
    ids: set[str] = set()
    for carta in cartas:
        ident, teste, categoria = carta["ID"], carta["Teste"], carta["Categoria"]
        if not RE_ID_R.match(ident) or ident in ids:
            erro(f"carta com identificador inválido ou repetido: {ident}")
        ids.add(ident)
        if teste in categoria_de:
            erro(f"teste repetido no catálogo: {teste}")
        categoria_de[teste] = categoria
        if not carta["Cópias"].isdigit():
            erro(f"{ident}: número de cópias inválido")
            continue
        if not carta["Pág."].isdigit() or not carta["Descrição"]:
            erro(f"{ident}: sem página ou sem descrição")
        if carta["Conjunto"] == "base":
            if categoria not in CATEGORIAS_BASE:
                erro(f"{ident}: categoria {categoria!r} não é do jogo base")
            copias_base[categoria] += int(carta["Cópias"])
        elif carta["Conjunto"] == "módulo":
            if categoria != CATEGORIA_MODULO:
                erro(f"{ident}: carta do módulo fora de {CATEGORIA_MODULO}")
            copias_modulo[categoria] += int(carta["Cópias"])
        else:
            erro(f"{ident}: conjunto desconhecido {carta['Conjunto']!r}")

    for carta in cartas:
        for nome in carta["Não confundir com"].split(";"):
            if nome.strip() not in categoria_de:
                erro(f"{carta['ID']}: 'não confundir com' cita teste inexistente: {nome.strip()!r}")

    testes_base = sum(1 for c in cartas if c["Conjunto"] == "base")
    testes_modulo = sum(1 for c in cartas if c["Conjunto"] == "módulo")
    total_base, total_modulo = sum(copias_base.values()), sum(copias_modulo.values())
    if set(copias_base) != set(CATEGORIAS_BASE):
        erro(f"categorias do jogo base no catálogo: {sorted(copias_base)}")
    por_categoria = int(valores.get("baralho.cartas_por_categoria", "0"))
    for categoria, total in sorted(copias_base.items()):
        if total != por_categoria:
            erro(f"categoria {categoria} tem {total} cartas, esperado {por_categoria}")
    esperar(valores, "baralho.cartas_base", total_base)
    esperar(valores, "baralho.testes_base", testes_base)
    esperar(valores, "baralho.cartas_modulo", total_modulo)
    esperar(valores, "baralho.testes_modulo", testes_modulo)
    esperar(valores, "baralho.cartas_com_modulo", total_base + total_modulo)
    esperar(valores, "baralho.testes_com_modulo", testes_base + testes_modulo)
    esperar(valores, "categorias.base", len(copias_base))
    print(
        f"  cartas: {total_base} no jogo base ({testes_base} testes), "
        f"{total_base + total_modulo} com o módulo ({testes_base + testes_modulo} testes)"
    )
    return categoria_de


def conferir_incidentes(valores: dict[str, str], categoria_de: dict[str, str]) -> None:
    incidentes: list[dict[str, str]] = []
    relatos: list[dict[str, str]] = []
    for cabecalho, linhas in ler_tabelas(ESPEC_V2):
        if "Categoria-chave" in cabecalho:
            incidentes = linhas
        if "Relato" in cabecalho:
            relatos = linhas
    if not incidentes:
        erro("catálogo de incidentes não encontrado")
        return

    por_categoria: Counter[str] = Counter()
    severos: set[str] = set()
    base = 0
    for inc in incidentes:
        ident, chave = inc["ID"], inc["Categoria-chave"]
        if not RE_ID_R.match(ident):
            erro(f"incidente com identificador inválido: {ident}")
        categorias_validas = [*CATEGORIAS_BASE, CATEGORIA_MODULO]
        if chave not in categorias_validas:
            erro(f"{ident}: categoria-chave desconhecida {chave!r}")
        secundaria = inc["Secundária"]
        if secundaria != "—" and (secundaria not in categorias_validas or secundaria == chave):
            erro(f"{ident}: categoria secundária inválida {secundaria!r}")
        testes = [t.strip() for t in inc["Testes-chave"].split(";")]
        if not 1 <= len(testes) <= 2:
            erro(f"{ident}: deve ter 1 ou 2 testes-chave")
        for teste in testes:
            if categoria_de.get(teste) != chave:
                erro(f"{ident}: teste-chave {teste!r} não pertence a {chave}")
        if inc["Severo"] == "sim":
            severos.add(ident)
        elif inc["Severo"] != "não":
            erro(f"{ident}: coluna Severo deve ser sim ou não")
        if inc["Conjunto"] == "base":
            base += 1
            por_categoria[chave] += 1
        elif inc["Conjunto"] != "módulo" or chave != CATEGORIA_MODULO:
            erro(f"{ident}: conjunto e categoria-chave não combinam")
        if not inc["Pág."].isdigit():
            erro(f"{ident}: sem página")

    if severos != SEVEROS_ESPERADOS:
        erro(f"incidentes severos: {sorted(severos)}, esperado {sorted(SEVEROS_ESPERADOS)}")
    por_cat = int(valores.get("incidentes.por_categoria", "0"))
    for categoria in CATEGORIAS_BASE:
        if por_categoria[categoria] != por_cat:
            erro(f"{categoria} tem {por_categoria[categoria]} incidentes, esperado {por_cat}")
    esperar(valores, "incidentes.base", base)
    esperar(valores, "incidentes.modulo", len(incidentes) - base)
    esperar(valores, "incidentes.com_modulo", len(incidentes))
    severos_base = len([i for i in incidentes if i["Severo"] == "sim" and i["Conjunto"] == "base"])
    esperar(valores, "incidentes.severos_base", severos_base)
    numeros = sorted(r["Incidente"] for r in relatos)
    if numeros != [f"{n:02d}" for n in range(1, len(incidentes) + 1)]:
        erro(f"relatos não cobrem todos os incidentes: {numeros}")
    if any(not r["Relato"] for r in relatos):
        erro("há incidente com relato vazio")
    print(f"  incidentes: {base} no jogo base, {len(incidentes)} com o módulo, severos {sorted(severos)}")


def conferir_baralho_v1(valores: dict[str, str]) -> None:
    cartas: list[dict[str, str]] = []
    for cabecalho, linhas in ler_tabelas(ESPEC_V1):
        if "Teste na Tabela 3" in cabecalho:
            cartas = linhas
    if not cartas:
        erro("baralho da v1 não encontrado")
        return
    por_atributo: Counter[str] = Counter()
    for carta in cartas:
        if not RE_ID_V1.match(carta["ID"]):
            erro(f"v1: identificador de carta inválido: {carta['ID']}")
        por_atributo[carta["Atributo"]] += int(carta["Cópias"])
    if dict(por_atributo) != ATRIBUTOS_V1:
        erro(f"v1: cartas por atributo {dict(por_atributo)}, esperado {ATRIBUTOS_V1}")
    esperar(valores, "v1.baralho.cartas", sum(por_atributo.values()))
    print(f"  v1: {sum(por_atributo.values())} cartas, {dict(por_atributo)}")


def conferir_ambiguidades() -> dict[str, str]:
    """Confere AMBIGUIDADES.md e devolve {id: estado}."""
    texto = AMBIGUIDADES.read_text(encoding="utf-8")
    blocos = re.split(r"^### (AMB-\d{2}) — ", texto, flags=re.MULTILINE)
    estados: dict[str, str] = {}
    for ident, corpo in zip(blocos[1::2], blocos[2::2], strict=True):
        if ident in estados:
            erro(f"ambiguidade repetida: {ident}")
        corpo = corpo.split("\n## ")[0]
        for campo in CAMPOS_AMB:
            if f"**{campo}:**" not in corpo:
                erro(f"{ident}: falta o campo {campo}")
        if "(a)" not in corpo:
            erro(f"{ident}: sem interpretações enumeradas")
        achado = re.search(r"\*\*Estado:\*\* (.+)", corpo)
        estado = achado.group(1).strip() if achado else ""
        if not estado.startswith(("aguardando decisão", "decidido")):
            erro(f"{ident}: estado inválido {estado!r}")
        estados[ident] = estado

    resumo: dict[str, str] = {}
    for cabecalho, linhas in ler_tabelas(AMBIGUIDADES):
        if cabecalho[:2] == ["ID", "Ponto"]:
            resumo = {linha["ID"]: linha["Estado"] for linha in linhas}
    if set(resumo) != set(estados):
        erro(f"resumo e entradas de ambiguidade diferem: {sorted(set(resumo) ^ set(estados))}")
    for ident, estado in estados.items():
        # Compara só a primeira palavra: "aguardando" ou "decidido".
        if ident in resumo and re.findall(r"\w+", resumo[ident])[:1] != re.findall(r"\w+", estado)[:1]:
            erro(f"{ident}: estado do resumo ({resumo[ident]!r}) difere do da entrada ({estado!r})")
    return estados


def conferir_requisitos() -> dict[str, str]:
    """Confere configs/requisitos.yaml sem depender de biblioteca de YAML."""
    texto = REQUISITOS.read_text(encoding="utf-8")
    blocos = re.split(r"^  - id: ((?:REQ|MET)-\d{2})\s*$", texto, flags=re.MULTILINE)
    estados: dict[str, str] = {}
    for ident, corpo in zip(blocos[1::2], blocos[2::2], strict=True):
        if ident in estados:
            erro(f"requisito repetido: {ident}")
        campos = CAMPOS_REQ if ident.startswith("REQ") else CAMPOS_MET
        for campo in campos:
            if not re.search(rf"^    {campo}:", corpo, flags=re.MULTILINE):
                erro(f"{ident}: falta o campo {campo}")
        achado = re.search(r"^    estado: (\S+)", corpo, flags=re.MULTILINE)
        estado = achado.group(1) if achado else ""
        if estado not in {"aguardando_decisao", "confirmado"}:
            erro(f"{ident}: estado inválido {estado!r}")
        estados[ident] = estado
    if not estados:
        erro("nenhum requisito encontrado em configs/requisitos.yaml")
    return estados


def identificadores_de_tabela(caminho: Path, prefixo: str) -> set[str]:
    achados: set[str] = set()
    for _cabecalho, linhas in ler_tabelas(caminho):
        for linha in linhas:
            primeiro = next(iter(linha.values()))
            if re.fullmatch(rf"{prefixo}-\d{{2}}", primeiro):
                achados.add(primeiro)
    return achados


def conferir_referencias(definidos: set[str]) -> None:
    outros = [
        RAIZ / "CLAUDE.md",
        RAIZ / "docs" / "HISTORICO_REGRAS.md",
        RAIZ / "docs" / "DIARIO_DE_BORDO.md",
    ]
    for caminho in (ESPEC_V2, ESPEC_V1, AMBIGUIDADES, REQUISITOS, *outros):
        if not caminho.exists():
            continue
        for numero, linha in enumerate(caminho.read_text(encoding="utf-8").splitlines(), start=1):
            for referencia in RE_REFERENCIA.findall(linha):
                if referencia not in definidos:
                    erro(f"{caminho.name}:{numero}: referência a identificador inexistente: {referencia}")


def main() -> int:
    # Saída em UTF-8 mesmo quando redirecionada no Windows.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    for caminho in (ESPEC_V2, ESPEC_V1, AMBIGUIDADES, REQUISITOS):
        if not caminho.exists():
            print(f"ERRO: arquivo ausente: {caminho}")
            return 1

    print("Conferindo as especificações")
    regras_v2, parametros_v2 = conferir_regras(ESPEC_V2, "v2.2", RE_ID_R)
    regras_v1, parametros_v1 = conferir_regras(ESPEC_V1, "v1", RE_ID_V1)
    valores = conferir_parametros({**parametros_v2, **parametros_v1})
    categoria_de = conferir_cartas(valores)
    conferir_incidentes(valores, categoria_de)
    conferir_baralho_v1(valores)
    ambiguidades = conferir_ambiguidades()
    requisitos = conferir_requisitos()

    definidos = set(regras_v2) | set(regras_v1) | set(ambiguidades) | set(requisitos)
    for cabecalho, linhas in ler_tabelas(ESPEC_V2) + ler_tabelas(ESPEC_V1):
        if "ID" in cabecalho and "Tipo" not in cabecalho:
            definidos |= {linha["ID"] for linha in linhas}
    definidos |= identificadores_de_tabela(ESPEC_V2, "MOD")
    definidos |= identificadores_de_tabela(ESPEC_V2, "VAR")
    conferir_referencias(definidos)

    for ident in sorted(ambiguidades):
        citada = any(ident in linha["Notas"] for linha in [*regras_v2.values(), *regras_v1.values()])
        if not citada:
            avisos.append(f"{ident} não é citada por nenhuma regra")

    por_tipo_v2 = Counter(linha["Tipo"] for linha in regras_v2.values())
    por_tipo_v1 = Counter(linha["Tipo"] for linha in regras_v1.values())
    pendentes = sorted(i for i, e in ambiguidades.items() if e.startswith("aguardando"))
    a_confirmar = sorted(i for i, e in requisitos.items() if e != "confirmado")
    print(f"  v2.2: {len(regras_v2)} itens {dict(sorted(por_tipo_v2.items()))}")
    print(f"  v1: {len(regras_v1)} itens {dict(sorted(por_tipo_v1.items()))}")
    print(f"  parâmetros com nome: {len(valores)}")
    print(f"  ambiguidades: {len(ambiguidades)}, aguardando decisão: {len(pendentes)}")
    print(f"  requisitos e métricas: {len(requisitos)}, aguardando confirmação: {len(a_confirmar)}")

    for aviso in avisos:
        print(f"AVISO: {aviso}")
    for mensagem in erros:
        print(f"ERRO: {mensagem}")
    print(f"\n{len(erros)} erro(s), {len(avisos)} aviso(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())

"""As convenções do projeto, conferidas por teste em vez de só declaradas."""

from __future__ import annotations

import ast
import re
from pathlib import Path

import matriz_rastreabilidade
import pytest
import verificar_especificacao
from conftest import RAIZ

MOTOR = RAIZ / "src" / "critical_failure" / "regras" / "v2"
MOTOR_V1 = RAIZ / "src" / "critical_failure" / "regras" / "v1"
PERMITIDOS = {0, 1}
"""Só índices e passos. Todo número de regra vem do YAML."""


def test_nenhum_numero_de_regra_no_codigo_do_motor() -> None:
    achados: list[str] = []
    # config.py da v1 valida o arquivo (por exemplo, "pelo menos 2 jogadores") e não aplica regra.
    arquivos = [*MOTOR.glob("*.py"), *(a for a in MOTOR_V1.glob("*.py") if a.name != "config.py")]
    for arquivo in sorted(arquivos):
        for no in ast.walk(ast.parse(arquivo.read_text(encoding="utf-8"))):
            if (
                isinstance(no, ast.Constant)
                and isinstance(no.value, int | float)
                and not isinstance(no.value, bool)
                and no.value not in PERMITIDOS
            ):
                achados.append(f"{arquivo.name}:{no.lineno}: {no.value}")
    assert achados == [], "número literal no motor; ele deveria vir do YAML: " + "; ".join(achados)


@pytest.mark.parametrize(
    "pasta, padrao_da_regra, minimo",
    # Na v2, o evento de uma variante de playtest cita a própria variante (VAR-xx).
    [
        (MOTOR, f"(?:{verificar_especificacao.PADRAO_R}|VAR-\\d{{2}})", 30),
        (MOTOR_V1, verificar_especificacao.PADRAO_V1, 15),
    ],
    ids=["v2", "v1"],
)
def test_todo_evento_do_motor_cita_uma_regra(pasta: Path, padrao_da_regra: str, minimo: int) -> None:
    arvore = ast.parse((pasta / "motor.py").read_text(encoding="utf-8"))
    chamadas = [
        no
        for no in ast.walk(arvore)
        if isinstance(no, ast.Call) and isinstance(no.func, ast.Attribute) and no.func.attr == "_ev"
    ]
    assert len(chamadas) > minimo
    padrao = re.compile(padrao_da_regra)
    for chamada in chamadas:
        regra = chamada.args[2]
        if isinstance(regra, ast.Constant):
            assert isinstance(regra.value, str) and padrao.fullmatch(regra.value), f"linha {chamada.lineno}"
        else:
            assert isinstance(regra, ast.Name) and regra.id == "regra", f"linha {chamada.lineno}"


def test_toda_regra_citada_no_codigo_existe_na_especificacao() -> None:
    itens = set(matriz_rastreabilidade.itens_da_especificacao())
    tabelas = verificar_especificacao.ler_tabelas(
        verificar_especificacao.ESPEC_V2
    ) + verificar_especificacao.ler_tabelas(verificar_especificacao.ESPEC_V1)
    for cabecalho, linhas in tabelas:
        if "ID" in cabecalho and "Tipo" not in cabecalho:
            itens |= {linha["ID"] for linha in linhas}  # cartas e incidentes
    desconhecidas = {
        regra: onde for regra, onde in matriz_rastreabilidade.codigo_por_regra().items() if regra not in itens
    }
    assert desconhecidas == {}


def test_toda_regra_que_exige_teste_tem_pelo_menos_um() -> None:
    assert matriz_rastreabilidade.sem_teste() == []
    assert matriz_rastreabilidade.marcas_desconhecidas() == []


def test_matriz_de_rastreabilidade_esta_em_dia() -> None:
    gravada = matriz_rastreabilidade.DESTINO.read_text(encoding="utf-8")
    assert gravada == matriz_rastreabilidade.renderizar(), "rode scripts/matriz_rastreabilidade.py"


def test_especificacao_passa_no_verificador() -> None:
    verificar_especificacao.erros.clear()
    verificar_especificacao.avisos.clear()
    assert verificar_especificacao.main() == 0


def test_dependencias_fixadas_e_fim_de_linha_lf() -> None:
    assert (RAIZ / "uv.lock").exists(), "o uv.lock precisa estar versionado para o ambiente ser reproduzível"
    assert "eol=lf" in (RAIZ / ".gitattributes").read_text(encoding="utf-8")

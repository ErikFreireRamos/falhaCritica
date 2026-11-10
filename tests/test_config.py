"""Configuração: os números do YAML são os da especificação, e arquivo ruim vira erro controlado."""

from __future__ import annotations

import copy
import re
from collections import Counter
from typing import Any

import pytest
from conftest import CONFIGS, RAIZ, REGRAS_ATUAIS, REGRAS_IMPRESSAS, criar_motor, ler_yaml

from critical_failure.nucleo.catalogo import CONJUNTO_BASE, ler_catalogo_bruto, montar_catalogo
from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.regras.config import carregar_regras, catalogo_das_regras, conferir_componentes, ler_regras
from critical_failure.regras.v2.motor import MotorV2

ESPECIFICACAO = (RAIZ / "docs" / "especificacao_v2_2.md").read_text(encoding="utf-8")


def _como_na_especificacao(valor: Any) -> str:
    if isinstance(valor, bool):
        return "sim" if valor else "nao"
    return str(valor)


def _parametros_da_especificacao() -> dict[str, str]:
    achados = dict(re.findall(r"`([a-z0-9_.]+)=([^`]+)`", ESPECIFICACAO))
    return {chave: valor for chave, valor in achados.items() if not chave.startswith("v1.")}


def _linha_da_regra(ident: str) -> str:
    achada = re.search(rf"^\| {re.escape(ident)} \|.*$", ESPECIFICACAO, flags=re.MULTILINE)
    assert achada is not None, f"regra {ident} não está na especificação"
    return achada.group(0)


@pytest.mark.regra("R-2.0.7", "R-2.0.8", "R-2.0.9", "R-2.0.10", "R-4.11")
def test_todo_parametro_da_especificacao_esta_no_yaml_com_o_mesmo_valor(motor: MotorV2) -> None:
    declarados = motor.regras.parametros()
    for chave, valor in _parametros_da_especificacao().items():
        assert chave in declarados, f"{chave} está na especificação e falta no YAML"
        assert _como_na_especificacao(declarados[chave][0]) == valor, chave


def test_todo_parametro_do_yaml_cita_a_regra_que_o_define(motor: MotorV2) -> None:
    na_especificacao = _parametros_da_especificacao()
    for chave, (_, regra) in motor.regras.parametros().items():
        if chave.startswith("interpretacoes.") or chave == "modulo_seguranca_operacional":
            continue  # decisões AMB e o interruptor do módulo não são números da especificação
        assert chave in na_especificacao, f"{chave} está no YAML e falta na especificação"
        assert f"`{chave}=" in _linha_da_regra(regra), f"{chave} cita {regra}, que não declara esse parâmetro"


def test_interpretacoes_citam_ambiguidades_decididas(motor: MotorV2) -> None:
    ambiguidades = (RAIZ / "docs" / "AMBIGUIDADES.md").read_text(encoding="utf-8")
    for chave, (_, regra) in motor.regras.parametros().items():
        if chave.startswith("interpretacoes."):
            bloco = ambiguidades.split(f"### {regra} — ")[1].split("\n### ")[0]
            assert "**Estado:** decidido" in bloco, f"{chave} usa {regra}, que não está decidida"


@pytest.mark.regra("R-1.4", "R-2.0.1", "R-2.0.2", "R-B.0.1", "R-C.0.1", "R-11.1", "R-11.2", "R-11.3", "R-11.7")
def test_componentes_do_catalogo(motor: MotorV2, motor_com_modulo: MotorV2) -> None:
    base, com_modulo = motor.catalogo, motor_com_modulo.catalogo
    assert len(base.cartas) == 63 and len(base.testes) == 29 and len(base.categorias) == 7
    assert set(Counter(base.categoria(carta) for carta in range(63)).values()) == {9}
    assert len(base.incidentes) == 14
    assert set(Counter(i.chave for i in base.incidentes.values()).values()) == {2}
    assert sorted(n for n, i in base.incidentes.items() if i.severo) == ["07", "09", "13"]

    assert len(com_modulo.cartas) == 72 and len(com_modulo.testes) == 33 and len(com_modulo.categorias) == 8
    assert com_modulo.categorias[-1] == "Segurança Operacional"
    do_modulo = {t.nome: t.copias for t in com_modulo.testes.values() if t.conjunto != CONJUNTO_BASE}
    assert do_modulo == {
        "Falha segura": 3,
        "Alerta de perigo": 2,
        "Restrição operacional": 2,
        "Análise de perigos": 2,
    }
    assert sorted(set(com_modulo.incidentes) - set(base.incidentes)) == ["15", "16"]
    # Ligar o módulo não muda o número das cartas do jogo base.
    assert com_modulo.cartas[:63] == base.cartas


@pytest.mark.regra("R-2.0.13")
def test_carta_tem_so_categoria_e_nome(motor: MotorV2) -> None:
    cat = motor.catalogo
    for carta in range(len(cat.cartas)):
        assert cat.teste(carta) in cat.testes
        assert cat.categoria(carta) in cat.categorias
    # A descrição existe só no catálogo (Documento do Auditor), nunca na observação dos jogadores.
    assert all(teste.descricao for teste in cat.testes.values())


@pytest.mark.regra("R-2.0.15", "R-2.0.10")
def test_faces_do_dado(motor: MotorV2, motor_com_modulo: MotorV2) -> None:
    esperado = [
        "Desempenho",
        "Compatibilidade",
        "Interação",
        "Confiabilidade",
        "Segurança da Informação",
        "Manutenibilidade",
        "Flexibilidade",
    ]
    assert [motor.catalogo.categoria_da_face(face) for face in range(1, 8)] == esperado
    assert motor.catalogo.categoria_da_face(8) is None
    assert motor_com_modulo.catalogo.categoria_da_face(8) == "Segurança Operacional"
    assert motor.faces == len(motor.catalogo.faces) == 8


def test_catalogo_yaml_esta_em_dia_com_a_especificacao() -> None:
    import gerar_catalogo

    assert gerar_catalogo.DESTINO.read_text(encoding="utf-8") == gerar_catalogo.renderizar()


@pytest.mark.regra("R-1.2", "R-6.9")
def test_v2_2_impressa_difere_da_atual_so_nas_duas_correcoes() -> None:
    atual = carregar_regras(REGRAS_ATUAIS).parametros()
    impressa = carregar_regras(REGRAS_IMPRESSAS).parametros()
    diferencas = {chave: (impressa[chave][0], atual[chave][0]) for chave in atual if atual[chave] != impressa[chave]}
    assert diferencas == {
        "jogadores.maximo": (6, 5),  # COR-01
        "alertas.limpeza_no_planejamento": (False, True),  # COR-02
    }


def test_hash_da_configuracao_e_estavel_e_sensivel() -> None:
    regras = carregar_regras(REGRAS_ATUAIS)
    assert regras.hash() == carregar_regras(REGRAS_ATUAIS).hash()
    assert regras.hash() != carregar_regras(REGRAS_IMPRESSAS).hash()
    assert regras.hash() != criar_motor(**{"fichas.iniciais": 6}).regras.hash()
    assert regras.hash().startswith("sha256:")


def _estragar(caminho: str, valor: Any) -> dict[str, Any]:
    dados = copy.deepcopy(ler_yaml(REGRAS_ATUAIS))
    no = dados
    *partes, ultima = caminho.split(".")
    for parte in partes:
        no = no[parte]
    if valor is ...:
        del no[ultima]
    else:
        no[ultima] = valor
    return dados


@pytest.mark.parametrize(
    "caminho, valor",
    [
        ("fichas.iniciais", ...),  # parâmetro ausente
        ("fichas.iniciais.valor", -1),
        ("fichas.iniciais.valor", "cinco"),
        ("fichas.iniciais.valor", 5.5),
        ("fichas.iniciais.valor", True),
        ("fichas.iniciais.regra", ...),
        ("sistema.teto.valor", 0),
        ("sistema.cartas_iniciais.valor", 9),
        ("jogadores.minimo.valor", 9),
        ("jogadores.minimo.valor", 2),
        ("linha_do_tempo.incidentes.valor", 2),
        ("radar.vagas.valor", 3),
        ("parametro_que_nao_existe", {"valor": 1, "regra": "R-0"}),
        ("interpretacoes.producao_ordem.valor", "tanto_faz"),
        ("alertas.limpeza_no_planejamento.valor", "sim"),
        ("esquema", "cf-regras/999"),
        ("familia", "v1"),
    ],
)
def test_configuracao_malformada_gera_erro_controlado(caminho: str, valor: Any) -> None:
    with pytest.raises(ConfiguracaoInvalida):
        ler_regras(_estragar(caminho, valor))


@pytest.mark.parametrize("entrada", [None, [], "texto", 42, {}])
def test_configuracao_que_nao_e_dicionario_gera_erro_controlado(entrada: Any) -> None:
    with pytest.raises(ConfiguracaoInvalida):
        ler_regras(entrada)


@pytest.mark.regra("R-2.0.1", "R-11.7")
def test_componentes_declarados_precisam_bater_com_o_catalogo() -> None:
    bruto = ler_catalogo_bruto(CONFIGS / "catalogo_v2.yaml")
    conferir_componentes(carregar_regras(REGRAS_ATUAIS), bruto)
    for chave in ("baralho.cartas_base", "baralho.testes_com_modulo", "incidentes.severos_base", "dado.faces"):
        errada = ler_regras(_estragar(f"{chave}.valor", 1))
        with pytest.raises(ConfiguracaoInvalida, match="componentes não batem"):
            conferir_componentes(errada, bruto)
    sem_uma_carta = copy.deepcopy(bruto)
    sem_uma_carta["testes"][0]["copias"] -= 1
    with pytest.raises(ConfiguracaoInvalida):
        conferir_componentes(carregar_regras(REGRAS_ATUAIS), sem_uma_carta)


@pytest.mark.parametrize("estrago", ["sem_testes", "teste_chave_de_outra_categoria", "teste_repetido", "lixo"])
def test_catalogo_malformado_gera_erro_controlado(estrago: str) -> None:
    bruto = copy.deepcopy(ler_catalogo_bruto(CONFIGS / "catalogo_v2.yaml"))
    if estrago == "sem_testes":
        del bruto["testes"]
    elif estrago == "teste_chave_de_outra_categoria":
        bruto["incidentes"][0]["testes_chave"] = ["Regressão"]
    elif estrago == "teste_repetido":
        bruto["testes"].append(bruto["testes"][0])
    else:
        bruto["testes"] = "não é uma lista"
    with pytest.raises(ConfiguracaoInvalida):
        montar_catalogo(bruto, com_modulo=False)


def test_regras_e_catalogo_carregam_juntos() -> None:
    regras = carregar_regras(REGRAS_ATUAIS)
    catalogo = catalogo_das_regras(regras, CONFIGS)
    assert catalogo.hash.startswith("sha256:") and not catalogo.com_modulo

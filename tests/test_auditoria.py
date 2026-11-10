"""Registro de auditoria: formato, determinismo, replay, narração e Folha de registro."""

from __future__ import annotations

import copy
import csv
import re
from pathlib import Path
from typing import Any

import pytest
from conftest import RAIZ

from critical_failure import cli
from critical_failure.auditoria import folha, registro, replay
from critical_failure.auditoria.narrar import narrar
from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.nucleo.canonico import json_canonico
from critical_failure.nucleo.erros import RegistroDivergente
from critical_failure.regras.v2.motor import MotorV2

ARQUIVO = "configs/regras_v2_2_1.yaml"
DATA = "2026-11-09T00:00:00+00:00"
Linhas = list[dict[str, Any]]


def gerar(motor: MotorV2, semente: int = 1, partida: int = 0, n: int = 4, **parametros: float) -> Linhas:
    bots = [BotAleatorio(**parametros) for _ in range(n)]
    linhas, _ = registro.gerar_linhas(motor, ARQUIVO, bots, semente, partida, data_hora=DATA)
    return linhas


@pytest.fixture(scope="module")
def linhas(motor: MotorV2) -> Linhas:
    return gerar(motor)


def eventos(linhas: Linhas) -> Linhas:
    return [linha for linha in linhas if linha["registro"] == "evento"]


# ---------------------------------------------------------------- formato


def test_cabecalho_tem_tudo_para_refazer_a_partida(linhas: Linhas, motor: MotorV2) -> None:
    cabecalho = linhas[0]
    assert cabecalho["registro"] == "cabecalho" and cabecalho["esquema"] == "cf-audit/1"
    assert cabecalho["regras"] == {
        "versao": "v2.2.1",
        "familia": "v2",
        "correcoes": ["COR-01", "COR-02"],
        "arquivo": ARQUIVO,
        "texto": "regras/v2.2.1.md",
    }
    assert cabecalho["config"] == motor.regras.resolvida() and cabecalho["config_hash"] == motor.regras.hash()
    assert cabecalho["catalogo_hash"] == motor.catalogo.hash
    assert (cabecalho["semente_mestre"], cabecalho["partida"], cabecalho["jogadores"]) == (1, 0, 4)
    assert cabecalho["bots"][2] == {
        "assento": 2,
        "tipo": "aleatorio",
        "parametros": {"explicacao_correta": 0.5, "precisao_auditor": 1.0},
    }
    assert set(cabecalho["git"]) == {"commit", "sujo"} and cabecalho["data_hora"] == DATA
    assert cabecalho["motor"]


def test_cada_evento_tem_os_campos_do_esquema(linhas: Linhas) -> None:
    obrigatorios = {"registro", "seq", "ciclo", "fase", "tipo", "ator", "regra", "publico", "oculto", "estado_hash"}
    for posicao, evento in enumerate(eventos(linhas)):
        assert obrigatorios <= set(evento) <= obrigatorios | {"amb", "decisao"}
        assert evento["seq"] == posicao
        assert isinstance(evento["publico"], dict) and isinstance(evento["oculto"], dict)
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", evento["estado_hash"])
        if "decisao" in evento:
            decisao = evento["decisao"]
            assert set(decisao) == {"opcoes", "escolha", "acao", "motivo"}
            assert decisao["escolha"] in decisao["opcoes"] and decisao["motivo"]


def test_toda_regra_citada_num_evento_existe_na_especificacao(linhas: Linhas) -> None:
    especificacao = (RAIZ / "docs" / "especificacao_v2_2.md").read_text(encoding="utf-8")
    ambiguidades = (RAIZ / "docs" / "AMBIGUIDADES.md").read_text(encoding="utf-8")
    regras = set(re.findall(r"^\| (R-[^ ]+) \|", especificacao, flags=re.MULTILINE))
    for evento in eventos(linhas):
        assert evento["regra"] in regras, f"evento {evento['tipo']} cita {evento['regra']}"
        if "amb" in evento:
            assert f"### {evento['amb']} — " in ambiguidades


def test_o_que_e_oculto_diz_quem_pode_ver(linhas: Linhas) -> None:
    com_oculto = [evento for evento in eventos(linhas) if evento["oculto"]]
    assert com_oculto, "a partida deveria ter eventos com informação oculta"
    for evento in com_oculto:
        visivel = evento["oculto"]["visivel_para"]
        campos = set(evento["oculto"]) - {"visivel_para"}
        assert set(visivel) <= campos
        assert all(0 <= assento < 4 for assentos in visivel.values() for assento in assentos)
    por_tipo = {evento["tipo"]: evento["oculto"]["visivel_para"] for evento in com_oculto}
    # A ordem do baralho e a Linha do Tempo não são visíveis para ninguém.
    assert por_tipo["baralho_embaralhado"] == {} and por_tipo["linha_do_tempo"] == {}
    # O sistema inicial e a compra do topo só o dono vê.
    donos = [e for e in com_oculto if e["tipo"] in ("sistema_inicial", "compra", "colocacao", "diagnostico_escolhido")]
    assert all(set(map(tuple, e["oculto"]["visivel_para"].values())) == {(e["ator"],)} for e in donos)


def test_o_fim_traz_o_placar_por_fonte_e_ele_fecha(linhas: Linhas) -> None:
    fim = linhas[-1]
    assert fim["registro"] == "fim" and fim["invariantes"] == "ok"
    assert fim["eventos"] == len(eventos(linhas))
    assert fim["criterio_de_desempate"] in {"fichas", "alertas", "diagnosticos", "dividida"}
    iniciais = linhas[0]["config"]["fichas"]["iniciais"]["valor"]
    for assento, final in enumerate(fim["placar"]["final"]):
        fontes = fim["placar"]["por_fonte"][assento]
        assert set(fontes) == {"homologacao", "diagnostico", "dano", "critical_failure", "pontuacao_final"}
        assert iniciais + sum(fontes.values()) == final
    assert fim["estado_hash_final"] == eventos(linhas)[-1]["estado_hash"]


# ---------------------------------------------------------------- determinismo


def test_mesma_configuracao_e_mesma_semente_geram_os_mesmos_bytes(motor: MotorV2, linhas: Linhas) -> None:
    de_novo = gerar(motor)
    assert [json_canonico(linha) for linha in de_novo[1:]] == [json_canonico(linha) for linha in linhas[1:]]
    assert json_canonico(gerar(motor, partida=1)[1:]) != json_canonico(linhas[1:])
    assert json_canonico(gerar(motor, semente=2)[1:]) != json_canonico(linhas[1:])


def test_trocar_os_bots_nao_muda_as_cartas(motor: MotorV2, linhas: Linhas) -> None:
    """Fluxos de aleatoriedade separados: o baralho e os incidentes não dependem dos bots."""
    outros = gerar(motor, explicacao_correta=0.9, precisao_auditor=0.8)

    def sorteios(registros: Linhas) -> list[Any]:
        return [e["oculto"] for e in eventos(registros) if e["tipo"] in ("baralho_embaralhado", "linha_do_tempo")]

    assert sorteios(outros) == sorteios(linhas)
    assert json_canonico(outros[1:]) != json_canonico(linhas[1:])


# ---------------------------------------------------------------- replay


@pytest.mark.parametrize("modo", replay.MODOS)
def test_replay_confere_todos_os_eventos(linhas: Linhas, modo: str) -> None:
    resultado = replay.refazer(linhas, modo)
    assert resultado.eventos == len(eventos(linhas))


def _adulterar(linhas: Linhas, estrago: str) -> Linhas:
    falsas = copy.deepcopy(linhas)
    com_fichas = next(e for e in falsas if e.get("tipo") == "falhou")
    com_decisao = next(e for e in falsas if e.get("tipo") == "compra" and e["publico"]["origem"] == "backlog")
    if estrago == "ficha a mais num evento":
        atacante = next(iter(com_fichas["publico"]["fichas"]))
        com_fichas["publico"]["fichas"][atacante] += 1
    elif estrago == "hash de estado trocado":
        com_fichas["estado_hash"] = "sha256:" + "0" * 64
    elif estrago == "placar final alterado":
        falsas[-1]["placar"]["final"][0] += 1
    elif estrago == "ação trocada":
        com_decisao["decisao"]["acao"] = {"tipo": "comprar", "origem": "topo"}
    elif estrago == "evento removido":
        falsas.remove(com_fichas)
    elif estrago == "informação oculta alterada":
        defesa = next(e for e in falsas if e.get("tipo") == "defesa" and e["oculto"])
        defesa["oculto"]["blefe"] = not defesa["oculto"]["blefe"]
    elif estrago == "semente trocada":
        falsas[0]["semente_mestre"] += 1
    elif estrago == "configuração alterada sem atualizar o hash":
        falsas[0]["config"]["fichas"]["iniciais"]["valor"] = 6
    return falsas


@pytest.mark.parametrize(
    "estrago",
    [
        "ficha a mais num evento",
        "hash de estado trocado",
        "placar final alterado",
        "ação trocada",
        "evento removido",
        "informação oculta alterada",
        "semente trocada",
        "configuração alterada sem atualizar o hash",
    ],
)
@pytest.mark.parametrize("modo", replay.MODOS)
def test_replay_acusa_qualquer_adulteracao(linhas: Linhas, estrago: str, modo: str) -> None:
    falsas = _adulterar(linhas, estrago)
    assert falsas != linhas
    with pytest.raises(RegistroDivergente):
        replay.refazer(falsas, modo)


def test_registro_gravado_em_disco_e_refeito(motor: MotorV2, tmp_path: Path) -> None:
    caminho = tmp_path / "partida.jsonl"
    bots = [BotAleatorio() for _ in range(5)]
    resultado = registro.gravar_partida(caminho, motor, ARQUIVO, bots, semente=4, partida=2, data_hora=DATA)
    bruto = caminho.read_bytes()
    assert b"\r" not in bruto and bruto.endswith(b"\n")
    lidas = registro.ler(caminho)
    assert lidas[-1]["placar"]["final"] == list(resultado.placar)
    assert replay.refazer(lidas, replay.MODO_ACOES).eventos == resultado.eventos


@pytest.mark.parametrize("conteudo", ["", "isto não é JSON\n", '{"registro":"cabecalho"}\n', "[1,2,3]\n[4]\n"])
def test_arquivo_que_nao_e_registro_gera_erro_controlado(tmp_path: Path, conteudo: str) -> None:
    caminho = tmp_path / "ruim.jsonl"
    caminho.write_text(conteudo, encoding="utf-8")
    with pytest.raises(RegistroDivergente):
        registro.ler(caminho)
    with pytest.raises(RegistroDivergente):
        registro.ler(tmp_path / "nao_existe.jsonl")


# ---------------------------------------------------------------- narração


def test_narracao_conta_a_partida_do_inicio_ao_fim(linhas: Linhas, motor: MotorV2) -> None:
    texto = narrar(linhas, motor.catalogo)
    assert texto.startswith("Critical Failure v2.2.1 | partida 0 | semente 1 | 4 jogadores")
    for trecho in ("== Ciclo 1: Planejamento ==", "== Ciclo 3: Produção ==", "== Critical Failure ==", "Placar final:"):
        assert trecho in texto
    assert "[" in texto, "por padrão a narração mostra o que estava oculto"
    sem_oculto = narrar(linhas, motor.catalogo, mostrar_oculto=False)
    assert "[" not in sem_oculto and "Placar final:" in sem_oculto
    com_regras = narrar(linhas, motor.catalogo, citar_regras=True)
    assert "(R-7.2.1" in com_regras and "(R-9.1.1)" in com_regras
    placar = ", ".join(
        f"{nome} {fichas}"
        for nome, fichas in zip(("Ana", "Bruno", "Carla", "Davi"), linhas[-1]["placar"]["final"], strict=True)
    )
    assert f"Placar final: {placar}." in texto


# ---------------------------------------------------------------- Folha de registro


@pytest.mark.regra("R-REG.1")
def test_folha_traz_o_diagnostico_de_cada_jogador_por_incidente(linhas: Linhas) -> None:
    diagnosticos = folha.extrair(linhas)["diagnosticos"]
    assert len(diagnosticos) == 4 * 3, "4 jogadores, 3 incidentes, inclusive o Auditor de cada ciclo"
    assert set(diagnosticos[0]) == set(folha.COLUNAS_DIAGNOSTICOS)
    for ciclo in (1, 2, 3):
        do_ciclo = [linha for linha in diagnosticos if linha["ciclo"] == ciclo]
        assert sorted(linha["assento"] for linha in do_ciclo) == [0, 1, 2, 3]
        assert [linha["era_auditor"] for linha in do_ciclo].count("sim") == 1
    for linha in diagnosticos:
        assert linha["classificacao"] in {"chave", "secundaria", "outra"}
        # Só a categoria-chave conta como acerto.
        assert (linha["acertou"] == "sim") == (linha["classificacao"] == "chave")


@pytest.mark.regra("R-REG.2")
def test_folha_traz_cada_defesa(linhas: Linhas) -> None:
    defesas = folha.extrair(linhas)["defesas"]
    testes = [e for e in eventos(linhas) if e["tipo"] == "teste"]
    assert len(defesas) == len(testes) > 0
    assert set(defesas[0]) == set(folha.COLUNAS_DEFESAS)
    blefes = [e["oculto"]["blefe"] for e in eventos(linhas) if e["tipo"] == "defesa" and e["oculto"]]
    assert [linha["era_blefe"] for linha in defesas if linha["era_blefe"]] == ["sim" if b else "nao" for b in blefes]
    for linha, teste in zip(defesas, testes, strict=True):
        assert linha["categoria_atacada"] == teste["publico"]["categoria"]
        if linha["resposta"] == "admitiu":
            assert (linha["teste_nomeado"], linha["era_blefe"], linha["decisao_do_auditor"]) == ("", "", "")
        assert linha["houve_contestacao"] == ("sim" if linha["resultado"].startswith("contestou") else "nao")


@pytest.mark.regra("R-REG.3")
def test_folha_traz_as_fichas_finais_e_e_exportada_em_csv(linhas: Linhas, tmp_path: Path) -> None:
    caminhos = folha.exportar(linhas, tmp_path, "p0")
    assert [caminho.name for caminho in caminhos] == ["p0_diagnosticos.csv", "p0_defesas.csv", "p0_fichas.csv"]
    with caminhos[2].open(encoding="utf-8", newline="") as arquivo:
        fichas = list(csv.DictReader(arquivo))
    assert [int(linha["fichas_finais"]) for linha in fichas] == linhas[-1]["placar"]["final"]
    assert [linha["venceu"] == "sim" for linha in fichas] == [j in linhas[-1]["vencedores"] for j in range(4)]
    with caminhos[1].open(encoding="utf-8", newline="") as arquivo:
        assert csv.DictReader(arquivo).fieldnames == folha.COLUNAS_DEFESAS


# ---------------------------------------------------------------- linha de comando


def test_linha_de_comando_de_ponta_a_ponta(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    log = tmp_path / "p.jsonl"
    assert cli.main(["jogar", "--semente", "3", "--jogadores", "5", "--log", str(log)]) == 0
    assert "registro gravado" in capsys.readouterr().out
    assert cli.main(["replay", str(log)]) == 0
    saida = capsys.readouterr().out
    assert "replay (acoes)" in saida and "replay (bots)" in saida and "nenhuma divergência" in saida
    assert cli.main(["narrar", str(log), "--sem-oculto", "--regras-citadas"]) == 0
    assert "Placar final" in capsys.readouterr().out
    assert cli.main(["folha", str(log), "--saida", str(tmp_path / "folha")]) == 0
    assert len(list((tmp_path / "folha").glob("p_*.csv"))) == 3
    assert cli.main(["jogar", "--narrar"]) == 0
    assert "== Ciclo 1: Planejamento ==" in capsys.readouterr().out


def test_linha_de_comando_devolve_erro_controlado(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    ruim = tmp_path / "ruim.jsonl"
    ruim.write_text("{}\n", encoding="utf-8")
    assert cli.main(["replay", str(ruim)]) == 1
    assert "erro: RegistroDivergente" in capsys.readouterr().err
    assert cli.main(["jogar", "--jogadores", "9"]) == 1
    assert "erro: ConfiguracaoInvalida" in capsys.readouterr().err

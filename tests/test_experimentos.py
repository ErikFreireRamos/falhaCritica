"""Executor de experimentos: tabela, registros, manifest, relatório e veredito dos requisitos."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from conftest import RAIZ

from critical_failure import cli
from critical_failure.auditoria import registro, replay
from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.experimentos import executor
from critical_failure.experimentos.config import aplicar_mudancas, carregar_experimento, ler_experimento
from critical_failure.metricas.estatistica import FALHA, INCONCLUSIVO
from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.partida import jogar_partida
from critical_failure.regras.v2.motor import MotorV2

ALEATORIO = {"tipo": "aleatorio", "parametros": {"explicacao_correta": 0.5, "precisao_auditor": 1.0}}


def experimento(**mudancas: Any) -> dict[str, Any]:
    dados: dict[str, Any] = {
        "esquema": "cf-experimento/1",
        "nome": "teste",
        "descricao": "Experimento pequeno usado nos testes.",
        "semente_mestre": 77,
        "duracao": "configs/duracao.yaml",
        "registros_completos_um_a_cada": 10,
        "cenarios": [
            {
                "nome": "quatro",
                "regras": "configs/regras_v2_2_1.yaml",
                "jogadores": 4,
                "partidas": 24,
                "bots": [ALEATORIO],
                "requisitos": ["REQ-01", "REQ-08"],
            },
            {
                "nome": "cinco_mistos",
                "regras": "configs/regras_v2_2_1.yaml",
                "jogadores": 5,
                "partidas": 12,
                "bots": [ALEATORIO, ALEATORIO, ALEATORIO, ALEATORIO, {"tipo": "aleatorio"}],
                "requisitos": ["REQ-01"],
            },
        ],
    }
    dados.update(mudancas)
    return dados


def rodar(tmp_path: Path, nome: str = "saida", processos: int = 1, **mudancas: Any) -> executor.Execucao:
    arquivo = tmp_path / f"{nome}.yaml"
    arquivo.write_text(yaml.safe_dump(experimento(**mudancas), allow_unicode=True), encoding="utf-8")
    return executor.executar(carregar_experimento(arquivo), arquivo, saida=tmp_path / nome, processos=processos)


@pytest.fixture(scope="module")
def execucao(tmp_path_factory: pytest.TempPathFactory) -> executor.Execucao:
    return rodar(tmp_path_factory.mktemp("experimento"))


# ---------------------------------------------------------------- tabela de partidas


def test_uma_linha_por_partida_e_a_tabela_volta_igual_do_parquet(execucao: executor.Execucao) -> None:
    linhas = execucao.linhas
    assert [(linha["cenario"], linha["partida"]) for linha in linhas] == [
        *(("quatro", i) for i in range(24)),
        *(("cinco_mistos", i) for i in range(12)),
    ]
    assert all(linha["erro"] is None for linha in linhas)
    assert all(len(linha["placar"]) == linha["jogadores"] for linha in linhas)
    assert all(linha["duracao_s"] > 0 for linha in linhas)
    assert executor.ler_tabela(execucao.pasta) == linhas


def test_cada_partida_e_a_mesma_que_rodaria_sozinha(execucao: executor.Execucao, motor: MotorV2) -> None:
    """Números aleatórios comuns: a partida i do experimento é a partida i da semente mestre."""
    for linha in execucao.linhas[:5]:
        sozinha = jogar_partida(motor, [BotAleatorio() for _ in range(4)], 77, linha["partida"])
        assert list(sozinha.placar) == linha["placar"]
        assert list(sozinha.vencedores) == linha["vencedores"]


def test_o_resultado_nao_depende_do_numero_de_processos(tmp_path: Path, execucao: executor.Execucao) -> None:
    em_paralelo = rodar(tmp_path, processos=2)
    assert em_paralelo.linhas == execucao.linhas
    assert (em_paralelo.pasta / "partidas.parquet").read_bytes() == (execucao.pasta / "partidas.parquet").read_bytes()


# ---------------------------------------------------------------- registros completos


def test_registro_completo_de_uma_amostra_e_ele_e_refeito(execucao: executor.Execucao) -> None:
    gravados = sorted((execucao.pasta / "registros").rglob("*.jsonl"))
    nomes = [caminho.relative_to(execucao.pasta).as_posix() for caminho in gravados]
    # Uma a cada 10: partidas 0, 10 e 20 do primeiro cenário; 0 e 10 do segundo.
    assert nomes == [
        "registros/cinco_mistos/partida_0000000.jsonl",
        "registros/cinco_mistos/partida_0000010.jsonl",
        "registros/quatro/partida_0000000.jsonl",
        "registros/quatro/partida_0000010.jsonl",
        "registros/quatro/partida_0000020.jsonl",
    ]
    linhas = registro.ler(gravados[-1])
    assert linhas[-1]["placar"]["final"] == execucao.linhas[20]["placar"]
    assert linhas[-1]["duracao_estimada_s"] == execucao.linhas[20]["duracao_s"]
    for modo in replay.MODOS:
        assert replay.refazer(linhas, modo).eventos == linhas[-1]["eventos"]


def test_partida_que_falha_vira_linha_de_erro_e_tem_registro(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    original = executor.jogar_partida

    def quebra_na_partida_3(*args: Any, **kwargs: Any) -> Any:
        if args[3] == 3:
            raise RuntimeError("defeito simulado")
        return original(*args, **kwargs)

    monkeypatch.setattr(executor, "jogar_partida", quebra_na_partida_3)
    resultado = rodar(tmp_path, cenarios=experimento()["cenarios"][:1])
    erros = [linha for linha in resultado.linhas if linha["erro"] is not None]
    assert [(linha["partida"], linha["erro"]) for linha in erros] == [(3, "RuntimeError: defeito simulado")]
    assert erros[0]["placar"] is None
    assert (resultado.pasta / "registros" / "quatro" / "falha_0000003.jsonl").exists()
    assert resultado.manifest["falhas"] == 1
    assert resultado.manifest["vereditos"]["REQ-09"] == [FALHA]


# ---------------------------------------------------------------- manifest


def test_manifest_identifica_tudo_o_que_gerou_os_numeros(execucao: executor.Execucao) -> None:
    manifest = json.loads((execucao.pasta / "manifest.json").read_text(encoding="utf-8"))
    assert manifest == execucao.manifest
    assert manifest["esquema"] == "cf-manifest/1"
    assert manifest["experimento"]["conteudo"] == ler_experimento(experimento()).resolvido()
    assert manifest["semente_mestre"] == 77 and manifest["partidas"] == 36 and manifest["falhas"] == 0
    assert set(manifest["git"]) == {"commit", "sujo"}
    assert manifest["invariantes_conferidos_a_cada_evento"] is True
    assert set(manifest["ambiente"]) == {"motor", "python", "numpy", "pyarrow", "plataforma"}
    quatro = manifest["cenarios"][0]
    assert quatro["versao"] == "v2.2.1" and quatro["config_hash"].startswith("sha256:")
    assert len(quatro["bots"]) == 4 and quatro["requisitos"] == ["REQ-01", "REQ-08"]
    for arquivo, hash_ in manifest["arquivos"].items():
        assert hash_ == executor._hash_do_arquivo(execucao.pasta / arquivo)
    assert manifest["registros_completos"] == 5


def test_experimento_oficial_recusa_repositorio_com_alteracao(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(registro, "info_git", lambda: {"commit": "abc1234", "sujo": True})
    arquivo = tmp_path / "e.yaml"
    arquivo.write_text(yaml.safe_dump(experimento(), allow_unicode=True), encoding="utf-8")
    with pytest.raises(executor.ExperimentoRecusado):
        executor.executar(carregar_experimento(arquivo), arquivo, saida=tmp_path / "s", oficial=True)
    assert not (tmp_path / "s").exists()


# ---------------------------------------------------------------- requisitos e relatório


def test_requisitos_medidos_so_onde_o_cenario_pede(execucao: executor.Execucao) -> None:
    texto = (execucao.pasta / "relatorio.md").read_text(encoding="utf-8")
    vereditos = execucao.manifest["vereditos"]
    assert set(vereditos) == {"REQ-01", "REQ-08", "REQ-09"}
    # Com 36 partidas a robustez não tem como passar: o critério pede 50.000.
    assert vereditos["REQ-09"] == [INCONCLUSIVO]
    # REQ-01 só vale com bots idênticos: o cenário de bots com parâmetros diferentes fica de fora.
    assert "| quatro | taxa de vitória da posição 3 |" in texto
    assert "| cinco_mistos | taxa de vitória" not in texto
    assert "| quatro | mediana da duração estimada (min) |" in texto
    assert "## Descrição das partidas" in texto and "## Como refazer" in texto


def test_relatorio_refeito_do_manifest_e_igual_ao_original(
    execucao: executor.Execucao, capsys: pytest.CaptureFixture[str]
) -> None:
    original = (execucao.pasta / "relatorio.md").read_text(encoding="utf-8")
    assert cli.main(["relatorio", str(execucao.pasta)]) == 0
    assert (execucao.pasta / "relatorio.md").read_text(encoding="utf-8") == original
    assert "# Relatório do experimento `teste`" in capsys.readouterr().out


def test_requisito_nao_confirmado_nao_recebe_veredito(tmp_path: Path) -> None:
    cenarios = experimento()["cenarios"][:1]
    cenarios[0] = {**cenarios[0], "partidas": 4, "requisitos": ["REQ-02", "REQ-06"]}
    resultado = rodar(tmp_path, cenarios=cenarios)
    assert set(resultado.manifest["vereditos"]) == {"REQ-09"}


# ---------------------------------------------------------------- configuração do experimento


@pytest.mark.parametrize(
    "mudanca",
    [
        {"esquema": "cf-experimento/9"},
        {"nome": "Nome Inválido"},
        {"registros_completos_um_a_cada": 0},
        {"cenarios": []},
        {"cenarios": [experimento()["cenarios"][0], experimento()["cenarios"][0]]},
        {"cenarios": [{**experimento()["cenarios"][0], "partidas": 0}]},
        {"cenarios": [{**experimento()["cenarios"][0], "bots": [ALEATORIO, ALEATORIO]}]},
        {"campo_que_nao_existe": 1},
    ],
)
def test_experimento_malformado_gera_erro_controlado(mudanca: dict[str, Any]) -> None:
    with pytest.raises(ConfiguracaoInvalida):
        ler_experimento(experimento(**mudanca))


@pytest.mark.parametrize(
    "cenario",
    [
        {"bots": [{"tipo": "bot_que_nao_existe"}]},
        {"bots": [{"tipo": "aleatorio", "parametros": {"parametro_errado": 1}}]},
        {"bots": [{"tipo": "aleatorio", "parametros": {"explicacao_correta": 1.5}}]},
        {"jogadores": 6, "bots": [ALEATORIO]},  # a v2.2.1 vai até 5 (COR-01)
        {"mudancas": {"parametro.que.nao.existe": 1}},
        {"mudancas": {"fichas.iniciais": -1}},
    ],
)
def test_cenario_invalido_e_recusado_antes_de_rodar(tmp_path: Path, cenario: dict[str, Any]) -> None:
    cenarios = [{**experimento()["cenarios"][0], **cenario}]
    with pytest.raises(ConfiguracaoInvalida):
        rodar(tmp_path, cenarios=cenarios)
    assert not (tmp_path / "saida" / "partidas.parquet").exists()


def test_mudancas_trocam_so_o_valor_pedido() -> None:
    dados = yaml.safe_load((RAIZ / "configs" / "regras_v2_2_1.yaml").read_text(encoding="utf-8"))
    novas = aplicar_mudancas(dados, {"planejamento.compras": 2, "modulo_seguranca_operacional": True})
    assert novas["planejamento"]["compras"] == {"valor": 2, "regra": "R-6.1"}
    assert novas["modulo_seguranca_operacional"]["valor"] is True
    assert dados["planejamento"]["compras"]["valor"] == 3, "a configuração original não pode mudar"


def test_experimento_da_fase_1b_e_valido() -> None:
    lido = carregar_experimento(RAIZ / "experimentos" / "fase1b_linha_de_base.yaml")
    assert sum(cenario.partidas for cenario in lido.cenarios) >= 50_000
    assert lido.conferir_invariantes


def test_linha_de_comando_roda_um_experimento(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    arquivo = tmp_path / "e.yaml"
    pequeno = experimento(cenarios=[{**experimento()["cenarios"][0], "partidas": 3}])
    arquivo.write_text(yaml.safe_dump(pequeno, allow_unicode=True), encoding="utf-8")
    assert cli.main(["experimento", str(arquivo), "--processos", "1", "--saida", str(tmp_path / "s")]) == 0
    saida = capsys.readouterr().out
    assert "3 partidas" in saida and "REQ-09: inconclusivo" in saida
    assert (tmp_path / "s" / "manifest.json").exists()
    assert cli.main(["relatorio", str(tmp_path / "nao_existe")]) == 1

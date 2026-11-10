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


# ---------------------------------------------------------------- rodízio e taxa de vitória por bot

ESTILOS = [
    {"tipo": "construtor", "parametros": {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}},
    {
        "tipo": "cacador",
        "parametros": {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar", "alvo": "lider"},
    },
    {"tipo": "heuristico", "parametros": {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}},
    {**ALEATORIO, "rotulo": "aleatorio experiente"},
]


def test_rodizio_roda_cada_rotacao_dos_bots_pelos_assentos() -> None:
    cenario = {
        "nome": "mista",
        "regras": "configs/regras_v2_2_1.yaml",
        "jogadores": 4,
        "partidas": 3,
        "bots": ESTILOS,
        "rodizio": True,
    }
    lido = ler_experimento(experimento(cenarios=[cenario]))
    rotacoes = lido.cenarios_expandidos()
    assert [c.nome for c in rotacoes] == ["mista_r0", "mista_r1", "mista_r2", "mista_r3"]
    assert all(c.grupo == "mista" and not c.rodizio for c in rotacoes)
    assert [bot.tipo for bot in rotacoes[1].bots] == ["cacador", "heuristico", "aleatorio", "construtor"]
    # Cada bot passa por todos os assentos.
    for k in range(4):
        assert {rotacao.bots[k].nome() for rotacao in rotacoes} == {bot.nome() for bot in rotacoes[0].bots}
    with pytest.raises(ConfiguracaoInvalida):
        ler_experimento(experimento(cenarios=[{**cenario, "bots": ESTILOS[:1]}]))


def test_taxa_de_vitoria_por_bot_no_relatorio(tmp_path: Path) -> None:
    cenario = {
        "nome": "mista",
        "regras": "configs/regras_v2_2_1.yaml",
        "jogadores": 4,
        "partidas": 6,
        "bots": ESTILOS,
        "rodizio": True,
    }
    resultado = rodar(tmp_path, cenarios=[cenario])
    assert resultado.manifest["partidas"] == 24
    assert {c["grupo"] for c in resultado.manifest["cenarios"]} == {"mista"}
    from critical_failure.metricas.requisitos import vitorias_por_bot

    estilos = vitorias_por_bot(resultado.linhas, ler_experimento(experimento(cenarios=[cenario])))
    assert sorted(e["bot"] for e in estilos) == ["aleatorio experiente", "cacador (lider)", "construtor", "heuristico"]
    assert all(e["assentos_jogados"] == 24 and e["referencia"] == 0.25 for e in estilos)
    # Cada partida distribui exatamente 1 vitória entre os assentos: as taxas somam 1.
    assert sum(e["taxa"] for e in estilos) == pytest.approx(1.0)
    texto = (resultado.pasta / "relatorio.md").read_text(encoding="utf-8")
    assert "## Taxa de vitória por bot (MET-07)" in texto and "| mista | cacador (lider) | 4 | 24 |" in texto


def test_experimento_da_fase_2_e_valido() -> None:
    lido = carregar_experimento(RAIZ / "experimentos" / "fase2_fumaca_estilos.yaml")
    rotacoes = lido.cenarios_expandidos()
    assert len(rotacoes) == 4 + 5
    assert sum(c.partidas for c in rotacoes) == 20_000


# ---------------------------------------------------------------- Fase 3: v1, MET-01, MET-02 e REQ-02

V1_PERFIL = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}


def test_desequilibrio_pelo_criterio_fixado() -> None:
    from critical_failure.metricas.requisitos import carregar_requisitos, desequilibrio

    lido = ler_experimento(experimento(cenarios=[{**experimento()["cenarios"][0], "partidas": 4}]))
    linhas = [
        {"cenario": "quatro", "familia": "v2", "erro": None, "placar": placar, "vencedores": [0]}
        for placar in ([6, 2, 2, 2], [3, 3, 2, 2], [9, 6, 6, 6], [0, 0, 0, 0])
    ]
    requisitos = carregar_requisitos(RAIZ / "configs" / "requisitos.yaml")
    medidas = {d["fator"]: d for d in desequilibrio(linhas, lido, requisitos)}
    # 6 >= 1,5 x 2 (sim); 3 >= 1,5 x 2,33 (não); 9 >= 1,5 x 6 (sim, no limite); placar zerado (não).
    assert medidas[1.5]["proporcao"] == 0.5 and medidas[1.5]["principal"]
    # Com 1,25: 3 >= 1,25 x 2,33 também conta. Com 2,0: só a primeira.
    assert medidas[1.25]["proporcao"] == 0.75 and medidas[2.0]["proporcao"] == 0.25
    assert set(medidas) == {1.5, 1.25, 2.0}


def test_amostra_do_lider_no_corte() -> None:
    from critical_failure.metricas.requisitos import amostra_do_lider

    linhas = [
        {"placar_no_corte": [3, 1, 1], "vencedores": [0]},  # líder venceu
        {"placar_no_corte": [3, 1, 1], "vencedores": [0, 2]},  # líder dividiu a vitória
        {"placar_no_corte": [1, 3, 1], "vencedores": [0]},  # líder perdeu
        {"placar_no_corte": [2, 2, 1], "vencedores": [0]},  # sem líder isolado: fica de fora
        {"placar_no_corte": None, "vencedores": [0]},
    ]
    assert list(amostra_do_lider(linhas)) == [1.0, 0.5, 0.0]


def test_experimento_com_v1_v2_matriz_e_req_02(tmp_path: Path) -> None:
    cacador = {"tipo": "cacador", "parametros": {**V1_PERFIL, "alvo": "lider"}}
    foco = {"tipo": "cacador", "rotulo": "foco", "parametros": {**V1_PERFIL, "alvo": "mais_fraco"}}
    mistos = [
        {"tipo": "construtor", "parametros": V1_PERFIL},
        cacador,
        {"tipo": "heuristico", "parametros": V1_PERFIL},
        {"tipo": "aleatorio", "parametros": {}},
    ]
    cenarios = [
        {
            "nome": "v1_mistos",
            "regras": "configs/regras_v1.yaml",
            "jogadores": 4,
            "partidas": 6,
            "rodizio": True,
            "bots": mistos,
        },
        {
            "nome": "v2_mistos",
            "regras": "configs/regras_v2_2_1.yaml",
            "jogadores": 4,
            "partidas": 6,
            "rodizio": True,
            "bots": mistos,
            "comparar_com": "v1_mistos",
            "requisitos": ["REQ-02"],
        },
        {
            "nome": "alvo_mais_fraco_contra_lider",
            "regras": "configs/regras_v1.yaml",
            "jogadores": 3,
            "partidas": 4,
            "rodizio": True,
            "celula": ["mais_fraco", "lider"],
            "bots": [foco, cacador, cacador],
        },
    ]
    resultado = rodar(tmp_path, cenarios=cenarios)
    v1 = [linha for linha in resultado.linhas if linha["familia"] == "v1"]
    assert v1 and all(linha["duracao_s"] is None for linha in v1)
    assert all(linha["placar_no_corte"] is not None for linha in resultado.linhas)
    assert resultado.manifest["vereditos"]["REQ-02"][0] in {"passa", "falha", "inconclusivo"}
    assert {c["familia"] for c in resultado.manifest["cenarios"]} == {"v1", "v2"}
    texto = (resultado.pasta / "relatorio.md").read_text(encoding="utf-8")
    for secao in ("### REQ-02", "## Política de alvo (MET-02)", "## Partidas desequilibradas (MET-01)"):
        assert secao in texto
    assert "| mais_fraco | " in texto and "vantagem do líder em v1_mistos menos a vantagem em v2_mistos" in texto
    # A v1 não tem duração: a coluna fica vazia, sem quebrar o relatório.
    assert "| v1_mistos_r0 |" in texto


def test_comparacao_com_grupo_que_nao_existe(tmp_path: Path) -> None:
    cenario = {**experimento()["cenarios"][0], "partidas": 2, "comparar_com": "nao_existe", "requisitos": ["REQ-02"]}
    with pytest.raises(ConfiguracaoInvalida):
        rodar(tmp_path, cenarios=[cenario])


def test_experimentos_da_fase_3_sao_validos() -> None:
    primeiro = carregar_experimento(RAIZ / "experimentos" / "fase3_exp1_validacao_v1.yaml")
    celulas = [c.celula for c in primeiro.cenarios if c.celula]
    assert len(celulas) == 9 and all(c.jogadores == 6 for c in primeiro.cenarios)
    segundo = carregar_experimento(RAIZ / "experimentos" / "fase3_exp2_v1_contra_v2.yaml")
    comparacoes = {c.nome: c.comparar_com for c in segundo.cenarios if c.comparar_com}
    assert comparacoes == {
        "v2_2_1_com_4_jogadores": "v1_com_4_jogadores",
        "v2_2_1_com_5_jogadores": "v1_com_5_jogadores",
    }


def test_falha_ao_gravar_um_registro_nao_derruba_o_experimento(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    def disco_com_problema(caminho: Path, linhas: Any) -> None:
        raise OSError(22, "Invalid argument")

    monkeypatch.setattr(registro, "escrever", disco_com_problema)
    resultado = rodar(tmp_path, cenarios=[{**experimento()["cenarios"][0], "partidas": 12}])
    assert len(resultado.linhas) == 12 and all(linha["erro"] is None for linha in resultado.linhas)
    avisos = [linha["aviso"] for linha in resultado.linhas if linha["aviso"]]
    assert len(avisos) == 2 and "registro não gravado" in avisos[0]  # partidas 0 e 10
    assert resultado.manifest["registros_nao_gravados"] == 2


# ---------------------------------------------------------------- Fase 4: melhor estilo (MET-07, REQ-03, 04 e 11)

PERFIL = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}


def celula(
    nome: str, foco: dict[str, Any], outros: dict[str, Any], linha: str, coluna: str, **extra: Any
) -> dict[str, Any]:
    return {
        "nome": nome,
        "regras": "configs/regras_v2_2_1.yaml",
        "jogadores": 4,
        "partidas": 2,
        "rodizio": True,
        "matriz": "estilos_teste",
        "celula": [linha, coluna],
        "bots": [{**foco, "rotulo": "foco"}, *[{**outros, "rotulo": "outros"}] * 3],
        **extra,
    }


def test_sistemas_cheios_no_fim_do_primeiro_planejamento() -> None:
    from critical_failure.bots.fabrica import criar_bot
    from critical_failure.regras.familias import carregar_motor

    motor = carregar_motor(RAIZ / "configs" / "regras_v2_2_1.yaml")
    teto = motor.regras.sistema.teto.valor
    vistos: list[tuple[bool, ...]] = []

    def ouvinte(evento: Any, _decisao: Any) -> None:
        if evento.tipo == "inicio_da_fase" and evento.publico["fase"] == "homologacao" and evento.ciclo == 1:
            vistos.append(tuple(len(j.sistema) >= teto for j in evento.estado.jogadores))

    bots = [criar_bot("construtor", PERFIL), criar_bot("cacador", {**PERFIL, "alvo": "lider"})] * 2
    resultado = jogar_partida(motor, bots, 5, 0, ouvinte=ouvinte)
    assert resultado.sistemas_cheios_no_planejamento == vistos[0]
    # O Construtor enche o sistema no primeiro Planejamento; o Caçador, não.
    assert resultado.sistemas_cheios_no_planejamento == (True, False, True, False)
    v1 = carregar_motor(RAIZ / "configs" / "regras_v1.yaml")
    v1_bots = [criar_bot("construtor", PERFIL, "v1") for _ in range(4)]
    assert jogar_partida(v1, v1_bots, 5, 0).sistemas_cheios_no_planejamento is None


def test_replicador() -> None:
    import numpy as np

    from critical_failure.metricas.matrizes import replicador

    # O estilo 0 se sai melhor contra as duas populações: ele toma a população.
    final, convergiu = replicador(np.array([[0.25, 0.40], [0.10, 0.25]]))
    assert convergiu and final[0] == pytest.approx(1.0)
    # Cada um invade a população do outro. Equilíbrio misto: 0,2 x + 0,4 (1 - x) = 0,3 x + 0,25 (1 - x), x = 0,6.
    final, convergiu = replicador(np.array([[0.20, 0.40], [0.30, 0.25]]))
    assert convergiu and final[0] == pytest.approx(0.6, abs=1e-6)


def _matriz_sintetica(taxas: dict[tuple[str, str], float], partidas: int = 400) -> tuple[Any, list[dict[str, Any]]]:
    """Uma matriz 2 x 2 com o resultado de cada partida escolhido: o foco vence na fração pedida de cada célula."""
    cenarios = [celula(f"{a}_contra_{b}", ALEATORIO, ALEATORIO, a, b, partidas=partidas) for a, b in taxas]
    lido = ler_experimento(experimento(cenarios=cenarios))
    linhas: list[dict[str, Any]] = []
    for cenario in lido.cenarios_expandidos():
        assert cenario.celula is not None
        taxa = taxas[(cenario.celula[0], cenario.celula[1])]
        foco = next(i for i, bot in enumerate(cenario.bots_por_assento()) if bot.rotulo == "foco")
        outro = (foco + 1) % cenario.jogadores
        for partida in range(cenario.partidas):
            venceu = partida < round(taxa * cenario.partidas)
            linhas.append({"cenario": cenario.nome, "erro": None, "vencedores": [foco if venceu else outro]})
    return lido, linhas


@pytest.mark.parametrize(
    ("taxas", "esperado"),
    [
        # a se sai melhor que b contra as duas mesas: a é dominante.
        ({("a", "b"): 0.60, ("b", "a"): 0.05}, "falha"),
        # cada um invade a mesa do outro: ninguém é dominante.
        ({("a", "b"): 0.60, ("b", "a"): 0.60}, "passa"),
        # contra a mesa de a, b fica colado em 1/4: não dá para afirmar nem descartar que a domina.
        ({("a", "b"): 0.60, ("b", "a"): 0.25}, "inconclusivo"),
    ],
)
def test_estilo_dominante(taxas: dict[tuple[str, str], float], esperado: str) -> None:
    from critical_failure.metricas.matrizes import medidas_de_dominancia, montar_matrizes

    lido, linhas = _matriz_sintetica(taxas)
    (matriz,) = montar_matrizes(linhas, lido, 0.0)
    assert matriz.completa and matriz.estilos == ("a", "b")
    assert matriz.celulas[("a", "a")].taxa == 0.25 and matriz.celulas[("a", "a")].intervalo is None
    assert matriz.celulas[("a", "b")].taxa == pytest.approx(taxas[("a", "b")])
    (medida,) = medidas_de_dominancia([matriz], {"diferenca_minima": 0.0})
    assert medida.requisito == "REQ-04" and medida.veredito == esperado
    if esperado == "falha":
        assert matriz.situacao == {"a": "dominante", "b": "não dominante"}
        assert matriz.replicador["a"] == pytest.approx(1.0)


def test_experimento_do_melhor_estilo_em_miniatura(tmp_path: Path) -> None:
    construtor = {"tipo": "construtor", "parametros": PERFIL}
    heuristico = {"tipo": "heuristico", "parametros": PERFIL}
    aleatorio = {"tipo": "aleatorio", "parametros": {"explicacao_correta": 0.85, "precisao_auditor": 0.95}}
    estilos = {"construtor": construtor, "heuristico": heuristico, "aleatorio": aleatorio}
    cenarios = [
        celula(
            f"{a}_contra_{b}",
            estilos[a],
            estilos[b],
            a,
            b,
            **({"requisitos": ["REQ-03"]} if (a, b) == ("heuristico", "aleatorio") else {}),
        )
        for a in estilos
        for b in estilos
        if a != b
    ]
    cenarios.append(
        {
            "nome": "todos_heuristicos",
            "regras": "configs/regras_v2_2_1.yaml",
            "jogadores": 4,
            "partidas": 6,
            "bots": [heuristico],
            "requisitos": ["REQ-01", "REQ-11"],
        }
    )
    resultado = rodar(tmp_path, cenarios=cenarios)
    assert resultado.manifest["partidas"] == 6 * 8 + 6
    assert {"REQ-03", "REQ-04", "REQ-11"} <= set(resultado.manifest["vereditos"])
    cheios = [linha["cheios_no_planejamento_1"] for linha in resultado.linhas]
    assert all(c is not None and len(c) == 4 for c in cheios)
    texto = (resultado.pasta / "relatorio.md").read_text(encoding="utf-8")
    for trecho in (
        "## Matriz de estilos (MET-07 e REQ-04)",
        "### estilos_teste (4 jogadores",
        "### REQ-03",
        "### REQ-04",
        "### REQ-11",
        "Dinâmica do replicador",
        "| construtor_contra_heuristico | 8 |",  # as 4 rotações da célula numa linha só da descrição
        "| construtor_contra_heuristico (rotações somadas) |",
    ):
        assert trecho in texto, trecho
    # As células da matriz não se repetem na tabela geral de taxa de vitória por bot, não entram no MET-01
    # e não criam a seção da matriz de políticas de alvo da v1 (MET-02).
    assert "| construtor_contra_heuristico | foco |" not in texto
    assert "| construtor_contra_heuristico | v2 |" not in texto and "| todos_heuristicos | v2 |" in texto
    assert "## Política de alvo (MET-02)" not in texto
    # O relatório refeito do manifest e da tabela é igual ao original.
    assert cli.main(["relatorio", str(resultado.pasta)]) == 0
    assert (resultado.pasta / "relatorio.md").read_text(encoding="utf-8") == texto


def test_celula_de_matriz_mal_formada() -> None:
    base = celula("x", ALEATORIO, ALEATORIO, "a", "b")
    with pytest.raises(ConfiguracaoInvalida):
        ler_experimento(experimento(cenarios=[{**base, "celula": ["a", "a"]}]))
    with pytest.raises(ConfiguracaoInvalida):
        ler_experimento(experimento(cenarios=[{**base, "bots": [ALEATORIO] * 4}]))


def test_experimento_da_fase_4_melhor_estilo_e_valido() -> None:
    lido = carregar_experimento(RAIZ / "experimentos" / "fase4_melhor_estilo.yaml")
    celulas = {(c.matriz, tuple(c.celula)) for c in lido.cenarios if c.celula}
    assert len(celulas) == 2 * 6 * 5
    por_celula: dict[tuple[str, ...], int] = {}
    for c in lido.cenarios_expandidos():
        if c.celula:
            chave = (str(c.matriz), *c.celula)
            por_celula[chave] = por_celula.get(chave, 0) + c.partidas
    assert set(por_celula.values()) == {2000}
    assert [c.nome for c in lido.cenarios if "REQ-03" in c.requisitos] == [
        "n4_heuristico_contra_aleatorio",
        "n5_heuristico_contra_aleatorio",
    ]

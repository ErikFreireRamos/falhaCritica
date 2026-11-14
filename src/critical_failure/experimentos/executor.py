"""Executor de experimentos.

Roda os cenários de um arquivo de experimento, em paralelo, e grava numa pasta:

- ``partidas.parquet``: uma linha por partida (placar, vencedores, duração...);
- ``registros/``: o registro de auditoria completo de uma amostra das partidas
  e de **toda** partida que falhar;
- ``manifest.json``: tudo o que identifica a execução (experimento, hashes das
  configurações, semente, commit, comando, ambiente e hash dos arquivos gerados);
- ``relatorio.md``: os requisitos medidos, com intervalo de confiança e veredito.

O resultado não depende do número de processos: a aleatoriedade de cada partida
vem só da semente mestre e do índice da partida.
"""

from __future__ import annotations

import hashlib
import json
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import numpy
import pyarrow as pa
import pyarrow.parquet as pq
import yaml

import critical_failure
from critical_failure.auditoria import registro
from critical_failure.bots.fabrica import criar_bot
from critical_failure.duracao import carregar_duracao, ler_duracao
from critical_failure.experimentos.config import Experimento, aplicar_mudancas
from critical_failure.nucleo.canonico import sha256
from critical_failure.nucleo.erros import ConfiguracaoInvalida, ErroCF
from critical_failure.nucleo.rng import sortear_por_pesos
from critical_failure.partida import jogar_partida
from critical_failure.regras.familias import motor_de

RAIZ = registro.RAIZ
PARTIDAS_POR_LOTE = 250
COLUNAS_DA_COLETA = (
    "testes_recebidos",
    "testes_contra_o_menor",
    "zerado_antes_do_ultimo_ciclo",
    "parado_s",
    "cobre_incidente_1",
    "fichas_movimentadas",
    "fichas_de_dano",
    "fichas_de_diagnostico",
    "trocas_de_lider",
    "decisoes_com_escolha",
    "decisoes_avaliadas",
    "decisoes_apertadas",
)
"""Medidas de cada partida da v2 (``coleta.ColetorV2`` e as escolhas do MET-08) que viram colunas
da tabela (vazias na v1)."""
ESCOLHAS = "MET-08"
"""O critério confirmado do MET-08 traz o limiar da escolha apertada, usado durante as partidas."""
ESQUEMA_DO_MANIFEST = "cf-manifest/1"

ESQUEMA_DA_TABELA = pa.schema(
    [
        ("cenario", pa.string()),
        ("familia", pa.string()),
        ("partida", pa.int32()),
        ("jogadores", pa.int8()),
        ("placar", pa.list_(pa.int16())),
        ("vencedores", pa.list_(pa.int8())),
        ("criterio", pa.string()),
        ("eventos", pa.int32()),
        ("duracao_s", pa.int32()),
        ("testes", pa.int16()),
        ("contestacoes", pa.int16()),
        ("reembaralhamentos", pa.int16()),
        ("compras_impossiveis", pa.int16()),
        ("reposicoes_impossiveis", pa.int16()),
        ("placar_no_corte", pa.list_(pa.int16())),
        ("cheios_no_planejamento_1", pa.list_(pa.bool_())),
        ("blefes", pa.int16()),
        ("blefes_bem_sucedidos", pa.int16()),
        ("testes_recebidos", pa.list_(pa.int16())),
        ("testes_contra_o_menor", pa.int16()),
        ("zerado_antes_do_ultimo_ciclo", pa.bool_()),
        ("parado_s", pa.list_(pa.int32())),
        ("cobre_incidente_1", pa.list_(pa.bool_())),
        ("fichas_movimentadas", pa.int32()),
        ("fichas_de_dano", pa.int32()),
        ("fichas_de_diagnostico", pa.int32()),
        ("trocas_de_lider", pa.int16()),
        ("decisoes_com_escolha", pa.list_(pa.int16())),
        ("decisoes_avaliadas", pa.list_(pa.int16())),
        ("decisoes_apertadas", pa.list_(pa.int16())),
        ("bots_da_mesa", pa.list_(pa.string())),
        ("erro", pa.string()),
        ("aviso", pa.string()),
    ]
)


class ExperimentoRecusado(ErroCF):
    """O experimento não pode rodar como oficial no estado atual do repositório."""


@dataclass(frozen=True)
class Lote:
    """Um pedaço de um cenário, rodado num processo. Só tipos simples, para ir a outro processo."""

    cenario: str
    arquivo_de_regras: str
    regras: dict[str, Any]
    bots: tuple[tuple[str, tuple[tuple[str, Any], ...]], ...]
    duracao: dict[str, Any] | None
    semente: int
    partidas: tuple[int, ...]
    um_a_cada: int
    pasta_dos_registros: str
    conferir_invariantes: bool
    familia: str
    jogadores: int
    pesos: tuple[int, ...] | None = None
    """Mesa sorteada: ``bots`` são os candidatos, e cada assento é sorteado com estes pesos."""
    rotulos: tuple[str, ...] = ()
    """Nome de cada candidato, para a coluna ``bots_da_mesa``."""
    limiar_da_escolha_apertada: float | None = None
    """MET-08: a margem abaixo da qual uma decisão conta como apertada; ``None`` se o cenário não mede."""


@dataclass(frozen=True)
class Execucao:
    pasta: Path
    manifest: dict[str, Any]
    linhas: list[dict[str, Any]]


def _linha_de_falha(lote: Lote, partida: int, erro: Exception) -> dict[str, Any]:
    return {
        "cenario": lote.cenario,
        "familia": lote.familia,
        "partida": partida,
        "jogadores": lote.jogadores,
        "placar": None,
        "vencedores": None,
        "criterio": None,
        "eventos": None,
        "duracao_s": None,
        "testes": None,
        "contestacoes": None,
        "reembaralhamentos": None,
        "compras_impossiveis": None,
        "reposicoes_impossiveis": None,
        "placar_no_corte": None,
        "cheios_no_planejamento_1": None,
        "blefes": None,
        "blefes_bem_sucedidos": None,
        "testes_recebidos": None,
        "testes_contra_o_menor": None,
        "zerado_antes_do_ultimo_ciclo": None,
        "parado_s": None,
        "cobre_incidente_1": None,
        "fichas_movimentadas": None,
        "fichas_de_dano": None,
        "fichas_de_diagnostico": None,
        "bots_da_mesa": None,
        "erro": f"{type(erro).__name__}: {erro}",
        "aviso": None,
    }


def rodar_lote(lote: Lote) -> list[dict[str, Any]]:
    """Roda as partidas de um lote e devolve uma linha por partida. Nunca levanta exceção de partida."""
    motor = motor_de(lote.regras, registro.PASTA_CONFIGS)
    # O modelo de duração (MOD-05) só existe para a família v2.
    modelo = ler_duracao(lote.duracao) if lote.duracao is not None and motor.familia == "v2" else None
    pasta = Path(lote.pasta_dos_registros) / lote.cenario

    def indices_da_mesa(partida: int) -> list[int]:
        if lote.pesos is None:
            return list(range(len(lote.bots)))
        return sortear_por_pesos(lote.semente, partida, lote.jogadores, lote.pesos)

    def novos_bots(partida: int) -> list[Any]:
        return [criar_bot(lote.bots[i][0], dict(lote.bots[i][1]), motor.familia) for i in indices_da_mesa(partida)]

    def gravar_registro(partida: int, prefixo: str) -> str | None:
        """Refaz a partida no modo auditado e grava o registro completo.

        Se o arquivo não puder ser gravado (disco cheio, pasta sincronizada travada...),
        devolve um aviso em vez de derrubar o experimento inteiro.
        """
        caminho = pasta / f"{prefixo}_{partida:07d}.jsonl"
        try:
            linhas, _ = registro.gerar_linhas(
                motor, lote.arquivo_de_regras, novos_bots(partida), lote.semente, partida, duracao=modelo
            )
        except ErroCF as erro:
            linhas = getattr(erro, "linhas", [])
        except Exception as erro:  # noqa: BLE001 - a falha já está na tabela; aqui só não há registro para gravar
            linhas = [{"registro": "falha_sem_registro", "erro": f"{type(erro).__name__}: {erro}"}]
        try:
            registro.escrever(caminho, linhas)
        except OSError as erro:
            return f"registro não gravado em {caminho.name}: {type(erro).__name__}: {erro}"
        return None

    saida: list[dict[str, Any]] = []
    for partida in lote.partidas:
        try:
            resultado = jogar_partida(
                motor,
                novos_bots(partida),
                lote.semente,
                partida,
                duracao=modelo,
                conferir_invariantes=lote.conferir_invariantes,
                limiar_da_escolha_apertada=lote.limiar_da_escolha_apertada,
            )
        except Exception as erro:  # noqa: BLE001 - REQ-09: qualquer exceção numa partida é uma falha a registrar
            saida.append(_linha_de_falha(lote, partida, erro))
            saida[-1]["aviso"] = gravar_registro(partida, "falha")
            continue
        saida.append(
            {
                "cenario": lote.cenario,
                "familia": motor.familia,
                "partida": partida,
                "jogadores": resultado.n_jogadores,
                "placar": list(resultado.placar),
                "vencedores": list(resultado.vencedores),
                "criterio": resultado.criterio,
                "eventos": resultado.eventos,
                "duracao_s": resultado.duracao_s,
                "testes": resultado.vezes("teste"),
                "contestacoes": resultado.vezes("contestacao"),
                "reembaralhamentos": resultado.vezes("reembaralhamento"),
                "compras_impossiveis": resultado.vezes("compra_impossivel"),
                "reposicoes_impossiveis": resultado.vezes("reposicao_impossivel"),
                "placar_no_corte": list(resultado.placar_no_corte) if resultado.placar_no_corte else None,
                "cheios_no_planejamento_1": (
                    list(resultado.sistemas_cheios_no_planejamento)
                    if resultado.sistemas_cheios_no_planejamento is not None
                    else None
                ),
                "blefes": resultado.blefes,
                "blefes_bem_sucedidos": resultado.blefes_bem_sucedidos,
                **{coluna: resultado.medidas.get(coluna) for coluna in COLUNAS_DA_COLETA},
                "bots_da_mesa": (
                    [lote.rotulos[i] for i in indices_da_mesa(partida)] if lote.pesos is not None else None
                ),
                "erro": None,
                "aviso": None,
            }
        )
        if partida % lote.um_a_cada == 0:
            saida[-1]["aviso"] = gravar_registro(partida, "partida")
    return saida


def hash_do_arquivo(caminho: Path) -> str:
    return "sha256:" + hashlib.sha256(caminho.read_bytes()).hexdigest()


def _ler_yaml(caminho: Path) -> Any:
    try:
        return yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as erro:
        raise ConfiguracaoInvalida(f"não foi possível ler {caminho}: {erro}") from erro


def montar_lotes(experimento: Experimento, pasta_dos_registros: Path) -> tuple[list[Lote], list[dict[str, Any]]]:
    """Divide os cenários em lotes e devolve também o resumo de cada cenário para o manifest."""
    from critical_failure.metricas.requisitos import carregar_requisitos, criterio_confirmado

    duracao_do_experimento = carregar_duracao(RAIZ / experimento.duracao).resolvido()
    escolhas = criterio_confirmado(carregar_requisitos(RAIZ / experimento.requisitos_arquivo), ESCOLHAS)
    lotes: list[Lote] = []
    resumos: list[dict[str, Any]] = []
    for cenario in experimento.cenarios_expandidos():
        duracao = carregar_duracao(RAIZ / cenario.duracao).resolvido() if cenario.duracao else duracao_do_experimento
        dados = aplicar_mudancas(_ler_yaml(RAIZ / cenario.regras), cenario.mudancas)
        motor = motor_de(dados, registro.PASTA_CONFIGS)
        regras, catalogo = motor.regras, motor.catalogo
        motor.preparar(cenario.jogadores, experimento.semente_mestre, 0)  # valida o cenário
        bots = cenario.bots if cenario.pesos is not None else cenario.bots_por_assento()
        for bot in bots:
            criar_bot(bot.tipo, bot.parametros, motor.familia)  # valida os bots antes de gastar tempo de máquina
        resumos.append(
            {
                "nome": cenario.nome,
                "regras": cenario.regras,
                "versao": regras.versao,
                "familia": motor.familia,
                "mudancas": cenario.mudancas,
                "config_hash": regras.hash(),
                "catalogo_hash": catalogo.hash,
                "jogadores": cenario.jogadores,
                "partidas": cenario.partidas,
                "bots": [bot.model_dump(mode="json") for bot in bots],
                "grupo": cenario.grupo or cenario.nome,
                "comparar_com": cenario.comparar_com,
                "celula": cenario.celula,
                "pesos": cenario.pesos,
                **(
                    {"duracao": {"arquivo": cenario.duracao, "sha256": carregar_duracao(RAIZ / cenario.duracao).hash()}}
                    if cenario.duracao
                    else {}
                ),
                "matriz": cenario.matriz,
                "requisitos": cenario.requisitos,
            }
        )
        indices = range(cenario.partidas)
        for inicio in range(0, cenario.partidas, PARTIDAS_POR_LOTE):
            lotes.append(
                Lote(
                    cenario=cenario.nome,
                    arquivo_de_regras=cenario.regras,
                    regras=regras.resolvida(),
                    bots=tuple((bot.tipo, tuple(sorted(bot.parametros.items()))) for bot in bots),
                    duracao=duracao,
                    semente=experimento.semente_mestre,
                    partidas=tuple(indices[inicio : inicio + PARTIDAS_POR_LOTE]),
                    um_a_cada=experimento.registros_completos_um_a_cada,
                    pasta_dos_registros=str(pasta_dos_registros),
                    conferir_invariantes=experimento.conferir_invariantes,
                    familia=motor.familia,
                    jogadores=cenario.jogadores,
                    pesos=tuple(cenario.pesos) if cenario.pesos is not None else None,
                    rotulos=tuple(bot.nome() for bot in bots),
                    limiar_da_escolha_apertada=(
                        float(escolhas["limiar_da_escolha_apertada"])
                        if escolhas is not None and ESCOLHAS in cenario.requisitos
                        else None
                    ),
                )
            )
    return lotes, resumos


def executar(
    experimento: Experimento,
    arquivo: Path,
    saida: Path | None = None,
    processos: int = 1,
    oficial: bool = False,
    comando: str = "",
) -> Execucao:
    """Roda o experimento inteiro e grava tabela, registros, manifest e relatório."""
    from critical_failure.metricas.analise import analisar
    from critical_failure.metricas.requisitos import carregar_requisitos
    from critical_failure.relatorios.markdown import renderizar

    git = registro.info_git()
    if oficial and git["sujo"] is not False:
        raise ExperimentoRecusado(
            "experimento oficial exige o repositório sem alterações não commitadas: "
            "o commit do manifest precisa identificar exatamente o código que rodou"
        )
    inicio = datetime.now(UTC)
    relogio = time.perf_counter()
    carimbo = inicio.strftime("%Y%m%d-%H%M%S") + "-" + (git["commit"] or "semgit")[:7]
    pasta = saida if saida is not None else RAIZ / "resultados" / experimento.nome / carimbo
    pasta.mkdir(parents=True, exist_ok=True)

    lotes, cenarios = montar_lotes(experimento, pasta / "registros")
    if processos > 1:
        with ProcessPoolExecutor(max_workers=processos) as executor:
            blocos = list(executor.map(rodar_lote, lotes))
    else:
        blocos = [rodar_lote(lote) for lote in lotes]
    linhas = [linha for bloco in blocos for linha in bloco]

    caminho_da_tabela = pasta / "partidas.parquet"
    pq.write_table(pa.Table.from_pylist(linhas, schema=ESQUEMA_DA_TABELA), caminho_da_tabela, compression="zstd")

    requisitos = carregar_requisitos(RAIZ / experimento.requisitos_arquivo)
    analise = analisar(linhas, experimento, requisitos)
    medidas = analise.medidas
    falhas = sum(1 for linha in linhas if linha["erro"] is not None)
    registros = sorted(p.relative_to(pasta).as_posix() for p in (pasta / "registros").rglob("*.jsonl"))
    manifest: dict[str, Any] = {
        "esquema": ESQUEMA_DO_MANIFEST,
        "experimento": {
            "arquivo": arquivo.as_posix(),
            "sha256": sha256(experimento.resolvido()),
            "conteudo": experimento.resolvido(),
        },
        "semente_mestre": experimento.semente_mestre,
        "cenarios": cenarios,
        "duracao": {"arquivo": experimento.duracao, "sha256": carregar_duracao(RAIZ / experimento.duracao).hash()},
        "requisitos": {
            "arquivo": experimento.requisitos_arquivo,
            "sha256": hash_do_arquivo(RAIZ / experimento.requisitos_arquivo),
        },
        "git": git,
        "oficial": oficial,
        "comando": comando,
        "ambiente": {
            "motor": critical_failure.__version__,
            "python": platform.python_version(),
            "numpy": numpy.__version__,
            "pyarrow": pa.__version__,
            "plataforma": platform.platform(),
        },
        "inicio": inicio.isoformat(timespec="seconds"),
        "segundos": round(time.perf_counter() - relogio, 1),
        "processos": processos,
        "invariantes_conferidos_a_cada_evento": experimento.conferir_invariantes,
        "partidas": len(linhas),
        "falhas": falhas,
        "registros_completos": len(registros),
        "registros_nao_gravados": sum(1 for linha in linhas if linha.get("aviso")),
        "vereditos": {
            requisito: sorted({m.veredito for m in medidas if m.requisito == requisito})
            for requisito in sorted({m.requisito for m in medidas})
        },
    }
    relatorio = renderizar(manifest, analise)
    (pasta / "relatorio.md").write_text(relatorio, encoding="utf-8", newline="\n")
    manifest["arquivos"] = {
        "partidas.parquet": hash_do_arquivo(caminho_da_tabela),
        "relatorio.md": hash_do_arquivo(pasta / "relatorio.md"),
    }
    (pasta / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
    )
    return Execucao(pasta, manifest, linhas)


def ler_tabela(pasta: Path) -> list[dict[str, Any]]:
    """Lê ``partidas.parquet`` de uma execução como lista de linhas."""
    linhas: list[dict[str, Any]] = pq.read_table(pasta / "partidas.parquet").to_pylist()
    return linhas


def comando_atual() -> str:
    return "cf " + " ".join(sys.argv[1:])

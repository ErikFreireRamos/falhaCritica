"""Linha de comando ``cf``.

cf jogar        joga uma partida entre bots e, se pedido, grava o registro
cf replay       refaz uma partida a partir do registro e confere cada evento
cf narrar       conta a partida em português
cf folha        exporta a Folha de registro em CSV
cf experimento  roda muitas partidas a partir de um arquivo de experimento
cf relatorio    refaz o relatório de um experimento já rodado
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from critical_failure.auditoria import folha, registro, replay
from critical_failure.auditoria.narrar import narrar
from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.bots.fabrica import criar_bot
from critical_failure.duracao import carregar_duracao
from critical_failure.experimentos import executor
from critical_failure.experimentos.config import carregar_experimento, ler_experimento
from critical_failure.metricas.requisitos import (
    avaliar,
    carregar_requisitos,
    descrever,
    desequilibrio,
    vitorias_por_bot,
)
from critical_failure.nucleo.erros import ConfiguracaoInvalida, ErroCF
from critical_failure.regras.familias import carregar_motor
from critical_failure.relatorios.markdown import renderizar

REGRAS_PADRAO = registro.PASTA_CONFIGS / "regras_v2_2_1.yaml"
DURACAO_PADRAO = registro.PASTA_CONFIGS / "duracao.yaml"


def _relativo(caminho: Path) -> str:
    """Caminho relativo à raiz do projeto, com barras normais, para o cabeçalho."""
    try:
        return caminho.resolve().relative_to(registro.RAIZ).as_posix()
    except ValueError:
        return caminho.as_posix()


def _jogar(args: argparse.Namespace) -> int:
    motor = carregar_motor(args.regras)
    jogadores = args.jogadores if args.jogadores is not None else motor.regras.jogadores.minimo.valor
    bots = [criar_bot(BotAleatorio.tipo, {}, motor.familia) for _ in range(jogadores)]
    duracao = carregar_duracao(DURACAO_PADRAO) if motor.familia == "v2" else None
    linhas, resultado = registro.gerar_linhas(
        motor, _relativo(args.regras), bots, args.semente, args.partida, duracao=duracao
    )
    if args.log is not None:
        registro.escrever(args.log, linhas)
        print(f"registro gravado em {args.log} ({resultado.eventos} eventos)")
    if args.narrar:
        print(narrar(linhas, motor.catalogo, mostrar_oculto=not args.sem_oculto, citar_regras=args.regras_citadas))
    else:
        placar = ", ".join(str(fichas) for fichas in resultado.placar)
        minutos = (resultado.duracao_s or 0) // 60
        print(
            f"placar: {placar} | vencedores: {list(resultado.vencedores)} | critério: {resultado.criterio} | "
            f"duração estimada: {minutos} min"
        )
    return 0


def _experimento(args: argparse.Namespace) -> int:
    experimento = carregar_experimento(args.arquivo)
    processos = args.processos if args.processos is not None else max(1, (os.cpu_count() or 2) - 1)
    execucao = executor.executar(
        experimento,
        Path(_relativo(args.arquivo)),
        saida=args.saida,
        processos=processos,
        oficial=args.oficial,
        comando=executor.comando_atual(),
    )
    manifest = execucao.manifest
    print(f"{manifest['partidas']} partidas em {manifest['segundos']} s, com {processos} processo(s)")
    print(f"falhas: {manifest['falhas']} | registros completos: {manifest['registros_completos']}")
    for requisito, vereditos in manifest["vereditos"].items():
        print(f"{requisito}: {', '.join(vereditos)}")
    print(f"resultados em {execucao.pasta}")
    return 0


def _relatorio(args: argparse.Namespace) -> int:
    try:
        manifest = json.loads((args.pasta / "manifest.json").read_text(encoding="utf-8"))
        experimento = ler_experimento(manifest["experimento"]["conteudo"])
    except (OSError, ValueError, KeyError) as erro:
        raise ConfiguracaoInvalida(f"{args.pasta} não é a pasta de um experimento rodado: {erro!r}") from erro
    linhas = executor.ler_tabela(args.pasta)
    requisitos = carregar_requisitos(registro.RAIZ / experimento.requisitos_arquivo)
    texto = renderizar(
        manifest,
        avaliar(linhas, experimento, requisitos),
        descrever(linhas, experimento),
        vitorias_por_bot(linhas, experimento),
        desequilibrio(linhas, experimento, requisitos),
    )
    (args.pasta / "relatorio.md").write_text(texto, encoding="utf-8", newline="\n")
    print(texto)
    return 0


def _replay(args: argparse.Namespace) -> int:
    linhas = registro.ler(args.log)
    modos = replay.MODOS if args.modo == "ambos" else (args.modo,)
    for modo in modos:
        resultado = replay.refazer(linhas, modo)
        print(f"replay ({resultado.modo}): {resultado.eventos} eventos conferidos, nenhuma divergência")
    return 0


def _narrar(args: argparse.Namespace) -> int:
    linhas = registro.ler(args.log)
    catalogo = replay.motor_do_cabecalho(linhas[0]).catalogo
    print(narrar(linhas, catalogo, mostrar_oculto=not args.sem_oculto, citar_regras=args.regras_citadas))
    return 0


def _folha(args: argparse.Namespace) -> int:
    linhas = registro.ler(args.log)
    pasta = args.saida if args.saida is not None else args.log.parent
    for caminho in folha.exportar(linhas, pasta, args.log.stem):
        print(f"escrito {caminho}")
    return 0


def _opcoes_de_narracao(analisador: argparse.ArgumentParser) -> None:
    analisador.add_argument("--sem-oculto", action="store_true", help="não mostra o que estava oculto na mesa")
    analisador.add_argument("--regras-citadas", action="store_true", help="cita a regra da especificação em cada passo")


def montar_analisador() -> argparse.ArgumentParser:
    analisador = argparse.ArgumentParser(prog="cf", description="Simulador do jogo de cartas Critical Failure")
    comandos = analisador.add_subparsers(dest="comando", required=True)

    jogar = comandos.add_parser("jogar", help="joga uma partida entre bots aleatórios")
    jogar.add_argument("--regras", type=Path, default=REGRAS_PADRAO, help="arquivo YAML das regras")
    jogar.add_argument("--jogadores", type=int, default=None, help="número de jogadores (padrão: o mínimo)")
    jogar.add_argument("--semente", type=int, default=1, help="semente mestre")
    jogar.add_argument("--partida", type=int, default=0, help="índice da partida dentro da semente")
    jogar.add_argument("--log", type=Path, default=None, help="grava o registro de auditoria neste arquivo")
    jogar.add_argument("--narrar", action="store_true", help="imprime a narração da partida")
    _opcoes_de_narracao(jogar)
    jogar.set_defaults(funcao=_jogar)

    refazer = comandos.add_parser("replay", help="refaz a partida e confere o estado_hash de cada evento")
    refazer.add_argument("log", type=Path)
    refazer.add_argument("--modo", choices=[*replay.MODOS, "ambos"], default="ambos")
    refazer.set_defaults(funcao=_replay)

    narracao = comandos.add_parser("narrar", help="conta a partida em português")
    narracao.add_argument("log", type=Path)
    _opcoes_de_narracao(narracao)
    narracao.set_defaults(funcao=_narrar)

    exportar = comandos.add_parser("folha", help="exporta a Folha de registro em três arquivos CSV")
    exportar.add_argument("log", type=Path)
    exportar.add_argument("--saida", type=Path, default=None, help="pasta de destino (padrão: a do registro)")
    exportar.set_defaults(funcao=_folha)

    experimento = comandos.add_parser("experimento", help="roda um experimento e grava tabela, manifest e relatório")
    experimento.add_argument("arquivo", type=Path, help="arquivo YAML do experimento")
    experimento.add_argument("--processos", type=int, default=None, help="processos em paralelo (padrão: núcleos - 1)")
    experimento.add_argument("--saida", type=Path, default=None, help="pasta de saída (padrão: resultados/<nome>/...)")
    experimento.add_argument(
        "--oficial", action="store_true", help="recusa rodar se houver alteração não commitada no repositório"
    )
    experimento.set_defaults(funcao=_experimento)

    relatorio = comandos.add_parser("relatorio", help="refaz o relatório a partir do manifest e da tabela de partidas")
    relatorio.add_argument("pasta", type=Path, help="pasta de um experimento já rodado")
    relatorio.set_defaults(funcao=_relatorio)
    return analisador


def main(argumentos: list[str] | None = None) -> int:
    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(encoding="utf-8")
    args = montar_analisador().parse_args(argumentos)
    try:
        return int(args.funcao(args))
    except ErroCF as erro:
        print(f"erro: {type(erro).__name__}: {erro}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

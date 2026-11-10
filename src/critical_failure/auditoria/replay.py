"""Refaz uma partida a partir do registro e confere cada evento.

Dois modos:

- ``acoes``: o motor sozinho reaplica as ações gravadas, sem bots. Confere o
  motor e serve também para registros que não vieram de bots.
- ``bots``: recria os bots do cabeçalho e joga de novo. Confere o conjunto
  inteiro, inclusive a aleatoriedade dos bots.

Qualquer diferença, em qualquer campo de qualquer evento, é erro.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from critical_failure.auditoria.registro import (
    EVENTO,
    PASTA_CONFIGS,
    Linha,
    gerar_linhas,
    linha_do_evento,
)
from critical_failure.bots.fabrica import criar_bot
from critical_failure.duracao import ler_duracao
from critical_failure.nucleo.canonico import como_dict, sha256
from critical_failure.nucleo.erros import ErroCF, RegistroDivergente
from critical_failure.regras.familias import Motor, motor_de

MODO_ACOES = "acoes"
MODO_BOTS = "bots"
MODOS = (MODO_ACOES, MODO_BOTS)


@dataclass(frozen=True, slots=True)
class ResultadoReplay:
    modo: str
    eventos: int


def motor_do_cabecalho(cabecalho: Linha) -> Motor:
    """Monta o motor com a configuração gravada no registro, não com a do disco."""
    motor = motor_de(cabecalho.get("config"), PASTA_CONFIGS)
    if motor.regras.hash() != cabecalho.get("config_hash"):
        raise RegistroDivergente("o hash da configuração não corresponde à configuração gravada")
    if motor.catalogo.hash != cabecalho.get("catalogo_hash"):
        raise RegistroDivergente(
            "o catálogo de cartas mudou desde que o registro foi gravado; "
            "use o commit indicado no cabeçalho para refazer a partida"
        )
    return motor


def _comparar(esperada: Linha, gerada: Linha, ignorar: tuple[str, ...] = ()) -> None:
    for campo in sorted(set(esperada) | set(gerada)):
        if campo in ignorar:
            continue
        if esperada.get(campo) != gerada.get(campo):
            raise RegistroDivergente(
                f"evento {esperada.get('seq', '?')} ({esperada.get('tipo', esperada.get('registro'))}): "
                f"campo '{campo}' diverge. Registro: {esperada.get(campo)!r}. Reexecução: {gerada.get(campo)!r}"
            )


def _por_acoes(linhas: list[Linha], motor: Motor) -> int:
    cabecalho, fim = linhas[0], linhas[-1]
    esperadas = [linha for linha in linhas if linha.get("registro") == EVENTO]
    estado: Any
    estado, eventos = motor.preparar(cabecalho["jogadores"], cabecalho["semente_mestre"], cabecalho["partida"])
    geradas = [linha_do_evento(seq, evento, None) for seq, evento in enumerate(eventos)]
    conferidas = 0
    while True:
        if len(geradas) > len(esperadas):
            raise RegistroDivergente(f"a reexecução gerou mais eventos ({len(geradas)}) do que o registro")
        for posicao in range(conferidas, len(geradas)):
            _comparar(esperadas[posicao], geradas[posicao], ignorar=("decisao",))
        conferidas = len(geradas)
        if conferidas == len(esperadas):
            break
        proxima = esperadas[conferidas]
        decisao = proxima.get("decisao")
        if not isinstance(decisao, dict):
            raise RegistroDivergente(f"evento {conferidas}: o registro continua, mas não há decisão para aplicar")
        legais = [opcao.texto() for opcao in motor.acoes_legais(estado)]
        if decisao.get("opcoes") != legais:
            raise RegistroDivergente(f"evento {conferidas}: as opções gravadas não são as ações legais do motor")
        estado, eventos = motor.aplicar(estado, motor.acao_de_dict(decisao.get("acao")))  # type: ignore[arg-type]
        geradas += [linha_do_evento(len(geradas) + k, evento, None) for k, evento in enumerate(eventos)]
    if estado.pendente is not None:
        raise RegistroDivergente("o registro terminou, mas a partida refeita ainda não acabou")
    final: dict[str, Any] = {
        "placar_final": list(motor.placar(estado)),
        "vencedores": list(estado.vencedores),
        "estado_hash_final": sha256(como_dict(estado)),
    }
    gravado = {
        "placar_final": (fim.get("placar") or {}).get("final"),
        "vencedores": fim.get("vencedores"),
        "estado_hash_final": fim.get("estado_hash_final"),
    }
    if final != gravado:
        raise RegistroDivergente(f"o fim da partida diverge. Registro: {gravado}. Reexecução: {final}")
    return conferidas


def _por_bots(linhas: list[Linha], motor: Motor) -> int:
    cabecalho = linhas[0]
    bots = [criar_bot(bot["tipo"], bot["parametros"], motor.familia) for bot in cabecalho["bots"]]
    modelo = (cabecalho.get("modelos") or {}).get("duracao")
    novas, _ = gerar_linhas(
        motor,
        cabecalho["regras"]["arquivo"],
        bots,
        cabecalho["semente_mestre"],
        cabecalho["partida"],
        data_hora=cabecalho["data_hora"],
        duracao=ler_duracao(modelo) if modelo is not None else None,
    )
    if len(novas) != len(linhas):
        raise RegistroDivergente(f"o registro tem {len(linhas)} linhas e a reexecução gerou {len(novas)}")
    _comparar(linhas[0], novas[0], ignorar=("git",))
    for esperada, gerada in zip(linhas[1:], novas[1:], strict=True):
        _comparar(esperada, gerada)
    return len(linhas) - len((linhas[0], linhas[-1]))


def refazer(linhas: list[Linha], modo: str = MODO_ACOES) -> ResultadoReplay:
    """Refaz a partida e confere tudo. Levanta ``RegistroDivergente`` se algo não bater."""
    if modo not in MODOS:
        raise ValueError(f"modo de replay desconhecido: {modo}")
    try:
        motor = motor_do_cabecalho(linhas[0])
        eventos = _por_acoes(linhas, motor) if modo == MODO_ACOES else _por_bots(linhas, motor)
    except RegistroDivergente:
        raise
    except (ErroCF, KeyError, TypeError, ValueError) as erro:
        raise RegistroDivergente(f"não foi possível refazer a partida: {type(erro).__name__}: {erro}") from erro
    return ResultadoReplay(modo, eventos)

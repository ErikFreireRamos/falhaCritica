"""Laço de uma partida: motor, bots e, se pedido, um ouvinte de eventos.

Serve às duas famílias de regras: só usa a interface comum dos motores
(``preparar``, ``acoes_legais``, ``aplicar``, ``observar``,
``conferir_invariantes``, ``placar`` e ``ponto_de_corte``).

O ouvinte recebe cada evento na ordem, com a decisão do bot que o causou. É
assim que o registro de auditoria é escrito, sem que o motor saiba dele.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from critical_failure.bots.base import Bot
from critical_failure.bots.mesa import mesa_para
from critical_failure.duracao import Cronometro, ModeloDeDuracao
from critical_failure.nucleo.erros import ErroCF

if TYPE_CHECKING:
    from critical_failure.regras.familias import Motor

LIMITE_DE_PASSOS = 100_000
"""Guarda do simulador contra laço infinito. Não é número de regra."""

Ouvinte = Callable[[Any, dict[str, Any] | None], None]


class PartidaSemFim(ErroCF):
    """A partida passou do limite de passos sem terminar."""


@dataclass(frozen=True, slots=True)
class ResultadoPartida:
    n_jogadores: int
    placar: tuple[int, ...]
    """Fichas (família v2) ou pontos do sistema (v1) de cada assento no fim."""
    vencedores: tuple[int, ...]
    criterio: str
    """Como o vencedor foi definido: fichas, pontos, alertas, diagnosticos ou dividida."""
    fontes: tuple[dict[str, int], ...]
    """Para cada assento, o saldo de fichas por fonte (vazio na v1)."""
    eventos: int
    estado_final: Any
    duracao_s: int | None = None
    """Duração estimada pelo modelo MOD-05, em segundos. ``None`` sem modelo."""
    tipos_de_evento: tuple[tuple[str, int], ...] = ()
    """Quantas vezes cada tipo de evento aconteceu, em ordem alfabética."""
    placar_no_corte: tuple[int, ...] | None = None
    """REQ-02: o placar no ponto de corte (fichas no fim do ciclo 1; na v1, cartas no sistema
    depois que todos fizeram o primeiro teste)."""
    sistemas_cheios_no_planejamento: tuple[bool, ...] | None = None
    """REQ-11: quem terminou o Planejamento do ciclo 1 com o sistema no teto (só na v2)."""

    def vezes(self, tipo: str) -> int:
        return dict(self.tipos_de_evento).get(tipo, 0)

    @property
    def lider_no_corte(self) -> int | None:
        """O assento que lidera sozinho no ponto de corte; ``None`` se há empate ou não houve corte."""
        if self.placar_no_corte is None:
            return None
        maximo = max(self.placar_no_corte)
        lideres = [assento for assento, valor in enumerate(self.placar_no_corte) if valor == maximo]
        return lideres[0] if len(lideres) == 1 else None


def somar_fontes(fontes: list[dict[str, int]], evento: Any) -> None:
    fichas = evento.publico.get("fichas")
    if fichas:
        fonte = evento.publico["fonte"]
        for assento, variacao in fichas.items():
            fontes[int(assento)][fonte] += variacao


def jogar_partida(
    motor: Motor,
    bots: Sequence[Bot],
    semente: int,
    partida: int,
    ouvinte: Ouvinte | None = None,
    conferir_invariantes: bool = False,
    duracao: ModeloDeDuracao | None = None,
) -> ResultadoPartida:
    n = len(bots)
    mesa = mesa_para(motor)
    for assento, bot in enumerate(bots):
        bot.iniciar(semente, partida, assento, mesa)
    fontes: list[dict[str, int]] = [dict.fromkeys(motor.fontes, 0) for _ in range(n)]
    total = 0
    criterio = ""
    cronometro = Cronometro(duracao) if duracao is not None else None
    tipos: Counter[str] = Counter()
    placar_no_corte: tuple[int, ...] | None = None
    cheios: tuple[bool, ...] | None = None

    def entregar(eventos: Sequence[Any], decisao: dict[str, Any] | None) -> None:
        nonlocal total, criterio, placar_no_corte, cheios
        for posicao, evento in enumerate(eventos):
            if conferir_invariantes:
                motor.conferir_invariantes(evento.estado, em_repouso=posicao == len(eventos) - 1)
            somar_fontes(fontes, evento)
            tipos[evento.tipo] += 1
            if cronometro is not None:
                cronometro.somar(evento)
            if placar_no_corte is None:
                placar_no_corte = motor.ponto_de_corte(evento)
            if cheios is None:
                cheios = motor.sistemas_cheios_no_planejamento(evento)
            if evento.tipo == "fim_de_jogo":
                criterio = evento.publico["criterio"]
            if ouvinte is not None:
                ouvinte(evento, decisao if posicao == 0 else None)
        total += len(eventos)

    estado: Any
    estado, eventos = motor.preparar(n, semente, partida)
    entregar(eventos, None)
    for _ in range(LIMITE_DE_PASSOS):
        pendente = estado.pendente
        if pendente is None:
            break
        opcoes: Sequence[Any] = motor.acoes_legais(estado)
        decisao = bots[pendente.jogador].decidir(motor.observar(estado, pendente.jogador), opcoes)
        estado, eventos = motor.aplicar(estado, decisao.acao)
        entregar(
            eventos,
            {
                "opcoes": [opcao.texto() for opcao in opcoes],
                "escolha": decisao.acao.texto(),
                "acao": decisao.acao.para_dict(),
                "motivo": decisao.motivo,
            },
        )
    else:
        raise PartidaSemFim(f"partida {partida} não terminou em {LIMITE_DE_PASSOS} passos")

    return ResultadoPartida(
        n_jogadores=n,
        placar=motor.placar(estado),
        vencedores=estado.vencedores,
        criterio=criterio,
        fontes=tuple(fontes),
        eventos=total,
        estado_final=estado,
        duracao_s=cronometro.segundos if cronometro is not None else None,
        tipos_de_evento=tuple(sorted(tipos.items())),
        placar_no_corte=placar_no_corte,
        sistemas_cheios_no_planejamento=cheios,
    )

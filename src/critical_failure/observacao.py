"""O que um jogador vê.

``observar(estado, assento, catalogo)`` monta a ``Observacao`` só com o que uma
pessoa sentada naquele assento veria na mesa, seguindo a lista fechada decidida
em AMB-10. Bots recebem a ``Observacao`` e nunca o estado.

Público: fichas e Alertas de todos, Backlog, frente dos incidentes do Radar,
quantas cartas cada um tem na mão e no sistema, cartas pegas do Backlog, cartas
de ataque e descarte, andamento da disputa, cartas reveladas, diagnósticos
depois de revelados, gabarito depois de virado.
Privado: a própria mão e o próprio sistema.
Oculto de todos: a ordem do baralho, o verso dos incidentes e os incidentes
ainda na Linha do Tempo.
"""

from __future__ import annotations

from dataclasses import dataclass

from critical_failure.nucleo.catalogo import Catalogo
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.estado import DisputaEncerrada, Estado


@dataclass(frozen=True, slots=True)
class JogadorVisto:
    assento: int
    fichas: int
    alertas: tuple[str, ...]
    cartas_na_mao: int
    cartas_no_sistema: int
    passou: bool
    acertos: int
    reveladas: tuple[str, ...]
    """Testes do sistema que a mesa já viu."""
    pegas_do_backlog: tuple[str, ...]
    """Testes que a mesa viu o jogador pegar e que ele ainda tem, na mão ou no sistema."""


@dataclass(frozen=True, slots=True)
class IncidenteVisto:
    """A frente de um incidente: sem categoria-chave, secundária nem testes-chave (R-2.1.1)."""

    numero: str
    nome: str
    relato: str


@dataclass(frozen=True, slots=True)
class GabaritoVisto:
    """O verso de um incidente já resolvido (R-8.0.3)."""

    numero: str
    chave: str
    secundaria: str | None
    testes_chave: tuple[str, ...]
    severo: bool


@dataclass(frozen=True, slots=True)
class DisputaVista:
    atacante: int
    defensor: int
    auditor: int
    teste_do_ataque: str
    categoria: str
    etapa: str
    teste_nomeado: str | None
    veredito: str | None
    explicacao_percebida: bool | None
    """Só o Auditor da disputa, na hora de conferir, sabe se a explicação está
    correta: é ele quem tem o Documento do Auditor (R-7.1.2, MOD-02)."""


@dataclass(frozen=True, slots=True)
class Observacao:
    assento: int
    n_jogadores: int
    ciclo: int
    fase: str
    primeiro: int
    auditor: int
    decisao_pedida: str | None
    """Tipo da decisão que o motor espera deste assento; ``None`` se não é a vez dele."""
    compras_restantes: int
    mao: tuple[str, ...]
    sistema: tuple[str, ...]
    jogadores: tuple[JogadorVisto, ...]
    backlog: tuple[str, ...]
    cartas_no_baralho: int
    descarte: tuple[str, ...]
    radar_agora: IncidenteVisto | None
    radar_proximo: IncidenteVisto | None
    gabaritos: tuple[GabaritoVisto, ...]
    disputa: DisputaVista | None
    diagnosticos: tuple[str | None, ...]
    """Antes da revelação, só a própria escolha aparece (R-8.0.2b)."""
    historico: tuple[DisputaEncerrada, ...]


def _frente(catalogo: Catalogo, numero: str | None) -> IncidenteVisto | None:
    if numero is None:
        return None
    incidente = catalogo.incidentes[numero]
    return IncidenteVisto(incidente.numero, incidente.nome, incidente.relato)


def observar(estado: Estado, assento: int, catalogo: Catalogo) -> Observacao:
    eu = estado.jogadores[assento]

    def visto(j: int) -> JogadorVisto:
        jogador = estado.jogadores[j]
        return JogadorVisto(
            assento=j,
            fichas=jogador.fichas,
            alertas=jogador.alertas,
            cartas_na_mao=len(jogador.mao),
            cartas_no_sistema=len(jogador.sistema),
            passou=jogador.passou,
            acertos=jogador.acertos,
            reveladas=tuple(sorted(catalogo.nomes(jogador.reveladas))),
            pegas_do_backlog=tuple(sorted(catalogo.nomes(jogador.pegas_do_backlog))),
        )

    disputa: DisputaVista | None = None
    d = estado.disputa
    if d is not None:
        e_o_auditor_conferindo = d.etapa == E.CONFERIR and assento == d.auditor
        disputa = DisputaVista(
            atacante=d.atacante,
            defensor=d.defensor,
            auditor=d.auditor,
            teste_do_ataque=catalogo.teste(d.carta),
            categoria=d.categoria,
            etapa=d.etapa,
            teste_nomeado=d.teste_nomeado,
            veredito=d.veredito,
            explicacao_percebida=d.explicacao_correta if e_o_auditor_conferindo else None,
        )

    todos_escolheram = all(escolha is not None for escolha in estado.diagnosticos)
    diagnosticos = tuple(
        escolha if todos_escolheram or j == assento else None for j, escolha in enumerate(estado.diagnosticos)
    )
    gabaritos = tuple(
        GabaritoVisto(i.numero, i.chave, i.secundaria, i.testes_chave, i.severo)
        for i in (catalogo.incidentes[numero] for numero in estado.resolvidos)
    )
    pendente = estado.pendente
    return Observacao(
        assento=assento,
        n_jogadores=estado.n,
        ciclo=estado.ciclo,
        fase=estado.fase,
        primeiro=estado.primeiro,
        auditor=estado.auditor,
        decisao_pedida=pendente.tipo if pendente is not None and pendente.jogador == assento else None,
        compras_restantes=estado.compras_restantes,
        mao=tuple(catalogo.nomes(eu.mao)),
        sistema=tuple(catalogo.nomes(eu.sistema)),
        jogadores=tuple(visto(j) for j in range(estado.n)),
        backlog=tuple(catalogo.nomes(estado.backlog)),
        cartas_no_baralho=len(estado.baralho),
        descarte=tuple(catalogo.nomes(estado.descarte)),
        radar_agora=_frente(catalogo, estado.agora),
        radar_proximo=_frente(catalogo, estado.proximo),
        gabaritos=gabaritos,
        disputa=disputa,
        diagnosticos=diagnosticos,
        historico=estado.historico,
    )

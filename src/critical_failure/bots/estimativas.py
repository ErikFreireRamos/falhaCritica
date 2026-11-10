"""Estimativas que um bot faz só com a informação pública da mesa.

Um jogador atento sabe quais cartas já viu: as da própria mão e do próprio
sistema, o Backlog, o descarte, as cartas reveladas e as que viu os outros
pegarem do Backlog. As demais cópias de cada teste (o baralho tem a composição
do Apêndice B) estão em algum lugar que ele não vê. A partir disso ele estima a
chance de um adversário não ter um teste ou uma categoria no sistema, por
contagem sem reposição (hipergeométrica).
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable

from critical_failure.bots.mesa import MesaPublica
from critical_failure.observacao import Observacao


def cartas_conhecidas(obs: Observacao) -> Counter[str]:
    """Quantas cópias de cada teste o jogador já sabe onde estão."""
    vistas: Counter[str] = Counter(obs.mao) + Counter(obs.sistema) + Counter(obs.backlog) + Counter(obs.descarte)
    for jogador in obs.jogadores:
        if jogador.assento == obs.assento:
            continue
        # Uma carta pega do Backlog e depois revelada é a mesma carta: conta uma vez.
        vistas += Counter(jogador.reveladas) | Counter(jogador.pegas_do_backlog)
    if obs.disputa is not None:
        vistas[obs.disputa.teste_do_ataque] += 1
    return vistas


def copias_nao_vistas(obs: Observacao, mesa: MesaPublica) -> Counter[str]:
    vistas = cartas_conhecidas(obs)
    return Counter({nome: max(teste.copias - vistas[nome], 0) for nome, teste in mesa.testes.items()})


def chance_de_nao_ter(
    obs: Observacao,
    mesa: MesaPublica,
    alvo: int,
    testes: Iterable[str],
    nao_vistas: Counter[str] | None = None,
) -> float:
    """Chance estimada de o sistema do alvo não ter nenhuma carta destes testes.

    Se o alvo já revelou uma delas, a chance é 0. Se a mesa o viu pegar uma
    delas do Backlog, o bot supõe que ela foi para o sistema e a chance também
    é 0. Senão, as cartas não reveladas do sistema dele são tratadas como
    sorteadas, sem reposição, entre as cartas que o jogador ainda não viu.
    ``nao_vistas`` pode vir já calculado, para não refazer a contagem.
    """
    procurados = set(testes)
    jogador = obs.jogadores[alvo]
    if procurados & (set(jogador.reveladas) | set(jogador.pegas_do_backlog)):
        return 0.0
    escondidas = jogador.cartas_no_sistema - len(jogador.reveladas)
    if nao_vistas is None:
        nao_vistas = copias_nao_vistas(obs, mesa)
    total = sum(nao_vistas.values())
    favoraveis = sum(nao_vistas[teste] for teste in procurados)
    return chance_de_nenhuma(escondidas, total, favoraveis)


def chance_de_nenhuma(escondidas: int, total: int, favoraveis: int) -> float:
    """Chance de, tirando ``escondidas`` cartas sem reposição de ``total``, não sair nenhuma das ``favoraveis``."""
    chance = 1.0
    for retirada in range(escondidas):
        restantes = total - retirada
        if restantes <= 0:
            break
        chance *= max(restantes - favoraveis, 0) / restantes
    return chance


def teste_mais_provavel(obs: Observacao, mesa: MesaPublica, categoria: str) -> str:
    """O teste da categoria com mais cópias que o jogador ainda não viu (desempate pela ordem do catálogo)."""
    nao_vistas = copias_nao_vistas(obs, mesa)
    testes = mesa.testes_por_categoria[categoria]
    return max(testes, key=lambda teste: (nao_vistas[teste], -testes.index(teste)))

"""Pontuação da v1 (V1-4.3.15 a V1-4.3.18, Tabela 4).

Cada carta vale um ponto. Um par (cartas do mesmo atributo e de testes
diferentes) e um trio (cartas de atributos diferentes) valem um bônus. Cada
carta entra em no máximo uma combinação, e vale a divisão das cartas que dá
mais pontos (AMB-24). Os tamanhos e os valores vêm do YAML.

O cálculo é direto, sem busca e sem guardar nada em memória entre partidas:

- de um atributo dá para tirar ``p`` pares se, contando no máximo ``p`` cartas
  de cada teste, sobram pelo menos ``2p`` cartas (cada par precisa de testes
  diferentes);
- para os trios só importa quantas cartas de cada atributo sobraram: dá para
  formar ``t`` trios se, contando no máximo ``t`` cartas de cada atributo,
  sobram pelo menos ``3t`` cartas;
- então basta percorrer quantos pares sair de cada atributo e, para cada
  escolha, calcular o máximo de trios com o que sobrou.

Empate entre divisões com o mesmo bônus: mais pares, depois mais trios.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import product

Carta = tuple[str, str]
"""(atributo, nome do teste)."""


@dataclass(frozen=True, slots=True)
class Pontuacao:
    cartas: int
    pares: int
    trios: int
    total: int


@dataclass(frozen=True, slots=True)
class TabelaDePontos:
    por_carta: int
    por_par: int
    por_trio: int
    cartas_no_par: int
    cartas_no_trio: int


def _cabem(contagens: list[int], grupos: int, por_grupo: int) -> bool:
    """Dá para formar ``grupos`` grupos de ``por_grupo`` itens distintos, com estas contagens por tipo?"""
    return sum(min(contagem, grupos) for contagem in contagens) >= por_grupo * grupos


def _maximo_de_grupos(contagens: list[int], por_grupo: int) -> int:
    grupos = sum(contagens) // por_grupo
    while grupos > 0 and not _cabem(contagens, grupos, por_grupo):
        grupos -= 1
    return grupos


def pontuar(cartas: list[Carta], tabela: TabelaDePontos) -> Pontuacao:
    testes_por_atributo: dict[str, Counter[str]] = {}
    for atributo, teste in cartas:
        testes_por_atributo.setdefault(atributo, Counter())[teste] += 1
    atributos = sorted(testes_por_atributo)
    totais = [sum(testes_por_atributo[a].values()) for a in atributos]
    limites = [_maximo_de_grupos(list(testes_por_atributo[a].values()), tabela.cartas_no_par) for a in atributos]

    melhor = (0, 0, 0)  # (bônus, pares, trios)
    for pares_por_atributo in product(*(range(limite + 1) for limite in limites)):
        sobras = [total - tabela.cartas_no_par * pares for total, pares in zip(totais, pares_por_atributo, strict=True)]
        pares = sum(pares_por_atributo)
        trios = _maximo_de_grupos(sobras, tabela.cartas_no_trio)
        melhor = max(melhor, (pares * tabela.por_par + trios * tabela.por_trio, pares, trios))
    bonus, pares, trios = melhor
    return Pontuacao(len(cartas), pares, trios, len(cartas) * tabela.por_carta + bonus)

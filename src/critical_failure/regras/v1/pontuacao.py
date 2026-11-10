"""Pontuação da v1 (V1-4.3.15 a V1-4.3.18, Tabela 4).

Cada carta vale um ponto. Um par (cartas do mesmo atributo e de testes
diferentes) e um trio (cartas de atributos diferentes) valem um bônus. Cada
carta entra em no máximo uma combinação, e vale a divisão das cartas que dá
mais pontos (AMB-24). Os tamanhos e os valores vêm do YAML.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache
from itertools import combinations

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


def pontuar(cartas: list[Carta], tabela: TabelaDePontos) -> Pontuacao:
    bonus, pares, trios = _melhor(tuple(sorted(cartas)), tabela)
    return Pontuacao(len(cartas), pares, trios, len(cartas) * tabela.por_carta + bonus)


def _e_par(grupo: tuple[Carta, ...]) -> bool:
    return len({atributo for atributo, _ in grupo}) == 1 and len(set(grupo)) == len(grupo)


def _e_trio(grupo: tuple[Carta, ...]) -> bool:
    return len({atributo for atributo, _ in grupo}) == len(grupo)


@cache
def _melhor(resto: tuple[Carta, ...], tabela: TabelaDePontos) -> tuple[int, int, int]:
    """(bônus, pares, trios) da melhor divisão. A primeira carta fica sozinha ou entra num grupo."""
    if not resto:
        return (0, 0, 0)
    primeira, outras = resto[0], resto[1:]
    opcoes = [_melhor(outras, tabela)]
    for tamanho, valido, bonus_do_grupo, e_par in (
        (tabela.cartas_no_par, _e_par, tabela.por_par, True),
        (tabela.cartas_no_trio, _e_trio, tabela.por_trio, False),
    ):
        vistos: set[tuple[Carta, ...]] = set()
        for indices in combinations(range(len(outras)), tamanho - 1):
            companheiras = tuple(outras[i] for i in indices)
            if companheiras in vistos or not valido((primeira, *companheiras)):
                continue
            vistos.add(companheiras)
            sobra = tuple(carta for k, carta in enumerate(outras) if k not in indices)
            bonus, pares, trios = _melhor(sobra, tabela)
            opcoes.append((bonus + bonus_do_grupo, pares + e_par, trios + (not e_par)))
    return max(opcoes)

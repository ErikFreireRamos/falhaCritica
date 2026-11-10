"""O que um bot sabe antes de a partida começar, além do que observa na mesa.

Tudo em ``MesaPublica`` é informação que um jogador real tem: o texto das regras,
o Cartão de Referência com os testes de cada categoria (MOD-06) e a composição
do baralho do Apêndice B, inclusive quantos incidentes são severos (MOD-08).

O gabarito dos incidentes não está aqui. Ele fica guardado no ``Leitor``, que só
devolve a *leitura* que o bot faz de um relato, sorteada com a chance de acerto
do perfil de conhecimento dele (MOD-03 e MOD-04). O código dos bots usa só o
método ``ler``; nenhum bot consulta o gabarito por outro caminho.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import numpy as np

from critical_failure.nucleo.catalogo import Catalogo
from critical_failure.regras.config import RegrasV2
from critical_failure.regras.v2.motor import MotorV2

MIL = 1000


@dataclass(frozen=True, slots=True)
class TestePublico:
    nome: str
    categoria: str
    copias: int


@dataclass(frozen=True, slots=True)
class Leitura:
    categoria: str
    motivo: str


class Leitor:
    """Simula a leitura que um jogador faz do relato de um incidente (MOD-03, MOD-04).

    Com a chance ``diagnostico_certo`` a leitura é a categoria-chave. Ao errar,
    com a chance ``secundaria_no_erro`` ela cai na categoria secundária, se o
    incidente tiver uma; o resto do erro vai, por igual, para as categorias
    vizinhas: as dos testes que o Documento do Auditor manda "não confundir com"
    os testes-chave. Sem vizinhas, o erro vai por igual para as outras categorias.
    """

    def __init__(self, catalogo: Catalogo) -> None:
        self.__gabaritos: dict[str, tuple[str, str | None, tuple[str, ...]]] = {}
        for numero, incidente in catalogo.incidentes.items():
            excluir = {incidente.chave, incidente.secundaria}
            vizinhas: list[str] = []
            for teste in incidente.testes_chave:
                for confundivel in catalogo.testes[teste].nao_confundir:
                    vizinho = catalogo.testes.get(confundivel)
                    if vizinho is not None and vizinho.categoria not in excluir and vizinho.categoria not in vizinhas:
                        vizinhas.append(vizinho.categoria)
            if not vizinhas:
                vizinhas = [categoria for categoria in catalogo.categorias if categoria not in excluir]
            ordem = {categoria: posicao for posicao, categoria in enumerate(catalogo.categorias)}
            vizinhas.sort(key=ordem.__getitem__)
            self.__gabaritos[numero] = (incidente.chave, incidente.secundaria, tuple(vizinhas))

    def ler(self, numero: str, certo_por_mil: int, secundaria_por_mil: int, rng: np.random.Generator) -> Leitura:
        chave, secundaria, vizinhas = self.__gabaritos[numero]
        sorteio = int(rng.integers(MIL))
        if sorteio < certo_por_mil:
            return Leitura(chave, f"leu a categoria certa (p={certo_por_mil}/{MIL}, sorteio={sorteio})")
        if secundaria is not None:
            segundo = int(rng.integers(MIL))
            if segundo < secundaria_por_mil:
                return Leitura(secundaria, f"errou para a secundária (sorteios {sorteio} e {segundo})")
        escolhida = vizinhas[int(rng.integers(len(vizinhas)))]
        return Leitura(escolhida, f"errou para uma categoria vizinha (sorteio={sorteio})")


class MesaPublica:
    """Regras e composição do baralho, como um jogador conhece antes de jogar."""

    def __init__(self, regras: RegrasV2, catalogo: Catalogo) -> None:
        self.regras = regras
        self.categorias = catalogo.categorias
        self.testes = {
            nome: TestePublico(nome, teste.categoria, teste.copias) for nome, teste in catalogo.testes.items()
        }
        self.testes_por_categoria = {
            categoria: tuple(nome for nome, teste in self.testes.items() if teste.categoria == categoria)
            for categoria in self.categorias
        }
        self.total_de_cartas = len(catalogo.cartas)
        severos = sum(1 for incidente in catalogo.incidentes.values() if incidente.severo)
        self.chance_de_severo = severos / len(catalogo.incidentes)
        self.leitor = Leitor(catalogo)

    def categoria(self, teste: str) -> str:
        return self.testes[teste].categoria


@lru_cache(maxsize=16)
def mesa_do_motor(motor: MotorV2) -> MesaPublica:
    """A mesa pública de um motor, montada uma vez só."""
    return MesaPublica(motor.regras, motor.catalogo)

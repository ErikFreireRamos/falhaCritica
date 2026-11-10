"""Catálogo de cartas de Teste e de incidentes.

O catálogo vem de ``configs/catalogo_v2.yaml``, que é gerado a partir da
especificação. Aqui cada carta física ganha um número: as cartas do jogo base
são sempre numeradas primeiro, então ligar o módulo não muda o número delas.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from critical_failure.nucleo.canonico import sha256
from critical_failure.nucleo.erros import ConfiguracaoInvalida

CONJUNTO_BASE = "base"
CONJUNTO_MODULO = "módulo"


@dataclass(frozen=True, slots=True)
class Teste:
    nome: str
    categoria: str
    copias: int
    conjunto: str
    regra: str
    nao_confundir: tuple[str, ...]
    descricao: str


@dataclass(frozen=True, slots=True)
class Incidente:
    numero: str
    nome: str
    chave: str
    secundaria: str | None
    testes_chave: tuple[str, ...]
    severo: bool
    conjunto: str
    relato: str
    regra: str


@dataclass(frozen=True, eq=False)
class Catalogo:
    """Cartas e incidentes ativos numa partida (com ou sem o módulo)."""

    categorias: tuple[str, ...]
    """Categorias ativas, na ordem das faces do dado."""
    faces: tuple[tuple[int, str], ...]
    """Todas as faces do dado, inclusive a do módulo desligado: (face, categoria)."""
    testes: dict[str, Teste]
    incidentes: dict[str, Incidente]
    cartas: tuple[str, ...]
    """Nome do teste de cada carta física; o índice é o número da carta."""
    hash: str
    com_modulo: bool

    def teste(self, carta: int) -> str:
        return self.cartas[carta]

    def categoria(self, carta: int) -> str:
        return self.testes[self.cartas[carta]].categoria

    def testes_da_categoria(self, categoria: str) -> tuple[str, ...]:
        return tuple(t.nome for t in self.testes.values() if t.categoria == categoria)

    def categoria_da_face(self, face: int) -> str | None:
        """Categoria sorteada por uma face; ``None`` se a categoria não está em jogo."""
        for numero, categoria in self.faces:
            if numero == face:
                return categoria if categoria in self.categorias else None
        return None

    def nomes(self, cartas: tuple[int, ...] | list[int]) -> list[str]:
        return [self.cartas[c] for c in cartas]


def ler_catalogo_bruto(caminho: Path) -> dict[str, Any]:
    try:
        dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as erro:
        raise ConfiguracaoInvalida(f"não foi possível ler o catálogo {caminho}: {erro}") from erro
    if not isinstance(dados, dict) or dados.get("esquema") != "cf-catalogo/1":
        raise ConfiguracaoInvalida(f"{caminho} não é um catálogo cf-catalogo/1")
    return dados


def montar_catalogo(bruto: dict[str, Any], com_modulo: bool) -> Catalogo:
    """Monta o catálogo ativo a partir do YAML já lido."""
    try:
        ativos = {CONJUNTO_BASE, CONJUNTO_MODULO} if com_modulo else {CONJUNTO_BASE}
        categorias = tuple(c["nome"] for c in bruto["categorias"] if c["conjunto"] in ativos)
        faces = tuple((int(c["face_do_dado"]), str(c["nome"])) for c in bruto["categorias"])
        testes: dict[str, Teste] = {}
        cartas: list[str] = []
        for t in bruto["testes"]:
            if t["conjunto"] not in ativos:
                continue
            teste = Teste(
                nome=t["nome"],
                categoria=t["categoria"],
                copias=int(t["copias"]),
                conjunto=t["conjunto"],
                regra=t["regra"],
                nao_confundir=tuple(t["nao_confundir"]),
                descricao=t["descricao"],
            )
            if teste.nome in testes or teste.categoria not in categorias:
                raise ConfiguracaoInvalida(f"teste repetido ou de categoria inativa: {teste.nome}")
            testes[teste.nome] = teste
            cartas.extend([teste.nome] * teste.copias)
        incidentes: dict[str, Incidente] = {}
        for i in bruto["incidentes"]:
            if i["conjunto"] not in ativos:
                continue
            incidente = Incidente(
                numero=str(i["numero"]),
                nome=i["nome"],
                chave=i["chave"],
                secundaria=i["secundaria"],
                testes_chave=tuple(i["testes_chave"]),
                severo=bool(i["severo"]),
                conjunto=i["conjunto"],
                relato=i["relato"],
                regra=i["regra"],
            )
            if incidente.chave not in categorias:
                raise ConfiguracaoInvalida(f"incidente {incidente.numero} com categoria-chave inativa")
            if any(t not in testes or testes[t].categoria != incidente.chave for t in incidente.testes_chave):
                raise ConfiguracaoInvalida(f"incidente {incidente.numero} com teste-chave inválido")
            incidentes[incidente.numero] = incidente
    except (KeyError, TypeError, ValueError) as erro:
        raise ConfiguracaoInvalida(f"catálogo malformado: {erro!r}") from erro
    return Catalogo(
        categorias=categorias,
        faces=faces,
        testes=testes,
        incidentes=incidentes,
        cartas=tuple(cartas),
        hash=sha256(bruto),
        com_modulo=com_modulo,
    )


def carregar_catalogo(caminho: Path, com_modulo: bool) -> Catalogo:
    return montar_catalogo(ler_catalogo_bruto(caminho), com_modulo)

"""Configuração das regras da v1 (``configs/regras_v1.yaml``).

Mesma ideia da família v2: todo número de regra vem do YAML, com a regra ao
lado, e o hash da configuração resolvida vai para o cabeçalho do registro.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError, model_validator

from critical_failure.nucleo.canonico import sha256
from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.regras.config import P

Inteiro = P[int]
ATRIBUTO_ESPECIAL = "Especial"


class _Base(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", strict=True)


class Jogadores(_Base):
    minimo: Inteiro
    maximo: Inteiro


class TesteV1(_Base):
    atributo: str
    teste: str
    copias: int
    regra: str
    especial: bool = False

    @property
    def nome(self) -> str:
        """Identificador único do teste: o nome com o atributo (AMB-26)."""
        return self.teste if self.especial else f"{self.teste} ({self.atributo})"


class Baralho(_Base):
    cartas: Inteiro
    testes: list[TesteV1]


class Falha(_Base):
    cartas_tomadas: Inteiro


class ContestacaoVerdade(_Base):
    cartas_tomadas: Inteiro


class ContestacaoBlefe(_Base):
    cartas_extras: Inteiro


class Pontos(_Base):
    carta: Inteiro
    par: Inteiro
    trio: Inteiro


class Combinacoes(_Base):
    cartas_no_par: Inteiro
    cartas_no_trio: Inteiro


class Interpretacoes(_Base):
    """Decisões do autor (docs/AMBIGUIDADES.md). Onde o tipo aceita um valor só, a alternativa não está implementada."""

    blefe_aceito: P[Literal["declaracao", "verdade"]]
    carta_de_ataque_apos_falha: P[Literal["descarte"]]
    pontuacao_combinacoes: P[Literal["particao"]]
    alvo_com_sistema_vazio: P[bool]
    empate: P[Literal["dividido"]]


class RegrasV1(_Base):
    esquema: Literal["cf-regras/1"]
    familia: Literal["v1"]
    versao: str
    texto: str
    correcoes: list[str]
    jogadores: Jogadores
    atributos: Inteiro
    baralho: Baralho
    mao_inicial: Inteiro
    sistema_inicial: Inteiro
    cartas_de_teste: Inteiro
    falha: Falha
    contestacao_verdade: ContestacaoVerdade
    contestacao_blefe: ContestacaoBlefe
    pontos: Pontos
    combinacoes: Combinacoes
    interpretacoes: Interpretacoes

    @model_validator(mode="after")
    def _coerencia(self) -> RegrasV1:
        negativos = [
            chave
            for chave, (valor, _) in self.parametros().items()
            if isinstance(valor, int) and not isinstance(valor, bool) and valor < 0
        ]
        if negativos or any(teste.copias < 1 for teste in self.baralho.testes):
            raise ValueError(f"valores negativos ou cópias inválidas: {negativos}")
        nomes = [teste.nome for teste in self.baralho.testes]
        if len(set(nomes)) != len(nomes):
            raise ValueError("teste repetido no baralho da v1")
        total = sum(teste.copias for teste in self.baralho.testes)
        if total != self.baralho.cartas.valor:
            raise ValueError(f"o baralho declara {self.baralho.cartas.valor} cartas, mas os testes somam {total}")
        atributos = {teste.atributo for teste in self.baralho.testes if not teste.especial}
        if len(atributos) != self.atributos.valor:
            raise ValueError(f"o baralho tem {len(atributos)} atributos, mas a regra diz {self.atributos.valor}")
        if self.sistema_inicial.valor + self.cartas_de_teste.valor != self.mao_inicial.valor:
            raise ValueError("sistema_inicial + cartas_de_teste precisa ser igual a mao_inicial")
        if not 2 <= self.jogadores.minimo.valor <= self.jogadores.maximo.valor:
            raise ValueError("número de jogadores inválido")
        if self.jogadores.maximo.valor * self.mao_inicial.valor > total:
            raise ValueError("não há cartas para dar a mão inicial ao número máximo de jogadores")
        especiais = sum(teste.copias for teste in self.baralho.testes if teste.especial)
        if especiais > self.cartas_de_teste.valor and self.mao_inicial.valor - especiais < self.sistema_inicial.valor:
            raise ValueError("cartas especiais demais: um jogador poderia não conseguir montar o sistema")
        return self

    def resolvida(self) -> dict[str, Any]:
        return self.model_dump(mode="json")

    def hash(self) -> str:
        return sha256(self.resolvida())

    def parametros(self) -> dict[str, tuple[Any, str]]:
        achados: dict[str, tuple[Any, str]] = {}

        def descer(prefixo: str, no: Any) -> None:
            if isinstance(no, dict):
                if set(no) == {"valor", "regra"}:
                    achados[prefixo] = (no["valor"], no["regra"])
                    return
                for chave, filho in no.items():
                    descer(f"{prefixo}.{chave}" if prefixo else chave, filho)

        descer("", self.model_dump())
        return achados


@dataclass(frozen=True, eq=False)
class CatalogoV1:
    """As cartas da v1. O índice de cada carta física é a sua posição em ``cartas``."""

    cartas: tuple[str, ...]
    atributo: dict[str, str]
    especiais: frozenset[str]
    atributos: tuple[str, ...]
    hash: str

    def atributo_da(self, carta: int) -> str:
        return self.atributo[self.cartas[carta]]

    def nomes(self, cartas: tuple[int, ...] | list[int]) -> list[str]:
        return [self.cartas[carta] for carta in cartas]


def catalogo_v1(regras: RegrasV1) -> CatalogoV1:
    cartas: list[str] = []
    atributo: dict[str, str] = {}
    for teste in regras.baralho.testes:
        cartas.extend([teste.nome] * teste.copias)
        atributo[teste.nome] = teste.atributo
    especiais = frozenset(teste.nome for teste in regras.baralho.testes if teste.especial)
    atributos = tuple(dict.fromkeys(t.atributo for t in regras.baralho.testes if not t.especial))
    return CatalogoV1(
        cartas=tuple(cartas),
        atributo=atributo,
        especiais=especiais,
        atributos=atributos,
        hash=sha256([teste.model_dump(mode="json") for teste in regras.baralho.testes]),
    )


def ler_regras_v1(dados: Any) -> RegrasV1:
    try:
        return RegrasV1.model_validate(dados)
    except ValidationError as erro:
        raise ConfiguracaoInvalida(f"arquivo de regras da v1 inválido: {erro}") from erro


def carregar_regras_v1(caminho: Path) -> RegrasV1:
    try:
        dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as erro:
        raise ConfiguracaoInvalida(f"não foi possível ler {caminho}: {erro}") from erro
    return ler_regras_v1(dados)


def contagem_por_atributo(regras: RegrasV1) -> Counter[str]:
    contagem: Counter[str] = Counter()
    for teste in regras.baralho.testes:
        contagem[teste.atributo] += teste.copias
    return contagem

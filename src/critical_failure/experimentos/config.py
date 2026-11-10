"""Arquivo de experimento (``experimentos/*.yaml``).

Um experimento é uma lista de cenários. Cada cenário fixa as regras, o número
de jogadores, os bots e quantas partidas rodar. A semente mestre é uma só: a
partida de índice ``i`` usa os mesmos números aleatórios em todos os cenários,
o que reduz a variância das comparações.
"""

from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from critical_failure.nucleo.erros import ConfiguracaoInvalida

NOME_VALIDO = re.compile(r"^[a-z0-9_]+$")


class _Base(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", strict=True)


class BotDoCenario(_Base):
    tipo: str
    parametros: dict[str, Any] = Field(default_factory=dict)
    rotulo: str | None = None
    """Nome do bot nos relatórios. Sem rótulo, usa o tipo (e a política de alvo, no Caçador)."""

    def nome(self) -> str:
        from critical_failure.bots.fabrica import rotulo

        return self.rotulo or rotulo(self.tipo, self.parametros)


class Cenario(_Base):
    nome: str
    regras: str
    """Arquivo YAML das regras, relativo à raiz do projeto."""
    jogadores: int
    partidas: int
    bots: list[BotDoCenario]
    """Um bot só vale para todos os assentos; senão, um por assento."""
    mudancas: dict[str, Any] = Field(default_factory=dict)
    """Valores trocados nas regras, por caminho pontuado (``planejamento.compras: 2``)."""
    requisitos: list[str] = Field(default_factory=list)
    """Requisitos medidos neste cenário, além da robustez, que vale para todos."""
    rodizio: bool = False
    """Roda o cenário uma vez em cada rotação dos bots pelos assentos, com as mesmas sementes.
    ``partidas`` vale para cada rotação. Exige um bot por assento."""
    grupo: str | None = None
    """Preenchido no rodízio: o nome do cenário de origem, para os relatórios somarem as rotações."""
    comparar_com: str | None = None
    """REQ-02: o grupo de referência (a v1) com que este grupo é comparado."""
    celula: list[str] | None = None
    """Linha e coluna deste grupo numa matriz de ganhos: (estilo do bot "foco", estilo dos outros N-1)."""
    matriz: str | None = None
    """Nome da matriz de estilos (MET-07, REQ-04) a que a célula pertence. Sem nome, a célula é da
    matriz de políticas de alvo da v1 (MET-02), como no Experimento 1 da Fase 3."""

    @model_validator(mode="after")
    def _coerencia(self) -> Cenario:
        if not NOME_VALIDO.fullmatch(self.nome):
            raise ValueError(f"nome de cenário inválido: {self.nome!r} (use letras minúsculas, números e _)")
        if self.celula is not None and len(self.celula) != 2:
            raise ValueError(f"cenário {self.nome}: a célula tem 2 nomes (estilo do foco, estilo dos outros)")
        if self.matriz is not None:
            if self.celula is None:
                raise ValueError(f"cenário {self.nome}: cenário de matriz precisa de célula")
            if self.celula[0] == self.celula[1]:
                # Mesa de perfis iguais (diagonal): o foco venceria exatamente 1/N, então ela só serve
                # para medir o que acontece numa população pura (o REQ-05, por exemplo).
                if self.rodizio or not self.bots_identicos():
                    raise ValueError(
                        f"cenário {self.nome}: a diagonal da matriz é uma mesa de bots iguais, sem rodízio"
                    )
            elif sum(1 for bot in self.bots if bot.rotulo == "foco") != 1:
                raise ValueError(f"cenário {self.nome}: célula de matriz precisa de exatamente 1 bot com rótulo foco")
        if self.partidas < 1:
            raise ValueError("partidas precisa ser pelo menos 1")
        if len(self.bots) not in (1, self.jogadores):
            raise ValueError(f"cenário {self.nome}: informe 1 bot ou um por jogador ({self.jogadores})")
        if self.rodizio and len(self.bots) != self.jogadores:
            raise ValueError(f"cenário {self.nome}: o rodízio exige um bot por assento")
        return self

    def rotacoes(self) -> list[Cenario]:
        """As rotações do rodízio: na rotação k, o assento 0 recebe o bot k da lista."""
        if not self.rodizio:
            return [self]
        return [
            self.model_copy(
                update={
                    "nome": f"{self.nome}_r{k}",
                    "bots": self.bots[k:] + self.bots[:k],
                    "rodizio": False,
                    "grupo": self.nome,
                }
            )
            for k in range(self.jogadores)
        ]

    def bots_por_assento(self) -> list[BotDoCenario]:
        return list(self.bots) * self.jogadores if len(self.bots) == 1 else list(self.bots)

    def bots_identicos(self) -> bool:
        return len({(bot.tipo, repr(sorted(bot.parametros.items()))) for bot in self.bots}) == 1


class Experimento(_Base):
    esquema: Literal["cf-experimento/1"]
    nome: str
    descricao: str
    semente_mestre: int
    duracao: str
    """Arquivo do modelo de duração (MOD-05), relativo à raiz do projeto."""
    requisitos_arquivo: str = "configs/requisitos.yaml"
    registros_completos_um_a_cada: int
    """Grava o registro de auditoria completo de 1 partida a cada tantas. Falhas são sempre gravadas."""
    conferir_invariantes: bool = True
    """Confere os invariantes a cada evento de cada partida (REQ-09). Deixa a execução cerca de 2 vezes mais lenta."""
    cenarios: list[Cenario]

    @model_validator(mode="after")
    def _coerencia(self) -> Experimento:
        if not NOME_VALIDO.fullmatch(self.nome):
            raise ValueError(f"nome de experimento inválido: {self.nome!r}")
        if self.registros_completos_um_a_cada < 1 or self.semente_mestre < 0:
            raise ValueError("registros_completos_um_a_cada precisa ser positivo e a semente não pode ser negativa")
        nomes = [cenario.nome for cenario in self.cenarios]
        if not nomes or len(set(nomes)) != len(nomes):
            raise ValueError("o experimento precisa de cenários com nomes diferentes")
        return self

    def resolvido(self) -> dict[str, Any]:
        return self.model_dump(mode="json")

    def cenarios_expandidos(self) -> list[Cenario]:
        """Os cenários que de fato rodam, com o rodízio já aberto em rotações."""
        expandidos = [rotacao for cenario in self.cenarios for rotacao in cenario.rotacoes()]
        nomes = [cenario.nome for cenario in expandidos]
        if len(set(nomes)) != len(nomes):
            raise ConfiguracaoInvalida("as rotações do rodízio repetem o nome de outro cenário")
        return expandidos


def ler_experimento(dados: Any) -> Experimento:
    try:
        return Experimento.model_validate(dados)
    except ValidationError as erro:
        raise ConfiguracaoInvalida(f"arquivo de experimento inválido: {erro}") from erro


def carregar_experimento(caminho: Path) -> Experimento:
    try:
        dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as erro:
        raise ConfiguracaoInvalida(f"não foi possível ler {caminho}: {erro}") from erro
    return ler_experimento(dados)


def aplicar_mudancas(regras: dict[str, Any], mudancas: dict[str, Any]) -> dict[str, Any]:
    """Devolve uma cópia das regras com os valores trocados por caminho pontuado."""
    novas = copy.deepcopy(regras)
    for caminho, valor in mudancas.items():
        no: Any = novas
        try:
            for parte in caminho.split("."):
                no = no[parte]
            if not isinstance(no, dict) or "valor" not in no:
                raise KeyError(caminho)
        except (KeyError, TypeError) as erro:
            raise ConfiguracaoInvalida(f"mudança em parâmetro que não existe nas regras: {caminho}") from erro
        no["valor"] = valor
    return novas

"""Modelo de duração da partida (MOD-05).

Não é regra do jogo: é uma hipótese do simulador para estimar quanto tempo uma
partida levaria na mesa. A duração é a soma de tempos por ação, lidos de
``configs/duracao.yaml``. Os tempos são provisórios (decisão do autor em
2026-11-10) e serão calibrados com cronômetro no playtest.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError

from critical_failure.nucleo.canonico import sha256
from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.regras.v2.estado import Evento


class _Base(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", strict=True)


class Tempo(_Base):
    """Um tempo em segundos e de onde ele veio."""

    valor: int
    fonte: str


class ModeloDeDuracao(_Base):
    esquema: Literal["cf-duracao/1"]
    preparacao: Tempo
    turno_de_planejamento: Tempo
    teste_admitido: Tempo
    """Teste em que o defensor admite a falha: não há explicação nem conferência."""
    teste_com_defesa: Tempo
    """Teste com explicação, conferência do Auditor e leitura da descrição."""
    contestacao: Tempo
    """Acréscimo quando o atacante contesta e a carta é revelada."""
    passar: Tempo
    producao: Tempo
    """Leitura do relato, diagnóstico, gabarito, dano, Lição aprendida e limpeza."""
    fim_de_jogo: Tempo
    """Critical Failure, revelação dos sistemas e pontuação final."""

    def resolvido(self) -> dict[str, Any]:
        return self.model_dump(mode="json")

    def hash(self) -> str:
        return sha256(self.resolvido())


def ler_duracao(dados: Any) -> ModeloDeDuracao:
    try:
        modelo = ModeloDeDuracao.model_validate(dados)
    except ValidationError as erro:
        raise ConfiguracaoInvalida(f"modelo de duração inválido: {erro}") from erro
    negativos = [nome for nome, tempo in modelo.resolvido().items() if isinstance(tempo, dict) and tempo["valor"] < 0]
    if negativos:
        raise ConfiguracaoInvalida(f"tempos negativos no modelo de duração: {negativos}")
    return modelo


def carregar_duracao(caminho: Path) -> ModeloDeDuracao:
    try:
        dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as erro:
        raise ConfiguracaoInvalida(f"não foi possível ler {caminho}: {erro}") from erro
    return ler_duracao(dados)


class Cronometro:
    """Soma o tempo estimado conforme os eventos da partida acontecem."""

    def __init__(self, modelo: ModeloDeDuracao) -> None:
        self.segundos = modelo.preparacao.valor
        self._por_evento = {
            "fim_do_turno": modelo.turno_de_planejamento.valor,
            "teste": modelo.teste_admitido.valor,
            # A conferência só acontece quando há defesa: completa o tempo do teste.
            "conferencia": modelo.teste_com_defesa.valor - modelo.teste_admitido.valor,
            "contestacao": modelo.contestacao.valor,
            "passou": modelo.passar.valor,
            "relato_lido": modelo.producao.valor,
            "critical_failure": modelo.fim_de_jogo.valor,
        }

    def somar(self, evento: Evento) -> None:
        self.segundos += self._por_evento.get(evento.tipo, 0)

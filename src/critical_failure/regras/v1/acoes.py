"""Ações da v1. Cartas citadas pelo nome do teste com o atributo, como ``Stress (Usabilidade)``."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from critical_failure.nucleo.erros import AcaoIlegal

MONTAR = "montar"
TESTAR = "testar"
DECLARAR = "declarar"
ACEITAR = "aceitar"
DUVIDAR = "duvidar"
CONTESTAR = "contestar"
TIPOS = frozenset({MONTAR, TESTAR, DECLARAR, ACEITAR, DUVIDAR, CONTESTAR})


@dataclass(frozen=True, slots=True)
class AcaoV1:
    tipo: str
    cartas: tuple[str, ...] = ()
    """Em ``montar``, as cartas do sistema; em ``testar``, a carta de teste."""
    alvo: int | None = None
    tem: bool | None = None
    """Em ``declarar``: se o defensor diz ter carta do atributo."""
    explicacao_correta: bool | None = None
    """Em ``declarar`` com ``tem``: se a definição que ele dará, caso o atacante duvide, está certa.
    Na v1 a definição não pesa na decisão do atacante (decisão do autor em 2026-11-10); fica só registrada."""

    def texto(self) -> str:
        partes = [self.tipo]
        if self.cartas:
            partes.append(" + ".join(self.cartas))
        if self.alvo is not None:
            partes.append(str(self.alvo))
        if self.tem is not None:
            partes.append("tem" if self.tem else "nao_tem")
        return ":".join(partes)

    def sem_explicacao(self) -> AcaoV1:
        return AcaoV1(self.tipo, self.cartas, self.alvo, self.tem)

    def com_explicacao(self, correta: bool) -> AcaoV1:
        return AcaoV1(self.tipo, self.cartas, self.alvo, self.tem, correta)

    def para_dict(self) -> dict[str, Any]:
        campos: dict[str, Any] = {
            "tipo": self.tipo,
            "cartas": list(self.cartas) or None,
            "alvo": self.alvo,
            "tem": self.tem,
            "explicacao_correta": self.explicacao_correta,
        }
        return {chave: valor for chave, valor in campos.items() if valor is not None}


def acao_v1_de_dict(dados: Any) -> AcaoV1:
    """Reconstrói uma ação gravada no registro. Entrada ruim vira ``AcaoIlegal``."""
    if not isinstance(dados, dict) or dados.get("tipo") not in TIPOS:
        raise AcaoIlegal(f"ação desconhecida: {dados!r}")
    if set(dados) - {"tipo", "cartas", "alvo", "tem", "explicacao_correta"}:
        raise AcaoIlegal(f"ação com campos desconhecidos: {dados!r}")
    cartas = dados.get("cartas") or []
    alvo, tem, explicacao = dados.get("alvo"), dados.get("tem"), dados.get("explicacao_correta")
    if not isinstance(cartas, list) or not all(isinstance(carta, str) for carta in cartas):
        raise AcaoIlegal(f"cartas inválidas: {cartas!r}")
    if alvo is not None and (isinstance(alvo, bool) or not isinstance(alvo, int)):
        raise AcaoIlegal(f"alvo inválido: {alvo!r}")
    if any(valor is not None and not isinstance(valor, bool) for valor in (tem, explicacao)):
        raise AcaoIlegal(f"ação com campo de tipo errado: {dados!r}")
    return AcaoV1(dados["tipo"], tuple(cartas), alvo, tem, explicacao)

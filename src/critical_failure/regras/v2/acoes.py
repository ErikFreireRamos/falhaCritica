"""Ações que um jogador pode pedir ao motor.

Cartas são citadas pelo nome do teste: cópias do mesmo teste são equivalentes,
então o motor escolhe sozinho qual carta física usar. Isso deixa o registro
legível ("testar:Carga:2") e evita opções duplicadas.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from critical_failure.nucleo.erros import AcaoIlegal

COMPRAR = "comprar"
COLOCAR = "colocar"
ENCERRAR = "encerrar"
TESTAR = "testar"
PASSAR = "passar"
ADMITIR = "admitir"
DEFENDER = "defender"
CONFERE = "confere"
NAO_CONFERE = "nao_confere"
ACEITAR = "aceitar"
CONTESTAR = "contestar"
DIAGNOSTICAR = "diagnosticar"
PEGAR = "pegar"
RECUSAR = "recusar"

TIPOS = frozenset(
    {
        COMPRAR,
        COLOCAR,
        ENCERRAR,
        TESTAR,
        PASSAR,
        ADMITIR,
        DEFENDER,
        CONFERE,
        NAO_CONFERE,
        ACEITAR,
        CONTESTAR,
        DIAGNOSTICAR,
        PEGAR,
        RECUSAR,
    }
)

ORIGEM_BACKLOG = "backlog"
ORIGEM_TOPO = "topo"


@dataclass(frozen=True, slots=True)
class Acao:
    tipo: str
    teste: str | None = None
    alvo: int | None = None
    categoria: str | None = None
    origem: str | None = None
    explicacao_correta: bool | None = None
    """Só em ``defender``: se a explicação dada está certa (MOD-01). Não é uma
    escolha do jogador; é um fato sobre o que ele disse, sorteado pelo perfil de
    conhecimento do bot."""

    def texto(self) -> str:
        """Forma curta e legível, usada no registro de auditoria."""
        partes = [self.tipo]
        if self.origem is not None:
            partes.append(self.origem)
        if self.teste is not None:
            partes.append(self.teste)
        if self.alvo is not None:
            partes.append(str(self.alvo))
        if self.categoria is not None:
            partes.append(self.categoria)
        return ":".join(partes)

    def sem_explicacao(self) -> Acao:
        return Acao(self.tipo, self.teste, self.alvo, self.categoria, self.origem)

    def com_explicacao(self, correta: bool) -> Acao:
        return Acao(self.tipo, self.teste, self.alvo, self.categoria, self.origem, correta)

    def para_dict(self) -> dict[str, Any]:
        campos = {
            "tipo": self.tipo,
            "teste": self.teste,
            "alvo": self.alvo,
            "categoria": self.categoria,
            "origem": self.origem,
            "explicacao_correta": self.explicacao_correta,
        }
        return {chave: valor for chave, valor in campos.items() if valor is not None}


def acao_de_dict(dados: Any) -> Acao:
    """Reconstrói uma ação gravada no registro. Entrada ruim vira ``AcaoIlegal``."""
    if not isinstance(dados, dict) or dados.get("tipo") not in TIPOS:
        raise AcaoIlegal(f"ação desconhecida: {dados!r}")
    permitidos = {"tipo", "teste", "alvo", "categoria", "origem", "explicacao_correta"}
    if set(dados) - permitidos:
        raise AcaoIlegal(f"ação com campos desconhecidos: {sorted(set(dados) - permitidos)}")
    teste, alvo, categoria, origem = (dados.get(c) for c in ("teste", "alvo", "categoria", "origem"))
    explicacao = dados.get("explicacao_correta")
    if not all(v is None or isinstance(v, str) for v in (teste, categoria, origem)):
        raise AcaoIlegal(f"ação com campo de tipo errado: {dados!r}")
    if alvo is not None and (isinstance(alvo, bool) or not isinstance(alvo, int)):
        raise AcaoIlegal(f"alvo inválido: {alvo!r}")
    if explicacao is not None and not isinstance(explicacao, bool):
        raise AcaoIlegal(f"explicacao_correta inválida: {explicacao!r}")
    return Acao(dados["tipo"], teste, alvo, categoria, origem, explicacao)

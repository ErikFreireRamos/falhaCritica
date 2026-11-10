"""Erros controlados do simulador.

O motor nunca deve quebrar com uma exceção genérica: entrada inválida vira um
destes erros, que o fuzzing e os testes sabem esperar.
"""

from __future__ import annotations


class ErroCF(Exception):
    """Base de todos os erros controlados do simulador."""


class AcaoIlegal(ErroCF):
    """A ação pedida não é permitida pelas regras no estado atual."""


class ConfiguracaoInvalida(ErroCF):
    """O arquivo de regras, de catálogo ou de perfil está malformado ou incoerente."""


class ViolacaoDeInvariante(ErroCF):
    """O estado da partida deixou de respeitar uma propriedade que sempre deve valer."""


class RegistroDivergente(ErroCF):
    """A reexecução de uma partida não bateu com o registro de auditoria."""

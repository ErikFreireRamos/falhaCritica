"""JSON canônico e hash.

Toda serialização que entra num hash ou num registro de auditoria passa por
aqui: chaves ordenadas, sem espaços, UTF-8 sem escape. Assim o mesmo dado gera
os mesmos bytes em qualquer plataforma.
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
from typing import Any


def json_canonico(dados: Any) -> str:
    """Serializa em JSON com chaves ordenadas e sem espaços."""
    return json.dumps(dados, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256(dados: Any) -> str:
    """Hash SHA-256 do JSON canônico, no formato ``sha256:<hex>``."""
    resumo = hashlib.sha256(json_canonico(dados).encode("utf-8")).hexdigest()
    return f"sha256:{resumo}"


OMITIR_SE_PADRAO = "omitir_se_padrao"
"""Metadado de campo: o campo fica fora do dicionário (e do hash) enquanto vale o padrão.

Serve para acrescentar ao estado um campo de variante sem mudar o ``estado_hash``
das partidas que não usam a variante.
"""


def como_dict(objeto: Any) -> Any:
    """Converte dataclasses aninhadas em dicionários, como ``dataclasses.asdict``.

    Campos marcados com ``OMITIR_SE_PADRAO`` ficam de fora enquanto valem o padrão.
    """
    if dataclasses.is_dataclass(objeto) and not isinstance(objeto, type):
        return {
            campo.name: como_dict(getattr(objeto, campo.name))
            for campo in dataclasses.fields(objeto)
            if not (campo.metadata.get(OMITIR_SE_PADRAO) and getattr(objeto, campo.name) == campo.default)
        }
    if isinstance(objeto, tuple):
        return tuple(como_dict(item) for item in objeto)
    if isinstance(objeto, list):
        return [como_dict(item) for item in objeto]
    if isinstance(objeto, dict):
        return {chave: como_dict(valor) for chave, valor in objeto.items()}
    return objeto

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


def como_dict(objeto: Any) -> Any:
    """Converte dataclasses aninhadas em dicionários e tuplas em listas."""
    return dataclasses.asdict(objeto)

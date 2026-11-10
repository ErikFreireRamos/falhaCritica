"""Escolhe o motor pela família declarada no arquivo de regras (``familia: v1`` ou ``familia: v2``).

Os dois motores têm a mesma interface: ``preparar``, ``acoes_legais``,
``aplicar``, ``observar``, ``conferir_invariantes``, ``placar``,
``ponto_de_corte`` e ``acao_de_dict``. O laço da partida, o registro de
auditoria, o replay e o executor só usam essa interface.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from critical_failure.nucleo.erros import ConfiguracaoInvalida
from critical_failure.regras.config import catalogo_das_regras, ler_regras
from critical_failure.regras.v1.config import ler_regras_v1
from critical_failure.regras.v1.motor import MotorV1
from critical_failure.regras.v2.motor import MotorV2

Motor = MotorV2 | MotorV1


def motor_de(dados: Any, pasta_configs: Path) -> Motor:
    """Monta o motor a partir das regras já lidas (do YAML ou do cabeçalho de um registro)."""
    familia = dados.get("familia") if isinstance(dados, dict) else None
    if familia == "v2":
        regras = ler_regras(dados)
        return MotorV2(regras, catalogo_das_regras(regras, pasta_configs))
    if familia == "v1":
        return MotorV1(ler_regras_v1(dados))
    raise ConfiguracaoInvalida(f"família de regras desconhecida: {familia!r} (esperado v1 ou v2)")


def ler_yaml(caminho: Path) -> Any:
    try:
        return yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as erro:
        raise ConfiguracaoInvalida(f"não foi possível ler {caminho}: {erro}") from erro


def carregar_motor(caminho: Path) -> Motor:
    return motor_de(ler_yaml(caminho), caminho.parent)

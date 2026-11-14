"""COR-03 (v2.2.2): a recomendação de 4 jogadores só muda o texto; as partidas são as mesmas da v2.2.1."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from conftest import CONFIGS, RAIZ, REGRAS_ATUAIS, criar_motor, ler_yaml

from critical_failure import cli
from critical_failure.bots.fabrica import criar_bot
from critical_failure.partida import jogar_partida

V2_2_2 = CONFIGS / "regras_v2_2_2.yaml"
PERFIL = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}
SO_DO_ROTULO = {"versao", "texto", "correcoes"}


def test_v2_2_2_so_muda_o_rotulo_e_o_texto() -> None:
    antiga, nova = ler_yaml(REGRAS_ATUAIS), ler_yaml(V2_2_2)
    assert {k: v for k, v in antiga.items() if k not in SO_DO_ROTULO} == {
        k: v for k, v in nova.items() if k not in SO_DO_ROTULO
    }
    assert nova["versao"] == "v2.2.2" and nova["correcoes"] == ["COR-01", "COR-02", "COR-03"]
    texto = (RAIZ / nova["texto"]).read_text(encoding="utf-8")
    assert "| Jogadores | 4 a 5 **[COR-01]**; recomendado: 4 **[COR-03]** |" in texto
    assert "## Histórico - revisão 2.2.2" in texto


@pytest.mark.regra("R-1.2")
@pytest.mark.parametrize("n", [4, 5])
def test_partidas_da_v2_2_2_sao_as_da_v2_2_1(n: int) -> None:
    def jogar(caminho: Path, partida: int) -> tuple[Any, list[Any]]:
        bots = [criar_bot("heuristico", PERFIL) for _ in range(n - 1)] + [criar_bot("aleatorio", {})]
        eventos: list[Any] = []
        resultado = jogar_partida(
            criar_motor(caminho), bots, 7, partida, ouvinte=lambda evento, _: eventos.append(evento)
        )
        return resultado, eventos

    for partida in range(3):
        (antigo, eventos_antigos), (novo, eventos_novos) = jogar(REGRAS_ATUAIS, partida), jogar(V2_2_2, partida)
        assert eventos_novos == eventos_antigos and len(eventos_novos) > 0
        assert (novo.placar, novo.vencedores, novo.estado_final) == (
            antigo.placar,
            antigo.vencedores,
            antigo.estado_final,
        )


def test_cf_jogar_usa_a_v2_2_2_por_padrao() -> None:
    assert Path(cli.REGRAS_PADRAO).name == V2_2_2.name

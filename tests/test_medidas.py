"""Ganchos de medida dos motores (REQ-05 e REQ-11), conferidos evento a evento.

Estes testes ficavam em ``test_experimentos.py``, que o teste de mutação deixa de fora por ser lento.
Num arquivo próprio, o mutmut os roda (achado do teste de mutação de 2026-11-14).
"""

from __future__ import annotations

from typing import Any

from conftest import RAIZ

from critical_failure.partida import jogar_partida

PERFIL = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}


def test_sistemas_cheios_no_fim_do_primeiro_planejamento() -> None:
    from critical_failure.bots.fabrica import criar_bot
    from critical_failure.regras.familias import carregar_motor

    motor = carregar_motor(RAIZ / "configs" / "regras_v2_2_1.yaml")
    teto = motor.regras.sistema.teto.valor
    vistos: list[tuple[bool, ...]] = []

    def ouvinte(evento: Any, _decisao: Any) -> None:
        if evento.tipo == "inicio_da_fase" and evento.publico["fase"] == "homologacao" and evento.ciclo == 1:
            vistos.append(tuple(len(j.sistema) >= teto for j in evento.estado.jogadores))

    bots = [criar_bot("construtor", PERFIL), criar_bot("cacador", {**PERFIL, "alvo": "lider"})] * 2
    resultado = jogar_partida(motor, bots, 5, 0, ouvinte=ouvinte)
    assert resultado.sistemas_cheios_no_planejamento == vistos[0]
    # O Construtor enche o sistema no primeiro Planejamento; o Caçador, não.
    assert resultado.sistemas_cheios_no_planejamento == (True, False, True, False)
    v1 = carregar_motor(RAIZ / "configs" / "regras_v1.yaml")
    v1_bots = [criar_bot("construtor", PERFIL, "v1") for _ in range(4)]
    assert jogar_partida(v1, v1_bots, 5, 0).sistemas_cheios_no_planejamento is None


def test_blefes_contados_evento_a_evento() -> None:
    from critical_failure.bots.fabrica import criar_bot
    from critical_failure.regras.familias import carregar_motor

    motor = carregar_motor(RAIZ / "configs" / "regras_v2_2_1.yaml")
    contagem = {"tentados": 0, "aceitos": 0}
    aberto = {"blefe": False}

    def ouvinte(evento: Any, _decisao: Any) -> None:
        if evento.tipo == "defesa" and evento.oculto.get("blefe"):
            aberto["blefe"] = True
        if evento.tipo == "fim_da_disputa" and aberto["blefe"]:
            contagem["tentados"] += 1
            contagem["aceitos"] += evento.publico["resultado"] == "aceita"
            aberto["blefe"] = False

    blefadores = [criar_bot("heuristico", {**PERFIL, "blefe": "sempre", "contestacao": "nunca"}) for _ in range(4)]
    resultado = jogar_partida(motor, blefadores, 11, 0, ouvinte=ouvinte)
    assert resultado.blefes == contagem["tentados"] > 0
    assert resultado.blefes_bem_sucedidos == contagem["aceitos"] > 0
    honestos = [criar_bot("heuristico", {**PERFIL, "blefe": "nunca"}) for _ in range(4)]
    assert jogar_partida(motor, honestos, 11, 0).blefes == 0
    v1 = carregar_motor(RAIZ / "configs" / "regras_v1.yaml")
    assert jogar_partida(v1, [criar_bot("construtor", PERFIL, "v1") for _ in range(4)], 11, 0).blefes == 0

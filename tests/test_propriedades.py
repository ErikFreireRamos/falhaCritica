"""Propriedades que valem em qualquer partida, conferidas em partidas aleatórias (hypothesis)."""

from __future__ import annotations

from typing import Any

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from critical_failure.auditoria import registro, replay
from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.bots.mesa import mesa_do_motor
from critical_failure.nucleo.canonico import json_canonico
from critical_failure.nucleo.erros import AcaoIlegal
from critical_failure.observacao import observar
from critical_failure.partida import jogar_partida
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2 import invariantes
from critical_failure.regras.v2.acoes import TIPOS, Acao
from critical_failure.regras.v2.estado import Evento
from critical_failure.regras.v2.motor import MotorV2

sementes = st.integers(0, 2**32 - 1)
partidas = st.integers(0, 10**6)
mesas = st.sampled_from([4, 5])
PARTIDAS = settings(max_examples=60, deadline=None)


def jogar(motor: MotorV2, semente: int, partida: int, n: int, **bots: float) -> tuple[Any, list[Evento]]:
    eventos: list[Evento] = []
    resultado = jogar_partida(
        motor,
        [BotAleatorio(**bots) for _ in range(n)],
        semente,
        partida,
        ouvinte=lambda evento, decisao: eventos.append(evento),
        conferir_invariantes=True,
    )
    return resultado, eventos


@pytest.mark.regra("R-2.0.1", "R-2.0.9", "R-2.0.14", "R-5.2")
@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_invariantes_valem_a_cada_evento(motor: MotorV2, semente: int, partida: int, n: int) -> None:
    """Cartas se conservam (63), sistema até o teto, fichas nunca negativas, 1 Alerta por categoria."""
    resultado, eventos = jogar(motor, semente, partida, n)
    final = resultado.estado_final
    assert invariantes.violacoes(final, motor.regras, motor.catalogo) == []
    em_jogo = [*final.baralho, *final.descarte, *final.backlog]
    for jogador in final.jogadores:
        em_jogo += [*jogador.mao, *jogador.sistema]
        assert len(jogador.sistema) <= 5 and jogador.fichas >= 0
    assert sorted(em_jogo) == list(range(63))


@pytest.mark.regra("R-11.7", "R-11.2", "R-11.3")
@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_com_o_modulo_as_72_cartas_se_conservam(motor_com_modulo: MotorV2, semente: int, partida: int, n: int) -> None:
    resultado, eventos = jogar(motor_com_modulo, semente, partida, n)
    final = resultado.estado_final
    em_jogo = [*final.baralho, *final.descarte, *final.backlog]
    for jogador in final.jogadores:
        em_jogo += [*jogador.mao, *jogador.sistema]
    assert sorted(em_jogo) == list(range(72))
    incidentes = {ev.publico["incidente"] for ev in eventos if ev.tipo == "gabarito_revelado"}
    assert incidentes <= {f"{numero:02d}" for numero in range(1, 17)}


@PARTIDAS
@given(semente=sementes, partida=partidas, n=st.sampled_from([4, 5, 6]))
def test_regra_impressa_tambem_respeita_os_invariantes(
    motor_impresso: MotorV2, semente: int, partida: int, n: int
) -> None:
    resultado, _ = jogar(motor_impresso, semente, partida, n)
    assert resultado.estado_final.fase == E.FIM


@pytest.mark.regra("R-6.3", "R-6.2a")
@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_o_sistema_so_muda_no_planejamento_e_so_cresce(motor: MotorV2, semente: int, partida: int, n: int) -> None:
    _, eventos = jogar(motor, semente, partida, n)
    anterior = eventos[0].estado
    for evento in eventos[1:]:
        for antes, depois in zip(anterior.jogadores, evento.estado.jogadores, strict=True):
            if antes.sistema != depois.sistema:
                assert evento.fase in (E.PREPARACAO, E.PLANEJAMENTO), evento.tipo
                if evento.fase == E.PLANEJAMENTO:
                    # Colocar é permanente: as cartas de antes continuam lá, na mesma ordem.
                    assert depois.sistema[: len(antes.sistema)] == antes.sistema
        anterior = evento.estado


@pytest.mark.regra("R-8.0.4a", "R-2.1.5", "R-2.1.4")
@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_so_o_diagnostico_pela_categoria_chave_da_ficha(motor: MotorV2, semente: int, partida: int, n: int) -> None:
    _, eventos = jogar(motor, semente, partida, n)
    pontuados = [evento for evento in eventos if evento.tipo == "diagnostico_pontuado"]
    assert len(pontuados) == n * 3
    for evento in pontuados:
        acertou = evento.publico["classificacao"] == "chave"
        assert ("fichas" in evento.publico) == acertou
        if acertou:
            assert evento.publico["fichas"] == {str(evento.ator): 1}


@pytest.mark.regra("R-7.4.2", "R-7.1.4", "R-4.9a")
@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_disputas_respeitam_o_bug_duplicado_e_o_auditor_nunca_esta_envolvido(
    motor: MotorV2, semente: int, partida: int, n: int
) -> None:
    _, eventos = jogar(motor, semente, partida, n)
    anterior = eventos[0].estado
    for evento in eventos:
        if evento.tipo == "teste":
            p = evento.publico
            assert p["categoria"] not in anterior.jogadores[p["defensor"]].alertas
            assert p["auditor_da_disputa"] not in (p["atacante"], p["defensor"])
            assert p["atacante"] != p["defensor"]
        # O Auditor titular é sempre o último da ordem de jogo.
        assert (evento.estado.primeiro - 1) % n == evento.estado.auditor
        anterior = evento.estado


@pytest.mark.regra("R-6.9")
@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_no_planejamento_ninguem_tem_alerta(motor: MotorV2, semente: int, partida: int, n: int) -> None:
    """COR-02: os cubos saem no início do Planejamento e nada os cria durante a fase."""
    _, eventos = jogar(motor, semente, partida, n)
    em_repouso = [ev for ev in eventos if ev.fase == E.PLANEJAMENTO and ev.estado.pendente is not None]
    assert em_repouso
    assert all(jogador.alertas == () for ev in em_repouso for jogador in ev.estado.jogadores)


@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_o_sistema_vale_no_maximo_cinco_fichas(motor: MotorV2, semente: int, partida: int, n: int) -> None:
    """Nota R-9.2.6."""
    _, eventos = jogar(motor, semente, partida, n)
    finais = [evento for evento in eventos if evento.tipo == "pontuacao_final"]
    assert len(finais) == n and all(evento.publico["ganho"] <= 5 for evento in finais)


@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_placar_final_e_a_soma_das_fontes(motor: MotorV2, semente: int, partida: int, n: int) -> None:
    resultado, _ = jogar(motor, semente, partida, n)
    for assento in range(n):
        assert 5 + sum(resultado.fontes[assento].values()) == resultado.placar[assento]
    assert resultado.vencedores and max(resultado.placar) == resultado.placar[resultado.vencedores[0]]


@PARTIDAS
@given(semente=sementes, partida=partidas, n=mesas)
def test_modo_rapido_e_modo_auditado_dao_o_mesmo_resultado(motor: MotorV2, semente: int, partida: int, n: int) -> None:
    auditado, _ = jogar(motor, semente, partida, n)
    rapido = jogar_partida(motor, [BotAleatorio() for _ in range(n)], semente, partida)
    assert rapido == auditado


@settings(max_examples=25, deadline=None)
@given(semente=sementes, partida=partidas, n=mesas)
def test_replay_e_reexecucao_geram_registros_identicos(motor: MotorV2, semente: int, partida: int, n: int) -> None:
    arquivo, data = "configs/regras_v2_2_1.yaml", "2026-11-09T00:00:00+00:00"
    linhas, _ = registro.gerar_linhas(motor, arquivo, [BotAleatorio() for _ in range(n)], semente, partida, data)
    de_novo, _ = registro.gerar_linhas(motor, arquivo, [BotAleatorio() for _ in range(n)], semente, partida, data)
    assert [json_canonico(linha) for linha in linhas[1:]] == [json_canonico(linha) for linha in de_novo[1:]]
    for modo in replay.MODOS:
        assert replay.refazer(linhas, modo).eventos == len(linhas) - 2


# ---------------------------------------------------------------- fuzzing básico do motor

textos = st.sampled_from(["Carga", "Regressão", "Não repúdio", "Desempenho", "backlog", "topo", "", "x" * 30])
acoes_quaisquer = st.builds(
    Acao,
    tipo=st.sampled_from(sorted(TIPOS) + ["", "explodir"]),
    teste=st.none() | textos,
    alvo=st.none() | st.integers(-3, 9),
    categoria=st.none() | textos,
    origem=st.none() | textos,
    explicacao_correta=st.none() | st.booleans(),
)


@settings(max_examples=80, deadline=None)
@given(semente=sementes, partida=partidas, n=mesas, dados=st.data())
def test_acoes_quaisquer_so_geram_erro_controlado(
    motor: MotorV2, semente: int, partida: int, n: int, dados: st.DataObject
) -> None:
    """Uma ação arbitrária ou é aplicada, mantendo os invariantes, ou é recusada com AcaoIlegal."""
    estado, _ = motor.preparar(n, semente, partida)
    bots = [BotAleatorio() for _ in range(n)]
    for assento, bot in enumerate(bots):
        bot.iniciar(semente, partida, assento, mesa_do_motor(motor))
    for _ in range(120):
        if estado.pendente is None:
            break
        j = estado.pendente.jogador
        if dados.draw(st.booleans()):
            tentativa = dados.draw(acoes_quaisquer)
        else:
            tentativa = bots[j].decidir(observar(estado, j, motor.catalogo), motor.acoes_legais(estado)).acao
        try:
            novo, _ = motor.aplicar(estado, tentativa)
        except AcaoIlegal:
            # Ação recusada não pode ter mexido em nada: o estado é imutável e segue íntegro.
            assert invariantes.violacoes(estado, motor.regras, motor.catalogo) == []
            continue
        assert invariantes.violacoes(novo, motor.regras, motor.catalogo) == []
        estado = novo

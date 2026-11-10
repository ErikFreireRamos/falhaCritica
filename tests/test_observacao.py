"""O que cada jogador vê (AMB-10) e o teste de que nada oculto vaza para um bot."""

from __future__ import annotations

from dataclasses import fields, replace

import pytest
from conftest import jogar, montar
from hypothesis import given, settings
from hypothesis import strategies as st

from critical_failure.bots.aleatorio import BotAleatorio
from critical_failure.nucleo.canonico import como_dict, json_canonico
from critical_failure.observacao import Observacao, observar
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.estado import Estado, Pendente
from critical_failure.regras.v2.motor import MotorV2


def texto(estado: Estado, assento: int, motor: MotorV2) -> str:
    return json_canonico(como_dict(observar(estado, assento, motor.catalogo)))


@pytest.mark.regra("R-3.4a")
def test_cada_um_ve_a_propria_mao_e_o_proprio_sistema_e_so_eles(motor: MotorV2) -> None:
    # "Não repúdio" tem uma cópia só: se aparecer na observação de outro jogador, vazou.
    estado = montar(
        motor, sistemas=[["Carga", "Pico"], ["Não repúdio"], [], []], maos=[["Regressão"], ["Recuperação"], [], []]
    )
    ana = observar(estado, 0, motor.catalogo)
    assert ana.sistema == ("Carga", "Pico") and ana.mao == ("Regressão",)
    assert "Não repúdio" not in texto(estado, 0, motor) and "Recuperação" not in texto(estado, 0, motor)
    assert "Não repúdio" in texto(estado, 1, motor)
    for assento in (2, 3):
        visto = texto(estado, assento, motor)
        assert all(carta not in visto for carta in ("Carga", "Pico", "Regressão", "Não repúdio", "Recuperação"))


@pytest.mark.regra("R-5.4", "R-3.5")
def test_fichas_alertas_contagens_backlog_e_descarte_sao_publicos(motor: MotorV2) -> None:
    estado = montar(
        motor,
        sistemas=[["Carga"], [], [], []],
        maos=[["Pico", "Regressão"], [], [], []],
        fichas=[3, 7, 5, 0],
        alertas=[[], ["Interação"], [], []],
        backlog=["Recuperação", "Autenticação"],
        descarte=["Estresse"],
    )
    for assento in range(4):
        obs = observar(estado, assento, motor.catalogo)
        assert [j.fichas for j in obs.jogadores] == [3, 7, 5, 0]
        assert [j.alertas for j in obs.jogadores] == [(), ("Interação",), (), ()]
        assert (obs.jogadores[0].cartas_na_mao, obs.jogadores[0].cartas_no_sistema) == (2, 1)
        assert obs.backlog == ("Recuperação", "Autenticação") and obs.descarte == ("Estresse",)
        assert obs.cartas_no_baralho == len(estado.baralho)


def test_a_observacao_nao_tem_campo_para_o_que_e_oculto() -> None:
    campos = {campo.name for campo in fields(Observacao)}
    assert not campos & {"baralho", "linha_do_tempo", "contador_rng", "semente", "jogadores_completos"}


@pytest.mark.regra("R-6.1c")
def test_carta_pega_do_backlog_fica_conhecida_ate_ser_usada(motor: MotorV2) -> None:
    # A primeira compra no Backlog é reposta com Pico; a compra do topo é a carta de cópia única.
    estado = montar(motor, fase=E.PLANEJAMENTO, backlog=["Carga", "Regressão"], baralho=["Pico", "Não repúdio"])
    estado, _ = jogar(motor, estado, "comprar:backlog:Carga", "comprar:topo", "comprar:backlog:Regressão")
    assert sorted(motor.catalogo.nomes(estado.jogadores[0].mao)) == ["Carga", "Não repúdio", "Regressão"]
    visto_por_bruno = observar(estado, 1, motor.catalogo).jogadores[0]
    assert visto_por_bruno.pegas_do_backlog == ("Carga", "Regressão")
    # O que Ana comprou do topo, ninguém mais sabe.
    assert "Não repúdio" not in texto(estado, 1, motor) and "Não repúdio" in texto(estado, 0, motor)
    # Colocada no sistema, a carta continua conhecida; usada num teste, deixa de ser dela.
    estado, _ = jogar(motor, estado, "colocar:Carga", "encerrar")
    assert "Carga" in observar(estado, 1, motor.catalogo).jogadores[0].pegas_do_backlog
    estado = replace(estado, fase=E.HOMOLOGACAO, pendente=Pendente(E.AGIR, 0), compras_restantes=0)
    estado, _ = jogar(motor, estado, "testar:Regressão:1")
    assert observar(estado, 1, motor.catalogo).jogadores[0].pegas_do_backlog == ("Carga",)


@pytest.mark.regra("R-7.2.4b")
def test_carta_revelada_na_contestacao_fica_conhecida(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga"], [], [], []], sistemas=[[], ["Estresse", "Não repúdio"], [], []])
    estado, _ = jogar(motor, estado, "testar:Carga:1", "defender:Estresse", "confere", "contestar")
    for assento in (0, 2, 3):
        obs = observar(estado, assento, motor.catalogo)
        assert obs.jogadores[1].reveladas == ("Estresse",)
        assert "Não repúdio" not in texto(estado, assento, motor), "a outra carta do sistema continua oculta"


@pytest.mark.regra("R-7.1.3")
def test_o_auditor_julga_a_explicacao_sem_saber_se_o_defensor_tem_a_carta(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga"], [], [], []], sistemas=[[], ["Não repúdio"], [], []])
    estado, _ = jogar(motor, estado, "testar:Carga:1", "defender:Estresse")
    assert estado.pendente == Pendente(E.CONFERIR, 3)
    auditor = observar(estado, 3, motor.catalogo)
    assert auditor.disputa is not None and auditor.disputa.explicacao_percebida is True
    assert auditor.decisao_pedida == E.CONFERIR
    # Ele não vê o sistema do defensor, e a observação nem tem campo para "tem a carta".
    assert "Não repúdio" not in texto(estado, 3, motor) and "tem_carta" not in texto(estado, 3, motor)
    # Ninguém além do Auditor da disputa percebe se a explicação está correta.
    for assento in (0, 1, 2):
        outro = observar(estado, assento, motor.catalogo)
        assert outro.disputa is not None and outro.disputa.explicacao_percebida is None
        assert outro.decisao_pedida is None


# ---------------------------------------------------------------- não interferência


def _estado_no_meio_de_uma_partida(motor: MotorV2, semente: int, partida: int, n: int, passos: int) -> Estado:
    bots = [BotAleatorio() for _ in range(n)]
    for assento, bot in enumerate(bots):
        bot.iniciar(semente, partida, assento)
    estado, _ = motor.preparar(n, semente, partida)
    for _ in range(passos):
        if estado.pendente is None:
            break
        j = estado.pendente.jogador
        decisao = bots[j].decidir(observar(estado, j, motor.catalogo), motor.acoes_legais(estado))
        estado, _ = motor.aplicar(estado, decisao.acao)
    return estado


def _trocar(estado: Estado, a: int, b: int) -> Estado:
    """Troca de lugar duas cartas físicas em todo o estado."""

    def t(cartas: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(b if carta == a else a if carta == b else carta for carta in cartas)

    jogadores = tuple(replace(j, mao=t(j.mao), sistema=t(j.sistema)) for j in estado.jogadores)
    return replace(estado, jogadores=jogadores, baralho=t(estado.baralho))


def _ocultas_para(estado: Estado, assento: int) -> list[int]:
    """Cartas cuja identidade o jogador do assento não tem como conhecer."""
    ocultas = list(estado.baralho)
    for j, jogador in enumerate(estado.jogadores):
        if j == assento:
            continue
        conhecidas = set(jogador.reveladas) | set(jogador.pegas_do_backlog)
        ocultas += [carta for carta in (*jogador.mao, *jogador.sistema) if carta not in conhecidas]
    return ocultas


@settings(max_examples=120, deadline=None)
@given(
    semente=st.integers(0, 2**32 - 1),
    partida=st.integers(0, 10**6),
    n=st.sampled_from([4, 5]),
    passos=st.integers(0, 150),
    dados=st.data(),
)
def test_nenhuma_informacao_oculta_chega_ao_bot(
    motor: MotorV2, semente: int, partida: int, n: int, passos: int, dados: st.DataObject
) -> None:
    """Não interferência: mudar só o que está oculto para um jogador não muda a observação dele."""
    estado = _estado_no_meio_de_uma_partida(motor, semente, partida, n, passos)
    if estado.fase == E.FIM:
        return  # no fim todos os sistemas são revelados
    assento = dados.draw(st.integers(0, n - 1))
    antes = observar(estado, assento, motor.catalogo)

    ocultas = _ocultas_para(estado, assento)
    if len(ocultas) >= 2:
        a, b = dados.draw(st.lists(st.sampled_from(ocultas), min_size=2, max_size=2, unique=True))
        assert observar(_trocar(estado, a, b), assento, motor.catalogo) == antes

    # Os incidentes ainda na Linha do Tempo e o contador de aleatoriedade também são ocultos.
    fora_do_jogo = sorted(
        set(motor.catalogo.incidentes) - {estado.agora, estado.proximo, *estado.linha_do_tempo, *estado.resolvidos}
    )
    outra_linha = tuple(dados.draw(st.sampled_from(fora_do_jogo)) for _ in estado.linha_do_tempo)
    variante = replace(estado, linha_do_tempo=outra_linha, contador_rng=estado.contador_rng + 7, semente=semente + 1)
    assert observar(variante, assento, motor.catalogo) == antes

    # Os diagnósticos dos outros, antes da revelação, não aparecem.
    if any(escolha is None for escolha in estado.diagnosticos):
        embaralhados = tuple(
            escolha if j == assento or escolha is None else "Flexibilidade"
            for j, escolha in enumerate(estado.diagnosticos)
        )
        assert observar(replace(estado, diagnosticos=embaralhados), assento, motor.catalogo) == antes

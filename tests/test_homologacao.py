"""Seção 7 da especificação: Homologação, disputa e Auditor. Seção 5: fichas."""

from __future__ import annotations

from dataclasses import replace
from fractions import Fraction

import pytest
from conftest import acao, criar_motor, fichas, jogar, montar, tipos, todos, um

from critical_failure.nucleo.erros import AcaoIlegal
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.acoes import Acao
from critical_failure.regras.v2.estado import Estado, Pendente
from critical_failure.regras.v2.motor import MotorV2


def legais(motor: MotorV2, estado: Estado) -> list[str]:
    return [opcao.texto() for opcao in motor.acoes_legais(estado)]


def disputa(motor: MotorV2, sistema_do_defensor: list[str] | None = None, **mais: object) -> Estado:
    """Ana (0) ataca Bruno (1) com Carga (Desempenho); o Auditor é Davi (3)."""
    estado = montar(motor, maos=[["Carga"], [], [], []], sistemas=[[], sistema_do_defensor or [], [], []], **mais)  # type: ignore[arg-type]
    estado, _ = jogar(motor, estado, "testar:Carga:1")
    return estado


# ---------------------------------------------------------------- a vez na Homologação


@pytest.mark.regra("R-7.0.1", "R-4.8")
def test_na_sua_vez_o_jogador_testa_qualquer_outro_ou_passa(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga", "Regressão"], [], [], []])
    assert legais(motor, estado) == [
        "testar:Carga:1",
        "testar:Carga:2",
        "testar:Carga:3",
        "testar:Regressão:1",
        "testar:Regressão:2",
        "testar:Regressão:3",
        "passar",
    ]
    with pytest.raises(AcaoIlegal):  # não pode testar a si mesmo
        motor.aplicar(estado, acao("testar:Carga:0"))
    with pytest.raises(AcaoIlegal):  # nem com carta que não tem
        motor.aplicar(estado, acao("testar:Pico:1"))


@pytest.mark.regra("R-7.0.2", "R-4.3")
def test_a_vez_segue_em_sentido_horario_e_da_voltas(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga", "Pico"], ["Regressão"], [], []])
    estado, _ = jogar(motor, estado, "testar:Carga:1", "admitir")
    assert estado.pendente == Pendente(E.AGIR, 1)
    estado, eventos = jogar(motor, estado, "testar:Regressão:2", "admitir")
    # Carla e Davi não têm cartas e passam sozinhos; a vez dá a volta e chega de novo a Ana.
    assert [evento.ator for evento in todos(eventos, "passou")] == [2, 3]
    assert estado.pendente == Pendente(E.AGIR, 0)


@pytest.mark.regra("R-7.0.3", "R-7.4.3")
def test_quem_passa_sai_da_fase_e_guarda_as_cartas(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga"], ["Regressão"], [], []])
    estado, _ = jogar(motor, estado, "passar")
    assert estado.jogadores[0].passou and estado.pendente == Pendente(E.AGIR, 1)
    estado, eventos = jogar(motor, estado, "testar:Regressão:0", "admitir")
    # Depois da disputa a vez não volta para Ana, que já passou: a fase acaba.
    assert estado.fase == E.PRODUCAO
    assert motor.catalogo.nomes(estado.jogadores[0].mao) == ["Carga"]


@pytest.mark.regra("R-7.0.4", "R-4.6")
def test_a_fase_termina_quando_todos_passaram(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga"], ["Pico"], [], []])
    estado, eventos = jogar(motor, estado, "passar")
    assert estado.fase == E.HOMOLOGACAO
    estado, eventos = jogar(motor, estado, "passar")
    assert estado.fase == E.PRODUCAO
    assert all(jogador.passou for jogador in estado.jogadores)
    assert [evento.publico["automatico"] for evento in todos(eventos, "passou")] == [False, True, True]


@pytest.mark.regra("R-7.0.1")
def test_quem_nao_tem_jogada_possivel_passa_automaticamente(motor: MotorV2) -> None:
    """AMB-03: mão vazia, ou só alvos que já têm Alerta nas categorias da mão."""
    com_alerta = [["Desempenho"], [], ["Desempenho"], ["Desempenho"]]
    estado = montar(motor, maos=[["Regressão"], ["Carga"], [], []], alertas=com_alerta)
    estado, eventos = jogar(motor, estado, "passar")
    automaticos = [evento for evento in todos(eventos, "passou") if evento.publico["automatico"]]
    assert [evento.ator for evento in automaticos] == [1, 2, 3]
    assert all(evento.amb == "AMB-03" for evento in automaticos)
    assert motor.catalogo.nomes(estado.jogadores[1].mao) == ["Carga"]


@pytest.mark.regra("R-7.0.3")
def test_quem_ja_passou_continua_podendo_ser_testado(motor: MotorV2) -> None:
    """AMB-04."""
    estado = montar(motor, maos=[["Carga"], ["Regressão"], [], []])
    estado, _ = jogar(motor, estado, "passar")
    assert "testar:Regressão:0" in legais(motor, estado)

    imune = criar_motor(**{"interpretacoes.quem_passou_pode_ser_alvo": False})
    estado = montar(imune, maos=[["Carga"], ["Regressão"], [], []])
    estado, _ = jogar(imune, estado, "passar")
    assert legais(imune, estado) == ["testar:Regressão:2", "testar:Regressão:3", "passar"]


# ---------------------------------------------------------------- o Auditor


@pytest.mark.regra("R-7.1.1")
def test_o_auditor_joga_normalmente(motor: MotorV2) -> None:
    estado = montar(motor, maos=[[], [], [], ["Carga"]], pendente=Pendente(E.AGIR, 3))
    assert estado.auditor == 3
    assert legais(motor, estado) == ["testar:Carga:0", "testar:Carga:1", "testar:Carga:2", "passar"]


@pytest.mark.regra("R-7.1.4")
@pytest.mark.parametrize(
    "n, atacante, defensor, esperado",
    [
        (4, 0, 1, 3),  # o Auditor (3) não está envolvido
        (4, 3, 1, 0),  # o Auditor ataca: o primeiro à esquerda dele é o 0
        (4, 1, 3, 0),  # o Auditor defende
        (4, 0, 3, 1),  # o Auditor defende e o 0 ataca: pula o 0
        (4, 3, 0, 1),  # o Auditor ataca o 0: pula o 0
        (5, 4, 0, 1),
        (5, 2, 4, 0),
    ],
)
def test_auditor_envolvido_passa_a_funcao_a_esquerda(
    motor: MotorV2, n: int, atacante: int, defensor: int, esperado: int
) -> None:
    maos: list[list[str]] = [[] for _ in range(n)]
    maos[atacante] = ["Carga"]
    estado = montar(motor, n=n, maos=maos, pendente=Pendente(E.AGIR, atacante))
    titular = n - 1
    estado, eventos = jogar(motor, estado, f"testar:Carga:{defensor}")
    teste = um(eventos, "teste")
    assert teste.publico["auditor_titular"] == titular
    assert teste.publico["auditor_da_disputa"] == esperado
    assert teste.amb == (None if esperado == titular else "AMB-05")
    # A troca vale só nesta disputa: o Marcador de Auditor não muda de lugar.
    assert estado.auditor == titular
    estado, _ = jogar(motor, estado, "defender:Carga")
    assert estado.pendente == Pendente(E.CONFERIR, esperado)


@pytest.mark.regra("R-7.1.5", "R-7.2.3", "R-7.2.3b")
def test_a_decisao_do_auditor_e_final(motor: MotorV2) -> None:
    # O defensor tem a carta e explicou certo, mas o Auditor diz "não confere": conta como "Falhou".
    estado = disputa(motor, ["Carga"])
    estado, eventos = jogar(motor, estado, "defender:Carga", "nao_confere")
    assert um(eventos, "conferencia").publico == {"veredito": "nao_confere"}
    assert um(eventos, "falhou").publico["motivo"] == "nao_confere"
    assert fichas(estado) == [6, 5, 5, 5] and estado.jogadores[1].alertas == ("Desempenho",)
    assert "contestacao" not in tipos(eventos)

    # A explicação estava errada, mas o Auditor diz "confere": a disputa segue para o atacante.
    estado = disputa(motor, [])
    estado, eventos = jogar(motor, estado, acao("defender:Carga", explicacao=False), "confere")
    assert estado.pendente == Pendente(E.CONTESTAR, 0)


# ---------------------------------------------------------------- passo a passo da disputa


@pytest.mark.regra("R-7.2.1", "R-7.4.1")
def test_executar_o_teste_gasta_uma_carta_e_define_a_categoria(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga", "Regressão"], [], [], []])
    estado, eventos = jogar(motor, estado, "testar:Carga:1")
    assert motor.catalogo.nomes(estado.jogadores[0].mao) == ["Regressão"]
    assert estado.disputa is not None and estado.disputa.categoria == "Desempenho"
    assert um(eventos, "teste").publico == {
        "atacante": 0,
        "defensor": 1,
        "teste": "Carga",
        "categoria": "Desempenho",
        "auditor_titular": 3,
        "auditor_da_disputa": 3,
    }
    assert estado.pendente == Pendente(E.RESPONDER, 1)
    # Não há outro limite: com outra carta, Ana testa de novo na volta seguinte.
    estado, _ = jogar(motor, estado, "admitir")
    assert estado.pendente == Pendente(E.AGIR, 0) and "testar:Regressão:1" in legais(motor, estado)


@pytest.mark.regra("R-7.2.1a")
@pytest.mark.parametrize(
    "passos",
    [
        ["admitir"],
        ["defender:Carga", "nao_confere"],
        ["defender:Carga", "confere", "aceitar"],
        ["defender:Carga", "confere", "contestar"],
        ["defender:Estresse", "confere", "contestar"],
    ],
)
def test_a_carta_de_ataque_vai_para_o_descarte_no_fim_da_disputa(motor: MotorV2, passos: list[str]) -> None:
    estado = disputa(motor, ["Carga"])
    assert estado.descarte == ()
    estado, eventos = jogar(motor, estado, *passos)
    assert motor.catalogo.nomes(estado.descarte) == ["Carga"]
    assert um(eventos, "fim_da_disputa").publico["descartada"] == "Carga"
    assert estado.disputa is None


@pytest.mark.regra("R-7.2.2", "R-7.3.1")
def test_admitir_e_falhou(motor: MotorV2) -> None:
    estado = disputa(motor)
    estado, eventos = jogar(motor, estado, "admitir")
    assert um(eventos, "defesa").publico == {"resposta": "admitiu"}
    falhou = um(eventos, "falhou")
    assert falhou.publico["fichas"] == {"0": 1} and falhou.publico["motivo"] == "admitiu"
    assert falhou.publico["alerta"] == {"jogador": 1, "categoria": "Desempenho"}
    assert fichas(estado) == [6, 5, 5, 5]
    assert estado.jogadores[1].alertas == ("Desempenho",)
    assert estado.historico[-1].resultado == E.FALHOU


@pytest.mark.regra("R-7.2.2a", "R-7.2.2b", "R-7.0.5")
def test_o_defensor_nomeia_um_teste_da_categoria_com_ou_sem_a_carta(motor: MotorV2) -> None:
    estado = disputa(motor, sistema_do_defensor=["Regressão"])
    # Quem decide é o defensor, e as opções são os testes da categoria atacada (MOD-06).
    assert estado.pendente == Pendente(E.RESPONDER, 1)
    assert legais(motor, estado) == [
        "admitir",
        "defender:Carga",
        "defender:Estresse",
        "defender:Pico",
        "defender:Resistência",
    ]
    estado, eventos = jogar(motor, estado, "defender:Pico")
    defesa = um(eventos, "defesa")
    assert defesa.publico == {"resposta": "defendeu", "teste_nomeado": "Pico"}
    # Blefe: ele não tem Pico. Só ele sabe; o Auditor só fica sabendo se a explicação confere.
    assert defesa.oculto == {"tem_carta": False, "blefe": True, "explicacao_correta": True}
    assert defesa.visivel_para == {"tem_carta": [1], "blefe": [1], "explicacao_correta": [3]}
    assert estado.pendente == Pendente(E.CONFERIR, 3)


def test_defesa_precisa_dizer_se_a_explicacao_esta_correta(motor: MotorV2) -> None:
    estado = disputa(motor)
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, Acao("defender", teste="Carga"))
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, Acao("defender", teste="Teste que não existe", explicacao_correta=True))
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, Acao("defender", teste="Carga", alvo=2, explicacao_correta=True))


@pytest.mark.regra("R-7.2.2c")
def test_nomear_teste_de_outra_categoria_conta_como_falhou(motor: MotorV2) -> None:
    estado = disputa(motor, sistema_do_defensor=["Regressão"])
    assert "defender:Regressão" not in legais(motor, estado)  # AMB-16: não é oferecido aos bots
    estado, eventos = jogar(motor, estado, "defender:Regressão")
    assert um(eventos, "defesa").regra == "R-7.2.2c"
    assert um(eventos, "falhou").publico["motivo"] == "outra_categoria"
    assert fichas(estado) == [6, 5, 5, 5] and estado.jogadores[1].alertas == ("Desempenho",)
    assert "conferencia" not in tipos(eventos)


@pytest.mark.regra("R-7.2.4", "R-7.3.2")
def test_defesa_aceita_nada_acontece_e_nada_e_revelado(motor: MotorV2) -> None:
    estado = disputa(motor)  # Bruno não tem carta nenhuma: é blefe
    estado, eventos = jogar(motor, estado, "defender:Carga", "confere")
    assert legais(motor, estado) == ["aceitar", "contestar"] and estado.pendente == Pendente(E.CONTESTAR, 0)
    estado, eventos = jogar(motor, estado, "aceitar")
    assert fichas(estado) == [5, 5, 5, 5]
    assert estado.jogadores[1].alertas == () and estado.jogadores[1].reveladas == ()
    assert estado.historico[-1].resultado == E.ACEITA and not estado.historico[-1].contestou


@pytest.mark.regra("R-7.2.4a", "R-7.2.4b", "R-7.3.3")
def test_contestou_e_o_defensor_tinha_a_carta(motor: MotorV2) -> None:
    estado = disputa(motor, sistema_do_defensor=["Pico", "Carga"])
    estado, eventos = jogar(motor, estado, "defender:Carga", "confere", "contestar")
    contestacao = um(eventos, "contestacao")
    assert contestacao.regra == "R-7.3.3"
    assert contestacao.publico["tinha_carta"] and contestacao.publico["carta_revelada"] == "Carga"
    assert contestacao.publico["fichas"] == {"0": -1, "1": 1}
    assert fichas(estado) == [4, 6, 5, 5]
    bruno = estado.jogadores[1]
    # A carta volta para o sistema, mas a mesa passa a conhecê-la.
    assert motor.catalogo.nomes(bruno.sistema) == ["Pico", "Carga"]
    assert motor.catalogo.nomes(bruno.reveladas) == ["Carga"]
    assert bruno.alertas == ()


@pytest.mark.regra("R-7.3.4", "R-7.2.4a")
@pytest.mark.parametrize("sistema", [[], ["Regressão"], ["Estresse", "Pico"]])
def test_contestou_e_era_blefe(motor: MotorV2, sistema: list[str]) -> None:
    """AMB-15: é blefe sempre que o teste nomeado não está no sistema, mesmo com outra carta da categoria."""
    estado = disputa(motor, sistema_do_defensor=sistema)
    estado, eventos = jogar(motor, estado, "defender:Carga", "confere", "contestar")
    contestacao = um(eventos, "contestacao")
    assert contestacao.regra == "R-7.3.4" and not contestacao.publico["tinha_carta"]
    assert contestacao.publico["fichas"] == {"0": 2, "1": -1}
    assert fichas(estado) == [7, 4, 5, 5]
    assert estado.jogadores[1].alertas == ("Desempenho",) and estado.jogadores[1].reveladas == ()
    assert estado.historico[-1].resultado == E.CONTESTOU_BLEFE and estado.historico[-1].contestou


# ---------------------------------------------------------------- regras adicionais


@pytest.mark.regra("R-7.4.2", "R-7.4.2a", "R-2.0.14")
def test_bug_duplicado(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga", "Pico", "Regressão"], [], [], []], alertas=[[], ["Desempenho"], [], []])
    opcoes = legais(motor, estado)
    assert "testar:Carga:1" not in opcoes and "testar:Pico:1" not in opcoes
    assert "testar:Regressão:1" in opcoes and "testar:Carga:2" in opcoes
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, acao("testar:Carga:1"))
    # Quando o cubo sai, a categoria volta a poder ser testada.
    jogadores = list(estado.jogadores)
    jogadores[1] = replace(jogadores[1], alertas=())
    assert "testar:Carga:1" in legais(motor, replace(estado, jogadores=tuple(jogadores)))


@pytest.mark.regra("R-2.0.14")
def test_no_maximo_um_alerta_por_categoria(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga", "Pico"], ["Estresse"], [], []])
    estado, _ = jogar(motor, estado, "testar:Carga:2", "admitir")
    assert estado.jogadores[2].alertas == ("Desempenho",)
    # Bruno não consegue dar o segundo Alerta de Desempenho a Carla.
    assert "testar:Estresse:2" not in legais(motor, estado)
    estado, _ = jogar(motor, estado, "testar:Estresse:3", "admitir")
    assert all(len(set(jogador.alertas)) == len(jogador.alertas) for jogador in estado.jogadores)


def test_contestar_so_compensa_a_partir_de_um_terco_de_chance_de_blefe(motor: MotorV2) -> None:
    """Oráculo da nota R-7.3.5, calculado a partir dos números do YAML."""
    ganho_se_blefe = motor.blefe_defensor_paga + motor.blefe_atacante_ganha
    perda_se_verdade = motor.verdade_atacante_paga
    limiar = Fraction(perda_se_verdade, perda_se_verdade + ganho_se_blefe)
    assert limiar == Fraction(1, 3)


def test_explicar_e_errar_custa_o_mesmo_que_admitir(motor: MotorV2) -> None:
    """Outra parte da nota R-7.3.5."""
    admitiu, _ = jogar(motor, disputa(motor), "admitir")
    errou, _ = jogar(motor, disputa(motor), acao("defender:Carga", explicacao=False), "nao_confere")
    assert fichas(admitiu) == fichas(errou)
    assert admitiu.jogadores[1].alertas == errou.jogadores[1].alertas


# ---------------------------------------------------------------- fichas (seção 5)


@pytest.mark.regra("R-5.1")
def test_ganhar_vem_do_banco_e_pagar_passa_de_um_jogador_a_outro(motor: MotorV2) -> None:
    falhou, _ = jogar(motor, disputa(motor), "admitir")
    assert sum(fichas(falhou)) == 21  # o atacante ganhou 1 do banco
    verdade, _ = jogar(motor, disputa(motor, ["Carga"]), "defender:Carga", "confere", "contestar")
    assert sum(fichas(verdade)) == 20  # pagamento entre jogadores: o total não muda
    blefe, _ = jogar(motor, disputa(motor), "defender:Carga", "confere", "contestar")
    assert sum(fichas(blefe)) == 21  # 1 passou do defensor ao atacante e 1 veio do banco


@pytest.mark.regra("R-5.2", "R-5.2a")
def test_minimo_zero_e_o_banco_completa_o_pagamento(motor: MotorV2) -> None:
    # Atacante sem fichas contesta uma verdade: paga o que tem (nada) e o defensor recebe do banco.
    estado = disputa(motor, ["Carga"], fichas=[0, 5, 5, 5])
    estado, eventos = jogar(motor, estado, "defender:Carga", "confere", "contestar")
    assert fichas(estado) == [0, 6, 5, 5]
    assert um(eventos, "contestacao").publico["fichas"] == {"0": 0, "1": 1}
    # Defensor sem fichas é pego no blefe: o atacante recebe as 2 mesmo assim.
    estado = disputa(motor, [], fichas=[5, 0, 5, 5])
    estado, eventos = jogar(motor, estado, "defender:Carga", "confere", "contestar")
    assert fichas(estado) == [7, 0, 5, 5]
    assert um(eventos, "contestacao").publico["fichas"] == {"0": 2, "1": 0}


def test_punicao_do_blefe_vem_da_configuracao() -> None:
    """VAR-01: sem punição, 1 ficha (atual) ou 2 fichas é só um número do YAML."""
    for punicao, esperado in ((0, [6, 5, 5, 5]), (2, [8, 3, 5, 5])):
        motor = criar_motor(**{"disputa.contestacao_blefe.defensor_paga": punicao})
        estado, _ = jogar(motor, disputa(motor), "defender:Carga", "confere", "contestar")
        assert fichas(estado) == esperado


# ---------------------------------------------------------------- ações fora de hora


@pytest.mark.parametrize("texto", ["admitir", "confere", "aceitar", "contestar", "encerrar", "comprar:topo", "recusar"])
def test_acao_de_outra_decisao_e_ilegal(motor: MotorV2, texto: str) -> None:
    estado = montar(motor, maos=[["Carga"], [], [], []])
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, acao(texto))


def test_so_o_dono_da_decisao_tem_opcoes(motor: MotorV2) -> None:
    estado = disputa(motor)
    with pytest.raises(AcaoIlegal):  # é a vez do defensor responder, não de alguém testar ou passar
        motor.aplicar(estado, acao("passar"))
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, "admitir")  # type: ignore[arg-type]

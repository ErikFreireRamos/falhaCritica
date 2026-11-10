"""Seção 6 da especificação: Planejamento."""

from __future__ import annotations

import pytest
from conftest import acao, criar_motor, jogar, montar, tipos, todos, um

from critical_failure.nucleo.erros import AcaoIlegal
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.estado import Pendente
from critical_failure.regras.v2.motor import MotorV2

BACKLOG = ["Carga", "Coexistência", "Acessibilidade", "Recuperação", "Regressão"]
COBERTOS_EM_DESEMPENHO = [["Carga"], ["Estresse"], ["Pico"], ["Resistência"]]
"""Um sistema por jogador, todos com uma carta de Desempenho (categoria-chave do incidente 01)."""


@pytest.mark.regra("R-6.1", "R-6.1a")
def test_tres_compras_obrigatorias_do_backlog_ou_do_topo(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PLANEJAMENTO, backlog=BACKLOG, baralho=["Pico", "Estresse", "Resistência"])
    legais = [opcao.texto() for opcao in motor.acoes_legais(estado)]
    assert legais == [f"comprar:backlog:{teste}" for teste in BACKLOG] + ["comprar:topo"]
    with pytest.raises(AcaoIlegal):  # não dá para pular as compras
        motor.aplicar(estado, acao("encerrar"))
    with pytest.raises(AcaoIlegal):
        motor.aplicar(estado, acao("colocar:Carga"))

    estado, _ = jogar(motor, estado, "comprar:topo", "comprar:backlog:Carga")
    assert estado.pendente == Pendente(E.COMPRAR, 0) and estado.compras_restantes == 1
    estado, _ = jogar(motor, estado, "comprar:topo")
    assert estado.pendente == Pendente(E.COLOCAR, 0) and estado.compras_restantes == 0
    # Pico veio do topo; a compra no Backlog foi reposta com Estresse; a última do topo foi Resistência.
    assert sorted(motor.catalogo.nomes(estado.jogadores[0].mao)) == ["Carga", "Pico", "Resistência"]
    assert "Estresse" in motor.catalogo.nomes(estado.backlog)


@pytest.mark.regra("R-6.1b", "R-6.1c")
def test_compra_do_backlog_e_publica_e_a_vaga_e_reposta(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PLANEJAMENTO, backlog=BACKLOG, baralho=["Pico"])
    estado, eventos = jogar(motor, estado, "comprar:backlog:Coexistência")
    compra = um(eventos, "compra")
    assert compra.publico == {"origem": "backlog", "carta": "Coexistência"} and compra.oculto == {}
    assert um(eventos, "backlog_reposto").publico == {"carta": "Pico"}
    # A carta nova entra na mesma vaga.
    assert motor.catalogo.nomes(estado.backlog) == ["Carga", "Pico", "Acessibilidade", "Recuperação", "Regressão"]
    assert motor.catalogo.nomes(estado.jogadores[0].pegas_do_backlog) == ["Coexistência"]


@pytest.mark.regra("R-6.1c")
def test_compra_do_topo_e_privada(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PLANEJAMENTO, backlog=BACKLOG, baralho=["Pico"])
    estado, eventos = jogar(motor, estado, "comprar:topo")
    compra = um(eventos, "compra")
    assert compra.publico == {"origem": "topo"}
    assert compra.oculto == {"carta": "Pico"} and compra.visivel_para == {"carta": [0]}
    assert estado.jogadores[0].pegas_do_backlog == ()
    assert len(estado.backlog) == 5


@pytest.mark.regra("R-6.2", "R-6.2a")
def test_colocar_e_opcional_e_permanente(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PLANEJAMENTO, maos=[["Carga", "Pico"], [], [], []], pendente=Pendente(E.COLOCAR, 0))
    assert [opcao.texto() for opcao in motor.acoes_legais(estado)] == ["colocar:Carga", "colocar:Pico", "encerrar"]
    # Opcional: pode encerrar sem colocar nada.
    sem_colocar, _ = jogar(motor, estado, "encerrar")
    assert sem_colocar.jogadores[0].sistema == ()

    estado, eventos = jogar(motor, estado, "colocar:Carga")
    colocacao = um(eventos, "colocacao")
    assert colocacao.publico == {"cartas_no_sistema": 1}
    assert colocacao.oculto == {"carta": "Carga"} and colocacao.visivel_para == {"carta": [0]}
    assert motor.catalogo.nomes(estado.jogadores[0].sistema) == ["Carga"]
    # Permanente: nenhuma ação tira carta do sistema.
    assert all(opcao.tipo in ("colocar", "encerrar") for opcao in motor.acoes_legais(estado))


@pytest.mark.regra("R-6.2", "R-2.0.9")
def test_teto_do_sistema(motor: MotorV2) -> None:
    cheio = ["Carga", "Pico", "Estresse", "Resistência", "Regressão"]
    estado = montar(
        motor,
        fase=E.PLANEJAMENTO,
        sistemas=[cheio[:4], [], [], []],
        maos=[["Regressão", "Recuperação"], [], [], []],
        pendente=Pendente(E.COLOCAR, 0),
    )
    estado, eventos = jogar(motor, estado, "colocar:Regressão")
    assert len(estado.jogadores[0].sistema) == motor.teto == 5
    # Sistema cheio: o turno acaba sozinho, mesmo com carta na mão.
    assert "fim_do_turno" in tipos(eventos)
    assert estado.pendente == Pendente(E.COMPRAR, 1)
    assert motor.catalogo.nomes(estado.jogadores[0].mao) == ["Recuperação"]


@pytest.mark.regra("R-6.4", "R-4.3", "R-4.5")
def test_cada_um_faz_o_turno_inteiro_em_sentido_horario(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PLANEJAMENTO, primeiro=2, backlog=BACKLOG)
    ordem = []
    while estado.fase == E.PLANEJAMENTO:
        assert estado.pendente is not None
        j = estado.pendente.jogador
        ordem.append(j)
        estado, _ = jogar(motor, estado, "comprar:topo", "comprar:topo", "comprar:topo", "encerrar")
    assert ordem == [2, 3, 0, 1]
    # Quando todos fizeram a vez, começa a Homologação com o primeiro jogador.
    assert estado.fase == E.HOMOLOGACAO and estado.pendente == Pendente(E.AGIR, 2)


@pytest.mark.regra("R-6.5")
def test_nao_ha_limite_de_cartas_na_mao(motor: MotorV2) -> None:
    mao = ["Carga", "Carga", "Pico", "Estresse", "Resistência", "Regressão", "Recuperação", "Autenticação"]
    estado = montar(motor, fase=E.PLANEJAMENTO, maos=[mao, [], [], []])
    estado, _ = jogar(motor, estado, "comprar:topo", "comprar:topo", "comprar:topo", "encerrar")
    assert len(estado.jogadores[0].mao) == len(mao) + 3


@pytest.mark.regra("R-6.6")
def test_baralho_vazio_reembaralha_o_descarte(motor: MotorV2) -> None:
    quase_tudo = [teste for teste in motor.catalogo.cartas if teste not in ("Carga", "Pico")]
    estado = montar(
        motor,
        fase=E.PLANEJAMENTO,
        maos=[quase_tudo, [], [], []],
        descarte=["Carga", "Carga", "Carga", "Pico", "Pico"],
    )
    assert estado.baralho == ()
    estado, eventos = jogar(motor, estado, "comprar:topo")
    embaralhou = um(eventos, "reembaralhamento")
    assert embaralhou.publico == {"cartas": 5} and sorted(embaralhou.oculto["ordem"]) == sorted(
        ["Carga"] * 3 + ["Pico"] * 2
    )
    assert estado.descarte == () and len(estado.baralho) == 4
    assert estado.contador_rng == 11  # o sorteio avançou o contador do fluxo do jogo


@pytest.mark.regra("R-6.1", "R-6.1b")
def test_baralho_e_descarte_vazios_a_compra_nao_acontece(motor: MotorV2) -> None:
    tudo_menos_duas = list(motor.catalogo.cartas)
    tudo_menos_duas.remove("Carga")
    tudo_menos_duas.remove("Pico")
    # AMB-06, reposição: só há 2 cartas, no Backlog.
    estado = montar(motor, fase=E.PLANEJAMENTO, maos=[[], tudo_menos_duas, [], []], backlog=["Carga", "Pico"])
    assert [opcao.texto() for opcao in motor.acoes_legais(estado)] == ["comprar:backlog:Carga", "comprar:backlog:Pico"]
    estado, eventos = jogar(motor, estado, "comprar:backlog:Carga")
    assert um(eventos, "reposicao_impossivel").amb == "AMB-06"
    estado, eventos = jogar(motor, estado, "comprar:backlog:Pico")
    # AMB-06, compra: não sobrou carta em lugar nenhum; a terceira compra é perdida.
    impossivel = um(eventos, "compra_impossivel")
    assert impossivel.publico == {"compras_perdidas": 1} and impossivel.amb == "AMB-06"
    assert estado.pendente == Pendente(E.COLOCAR, 0) and estado.backlog == ()


@pytest.mark.regra("R-6.9")
def test_alertas_saem_no_inicio_de_cada_planejamento(motor: MotorV2) -> None:
    # Fim do ciclo 1 com Alertas fora da categoria-chave do incidente (01 é de Desempenho).
    estado = montar(
        motor,
        fase=E.PRODUCAO,
        alertas=[["Flexibilidade"], [], ["Interação", "Confiabilidade"], []],
        sistemas=COBERTOS_EM_DESEMPENHO,
    )
    estado, eventos = jogar(motor, estado, *["diagnosticar:Flexibilidade"] * 4)
    assert estado.fase == E.PLANEJAMENTO and estado.ciclo == 2
    zerados = um(eventos, "alertas_zerados")
    assert zerados.regra == "R-6.9"
    assert zerados.publico == {"removidos": {"0": ["Flexibilidade"], "2": ["Interação", "Confiabilidade"]}}
    assert all(jogador.alertas == () for jogador in estado.jogadores)


@pytest.mark.regra("R-6.2b", "R-6.9")
def test_regra_impressa_o_alerta_persiste_e_a_carta_o_corrige(motor_impresso: MotorV2) -> None:
    """Com a COR-02 desligada vale o PDF 2.2: o Alerta fica até o jogador colocar carta da categoria."""
    estado = montar(
        motor_impresso,
        fase=E.PRODUCAO,
        alertas=[["Flexibilidade"], [], [], []],
        sistemas=COBERTOS_EM_DESEMPENHO,
        maos=[["Escalabilidade", "Regressão"], [], [], []],
    )
    estado, eventos = jogar(motor_impresso, estado, *["diagnosticar:Flexibilidade"] * 4)
    assert "alertas_zerados" not in tipos(eventos)
    assert estado.jogadores[0].alertas == ("Flexibilidade",)

    # No ciclo 2 quem começa é o assento 1; ele faz o turno e a vez chega ao assento 2... até o 0.
    while estado.pendente != Pendente(E.COMPRAR, 0):
        estado, _ = jogar(motor_impresso, estado, "comprar:topo", "comprar:topo", "comprar:topo", "encerrar")
    estado, _ = jogar(motor_impresso, estado, "comprar:topo", "comprar:topo", "comprar:topo")
    estado, eventos = jogar(motor_impresso, estado, "colocar:Regressão")
    assert estado.jogadores[0].alertas == ("Flexibilidade",), "carta de outra categoria não corrige"
    estado, eventos = jogar(motor_impresso, estado, "colocar:Escalabilidade")
    assert um(eventos, "alerta_corrigido").publico == {"categoria": "Flexibilidade"}
    assert estado.jogadores[0].alertas == ()


def test_com_a_correcao_colocar_carta_nao_gera_evento_de_alerta(motor: MotorV2) -> None:
    estado = montar(
        motor,
        fase=E.PLANEJAMENTO,
        alertas=[["Desempenho"], [], [], []],
        maos=[["Carga"], [], [], []],
        pendente=Pendente(E.COLOCAR, 0),
    )
    estado, eventos = jogar(motor, estado, "colocar:Carga")
    assert todos(eventos, "alerta_corrigido") == []
    assert estado.jogadores[0].alertas == ("Desempenho",)


@pytest.mark.regra("R-6.3")
def test_fora_do_planejamento_nao_ha_acao_que_mude_o_sistema(motor: MotorV2) -> None:
    for fase in (E.HOMOLOGACAO, E.PRODUCAO):
        estado = montar(motor, fase=fase, maos=[["Carga"], [], [], []])
        assert all(opcao.tipo not in ("colocar", "comprar") for opcao in motor.acoes_legais(estado))
        with pytest.raises(AcaoIlegal):
            motor.aplicar(estado, acao("colocar:Carga"))


def test_parametro_de_compras_vem_da_configuracao() -> None:
    """VAR-07: compras por Planejamento é só um número do YAML."""
    motor = criar_motor(**{"planejamento.compras": 2})
    estado = montar(motor, fase=E.PLANEJAMENTO)
    estado, _ = jogar(motor, estado, "comprar:topo", "comprar:topo")
    assert estado.pendente == Pendente(E.COLOCAR, 0)

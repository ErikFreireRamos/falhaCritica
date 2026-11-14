"""Seção 8 da especificação: Produção, incidentes, dano e fim do ciclo."""

from __future__ import annotations

from dataclasses import replace

import pytest
from conftest import avancar, criar_motor, diagnosticar, fichas, jogar, montar, tipos, todos, um

from critical_failure.nucleo.erros import AcaoIlegal
from critical_failure.observacao import observar
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.acoes import Acao
from critical_failure.regras.v2.estado import Pendente
from critical_failure.regras.v2.motor import MotorV2

DESEMPENHO = [["Carga"], ["Estresse"], ["Pico"], ["Resistência"]]
"""Um sistema por jogador, todos cobertos em Desempenho."""


def legais(motor: MotorV2, estado: object) -> list[str]:
    return [opcao.texto() for opcao in motor.acoes_legais(estado)]  # type: ignore[arg-type]


def dano_de(eventos: list, assento: int) -> dict[str, int]:  # type: ignore[type-arg]
    (evento,) = [ev for ev in todos(eventos, "dano_incidente") if ev.ator == assento]
    return dict(evento.publico["itens"])


# ---------------------------------------------------------------- diagnóstico


@pytest.mark.regra("R-8.0.2", "R-8.0.2a", "R-7.1.6", "R-2.0.6")
def test_todos_diagnosticam_uma_categoria_inclusive_o_auditor(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PRODUCAO, primeiro=1, sistemas=DESEMPENHO)
    assert estado.auditor == 0
    assert legais(motor, estado) == [f"diagnosticar:{categoria}" for categoria in motor.catalogo.categorias]
    assert len(legais(motor, estado)) == 7
    quem = []
    while estado.pendente is not None and estado.pendente.tipo == E.DIAGNOSTICAR:
        quem.append(estado.pendente.jogador)
        estado, _ = jogar(motor, estado, "diagnosticar:Interação")
    assert quem == [1, 2, 3, 0], "todos escolhem, na ordem de jogo, e o Auditor (0) também"


@pytest.mark.regra("R-11.4", "R-11.6")
def test_com_o_modulo_ha_oito_categorias_no_leque(motor_com_modulo: MotorV2) -> None:
    estado = montar(motor_com_modulo, fase=E.PRODUCAO, agora="15", sistemas=DESEMPENHO)
    assert len(legais(motor_com_modulo, estado)) == 8
    estado, eventos = diagnosticar(motor_com_modulo, estado, ["Segurança Operacional", "Confiabilidade"] * 2)
    pontuados = todos(eventos, "diagnostico_pontuado")
    # Só a categoria-chave pontua, também nos incidentes do módulo; a secundária do 15 é Confiabilidade.
    assert [ev.publico["classificacao"] for ev in pontuados] == ["chave", "secundaria", "chave", "secundaria"]
    # O teto continua valendo e o dano usa só a categoria-chave: ninguém tem carta dela.
    assert dano_de(eventos, 0) == {"sem_cobertura": 2, "severo_sem_teste_chave": 1}


@pytest.mark.regra("R-8.0.2b", "R-4.4")
def test_escolhas_ficam_ocultas_ate_todos_escolherem(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PRODUCAO, sistemas=DESEMPENHO)
    estado, eventos = jogar(motor, estado, "diagnosticar:Flexibilidade")
    escolha = um(eventos, "diagnostico_escolhido")
    assert escolha.publico == {} and escolha.oculto == {"categoria": "Flexibilidade"}
    assert escolha.visivel_para == {"categoria": [0]}
    # Bruno, que escolhe em seguida, não vê a escolha de Ana; Ana vê a própria.
    assert observar(estado, 1, motor.catalogo).diagnosticos == (None, None, None, None)
    assert observar(estado, 0, motor.catalogo).diagnosticos == ("Flexibilidade", None, None, None)
    # Depois de escolher não dá para mudar: a vez já é do próximo.
    assert estado.pendente == Pendente(E.DIAGNOSTICAR, 1)
    estado, eventos = jogar(motor, estado, *["diagnosticar:Desempenho"] * 3)
    revelados = um(eventos, "diagnosticos_revelados")
    assert revelados.publico == {"escolhas": ["Flexibilidade", "Desempenho", "Desempenho", "Desempenho"]}


@pytest.mark.regra("R-8.0.3", "R-2.1.2", "R-4.14", "R-3.7", "R-2.1.1", "R-4.12")
def test_o_gabarito_so_aparece_depois_de_todos_revelarem(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PRODUCAO, agora="13", sistemas=DESEMPENHO)
    for assento in range(4):
        obs = observar(estado, assento, motor.catalogo)
        # A frente é pública: nome, número e relato. O verso não aparece em lugar nenhum.
        assert obs.radar_agora is not None and obs.radar_agora.numero == "13"
        assert obs.radar_agora.relato.startswith("Os usuários dobraram")
        assert not hasattr(obs.radar_agora, "chave")
        assert obs.gabaritos == ()
    estado, eventos = jogar(motor, estado, *["diagnosticar:Desempenho"] * 3)
    assert "gabarito_revelado" not in tipos(eventos)
    estado, eventos = jogar(motor, estado, "diagnosticar:Desempenho")
    ordem = tipos(eventos)
    assert ordem.index("diagnosticos_revelados") < ordem.index("gabarito_revelado")
    assert um(eventos, "gabarito_revelado").publico == {
        "incidente": "13",
        "nome": "Campanha viral",
        "chave": "Flexibilidade",
        "secundaria": "Desempenho",
        "testes_chave": ["Escalabilidade"],
        "severo": True,
    }
    assert [g.numero for g in observar(estado, 0, motor.catalogo).gabaritos] == ["13"]


@pytest.mark.regra("R-8.0.4", "R-8.0.4a", "R-2.1.3", "R-2.1.5", "R-8.0.8")
def test_so_a_categoria_chave_pontua(motor: MotorV2) -> None:
    # Incidente 01: chave Desempenho, secundária Confiabilidade. Todos cobertos: sem dano.
    estado = montar(motor, fase=E.PRODUCAO, sistemas=DESEMPENHO)
    escolhas = ["Desempenho", "Confiabilidade", "Flexibilidade", "Desempenho"]
    estado, eventos = diagnosticar(motor, estado, escolhas)
    pontuados = {ev.ator: ev.publico for ev in todos(eventos, "diagnostico_pontuado")}
    assert [pontuados[j]["classificacao"] for j in range(4)] == ["chave", "secundaria", "outra", "chave"]
    assert [pontuados[j].get("fichas") for j in range(4)] == [{"0": 1}, None, None, {"3": 1}]
    estado, _ = avancar(motor, estado, E.PLANEJAMENTO, ciclo=2)
    # Categoria próxima ou secundária não vale nada, e errar não custa nada.
    assert fichas(estado) == [6, 5, 5, 6]
    assert [jogador.acertos for jogador in estado.jogadores] == [1, 0, 0, 1]


@pytest.mark.regra("R-2.1.6")
def test_na_producao_o_auditor_nao_tem_decisao_propria(motor: MotorV2) -> None:
    """O gabarito impresso decide: as únicas decisões da fase são diagnosticar e a Lição aprendida."""
    estado = montar(motor, fase=E.PRODUCAO, sistemas=DESEMPENHO, backlog=["Carga"])
    vistos = set()
    while estado.fase == E.PRODUCAO:
        assert estado.pendente is not None
        vistos.add(estado.pendente.tipo)
        passo = "diagnosticar:Desempenho" if estado.pendente.tipo == E.DIAGNOSTICAR else "recusar"
        estado, _ = jogar(motor, estado, passo)
    assert vistos == {E.DIAGNOSTICAR, E.LICAO}


# ---------------------------------------------------------------- dano


@pytest.mark.regra("R-8.0.5", "R-8.1.1", "R-8.1.2", "R-8.1.3", "R-C.0.2", "R-C.0.3", "R-5.3")
@pytest.mark.parametrize(
    "incidente, sistema, alertas, itens",
    [
        # 01: Desempenho, normal
        ("01", [], [], {"sem_cobertura": 2}),
        ("01", ["Carga"], [], {}),
        ("01", [], ["Desempenho"], {"sem_cobertura": 2, "alerta": 1}),
        ("01", ["Resistência"], ["Desempenho"], {"alerta": 1}),
        ("01", ["Regressão", "Recuperação"], ["Interação"], {"sem_cobertura": 2}),
        # 13: Flexibilidade, severo, teste-chave Escalabilidade
        ("13", [], [], {"sem_cobertura": 2, "severo_sem_teste_chave": 1}),
        ("13", ["Adaptabilidade"], [], {"severo_sem_teste_chave": 1}),
        ("13", ["Escalabilidade"], [], {}),
        ("13", [], ["Flexibilidade"], {"sem_cobertura": 2, "alerta": 1, "severo_sem_teste_chave": 1}),
        # 07: Confiabilidade, severo, testes-chave Recuperação ou Engenharia do Caos: basta um dos dois
        ("07", ["Engenharia do Caos"], [], {}),
        ("07", ["Recuperação"], [], {}),
        ("07", ["Disponibilidade", "Tolerância a falhas"], [], {"severo_sem_teste_chave": 1}),
    ],
)
def test_itens_de_dano_do_incidente(
    motor: MotorV2, incidente: str, sistema: list[str], alertas: list[str], itens: dict[str, int]
) -> None:
    estado = montar(
        motor,
        fase=E.PRODUCAO,
        agora=incidente,
        sistemas=[sistema, [], [], []],
        alertas=[alertas, [], [], []],
        fichas=[10, 10, 10, 10],
    )
    estado, eventos = diagnosticar(motor, estado, ["Manutenibilidade"] * 4)  # ninguém acerta
    (evento,) = [ev for ev in todos(eventos, "dano_incidente") if ev.ator == 0]
    assert evento.publico["itens"] == itens
    # O total é a soma dos itens aplicáveis, devolvida ao banco.
    assert evento.publico["devido"] == sum(itens.values())
    assert evento.publico["fichas"] == {"0": -sum(itens.values())}


@pytest.mark.regra("R-8.0.4", "R-8.0.5")
def test_exemplo_de_dano_do_pdf(motor: MotorV2) -> None:
    """R-8.1.5: incidente normal; Ana sem carta da categoria, com Alerta, acerta. Pega 1 e devolve 3."""
    estado = montar(motor, fase=E.PRODUCAO, agora="10", alertas=[["Segurança da Informação"], [], [], []])
    estado, eventos = diagnosticar(motor, estado, ["Segurança da Informação", "Interação", "Interação", "Interação"])
    assert dano_de(eventos, 0) == {"sem_cobertura": 2, "alerta": 1}
    saldo_da_ana = sum(ev.publico["fichas"].get("0", 0) for ev in eventos if "fichas" in ev.publico)
    assert saldo_da_ana == -2


@pytest.mark.regra("R-2.1.4", "R-8.0.5b", "R-8.0.7a")
def test_exemplo_da_categoria_secundaria_do_pdf(motor_impresso: MotorV2) -> None:
    """R-8.1.6, Campanha viral: chave Flexibilidade, secundária Desempenho, severo.

    Roda com a regra impressa para o Alerta de Bruno sobreviver ao Planejamento
    seguinte e dar para ver que a limpeza não o removeu.
    """
    motor = motor_impresso
    estado = montar(
        motor,
        fase=E.PRODUCAO,
        agora="13",
        sistemas=[["Adaptabilidade"], ["Carga", "Pico"], [], []],
        alertas=[[], ["Desempenho"], [], []],
        backlog=["Regressão"],
    )
    estado, eventos = diagnosticar(motor, estado, ["Flexibilidade", "Desempenho", "Interação", "Interação"])
    pontuados = {ev.ator: ev.publico for ev in todos(eventos, "diagnostico_pontuado")}
    assert pontuados[0]["classificacao"] == "chave" and pontuados[0]["fichas"] == {"0": 1}
    assert pontuados[1]["classificacao"] == "secundaria" and "fichas" not in pontuados[1]
    # Ana tem Flexibilidade, mas não Escalabilidade: paga só o item do incidente severo.
    assert dano_de(eventos, 0) == {"severo_sem_teste_chave": 1}
    # Bruno: cartas e Alerta de Desempenho (a secundária) não protegem nem são cobrados.
    assert dano_de(eventos, 1) == {"sem_cobertura": 2, "severo_sem_teste_chave": 1}
    assert estado.jogadores[1].alertas == ("Desempenho",)
    # Quem escolheu a secundária não tem direito à Lição aprendida.
    assert all(ev.ator != 1 for ev in eventos if ev.tipo.startswith("licao"))


@pytest.mark.regra("R-8.0.5a", "R-8.0.7b")
def test_comprovar_cobertura_revela_o_minimo(motor: MotorV2) -> None:
    """AMB-11: uma carta da categoria; em incidente severo, um teste-chave, se tiver."""
    cat = motor.catalogo
    estado = montar(
        motor,
        fase=E.PRODUCAO,
        agora="13",
        sistemas=[["Adaptabilidade", "Escalabilidade", "Instalabilidade"], ["Substituibilidade", "Carga"], [], []],
    )
    estado, eventos = diagnosticar(motor, estado, ["Interação"] * 4)
    comprovadas = {ev.ator: ev.publico["carta"] for ev in todos(eventos, "cobertura_comprovada")}
    assert comprovadas == {0: "Escalabilidade", 1: "Substituibilidade"}
    assert all(ev.amb == "AMB-11" for ev in todos(eventos, "cobertura_comprovada"))
    # A carta revelada volta virada para baixo: continua no sistema, mas a mesa a conhece.
    assert cat.nomes(estado.jogadores[0].reveladas) == ["Escalabilidade"]
    assert cat.nomes(estado.jogadores[0].sistema) == ["Adaptabilidade", "Escalabilidade", "Instalabilidade"]
    assert observar(estado, 2, cat).jogadores[0].reveladas == ("Escalabilidade",)
    # Quem não tem carta da categoria não revela nada.
    assert 2 not in comprovadas and estado.jogadores[2].reveladas == ()


@pytest.mark.regra("R-8.0.5a")
def test_comprovar_cobertura_prefere_a_carta_que_a_mesa_ja_conhece(motor: MotorV2) -> None:
    """AMB-11: com duas cartas da categoria-chave, revela a que já foi revelada antes (nada novo)."""
    cat = motor.catalogo
    estado = montar(motor, fase=E.PRODUCAO, agora="01", sistemas=[["Carga", "Pico"], [], [], []])
    pico = next(carta for carta in estado.jogadores[0].sistema if cat.teste(carta) == "Pico")
    ana = replace(estado.jogadores[0], reveladas=(pico,))
    estado = replace(estado, jogadores=(ana, *estado.jogadores[1:]))
    estado, eventos = diagnosticar(motor, estado, ["Desempenho"] * 4)
    comprovadas = {ev.ator: ev.publico["carta"] for ev in todos(eventos, "cobertura_comprovada")}
    assert comprovadas[0] == "Pico"
    assert cat.nomes(estado.jogadores[0].reveladas) == ["Pico"]


@pytest.mark.regra("R-8.1.4")
def test_blefe_aceito_nao_protege_na_producao(motor: MotorV2) -> None:
    estado = montar(motor, maos=[["Carga"], [], [], []])
    estado, _ = jogar(motor, estado, "testar:Carga:1", "defender:Carga", "confere", "aceitar")
    estado, _ = avancar(motor, estado, E.PRODUCAO)
    estado, eventos = diagnosticar(motor, estado, ["Interação"] * 4)
    # Bruno passou pelo teste blefando, mas não tem carta de Desempenho quando o incidente 01 chega.
    assert dano_de(eventos, 1) == {"sem_cobertura": 2}


@pytest.mark.regra("R-5.2")
def test_ordem_entre_o_diagnostico_e_o_dano(motor: MotorV2) -> None:
    """AMB-01: com 1 ficha, acerto (+1) e dano 3. Diagnóstico antes termina em 0; dano antes, em 1."""

    def resultado(m: MotorV2) -> int:
        estado = montar(
            m, fase=E.PRODUCAO, agora="10", alertas=[["Segurança da Informação"], [], [], []], fichas=[1, 5, 5, 5]
        )
        estado, eventos = diagnosticar(m, estado, ["Segurança da Informação", "Interação", "Interação", "Interação"])
        (dano,) = [ev for ev in todos(eventos, "dano_incidente") if ev.ator == 0]
        assert dano.publico["devido"] == 3
        return sum(ev.publico["fichas"].get("0", 0) for ev in eventos if "fichas" in ev.publico) + 1

    assert resultado(motor) == 0
    assert resultado(criar_motor(**{"interpretacoes.producao_ordem": "dano_primeiro"})) == 1


# ---------------------------------------------------------------- Lição aprendida e limpeza


@pytest.mark.regra("R-8.0.6", "R-8.0.6a", "R-8.0.6b")
def test_licao_aprendida(motor: MotorV2) -> None:
    cat = motor.catalogo
    backlog = ["Carga", "Regressão", "Recuperação", "Coexistência", "Acessibilidade"]
    estado = montar(motor, fase=E.PRODUCAO, sistemas=DESEMPENHO, backlog=backlog, baralho=["Estresse", "Autenticação"])
    # Incidente 01 (Desempenho, secundária Confiabilidade): Ana e Carla acertam; Bruno fica na secundária.
    estado, eventos = diagnosticar(motor, estado, ["Desempenho", "Confiabilidade", "Desempenho", "Interação"])
    assert estado.pendente == Pendente(E.LICAO, 0)
    assert legais(motor, estado) == ["pegar:Carga", "recusar"]
    with pytest.raises(AcaoIlegal):  # só carta da categoria-chave
        motor.aplicar(estado, Acao("pegar", teste="Regressão"))

    estado, eventos = jogar(motor, estado, "pegar:Carga")
    assert um(eventos, "licao_aprendida").publico == {"carta": "Carga"}
    assert cat.nomes(estado.jogadores[0].mao) == ["Carga"]
    # O Backlog é reposto depois de cada retirada, e a carta nova serve ao próximo da ordem.
    assert um(eventos, "backlog_reposto").regra == "R-8.0.6a"
    assert cat.nomes(estado.backlog)[0] == "Estresse"
    assert estado.pendente == Pendente(E.LICAO, 2), "Bruno (secundária) não entra na fila"
    assert legais(motor, estado) == ["pegar:Estresse", "recusar"]
    estado, eventos = jogar(motor, estado, "recusar")  # pegar é opcional (AMB-02)
    assert um(eventos, "licao_recusada").ator == 2 and estado.jogadores[2].mao == ()
    assert estado.fase == E.PLANEJAMENTO


@pytest.mark.regra("R-8.0.6")
def test_licao_aprendida_sem_carta_da_categoria_nao_acontece(motor: MotorV2) -> None:
    """AMB-02."""
    estado = montar(motor, fase=E.PRODUCAO, sistemas=DESEMPENHO, backlog=["Regressão", "Recuperação"])
    estado, eventos = diagnosticar(motor, estado, ["Desempenho"] * 4)
    indisponiveis = todos(eventos, "licao_indisponivel")
    assert [ev.ator for ev in indisponiveis] == [0, 1, 2, 3] and all(ev.amb == "AMB-02" for ev in indisponiveis)
    assert estado.fase == E.PLANEJAMENTO and len(estado.backlog) == 2


@pytest.mark.regra("R-8.0.7", "R-8.0.7a", "R-8.0.7c")
def test_limpeza_remove_so_os_alertas_da_categoria_chave(motor_impresso: MotorV2) -> None:
    """Com a regra impressa, para os outros Alertas não saírem no Planejamento seguinte."""
    motor = motor_impresso
    alertas = [["Desempenho", "Interação"], ["Desempenho"], ["Confiabilidade"], []]
    estado = montar(motor, fase=E.PRODUCAO, sistemas=DESEMPENHO, alertas=alertas)
    estado, eventos = diagnosticar(motor, estado, ["Interação"] * 4)
    limpeza = um(eventos, "limpeza")
    assert limpeza.publico == {"categoria": "Desempenho", "alertas_removidos": [0, 1], "incidente": "01"}
    # Saem os de Desempenho (a chave). Os de outras categorias, inclusive a secundária, ficam.
    assert [jogador.alertas for jogador in estado.jogadores] == [("Interação",), (), ("Confiabilidade",), ()]
    # O incidente sai do jogo.
    assert estado.agora != "01" and estado.resolvidos == ("01",)


# ---------------------------------------------------------------- fim do ciclo e Radar


@pytest.mark.regra("R-4.7", "R-4.9", "R-4.9a", "R-4.10", "R-4.13")
def test_fim_do_ciclo_passa_os_marcadores_e_avanca_o_radar(motor: MotorV2) -> None:
    estado = montar(motor, fase=E.PRODUCAO, agora="01", proximo="02", linha_do_tempo=("03",))
    radar = [(estado.ciclo, estado.agora, estado.proximo)]
    marcadores = [(estado.primeiro, estado.auditor)]
    for ciclo in (2, 3):
        estado, eventos = avancar(motor, estado, E.PLANEJAMENTO, ciclo=ciclo)
        fim = um(eventos, "fim_do_ciclo")
        assert fim.publico["ciclo_encerrado"] == ciclo - 1
        radar.append((estado.ciclo, estado.agora, estado.proximo))
        marcadores.append((estado.primeiro, estado.auditor))
    # R-4.13: no ciclo 3 a vaga Próximo é o Critical Failure (None).
    assert radar == [(1, "01", "02"), (2, "02", "03"), (3, "03", None)]
    # Os marcadores passam para a esquerda, e o Auditor é sempre o último da ordem.
    assert marcadores == [(0, 3), (1, 0), (2, 1)]
    assert all((primeiro - 1) % 4 == auditor for primeiro, auditor in marcadores)


@pytest.mark.regra("R-4.1")
def test_as_fases_vem_sempre_na_mesma_ordem(motor: MotorV2) -> None:
    estado, eventos = motor.preparar(4, semente=3, partida=1)
    while estado.pendente is not None:
        estado, novos = avancar(motor, estado, E.FIM)
        eventos += novos
    fases = [ev.publico["fase"] for ev in todos(eventos, "inicio_da_fase")]
    assert fases == [E.PLANEJAMENTO, E.HOMOLOGACAO, E.PRODUCAO] * 3

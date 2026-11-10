"""Apoio comum aos testes: motores prontos e um montador de estados.

O montador ``montar`` cria um estado de partida a partir de nomes de testes,
respeitando a conservação das cartas: o que não foi pedido vai para o baralho.
Assim cada teste de regra descreve só a situação que interessa.
"""

from __future__ import annotations

import copy
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any

import pytest
import yaml

from critical_failure.nucleo.catalogo import Catalogo
from critical_failure.regras.config import RegrasV2, catalogo_das_regras, ler_regras
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.acoes import Acao
from critical_failure.regras.v2.estado import Estado, Evento, Jogador, Pendente
from critical_failure.regras.v2.motor import MotorV2

RAIZ = Path(__file__).resolve().parents[1]
CONFIGS = RAIZ / "configs"
# Os scripts do projeto (verificador, matriz, catálogo, dourados) também são testados.
sys.path.insert(0, str(RAIZ / "scripts"))
REGRAS_ATUAIS = CONFIGS / "regras_v2_2_1.yaml"
REGRAS_IMPRESSAS = CONFIGS / "regras_v2_2.yaml"


def ler_yaml(caminho: Path) -> dict[str, Any]:
    dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    assert isinstance(dados, dict)
    return dados


def criar_motor(caminho: Path = REGRAS_ATUAIS, **mudancas: Any) -> MotorV2:
    """Motor com as regras do arquivo, trocando valores por caminho pontuado.

    Exemplo: ``criar_motor(**{"interpretacoes.producao_ordem": "dano_primeiro"})``.
    """
    dados = copy.deepcopy(ler_yaml(caminho))
    for chave, valor in mudancas.items():
        no = dados
        for parte in chave.split("."):
            no = no[parte]
        no["valor"] = valor
    regras = ler_regras(dados)
    return MotorV2(regras, catalogo_das_regras(regras, CONFIGS))


@pytest.fixture(scope="session")
def motor() -> MotorV2:
    """Regras atuais (v2.2.1)."""
    return criar_motor()


@pytest.fixture(scope="session")
def motor_impresso() -> MotorV2:
    """Regras como impressas no PDF (v2.2): até 6 jogadores e Alertas que persistem."""
    return criar_motor(REGRAS_IMPRESSAS)


@pytest.fixture(scope="session")
def motor_com_modulo() -> MotorV2:
    return criar_motor(modulo_seguranca_operacional=True)


@pytest.fixture(scope="session")
def regras(motor: MotorV2) -> RegrasV2:
    return motor.regras


@pytest.fixture(scope="session")
def catalogo(motor: MotorV2) -> Catalogo:
    return motor.catalogo


def montar(
    motor: MotorV2,
    *,
    n: int = 4,
    fase: str = E.HOMOLOGACAO,
    ciclo: int = 1,
    primeiro: int = 0,
    sistemas: Sequence[Sequence[str]] | None = None,
    maos: Sequence[Sequence[str]] | None = None,
    fichas: Sequence[int] | None = None,
    alertas: Sequence[Sequence[str]] | None = None,
    passou: Sequence[bool] | None = None,
    backlog: Sequence[str] = (),
    baralho: Sequence[str] | None = None,
    descarte: Sequence[str] = (),
    agora: str | None = "01",
    proximo: str | None = "02",
    linha_do_tempo: Sequence[str] = ("03",),
    pendente: Pendente | None = None,
) -> Estado:
    """Monta um estado em repouso na fase pedida, pronto para ``motor.aplicar``."""
    catalogo = motor.catalogo
    livres: dict[str, list[int]] = {}
    for carta, teste in enumerate(catalogo.cartas):
        livres.setdefault(teste, []).append(carta)

    def pegar(nomes: Sequence[str]) -> tuple[int, ...]:
        return tuple(livres[nome].pop(0) for nome in nomes)

    vazio: list[list[str]] = [[] for _ in range(n)]
    cartas_do_sistema = [pegar(nomes) for nomes in (sistemas or vazio)]
    cartas_da_mao = [pegar(nomes) for nomes in (maos or vazio)]
    cartas_do_backlog = pegar(backlog)
    cartas_do_descarte = pegar(descarte)
    if baralho is None:
        cartas_do_baralho = tuple(sorted(carta for restantes in livres.values() for carta in restantes))
    else:
        topo = pegar(baralho)
        cartas_do_baralho = topo + tuple(sorted(carta for restantes in livres.values() for carta in restantes))

    jogadores = tuple(
        Jogador(
            fichas=(fichas or [motor.fichas_iniciais] * n)[j],
            mao=cartas_da_mao[j],
            sistema=cartas_do_sistema[j],
            alertas=tuple(x for x in catalogo.categorias if x in (alertas or vazio)[j]),
            reveladas=(),
            pegas_do_backlog=(),
            passou=(passou or [False] * n)[j],
            acertos=0,
        )
        for j in range(n)
    )
    compras = 0
    diagnosticos: tuple[str | None, ...] = ()
    if pendente is None:
        if fase == E.PLANEJAMENTO:
            pendente, compras = Pendente(E.COMPRAR, primeiro), motor.compras
        elif fase == E.HOMOLOGACAO:
            pendente = Pendente(E.AGIR, primeiro)
        elif fase == E.PRODUCAO:
            pendente, diagnosticos = Pendente(E.DIAGNOSTICAR, primeiro), (None,) * n
    return Estado(
        semente=123,
        partida=0,
        contador_rng=10,
        jogadores=jogadores,
        baralho=cartas_do_baralho,
        descarte=cartas_do_descarte,
        backlog=cartas_do_backlog,
        linha_do_tempo=tuple(linha_do_tempo),
        agora=agora,
        proximo=proximo,
        resolvidos=(),
        ciclo=ciclo,
        fase=fase,
        primeiro=primeiro,
        auditor=(primeiro - 1) % n,
        pendente=pendente,
        compras_restantes=compras,
        disputa=None,
        diagnosticos=diagnosticos,
        fila_da_licao=(),
        historico=(),
        vencedores=(),
    )


def acao(texto: str, explicacao: bool | None = None) -> Acao:
    """Cria uma ação a partir da forma curta do registro, como ``testar:Carga:1``."""
    tipo, *resto = texto.split(":")
    if tipo == "comprar":
        return Acao(tipo, origem=resto[0], teste=resto[1] if len(resto) > 1 else None)
    if tipo == "testar":
        return Acao(tipo, teste=resto[0], alvo=int(resto[1]))
    if tipo == "diagnosticar":
        return Acao(tipo, categoria=resto[0])
    if tipo in ("colocar", "pegar", "defender"):
        return Acao(tipo, teste=resto[0], explicacao_correta=explicacao)
    return Acao(tipo)


def jogar(motor: MotorV2, estado: Estado, *passos: str | Acao) -> tuple[Estado, list[Evento]]:
    """Aplica uma sequência de ações e devolve o estado final com todos os eventos.

    Uma defesa escrita como texto leva explicação correta; para explicação
    incorreta, passe ``acao("defender:Carga", explicacao=False)``.
    """
    eventos: list[Evento] = []
    for passo in passos:
        if isinstance(passo, str):
            passo = acao(passo, explicacao=True if passo.startswith("defender") else None)
        estado, novos = motor.aplicar(estado, passo)
        eventos += novos
    return estado, eventos


def tipos(eventos: Sequence[Evento]) -> list[str]:
    return [evento.tipo for evento in eventos]


def um(eventos: Sequence[Evento], tipo: str) -> Evento:
    """O único evento do tipo pedido."""
    achados = [evento for evento in eventos if evento.tipo == tipo]
    assert len(achados) == 1, f"esperado 1 evento '{tipo}', achados {len(achados)}: {tipos(eventos)}"
    return achados[0]


def todos(eventos: Sequence[Evento], tipo: str) -> list[Evento]:
    return [evento for evento in eventos if evento.tipo == tipo]


def fichas(estado: Estado) -> list[int]:
    return [jogador.fichas for jogador in estado.jogadores]


ACAO_MINIMA = {
    E.COMPRAR: "comprar:topo",
    E.COLOCAR: "encerrar",
    E.AGIR: "passar",
    E.RESPONDER: "admitir",
    E.CONFERIR: "confere",
    E.CONTESTAR: "aceitar",
    E.LICAO: "recusar",
}


def avancar(motor: MotorV2, estado: Estado, ate: str, ciclo: int | None = None) -> tuple[Estado, list[Evento]]:
    """Joga o mínimo (compra do topo, não coloca, passa, diagnostica a 1ª categoria) até a fase pedida."""
    eventos: list[Evento] = []
    while not (estado.fase == ate and (ciclo is None or estado.ciclo == ciclo)):
        assert estado.pendente is not None, f"a partida acabou antes de chegar a {ate}"
        if estado.pendente.tipo == E.DIAGNOSTICAR:
            passo = Acao("diagnosticar", categoria=motor.catalogo.categorias[0])
        else:
            passo = acao(ACAO_MINIMA[estado.pendente.tipo])
        estado, novos = motor.aplicar(estado, passo)
        eventos += novos
    return estado, eventos


def diagnosticar(motor: MotorV2, estado: Estado, escolhas: Sequence[str]) -> tuple[Estado, list[Evento]]:
    """Faz todos diagnosticarem; ``escolhas`` é indexado por assento."""
    eventos: list[Evento] = []
    while estado.pendente is not None and estado.pendente.tipo == E.DIAGNOSTICAR:
        j = estado.pendente.jogador
        estado, novos = motor.aplicar(estado, Acao("diagnosticar", categoria=escolhas[j]))
        eventos += novos
    return estado, eventos

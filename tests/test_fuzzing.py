"""Fuzzing (Fase 5): entradas aleatórias ou malformadas só podem gerar erros controlados.

"Erro controlado" é uma exceção de ``ErroCF`` (ação ilegal, configuração
inválida, registro divergente...). Qualquer outra exceção é um defeito do
simulador. Na suíte noturna (``CF_NOTURNO=1``) cada teste roda muito mais casos.
"""

from __future__ import annotations

import contextlib
import copy
import json
import os
import random
from typing import Any

import yaml
from conftest import CONFIGS, RAIZ
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from critical_failure.auditoria import registro, replay
from critical_failure.duracao import ler_duracao
from critical_failure.experimentos.config import ler_experimento
from critical_failure.nucleo.erros import AcaoIlegal, ConfiguracaoInvalida, ErroCF
from critical_failure.regras.familias import motor_de
from critical_failure.regras.v1 import acoes as A1
from critical_failure.regras.v1.acoes import AcaoV1
from critical_failure.regras.v2 import acoes as A2
from critical_failure.regras.v2.acoes import Acao, acao_de_dict

NOTURNO = bool(os.environ.get("CF_NOTURNO"))
CASOS = 400 if NOTURNO else 20
AJUSTES = settings(max_examples=CASOS, deadline=None, suppress_health_check=[HealthCheck.too_slow])
PASSOS = 600


def ler(nome: str) -> dict[str, Any]:
    dados: dict[str, Any] = yaml.safe_load((CONFIGS / nome).read_text(encoding="utf-8"))
    return dados


REGRAS_V2 = ler("regras_v2_2_1.yaml")
REGRAS_V1 = ler("regras_v1.yaml")
MOTOR_V2 = motor_de(REGRAS_V2, CONFIGS)
MOTOR_V1 = motor_de(REGRAS_V1, CONFIGS)
NOMES_V2 = sorted(MOTOR_V2.catalogo.testes)
CATEGORIAS = list(MOTOR_V2.catalogo.categorias)
LIXO: list[Any] = [None, -1, 0, 1, 99, 10**9, "x", "", True, 2.5, [], {}, [1, "a"]]


# ---------------------------------------------------------------- ações


def acao_v2_qualquer(sorteio: random.Random) -> Acao:
    return Acao(
        sorteio.choice([*sorted(A2.TIPOS), "inexistente"]),
        sorteio.choice([None, *NOMES_V2, "NaoExiste"]),
        sorteio.choice([None, *range(-2, 8)]),
        sorteio.choice([None, *CATEGORIAS, "Nenhuma"]),
        sorteio.choice([None, A2.ORIGEM_BACKLOG, A2.ORIGEM_TOPO, "lixo"]),
        sorteio.choice([None, True, False]),
    )


def acao_v1_qualquer(sorteio: random.Random, nomes: list[str]) -> AcaoV1:
    return AcaoV1(
        sorteio.choice([*sorted(A1.TIPOS), "inexistente"]),
        tuple(sorteio.choice([*nomes, "NaoExiste"]) for _ in range(sorteio.randint(0, 4))),
        sorteio.choice([None, *range(-2, 8)]),
        sorteio.choice([None, True, False]),
        sorteio.choice([None, True, False]),
    )


def jogar_aos_trancos(motor: Any, semente: int, caos: int, aleatoria: Any) -> None:
    """Joga misturando ações legais e ações quaisquer. Ação recusada é AcaoIlegal e não muda nada.

    O hypothesis escolhe a semente e a dose de caos (de 0 a 10 em 10); um gerador derivado dela
    sorteia cada passo.
    """
    sorteio = random.Random(semente)
    n = sorteio.randint(motor.jogadores_minimo, motor.jogadores_maximo)
    estado, _ = motor.preparar(n, semente, sorteio.randint(0, 50))
    for _ in range(PASSOS):
        if estado.pendente is None:
            break
        legais = motor.acoes_legais(estado)
        if legais and sorteio.randint(1, 10) > caos:
            acao = sorteio.choice(legais)
            if acao.tipo == A2.DEFENDER and isinstance(acao, Acao):
                acao = acao.com_explicacao(sorteio.choice([True, False]))
        else:
            acao = aleatoria(sorteio)
        try:
            estado, _ = motor.aplicar(estado, acao)
        except AcaoIlegal:
            continue
        motor.conferir_invariantes(estado, em_repouso=True)


@AJUSTES
@given(st.integers(0, 2**32), st.integers(0, 10))
def test_acoes_aleatorias_na_v2_so_geram_erro_controlado(semente: int, caos: int) -> None:
    jogar_aos_trancos(MOTOR_V2, semente, caos, acao_v2_qualquer)


@AJUSTES
@given(st.integers(0, 2**32), st.integers(0, 10))
def test_acoes_aleatorias_na_v1_so_geram_erro_controlado(semente: int, caos: int) -> None:
    nomes = sorted(set(MOTOR_V1.catalogo.cartas))
    jogar_aos_trancos(MOTOR_V1, semente, caos, lambda sorteio: acao_v1_qualquer(sorteio, nomes))


JSON = st.recursive(
    st.one_of(st.none(), st.booleans(), st.integers(-5, 10), st.text(max_size=8), st.sampled_from(NOMES_V2)),
    lambda filhos: st.one_of(st.lists(filhos, max_size=3), st.dictionaries(st.text(max_size=12), filhos, max_size=4)),
    max_leaves=10,
)


@AJUSTES
@given(
    st.one_of(
        JSON,
        st.fixed_dictionaries(
            {"tipo": st.sampled_from(sorted(A2.TIPOS))},
            optional={"teste": JSON, "alvo": JSON, "categoria": JSON, "origem": JSON, "explicacao_correta": JSON},
        ),
    )
)
def test_acao_gravada_malformada_vira_acao_ilegal(dados: Any) -> None:
    for ler_acao in (acao_de_dict, MOTOR_V1.acao_de_dict):
        with contextlib.suppress(AcaoIlegal):
            ler_acao(dados)


# ---------------------------------------------------------------- configurações


def caminhos(no: Any, prefixo: tuple[Any, ...] = ()) -> list[tuple[Any, ...]]:
    """Todos os caminhos de um YAML lido (chaves de dicionário e índices de lista)."""
    achados = [prefixo] if prefixo else []
    if isinstance(no, dict):
        for chave, filho in no.items():
            achados += caminhos(filho, (*prefixo, chave))
    elif isinstance(no, list):
        for indice, filho in enumerate(no):
            achados += caminhos(filho, (*prefixo, indice))
    return achados


def estragar(dados: Any, data: st.DataObject) -> Any:
    """Troca um valor qualquer por lixo, ou apaga a chave."""
    novo = copy.deepcopy(dados)
    caminho = data.draw(st.sampled_from(caminhos(novo)))
    pai = novo
    for parte in caminho[:-1]:
        pai = pai[parte]
    if isinstance(pai, dict) and data.draw(st.booleans()):
        del pai[caminho[-1]]
    else:
        pai[caminho[-1]] = data.draw(st.sampled_from(LIXO))
    return novo


@AJUSTES
@given(st.data())
def test_regras_malformadas_so_geram_erro_controlado(data: st.DataObject) -> None:
    from critical_failure.bots.aleatorio import BotAleatorio
    from critical_failure.partida import jogar_partida

    base = data.draw(st.sampled_from([REGRAS_V2, REGRAS_V1]))
    dados = estragar(base, data)
    try:
        motor = motor_de(dados, CONFIGS)
        n = motor.jogadores_minimo
        bots = [BotAleatorio(0.5, 0.9) for _ in range(n)] if motor.familia == "v2" else None
        if bots is not None:
            jogar_partida(motor, bots, 1, 0, conferir_invariantes=True)
        else:
            motor.preparar(n, 1, 0)
    except ErroCF:
        pass


@AJUSTES
@given(st.data())
def test_experimento_malformado_so_gera_configuracao_invalida(data: st.DataObject) -> None:
    dados = ler_yaml_experimento()
    with contextlib.suppress(ConfiguracaoInvalida):
        ler_experimento(estragar(dados, data)).cenarios_expandidos()


def ler_yaml_experimento() -> dict[str, Any]:
    dados: dict[str, Any] = yaml.safe_load(
        (RAIZ / "experimentos" / "fase4_exp5b_blefe_equilibrio.yaml").read_text(encoding="utf-8")
    )
    return dados


@AJUSTES
@given(st.data())
def test_modelo_de_duracao_malformado_so_gera_configuracao_invalida(data: st.DataObject) -> None:
    with contextlib.suppress(ConfiguracaoInvalida):
        ler_duracao(estragar(ler("duracao.yaml"), data))


# ---------------------------------------------------------------- registros de auditoria


LINHAS_DOURADAS = registro.ler(RAIZ / "tests" / "dourados" / "v2_2_1_com_4_jogadores.jsonl")


@AJUSTES
@given(st.data())
def test_registro_adulterado_nao_passa_no_replay(data: st.DataObject) -> None:
    """Mudar qualquer valor de um evento faz o replay acusar a divergência (ou recusar o registro)."""
    linhas = json.loads(json.dumps(LINHAS_DOURADAS))
    indice = data.draw(st.integers(1, len(linhas) - 1))
    evento = linhas[indice]
    caminho = data.draw(st.sampled_from([c for c in caminhos(evento) if not isinstance(c[-1], int) or len(c) > 1]))
    pai = evento
    for parte in caminho[:-1]:
        pai = pai[parte]
    antigo = pai[caminho[-1]]
    novo = data.draw(st.sampled_from([v for v in LIXO if v != antigo and type(v) is not type(antigo)] or ["x"]))
    pai[caminho[-1]] = novo
    modo = data.draw(st.sampled_from(replay.MODOS))
    try:
        replay.refazer(linhas, modo)
    except ErroCF:
        return
    # Alguns campos não entram na conferência (por exemplo, o texto do motivo de uma decisão).
    assert caminho[0] in CAMPOS_SEM_CONFERENCIA, f"adulteração não detectada em {caminho}"


CAMPOS_SEM_CONFERENCIA = {"decisao", "data_hora", "duracao_s"}


def test_cada_campo_do_fim_adulterado_nao_passa_no_replay() -> None:
    """Regressão do achado do fuzzing: no modo ``acoes``, o critério de desempate não era conferido."""
    for campo in sorted(set(LINHAS_DOURADAS[-1]) - {"registro"}):
        for modo in replay.MODOS:
            linhas = json.loads(json.dumps(LINHAS_DOURADAS))
            linhas[-1][campo] = "adulterado"
            try:
                replay.refazer(linhas, modo)
            except ErroCF:
                continue
            raise AssertionError(f"campo '{campo}' do fim adulterado e não detectado no modo {modo}")

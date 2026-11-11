"""Matriz de ganhos entre estilos (MET-07), estilo dominante (REQ-04) e dinâmica do replicador.

Cada célula (i, j) é a taxa de vitória de 1 bot do estilo i (o "foco") numa mesa
em que os outros N-1 são do estilo j, com rodízio de assentos. Na mesa de bots
iguais, o foco vence exatamente 1/N: com o rodízio, o mesmo jogo é repetido com
o foco em cada assento, e cada jogo distribui exatamente 1 vitória. Por isso a
diagonal não é rodada.

REQ-04 (autor, 2026-11-10): um estilo é **dominante** se é a melhor resposta
contra todas as mesas, inclusive a de bots iguais a ele. Em cada coluna, a
diferença para cada outro estilo precisa ter o intervalo de confiança de 95%
inteiro acima da diferença mínima do critério. Passa se nenhum estilo é
dominante; falha se algum é; inconclusivo se algum não pode ser nem afirmado
nem descartado.

A dinâmica do replicador é um complemento sem veredito. Usa uma aproximação
linear: o ganho de um estilo numa população mista é a média dos ganhos contra
cada população pura, pesada pela proporção de cada estilo.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from numpy.typing import NDArray

from critical_failure.experimentos.config import Cenario, Experimento
from critical_failure.metricas.estatistica import (
    FALHA,
    INCONCLUSIVO,
    PASSA,
    Intervalo,
    intervalo_da_razao,
    veredito,
)
from critical_failure.metricas.requisitos import Medida, amostra_do_foco, rng_da_analise

DOMINANCIA = "REQ-04"
BLEFES = "REQ-05"
PROPORCAO_PURA = 0.999
"""A dinâmica do replicador terminou num perfil só quando ele fica com pelo menos esta proporção."""
CHAVE_DOS_BLEFES = 60_000
DOMINANTE = "dominante"
NAO_DOMINANTE = "não dominante"
INDEFINIDO = "indefinido"
REAMOSTRAS = 1000
CONFIANCA = 0.95
PASSOS_DO_REPLICADOR = 400_000
PASSO_DO_REPLICADOR = 0.05
TOLERANCIA_DO_REPLICADOR = 1e-13
TOLERANCIA_DE_NASH = 1e-6
"""Folga numérica para dizer que nenhum estilo se sai melhor que a média no ponto final."""
CHAVE_DAS_MATRIZES = 50_000
"""Chave do fluxo de aleatoriedade do bootstrap das matrizes, separada das dos outros requisitos."""


@dataclass(frozen=True, slots=True)
class Celula:
    taxa: float
    intervalo: Intervalo | None
    """``None`` na diagonal, que é exata."""
    assentos: int
    """Quantas vezes o foco jogou (0 na diagonal, que não é rodada)."""


@dataclass(frozen=True, slots=True)
class Populacao:
    """Uma mesa de perfis iguais (a diagonal da matriz, quando é rodada): os blefes do REQ-05."""

    estilo: str
    partidas: int
    blefes_por_partida: float
    taxa_de_sucesso: float | None
    """Blefes bem-sucedidos divididos por blefes tentados; ``None`` se ninguém blefou."""
    intervalo: Intervalo | None


@dataclass(frozen=True, slots=True)
class MatrizDeEstilos:
    nome: str
    jogadores: int
    estilos: tuple[str, ...]
    celulas: dict[tuple[str, str], Celula]
    completa: bool
    """Todas as células fora da diagonal foram rodadas. Sem isso não há análise de dominância."""
    partidas: int
    melhores_respostas: dict[str, tuple[str, ...]]
    """Para cada mesa (coluna), os estilos que nenhum outro supera com clareza."""
    situacao: dict[str, str]
    motivo: dict[str, str]
    replicador: dict[str, float]
    replicador_convergiu: bool
    populacoes: tuple[Populacao, ...] = ()
    mede_blefes: bool = False
    """Alguma mesa de perfis iguais desta matriz pede o REQ-05."""


def _medias_por_bootstrap(valores: NDArray[np.float64], rng: np.random.Generator) -> NDArray[np.float64]:
    medias = np.empty(REAMOSTRAS, dtype=np.float64)
    for inicio in range(0, REAMOSTRAS, 50):
        fim = min(inicio + 50, REAMOSTRAS)
        indices = rng.integers(0, valores.size, size=(fim - inicio, valores.size))
        medias[inicio:fim] = valores[indices].mean(axis=1)
    return medias


def _intervalo(medias: NDArray[np.float64]) -> Intervalo:
    cauda = (1 - CONFIANCA) / 2
    baixo, alto = np.quantile(medias, [cauda, 1 - cauda])
    return float(baixo), float(alto)


def replicador(ganhos: NDArray[np.float64]) -> tuple[NDArray[np.float64], bool]:
    """Dinâmica do replicador em tempo contínuo (passo pequeno), a partir da população uniforme.

    ``ganhos[i, j]`` é o ganho do estilo i contra a população pura j. Devolve a
    proporção final de cada estilo e se ela é um ponto de repouso estável de fato:
    a dinâmica parou de mudar **e** nenhum estilo se sai melhor que a média ali
    (um equilíbrio de Nash simétrico do jogo linearizado).

    A versão em tempo discreto com passo cheio, usada antes, espiralava para fora
    em jogos cíclicos (pedra-papel-tesoura) e parava num vértice que outro estilo
    invadia; o teste de Nash abaixo pega esse caso.
    """
    n = ganhos.shape[0]
    x = np.full(n, 1 / n)
    for _ in range(PASSOS_DO_REPLICADOR):
        aptidao = ganhos @ x
        novo = x + PASSO_DO_REPLICADOR * x * (aptidao - float(x @ aptidao))
        novo = np.clip(novo, 0.0, None)
        novo /= novo.sum()
        mudou = float(np.max(np.abs(novo - x)))
        x = novo
        if mudou < TOLERANCIA_DO_REPLICADOR:
            break
    aptidao = ganhos @ x
    estavel = bool(np.all(aptidao <= float(x @ aptidao) + TOLERANCIA_DE_NASH))
    return x, estavel


def _dominancia(
    estilos: tuple[str, ...],
    medias: dict[tuple[str, str], NDArray[np.float64]],
    diferenca_minima: float,
) -> tuple[dict[str, tuple[str, ...]], dict[str, str], dict[str, str]]:
    def supera(i: str, k: str, mesa: str) -> bool:
        baixo, _ = _intervalo(medias[(i, mesa)] - medias[(k, mesa)])
        return baixo > diferenca_minima

    melhores: dict[str, tuple[str, ...]] = {}
    for mesa in estilos:
        melhores[mesa] = tuple(i for i in estilos if not any(supera(k, i, mesa) for k in estilos if k != i))
    situacao: dict[str, str] = {}
    motivo: dict[str, str] = {}
    for i in estilos:
        derrota = next(
            ((k, mesa) for mesa in estilos for k in estilos if k != i and supera(k, i, mesa)),
            None,
        )
        if derrota is not None:
            situacao[i] = NAO_DOMINANTE
            motivo[i] = f"{derrota[0]} se sai melhor contra a mesa de {derrota[1]}"
        elif all(supera(i, k, mesa) for mesa in estilos for k in estilos if k != i):
            situacao[i] = DOMINANTE
            motivo[i] = "melhor resposta, com clareza, contra todas as mesas"
        else:
            situacao[i] = INDEFINIDO
            motivo[i] = "nenhum outro estilo o supera com clareza, mas ele também não supera todos"
    return melhores, situacao, motivo


def montar_matrizes(
    linhas: list[dict[str, Any]], experimento: Experimento, diferenca_minima: float
) -> list[MatrizDeEstilos]:
    por_matriz: dict[str, dict[tuple[str, str], list[Cenario]]] = {}
    diagonais: dict[str, dict[str, list[Cenario]]] = {}
    for cenario in experimento.cenarios_expandidos():
        if cenario.matriz is not None and cenario.celula is not None:
            celula = (cenario.celula[0], cenario.celula[1])
            por_matriz.setdefault(cenario.matriz, {})
            if celula[0] == celula[1]:
                diagonais.setdefault(cenario.matriz, {}).setdefault(celula[0], []).append(cenario)
            else:
                por_matriz[cenario.matriz].setdefault(celula, []).append(cenario)
    resultado: list[MatrizDeEstilos] = []
    for indice_da_matriz, (nome, celulas_rodadas) in enumerate(por_matriz.items()):
        mesas_iguais = diagonais.get(nome, {})
        jogadores = next(iter([*celulas_rodadas.values(), *mesas_iguais.values()]))[0].jogadores
        estilos = tuple(
            dict.fromkeys([*(i for i, _ in celulas_rodadas), *(j for _, j in celulas_rodadas), *mesas_iguais])
        )
        referencia = 1 / jogadores
        medias: dict[tuple[str, str], NDArray[np.float64]] = {}
        celulas: dict[tuple[str, str], Celula] = {}
        partidas = 0
        for indice_da_celula, (celula, cenarios) in enumerate(celulas_rodadas.items()):
            amostra = amostra_do_foco(linhas, cenarios)
            if amostra.size == 0:
                continue
            partidas += amostra.size
            rng = rng_da_analise(experimento.semente_mestre, CHAVE_DAS_MATRIZES + indice_da_matriz, indice_da_celula)
            medias[celula] = _medias_por_bootstrap(amostra, rng)
            celulas[celula] = Celula(float(amostra.mean()), _intervalo(medias[celula]), int(amostra.size))
        for estilo in estilos:
            medias[(estilo, estilo)] = np.full(REAMOSTRAS, referencia)
            celulas[(estilo, estilo)] = Celula(referencia, None, 0)
        completa = all((i, j) in celulas for i in estilos for j in estilos)
        melhores: dict[str, tuple[str, ...]] = {}
        situacao: dict[str, str] = {}
        motivo: dict[str, str] = {}
        proporcoes: dict[str, float] = {}
        convergiu = False
        if completa:
            melhores, situacao, motivo = _dominancia(estilos, medias, diferenca_minima)
            ganhos = np.array([[celulas[(i, j)].taxa for j in estilos] for i in estilos], dtype=np.float64)
            final, convergiu = replicador(ganhos)
            proporcoes = {estilo: float(p) for estilo, p in zip(estilos, final, strict=True)}
        resultado.append(
            MatrizDeEstilos(
                nome=nome,
                jogadores=jogadores,
                estilos=estilos,
                celulas=celulas,
                completa=completa,
                partidas=partidas,
                melhores_respostas=melhores,
                situacao=situacao,
                motivo=motivo,
                replicador=proporcoes,
                replicador_convergiu=convergiu,
                populacoes=_populacoes(linhas, experimento, indice_da_matriz, estilos, mesas_iguais),
                mede_blefes=any(BLEFES in c.requisitos for grupo in mesas_iguais.values() for c in grupo),
            )
        )
    return resultado


def _populacoes(
    linhas: list[dict[str, Any]],
    experimento: Experimento,
    indice_da_matriz: int,
    estilos: tuple[str, ...],
    mesas_iguais: dict[str, list[Cenario]],
) -> tuple[Populacao, ...]:
    populacoes: list[Populacao] = []
    for ordem, estilo in enumerate(estilos):
        nomes = {cenario.nome for cenario in mesas_iguais.get(estilo, [])}
        validas = [
            linha
            for linha in linhas
            if linha["cenario"] in nomes and linha["erro"] is None and linha.get("blefes") is not None
        ]
        if not validas:
            continue
        tentados = np.array([linha["blefes"] for linha in validas], dtype=np.float64)
        sucessos = np.array([linha["blefes_bem_sucedidos"] for linha in validas], dtype=np.float64)
        taxa: float | None = None
        intervalo: Intervalo | None = None
        if tentados.sum() > 0:
            taxa = float(sucessos.sum() / tentados.sum())
            rng = rng_da_analise(experimento.semente_mestre, CHAVE_DOS_BLEFES + indice_da_matriz, ordem)
            intervalo = intervalo_da_razao(sucessos, tentados, rng)
        populacoes.append(Populacao(estilo, len(validas), float(tentados.mean()), taxa, intervalo))
    return tuple(populacoes)


def medidas_de_blefe(matrizes: list[MatrizDeEstilos], criterio: dict[str, Any]) -> list[Medida]:
    """REQ-05 no equilíbrio da dinâmica do replicador (autor, 2026-11-10).

    Se a dinâmica termina num perfil só, vale a mesa de perfis iguais dele. Se
    termina numa mistura, o veredito fica para uma mesa sorteada da mistura, que
    é outro experimento: aqui a medida sai inconclusiva, com a mistura na nota.
    """
    zona = (float(criterio["minimo"]), float(criterio["maximo"]))
    medidas: list[Medida] = []
    for matriz in matrizes:
        if not matriz.completa or not matriz.mede_blefes:
            continue
        puros = [e for e, p in matriz.replicador.items() if p >= PROPORCAO_PURA] if matriz.replicador_convergiu else []
        populacao = next((p for p in matriz.populacoes if puros and p.estilo == puros[0]), None)
        if not puros or populacao is None or populacao.taxa_de_sucesso is None or populacao.intervalo is None:
            if not matriz.replicador_convergiu:
                nota = "a dinâmica do replicador não chegou a um equilíbrio"
            elif not puros:
                mistura = ", ".join(f"{e} {p:.3f}" for e, p in matriz.replicador.items() if p >= 0.0005)
                nota = f"o equilíbrio é uma mistura ({mistura}); falta a mesa sorteada da mistura"
            elif populacao is None:
                nota = f"o equilíbrio é {puros[0]}, mas a mesa de perfis iguais dele não foi rodada"
            else:
                nota = f"o equilíbrio é {puros[0]}, e nessa mesa ninguém blefa"
            medidas.append(
                Medida(
                    requisito=BLEFES,
                    cenario=matriz.nome,
                    o_que="blefes bem-sucedidos no equilíbrio",
                    valor=float("nan"),
                    intervalo=None,
                    zona=zona,
                    veredito=INCONCLUSIVO,
                    partidas=matriz.partidas,
                    nota=nota,
                )
            )
            continue
        medidas.append(
            Medida(
                requisito=BLEFES,
                cenario=f"{matriz.nome}, equilíbrio {populacao.estilo}",
                o_que="blefes bem-sucedidos / blefes tentados",
                valor=populacao.taxa_de_sucesso,
                intervalo=populacao.intervalo,
                zona=zona,
                veredito=veredito(populacao.intervalo, zona),
                partidas=populacao.partidas,
                nota=f"{matriz.nome}: a dinâmica do replicador termina em {populacao.estilo}",
            )
        )
    return medidas


def medidas_de_dominancia(matrizes: list[MatrizDeEstilos], criterio: dict[str, Any]) -> list[Medida]:
    """REQ-04, uma medida por matriz completa."""
    diferenca_minima = float(criterio["diferenca_minima"])
    medidas: list[Medida] = []
    for matriz in matrizes:
        if not matriz.completa:
            continue
        situacoes = list(matriz.situacao.values())
        if DOMINANTE in situacoes:
            resultado = FALHA
        elif INDEFINIDO in situacoes:
            resultado = INCONCLUSIVO
        else:
            resultado = PASSA
        detalhe = "; ".join(f"{estilo}: {matriz.situacao[estilo]}" for estilo in matriz.estilos)
        medidas.append(
            Medida(
                requisito=DOMINANCIA,
                cenario=matriz.nome,
                o_que="estilos dominantes (melhor resposta contra todas as mesas)",
                valor=float(situacoes.count(DOMINANTE)),
                intervalo=None,
                zona=(0.0, 0.0),
                veredito=resultado,
                partidas=matriz.partidas,
                nota=f"{matriz.nome} (diferença mínima {diferenca_minima:g}): {detalhe}",
            )
        )
    return medidas

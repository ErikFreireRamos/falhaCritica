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
from critical_failure.metricas.estatistica import FALHA, INCONCLUSIVO, PASSA, Intervalo
from critical_failure.metricas.requisitos import Medida, amostra_do_foco, rng_da_analise

DOMINANCIA = "REQ-04"
DOMINANTE = "dominante"
NAO_DOMINANTE = "não dominante"
INDEFINIDO = "indefinido"
REAMOSTRAS = 1000
CONFIANCA = 0.95
PASSOS_DO_REPLICADOR = 200_000
TOLERANCIA_DO_REPLICADOR = 1e-12
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
    """Dinâmica do replicador em tempo discreto, a partir da população uniforme.

    ``ganhos[i, j]`` é o ganho do estilo i contra a população pura j. Devolve a
    proporção final de cada estilo e se a dinâmica parou de mudar.
    """
    n = ganhos.shape[0]
    x = np.full(n, 1 / n)
    for _ in range(PASSOS_DO_REPLICADOR):
        aptidao = ganhos @ x
        media = float(x @ aptidao)
        if media <= 0:
            return x, False
        novo = x * aptidao / media
        if float(np.max(np.abs(novo - x))) < TOLERANCIA_DO_REPLICADOR:
            return novo, True
        x = novo
    return x, False


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
    for cenario in experimento.cenarios_expandidos():
        if cenario.matriz is not None and cenario.celula is not None:
            celula = (cenario.celula[0], cenario.celula[1])
            por_matriz.setdefault(cenario.matriz, {}).setdefault(celula, []).append(cenario)
    resultado: list[MatrizDeEstilos] = []
    for indice_da_matriz, (nome, celulas_rodadas) in enumerate(por_matriz.items()):
        jogadores = next(iter(celulas_rodadas.values()))[0].jogadores
        estilos = tuple(dict.fromkeys([*(i for i, _ in celulas_rodadas), *(j for _, j in celulas_rodadas)]))
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
            )
        )
    return resultado


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

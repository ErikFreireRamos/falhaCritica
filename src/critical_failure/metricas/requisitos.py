"""Mede os requisitos de balanceamento a partir da tabela de partidas de um experimento.

Só recebe veredito o requisito que o autor confirmou em ``configs/requisitos.yaml``
(``estado: confirmado``) e que tem ``criterio`` em forma estruturada. A zona de
aceite vem desse arquivo, fixada antes de o experimento rodar.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from critical_failure.experimentos.config import Cenario, Experimento
from critical_failure.metricas.estatistica import (
    FALHA,
    INCONCLUSIVO,
    PASSA,
    Intervalo,
    intervalo_por_bootstrap,
    veredito,
)
from critical_failure.nucleo.erros import ConfiguracaoInvalida

FLUXO_DO_BOOTSTRAP = 900_000
"""Fluxo de aleatoriedade do bootstrap, separado dos fluxos das partidas."""

EQUIDADE_DE_ASSENTO = "REQ-01"
DURACAO = "REQ-08"
ROBUSTEZ = "REQ-09"


@dataclass(frozen=True, slots=True)
class Medida:
    requisito: str
    cenario: str
    o_que: str
    valor: float
    intervalo: Intervalo | None
    zona: Intervalo | None
    veredito: str
    partidas: int
    nota: str = ""


def carregar_requisitos(caminho: Path) -> dict[str, dict[str, Any]]:
    try:
        dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
        blocos = [*dados["requisitos"], *dados.get("metricas_registradas", [])]
        return {bloco["id"]: bloco for bloco in blocos}
    except (OSError, yaml.YAMLError, KeyError, TypeError) as erro:
        raise ConfiguracaoInvalida(f"arquivo de requisitos inválido ({caminho}): {erro!r}") from erro


def _criterio(requisitos: dict[str, dict[str, Any]], ident: str) -> dict[str, Any] | None:
    """O critério estruturado do requisito, se o autor já o confirmou."""
    bloco = requisitos.get(ident)
    if bloco is None or bloco.get("estado") != "confirmado" or not isinstance(bloco.get("criterio"), dict):
        return None
    criterio: dict[str, Any] = bloco["criterio"]
    return criterio


def _rng(semente: int, *chave: int) -> np.random.Generator:
    sequencia = np.random.SeedSequence(entropy=semente, spawn_key=(FLUXO_DO_BOOTSTRAP, *chave))
    return np.random.Generator(np.random.PCG64(sequencia))


def _equidade_de_assento(
    cenario: Cenario, indice: int, linhas: list[dict[str, Any]], criterio: dict[str, Any], semente: int
) -> list[Medida]:
    """REQ-01: fração de vitórias de cada posição da ordem inicial, com vitória dividida (AMB-14)."""
    n = cenario.jogadores
    margem = float(criterio["margem"])
    zona = (1 / n - margem, 1 / n + margem)
    medidas: list[Medida] = []
    for posicao in range(n):
        fatias = np.array(
            [1 / len(linha["vencedores"]) if posicao in linha["vencedores"] else 0.0 for linha in linhas],
            dtype=np.float64,
        )
        intervalo = intervalo_por_bootstrap(fatias, "media", _rng(semente, indice, posicao))
        medidas.append(
            Medida(
                requisito=EQUIDADE_DE_ASSENTO,
                cenario=cenario.nome,
                o_que=f"taxa de vitória da posição {posicao}",
                valor=float(fatias.mean()),
                intervalo=intervalo,
                zona=zona,
                veredito=veredito(intervalo, zona),
                partidas=len(linhas),
            )
        )
    return medidas


def _duracao(
    cenario: Cenario, indice: int, linhas: list[dict[str, Any]], criterio: dict[str, Any], semente: int
) -> list[Medida]:
    """REQ-08: mediana da duração estimada pelo modelo MOD-05, em minutos."""
    minutos = np.array([linha["duracao_s"] / 60 for linha in linhas], dtype=np.float64)
    zona = (float(criterio["minimo"]), float(criterio["maximo"]))
    intervalo = intervalo_por_bootstrap(minutos, "mediana", _rng(semente, indice, cenario.jogadores))
    return [
        Medida(
            requisito=DURACAO,
            cenario=cenario.nome,
            o_que="mediana da duração estimada (min)",
            valor=float(np.median(minutos)),
            intervalo=intervalo,
            zona=zona,
            veredito=veredito(intervalo, zona),
            partidas=len(linhas),
            nota="depende dos tempos provisórios de configs/duracao.yaml (MOD-05)",
        )
    ]


def _robustez(linhas: list[dict[str, Any]], criterio: dict[str, Any]) -> Medida:
    """REQ-09: nenhuma exceção nem violação de invariante no número de partidas pedido."""
    falhas = sum(1 for linha in linhas if linha["erro"] is not None)
    minimo = int(criterio["partidas_minimas"])
    if falhas:
        resultado = FALHA
    elif len(linhas) >= minimo:
        resultado = PASSA
    else:
        resultado = INCONCLUSIVO
    return Medida(
        requisito=ROBUSTEZ,
        cenario="todos",
        o_que="partidas com exceção ou violação de invariante",
        valor=float(falhas),
        intervalo=None,
        zona=(0.0, 0.0),
        veredito=resultado,
        partidas=len(linhas),
        nota=f"o critério pede pelo menos {minimo} partidas",
    )


def avaliar(
    linhas: list[dict[str, Any]], experimento: Experimento, requisitos: dict[str, dict[str, Any]]
) -> list[Medida]:
    """Mede os requisitos confirmados que cada cenário pede. A robustez vale para o experimento inteiro."""
    medidas: list[Medida] = []
    for indice, cenario in enumerate(experimento.cenarios):
        validas = [linha for linha in linhas if linha["cenario"] == cenario.nome and linha["erro"] is None]
        if not validas:
            continue
        if EQUIDADE_DE_ASSENTO in cenario.requisitos:
            criterio = _criterio(requisitos, EQUIDADE_DE_ASSENTO)
            if criterio is not None and cenario.bots_identicos():
                medidas += _equidade_de_assento(cenario, indice, validas, criterio, experimento.semente_mestre)
        if DURACAO in cenario.requisitos:
            criterio = _criterio(requisitos, DURACAO)
            if criterio is not None:
                medidas += _duracao(cenario, indice, validas, criterio, experimento.semente_mestre)
    criterio = _criterio(requisitos, ROBUSTEZ)
    if criterio is not None:
        medidas.append(_robustez(linhas, criterio))
    return medidas


def descrever(linhas: list[dict[str, Any]], experimento: Experimento) -> list[dict[str, Any]]:
    """Números descritivos por cenário. Não têm critério de aceite."""
    descricoes: list[dict[str, Any]] = []
    for cenario in experimento.cenarios:
        do_cenario = [linha for linha in linhas if linha["cenario"] == cenario.nome]
        validas = [linha for linha in do_cenario if linha["erro"] is None]
        if not validas:
            descricoes.append({"cenario": cenario.nome, "partidas": len(do_cenario), "falhas": len(do_cenario)})
            continue
        minutos = np.array([linha["duracao_s"] / 60 for linha in validas])
        p10, p50, p90 = (float(x) for x in np.quantile(minutos, [0.1, 0.5, 0.9]))
        descricoes.append(
            {
                "cenario": cenario.nome,
                "partidas": len(do_cenario),
                "falhas": len(do_cenario) - len(validas),
                "testes_por_partida": float(np.mean([linha["testes"] for linha in validas])),
                "contestacoes_por_partida": float(np.mean([linha["contestacoes"] for linha in validas])),
                "vitorias_divididas": float(np.mean([linha["criterio"] == "dividida" for linha in validas])),
                "partidas_com_reembaralhamento": float(np.mean([linha["reembaralhamentos"] > 0 for linha in validas])),
                "partidas_com_compra_impossivel": float(
                    np.mean([linha["compras_impossiveis"] + linha["reposicoes_impossiveis"] > 0 for linha in validas])
                ),
                "fichas_do_vencedor": float(np.mean([max(linha["placar"]) for linha in validas])),
                "fichas_medias": float(np.mean([np.mean(linha["placar"]) for linha in validas])),
                "duracao_p10": p10,
                "duracao_mediana": p50,
                "duracao_p90": p90,
            }
        )
    return descricoes

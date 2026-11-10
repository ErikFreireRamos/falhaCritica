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
    intervalo_da_diferenca,
    intervalo_de_wilson,
    intervalo_por_bootstrap,
    veredito,
)
from critical_failure.nucleo.erros import ConfiguracaoInvalida

FLUXO_DO_BOOTSTRAP = 900_000
"""Fluxo de aleatoriedade do bootstrap, separado dos fluxos das partidas."""

EQUIDADE_DE_ASSENTO = "REQ-01"
ANTI_BOLA_DE_NEVE = "REQ-02"
DURACAO = "REQ-08"
ROBUSTEZ = "REQ-09"
DESEQUILIBRIO = "MET-01"
ARTIGO_DESEQUILIBRADAS = (4, 6)
"""Artigo, seção 4.4: 4 das 6 partidas foram vencidas por pontuação bem maior que a dos outros."""


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
    for indice, cenario in enumerate(experimento.cenarios_expandidos()):
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
    criterio = _criterio(requisitos, ANTI_BOLA_DE_NEVE)
    if criterio is not None:
        medidas += _anti_bola_de_neve(linhas, experimento, criterio)
    criterio = _criterio(requisitos, ROBUSTEZ)
    if criterio is not None:
        medidas.append(_robustez(linhas, criterio))
    return medidas


def grupos(experimento: Experimento) -> dict[str, list[Cenario]]:
    """Os cenários de cada grupo (as rotações de um rodízio formam um grupo), na ordem do arquivo."""
    resultado: dict[str, list[Cenario]] = {}
    for cenario in experimento.cenarios_expandidos():
        resultado.setdefault(cenario.grupo or cenario.nome, []).append(cenario)
    return resultado


def _validas_do_grupo(linhas: list[dict[str, Any]], cenarios: list[Cenario]) -> list[dict[str, Any]]:
    nomes = {cenario.nome for cenario in cenarios}
    return [linha for linha in linhas if linha["cenario"] in nomes and linha["erro"] is None]


def amostra_do_lider(linhas: list[dict[str, Any]]) -> np.ndarray[Any, np.dtype[np.float64]]:
    """Para cada partida com líder isolado no corte: 1 se ele venceu, 1/k numa vitória dividida, 0 se perdeu."""
    valores: list[float] = []
    for linha in linhas:
        corte = linha.get("placar_no_corte")
        if not corte:
            continue
        maximo = max(corte)
        lideres = [assento for assento, valor in enumerate(corte) if valor == maximo]
        if len(lideres) != 1:
            continue
        vencedores = linha["vencedores"]
        valores.append(1 / len(vencedores) if lideres[0] in vencedores else 0.0)
    return np.array(valores, dtype=np.float64)


def _anti_bola_de_neve(
    linhas: list[dict[str, Any]], experimento: Experimento, criterio: dict[str, Any]
) -> list[Medida]:
    """REQ-02: a vantagem do líder, P(vencer | líder isolado no corte) - 1/N, cai pelo menos a margem da v1 à v2."""
    por_grupo = grupos(experimento)
    medidas: list[Medida] = []
    for indice, (grupo, cenarios) in enumerate(por_grupo.items()):
        base = cenarios[0].comparar_com
        if ANTI_BOLA_DE_NEVE not in cenarios[0].requisitos or base is None:
            continue
        if base not in por_grupo:
            raise ConfiguracaoInvalida(f"o cenário {grupo} compara com {base}, que não existe no experimento")
        n_novo, n_base = cenarios[0].jogadores, por_grupo[base][0].jogadores
        novo = amostra_do_lider(_validas_do_grupo(linhas, cenarios))
        antigo = amostra_do_lider(_validas_do_grupo(linhas, por_grupo[base]))
        if novo.size == 0 or antigo.size == 0:
            continue
        rng = _rng(experimento.semente_mestre, 20_000 + indice)
        vantagem_antiga = antigo - 1 / n_base
        vantagem_nova = novo - 1 / n_novo
        intervalo = intervalo_da_diferenca(vantagem_antiga, vantagem_nova, rng)
        margem = float(criterio["margem"])
        diferenca = float(vantagem_antiga.mean() - vantagem_nova.mean())
        medidas.append(
            Medida(
                requisito=ANTI_BOLA_DE_NEVE,
                cenario=grupo,
                o_que=f"vantagem do líder em {base} menos a vantagem em {grupo}",
                valor=diferenca,
                intervalo=intervalo,
                zona=(margem, 1.0),
                veredito=veredito(intervalo, (margem, 1.0)),
                partidas=int(novo.size + antigo.size),
                nota=(
                    f"vantagem do líder: {base} {float(vantagem_antiga.mean()):.3f} "
                    f"({antigo.size} partidas com líder isolado); {grupo} {float(vantagem_nova.mean()):.3f} "
                    f"({novo.size} partidas)"
                ),
            )
        )
    return medidas


def desequilibrio(
    linhas: list[dict[str, Any]], experimento: Experimento, requisitos: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """MET-01: fração de partidas em que o vencedor tem pelo menos ``fator`` vezes a média dos demais.

    Sem veredito: a métrica é comparada com as 4 de 6 do artigo só como checagem de plausibilidade.
    """
    criterio = _criterio(requisitos, DESEQUILIBRIO)
    if criterio is None:
        return []
    fatores = [float(criterio["fator"]), *(float(f) for f in criterio.get("sensibilidade", []))]
    resultado: list[dict[str, Any]] = []
    for grupo, cenarios in grupos(experimento).items():
        validas = _validas_do_grupo(linhas, cenarios)
        if not validas:
            continue
        for posicao, fator in enumerate(fatores):
            desequilibradas = 0
            for linha in validas:
                placar = sorted(linha["placar"], reverse=True)
                media_dos_outros = sum(placar[1:]) / (len(placar) - 1)
                if placar[0] >= fator * media_dos_outros and placar[0] > 0:
                    desequilibradas += 1
            resultado.append(
                {
                    "grupo": grupo,
                    "familia": validas[0]["familia"],
                    "jogadores": cenarios[0].jogadores,
                    "partidas": len(validas),
                    "fator": fator,
                    "principal": posicao == 0,
                    "proporcao": desequilibradas / len(validas),
                    "intervalo": intervalo_de_wilson(desequilibradas, len(validas)),
                }
            )
    return resultado


def descrever(linhas: list[dict[str, Any]], experimento: Experimento) -> list[dict[str, Any]]:
    """Números descritivos por cenário. Não têm critério de aceite."""
    descricoes: list[dict[str, Any]] = []
    for cenario in experimento.cenarios_expandidos():
        do_cenario = [linha for linha in linhas if linha["cenario"] == cenario.nome]
        validas = [linha for linha in do_cenario if linha["erro"] is None]
        if not validas:
            descricoes.append({"cenario": cenario.nome, "partidas": len(do_cenario), "falhas": len(do_cenario)})
            continue
        p10 = p50 = p90 = None
        if all(linha["duracao_s"] is not None for linha in validas):
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
                "vantagem_do_lider": (
                    float(amostra.mean() - 1 / cenario.jogadores)
                    if (amostra := amostra_do_lider(validas)).size
                    else None
                ),
                "fichas_do_vencedor": float(np.mean([max(linha["placar"]) for linha in validas])),
                "fichas_medias": float(np.mean([np.mean(linha["placar"]) for linha in validas])),
                "duracao_p10": p10,
                "duracao_mediana": p50,
                "duracao_p90": p90,
            }
        )
    return descricoes


def vitorias_por_bot(linhas: list[dict[str, Any]], experimento: Experimento) -> list[dict[str, Any]]:
    """MET-07: taxa de vitória de cada bot nos grupos de cenários com bots diferentes.

    Para cada assento ocupado por um bot conta 1 se ele venceu sozinho, 1/k numa
    vitória dividida por k (AMB-14) e 0 se perdeu; a taxa é a média disso. A
    referência de quem não leva vantagem nenhuma é 1/N. As rotações de um rodízio
    são somadas no mesmo grupo. Sem veredito: a métrica aguarda o autor.
    """
    grupos: dict[str, list[Cenario]] = {}
    for cenario in experimento.cenarios_expandidos():
        if not cenario.bots_identicos():
            grupos.setdefault(cenario.grupo or cenario.nome, []).append(cenario)
    resultado: list[dict[str, Any]] = []
    for indice, (grupo, cenarios) in enumerate(grupos.items()):
        fatias: dict[str, list[float]] = {}
        for cenario in cenarios:
            nomes = [bot.nome() for bot in cenario.bots_por_assento()]
            for linha in linhas:
                if linha["cenario"] != cenario.nome or linha["erro"] is not None:
                    continue
                vencedores = linha["vencedores"]
                for assento, nome in enumerate(nomes):
                    fatias.setdefault(nome, []).append(1 / len(vencedores) if assento in vencedores else 0.0)
        jogadores = cenarios[0].jogadores
        for ordem, (nome, valores) in enumerate(sorted(fatias.items())):
            amostra = np.array(valores, dtype=np.float64)
            intervalo = intervalo_por_bootstrap(
                amostra,
                "media",
                _rng(experimento.semente_mestre, len(experimento.cenarios_expandidos()) + indice, ordem),
            )
            resultado.append(
                {
                    "grupo": grupo,
                    "bot": nome,
                    "jogadores": jogadores,
                    "assentos_jogados": len(valores),
                    "taxa": float(amostra.mean()),
                    "intervalo": intervalo,
                    "referencia": 1 / jogadores,
                }
            )
    return resultado

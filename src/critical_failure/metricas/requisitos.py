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
    intervalo_da_razao,
    intervalo_de_wilson,
    intervalo_do_quantil_por_grupos,
    intervalo_por_bootstrap,
    veredito,
)
from critical_failure.nucleo.erros import ConfiguracaoInvalida

FLUXO_DO_BOOTSTRAP = 900_000
"""Fluxo de aleatoriedade do bootstrap, separado dos fluxos das partidas."""

EQUIDADE_DE_ASSENTO = "REQ-01"
ANTI_BOLA_DE_NEVE = "REQ-02"
HABILIDADE = "REQ-03"
DURACAO = "REQ-08"
ROBUSTEZ = "REQ-09"
DISTRIBUICAO_DE_ATAQUES = "REQ-06"
FICHAS_NAO_ZERAM = "REQ-07"
TEMPO_PARADO = "REQ-10"
PRIMEIRO_INCIDENTE = "REQ-12"
PESO_DOS_INCIDENTES = "REQ-13"
BLEFES_BEM_SUCEDIDOS = "REQ-05"
OS_DOIS_ESTILOS = "REQ-11"
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


def criterio_confirmado(requisitos: dict[str, dict[str, Any]], ident: str) -> dict[str, Any] | None:
    """O critério estruturado do requisito, se o autor já o confirmou."""
    bloco = requisitos.get(ident)
    if bloco is None or bloco.get("estado") != "confirmado" or not isinstance(bloco.get("criterio"), dict):
        return None
    criterio: dict[str, Any] = bloco["criterio"]
    return criterio


def rng_da_analise(semente: int, *chave: int) -> np.random.Generator:
    """Gerador do bootstrap, derivado da semente do experimento e de uma chave própria de cada medida."""
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
        intervalo = intervalo_por_bootstrap(fatias, "media", rng_da_analise(semente, indice, posicao))
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
    intervalo = intervalo_por_bootstrap(minutos, "mediana", rng_da_analise(semente, indice, cenario.jogadores))
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


def _da_coleta(linhas: list[dict[str, Any]], coluna: str) -> list[dict[str, Any]]:
    """As partidas que têm a medida do coletor (a v2, numa tabela que já tem a coluna)."""
    return [linha for linha in linhas if linha.get(coluna) is not None]


def _distribuicao_de_ataques(
    cenario: Cenario, indice: int, linhas: list[dict[str, Any]], criterio: dict[str, Any], semente: int
) -> list[Medida]:
    """REQ-06: (a) razão máximo/média de testes recebidos; (b) fração dos testes contra o menor placar."""
    com_testes = [linha for linha in _da_coleta(linhas, "testes_recebidos") if sum(linha["testes_recebidos"]) > 0]
    if not com_testes:
        return []
    n = cenario.jogadores
    razoes = np.array([max(t) / (sum(t) / len(t)) for t in (linha["testes_recebidos"] for linha in com_testes)])
    zona_a = (0.0, float(criterio["razao_maxima"]))
    intervalo_a = intervalo_por_bootstrap(razoes, "media", rng_da_analise(semente, 70_000 + indice))
    contra = np.array([linha["testes_contra_o_menor"] for linha in com_testes], dtype=np.float64)
    testes = np.array([sum(linha["testes_recebidos"]) for linha in com_testes], dtype=np.float64)
    zona_b = (0.0, 1 / (n - 1) + float(criterio["acima_do_uniforme"]))
    intervalo_b = intervalo_da_razao(contra, testes, rng_da_analise(semente, 71_000 + indice))
    return [
        Medida(
            DISTRIBUICAO_DE_ATAQUES,
            cenario.nome,
            "(a) média da razão máximo/média de testes recebidos",
            float(razoes.mean()),
            intervalo_a,
            zona_a,
            veredito(intervalo_a, zona_a),
            len(com_testes),
        ),
        Medida(
            DISTRIBUICAO_DE_ATAQUES,
            cenario.nome,
            "(b) fração dos testes contra quem tinha o menor placar",
            float(contra.sum() / testes.sum()),
            intervalo_b,
            zona_b,
            veredito(intervalo_b, zona_b),
            len(com_testes),
            nota="(b): empate no menor placar conta como teste contra o menor",
        ),
    ]


def _fichas_nao_zeram(
    cenario: Cenario, indice: int, linhas: list[dict[str, Any]], criterio: dict[str, Any], semente: int
) -> list[Medida]:
    """REQ-07: fração de partidas em que alguém ficou com 0 ficha antes do último ciclo."""
    partidas = _da_coleta(linhas, "zerado_antes_do_ultimo_ciclo")
    if not partidas:
        return []
    zeradas = sum(1 for linha in partidas if linha["zerado_antes_do_ultimo_ciclo"])
    zona = (0.0, float(criterio["maximo"]))
    intervalo = intervalo_de_wilson(zeradas, len(partidas))
    return [
        Medida(
            FICHAS_NAO_ZERAM,
            cenario.nome,
            "partidas com alguém em 0 ficha antes do último ciclo",
            zeradas / len(partidas),
            intervalo,
            zona,
            veredito(intervalo, zona),
            len(partidas),
        )
    ]


def _tempo_parado(
    cenario: Cenario, indice: int, linhas: list[dict[str, Any]], criterio: dict[str, Any], semente: int
) -> list[Medida]:
    """REQ-10: quantil do tempo parado por jogador e por ciclo, em minutos, com bootstrap sobre as partidas."""
    partidas = _da_coleta(linhas, "parado_s")
    if not partidas:
        return []
    quantil = float(criterio["quantil"])
    grupos = [np.array(linha["parado_s"], dtype=np.float64) / 60 for linha in partidas]
    valor = float(np.quantile(np.concatenate(grupos), quantil))
    intervalo = intervalo_do_quantil_por_grupos(grupos, quantil, rng_da_analise(semente, 72_000 + indice))
    zona = (0.0, float(criterio["maximo_min"]))
    return [
        Medida(
            TEMPO_PARADO,
            cenario.nome,
            f"percentil {round(100 * quantil)} do tempo parado por jogador e ciclo (min)",
            valor,
            intervalo,
            zona,
            veredito(intervalo, zona),
            len(partidas),
            nota="depende dos tempos provisórios de configs/duracao.yaml (MOD-05)",
        )
    ]


def _primeiro_incidente(
    cenario: Cenario, indice: int, linhas: list[dict[str, Any]], criterio: dict[str, Any], semente: int
) -> list[Medida]:
    """REQ-12: taxa de vitória de quem começou cobrindo a categoria-chave do incidente 1, menos a dos demais."""
    cobre: list[float] = []
    nao_cobre: list[float] = []
    for linha in _da_coleta(linhas, "cobre_incidente_1"):
        vencedores = linha["vencedores"]
        for assento, cobria in enumerate(linha["cobre_incidente_1"]):
            fatia = 1 / len(vencedores) if assento in vencedores else 0.0
            (cobre if cobria else nao_cobre).append(fatia)
    if not cobre or not nao_cobre:
        return []
    a, b = np.array(cobre), np.array(nao_cobre)
    limite = float(criterio["diferenca_maxima"])
    zona = (-limite, limite)
    intervalo = intervalo_da_diferenca(a, b, rng_da_analise(semente, 73_000 + indice))
    return [
        Medida(
            PRIMEIRO_INCIDENTE,
            cenario.nome,
            "vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais",
            float(a.mean() - b.mean()),
            intervalo,
            zona,
            veredito(intervalo, zona),
            len(linhas),
            nota=f"{cenario.nome}: {a.size} assentos começaram cobrindo, {b.size} não",
        )
    ]


def _peso_dos_incidentes(
    cenario: Cenario, indice: int, linhas: list[dict[str, Any]], criterio: dict[str, Any], semente: int
) -> list[Medida]:
    """REQ-13 (definição do autor em 2026-11-14): fichas movimentadas pelos incidentes, o dano e o ganho do
    diagnóstico, divididas pelo total de fichas movimentadas (ganhos e perdas, todas as fontes). Uma tabela de
    antes dessa definição não tem a coluna do diagnóstico, e o requisito não é medido nela."""
    partidas = [
        linha
        for linha in _da_coleta(_da_coleta(linhas, "fichas_movimentadas"), "fichas_de_diagnostico")
        if linha["fichas_movimentadas"] > 0
    ]
    if not partidas:
        return []
    incidente = np.array(
        [linha["fichas_de_dano"] + linha["fichas_de_diagnostico"] for linha in partidas], dtype=np.float64
    )
    total = np.array([linha["fichas_movimentadas"] for linha in partidas], dtype=np.float64)
    zona = (float(criterio["minimo"]), float(criterio["maximo"]))
    intervalo = intervalo_da_razao(incidente, total, rng_da_analise(semente, 74_000 + indice))
    return [
        Medida(
            PESO_DOS_INCIDENTES,
            cenario.nome,
            "fichas dos incidentes (dano e diagnóstico) / fichas movimentadas",
            float(incidente.sum() / total.sum()),
            intervalo,
            zona,
            veredito(intervalo, zona),
            len(partidas),
            nota="o Critical Failure não conta como incidente",
        )
    ]


def _blefes_na_mesa_sorteada(
    cenario: Cenario, indice: int, linhas: list[dict[str, Any]], criterio: dict[str, Any], semente: int
) -> list[Medida]:
    """REQ-05 numa mesa sorteada da mistura do equilíbrio: blefes bem-sucedidos sobre blefes tentados.

    Só vale em cenário com ``pesos``: numa população pura, o veredito sai da matriz (``matrizes.py``).
    """
    if cenario.pesos is None:
        return []
    partidas = [linha for linha in _da_coleta(linhas, "blefes")]
    tentados = np.array([linha["blefes"] for linha in partidas], dtype=np.float64)
    if not partidas or tentados.sum() <= 0:
        return []
    sucessos = np.array([linha["blefes_bem_sucedidos"] for linha in partidas], dtype=np.float64)
    zona = (float(criterio["minimo"]), float(criterio["maximo"]))
    intervalo = intervalo_da_razao(sucessos, tentados, rng_da_analise(semente, 75_000 + indice))
    mistura = ", ".join(f"{bot.nome()} {peso}" for bot, peso in zip(cenario.bots, cenario.pesos, strict=True))
    return [
        Medida(
            BLEFES_BEM_SUCEDIDOS,
            cenario.nome,
            "blefes bem-sucedidos / blefes tentados, na mesa sorteada da mistura",
            float(sucessos.sum() / tentados.sum()),
            intervalo,
            zona,
            veredito(intervalo, zona),
            len(partidas),
            nota=f"{cenario.nome}: pesos da mistura ({mistura}); {int(tentados.sum())} blefes tentados",
        )
    ]


MEDIDAS_POR_CENARIO = {
    BLEFES_BEM_SUCEDIDOS: _blefes_na_mesa_sorteada,
    DISTRIBUICAO_DE_ATAQUES: _distribuicao_de_ataques,
    FICHAS_NAO_ZERAM: _fichas_nao_zeram,
    TEMPO_PARADO: _tempo_parado,
    PRIMEIRO_INCIDENTE: _primeiro_incidente,
    PESO_DOS_INCIDENTES: _peso_dos_incidentes,
}
"""Requisitos medidos cenário a cenário, além do REQ-01 e do REQ-08."""


def equilibrio_interno(linhas: list[dict[str, Any]], experimento: Experimento) -> list[dict[str, Any]]:
    """Descrição, sem critério, do equilíbrio dentro da partida (REQ-06, 07, 10, 12, 13 e 14), por cenário.
    O peso do dano (só o dano, a definição do REQ-13 até 2026-11-14) continua como descrição."""
    resultado: list[dict[str, Any]] = []
    for nome, cenarios in _unidades_de_descricao(experimento).items():
        nomes = {cenario.nome for cenario in cenarios}
        validas = [linha for linha in linhas if linha["cenario"] in nomes and linha["erro"] is None]
        com_coleta = _da_coleta(validas, "testes_recebidos")
        if not com_coleta:
            continue
        com_testes = [linha for linha in com_coleta if sum(linha["testes_recebidos"]) > 0]
        testes = sum(sum(linha["testes_recebidos"]) for linha in com_coleta)
        parado = [linha["parado_s"] for linha in com_coleta if linha.get("parado_s") is not None]
        movimentadas = sum(linha["fichas_movimentadas"] for linha in com_coleta)
        resultado.append(
            {
                "cenario": nome,
                "razao_de_testes": (
                    float(np.mean([max(t) / (sum(t) / len(t)) for t in (x["testes_recebidos"] for x in com_testes)]))
                    if com_testes
                    else None
                ),
                "contra_o_menor": sum(linha["testes_contra_o_menor"] for linha in com_coleta) / testes
                if testes
                else None,
                "zeradas": float(np.mean([linha["zerado_antes_do_ultimo_ciclo"] for linha in com_coleta])),
                "parado_p90_min": float(np.quantile(np.concatenate(parado), 0.9)) / 60 if parado else None,
                "peso_do_dano": (
                    sum(linha["fichas_de_dano"] for linha in com_coleta) / movimentadas if movimentadas else None
                ),
                "peso_do_incidente": (
                    sum(linha["fichas_de_dano"] + linha["fichas_de_diagnostico"] for linha in com_coleta) / movimentadas
                    if movimentadas and all(linha.get("fichas_de_diagnostico") is not None for linha in com_coleta)
                    else None
                ),
                "dispersao_final": float(
                    np.mean([max(linha["placar"]) - min(linha["placar"]) for linha in com_coleta])
                ),
            }
        )
    return resultado


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
            criterio = criterio_confirmado(requisitos, EQUIDADE_DE_ASSENTO)
            if criterio is not None and cenario.bots_identicos():
                medidas += _equidade_de_assento(cenario, indice, validas, criterio, experimento.semente_mestre)
        if DURACAO in cenario.requisitos:
            criterio = criterio_confirmado(requisitos, DURACAO)
            if criterio is not None:
                medidas += _duracao(cenario, indice, validas, criterio, experimento.semente_mestre)
        for ident, medir in MEDIDAS_POR_CENARIO.items():
            criterio = criterio_confirmado(requisitos, ident)
            if ident in cenario.requisitos and criterio is not None:
                medidas += medir(cenario, indice, validas, criterio, experimento.semente_mestre)
    criterio = criterio_confirmado(requisitos, ANTI_BOLA_DE_NEVE)
    if criterio is not None:
        medidas += _anti_bola_de_neve(linhas, experimento, criterio)
    criterio = criterio_confirmado(requisitos, HABILIDADE)
    if criterio is not None:
        medidas += _habilidade(linhas, experimento, criterio)
    criterio = criterio_confirmado(requisitos, OS_DOIS_ESTILOS)
    if criterio is not None:
        medidas += _os_dois_estilos(linhas, experimento, criterio)
    criterio = criterio_confirmado(requisitos, ROBUSTEZ)
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
        rng = rng_da_analise(experimento.semente_mestre, 20_000 + indice)
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


def amostra_do_foco(linhas: list[dict[str, Any]], cenarios: list[Cenario]) -> np.ndarray[Any, np.dtype[np.float64]]:
    """Para cada partida das rotações: 1 se o bot "foco" venceu, 1/k numa vitória dividida por k, 0 se perdeu."""
    valores: list[float] = []
    for cenario in cenarios:
        assento = next(i for i, bot in enumerate(cenario.bots_por_assento()) if bot.rotulo == "foco")
        for linha in linhas:
            if linha["cenario"] == cenario.nome and linha["erro"] is None:
                vencedores = linha["vencedores"]
                valores.append(1 / len(vencedores) if assento in vencedores else 0.0)
    return np.array(valores, dtype=np.float64)


def _habilidade(linhas: list[dict[str, Any]], experimento: Experimento, criterio: dict[str, Any]) -> list[Medida]:
    """REQ-03: a taxa de vitória do bot foco (o Heurístico) fica acima de ``fator_minimo``/N."""
    medidas: list[Medida] = []
    for indice, (grupo, cenarios) in enumerate(grupos(experimento).items()):
        if HABILIDADE not in cenarios[0].requisitos:
            continue
        if not any(bot.rotulo == "foco" for bot in cenarios[0].bots):
            raise ConfiguracaoInvalida(f"o cenário {grupo} mede o REQ-03, mas não tem bot com rótulo foco")
        amostra = amostra_do_foco(linhas, cenarios)
        if amostra.size == 0:
            continue
        zona = (float(criterio["fator_minimo"]) / cenarios[0].jogadores, 1.0)
        intervalo = intervalo_por_bootstrap(
            amostra, "media", rng_da_analise(experimento.semente_mestre, 30_000 + indice)
        )
        medidas.append(
            Medida(
                requisito=HABILIDADE,
                cenario=grupo,
                o_que="taxa de vitória do bot foco",
                valor=float(amostra.mean()),
                intervalo=intervalo,
                zona=zona,
                veredito=veredito(intervalo, zona),
                partidas=int(amostra.size),
                nota=f"piso {float(criterio['fator_minimo']):g}/N; o teto ficou de fora (autor, 2026-11-10)",
            )
        )
    return medidas


def fracao_de_sistemas_cheios(linha: dict[str, Any]) -> float | None:
    """REQ-11: fração dos jogadores da partida com o sistema no teto ao fim do Planejamento do ciclo 1."""
    cheios = linha.get("cheios_no_planejamento_1")
    if not cheios:
        return None
    return sum(1 for cheio in cheios if cheio) / len(cheios)


def _os_dois_estilos(linhas: list[dict[str, Any]], experimento: Experimento, criterio: dict[str, Any]) -> list[Medida]:
    """REQ-11: a fração de jogadores com o sistema cheio ao fim do 1º Planejamento fica dentro da zona.

    A média é sobre as partidas (cada partida contribui com a sua fração), e o
    intervalo vem do bootstrap sobre as partidas, porque os jogadores da mesma
    partida não são independentes.
    """
    medidas: list[Medida] = []
    for indice, (grupo, cenarios) in enumerate(grupos(experimento).items()):
        if OS_DOIS_ESTILOS not in cenarios[0].requisitos:
            continue
        fracoes = [
            f for linha in _validas_do_grupo(linhas, cenarios) if (f := fracao_de_sistemas_cheios(linha)) is not None
        ]
        if not fracoes:
            continue
        amostra = np.array(fracoes, dtype=np.float64)
        zona = (float(criterio["minimo"]), float(criterio["maximo"]))
        intervalo = intervalo_por_bootstrap(
            amostra, "media", rng_da_analise(experimento.semente_mestre, 40_000 + indice)
        )
        medidas.append(
            Medida(
                requisito=OS_DOIS_ESTILOS,
                cenario=grupo,
                o_que="fração de jogadores com o sistema cheio ao fim do 1º Planejamento",
                valor=float(amostra.mean()),
                intervalo=intervalo,
                zona=zona,
                veredito=veredito(intervalo, zona),
                partidas=int(amostra.size),
            )
        )
    return medidas


def desequilibrio(
    linhas: list[dict[str, Any]], experimento: Experimento, requisitos: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """MET-01: fração de partidas em que o vencedor tem pelo menos ``fator`` vezes a média dos demais.

    Sem veredito: a métrica é comparada com as 4 de 6 do artigo só como checagem de plausibilidade.
    """
    criterio = criterio_confirmado(requisitos, DESEQUILIBRIO)
    if criterio is None:
        return []
    fatores = [float(criterio["fator"]), *(float(f) for f in criterio.get("sensibilidade", []))]
    resultado: list[dict[str, Any]] = []
    for grupo, cenarios in grupos(experimento).items():
        if cenarios[0].matriz is not None:  # as células das matrizes de estilos têm a sua própria seção
            continue
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


def _unidades_de_descricao(experimento: Experimento) -> dict[str, list[Cenario]]:
    """Cada cenário vira uma linha da descrição; as rotações de uma célula de matriz são somadas numa só."""
    unidades: dict[str, list[Cenario]] = {}
    for cenario in experimento.cenarios_expandidos():
        chave = (cenario.grupo or cenario.nome) if cenario.matriz is not None else cenario.nome
        unidades.setdefault(chave, []).append(cenario)
    return unidades


def _blefes_descritos(validas: list[dict[str, Any]]) -> dict[str, float | None]:
    """Blefes por partida e a fração bem-sucedida (REQ-05). Só a v2 conta blefes."""
    if validas[0]["familia"] != "v2" or any(linha.get("blefes") is None for linha in validas):
        return {"blefes_por_partida": None, "blefes_bem_sucedidos": None}
    tentados = sum(linha["blefes"] for linha in validas)
    sucessos = sum(linha["blefes_bem_sucedidos"] for linha in validas)
    return {
        "blefes_por_partida": tentados / len(validas),
        "blefes_bem_sucedidos": sucessos / tentados if tentados else None,
    }


def descrever(linhas: list[dict[str, Any]], experimento: Experimento) -> list[dict[str, Any]]:
    """Números descritivos por cenário. Não têm critério de aceite."""
    descricoes: list[dict[str, Any]] = []
    for nome, cenarios in _unidades_de_descricao(experimento).items():
        nomes = {cenario.nome for cenario in cenarios}
        do_cenario = [linha for linha in linhas if linha["cenario"] in nomes]
        validas = [linha for linha in do_cenario if linha["erro"] is None]
        cenario = cenarios[0]
        if not validas:
            descricoes.append({"cenario": nome, "partidas": len(do_cenario), "falhas": len(do_cenario)})
            continue
        cheios = [f for linha in validas if (f := fracao_de_sistemas_cheios(linha)) is not None]
        p10 = p50 = p90 = None
        if all(linha["duracao_s"] is not None for linha in validas):
            minutos = np.array([linha["duracao_s"] / 60 for linha in validas])
            p10, p50, p90 = (float(x) for x in np.quantile(minutos, [0.1, 0.5, 0.9]))
        descricoes.append(
            {
                "cenario": nome,
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
                "sistemas_cheios_no_planejamento_1": float(np.mean(cheios)) if cheios else None,
                **_blefes_descritos(validas),
            }
        )
    return descricoes


def vitorias_por_bot(linhas: list[dict[str, Any]], experimento: Experimento) -> list[dict[str, Any]]:
    """MET-07: taxa de vitória de cada bot nos grupos de cenários com bots diferentes.

    Para cada assento ocupado por um bot conta 1 se ele venceu sozinho, 1/k numa
    vitória dividida por k (AMB-14) e 0 se perdeu; a taxa é a média disso. A
    referência de quem não leva vantagem nenhuma é 1/N. As rotações de um rodízio
    são somadas no mesmo grupo. Sem veredito. As células das matrizes de estilos
    ficam de fora: elas têm uma seção própria no relatório.
    """
    grupos: dict[str, list[Cenario]] = {}
    for cenario in experimento.cenarios_expandidos():
        if (not cenario.bots_identicos() or cenario.pesos is not None) and cenario.matriz is None:
            grupos.setdefault(cenario.grupo or cenario.nome, []).append(cenario)
    resultado: list[dict[str, Any]] = []
    for indice, (grupo, cenarios) in enumerate(grupos.items()):
        fatias: dict[str, list[float]] = {}
        for cenario in cenarios:
            fixos = [bot.nome() for bot in cenario.bots_por_assento()] if cenario.pesos is None else []
            for linha in linhas:
                if linha["cenario"] != cenario.nome or linha["erro"] is not None:
                    continue
                nomes = linha["bots_da_mesa"] if cenario.pesos is not None else fixos
                vencedores = linha["vencedores"]
                for assento, nome in enumerate(nomes):
                    fatias.setdefault(nome, []).append(1 / len(vencedores) if assento in vencedores else 0.0)
        jogadores = cenarios[0].jogadores
        for ordem, (nome, valores) in enumerate(sorted(fatias.items())):
            amostra = np.array(valores, dtype=np.float64)
            intervalo = intervalo_por_bootstrap(
                amostra,
                "media",
                rng_da_analise(experimento.semente_mestre, len(experimento.cenarios_expandidos()) + indice, ordem),
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

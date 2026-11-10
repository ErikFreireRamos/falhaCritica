"""Propriedades que todo estado de partida da família v2 precisa respeitar.

São conferidas a cada evento nos testes e nas partidas auditadas. Uma violação
é sempre defeito do motor, nunca jogada ruim de um bot.
"""

from __future__ import annotations

from critical_failure.nucleo.catalogo import Catalogo
from critical_failure.nucleo.erros import ViolacaoDeInvariante
from critical_failure.regras.config import RegrasV2
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.estado import Estado


def violacoes(estado: Estado, regras: RegrasV2, catalogo: Catalogo, em_repouso: bool = True) -> list[str]:
    """Lista as violações encontradas. Vazia quando o estado está íntegro.

    ``em_repouso`` indica que o estado é o resultado final de um ``aplicar``, e
    não um estado intermediário gravado junto de um evento. Só em repouso se
    exige que haja uma decisão pendente. Durante a preparação, antes de o
    baralho existir, nada é conferido.
    """
    achadas: list[str] = []
    if estado.fase == E.PREPARACAO:
        return achadas
    teto = regras.sistema.teto.valor
    minimo = regras.fichas.minimo.valor

    # Conservação das cartas: cada carta do catálogo está em exatamente um lugar.
    lugares: list[int] = [*estado.baralho, *estado.descarte, *estado.backlog]
    for jogador in estado.jogadores:
        lugares += [*jogador.mao, *jogador.sistema]
    if estado.disputa is not None:
        lugares.append(estado.disputa.carta)
    if sorted(lugares) != list(range(len(catalogo.cartas))):
        achadas.append(f"cartas não se conservam: {len(lugares)} em jogo, {len(catalogo.cartas)} no catálogo")

    if len(estado.backlog) > regras.backlog.tamanho.valor:
        achadas.append(f"Backlog com {len(estado.backlog)} cartas")

    for assento, jogador in enumerate(estado.jogadores):
        if len(jogador.sistema) > teto:
            achadas.append(f"assento {assento}: sistema com {len(jogador.sistema)} cartas (teto {teto})")
        if jogador.fichas < minimo:
            achadas.append(f"assento {assento}: {jogador.fichas} fichas (mínimo {minimo})")
        if len(set(jogador.alertas)) != len(jogador.alertas):
            achadas.append(f"assento {assento}: mais de um Alerta na mesma categoria")
        if not set(jogador.alertas) <= set(catalogo.categorias):
            achadas.append(f"assento {assento}: Alerta em categoria fora do jogo")
        if not set(jogador.reveladas) <= set(jogador.sistema):
            achadas.append(f"assento {assento}: carta revelada que não está no sistema")
        if not set(jogador.pegas_do_backlog) <= set(jogador.mao) | set(jogador.sistema):
            achadas.append(f"assento {assento}: carta pega do Backlog que o jogador não tem mais")
        if jogador.acertos > estado.ciclo:
            achadas.append(f"assento {assento}: mais acertos do que incidentes já diagnosticados")

    if not 0 <= estado.primeiro < estado.n or not 0 <= estado.auditor < estado.n:
        achadas.append("marcadores fora da mesa")
    elif (estado.primeiro - 1) % estado.n != estado.auditor:
        achadas.append("o Auditor não é o último da ordem de jogo (R-4.9a)")

    if estado.fase == E.FIM:
        if estado.pendente is not None or not estado.vencedores:
            achadas.append("partida encerrada com decisão pendente ou sem vencedor")
    elif em_repouso and estado.pendente is None:
        achadas.append(f"partida em andamento ({estado.fase}) sem decisão pendente")
    if estado.disputa is not None and estado.fase != E.HOMOLOGACAO:
        achadas.append("disputa aberta fora da Homologação")
    return achadas


def conferir(estado: Estado, regras: RegrasV2, catalogo: Catalogo, em_repouso: bool = True) -> None:
    achadas = violacoes(estado, regras, catalogo, em_repouso)
    if achadas:
        raise ViolacaoDeInvariante("; ".join(achadas))

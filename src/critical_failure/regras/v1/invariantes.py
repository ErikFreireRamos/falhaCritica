"""Propriedades que todo estado de partida da v1 precisa respeitar."""

from __future__ import annotations

from critical_failure.nucleo.erros import ViolacaoDeInvariante
from critical_failure.regras.v1 import estado as E
from critical_failure.regras.v1.config import CatalogoV1, RegrasV1
from critical_failure.regras.v1.estado import EstadoV1


def violacoes(estado: EstadoV1, regras: RegrasV1, catalogo: CatalogoV1, em_repouso: bool = True) -> list[str]:
    achadas: list[str] = []
    if estado.fase == E.PREPARACAO and not estado.baralho:
        return achadas
    lugares: list[int] = [*estado.baralho, *estado.descarte]
    for jogador in estado.jogadores:
        lugares += [*jogador.mao, *jogador.sistema]
    if estado.disputa is not None and not estado.disputa.carta_entregue:
        lugares.append(estado.disputa.carta)
    if sorted(lugares) != list(range(len(catalogo.cartas))):
        achadas.append(f"cartas não se conservam: {len(lugares)} em jogo, {len(catalogo.cartas)} no baralho")
    especiais = {i for i, nome in enumerate(catalogo.cartas) if nome in catalogo.especiais}
    for assento, jogador in enumerate(estado.jogadores):
        if especiais & set(jogador.sistema):
            achadas.append(f"assento {assento}: carta Critical Failure no sistema (V1-4.2.2)")
        if len(jogador.mao) > regras.mao_inicial.valor:
            achadas.append(f"assento {assento}: mão com {len(jogador.mao)} cartas")
        if jogador.testes_feitos > regras.cartas_de_teste.valor:
            achadas.append(f"assento {assento}: {jogador.testes_feitos} testes, mais que as cartas de teste")
        if not set(jogador.reveladas) <= set(jogador.sistema):
            achadas.append(f"assento {assento}: carta revelada que não está no sistema")
        if (
            estado.fase == E.TESTES
            and len(jogador.mao)
            + jogador.testes_feitos
            + (1 if estado.disputa is not None and estado.disputa.atacante == assento else 0)
            != regras.cartas_de_teste.valor
        ):
            achadas.append(f"assento {assento}: cartas de teste na mão e testes feitos não somam o esperado")
    if estado.fase == E.FIM:
        if estado.pendente is not None or not estado.vencedores:
            achadas.append("partida encerrada com decisão pendente ou sem vencedor")
    elif em_repouso and estado.pendente is None:
        achadas.append(f"partida em andamento ({estado.fase}) sem decisão pendente")
    if estado.disputa is not None and estado.fase != E.TESTES:
        achadas.append("disputa aberta fora da fase de testes")
    return achadas


def conferir(estado: EstadoV1, regras: RegrasV1, catalogo: CatalogoV1, em_repouso: bool = True) -> None:
    achadas = violacoes(estado, regras, catalogo, em_repouso)
    if achadas:
        raise ViolacaoDeInvariante("; ".join(achadas))

"""Motor de regras da família v2.

``aplicar(estado, acao)`` devolve o novo estado e os eventos produzidos. O motor
valida a ação, resolve sozinho tudo o que não é decisão de jogador (compras
impossíveis, passagens automáticas, Produção, Critical Failure, pontuação) e
para no próximo ponto em que alguém precisa decidir.

Cada evento cita a regra da especificação que o justificou. Nenhum número de
regra aparece aqui: todos vêm do YAML, por ``RegrasV2``.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import replace
from typing import Any

from critical_failure.nucleo.catalogo import Catalogo, Incidente
from critical_failure.nucleo.erros import AcaoIlegal, ConfiguracaoInvalida
from critical_failure.nucleo.rng import FLUXO_JOGO, gerador
from critical_failure.observacao import Observacao, observar
from critical_failure.regras.config import RegrasV2
from critical_failure.regras.v2 import acoes as A
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2 import invariantes
from critical_failure.regras.v2.acoes import Acao, acao_de_dict
from critical_failure.regras.v2.estado import (
    Disputa,
    DisputaEncerrada,
    Estado,
    Evento,
    Jogador,
    Pendente,
)

Passo = tuple[Estado, list[Evento]]

# De onde vieram as fichas, para o detalhamento do placar final.
FONTE_HOMOLOGACAO = "homologacao"
FONTE_DIAGNOSTICO = "diagnostico"
FONTE_DANO = "dano"
FONTE_CRITICAL_FAILURE = "critical_failure"
FONTE_FINAL = "pontuacao_final"
FONTES = (FONTE_HOMOLOGACAO, FONTE_DIAGNOSTICO, FONTE_DANO, FONTE_CRITICAL_FAILURE, FONTE_FINAL)


def _distintos(itens: Iterable[str]) -> list[str]:
    """Itens sem repetição, na ordem em que aparecem."""
    return list(dict.fromkeys(itens))


def _sem(tupla: tuple[Any, ...], item: Any) -> tuple[Any, ...]:
    """A tupla sem a primeira ocorrência de ``item``."""
    if item not in tupla:
        return tupla
    posicao = tupla.index(item)
    return tupla[:posicao] + tupla[posicao + 1 :]


class _Ctx:
    """Estado e eventos em construção durante um ``aplicar``."""

    __slots__ = ("e", "eventos")

    def __init__(self, estado: Estado) -> None:
        self.e = estado
        self.eventos: list[Evento] = []


class MotorV2:
    familia = "v2"
    fontes = FONTES

    def __init__(self, regras: RegrasV2, catalogo: Catalogo) -> None:
        self.regras = regras
        self.catalogo = catalogo
        r = regras
        self.jogadores_minimo = r.jogadores.minimo.valor
        self.jogadores_maximo = r.jogadores.maximo.valor
        self.ciclos = r.ciclos.valor
        self.fichas_iniciais = r.fichas.iniciais.valor
        self.fichas_minimo = r.fichas.minimo.valor
        self.incidentes_na_linha = r.linha_do_tempo.incidentes.valor
        self.cartas_iniciais = r.sistema.cartas_iniciais.valor
        self.teto = r.sistema.teto.valor
        self.tamanho_do_backlog = r.backlog.tamanho.valor
        self.compras = r.planejamento.compras.valor
        self.limpeza_no_planejamento = r.alertas.limpeza_no_planejamento.valor
        self.falhou_atacante_ganha = r.disputa.falhou.atacante_ganha.valor
        self.verdade_atacante_paga = r.disputa.contestacao_verdade.atacante_paga.valor
        self.blefe_defensor_paga = r.disputa.contestacao_blefe.defensor_paga.valor
        self.blefe_atacante_ganha = r.disputa.contestacao_blefe.atacante_ganha_do_banco.valor
        self.acerto = r.diagnostico.acerto.valor
        self.licao_cartas = r.licao_aprendida.cartas.valor
        self.dano_sem_cobertura = r.dano.incidente.sem_cobertura.valor
        self.dano_alerta = r.dano.incidente.alerta.valor
        self.dano_severo = r.dano.incidente.severo_sem_teste_chave.valor
        self.cf_sempre = r.dano.critical_failure.sempre.valor
        self.cf_sem_profunda = r.dano.critical_failure.sem_cobertura_profunda.valor
        self.cf_sem_cobertura = r.dano.critical_failure.sem_cobertura.valor
        self.cf_alerta = r.dano.critical_failure.alerta.valor
        self.final_categoria = r.final.categoria_distinta.valor
        self.final_profunda = r.final.cobertura_profunda.valor
        self.final_alerta = r.final.alerta_ativo.valor
        self.testes_distintos = r.cobertura_profunda.testes_distintos.valor
        self.faces = r.dado.faces.valor
        i = r.interpretacoes
        self.dano_primeiro = i.producao_ordem.valor == "dano_primeiro"
        self.passou_pode_ser_alvo = i.quem_passou_pode_ser_alvo.valor
        self.cf_limpa_alertas = i.critical_failure_limpa_alertas.valor
        self.final_por_saldo = i.final_ordem.valor == "saldo"

    # ------------------------------------------------------------------ utilidades

    def _ev(
        self,
        c: _Ctx,
        tipo: str,
        regra: str,
        ator: int | None = None,
        publico: dict[str, Any] | None = None,
        oculto: dict[str, Any] | None = None,
        visivel: dict[str, list[int]] | None = None,
        amb: str | None = None,
    ) -> None:
        """Registra um evento com o estado atual. Chamar depois de mudar o estado."""
        c.eventos.append(
            Evento(tipo, regra, c.e.ciclo, c.e.fase, ator, publico or {}, oculto or {}, visivel or {}, amb, c.e)
        )

    def _jog(self, c: _Ctx, j: int, **mudancas: Any) -> None:
        jogadores = list(c.e.jogadores)
        jogadores[j] = replace(jogadores[j], **mudancas)
        c.e = replace(c.e, jogadores=tuple(jogadores))

    def _esquerda(self, e: Estado, j: int) -> int:
        return (j + 1) % e.n

    def ordem_de_jogo(self, e: Estado) -> list[int]:
        """Assentos a partir do primeiro jogador, em sentido horário (R-4.3)."""
        return [(e.primeiro + k) % e.n for k in range(e.n)]

    def incidente_atual(self, e: Estado) -> Incidente:
        if e.agora is None:
            raise AcaoIlegal("não há incidente na vaga Agora")
        return self.catalogo.incidentes[e.agora]

    def _carta_por_teste(self, cartas: tuple[int, ...], teste: str | None) -> int:
        for carta in cartas:
            if self.catalogo.teste(carta) == teste:
                return carta
        raise AcaoIlegal(f"não há carta do teste {teste!r} disponível")

    def _permutar(self, c: _Ctx, itens: list[Any]) -> list[Any]:
        """Embaralha com o fluxo de aleatoriedade do jogo e avança o contador."""
        e = c.e
        ordem = gerador(e.semente, e.partida, FLUXO_JOGO, e.contador_rng).permutation(len(itens))
        c.e = replace(e, contador_rng=e.contador_rng + 1)
        return [itens[int(posicao)] for posicao in ordem]

    # ------------------------------------------------------------------ fichas (seção 5)

    def _ganhar(self, c: _Ctx, j: int, quantidade: int) -> int:
        self._jog(c, j, fichas=c.e.jogadores[j].fichas + quantidade)
        return quantidade

    def _perder(self, c: _Ctx, j: int, quantidade: int) -> int:
        """Devolve fichas ao banco, respeitando o mínimo (R-5.2). Retorna o que foi pago."""
        atual = c.e.jogadores[j].fichas
        pago = max(min(quantidade, atual - self.fichas_minimo), 0)
        self._jog(c, j, fichas=atual - pago)
        return pago

    def _pagar(self, c: _Ctx, de: int, para: int, quantidade: int) -> tuple[int, int]:
        """Pagamento entre jogadores. Quem recebe nunca perde: o banco completa (R-5.2a)."""
        pago = self._perder(c, de, quantidade)
        recebido = self._ganhar(c, para, quantidade)
        return pago, recebido

    def _dar_alerta(self, c: _Ctx, j: int, categoria: str) -> None:
        atuais = set(c.e.jogadores[j].alertas) | {categoria}
        self._jog(c, j, alertas=tuple(x for x in self.catalogo.categorias if x in atuais))

    # ------------------------------------------------------------------ preparação (seção 3)

    def preparar(self, n_jogadores: int, semente: int, partida: int) -> Passo:
        if not self.jogadores_minimo <= n_jogadores <= self.jogadores_maximo:
            raise ConfiguracaoInvalida(
                f"número de jogadores {n_jogadores} fora do intervalo "
                f"{self.jogadores_minimo} a {self.jogadores_maximo} (R-1.2)"
            )
        cat = self.catalogo
        vazio = Jogador(
            fichas=self.fichas_iniciais,
            mao=(),
            sistema=(),
            alertas=(),
            reveladas=(),
            pegas_do_backlog=(),
            passou=False,
            acertos=0,
        )
        primeiro = 0  # AMB-08: o assento 0 sempre começa
        c = _Ctx(
            Estado(
                semente=semente,
                partida=partida,
                contador_rng=0,
                jogadores=(vazio,) * n_jogadores,
                baralho=(),
                descarte=(),
                backlog=(),
                linha_do_tempo=(),
                agora=None,
                proximo=None,
                resolvidos=(),
                ciclo=0,
                fase=E.PREPARACAO,
                primeiro=primeiro,
                auditor=(primeiro - 1) % n_jogadores,
                pendente=None,
                compras_restantes=0,
                disputa=None,
                diagnosticos=(),
                fila_da_licao=(),
                historico=(),
                vencedores=(),
            )
        )
        self._ev(c, "fichas_iniciais", "R-3.1", publico={"fichas_por_jogador": self.fichas_iniciais})

        separados = self._permutar(c, sorted(cat.incidentes))[: self.incidentes_na_linha]
        agora, *resto = separados
        c.e = replace(c.e, agora=agora, proximo=resto[0] if resto else None, linha_do_tempo=tuple(resto[1:]))
        self._ev(c, "linha_do_tempo", "R-3.2", oculto={"incidentes": separados})
        self._ev(c, "radar", "R-3.3", publico={"agora": c.e.agora, "proximo": c.e.proximo})

        ordem = self._permutar(c, list(range(len(cat.cartas))))
        c.e = replace(c.e, baralho=tuple(ordem))
        self._ev(c, "baralho_embaralhado", "R-3.4", publico={"cartas": len(ordem)}, oculto={"ordem": ordem})
        for j in range(n_jogadores):
            iniciais = c.e.baralho[: self.cartas_iniciais]
            c.e = replace(c.e, baralho=c.e.baralho[self.cartas_iniciais :])
            self._jog(c, j, sistema=iniciais)
            self._trocar_repetidas(c, j)
            sistema = cat.nomes(c.e.jogadores[j].sistema)
            self._ev(
                c,
                "sistema_inicial",
                "R-3.4",
                ator=j,
                publico={"cartas": len(sistema)},
                oculto={"sistema": sistema},
                visivel={"sistema": [j]},
            )

        c.e = replace(
            c.e, backlog=c.e.baralho[: self.tamanho_do_backlog], baralho=c.e.baralho[self.tamanho_do_backlog :]
        )
        self._ev(c, "backlog_inicial", "R-3.5", publico={"cartas": cat.nomes(c.e.backlog)})
        self._ev(c, "marcadores", "R-3.6a", publico={"primeiro": c.e.primeiro, "auditor": c.e.auditor}, amb="AMB-08")
        c.e = replace(c.e, ciclo=1)
        self._iniciar_planejamento(c)
        return self._fechar(c)

    def _fechar(self, c: _Ctx) -> Passo:
        """Fecha um passo: o último evento passa a carregar o estado final.

        Depois do último evento o motor ainda pode ter feito alguma arrumação sem
        evento próprio, como dar a vez ao próximo jogador. Assim o último
        ``estado_hash`` do passo é sempre o do estado em repouso.
        """
        if not c.eventos:
            raise AcaoIlegal("a ação não produziu nenhum evento")
        c.eventos[-1] = replace(c.eventos[-1], estado=c.e)
        return c.e, c.eventos

    def _trocar_repetidas(self, c: _Ctx, j: int) -> None:
        """R-3.4b e AMB-07: carta repetida vai para o fundo; repete enquanto repetir."""
        cat = self.catalogo
        while c.e.baralho:
            sistema = c.e.jogadores[j].sistema
            vistos: set[str] = set()
            repetida: int | None = None
            for carta in sistema:
                if cat.teste(carta) in vistos:
                    repetida = carta
                    break
                vistos.add(cat.teste(carta))
            if repetida is None:
                return
            nova = c.e.baralho[0]
            c.e = replace(c.e, baralho=c.e.baralho[1:] + (repetida,))
            self._jog(c, j, sistema=tuple(nova if carta == repetida else carta for carta in sistema))
            self._ev(
                c,
                "carta_trocada",
                "R-3.4b",
                ator=j,
                publico={"trocas": 1},
                oculto={"saiu": cat.teste(repetida), "entrou": cat.teste(nova)},
                visivel={"saiu": [j], "entrou": [j]},
                amb="AMB-07",
            )

    # ------------------------------------------------------------------ consulta

    def acoes_legais(self, e: Estado) -> tuple[Acao, ...]:
        """Ações que o jogador da vez pode escolher. Vazio quando a partida acabou."""
        p = e.pendente
        if p is None:
            return ()
        cat = self.catalogo
        j = p.jogador
        if p.tipo == E.COMPRAR:
            opcoes = [Acao(A.COMPRAR, teste=t, origem=A.ORIGEM_BACKLOG) for t in _distintos(cat.nomes(e.backlog))]
            if e.baralho or e.descarte:
                opcoes.append(Acao(A.COMPRAR, origem=A.ORIGEM_TOPO))
            return tuple(opcoes)
        if p.tipo == E.COLOCAR:
            mao = _distintos(cat.nomes(e.jogadores[j].mao))
            return (*(Acao(A.COLOCAR, teste=t) for t in mao), Acao(A.ENCERRAR))
        if p.tipo == E.AGIR:
            return (*self._testes_legais(e, j), Acao(A.PASSAR))
        if p.tipo == E.RESPONDER:
            assert e.disputa is not None
            testes = cat.testes_da_categoria(e.disputa.categoria)
            return (Acao(A.ADMITIR), *(Acao(A.DEFENDER, teste=t) for t in testes))
        if p.tipo == E.CONFERIR:
            return (Acao(A.CONFERE), Acao(A.NAO_CONFERE))
        if p.tipo == E.CONTESTAR:
            return (Acao(A.ACEITAR), Acao(A.CONTESTAR))
        if p.tipo == E.DIAGNOSTICAR:
            return tuple(Acao(A.DIAGNOSTICAR, categoria=categoria) for categoria in cat.categorias)
        if p.tipo == E.LICAO:
            x = self.incidente_atual(e).chave
            da_categoria = _distintos(cat.teste(carta) for carta in e.backlog if cat.categoria(carta) == x)
            return (*(Acao(A.PEGAR, teste=t) for t in da_categoria), Acao(A.RECUSAR))
        raise AcaoIlegal(f"decisão pendente desconhecida: {p.tipo}")

    def _testes_legais(self, e: Estado, j: int) -> list[Acao]:
        cat = self.catalogo
        opcoes: list[Acao] = []
        for teste in _distintos(cat.nomes(e.jogadores[j].mao)):
            categoria = cat.testes[teste].categoria
            for alvo in range(e.n):
                outro = e.jogadores[alvo]
                if alvo == j:
                    continue
                if categoria in outro.alertas:  # R-7.4.2: bug duplicado
                    continue
                if outro.passou and not self.passou_pode_ser_alvo:  # AMB-04
                    continue
                opcoes.append(Acao(A.TESTAR, teste=teste, alvo=alvo))
        return opcoes

    def _auditor_da_disputa(self, e: Estado, atacante: int, defensor: int) -> int:
        """R-7.1.4 e AMB-05: o não envolvido mais próximo à esquerda do Auditor."""
        candidato = e.auditor
        for _ in range(e.n):
            if candidato not in (atacante, defensor):
                return candidato
            candidato = self._esquerda(e, candidato)
        raise AcaoIlegal("não há jogador livre para ser Auditor da disputa")

    # ------------------------------------------------------------------ aplicar

    def aplicar(self, estado: Estado, acao: Acao) -> Passo:
        p = estado.pendente
        if p is None:
            raise AcaoIlegal("a partida já terminou")
        if not isinstance(acao, Acao):
            raise AcaoIlegal(f"não é uma ação: {acao!r}")
        c = _Ctx(estado)
        if p.tipo == E.RESPONDER and acao.tipo == A.DEFENDER:
            # Aceita também teste de outra categoria, que conta como "Falhou" (R-7.2.2c).
            self._defender(c, p.jogador, acao)
        else:
            if acao not in self.acoes_legais(estado):
                raise AcaoIlegal(f"ação ilegal para a decisão '{p.tipo}': {acao.texto()}")
            self._MANIPULADORES[acao.tipo](self, c, p.jogador, acao)
        return self._fechar(c)

    # ------------------------------------------------------------------ Planejamento (seção 6)

    def _iniciar_planejamento(self, c: _Ctx) -> None:
        c.e = replace(
            c.e,
            fase=E.PLANEJAMENTO,
            compras_restantes=self.compras,
            jogadores=tuple(replace(jogador, passou=False) for jogador in c.e.jogadores),
        )
        self._ev(c, "inicio_da_fase", "R-4.1", publico={"fase": E.PLANEJAMENTO})
        if self.limpeza_no_planejamento:
            removidos = {str(j): list(jog.alertas) for j, jog in enumerate(c.e.jogadores) if jog.alertas}
            if removidos:
                c.e = replace(c.e, jogadores=tuple(replace(jogador, alertas=()) for jogador in c.e.jogadores))
                self._ev(c, "alertas_zerados", "R-6.9", publico={"removidos": removidos})
        self._pedir_compra(c, c.e.primeiro)

    def _pedir_compra(self, c: _Ctx, j: int) -> None:
        e = c.e
        if e.compras_restantes > 0:
            if e.backlog or e.baralho or e.descarte:
                c.e = replace(e, pendente=Pendente(E.COMPRAR, j))
                return
            c.e = replace(e, compras_restantes=0)
            self._ev(
                c,
                "compra_impossivel",
                "R-6.1",
                ator=j,
                publico={"compras_perdidas": e.compras_restantes},
                amb="AMB-06",
            )
        self._pedir_colocacao(c, j)

    def _pedir_colocacao(self, c: _Ctx, j: int) -> None:
        jogador = c.e.jogadores[j]
        if jogador.mao and len(jogador.sistema) < self.teto:
            c.e = replace(c.e, pendente=Pendente(E.COLOCAR, j))
            return
        self._fim_do_turno(c, j)

    def _fim_do_turno(self, c: _Ctx, j: int) -> None:
        jogador = c.e.jogadores[j]
        self._ev(
            c,
            "fim_do_turno",
            "R-6.4",
            ator=j,
            publico={"cartas_na_mao": len(jogador.mao), "cartas_no_sistema": len(jogador.sistema)},
        )
        proximo = self._esquerda(c.e, j)
        if proximo == c.e.primeiro:  # R-4.5: todos fizeram a sua vez
            self._iniciar_homologacao(c)
            return
        c.e = replace(c.e, compras_restantes=self.compras)
        self._pedir_compra(c, proximo)

    def _tirar_do_topo(self, c: _Ctx) -> int | None:
        """Tira a carta do topo. Reembaralha o descarte se preciso (R-6.6)."""
        if not c.e.baralho:
            if not c.e.descarte:
                return None
            ordem = self._permutar(c, list(c.e.descarte))
            c.e = replace(c.e, baralho=tuple(ordem), descarte=())
            self._ev(
                c,
                "reembaralhamento",
                "R-6.6",
                publico={"cartas": len(ordem)},
                oculto={"ordem": self.catalogo.nomes(ordem)},
            )
        carta = c.e.baralho[0]
        c.e = replace(c.e, baralho=c.e.baralho[1:])
        return carta

    def _repor_backlog(self, c: _Ctx, posicao: int, regra: str) -> None:
        carta = self._tirar_do_topo(c)
        if carta is None:
            self._ev(c, "reposicao_impossivel", regra, publico={"backlog": len(c.e.backlog)}, amb="AMB-06")
            return
        c.e = replace(c.e, backlog=c.e.backlog[:posicao] + (carta,) + c.e.backlog[posicao:])
        self._ev(c, "backlog_reposto", regra, publico={"carta": self.catalogo.teste(carta)})

    def _comprar(self, c: _Ctx, j: int, acao: Acao) -> None:
        cat = self.catalogo
        jogador = c.e.jogadores[j]
        restantes = c.e.compras_restantes - 1
        if acao.origem == A.ORIGEM_BACKLOG:
            carta = self._carta_por_teste(c.e.backlog, acao.teste)
            posicao = c.e.backlog.index(carta)
            c.e = replace(c.e, backlog=_sem(c.e.backlog, carta), compras_restantes=restantes)
            self._jog(c, j, mao=jogador.mao + (carta,), pegas_do_backlog=jogador.pegas_do_backlog + (carta,))
            self._ev(c, "compra", "R-6.1c", ator=j, publico={"origem": A.ORIGEM_BACKLOG, "carta": cat.teste(carta)})
            self._repor_backlog(c, posicao, "R-6.1b")
        else:
            carta_do_topo = self._tirar_do_topo(c)
            assert carta_do_topo is not None
            c.e = replace(c.e, compras_restantes=restantes)
            self._jog(c, j, mao=jogador.mao + (carta_do_topo,))
            self._ev(
                c,
                "compra",
                "R-6.1a",
                ator=j,
                publico={"origem": A.ORIGEM_TOPO},
                oculto={"carta": cat.teste(carta_do_topo)},
                visivel={"carta": [j]},
            )
        self._pedir_compra(c, j)

    def _colocar(self, c: _Ctx, j: int, acao: Acao) -> None:
        cat = self.catalogo
        jogador = c.e.jogadores[j]
        carta = self._carta_por_teste(jogador.mao, acao.teste)
        self._jog(c, j, mao=_sem(jogador.mao, carta), sistema=jogador.sistema + (carta,))
        self._ev(
            c,
            "colocacao",
            "R-6.2",
            ator=j,
            publico={"cartas_no_sistema": len(jogador.sistema) + 1},
            oculto={"carta": cat.teste(carta)},
            visivel={"carta": [j]},
        )
        categoria = cat.categoria(carta)
        if not self.limpeza_no_planejamento and categoria in jogador.alertas:
            # Regra impressa na v2.2 e revogada pela COR-02: a carta corrige o Alerta.
            self._jog(c, j, alertas=_sem(jogador.alertas, categoria))
            self._ev(c, "alerta_corrigido", "R-6.2b", ator=j, publico={"categoria": categoria})
        self._pedir_colocacao(c, j)

    def _encerrar_turno(self, c: _Ctx, j: int, acao: Acao) -> None:
        self._fim_do_turno(c, j)

    # ------------------------------------------------------------------ Homologação (seção 7)

    def _iniciar_homologacao(self, c: _Ctx) -> None:
        c.e = replace(c.e, fase=E.HOMOLOGACAO, compras_restantes=0)
        self._ev(c, "inicio_da_fase", "R-4.1", publico={"fase": E.HOMOLOGACAO})
        self._pedir_acao(c, c.e.primeiro)

    def _pedir_acao(self, c: _Ctx, inicio: int) -> None:
        """Dá a vez ao próximo que ainda não passou; quem não pode testar passa (AMB-03)."""
        j = inicio
        for _ in range(c.e.n):
            if not c.e.jogadores[j].passou:
                if self._testes_legais(c.e, j):
                    c.e = replace(c.e, pendente=Pendente(E.AGIR, j))
                    return
                self._jog(c, j, passou=True)
                self._ev(c, "passou", "R-7.0.3", ator=j, publico={"automatico": True}, amb="AMB-03")
            j = self._esquerda(c.e, j)
        self._iniciar_producao(c)  # R-4.6: todos passaram

    def _testar(self, c: _Ctx, j: int, acao: Acao) -> None:
        cat = self.catalogo
        jogador = c.e.jogadores[j]
        assert acao.alvo is not None
        carta = self._carta_por_teste(jogador.mao, acao.teste)
        categoria = cat.categoria(carta)
        auditor = self._auditor_da_disputa(c.e, j, acao.alvo)
        self._jog(c, j, mao=_sem(jogador.mao, carta), pegas_do_backlog=_sem(jogador.pegas_do_backlog, carta))
        c.e = replace(
            c.e,
            disputa=Disputa(j, acao.alvo, auditor, carta, categoria, E.RESPONDER),
            pendente=Pendente(E.RESPONDER, acao.alvo),
        )
        self._ev(
            c,
            "teste",
            "R-7.2.1",
            ator=j,
            publico={
                "atacante": j,
                "defensor": acao.alvo,
                "teste": cat.teste(carta),
                "categoria": categoria,
                "auditor_titular": c.e.auditor,
                "auditor_da_disputa": auditor,
            },
            amb="AMB-05" if auditor != c.e.auditor else None,
        )

    def _passar(self, c: _Ctx, j: int, acao: Acao) -> None:
        self._jog(c, j, passou=True)
        self._ev(c, "passou", "R-7.0.3", ator=j, publico={"automatico": False})
        self._pedir_acao(c, self._esquerda(c.e, j))

    def _admitir(self, c: _Ctx, j: int, acao: Acao) -> None:
        self._ev(c, "defesa", "R-7.2.2", ator=j, publico={"resposta": "admitiu"})
        self._falhou(c, "admitiu")

    def _defender(self, c: _Ctx, j: int, acao: Acao) -> None:
        cat = self.catalogo
        d = c.e.disputa
        assert d is not None
        teste = acao.teste
        if teste is None or teste not in cat.testes:
            raise AcaoIlegal(f"teste desconhecido na defesa: {teste!r}")
        if acao.explicacao_correta is None or acao.alvo is not None or acao.categoria or acao.origem:
            raise AcaoIlegal("a defesa precisa do teste nomeado e de dizer se a explicação está correta")
        if cat.testes[teste].categoria != d.categoria:
            c.e = replace(c.e, disputa=replace(d, teste_nomeado=teste))
            self._ev(c, "defesa", "R-7.2.2c", ator=j, publico={"resposta": "defendeu", "teste_nomeado": teste})
            self._falhou(c, "outra_categoria")
            return
        tem = any(cat.teste(carta) == teste for carta in c.e.jogadores[j].sistema)
        c.e = replace(
            c.e,
            disputa=replace(d, etapa=E.CONFERIR, teste_nomeado=teste, explicacao_correta=acao.explicacao_correta),
            pendente=Pendente(E.CONFERIR, d.auditor),
        )
        self._ev(
            c,
            "defesa",
            "R-7.2.2a",
            ator=j,
            publico={"resposta": "defendeu", "teste_nomeado": teste},
            oculto={"tem_carta": tem, "blefe": not tem, "explicacao_correta": acao.explicacao_correta},
            visivel={"tem_carta": [j], "blefe": [j], "explicacao_correta": [d.auditor]},
            amb="AMB-15",
        )

    def _conferir(self, c: _Ctx, j: int, acao: Acao) -> None:
        d = c.e.disputa
        assert d is not None
        d = replace(d, veredito=acao.tipo)
        if acao.tipo == A.NAO_CONFERE:
            c.e = replace(c.e, disputa=d)
            self._ev(c, "conferencia", "R-7.2.3", ator=j, publico={"veredito": acao.tipo})
            self._falhou(c, "nao_confere")
            return
        c.e = replace(c.e, disputa=replace(d, etapa=E.CONTESTAR), pendente=Pendente(E.CONTESTAR, d.atacante))
        self._ev(c, "conferencia", "R-7.2.3", ator=j, publico={"veredito": acao.tipo})

    def _aceitar(self, c: _Ctx, j: int, acao: Acao) -> None:
        self._ev(c, "aceite", "R-7.3.2", ator=j)
        self._encerrar_disputa(c, E.ACEITA, contestou=False)

    def _contestar(self, c: _Ctx, j: int, acao: Acao) -> None:
        cat = self.catalogo
        d = c.e.disputa
        assert d is not None
        defensor = c.e.jogadores[d.defensor]
        do_teste = [carta for carta in defensor.sistema if cat.teste(carta) == d.teste_nomeado]
        if do_teste:
            carta = self._escolher_para_revelar(defensor, do_teste)
            if carta not in defensor.reveladas:
                self._jog(c, d.defensor, reveladas=defensor.reveladas + (carta,))
            pago, recebido = self._pagar(c, d.atacante, d.defensor, self.verdade_atacante_paga)
            self._ev(
                c,
                "contestacao",
                "R-7.3.3",
                ator=j,
                publico={
                    "tinha_carta": True,
                    "carta_revelada": cat.teste(carta),
                    "fonte": FONTE_HOMOLOGACAO,
                    "fichas": {str(d.atacante): -pago, str(d.defensor): recebido},
                },
            )
            self._encerrar_disputa(c, E.CONTESTOU_VERDADE, contestou=True)
            return
        pago, recebido = self._pagar(c, d.defensor, d.atacante, self.blefe_defensor_paga)
        bonus = self._ganhar(c, d.atacante, self.blefe_atacante_ganha)
        self._dar_alerta(c, d.defensor, d.categoria)
        self._ev(
            c,
            "contestacao",
            "R-7.3.4",
            ator=j,
            publico={
                "tinha_carta": False,
                "fonte": FONTE_HOMOLOGACAO,
                "fichas": {str(d.atacante): recebido + bonus, str(d.defensor): -pago},
                "alerta": {"jogador": d.defensor, "categoria": d.categoria},
            },
        )
        self._encerrar_disputa(c, E.CONTESTOU_BLEFE, contestou=True)

    def _escolher_para_revelar(self, jogador: Jogador, candidatas: list[int]) -> int:
        """AMB-11: revela o mínimo. Prefere uma carta que a mesa já conhece."""
        for carta in candidatas:
            if carta in jogador.reveladas:
                return carta
        return candidatas[0]

    def _falhou(self, c: _Ctx, motivo: str) -> None:
        """R-7.3.1: o atacante ganha do banco e o defensor recebe Alerta na categoria."""
        d = c.e.disputa
        assert d is not None
        ganho = self._ganhar(c, d.atacante, self.falhou_atacante_ganha)
        self._dar_alerta(c, d.defensor, d.categoria)
        self._ev(
            c,
            "falhou",
            "R-7.3.1",
            ator=d.defensor,
            publico={
                "motivo": motivo,
                "fonte": FONTE_HOMOLOGACAO,
                "fichas": {str(d.atacante): ganho},
                "alerta": {"jogador": d.defensor, "categoria": d.categoria},
            },
        )
        self._encerrar_disputa(c, E.FALHOU, contestou=False)

    def _encerrar_disputa(self, c: _Ctx, resultado: str, contestou: bool) -> None:
        cat = self.catalogo
        d = c.e.disputa
        assert d is not None
        registro = DisputaEncerrada(
            ciclo=c.e.ciclo,
            atacante=d.atacante,
            defensor=d.defensor,
            auditor=d.auditor,
            categoria=d.categoria,
            teste_do_ataque=cat.teste(d.carta),
            teste_nomeado=d.teste_nomeado,
            veredito=d.veredito,
            contestou=contestou,
            resultado=resultado,
        )
        c.e = replace(c.e, descarte=c.e.descarte + (d.carta,), disputa=None, historico=c.e.historico + (registro,))
        self._ev(c, "fim_da_disputa", "R-7.2.1a", publico={"resultado": resultado, "descartada": cat.teste(d.carta)})
        self._pedir_acao(c, self._esquerda(c.e, d.atacante))

    # ------------------------------------------------------------------ Produção (seção 8)

    def _iniciar_producao(self, c: _Ctx) -> None:
        c.e = replace(
            c.e, fase=E.PRODUCAO, diagnosticos=(None,) * c.e.n, pendente=Pendente(E.DIAGNOSTICAR, c.e.primeiro)
        )
        incidente = self.incidente_atual(c.e)
        self._ev(c, "inicio_da_fase", "R-4.1", publico={"fase": E.PRODUCAO})
        self._ev(
            c,
            "relato_lido",
            "R-8.0.1",
            ator=c.e.auditor,
            publico={"incidente": incidente.numero, "nome": incidente.nome},
        )

    def _diagnosticar(self, c: _Ctx, j: int, acao: Acao) -> None:
        escolhas = list(c.e.diagnosticos)
        escolhas[j] = acao.categoria
        faltam = [k for k in self.ordem_de_jogo(c.e) if escolhas[k] is None]
        c.e = replace(
            c.e, diagnosticos=tuple(escolhas), pendente=Pendente(E.DIAGNOSTICAR, faltam[0]) if faltam else None
        )
        self._ev(
            c,
            "diagnostico_escolhido",
            "R-8.0.2",
            ator=j,
            oculto={"categoria": acao.categoria},
            visivel={"categoria": [j]},
        )
        if not faltam:
            self._resolver_producao(c)

    def _resolver_producao(self, c: _Ctx) -> None:
        incidente = self.incidente_atual(c.e)
        ordem = self.ordem_de_jogo(c.e)
        self._ev(c, "diagnosticos_revelados", "R-8.0.2b", publico={"escolhas": list(c.e.diagnosticos)})
        self._ev(
            c,
            "gabarito_revelado",
            "R-8.0.3",
            ator=c.e.auditor,
            publico={
                "incidente": incidente.numero,
                "nome": incidente.nome,
                "chave": incidente.chave,
                "secundaria": incidente.secundaria,
                "testes_chave": list(incidente.testes_chave),
                "severo": incidente.severo,
            },
        )
        etapas: list[Callable[[_Ctx, int, Incidente], None]] = [self._pontuar_diagnostico, self._aplicar_dano]
        if self.dano_primeiro:  # AMB-01
            etapas.reverse()
        for etapa in etapas:
            for j in ordem:
                etapa(c, j, incidente)
        acertaram = [j for j in ordem if c.e.diagnosticos[j] == incidente.chave]
        c.e = replace(c.e, fila_da_licao=tuple(j for j in acertaram for _ in range(self.licao_cartas)))
        self._pedir_licao(c)

    def _pontuar_diagnostico(self, c: _Ctx, j: int, incidente: Incidente) -> None:
        escolha = c.e.diagnosticos[j]
        publico: dict[str, Any] = {"escolha": escolha, "fonte": FONTE_DIAGNOSTICO}
        if escolha == incidente.chave:
            ganho = self._ganhar(c, j, self.acerto)
            self._jog(c, j, acertos=c.e.jogadores[j].acertos + 1)
            publico |= {"classificacao": "chave", "fichas": {str(j): ganho}}
            self._ev(c, "diagnostico_pontuado", "R-8.0.4", ator=j, publico=publico, amb="AMB-01")
            return
        publico["classificacao"] = "secundaria" if escolha == incidente.secundaria else "outra"
        self._ev(c, "diagnostico_pontuado", "R-8.0.4a", ator=j, publico=publico)

    def _aplicar_dano(self, c: _Ctx, j: int, incidente: Incidente) -> None:
        cat = self.catalogo
        jogador = c.e.jogadores[j]
        x = incidente.chave
        da_categoria = [carta for carta in jogador.sistema if cat.categoria(carta) == x]
        com_teste_chave = [carta for carta in da_categoria if cat.teste(carta) in incidente.testes_chave]
        itens: dict[str, int] = {}
        if not da_categoria:
            itens["sem_cobertura"] = self.dano_sem_cobertura  # R-8.1.1
        if x in jogador.alertas:
            itens["alerta"] = self.dano_alerta  # R-8.1.2
        if incidente.severo and not com_teste_chave:
            itens["severo_sem_teste_chave"] = self.dano_severo  # R-8.1.3
        candidatas = com_teste_chave if incidente.severo and com_teste_chave else da_categoria
        if candidatas:
            carta = self._escolher_para_revelar(jogador, candidatas)
            if carta not in jogador.reveladas:
                self._jog(c, j, reveladas=jogador.reveladas + (carta,))
            self._ev(c, "cobertura_comprovada", "R-8.0.5a", ator=j, publico={"carta": cat.teste(carta)}, amb="AMB-11")
        devido = sum(itens.values())
        pago = self._perder(c, j, devido)
        self._ev(
            c,
            "dano_incidente",
            "R-8.0.5",
            ator=j,
            publico={"itens": itens, "devido": devido, "fonte": FONTE_DANO, "fichas": {str(j): -pago}},
        )

    def _pedir_licao(self, c: _Ctx) -> None:
        cat = self.catalogo
        x = self.incidente_atual(c.e).chave
        while c.e.fila_da_licao:
            j = c.e.fila_da_licao[0]
            if any(cat.categoria(carta) == x for carta in c.e.backlog):
                c.e = replace(c.e, pendente=Pendente(E.LICAO, j))
                return
            c.e = replace(c.e, fila_da_licao=tuple(k for k in c.e.fila_da_licao if k != j))
            self._ev(c, "licao_indisponivel", "R-8.0.6", ator=j, amb="AMB-02")
        self._limpeza(c)

    def _pegar(self, c: _Ctx, j: int, acao: Acao) -> None:
        cat = self.catalogo
        jogador = c.e.jogadores[j]
        carta = self._carta_por_teste(c.e.backlog, acao.teste)
        posicao = c.e.backlog.index(carta)
        c.e = replace(c.e, backlog=_sem(c.e.backlog, carta), fila_da_licao=c.e.fila_da_licao[1:])
        self._jog(c, j, mao=jogador.mao + (carta,), pegas_do_backlog=jogador.pegas_do_backlog + (carta,))
        self._ev(c, "licao_aprendida", "R-8.0.6", ator=j, publico={"carta": cat.teste(carta)})
        self._repor_backlog(c, posicao, "R-8.0.6a")
        self._pedir_licao(c)

    def _recusar(self, c: _Ctx, j: int, acao: Acao) -> None:
        c.e = replace(c.e, fila_da_licao=tuple(k for k in c.e.fila_da_licao if k != j))
        self._ev(c, "licao_recusada", "R-8.0.6", ator=j, amb="AMB-02")
        self._pedir_licao(c)

    def _limpeza(self, c: _Ctx) -> None:
        incidente = self.incidente_atual(c.e)
        x = incidente.chave
        removidos = [j for j, jogador in enumerate(c.e.jogadores) if x in jogador.alertas]
        for j in removidos:
            self._jog(c, j, alertas=_sem(c.e.jogadores[j].alertas, x))
        c.e = replace(
            c.e,
            agora=None,
            resolvidos=c.e.resolvidos + (incidente.numero,),
            diagnosticos=(),
            fila_da_licao=(),
            pendente=None,
        )
        self._ev(
            c,
            "limpeza",
            "R-8.0.7",
            publico={"categoria": x, "alertas_removidos": removidos, "incidente": incidente.numero},
        )
        self._fim_do_ciclo(c)

    def _fim_do_ciclo(self, c: _Ctx) -> None:
        e = c.e
        if e.ciclo >= self.ciclos:  # R-9.0.1
            self._critical_failure(c)
            return
        linha = e.linha_do_tempo
        c.e = replace(
            e,
            primeiro=self._esquerda(e, e.primeiro),
            auditor=self._esquerda(e, e.auditor),
            agora=e.proximo,
            proximo=linha[0] if linha else None,
            linha_do_tempo=linha[1:],
            ciclo=e.ciclo + 1,
        )
        self._ev(
            c,
            "fim_do_ciclo",
            "R-4.9",
            publico={
                "ciclo_encerrado": e.ciclo,
                "primeiro": c.e.primeiro,
                "auditor": c.e.auditor,
                "agora": c.e.agora,
                "proximo": c.e.proximo,
            },
        )
        self._iniciar_planejamento(c)

    # ------------------------------------------------------------------ fim de jogo (seção 9)

    def _critical_failure(self, c: _Ctx) -> None:
        cat = self.catalogo
        e = c.e
        sorteio = gerador(e.semente, e.partida, FLUXO_JOGO, e.contador_rng)
        rolagens: list[int] = []
        categoria: str | None = None
        while categoria is None:  # R-2.0.16: face de categoria fora do jogo, rola de novo
            face = int(sorteio.integers(1, self.faces + 1))
            rolagens.append(face)
            categoria = cat.categoria_da_face(face)
        c.e = replace(e, fase=E.CRITICAL_FAILURE, contador_rng=e.contador_rng + 1)
        self._ev(c, "critical_failure", "R-9.1.1", publico={"rolagens": rolagens, "categoria": categoria})
        for j in self.ordem_de_jogo(c.e):
            jogador = c.e.jogadores[j]
            testes = {cat.teste(carta) for carta in jogador.sistema if cat.categoria(carta) == categoria}
            itens = {"sempre": self.cf_sempre}  # R-9.1.3
            if len(testes) < self.testes_distintos:
                itens["sem_cobertura_profunda"] = self.cf_sem_profunda  # R-9.1.4
            if not testes:
                itens["sem_cobertura"] = self.cf_sem_cobertura  # R-9.1.5
            if categoria in jogador.alertas:
                itens["alerta"] = self.cf_alerta  # R-9.1.6
            devido = sum(itens.values())
            pago = self._perder(c, j, devido)
            self._ev(
                c,
                "dano_critical_failure",
                "R-9.1.7",
                ator=j,
                publico={"itens": itens, "devido": devido, "fonte": FONTE_CRITICAL_FAILURE, "fichas": {str(j): -pago}},
            )
        if self.cf_limpa_alertas:  # alternativa de AMB-12; o padrão é o cubo ficar
            com_alerta = [j for j, jogador in enumerate(c.e.jogadores) if categoria in jogador.alertas]
            for j in com_alerta:
                self._jog(c, j, alertas=_sem(c.e.jogadores[j].alertas, categoria))
            self._ev(
                c,
                "limpeza_critical_failure",
                "R-9.1.6",
                publico={"categoria": categoria, "alertas_removidos": com_alerta},
                amb="AMB-12",
            )
        self._pontuacao_final(c)

    def _pontuacao_final(self, c: _Ctx) -> None:
        cat = self.catalogo
        for j in self.ordem_de_jogo(c.e):
            jogador = c.e.jogadores[j]
            por_categoria: dict[str, set[str]] = {}
            for carta in jogador.sistema:
                por_categoria.setdefault(cat.categoria(carta), set()).add(cat.teste(carta))
            amplitude = len(por_categoria)  # R-9.2.2
            profundas = sum(1 for testes in por_categoria.values() if len(testes) >= self.testes_distintos)
            ganho = amplitude * self.final_categoria + profundas * self.final_profunda
            perda = len(jogador.alertas) * self.final_alerta  # R-9.2.4
            if self.final_por_saldo:  # AMB-13
                fichas = max(self.fichas_minimo, jogador.fichas + ganho - perda)
            else:
                fichas = max(self.fichas_minimo, jogador.fichas - perda) + ganho
            self._jog(c, j, fichas=fichas, reveladas=jogador.sistema)
            self._ev(
                c,
                "pontuacao_final",
                "R-9.2.1",
                ator=j,
                publico={
                    "sistema": cat.nomes(jogador.sistema),
                    "categorias_distintas": amplitude,
                    "coberturas_profundas": profundas,
                    "alertas_ativos": len(jogador.alertas),
                    "ganho": ganho,
                    "perda": perda,
                    "fonte": FONTE_FINAL,
                    "fichas": {str(j): fichas - jogador.fichas},
                },
                amb="AMB-13",
            )
        self._encerrar(c)

    def _encerrar(self, c: _Ctx) -> None:
        """R-1.1, com os desempates R-9.2.7 e R-9.2.8 e a vitória dividida de AMB-14."""
        jogadores = c.e.jogadores
        mais_fichas = max(jogador.fichas for jogador in jogadores)
        candidatos = [j for j, jogador in enumerate(jogadores) if jogador.fichas == mais_fichas]
        criterio = "fichas"
        if len(candidatos) > 1:
            menos_alertas = min(len(jogadores[j].alertas) for j in candidatos)
            candidatos = [j for j in candidatos if len(jogadores[j].alertas) == menos_alertas]
            criterio = "alertas"
        if len(candidatos) > 1:
            mais_acertos = max(jogadores[j].acertos for j in candidatos)
            candidatos = [j for j in candidatos if jogadores[j].acertos == mais_acertos]
            criterio = "diagnosticos"
        if len(candidatos) > 1:
            criterio = "dividida"
        c.e = replace(c.e, fase=E.FIM, pendente=None, vencedores=tuple(candidatos))
        self._ev(
            c,
            "fim_de_jogo",
            "R-1.1",
            publico={
                "placar": [jogador.fichas for jogador in jogadores],
                "vencedores": candidatos,
                "criterio": criterio,
            },
            amb="AMB-14" if criterio == "dividida" else None,
        )

    # ------------------------------------------------------------------ para o laço da partida

    def observar(self, estado: Estado, assento: int) -> Observacao:
        return observar(estado, assento, self.catalogo)

    def conferir_invariantes(self, estado: Estado, em_repouso: bool = True) -> None:
        invariantes.conferir(estado, self.regras, self.catalogo, em_repouso)

    def acao_de_dict(self, dados: Any) -> Acao:
        return acao_de_dict(dados)

    def placar(self, estado: Estado) -> tuple[int, ...]:
        return tuple(jogador.fichas for jogador in estado.jogadores)

    def ponto_de_corte(self, evento: Evento) -> tuple[int, ...] | None:
        """REQ-02: no fim do ciclo 1, as fichas de cada jogador."""
        if evento.tipo == "fim_do_ciclo" and evento.publico.get("ciclo_encerrado") == 1:
            return self.placar(evento.estado)
        return None

    def sistemas_cheios_no_planejamento(self, evento: Evento) -> tuple[bool, ...] | None:
        """REQ-11: ao fim do Planejamento do ciclo 1 (início da Homologação), quem está com o sistema no teto."""
        if evento.tipo == "inicio_da_fase" and evento.publico.get("fase") == E.HOMOLOGACAO and evento.ciclo == 1:
            teto = self.regras.sistema.teto.valor
            return tuple(len(jogador.sistema) >= teto for jogador in evento.estado.jogadores)
        return None

    def blefe_na_defesa(self, evento: Evento) -> bool:
        """REQ-05 (AMB-15): a defesa nomeou um teste que não está no sistema do defensor."""
        return evento.tipo == "defesa" and evento.oculto.get("blefe") is True

    def defesa_aceita(self, evento: Evento) -> bool | None:
        """REQ-05: no fim de uma disputa, se ela terminou aceita (sem Alerta). ``None`` em outro evento."""
        if evento.tipo != "fim_da_disputa":
            return None
        return bool(evento.publico.get("resultado") == E.ACEITA)

    _MANIPULADORES: dict[str, Callable[[MotorV2, _Ctx, int, Acao], None]] = {
        A.COMPRAR: _comprar,
        A.COLOCAR: _colocar,
        A.ENCERRAR: _encerrar_turno,
        A.TESTAR: _testar,
        A.PASSAR: _passar,
        A.ADMITIR: _admitir,
        A.CONFERE: _conferir,
        A.NAO_CONFERE: _conferir,
        A.ACEITAR: _aceitar,
        A.CONTESTAR: _contestar,
        A.DIAGNOSTICAR: _diagnosticar,
        A.PEGAR: _pegar,
        A.RECUSAR: _recusar,
    }

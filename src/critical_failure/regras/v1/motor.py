"""Motor de regras da v1 (artigo do SBQS 2025, seção 4.3).

Mesma interface do motor da família v2: ``preparar``, ``acoes_legais`` e
``aplicar(estado, acao) -> (novo_estado, eventos)``, puro e determinístico.
Cada evento cita a regra da especificação da v1 (``V1-...``) e, quando a regra
foi resolvida por uma decisão do autor, a ambiguidade (``AMB-nn``).
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import replace
from itertools import combinations
from typing import Any

from critical_failure.nucleo.erros import AcaoIlegal, ConfiguracaoInvalida
from critical_failure.nucleo.rng import FLUXO_JOGO, gerador
from critical_failure.regras.v1 import acoes as A
from critical_failure.regras.v1 import estado as E
from critical_failure.regras.v1 import invariantes
from critical_failure.regras.v1.acoes import AcaoV1, acao_v1_de_dict
from critical_failure.regras.v1.config import RegrasV1, catalogo_v1
from critical_failure.regras.v1.estado import (
    DisputaEncerradaV1,
    DisputaV1,
    EstadoV1,
    EventoV1,
    JogadorV1,
    Pendente,
)
from critical_failure.regras.v1.observacao import ObservacaoV1, observar_v1
from critical_failure.regras.v1.pontuacao import TabelaDePontos, pontuar

Passo = tuple[EstadoV1, list[EventoV1]]


def _sem(tupla: tuple[int, ...], item: int) -> tuple[int, ...]:
    posicao = tupla.index(item)
    return tupla[:posicao] + tupla[posicao + 1 :]


class _Ctx:
    __slots__ = ("e", "eventos")

    def __init__(self, estado: EstadoV1) -> None:
        self.e = estado
        self.eventos: list[EventoV1] = []


class MotorV1:
    familia = "v1"
    fontes: tuple[str, ...] = ()
    """A v1 não tem fichas: o placar é a pontuação do sistema no fim."""

    def __init__(self, regras: RegrasV1) -> None:
        self.regras = regras
        self.catalogo = catalogo_v1(regras)
        r = regras
        self.jogadores_minimo = r.jogadores.minimo.valor
        self.jogadores_maximo = r.jogadores.maximo.valor
        self.mao_inicial = r.mao_inicial.valor
        self.sistema_inicial = r.sistema_inicial.valor
        self.cartas_de_teste = r.cartas_de_teste.valor
        self.falha_tomadas = r.falha.cartas_tomadas.valor
        self.verdade_tomadas = r.contestacao_verdade.cartas_tomadas.valor
        self.blefe_extras = r.contestacao_blefe.cartas_extras.valor
        self.tabela = TabelaDePontos(
            por_carta=r.pontos.carta.valor,
            por_par=r.pontos.par.valor,
            por_trio=r.pontos.trio.valor,
            cartas_no_par=r.combinacoes.cartas_no_par.valor,
            cartas_no_trio=r.combinacoes.cartas_no_trio.valor,
        )
        i = r.interpretacoes
        self.vale_a_declaracao = i.blefe_aceito.valor == "declaracao"
        self.alvo_vazio = i.alvo_com_sistema_vazio.valor

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
        c.eventos.append(
            EventoV1(tipo, regra, c.e.rodada, c.e.fase, ator, publico or {}, oculto or {}, visivel or {}, amb, c.e)
        )

    def _jog(self, c: _Ctx, j: int, **mudancas: Any) -> None:
        jogadores = list(c.e.jogadores)
        jogadores[j] = replace(jogadores[j], **mudancas)
        c.e = replace(c.e, jogadores=tuple(jogadores))

    def _fechar(self, c: _Ctx) -> Passo:
        if not c.eventos:
            raise AcaoIlegal("a ação não produziu nenhum evento")
        c.eventos[-1] = replace(c.eventos[-1], estado=c.e)
        return c.e, c.eventos

    def _sorteio(self, c: _Ctx) -> Any:
        e = c.e
        rng = gerador(e.semente, e.partida, FLUXO_JOGO, e.contador_rng)
        c.e = replace(e, contador_rng=e.contador_rng + 1)
        return rng

    def _esquerda(self, e: EstadoV1, j: int) -> int:
        return (j + 1) % e.n

    def _carta_por_nome(self, cartas: tuple[int, ...], nome: str) -> int:
        for carta in cartas:
            if self.catalogo.cartas[carta] == nome:
                return carta
        raise AcaoIlegal(f"não há carta {nome!r} disponível")

    def tem_atributo(self, jogador: JogadorV1, atributo: str) -> bool:
        return any(self.catalogo.atributo_da(carta) == atributo for carta in jogador.sistema)

    # ------------------------------------------------------------------ preparação

    def preparar(self, n_jogadores: int, semente: int, partida: int) -> Passo:
        if not self.jogadores_minimo <= n_jogadores <= self.jogadores_maximo:
            raise ConfiguracaoInvalida(
                f"número de jogadores {n_jogadores} fora do intervalo "
                f"{self.jogadores_minimo} a {self.jogadores_maximo} (V1-T2.2)"
            )
        vazio = JogadorV1(mao=(), sistema=(), reveladas=(), testes_feitos=0, pontos=0)
        c = _Ctx(
            EstadoV1(
                semente=semente,
                partida=partida,
                contador_rng=0,
                jogadores=(vazio,) * n_jogadores,
                baralho=(),
                descarte=(),
                fase=E.PREPARACAO,
                vez=0,
                pendente=None,
                disputa=None,
                historico=(),
                vencedores=(),
            )
        )
        ordem = [int(i) for i in self._sorteio(c).permutation(len(self.catalogo.cartas))]
        c.e = replace(c.e, baralho=tuple(ordem))
        self._ev(c, "baralho_embaralhado", "V1-4.3.1", publico={"cartas": len(ordem)}, oculto={"ordem": ordem})
        for j in range(n_jogadores):
            mao = c.e.baralho[: self.mao_inicial]
            c.e = replace(c.e, baralho=c.e.baralho[self.mao_inicial :])
            self._jog(c, j, mao=mao)
            self._ev(
                c,
                "mao_inicial",
                "V1-4.3.1",
                ator=j,
                publico={"cartas": len(mao)},
                oculto={"mao": self.catalogo.nomes(mao)},
                visivel={"mao": [j]},
            )
        c.e = replace(c.e, fase=E.MONTAGEM, pendente=Pendente(E.MONTAR, 0))
        self._ev(c, "ordem_de_jogo", "V1-4.3.2", publico={"ordem": list(range(n_jogadores))})
        return self._fechar(c)

    # ------------------------------------------------------------------ consulta

    def acoes_legais(self, e: EstadoV1) -> tuple[AcaoV1, ...]:
        p = e.pendente
        if p is None:
            return ()
        j = p.jogador
        if p.tipo == E.MONTAR:
            # AMB-28: a carta Critical Failure fica obrigatoriamente na mão.
            podem = sorted(self.catalogo.nomes([c for c in e.jogadores[j].mao if c not in self._especiais()]))
            escolhas = sorted(set(combinations(podem, self.sistema_inicial)))
            return tuple(AcaoV1(A.MONTAR, cartas=escolha) for escolha in escolhas)
        if p.tipo == E.TESTAR:
            opcoes: list[AcaoV1] = []
            for nome in dict.fromkeys(self.catalogo.nomes(e.jogadores[j].mao)):
                for alvo in range(e.n):
                    if alvo != j and (self.alvo_vazio or e.jogadores[alvo].sistema):
                        opcoes.append(AcaoV1(A.TESTAR, cartas=(nome,), alvo=alvo))
            return tuple(opcoes)
        if p.tipo == E.DECLARAR:
            return (AcaoV1(A.DECLARAR, tem=True), AcaoV1(A.DECLARAR, tem=False))
        if p.tipo == E.DUVIDAR:
            return (AcaoV1(A.ACEITAR), AcaoV1(A.DUVIDAR))
        if p.tipo == E.CONTESTAR:
            return (AcaoV1(A.ACEITAR), AcaoV1(A.CONTESTAR))
        raise AcaoIlegal(f"decisão pendente desconhecida: {p.tipo}")

    def _especiais(self) -> set[int]:
        return {i for i, nome in enumerate(self.catalogo.cartas) if nome in self.catalogo.especiais}

    def acao_de_dict(self, dados: Any) -> AcaoV1:
        return acao_v1_de_dict(dados)

    # ------------------------------------------------------------------ aplicar

    def aplicar(self, estado: EstadoV1, acao: AcaoV1) -> Passo:
        p = estado.pendente
        if p is None:
            raise AcaoIlegal("a partida já terminou")
        if not isinstance(acao, AcaoV1):
            raise AcaoIlegal(f"não é uma ação da v1: {acao!r}")
        legal = acao.sem_explicacao() in self.acoes_legais(estado)
        if not legal or (acao.explicacao_correta is not None and not (acao.tipo == A.DECLARAR and acao.tem)):
            raise AcaoIlegal(f"ação ilegal para a decisão '{p.tipo}': {acao.texto()}")
        c = _Ctx(estado)
        self._MANIPULADORES[p.tipo](self, c, p.jogador, acao)
        return self._fechar(c)

    # ------------------------------------------------------------------ montagem (V1-4.3.3)

    def _montar(self, c: _Ctx, j: int, acao: AcaoV1) -> None:
        jogador = c.e.jogadores[j]
        mao = jogador.mao
        sistema: tuple[int, ...] = ()
        for nome in acao.cartas:
            carta = self._carta_por_nome(mao, nome)
            mao, sistema = _sem(mao, carta), (*sistema, carta)
        self._jog(c, j, mao=mao, sistema=sistema)
        self._ev(
            c,
            "sistema_montado",
            "V1-4.3.3",
            ator=j,
            publico={"cartas": len(sistema)},
            oculto={"sistema": self.catalogo.nomes(sistema)},
            visivel={"sistema": [j]},
            amb="AMB-28",
        )
        proximo = j + 1
        if proximo < c.e.n:
            c.e = replace(c.e, pendente=Pendente(E.MONTAR, proximo))
            return
        c.e = replace(c.e, fase=E.TESTES)
        self._ev(c, "inicio_dos_testes", "V1-4.3.4", publico={"primeiro": 0})
        self._dar_a_vez(c, 0)

    # ------------------------------------------------------------------ testes (V1-4.3.4 a V1-4.3.12)

    def _dar_a_vez(self, c: _Ctx, inicio: int) -> None:
        j = inicio
        for _ in range(c.e.n):
            if c.e.jogadores[j].mao:
                c.e = replace(c.e, vez=j, pendente=Pendente(E.TESTAR, j))
                return
            j = self._esquerda(c.e, j)
        self._pontuacao_final(c)

    def _testar(self, c: _Ctx, j: int, acao: AcaoV1) -> None:
        assert acao.alvo is not None
        jogador = c.e.jogadores[j]
        carta = self._carta_por_nome(jogador.mao, acao.cartas[0])
        nome = self.catalogo.cartas[carta]
        atributo = self.catalogo.atributo[nome]
        self._jog(c, j, mao=_sem(jogador.mao, carta))
        c.e = replace(c.e, disputa=DisputaV1(j, acao.alvo, carta, atributo, E.DECLARAR))
        self._ev(
            c,
            "teste",
            "V1-4.3.5",
            ator=j,
            publico={"atacante": j, "defensor": acao.alvo, "carta": nome, "atributo": atributo},
            amb="AMB-25" if not c.e.jogadores[acao.alvo].sistema else None,
        )
        if nome in self.catalogo.especiais:
            self._ev(c, "falha_automatica", "V1-4.2.3", ator=j, publico={"carta": nome})
            self._tomar(c, acao.alvo, j, self.falha_tomadas, "V1-4.2.3")
            self._encerrar(c, E.CRITICAL_FAILURE, contestou=False, para_o_defensor=False)
            return
        c.e = replace(c.e, pendente=Pendente(E.DECLARAR, acao.alvo))

    def _declarar(self, c: _Ctx, j: int, acao: AcaoV1) -> None:
        d = c.e.disputa
        assert d is not None
        tem_a_cor = self.tem_atributo(c.e.jogadores[j], d.atributo)
        c.e = replace(c.e, disputa=replace(d, declarou_tem=acao.tem, explicacao_correta=acao.explicacao_correta))
        self._ev(
            c,
            "declaracao",
            "V1-4.3.8",
            ator=j,
            publico={"tem": acao.tem},
            oculto={"tem_a_cor": tem_a_cor, "blefe": bool(acao.tem) and not tem_a_cor},
            visivel={"tem_a_cor": [j], "blefe": [j]},
        )
        if not acao.tem:
            self._falha(c, "declarou que não tem", "V1-4.3.6")
            return
        c.e = replace(c.e, pendente=Pendente(E.DUVIDAR, d.atacante))

    def _aceitar(self, c: _Ctx, j: int, acao: AcaoV1) -> None:
        d = c.e.disputa
        assert d is not None
        self._ev(c, "aceite", "V1-4.3.10a", ator=j, publico={"duvidou": d.duvidou}, amb="AMB-20")
        if self.vale_a_declaracao or self.tem_atributo(c.e.jogadores[d.defensor], d.atributo):
            self._defesa(c)
        else:
            self._falha(c, "blefe aceito, resolvido pela verdade", "V1-4.3.10a")

    def _duvidar(self, c: _Ctx, j: int, acao: AcaoV1) -> None:
        d = c.e.disputa
        assert d is not None
        c.e = replace(c.e, disputa=replace(d, duvidou=True), pendente=Pendente(E.CONTESTAR, d.atacante))
        self._ev(c, "duvida", "V1-4.3.9", ator=j)
        self._ev(
            c,
            "definicao",
            "V1-4.3.9",
            ator=d.defensor,
            publico={"definicao_dada": True},
            oculto={"explicacao_correta": d.explicacao_correta},
            visivel={"explicacao_correta": [d.defensor]},
        )

    def _contestar(self, c: _Ctx, j: int, acao: AcaoV1) -> None:
        d = c.e.disputa
        assert d is not None
        defensor = c.e.jogadores[d.defensor]
        da_cor = [carta for carta in defensor.sistema if self.catalogo.atributo_da(carta) == d.atributo]
        if da_cor:
            revelada = next((carta for carta in da_cor if carta in defensor.reveladas), da_cor[0])
            if revelada not in defensor.reveladas:
                self._jog(c, d.defensor, reveladas=(*defensor.reveladas, revelada))
            self._ev(
                c,
                "contestacao",
                "V1-4.3.10b",
                ator=j,
                publico={"tinha_a_cor": True, "carta_revelada": self.catalogo.cartas[revelada]},
            )
            self._defesa(c, encerrar=False)
            self._ev(c, "punicao", "V1-4.3.11", ator=d.defensor)
            self._tomar(c, d.atacante, d.defensor, self.verdade_tomadas, "V1-4.3.11")
            self._encerrar(c, E.CONTESTOU_VERDADE, contestou=True, para_o_defensor=True)
            return
        self._ev(c, "contestacao", "V1-4.3.10b", ator=j, publico={"tinha_a_cor": False})
        self._tomar(c, d.defensor, d.atacante, self.falha_tomadas + self.blefe_extras, "V1-4.3.12")
        self._encerrar(c, E.CONTESTOU_BLEFE, contestou=True, para_o_defensor=False)

    # ------------------------------------------------------------------ resultados

    def _falha(self, c: _Ctx, motivo: str, regra: str) -> None:
        d = c.e.disputa
        assert d is not None
        self._ev(c, "falha_encontrada", regra, ator=d.defensor, publico={"motivo": motivo})
        self._tomar(c, d.defensor, d.atacante, self.falha_tomadas, "V1-4.3.6")
        self._encerrar(c, E.FALHA, contestou=False, para_o_defensor=False)

    def _defesa(self, c: _Ctx, encerrar: bool = True) -> None:
        """V1-4.3.7: o defensor acrescenta a carta de ataque ao sistema; a mesa sabe que ela está lá."""
        d = c.e.disputa
        assert d is not None
        defensor = c.e.jogadores[d.defensor]
        self._jog(c, d.defensor, sistema=(*defensor.sistema, d.carta), reveladas=(*defensor.reveladas, d.carta))
        c.e = replace(c.e, disputa=replace(d, carta_entregue=True))
        self._ev(
            c,
            "defesa_bem_sucedida",
            "V1-4.3.7",
            ator=d.defensor,
            publico={"carta_recebida": self.catalogo.cartas[d.carta]},
        )
        if encerrar:
            self._encerrar(c, E.DEFESA, contestou=False, para_o_defensor=True)

    def _tomar(self, c: _Ctx, de: int, para: int, quantas: int, regra: str) -> None:
        """Tira cartas ao acaso do sistema de ``de`` para o de ``para`` (AMB-22). Se faltar carta, tira o que houver."""
        for _ in range(quantas):
            origem = c.e.jogadores[de]
            if not origem.sistema:
                self._ev(c, "nada_a_tomar", regra, ator=para, publico={"de": de, "para": para}, amb="AMB-25")
                return
            posicao = int(self._sorteio(c).integers(len(origem.sistema)))
            carta = origem.sistema[posicao]
            # Depois de uma retirada ao acaso, a mesa já não sabe quais cartas reveladas continuam no sistema.
            self._jog(c, de, sistema=_sem(origem.sistema, carta), reveladas=())
            destino = c.e.jogadores[para]
            self._jog(c, para, sistema=(*destino.sistema, carta))
            self._ev(
                c,
                "carta_tomada",
                regra,
                ator=para,
                publico={"de": de, "para": para},
                oculto={"carta": self.catalogo.cartas[carta]},
                visivel={"carta": sorted({de, para})},
                amb="AMB-22",
            )

    def _encerrar(self, c: _Ctx, resultado: str, contestou: bool, para_o_defensor: bool) -> None:
        d = c.e.disputa
        assert d is not None
        if not para_o_defensor:
            c.e = replace(c.e, descarte=(*c.e.descarte, d.carta))
        atacante = c.e.jogadores[d.atacante]
        self._jog(c, d.atacante, testes_feitos=atacante.testes_feitos + 1)
        registro = DisputaEncerradaV1(
            atacante=d.atacante,
            defensor=d.defensor,
            teste_do_ataque=self.catalogo.cartas[d.carta],
            atributo=d.atributo,
            declarou_tem=d.declarou_tem,
            duvidou=d.duvidou,
            contestou=contestou,
            resultado=resultado,
        )
        c.e = replace(c.e, disputa=None, historico=(*c.e.historico, registro))
        self._ev(
            c,
            "fim_da_disputa",
            "V1-4.3.4",
            publico={"resultado": resultado},
            amb=None if para_o_defensor else "AMB-23",
        )
        self._dar_a_vez(c, self._esquerda(c.e, d.atacante))

    # ------------------------------------------------------------------ fim (V1-4.3.13 a V1-4.3.19)

    def _pontuacao_final(self, c: _Ctx) -> None:
        c.e = replace(c.e, pendente=None, vez=0)
        self._ev(c, "fim_da_rodada", "V1-4.3.13")
        for j, jogador in enumerate(c.e.jogadores):
            cartas = [(self.catalogo.atributo_da(carta), self.catalogo.cartas[carta]) for carta in jogador.sistema]
            pontos = pontuar(cartas, self.tabela)
            self._jog(c, j, pontos=pontos.total, reveladas=jogador.sistema)
            self._ev(
                c,
                "pontuacao_final",
                "V1-4.3.14",
                ator=j,
                publico={
                    "sistema": self.catalogo.nomes(jogador.sistema),
                    "cartas": pontos.cartas,
                    "pares": pontos.pares,
                    "trios": pontos.trios,
                    "pontos": pontos.total,
                },
                amb="AMB-24",
            )
        placar = [jogador.pontos for jogador in c.e.jogadores]
        vencedores = [j for j, pontos in enumerate(placar) if pontos == max(placar)]
        criterio = "pontos" if len(vencedores) == 1 else "dividida"
        c.e = replace(c.e, fase=E.FIM, vencedores=tuple(vencedores))
        self._ev(
            c,
            "fim_de_jogo",
            "V1-4.3.19",
            publico={"placar": placar, "vencedores": vencedores, "criterio": criterio},
            amb="AMB-29" if criterio == "dividida" else None,
        )

    # ------------------------------------------------------------------ para o laço da partida

    def observar(self, estado: EstadoV1, assento: int) -> ObservacaoV1:
        return observar_v1(estado, assento, self.catalogo)

    def conferir_invariantes(self, estado: EstadoV1, em_repouso: bool = True) -> None:
        invariantes.conferir(estado, self.regras, self.catalogo, em_repouso)

    def placar(self, estado: EstadoV1) -> tuple[int, ...]:
        return tuple(jogador.pontos for jogador in estado.jogadores)

    def ponto_de_corte(self, evento: EventoV1) -> tuple[int, ...] | None:
        """REQ-02: quando todos fizeram o primeiro teste, o tamanho de cada sistema."""
        if evento.tipo != "fim_da_disputa":
            return None
        feitos = [jogador.testes_feitos for jogador in evento.estado.jogadores]
        if all(feito == 1 for feito in feitos):
            return tuple(len(jogador.sistema) for jogador in evento.estado.jogadores)
        return None

    def sistemas_cheios_no_planejamento(self, evento: EventoV1) -> tuple[bool, ...] | None:
        """REQ-11 é da v2: a v1 não tem Planejamento nem teto no sistema."""
        return None

    _MANIPULADORES: dict[str, Callable[[MotorV1, _Ctx, int, AcaoV1], None]] = {
        E.MONTAR: _montar,
        E.TESTAR: _testar,
        E.DECLARAR: _declarar,
        E.DUVIDAR: lambda self, c, j, acao: (
            self._aceitar(c, j, acao) if acao.tipo == A.ACEITAR else self._duvidar(c, j, acao)
        ),
        E.CONTESTAR: lambda self, c, j, acao: (
            self._aceitar(c, j, acao) if acao.tipo == A.ACEITAR else self._contestar(c, j, acao)
        ),
    }

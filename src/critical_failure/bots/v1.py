"""Bots da v1: os mesmos quatro estilos da família v2, traduzidos (decisão do autor em 2026-11-10).

A v1 não tem Radar nem fichas: cada jogador monta 3 cartas no sistema, testa
com as outras 3 e, no fim, pontua as cartas do sistema. Os estilos ficam:

- **Aleatório:** escolhe ao acaso entre as ações legais.
- **Construtor:** monta o sistema que mais pontua e testa com carta e alvo ao acaso.
- **Caçador:** monta o sistema que mais pontua e escolhe o alvo pelo número de
  cartas no sistema: o "mais forte" do artigo (mais cartas), o mais fraco
  (menos cartas) ou ao acaso.
- **Heurístico:** monta o sistema que mais pontua e escolhe carta e alvo pelo
  ganho esperado de cartas, com softmax.

Blefe e contestação seguem os mesmos perfis da v2. A definição dada depois da
dúvida não pesa na decisão de contestar (decisão do autor em 2026-11-10): o
atacante que contesta "pelo limiar" usa só a chance estimada de o defensor não
ter a cor.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence
from fractions import Fraction
from typing import Any

import numpy as np

from critical_failure.bots.base import Decisao
from critical_failure.bots.estimativas import chance_de_nenhuma
from critical_failure.bots.estrategicos import (
    ALVOS,
    CAMPOS_DO_CONHECIMENTO,
    CONTESTACOES,
    PRECISAO_DOS_PESOS,
    _probabilidade,
    exp_deterministico,
)
from critical_failure.bots.mesa import MIL, MesaPublicaV1
from critical_failure.nucleo.rng import chance_por_mil, fluxo_do_bot, gerador
from critical_failure.regras.v1 import acoes as A
from critical_failure.regras.v1 import estado as E
from critical_failure.regras.v1.acoes import AcaoV1
from critical_failure.regras.v1.observacao import ObservacaoV1
from critical_failure.regras.v1.pontuacao import pontuar


class _BaseV1:
    tipo = "base"

    def __init__(self) -> None:
        self._rng: np.random.Generator | None = None
        self._mesa: MesaPublicaV1 | None = None

    def iniciar(self, semente: int, partida: int, assento: int, mesa: Any = None) -> None:
        if not isinstance(mesa, MesaPublicaV1):
            raise ValueError(f"o bot {self.tipo} da v1 precisa da mesa pública da v1")
        self._mesa = mesa
        self._rng = gerador(semente, partida, fluxo_do_bot(assento))

    @property
    def mesa(self) -> MesaPublicaV1:
        if self._mesa is None:
            raise RuntimeError("o bot precisa de iniciar() antes de decidir")
        return self._mesa

    def _sortear(self, limite: int) -> int:
        if self._rng is None:
            raise RuntimeError("o bot precisa de iniciar() antes de decidir")
        return int(self._rng.integers(limite))

    def _um_de(self, itens: Sequence[Any]) -> Any:
        return itens[self._sortear(len(itens))]

    def _explicar(self, acao: AcaoV1, por_mil: int) -> tuple[AcaoV1, str]:
        sorteio = self._sortear(MIL)
        correta = sorteio < por_mil
        return acao.com_explicacao(correta), (
            f"definição {'correta' if correta else 'incorreta'} (p={por_mil}/{MIL}, sorteio={sorteio})"
        )


class BotAleatorioV1(_BaseV1):
    """Escolhe ao acaso entre as ações legais. Mesmos parâmetros do Aleatório da v2."""

    tipo = "aleatorio"

    def __init__(self, explicacao_correta: float = 0.5, precisao_auditor: float = 1.0) -> None:
        super().__init__()
        self._explicacao = explicacao_correta
        self._precisao = precisao_auditor
        self._explicacao_por_mil = chance_por_mil(explicacao_correta)
        chance_por_mil(precisao_auditor)  # valida; na v1 não há Auditor

    def parametros(self) -> dict[str, Any]:
        return {"explicacao_correta": self._explicacao, "precisao_auditor": self._precisao}

    def decidir(self, observacao: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        indice = self._sortear(len(opcoes))
        acao = opcoes[indice]
        motivo = f"aleatório: opção {indice + 1} de {len(opcoes)}"
        if acao.tipo == A.DECLARAR and acao.tem:
            acao, sobre = self._explicar(acao, self._explicacao_por_mil)
            motivo += f"; {sobre}"
        return Decisao(acao, motivo)


class BotEstiloV1(_BaseV1):
    """Comum aos estilos: montagem, declaração, dúvida e contestação."""

    def __init__(self, conhecimento: dict[str, Any], blefe: float, contestacao: str) -> None:
        super().__init__()
        if not isinstance(conhecimento, dict) or set(conhecimento) != set(CAMPOS_DO_CONHECIMENTO):
            raise ValueError(f"conhecimento precisa ter exatamente os campos {CAMPOS_DO_CONHECIMENTO}")
        self._conhecimento = {campo: _probabilidade(campo, conhecimento[campo]) for campo in CAMPOS_DO_CONHECIMENTO}
        self._blefe = _probabilidade("blefe", blefe)
        self._blefe_por_mil = chance_por_mil(self._blefe)
        self._explicacao_por_mil = chance_por_mil(self._conhecimento["explicacao_correta"])
        if contestacao not in CONTESTACOES:
            raise ValueError(f"contestacao precisa ser uma de {CONTESTACOES}, veio {contestacao!r}")
        self._contestacao = contestacao

    def parametros(self) -> dict[str, Any]:
        return {"conhecimento": dict(self._conhecimento), "blefe": self._blefe, "contestacao": self._contestacao}

    def decidir(self, observacao: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        tratadores = {
            E.MONTAR: self._montar,
            E.TESTAR: self.testar,
            E.DECLARAR: self._declarar,
            E.DUVIDAR: self._duvidar,
            E.CONTESTAR: self._contestar,
        }
        return tratadores[observacao.decisao_pedida or ""](observacao, opcoes)

    # -- estimativas com a informação pública

    def copias_nao_vistas(self, obs: ObservacaoV1) -> Counter[str]:
        vistas: Counter[str] = Counter(obs.mao) + Counter(obs.sistema) + Counter(obs.descarte)
        for jogador in obs.jogadores:
            if jogador.assento != obs.assento:
                vistas += Counter(jogador.reveladas)
        if obs.disputa is not None:
            vistas[obs.disputa.carta] += 1
        return Counter({nome: max(copias - vistas[nome], 0) for nome, copias in self.mesa.copias.items()})

    def chance_sem_a_cor(self, obs: ObservacaoV1, alvo: int, atributo: str, nao_vistas: Counter[str]) -> float:
        jogador = obs.jogadores[alvo]
        if any(self.mesa.atributo[nome] == atributo for nome in jogador.reveladas):
            return 0.0
        escondidas = jogador.cartas_no_sistema - len(jogador.reveladas)
        favoraveis = sum(copias for nome, copias in nao_vistas.items() if self.mesa.atributo[nome] == atributo)
        return chance_de_nenhuma(escondidas, sum(nao_vistas.values()), favoraveis)

    def limiar_de_contestacao(self) -> Fraction:
        """Mesma conta de R-7.3.5, com os números da v1: perda se era verdade / (perda + ganho se era blefe)."""
        regras = self.mesa.regras
        perda = regras.contestacao_verdade.cartas_tomadas.valor
        ganho = regras.falha.cartas_tomadas.valor + regras.contestacao_blefe.cartas_extras.valor
        return Fraction(perda, perda + ganho) if perda + ganho else Fraction(0)

    # -- decisões comuns

    def _montar(self, obs: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        def pontos(acao: AcaoV1) -> int:
            return pontuar([(self.mesa.atributo[nome], nome) for nome in acao.cartas], self.mesa.tabela).total

        melhor = max(pontos(acao) for acao in opcoes)
        empatadas = [acao for acao in opcoes if pontos(acao) == melhor]
        escolhida = self._um_de(empatadas)
        return Decisao(escolhida, f"{self.tipo}: monta o sistema que mais pontua ({melhor} pontos)")

    def _declarar(self, obs: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        disputa = obs.disputa
        assert disputa is not None
        if any(self.mesa.atributo[nome] == disputa.atributo for nome in obs.sistema):
            acao, sobre = self._explicar(AcaoV1(A.DECLARAR, tem=True), self._explicacao_por_mil)
            return Decisao(acao, f"tem {disputa.atributo} no sistema: declara a verdade; {sobre}")
        sorteio = self._sortear(MIL)
        if sorteio >= self._blefe_por_mil:
            return Decisao(
                AcaoV1(A.DECLARAR, tem=False),
                f"não tem {disputa.atributo}; não blefa (blefe={self._blefe_por_mil}/{MIL}, sorteio={sorteio})",
            )
        acao, sobre = self._explicar(AcaoV1(A.DECLARAR, tem=True), self._explicacao_por_mil)
        motivo = f"não tem {disputa.atributo}; blefa (blefe={self._blefe_por_mil}/{MIL}, sorteio={sorteio}); {sobre}"
        return Decisao(acao, motivo)

    def _duvidar(self, obs: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        if self._contestacao == "nunca":
            return Decisao(AcaoV1(A.ACEITAR), "perfil: nunca contesta, então não duvida")
        return Decisao(AcaoV1(A.DUVIDAR), "duvidar não custa nada: pede a definição")

    def _contestar(self, obs: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        if self._contestacao == "sempre":
            return Decisao(AcaoV1(A.CONTESTAR), "perfil: sempre contesta")
        disputa = obs.disputa
        assert disputa is not None
        chance = self.chance_sem_a_cor(obs, disputa.defensor, disputa.atributo, self.copias_nao_vistas(obs))
        limiar = self.limiar_de_contestacao()
        contesta = chance >= limiar
        motivo = (
            f"chance estimada de o defensor não ter {disputa.atributo}: {chance:.3f}; limiar {limiar}: "
            f"{'contesta' if contesta else 'aceita'} (a definição não pesa)"
        )
        return Decisao(AcaoV1(A.CONTESTAR if contesta else A.ACEITAR), motivo)

    def testar(self, obs: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        raise NotImplementedError


class BotConstrutorV1(BotEstiloV1):
    tipo = "construtor"

    def testar(self, obs: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        escolhida = self._um_de(opcoes)
        return Decisao(escolhida, "construtor: testa com carta e alvo ao acaso")


class BotCacadorV1(BotEstiloV1):
    tipo = "cacador"

    def __init__(self, conhecimento: dict[str, Any], blefe: float, contestacao: str, alvo: str) -> None:
        super().__init__(conhecimento, blefe, contestacao)
        if alvo not in ALVOS:
            raise ValueError(f"alvo precisa ser um de {ALVOS}, veio {alvo!r}")
        self._alvo = alvo

    def parametros(self) -> dict[str, Any]:
        return {**super().parametros(), "alvo": self._alvo}

    def testar(self, obs: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        alvos = sorted({acao.alvo for acao in opcoes if acao.alvo is not None})
        if self._alvo == "aleatorio":
            alvo, razao = self._um_de(alvos), "alvo ao acaso"
        else:
            tamanhos = {a: obs.jogadores[a].cartas_no_sistema for a in alvos}
            extremo = max(tamanhos.values()) if self._alvo == "lider" else min(tamanhos.values())
            alvo = self._um_de([a for a in alvos if tamanhos[a] == extremo])
            razao = f"{'o mais forte' if self._alvo == 'lider' else 'o mais fraco'}, com {extremo} cartas no sistema"
        escolhida = self._um_de([acao for acao in opcoes if acao.alvo == alvo])
        return Decisao(escolhida, f"caçador: testa {razao}, com carta ao acaso")


class BotHeuristicoV1(BotEstiloV1):
    """Escolhe carta e alvo pelo ganho esperado de cartas, com softmax."""

    tipo = "heuristico"

    def __init__(
        self,
        conhecimento: dict[str, Any],
        blefe: float,
        contestacao: str,
        temperatura: float,
        desconto_do_futuro: float,
    ) -> None:
        super().__init__(conhecimento, blefe, contestacao)
        if isinstance(temperatura, bool) or not isinstance(temperatura, int | float) or temperatura <= 0:
            raise ValueError(f"temperatura precisa ser positiva, veio {temperatura!r}")
        self._temperatura = float(temperatura)
        self._desconto = _probabilidade("desconto_do_futuro", desconto_do_futuro)

    def parametros(self) -> dict[str, Any]:
        return {**super().parametros(), "temperatura": self._temperatura, "desconto_do_futuro": self._desconto}

    def _valor(self, obs: ObservacaoV1, acao: AcaoV1, nao_vistas: Counter[str]) -> float:
        """Cartas que espero ganhar, mais uma parte das que o alvo perde, menos uma parte das que ele ganha."""
        assert acao.alvo is not None
        peso_do_adversario = 1 / max(obs.n_jogadores - 1, 1)
        alvo = obs.jogadores[acao.alvo]
        regras = self.mesa.regras
        tomadas = regras.falha.cartas_tomadas.valor
        nome = acao.cartas[0]
        if nome in self.mesa.especiais:
            return min(tomadas, alvo.cartas_no_sistema) * (1 + peso_do_adversario)
        chance = self.chance_sem_a_cor(obs, acao.alvo, self.mesa.atributo[nome], nao_vistas)
        ganho = min(tomadas, alvo.cartas_no_sistema) * (1 + peso_do_adversario)
        return chance * ganho - (1 - chance) * peso_do_adversario

    def testar(self, obs: ObservacaoV1, opcoes: Sequence[AcaoV1]) -> Decisao:
        nao_vistas = self.copias_nao_vistas(obs)
        valores = [(acao, self._valor(obs, acao, nao_vistas)) for acao in opcoes]
        maximo = max(valor for _, valor in valores)
        pesos = [
            round(PRECISAO_DOS_PESOS * exp_deterministico((valor - maximo) / self._temperatura)) for _, valor in valores
        ]
        sorteio = self._sortear(sum(pesos))
        acumulado = 0
        escolhida = valores[-1][0]
        for (acao, _), peso in zip(valores, pesos, strict=True):
            acumulado += peso
            if sorteio < acumulado:
                escolhida = acao
                break
        maiores = sorted(valores, key=lambda par: -par[1])[:3]
        resumo = "; ".join(f"{acao.texto()}={valor:.3f}" for acao, valor in maiores)
        return Decisao(
            escolhida,
            f"heurístico: valores esperados (os maiores) {resumo}; softmax T={self._temperatura}, "
            f"sorteio={sorteio}/{sum(pesos)}",
        )

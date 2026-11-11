"""Medidas de cada partida para os requisitos de balanceamento da família v2.

O coletor vê os eventos na ordem em que o motor os produz, sem mexer no motor,
e resume a partida em números simples que vão para a tabela do executor:

- REQ-06: testes recebidos por jogador e testes contra quem tinha o menor placar;
- REQ-07: se alguém ficou com 0 ficha antes do último ciclo;
- REQ-10: tempo parado de cada jogador em cada ciclo, pelo modelo de duração;
- REQ-12: quem começou com a categoria-chave do incidente 1 no sistema;
- REQ-13: fichas movimentadas, no total e pelo dano de incidente.
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from critical_failure.duracao import Cronometro, ModeloDeDuracao
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.estado import Evento
from critical_failure.regras.v2.motor import FONTE_DANO, MotorV2

FASES_DOS_CICLOS = (E.PLANEJAMENTO, E.HOMOLOGACAO, E.PRODUCAO)


class ColetorV2:
    def __init__(self, motor: MotorV2, duracao: ModeloDeDuracao | None) -> None:
        self.motor = motor
        self.cronometro = Cronometro(duracao) if duracao is not None else None
        self.recebidos: list[int] = []
        self.testes = 0
        self.contra_o_menor = 0
        self.zerado = False
        self.parado: Counter[tuple[int, int]] = Counter()
        self.cobre: tuple[bool, ...] | None = None
        self.movimentado: Counter[str] = Counter()
        self.n = 0

    def ver(self, evento: Evento) -> None:
        e = evento.estado
        if not self.n:
            self.n = e.n
            self.recebidos = [0] * e.n
        if (
            self.cobre is None
            and evento.tipo == "inicio_da_fase"
            and evento.publico.get("fase") == E.PLANEJAMENTO
            and evento.ciclo == 1
        ):
            chave = self.motor.incidente_atual(e).chave
            cat = self.motor.catalogo
            self.cobre = tuple(any(cat.categoria(carta) == chave for carta in j.sistema) for j in e.jogadores)
        if evento.tipo == "teste":
            atacante, defensor = evento.publico["atacante"], evento.publico["defensor"]
            self.recebidos[defensor] += 1
            self.testes += 1
            menor = min(e.jogadores[k].fichas for k in range(e.n) if k != atacante)
            self.contra_o_menor += e.jogadores[defensor].fichas == menor
        if evento.ciclo < self.motor.ciclos and any(j.fichas <= self.motor.fichas_minimo for j in e.jogadores):
            self.zerado = True
        fichas = evento.publico.get("fichas")
        if fichas:
            self.movimentado[evento.publico["fonte"]] += sum(abs(valor) for valor in fichas.values())
        if self.cronometro is not None and evento.fase in FASES_DOS_CICLOS:
            tempo = self.cronometro.tempo(evento)
            if tempo:
                envolvidos = self._envolvidos(evento)
                for k in range(e.n):
                    if k not in envolvidos:
                        self.parado[(evento.ciclo, k)] += tempo

    def _envolvidos(self, evento: Evento) -> set[int]:
        """REQ-10: quem não está parado no tempo deste evento."""
        e = evento.estado
        if evento.fase == E.PRODUCAO:  # todos diagnosticam ao mesmo tempo
            return set(range(e.n))
        if e.disputa is not None:
            d = e.disputa
            return {d.atacante, d.defensor} | (set() if self.motor.auditor_externo else {d.auditor})
        return {evento.ator} if evento.ator is not None else set(range(e.n))

    def resumo(self) -> dict[str, Any]:
        return {
            "testes_recebidos": list(self.recebidos),
            "testes_contra_o_menor": self.contra_o_menor,
            "zerado_antes_do_ultimo_ciclo": self.zerado,
            "parado_s": (
                [self.parado[(ciclo, k)] for ciclo in range(1, self.motor.ciclos + 1) for k in range(self.n)]
                if self.cronometro is not None
                else None
            ),
            "cobre_incidente_1": list(self.cobre) if self.cobre is not None else None,
            "fichas_movimentadas": sum(self.movimentado.values()),
            "fichas_de_dano": self.movimentado[FONTE_DANO],
        }

"""Bots com estilo de jogo: Construtor, Caçador e Heurístico (prompt 3.4).

Cada bot combina três perfis independentes:

- **estilo**, que decide compra, colocação no sistema e testes;
- **blefe**: chance de blefar quando não tem carta da categoria atacada, e a
  forma de contestar (nunca, sempre ou pelo limiar de R-7.3.5);
- **conhecimento** (o aluno simulado): chance de a explicação estar certa
  (MOD-01), de o Auditor julgar certo (MOD-02) e de ler a categoria certa de um
  relato (MOD-03, MOD-04).

O comportamento de cada estilo foi decidido pelo autor em 2026-11-10 (ver o
diário). Toda decisão devolve um motivo, gravado no registro de auditoria.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Sequence
from fractions import Fraction
from typing import Any

import numpy as np

from critical_failure.bots.base import Decisao
from critical_failure.bots.estimativas import chance_de_nao_ter, copias_nao_vistas, teste_mais_provavel
from critical_failure.bots.mesa import MIL, Leitura, MesaPublica
from critical_failure.nucleo.rng import chance_por_mil, fluxo_do_bot, gerador
from critical_failure.observacao import Observacao
from critical_failure.regras.v2 import acoes as A
from critical_failure.regras.v2 import estado as E
from critical_failure.regras.v2.acoes import Acao

CONTADOR_DAS_LEITURAS = 1000
"""Cada leitura de incidente usa um contador próprio no fluxo do bot. Assim a
leitura não depende do estilo nem das outras decisões: bots de estilos
diferentes no mesmo assento leem o mesmo relato do mesmo jeito (números
aleatórios comuns)."""

CAMPOS_DO_CONHECIMENTO = ("explicacao_correta", "diagnostico_certo", "secundaria_no_erro", "precisao_auditor")
CONTESTACOES = ("nunca", "sempre", "limiar")
ALVOS = ("lider", "mais_fraco", "aleatorio")
PRECISAO_DOS_PESOS = 10**6
"""Os pesos do softmax viram inteiros antes do sorteio, para o determinismo."""


def exp_deterministico(x: float) -> float:
    """exp(x) para x <= 0 usando só soma, produto e divisão.

    Essas operações são exatas no padrão IEEE 754, então o resultado é o mesmo
    em qualquer plataforma, o que não é garantido para ``math.exp``.
    """
    if x > 0:
        raise ValueError("exp_deterministico só aceita x <= 0")
    if x < -60:
        return 0.0
    metades = 0
    while x < -0.5:
        x /= 2  # divisão por 2 é exata em ponto flutuante binário
        metades += 1
    termo, soma = 1.0, 1.0
    for n in range(1, 24):
        termo *= x / n
        soma += termo
    for _ in range(metades):
        soma *= soma
    return soma


def _probabilidade(nome: str, valor: Any) -> float:
    if isinstance(valor, bool) or not isinstance(valor, int | float) or not 0 <= valor <= 1:
        raise ValueError(f"{nome} precisa ser uma probabilidade entre 0 e 1, veio {valor!r}")
    return float(valor)


LIMIAR_DO_PALPITE = 0.5
"""VAR-06 (autor, 2026-11-10): o bot vota "blefe" quando a chance estimada de blefe passa de 1/2."""


class BotEstrategico:
    """O que é comum a todos os estilos: blefe, contestação, Auditor, leitura, diagnóstico e Lição aprendida."""

    tipo = "estrategico"

    def __init__(self, conhecimento: dict[str, Any], blefe: float, contestacao: str) -> None:
        if not isinstance(conhecimento, dict) or set(conhecimento) != set(CAMPOS_DO_CONHECIMENTO):
            raise ValueError(f"conhecimento precisa ter exatamente os campos {CAMPOS_DO_CONHECIMENTO}")
        self._conhecimento = {campo: _probabilidade(campo, conhecimento[campo]) for campo in CAMPOS_DO_CONHECIMENTO}
        self._por_mil = {campo: chance_por_mil(valor) for campo, valor in self._conhecimento.items()}
        self._blefe = _probabilidade("blefe", blefe)
        self._blefe_por_mil = chance_por_mil(self._blefe)
        if contestacao not in CONTESTACOES:
            raise ValueError(f"contestacao precisa ser uma de {CONTESTACOES}, veio {contestacao!r}")
        self._contestacao = contestacao
        self._rng: np.random.Generator | None = None
        self._mesa: MesaPublica | None = None
        self._origem = (0, 0, 0)
        self._leituras: dict[str, Leitura] = {}

    # ------------------------------------------------------------------ contrato

    def parametros(self) -> dict[str, Any]:
        return {"conhecimento": dict(self._conhecimento), "blefe": self._blefe, "contestacao": self._contestacao}

    def iniciar(self, semente: int, partida: int, assento: int, mesa: Any = None) -> None:
        if not isinstance(mesa, MesaPublica):
            raise ValueError(f"o bot {self.tipo} precisa da mesa pública para jogar")
        self._mesa = mesa
        self._origem = (semente, partida, assento)
        self._rng = gerador(semente, partida, fluxo_do_bot(assento))
        self._leituras = {}

    def decidir(self, observacao: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        tratadores: dict[str | None, Callable[[Observacao, Sequence[Acao]], Decisao]] = {
            E.COMPRAR: self.comprar,
            E.COLOCAR: self.colocar,
            E.AGIR: self.agir,
            E.RESPONDER: self._responder,
            E.CONFERIR: self._julgar,
            E.CONTESTAR: self._contestar,
            E.PALPITAR: self._palpitar,
            E.DIAGNOSTICAR: self._diagnosticar,
            E.LICAO: self.licao,
        }
        return tratadores[observacao.decisao_pedida](observacao, opcoes)

    # ------------------------------------------------------------------ utilidades

    @property
    def mesa(self) -> MesaPublica:
        if self._mesa is None:
            raise RuntimeError("o bot precisa de iniciar() antes de decidir")
        return self._mesa

    def _sortear(self, limite: int) -> int:
        if self._rng is None:
            raise RuntimeError("o bot precisa de iniciar() antes de decidir")
        return int(self._rng.integers(limite))

    def _um_de(self, itens: Sequence[Any]) -> Any:
        return itens[self._sortear(len(itens))]

    def leitura(self, numero: str) -> Leitura:
        """A leitura que o bot faz do relato de um incidente. Sorteada uma vez só (decisão do autor)."""
        if numero not in self._leituras:
            semente, partida, assento = self._origem
            rng = gerador(semente, partida, fluxo_do_bot(assento), CONTADOR_DAS_LEITURAS + int(numero))
            self._leituras[numero] = self.mesa.leitor.ler(
                numero, self._por_mil["diagnostico_certo"], self._por_mil["secundaria_no_erro"], rng
            )
        return self._leituras[numero]

    def categorias_do_radar(self, obs: Observacao) -> list[str]:
        """Categorias que o bot leu nos incidentes Agora e Próximo, nessa ordem, sem repetir."""
        lidas: list[str] = []
        for incidente in (obs.radar_agora, obs.radar_proximo):
            if incidente is not None:
                categoria = self.leitura(incidente.numero).categoria
                if categoria not in lidas:
                    lidas.append(categoria)
        return lidas

    def categoria_do_agora(self, obs: Observacao) -> str | None:
        return self.leitura(obs.radar_agora.numero).categoria if obs.radar_agora is not None else None

    def cobertas(self, sistema: Sequence[str]) -> set[str]:
        return {self.mesa.categoria(teste) for teste in sistema}

    def limiar_de_contestacao(self) -> Fraction:
        """R-7.3.5: contestar compensa a partir de perda / (perda + ganho), com os números das regras em uso."""
        disputa = self.mesa.regras.disputa
        perda = disputa.contestacao_verdade.atacante_paga.valor
        ganho = disputa.contestacao_blefe.defensor_paga.valor + disputa.contestacao_blefe.atacante_ganha_do_banco.valor
        return Fraction(perda, perda + ganho) if perda + ganho > 0 else Fraction(0)

    # ------------------------------------------------------------------ comum a todos os estilos

    def _responder(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        disputa = obs.disputa
        assert disputa is not None
        categoria = disputa.categoria
        meus = [teste for teste in obs.sistema if self.mesa.categoria(teste) == categoria]
        if meus:
            reveladas = set(obs.jogadores[obs.assento].reveladas)
            teste = next((t for t in meus if t in reveladas), meus[0])
            motivo = f"tem {teste} no sistema: defende com a verdade"
        else:
            sorteio = self._sortear(MIL)
            if sorteio >= self._blefe_por_mil:
                return Decisao(
                    Acao(A.ADMITIR),
                    f"não tem carta de {categoria}; não blefa (blefe={self._blefe_por_mil}/{MIL}, sorteio={sorteio})",
                )
            teste = teste_mais_provavel(obs, self.mesa, categoria)
            motivo = (
                f"não tem carta de {categoria}; blefa (blefe={self._blefe_por_mil}/{MIL}, sorteio={sorteio}) "
                f"com o teste mais provável, {teste}"
            )
        sorteio = self._sortear(MIL)
        correta = sorteio < self._por_mil["explicacao_correta"]
        motivo += (
            f"; explicação {'correta' if correta else 'incorreta'} "
            f"(p={self._por_mil['explicacao_correta']}/{MIL}, sorteio={sorteio})"
        )
        return Decisao(Acao(A.DEFENDER, teste=teste).com_explicacao(correta), motivo)

    def _julgar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        disputa = obs.disputa
        if disputa is None or disputa.explicacao_percebida is None:
            raise RuntimeError("pedido de conferência sem explicação para julgar")
        sorteio = self._sortear(MIL)
        acertou = sorteio < self._por_mil["precisao_auditor"]
        confere = disputa.explicacao_percebida if acertou else not disputa.explicacao_percebida
        motivo = (
            f"Auditor: a explicação estava {'correta' if disputa.explicacao_percebida else 'incorreta'}; "
            f"julgou {'certo' if acertou else 'errado'} (precisão={self._por_mil['precisao_auditor']}/{MIL}, "
            f"sorteio={sorteio})"
        )
        return Decisao(Acao(A.CONFERE if confere else A.NAO_CONFERE), motivo)

    def _contestar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        if self._contestacao == "nunca":
            return Decisao(Acao(A.ACEITAR), "perfil: nunca contesta")
        if self._contestacao == "sempre":
            return Decisao(Acao(A.CONTESTAR), "perfil: sempre contesta")
        disputa = obs.disputa
        assert disputa is not None and disputa.teste_nomeado is not None
        chance = chance_de_nao_ter(obs, self.mesa, disputa.defensor, [disputa.teste_nomeado])
        limiar = self.limiar_de_contestacao()
        contesta = chance >= limiar
        motivo = (
            f"chance estimada de o defensor não ter {disputa.teste_nomeado}: {chance:.3f}; "
            f"limiar {limiar} (R-7.3.5): {'contesta' if contesta else 'aceita'}"
        )
        return Decisao(Acao(A.CONTESTAR if contesta else A.ACEITAR), motivo)

    def _palpitar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        """VAR-06: vota "blefe" quando a chance estimada de o defensor não ter o teste nomeado passa de 1/2."""
        disputa = obs.disputa
        assert disputa is not None and disputa.teste_nomeado is not None
        chance = chance_de_nao_ter(obs, self.mesa, disputa.defensor, [disputa.teste_nomeado])
        blefe = chance > LIMIAR_DO_PALPITE
        motivo = (
            f"palpite: chance estimada de o defensor não ter {disputa.teste_nomeado}: {chance:.3f}; "
            f"vota {'blefe' if blefe else 'verdade'} (limiar {LIMIAR_DO_PALPITE})"
        )
        return Decisao(Acao(A.PALPITE_BLEFE if blefe else A.PALPITE_VERDADE), motivo)

    def _diagnosticar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        assert obs.radar_agora is not None
        leitura = self.leitura(obs.radar_agora.numero)
        return Decisao(Acao(A.DIAGNOSTICAR, categoria=leitura.categoria), f"leitura do relato: {leitura.motivo}")

    def licao(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        """Pega a carta: de preferência um teste que ainda não tem no sistema nem na mão."""
        pegas = [opcao for opcao in opcoes if opcao.tipo == A.PEGAR]
        if not pegas:
            return Decisao(Acao(A.RECUSAR), "não há carta para pegar")
        tenho = set(obs.sistema) | set(obs.mao)
        escolhida = next((opcao for opcao in pegas if opcao.teste not in tenho), pegas[0])
        return Decisao(escolhida, f"Lição aprendida: pega {escolhida.teste}")

    # ------------------------------------------------------------------ o que muda com o estilo

    def comprar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        raise NotImplementedError

    def colocar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        raise NotImplementedError

    def agir(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        raise NotImplementedError


# ====================================================================== Construtor


class BotConstrutor(BotEstrategico):
    """Enche o sistema cedo e testa só com as sobras (decisão do autor em 2026-11-10).

    Compra e coloca na ordem: categoria lida no incidente Agora, depois no
    Próximo, depois categorias que ainda não tem (amplitude), depois um segundo
    teste de uma categoria que já tem (cobertura profunda). Coloca até o teto o
    quanto antes. Testa com tudo o que sobra na mão: cartas repetidas ou que não
    cabem mais no sistema.
    """

    tipo = "construtor"

    def _prioridade(self, obs: Observacao, teste: str, sistema: Sequence[str]) -> int | None:
        """Quanto menor, mais o Construtor quer o teste no sistema. ``None``: não serve para o sistema."""
        if teste in sistema:
            return None
        categoria = self.mesa.categoria(teste)
        da_categoria = {t for t in sistema if self.mesa.categoria(t) == categoria}
        radar = self.categorias_do_radar(obs)
        ordem = self.mesa.categorias.index(categoria)
        if not da_categoria:
            return radar.index(categoria) if categoria in radar else len(radar) + ordem
        if len(da_categoria) < self.mesa.regras.cobertura_profunda.testes_distintos.valor:
            return len(radar) + len(self.mesa.categorias) + ordem
        return None

    def _melhor(self, obs: Observacao, candidatas: Sequence[str], sistema: Sequence[str]) -> str | None:
        notas = [(nota, posicao, teste) for posicao, teste in enumerate(candidatas)
                 if (nota := self._prioridade(obs, teste, sistema)) is not None]  # fmt: skip
        return min(notas)[2] if notas else None

    def _plano(self, obs: Observacao) -> list[str]:
        """O sistema depois de colocar as melhores cartas da mão, sem passar do teto."""
        teto = self.mesa.regras.sistema.teto.valor
        sistema, mao = list(obs.sistema), list(obs.mao)
        while len(sistema) < teto:
            melhor = self._melhor(obs, mao, sistema)
            if melhor is None:
                break
            sistema.append(melhor)
            mao.remove(melhor)
        return sistema

    def comprar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        plano = self._plano(obs)
        if len(plano) < self.mesa.regras.sistema.teto.valor:
            do_backlog = [opcao.teste for opcao in opcoes if opcao.origem == A.ORIGEM_BACKLOG and opcao.teste]
            melhor = self._melhor(obs, do_backlog, plano)
            if melhor is not None:
                categoria = self.mesa.categoria(melhor)
                return Decisao(
                    Acao(A.COMPRAR, teste=melhor, origem=A.ORIGEM_BACKLOG),
                    f"construtor: compra {melhor} ({categoria}) para o sistema",
                )
        if Acao(A.COMPRAR, origem=A.ORIGEM_TOPO) in opcoes:
            return Decisao(Acao(A.COMPRAR, origem=A.ORIGEM_TOPO), "construtor: nada útil no Backlog; compra do topo")
        escolhida = self._um_de(list(opcoes))
        return Decisao(escolhida, "construtor: baralho vazio e nada útil; compra qualquer carta do Backlog")

    def colocar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        melhor = self._melhor(obs, list(obs.mao), list(obs.sistema))
        if melhor is None:
            return Decisao(Acao(A.ENCERRAR), "construtor: nenhuma carta da mão melhora o sistema")
        categoria = self.mesa.categoria(melhor)
        if categoria in self.categorias_do_radar(obs) and categoria not in self.cobertas(obs.sistema):
            razao = f"cobre {categoria}, lida no Radar"
        elif categoria not in self.cobertas(obs.sistema):
            razao = f"categoria nova, {categoria}"
        else:
            razao = f"segundo teste de {categoria} (cobertura profunda)"
        return Decisao(Acao(A.COLOCAR, teste=melhor), f"construtor: coloca {melhor}: {razao}")

    def agir(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        testes = [opcao for opcao in opcoes if opcao.tipo == A.TESTAR]
        if not testes:
            return Decisao(Acao(A.PASSAR), "construtor: sem sobras para testar")
        escolhida = self._um_de(testes)
        return Decisao(escolhida, f"construtor: testa com a sobra {escolhida.teste}, alvo ao acaso")


# ====================================================================== Caçador


class BotCacador(BotEstrategico):
    """Mantém o sistema pequeno e usa as cartas para testar (decisão do autor em 2026-11-10).

    Coloca no máximo 1 carta por ciclo: uma da categoria que leu no incidente
    Agora, se ainda não a tiver. Compra cartas dessa categoria no Backlog e, se
    não houver, do topo. Testa enquanto tiver carta, começando pela categoria do
    incidente Agora (o Alerta nela custa mais na Produção). O alvo segue a
    política: líder (mais fichas), mais fraco (menos fichas) ou ao acaso.
    """

    tipo = "cacador"

    def __init__(self, conhecimento: dict[str, Any], blefe: float, contestacao: str, alvo: str) -> None:
        super().__init__(conhecimento, blefe, contestacao)
        if alvo not in ALVOS:
            raise ValueError(f"alvo precisa ser um de {ALVOS}, veio {alvo!r}")
        self._alvo = alvo

    def parametros(self) -> dict[str, Any]:
        return {**super().parametros(), "alvo": self._alvo}

    def comprar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        alvo_do_radar = self.categoria_do_agora(obs)
        do_backlog = [
            opcao.teste
            for opcao in opcoes
            if opcao.origem == A.ORIGEM_BACKLOG and opcao.teste and self.mesa.categoria(opcao.teste) == alvo_do_radar
        ]
        if do_backlog:
            teste = do_backlog[0]
            precisa_cobrir = alvo_do_radar not in self.cobertas([*obs.sistema, *obs.mao])
            razao = "para cobrir" if precisa_cobrir else "munição em"
            return Decisao(
                Acao(A.COMPRAR, teste=teste, origem=A.ORIGEM_BACKLOG),
                f"caçador: compra {teste} {razao} {alvo_do_radar}, lida no incidente Agora",
            )
        if Acao(A.COMPRAR, origem=A.ORIGEM_TOPO) in opcoes:
            return Decisao(Acao(A.COMPRAR, origem=A.ORIGEM_TOPO), "caçador: compra do topo (carta escondida)")
        escolhida = self._um_de(list(opcoes))
        return Decisao(escolhida, "caçador: baralho vazio; compra qualquer carta do Backlog")

    def colocar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        alvo_do_radar = self.categoria_do_agora(obs)
        if alvo_do_radar is not None and alvo_do_radar not in self.cobertas(obs.sistema):
            for teste in obs.mao:
                if self.mesa.categoria(teste) == alvo_do_radar:
                    return Decisao(
                        Acao(A.COLOCAR, teste=teste),
                        f"caçador: coloca só {teste}, para cobrir {alvo_do_radar}, lida no incidente Agora",
                    )
        return Decisao(Acao(A.ENCERRAR), "caçador: guarda o resto da mão para testar")

    def _escolher_alvo(self, obs: Observacao, alvos: list[int]) -> tuple[int, str]:
        if self._alvo == "aleatorio":
            return self._um_de(alvos), "alvo ao acaso"
        fichas = {alvo: obs.jogadores[alvo].fichas for alvo in alvos}
        extremo = max(fichas.values()) if self._alvo == "lider" else min(fichas.values())
        empatados = [alvo for alvo in alvos if fichas[alvo] == extremo]
        nome = "o líder" if self._alvo == "lider" else "o mais fraco"
        return self._um_de(empatados), f"{nome}, com {extremo} fichas"

    def agir(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        testes = [opcao for opcao in opcoes if opcao.tipo == A.TESTAR]
        if not testes:
            return Decisao(Acao(A.PASSAR), "caçador: sem cartas ou sem alvo permitido")
        alvo_do_radar = self.categoria_do_agora(obs)
        cartas = list(dict.fromkeys(opcao.teste for opcao in testes))
        cartas.sort(key=lambda teste: self.mesa.categoria(teste or "") != alvo_do_radar)
        teste = cartas[0]
        alvos = [opcao.alvo for opcao in testes if opcao.teste == teste and opcao.alvo is not None]
        alvo, razao = self._escolher_alvo(obs, alvos)
        da_categoria = self.mesa.categoria(teste or "") == alvo_do_radar
        sobre = f" ({alvo_do_radar}, lida no incidente Agora)" if da_categoria else ""
        return Decisao(Acao(A.TESTAR, teste=teste, alvo=alvo), f"caçador: testa com {teste}{sobre}; {razao}")


# ====================================================================== Heurístico


class BotHeuristico(BotEstrategico):
    """Estima o valor de cada ação e escolhe por softmax (decisão do autor em 2026-11-10).

    O valor é o ganho esperado de fichas, calculado só com a informação pública:

    - **carta no sistema:** dano evitado nos incidentes à frente, pela chance de a
      categoria ser a chave (a leitura do bot vale com a chance de acerto do
      perfil; as outras categorias dividem o resto), mais o Critical Failure
      (categoria sorteada) e a pontuação final (amplitude e cobertura profunda);
    - **carta para testar:** chance estimada de o alvo não ter a categoria
      (contagem das cartas não vistas) vezes o ganho do atacante, mais uma parte
      do dano que o Alerta causa ao alvo;
    - **guardar uma carta** para o próximo Planejamento vale o seu valor no
      sistema com o desconto do futuro.

    A ação é sorteada por softmax com a temperatura do perfil, sobre pesos
    inteiros, para o resultado ser igual em qualquer plataforma.
    """

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
        if isinstance(temperatura, bool) or not isinstance(temperatura, int | float) or temperatura < 0:
            raise ValueError(f"temperatura precisa ser um número não negativo, veio {temperatura!r}")
        self._temperatura = float(temperatura)
        self._desconto = _probabilidade("desconto_do_futuro", desconto_do_futuro)

    def parametros(self) -> dict[str, Any]:
        return {**super().parametros(), "temperatura": self._temperatura, "desconto_do_futuro": self._desconto}

    # -- crenças

    def _chance_de_ser_chave(self, numero: str, categoria: str) -> float:
        acerto = self._conhecimento["diagnostico_certo"]
        if self.leitura(numero).categoria == categoria:
            return acerto
        return (1 - acerto) / (len(self.mesa.categorias) - 1)

    def _incidentes_a_frente(self, obs: Observacao) -> list[tuple[str, float]]:
        """Incidentes cujo dano ainda vem, com o peso de cada um."""
        frente: list[tuple[str, float]] = []
        if obs.radar_agora is not None and obs.fase in (E.PLANEJAMENTO, E.HOMOLOGACAO):
            frente.append((obs.radar_agora.numero, 1.0))
        if obs.radar_proximo is not None:
            frente.append((obs.radar_proximo.numero, self._desconto))
        return frente

    # -- valores

    def _valor_no_sistema(self, obs: Observacao, teste: str, sistema: Sequence[str]) -> float | None:
        """Ganho esperado de colocar o teste no sistema. ``None`` se o sistema está cheio."""
        regras = self.mesa.regras
        if len(sistema) >= regras.sistema.teto.valor:
            return None
        if teste in sistema:
            return 0.0
        categoria = self.mesa.categoria(teste)
        distintos = len({t for t in sistema if self.mesa.categoria(t) == categoria})
        profunda = regras.cobertura_profunda.testes_distintos.valor
        dano = regras.dano.incidente
        chance_de_ser_teste_chave = 1 / len(self.mesa.testes_por_categoria[categoria])
        valor = 0.0
        for numero, peso in self._incidentes_a_frente(obs):
            chance = self._chance_de_ser_chave(numero, categoria)
            if distintos == 0:
                valor += peso * chance * dano.sem_cobertura.valor
            valor += (
                peso
                * chance
                * self.mesa.chance_de_severo
                * dano.severo_sem_teste_chave.valor
                * (chance_de_ser_teste_chave)
            )
        cf = regras.dano.critical_failure
        chance_no_dado = self._desconto * self._desconto / len(self.mesa.categorias)
        if distintos == 0:
            valor += chance_no_dado * cf.sem_cobertura.valor
        if distintos + 1 == profunda:
            valor += chance_no_dado * cf.sem_cobertura_profunda.valor + regras.final.cobertura_profunda.valor
        if distintos == 0:
            valor += regras.final.categoria_distinta.valor
        return valor

    def _valor_de_testar(self, obs: Observacao, teste: str, alvo: int, nao_vistas: Counter[str]) -> float:
        regras = self.mesa.regras
        categoria = self.mesa.categoria(teste)
        chance = chance_de_nao_ter(obs, self.mesa, alvo, self.mesa.testes_por_categoria[categoria], nao_vistas)
        dano_no_alvo = 0.0
        if obs.radar_agora is not None and obs.fase in (E.PLANEJAMENTO, E.HOMOLOGACAO):
            dano_no_alvo = self._chance_de_ser_chave(obs.radar_agora.numero, categoria) * (
                regras.dano.incidente.alerta.valor
            )
        peso_do_adversario = 1 / max(obs.n_jogadores - 1, 1)
        return chance * (regras.disputa.falhou.atacante_ganha.valor + peso_do_adversario * dano_no_alvo)

    def _valor_como_municao(self, obs: Observacao, teste: str, nao_vistas: Counter[str]) -> float:
        categoria = self.mesa.categoria(teste)
        valores = [
            self._valor_de_testar(obs, teste, jogador.assento, nao_vistas)
            for jogador in obs.jogadores
            if jogador.assento != obs.assento and categoria not in jogador.alertas
        ]
        return max(valores, default=0.0)

    def _valor_da_carta(
        self, obs: Observacao, teste: str, nao_vistas: Counter[str], outras: Sequence[float] = ()
    ) -> float:
        no_sistema = self._valor_no_sistema(obs, teste, obs.sistema)
        municao = self._municao_ajustada(obs, self._valor_como_municao(obs, teste, nao_vistas), outras)
        return max(no_sistema or 0.0, municao)

    # -- limite de testes por ciclo (VAR-11) e custo do teste (VAR-12): autor, 2026-11-11

    def _limite_e_custo(self) -> tuple[int, int, int]:
        """(testes por ciclo, custo do teste pago, primeiro teste pago); zeros na regra da versão."""
        regras = self.mesa.regras
        limite = regras.ablacoes.testes_por_ciclo.valor if regras.ablacoes is not None else 0
        if regras.propostas is None:
            return limite, 0, 0
        return limite, regras.propostas.custo_do_teste.valor, regras.propostas.teste_pago_a_partir_do.valor

    def _testes_feitos_no_ciclo(self, obs: Observacao) -> int:
        return sum(1 for disputa in obs.historico if disputa.ciclo == obs.ciclo and disputa.atacante == obs.assento)

    def _valores_da_mao(self, obs: Observacao, nao_vistas: Counter[str]) -> list[float]:
        """Valor de ataque de cada carta da mão, na ordem da mão. Vazio sem limite nem custo (não é usado)."""
        limite, custo, _ = self._limite_e_custo()
        if not limite and not custo:
            return []
        return [self._valor_como_municao(obs, teste, nao_vistas) for teste in obs.mao]

    def _municao_ajustada(self, obs: Observacao, valor: float, outras: Sequence[float]) -> float:
        """O valor de ataque de uma carta conforme o teste do ciclo em que ela seria usada.

        As cartas de ataque são usadas da mais valiosa para a menos valiosa. Além do limite de
        testes do ciclo, a carta fica para depois e vale o valor de ataque com o desconto do futuro;
        num teste pago, vale o melhor entre pagar agora e guardar. Sem limite nem custo, o valor
        não muda, e o bot joga como antes.
        """
        limite, custo, pago_a_partir_do = self._limite_e_custo()
        if not limite and not custo:
            return valor
        ordem = self._testes_feitos_no_ciclo(obs) + sum(1 for outra in outras if outra > valor) + 1
        if limite and ordem > limite:
            return self._desconto * valor
        if custo and ordem >= pago_a_partir_do:
            return max(valor - custo, self._desconto * valor)
        return valor

    def _custo_do_teste_agora(self, obs: Observacao) -> int:
        """VAR-12: o que o próximo teste deste ciclo custa; 0 se é de graça."""
        _, custo, pago_a_partir_do = self._limite_e_custo()
        if custo and self._testes_feitos_no_ciclo(obs) + 1 >= pago_a_partir_do:
            return custo
        return 0

    # -- softmax

    def _escolher(self, valores: list[tuple[Acao, float]], estilo: str, medir: bool = True) -> Decisao:
        """Sorteia a ação. Com ``medir``, a decisão leva a margem entre as duas melhores opções (MET-08)."""
        maximo = max(valor for _, valor in valores)
        margem = None
        if medir and len(valores) > 1:
            primeiro, segundo = sorted((valor for _, valor in valores), reverse=True)[:2]
            margem = primeiro - segundo
        if self._temperatura == 0:
            melhores = [acao for acao, valor in valores if valor == maximo]
            acao = self._um_de(melhores)
            return Decisao(acao, f"{estilo}: escolhe o maior valor ({maximo:.3f}) entre {len(valores)} opções", margem)
        pesos = [
            round(PRECISAO_DOS_PESOS * exp_deterministico((valor - maximo) / self._temperatura)) for _, valor in valores
        ]
        total = sum(pesos)
        sorteio = self._sortear(total)
        acumulado = 0
        escolhida = valores[-1][0]
        for (acao, _), peso in zip(valores, pesos, strict=True):
            acumulado += peso
            if sorteio < acumulado:
                escolhida = acao
                break
        maiores = sorted(valores, key=lambda par: -par[1])[:3]
        resumo = "; ".join(f"{acao.texto()}={valor:.3f}" for acao, valor in maiores)
        motivo = (
            f"{estilo}: valores esperados (os maiores) {resumo}; softmax T={self._temperatura}, "
            f"sorteio={sorteio}/{total}"
        )
        return Decisao(escolhida, motivo, margem)

    # -- decisões

    def comprar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        nao_vistas = copias_nao_vistas(obs, self.mesa)
        mao = self._valores_da_mao(obs, nao_vistas)
        valores: list[tuple[Acao, float]] = []
        for opcao in opcoes:
            if opcao.origem == A.ORIGEM_BACKLOG and opcao.teste is not None:
                valores.append((opcao, self._valor_da_carta(obs, opcao.teste, nao_vistas, mao)))
            else:
                total = sum(nao_vistas.values())
                esperado = (
                    sum(
                        copias * self._valor_da_carta(obs, teste, nao_vistas, mao)
                        for teste, copias in nao_vistas.items()
                        if copias
                    )
                    / total
                    if total
                    else 0.0
                )
                valores.append((opcao, esperado))
        return self._escolher(valores, "heurístico, compra")

    def colocar(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        nao_vistas = copias_nao_vistas(obs, self.mesa)
        mao = self._valores_da_mao(obs, nao_vistas)
        valores: list[tuple[Acao, float]] = []
        for opcao in opcoes:
            if opcao.tipo == A.COLOCAR and opcao.teste is not None:
                no_sistema = self._valor_no_sistema(obs, opcao.teste, obs.sistema) or 0.0
                outras = mao[:]
                if outras:  # a própria carta sai da comparação com as outras da mão
                    del outras[obs.mao.index(opcao.teste)]
                municao = self._municao_ajustada(obs, self._valor_como_municao(obs, opcao.teste, nao_vistas), outras)
                valores.append((opcao, no_sistema - municao))
            else:
                valores.append((opcao, 0.0))
        return self._escolher(valores, "heurístico, colocação")

    def agir(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        nao_vistas = copias_nao_vistas(obs, self.mesa)
        custo = self._custo_do_teste_agora(obs)  # VAR-12
        valores: list[tuple[Acao, float]] = []
        for opcao in opcoes:
            if opcao.tipo == A.TESTAR and opcao.teste is not None and opcao.alvo is not None:
                guardar = self._desconto * max(self._valor_no_sistema(obs, opcao.teste, obs.sistema) or 0.0, 0.0)
                valor = self._valor_de_testar(obs, opcao.teste, opcao.alvo, nao_vistas) - guardar
                valores.append((opcao, valor - custo if custo else valor))
            else:
                valores.append((opcao, 0.0))
        return self._escolher(valores, "heurístico, Homologação")

    def licao(self, obs: Observacao, opcoes: Sequence[Acao]) -> Decisao:
        nao_vistas = copias_nao_vistas(obs, self.mesa)
        mao = self._valores_da_mao(obs, nao_vistas)
        valores = [
            (opcao, self._desconto * self._valor_da_carta(obs, opcao.teste, nao_vistas, mao))
            if opcao.tipo == A.PEGAR and opcao.teste is not None
            else (opcao, 0.0)
            for opcao in opcoes
        ]
        return self._escolher(valores, "heurístico, Lição aprendida", medir=False)

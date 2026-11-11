"""Narração de uma partida em português, a partir do registro de auditoria.

Serve para uma pessoa conferir se o motor joga como as regras dizem. Por isso a
narração mostra também o que estava oculto na mesa, entre colchetes, e cita a
regra de cada passo quando pedido.
"""

from __future__ import annotations

from typing import Any

from critical_failure.auditoria.registro import EVENTO, Linha
from critical_failure.nucleo.catalogo import Catalogo

NOMES = ("Ana", "Bruno", "Carla", "Davi", "Elisa", "Fábio", "Gabi", "Hugo")
FASES = {
    "planejamento": "Planejamento",
    "homologacao": "Homologação",
    "producao": "Produção",
}
MOTIVOS = {
    "admitiu": "admitiu a falha",
    "outra_categoria": "nomeou um teste de outra categoria",
    "nao_confere": "a explicação não conferiu",
}
ITENS = {
    "sem_cobertura": "sem cobertura",
    "alerta": "Alerta",
    "severo_sem_teste_chave": "severo sem teste-chave",
    "sempre": "sempre",
    "sem_cobertura_profunda": "sem 2 testes diferentes",
}
CRITERIOS = {
    "fichas": "mais fichas",
    "alertas": "desempate por menos Alertas ativos",
    "diagnosticos": "desempate por mais diagnósticos certos",
    "dividida": "vitória dividida",
}


def nome(assento: int | None) -> str:
    if assento is None:
        return "?"
    return NOMES[assento] if assento < len(NOMES) else f"Jogador {assento}"


def _lista(itens: list[str]) -> str:
    return ", ".join(itens) if itens else "nenhuma"


def _fichas(publico: dict[str, Any]) -> str:
    partes = [f"{nome(int(assento))} {variacao:+d}" for assento, variacao in publico.get("fichas", {}).items()]
    return ", ".join(partes)


class Narrador:
    def __init__(self, cabecalho: Linha, catalogo: Catalogo, mostrar_oculto: bool, citar_regras: bool) -> None:
        self.catalogo = catalogo
        self.mostrar_oculto = mostrar_oculto
        self.citar_regras = citar_regras
        self.n = int(cabecalho["jogadores"])
        self.fichas = [int(cabecalho["config"]["fichas"]["iniciais"]["valor"])] * self.n
        self.linhas: list[str] = []

    # -- utilidades

    def _oculto(self, texto: str) -> str:
        return f" [{texto}]" if self.mostrar_oculto else ""

    def _incidente(self, numero: str | None) -> str:
        if numero is None:
            return "Critical Failure"
        return f"{numero} | {self.catalogo.incidentes[numero].nome}"

    def _placar(self) -> str:
        return ", ".join(f"{nome(j)} {fichas}" for j, fichas in enumerate(self.fichas))

    def _dizer(self, evento: Linha, texto: str) -> None:
        if self.citar_regras:
            marca = evento["regra"] + (f", {evento['amb']}" if "amb" in evento else "")
            texto = f"{texto} ({marca})"
        self.linhas.append(texto)

    def _dano(self, publico: dict[str, Any]) -> str:
        itens = publico["itens"]
        if not itens:
            return "sem dano"
        detalhe = ", ".join(f"{ITENS.get(item, item)} {valor}" for item, valor in itens.items())
        pago = -sum(publico.get("fichas", {}).values())
        texto = f"dano {publico['devido']} ({detalhe})"
        if pago != publico["devido"]:
            texto += f"; só tinha {pago} para pagar"
        return texto

    # -- eventos

    def evento(self, ev: Linha) -> None:
        for assento, variacao in ev["publico"].get("fichas", {}).items():
            self.fichas[int(assento)] += variacao
        metodo = getattr(self, f"_ev_{ev['tipo']}", None)
        if metodo is not None:
            metodo(ev, ev["publico"], ev["oculto"], nome(ev["ator"]))

    def _ev_fichas_iniciais(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"Cada jogador começa com {p['fichas_por_jogador']} fichas.")

    def _ev_radar(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        agora, proximo = self._incidente(p["agora"]), self._incidente(p["proximo"])
        self._dizer(ev, f"Radar de Riscos. Agora: {agora}. Próximo: {proximo}.")

    def _ev_sistema_inicial(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"{quem} recebe {p['cartas']} cartas no sistema{self._oculto(_lista(o['sistema']))}.")

    def _ev_carta_trocada(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        detalhe = self._oculto(f"saiu {o['saiu']}, entrou {o['entrou']}")
        self._dizer(ev, f"{quem} tinha duas cartas do mesmo teste e trocou uma pela do topo do baralho{detalhe}.")

    def _ev_backlog_inicial(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"Backlog: {_lista(p['cartas'])}.")

    def _ev_marcadores(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"{nome(p['primeiro'])} é quem começa. {nome(p['auditor'])} é o Auditor.")

    def _ev_inicio_da_fase(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self.linhas.append("")
        self.linhas.append(f"== Ciclo {ev['ciclo']}: {FASES[p['fase']]} ==")

    def _ev_alertas_zerados(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        quem_tinha = "; ".join(f"{nome(int(j))}: {_lista(cats)}" for j, cats in p["removidos"].items())
        self._dizer(ev, f"Início do Planejamento: todos os Alertas saem. {quem_tinha}.")

    def _ev_compra(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        if p["origem"] == "backlog":
            self._dizer(ev, f"{quem} compra {p['carta']} do Backlog.")
        else:
            self._dizer(ev, f"{quem} compra do topo do baralho{self._oculto(o['carta'])}.")

    def _ev_backlog_reposto(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  O Backlog é reposto com {p['carta']}.")

    def _ev_reposicao_impossivel(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  Baralho e descarte vazios: o Backlog fica com {p['backlog']} cartas.")

    def _ev_compra_impossivel(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"{quem} não tem de onde comprar e perde {p['compras_perdidas']} compra(s).")

    def _ev_reembaralhamento(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"O baralho acabou: o descarte ({p['cartas']} cartas) é embaralhado e vira o novo baralho.")

    def _ev_colocacao(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        detalhe = self._oculto(o["carta"])
        self._dizer(ev, f"{quem} coloca uma carta no sistema{detalhe}, que fica com {p['cartas_no_sistema']}.")

    def _ev_alerta_corrigido(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  A carta corrige o Alerta de {p['categoria']} de {quem}.")

    def _ev_fim_do_turno(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(
            ev, f"{quem} encerra o turno com {p['cartas_na_mao']} na mão e {p['cartas_no_sistema']} no sistema."
        )

    def _ev_teste(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        auditor = f"Auditor: {nome(p['auditor_da_disputa'])}"
        if p["auditor_da_disputa"] != p["auditor_titular"]:
            auditor += f", no lugar de {nome(p['auditor_titular'])}, que está na disputa"
        self._dizer(ev, f"{quem} testa {nome(p['defensor'])} com {p['teste']} ({p['categoria']}). {auditor}.")

    def _ev_defesa(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        if p["resposta"] == "admitiu":
            self._dizer(ev, f'  {quem} admite: "Falhou".')
            return
        detalhe = ""
        if o:
            posse = "tem a carta" if o["tem_carta"] else "não tem a carta: é blefe"
            explicacao = "explicação correta" if o["explicacao_correta"] else "explicação incorreta"
            detalhe = self._oculto(f"{posse}; {explicacao}")
        self._dizer(ev, f"  {quem} se defende com {p['teste_nomeado']}{detalhe}.")

    def _ev_conferencia(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        veredito = "confere" if p["veredito"] == "confere" else "não confere"
        self._dizer(ev, f'  O Auditor {quem} diz: "{veredito}".')

    def _ev_aceite(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  {quem} aceita a defesa. Nada é revelado.")

    def _ev_contestacao(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        if p["tinha_carta"]:
            self._dizer(ev, f"  {quem} contesta. A carta {p['carta_revelada']} é revelada: era verdade. {_fichas(p)}.")
        else:
            alerta = p["alerta"]
            self._dizer(
                ev,
                f"  {quem} contesta. Era blefe. {_fichas(p)}. "
                f"{nome(alerta['jogador'])} recebe Alerta de {alerta['categoria']}.",
            )

    def _ev_falhou(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        alerta = p["alerta"]
        self._dizer(
            ev,
            f"  Falhou ({MOTIVOS[p['motivo']]}). {_fichas(p)}. "
            f"{nome(alerta['jogador'])} recebe Alerta de {alerta['categoria']}.",
        )

    def _ev_custo_do_teste(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  Teste pago neste ciclo: {_fichas(p)} para o banco.")

    def _ev_passou(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        motivo = " automaticamente, por não ter jogada possível" if p["automatico"] else ""
        self._dizer(ev, f"{quem} passa{motivo}.")

    def _ev_relato_lido(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        incidente = self.catalogo.incidentes[p["incidente"]]
        self._dizer(ev, f'O Auditor {quem} lê o incidente {self._incidente(p["incidente"])}: "{incidente.relato}"')

    def _ev_diagnosticos_revelados(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        escolhas = "; ".join(f"{nome(j)}: {escolha}" for j, escolha in enumerate(p["escolhas"]))
        self._dizer(ev, f"Todos revelam o diagnóstico. {escolhas}.")

    def _ev_gabarito_revelado(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        secundaria = p["secundaria"] or "não indicada"
        severidade = "SEVERO" if p["severo"] else "normal"
        self._dizer(
            ev,
            f"Gabarito: categoria-chave {p['chave']}; secundária {secundaria}; "
            f"testes-chave {' ou '.join(p['testes_chave'])}; incidente {severidade}.",
        )

    def _ev_diagnostico_pontuado(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        if p["classificacao"] == "chave":
            self._dizer(ev, f"  {quem} acertou a categoria-chave: {_fichas(p)}.")
        elif p["classificacao"] == "secundaria":
            self._dizer(ev, f"  {quem} escolheu a categoria secundária: 0.")
        else:
            self._dizer(ev, f"  {quem} errou: 0.")

    def _ev_cobertura_comprovada(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  {quem} comprova cobertura revelando {p['carta']}.")

    def _ev_dano_incidente(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  {quem}: {self._dano(p)}.")

    _ev_dano_critical_failure = _ev_dano_incidente

    def _ev_licao_aprendida(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"Lição aprendida: {quem} pega {p['carta']} do Backlog.")

    def _ev_licao_recusada(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"Lição aprendida: {quem} prefere não pegar carta.")

    def _ev_licao_indisponivel(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"Lição aprendida: não há carta da categoria no Backlog para {quem}.")

    def _ev_limpeza(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        donos = ", ".join(nome(j) for j in p["alertas_removidos"]) or "ninguém tinha"
        self._dizer(ev, f"Limpeza: saem os Alertas de {p['categoria']} ({donos}). O incidente sai do jogo.")

    def _ev_fim_do_ciclo(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(
            ev,
            f"Fim do ciclo {p['ciclo_encerrado']}. Placar: {self._placar()}. "
            f"Os marcadores passam para a esquerda: {nome(p['primeiro'])} começa e {nome(p['auditor'])} é o Auditor. "
            f"Radar. Agora: {self._incidente(p['agora'])}. Próximo: {self._incidente(p['proximo'])}.",
        )

    def _ev_critical_failure(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self.linhas.append("")
        self.linhas.append("== Critical Failure ==")
        rolagens = ", ".join(str(face) for face in p["rolagens"])
        self._dizer(ev, f"Placar antes: {self._placar_antes(ev)}. O dado deu {rolagens}: {p['categoria']}.")

    def _placar_antes(self, ev: Linha) -> str:
        return self._placar()

    def _ev_limpeza_critical_failure(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"Saem os Alertas de {p['categoria']}.")

    def _ev_pontuacao_final(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        if not any(linha == "== Revelação e pontuação final ==" for linha in self.linhas):
            self.linhas.append("")
            self.linhas.append("== Revelação e pontuação final ==")
        self._dizer(
            ev,
            f"{quem} revela o sistema: {_lista(p['sistema'])}. "
            f"{p['categorias_distintas']} categoria(s) distinta(s), {p['coberturas_profundas']} cobertura(s) "
            f"profunda(s), {p['alertas_ativos']} Alerta(s) ativo(s): +{p['ganho']} e -{p['perda']}.",
        )

    def _ev_fim_de_jogo(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        vencedores = " e ".join(nome(j) for j in p["vencedores"])
        self.linhas.append("")
        self._dizer(ev, f"Placar final: {self._placar()}. Vence: {vencedores} ({CRITERIOS[p['criterio']]}).")


def narrar(linhas: list[Linha], catalogo: Any, mostrar_oculto: bool = True, citar_regras: bool = False) -> str:
    """Narra a partida. A família das regras vem do cabeçalho do registro."""
    if linhas[0]["regras"].get("familia") == "v1":
        from critical_failure.auditoria.narrar_v1 import narrar_v1

        return narrar_v1(linhas, mostrar_oculto, citar_regras)
    cabecalho, fim = linhas[0], linhas[-1]
    regras = cabecalho["regras"]
    bots = ", ".join(f"{nome(bot['assento'])} ({bot['tipo']})" for bot in cabecalho["bots"])
    titulo = [
        f"Critical Failure {regras['versao']} | partida {cabecalho['partida']} | "
        f"semente {cabecalho['semente_mestre']} | {cabecalho['jogadores']} jogadores",
        f"Jogadores, em sentido horário: {bots}.",
    ]
    if mostrar_oculto:
        titulo.append("O que aparece entre colchetes estava oculto na mesa.")
    titulo.append("")
    narrador = Narrador(cabecalho, catalogo, mostrar_oculto, citar_regras)
    for linha in linhas:
        if linha.get("registro") == EVENTO:
            narrador.evento(linha)
    if fim.get("placar") is None:
        narrador.linhas.append(f"A partida não terminou: {fim.get('invariantes')}")
    segundos = fim.get("duracao_estimada_s")
    if segundos is not None:
        narrador.linhas.append(
            f"Duração estimada pelo modelo de tempos (MOD-05, provisório): {segundos // 60} min {segundos % 60} s."
        )
    return "\n".join(titulo + narrador.linhas) + "\n"

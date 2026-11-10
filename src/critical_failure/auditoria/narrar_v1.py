"""Narração de uma partida da v1 em português, a partir do registro de auditoria."""

from __future__ import annotations

from typing import Any

from critical_failure.auditoria.registro import EVENTO, Linha

NOMES = ("Ana", "Bruno", "Carla", "Davi", "Elisa", "Fábio", "Gabi", "Hugo")
RESULTADOS = {
    "falha_encontrada": "falha encontrada",
    "defesa_bem_sucedida": "defesa bem-sucedida",
    "critical_failure": "falha automática da Critical Failure",
    "contestou_verdade": "contestação errada: era verdade",
    "contestou_blefe": "contestação certa: era blefe",
}


def nome(assento: int | None) -> str:
    if assento is None:
        return "?"
    return NOMES[assento] if assento < len(NOMES) else f"Jogador {assento}"


class NarradorV1:
    def __init__(self, mostrar_oculto: bool, citar_regras: bool) -> None:
        self.mostrar_oculto = mostrar_oculto
        self.citar_regras = citar_regras
        self.linhas: list[str] = []
        self.rodada = -1

    def _oculto(self, texto: str) -> str:
        return f" [{texto}]" if self.mostrar_oculto else ""

    def _dizer(self, ev: Linha, texto: str) -> None:
        if self.citar_regras:
            marca = ev["regra"] + (f", {ev['amb']}" if "amb" in ev else "")
            texto = f"{texto} ({marca})"
        self.linhas.append(texto)

    def evento(self, ev: Linha) -> None:
        if ev["fase"] == "testes" and ev["ciclo"] != self.rodada and ev["tipo"] == "teste":
            self.rodada = ev["ciclo"]
            self.linhas += ["", f"== Rodada {self.rodada} de testes =="]
        metodo = getattr(self, f"_ev_{ev['tipo']}", None)
        if metodo is not None:
            metodo(ev, ev["publico"], ev["oculto"], nome(ev["ator"]))

    def _ev_mao_inicial(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"{quem} compra {p['cartas']} cartas{self._oculto(', '.join(o['mao']))}.")

    def _ev_ordem_de_jogo(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self.linhas += ["", "== Montagem dos sistemas =="]
        self._dizer(ev, f"Ordem de jogo: {', '.join(nome(j) for j in p['ordem'])}.")

    def _ev_sistema_montado(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"{quem} monta o sistema com {p['cartas']} cartas{self._oculto(', '.join(o['sistema']))}.")

    def _ev_teste(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"{quem} testa {nome(p['defensor'])} com {p['carta']}.")

    def _ev_falha_automatica(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, "  É a carta Critical Failure: falha automática, sem defesa.")

    def _ev_declaracao(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        if not p["tem"]:
            self._dizer(ev, f"  {quem} declara que não tem a cor.")
            return
        detalhe = self._oculto("tem a cor" if o["tem_a_cor"] else "não tem a cor: é blefe")
        self._dizer(ev, f"  {quem} declara que tem a cor{detalhe}.")

    def _ev_aceite(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  {quem} aceita a declaração.")

    def _ev_duvida(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  {quem} duvida.")

    def _ev_definicao(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        detalhe = self._oculto("certa" if o.get("explicacao_correta") else "errada")
        self._dizer(ev, f"  {quem} dá a definição de um teste{detalhe}.")

    def _ev_contestacao(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        if p["tinha_a_cor"]:
            self._dizer(ev, f"  {quem} contesta. A carta {p['carta_revelada']} é revelada: era verdade.")
        else:
            self._dizer(ev, f"  {quem} contesta. Não há carta da cor: era blefe.")

    def _ev_defesa_bem_sucedida(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  Defesa bem-sucedida: {quem} fica com {p['carta_recebida']} no sistema.")

    def _ev_punicao(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  Como punição pela contestação errada, {quem} tira uma carta do sistema do atacante.")

    def _ev_falha_encontrada(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  Falha encontrada ({p['motivo']}).")

    def _ev_carta_tomada(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  {quem} tira ao acaso uma carta do sistema de {nome(p['de'])}{self._oculto(o['carta'])}.")

    def _ev_nada_a_tomar(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  O sistema de {nome(p['de'])} está vazio: não há carta para tirar.")

    def _ev_fim_da_disputa(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(ev, f"  Resultado: {RESULTADOS[p['resultado']]}.")

    def _ev_fim_da_rodada(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self.linhas += ["", "== Revelação e pontuação =="]

    def _ev_pontuacao_final(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        self._dizer(
            ev,
            f"{quem} revela o sistema: {', '.join(p['sistema']) or 'vazio'}. {p['cartas']} carta(s), "
            f"{p['pares']} par(es), {p['trios']} trio(s): {p['pontos']} pontos.",
        )

    def _ev_fim_de_jogo(self, ev: Linha, p: dict[str, Any], o: dict[str, Any], quem: str) -> None:
        placar = ", ".join(f"{nome(j)} {pontos}" for j, pontos in enumerate(p["placar"]))
        vencedores = " e ".join(nome(j) for j in p["vencedores"])
        criterio = "vitória dividida" if p["criterio"] == "dividida" else "mais pontos"
        self.linhas.append("")
        self._dizer(ev, f"Placar final: {placar}. Vence: {vencedores} ({criterio}).")


def narrar_v1(linhas: list[Linha], mostrar_oculto: bool = True, citar_regras: bool = False) -> str:
    cabecalho, fim = linhas[0], linhas[-1]
    bots = ", ".join(f"{nome(bot['assento'])} ({bot['tipo']})" for bot in cabecalho["bots"])
    titulo = [
        f"Critical Failure {cabecalho['regras']['versao']} | partida {cabecalho['partida']} | "
        f"semente {cabecalho['semente_mestre']} | {cabecalho['jogadores']} jogadores",
        f"Jogadores, em sentido horário: {bots}.",
    ]
    if mostrar_oculto:
        titulo.append("O que aparece entre colchetes estava oculto na mesa.")
    titulo.append("")
    narrador = NarradorV1(mostrar_oculto, citar_regras)
    for linha in linhas:
        if linha.get("registro") == EVENTO:
            narrador.evento(linha)
    if fim.get("placar") is None:
        narrador.linhas.append(f"A partida não terminou: {fim.get('invariantes')}")
    return "\n".join(titulo + narrador.linhas) + "\n"

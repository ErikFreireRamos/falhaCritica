"""Experimento 7 (profundidade): o Heurístico com limite e custo de teste, e as medidas MET-08 a MET-10."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest
import yaml
from conftest import RAIZ

from critical_failure import cli
from critical_failure.bots.estrategicos import BotHeuristico
from critical_failure.bots.fabrica import criar_bot
from critical_failure.bots.mesa import mesa_do_motor
from critical_failure.coleta import ColetorV2
from critical_failure.experimentos import executor
from critical_failure.experimentos.config import aplicar_mudancas, carregar_experimento
from critical_failure.partida import jogar_partida
from critical_failure.regras.familias import motor_de
from critical_failure.regras.v2 import acoes as A
from critical_failure.regras.v2.acoes import Acao
from critical_failure.regras.v2.motor import MotorV2

PERFIL = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}
LIMITE_1 = {
    "ablacoes": {
        "bug_duplicado_permitido": {"valor": False, "regra": "VAR-10"},
        "testes_por_ciclo": {"valor": 1, "regra": "VAR-11"},
    }
}
CUSTO = {
    "propostas": {
        "custo_do_teste": {"valor": 1, "regra": "VAR-12"},
        "teste_pago_a_partir_do": {"valor": 2, "regra": "VAR-12"},
    }
}
ARQUIVO = RAIZ / "experimentos" / "fase4_exp7_profundidade.yaml"


def motor(mudancas: dict[str, Any] | None = None) -> MotorV2:
    dados = yaml.safe_load((RAIZ / "configs" / "regras_v2_2_1.yaml").read_text(encoding="utf-8"))
    m = motor_de(aplicar_mudancas(dados, mudancas or {}), RAIZ / "configs")
    assert isinstance(m, MotorV2)
    return m


def heuristico(mudancas: dict[str, Any] | None = None) -> BotHeuristico:
    bot = criar_bot("heuristico", PERFIL)
    assert isinstance(bot, BotHeuristico)
    bot.iniciar(1, 0, 0, mesa_do_motor(motor(mudancas)))
    return bot


def obs(testes_feitos: int = 0) -> Any:
    """Só o que o ajuste do bot lê da observação: o ciclo, o assento e as disputas do ciclo."""
    historico = tuple(SimpleNamespace(ciclo=1, atacante=0) for _ in range(testes_feitos))
    return SimpleNamespace(ciclo=1, assento=0, historico=historico)


# ---------------------------------------------------------------- o Heurístico com limite e custo


def test_sem_limite_nem_custo_o_valor_de_ataque_nao_muda() -> None:
    bot = heuristico()
    assert bot._municao_ajustada(obs(), 0.8, [0.9, 1.0]) == 0.8
    assert bot._custo_do_teste_agora(obs(3)) == 0


def test_com_limite_a_carta_alem_do_limite_vale_com_o_desconto() -> None:
    bot = heuristico(LIMITE_1)
    desconto = bot.parametros()["desconto_do_futuro"]
    assert bot._municao_ajustada(obs(), 0.8, [0.5]) == 0.8  # é a melhor: seria o teste do ciclo
    assert bot._municao_ajustada(obs(), 0.8, [0.9]) == pytest.approx(desconto * 0.8)  # fica para depois
    assert bot._municao_ajustada(obs(1), 0.8, []) == pytest.approx(desconto * 0.8)  # o teste do ciclo já foi


def test_com_custo_o_teste_pago_vale_o_melhor_entre_pagar_e_guardar() -> None:
    bot = heuristico(CUSTO)
    desconto = bot.parametros()["desconto_do_futuro"]
    assert bot._municao_ajustada(obs(), 0.8, []) == 0.8  # 1º teste: de graça
    assert bot._municao_ajustada(obs(), 0.8, [0.9]) == pytest.approx(desconto * 0.8)  # pagar não compensa
    assert bot._municao_ajustada(obs(1), 6.0, []) == pytest.approx(5.0)  # pagar compensa
    assert bot._custo_do_teste_agora(obs()) == 0
    assert bot._custo_do_teste_agora(obs(1)) == 1


def test_margem_entre_as_duas_melhores_opcoes() -> None:
    bot = heuristico()
    valores = [
        (Acao(A.PASSAR), 0.0),
        (Acao(A.TESTAR, teste="x", alvo=1), 1.0),
        (Acao(A.TESTAR, teste="y", alvo=1), 0.7),
    ]
    assert bot._escolher(valores, "teste").margem == pytest.approx(0.3)
    assert bot._escolher(valores, "teste", medir=False).margem is None
    assert bot._escolher(valores[:1], "teste").margem is None


def test_heuristico_joga_partidas_com_limite_e_com_custo() -> None:
    for mudancas in (LIMITE_1, CUSTO):
        m = motor(mudancas)
        for partida in range(3):
            bots = [criar_bot("heuristico", PERFIL) for _ in range(4)]
            resultado = jogar_partida(m, bots, 3, partida, conferir_invariantes=True)
            assert resultado.vencedores


# ---------------------------------------------------------------- MET-08 e MET-09 em cada partida


def test_trocas_de_lider_isolado() -> None:
    """MET-09: empate no topo não é troca e não apaga o último líder isolado."""
    m = motor()
    coletor = ColetorV2(m, None)
    for placar in [(5, 5, 5), (6, 5, 5), (6, 6, 5), (6, 7, 5), (8, 7, 5), (8, 8, 8), (8, 9, 8), (9, 9, 9)]:
        coletor._conferir_lider(SimpleNamespace(jogadores=[SimpleNamespace(fichas=f) for f in placar]))
    assert coletor.trocas_de_lider == 3


@pytest.mark.parametrize(("limiar", "esperado"), [(None, None), (0.0, "nenhuma"), (1e9, "todas"), (0.5, "algumas")])
def test_escolhas_contadas_na_partida(limiar: float | None, esperado: str | None) -> None:
    bots = [criar_bot("heuristico", PERFIL) for _ in range(3)] + [criar_bot("aleatorio", {})]
    medidas = jogar_partida(motor(), bots, 11, 0, limiar_da_escolha_apertada=limiar).medidas
    com_escolha, avaliadas = medidas["decisoes_com_escolha"], medidas["decisoes_avaliadas"]
    assert len(com_escolha) == len(avaliadas) == 4
    assert all(a <= c for a, c in zip(avaliadas, com_escolha, strict=True))
    assert avaliadas[3] == 0 and com_escolha[3] > 0  # o Aleatório não avalia por valor
    assert medidas["trocas_de_lider"] >= 0
    apertadas = medidas["decisoes_apertadas"]
    if esperado is None:
        assert apertadas is None
    elif esperado == "nenhuma":
        assert apertadas == [0, 0, 0, 0]
    elif esperado == "todas":
        assert apertadas == avaliadas
    else:
        assert 0 < sum(apertadas) < sum(avaliadas)


# ---------------------------------------------------------------- o experimento


def test_experimento_7_e_valido() -> None:
    lido = carregar_experimento(ARQUIVO)
    assert len(lido.cenarios) == 40 and sum(c.partidas for c in lido.cenarios_expandidos()) == 80_000
    principais = [c for c in lido.cenarios if not c.nome.startswith("degraus")]
    degraus = [c for c in lido.cenarios if c.nome.startswith("degraus")]
    assert len(principais) == 16 and len(degraus) == 24
    for cenario in principais:
        assert {"MET-08", "MET-09"} <= set(cenario.requisitos) and cenario.pesos is not None
    for cenario in degraus:
        assert cenario.requisitos == ["MET-10"] and cenario.rodizio
        temperaturas = {bot.parametros.get("temperatura") for bot in cenario.bots if bot.rotulo != "foco"}
        assert len(temperaturas) == 1 and temperaturas <= {1, 2, 4}
    regras = {c.nome.split("_", 2)[2] for c in principais}
    assert regras == {"base", "var11_1_teste", "var11_2_testes", "var12_custo"}


def test_experimento_7_em_miniatura(tmp_path: Path) -> None:
    dados = yaml.safe_load(ARQUIVO.read_text(encoding="utf-8"))
    escolhidos = {"n4_iniciante_base", "n4_iniciante_var12_custo", "degraus_n4_var11_2_testes_t2"}
    dados["cenarios"] = [{**c, "partidas": 2} for c in dados["cenarios"] if c["nome"] in escolhidos]
    arquivo = tmp_path / "exp7.yaml"
    arquivo.write_text(yaml.safe_dump(dados, allow_unicode=True), encoding="utf-8")
    execucao = executor.executar(carregar_experimento(arquivo), arquivo, saida=tmp_path / "saida")
    assert execucao.manifest["falhas"] == 0
    principais = [linha for linha in execucao.linhas if not linha["cenario"].startswith("degraus")]
    assert all(linha["decisoes_apertadas"] is not None for linha in principais)
    degraus = [linha for linha in execucao.linhas if linha["cenario"].startswith("degraus")]
    assert all(linha["decisoes_apertadas"] is None for linha in degraus)  # o cenário não pede MET-08
    texto = (execucao.pasta / "relatorio.md").read_text(encoding="utf-8")
    assert "## Profundidade (descrição)" in texto
    for cenario in escolhidos:
        assert f"| {cenario} |" in texto
    assert cli.main(["relatorio", str(execucao.pasta)]) == 0
    assert (execucao.pasta / "relatorio.md").read_text(encoding="utf-8") == texto

"""Testes metamórficos (Fase 5): transformações que não deveriam mudar o jogo.

Critério de dois níveis (autor, 2026-11-11):

- **suíte normal**: poucas partidas, sementes fixas; passa se o intervalo de 99%
  da diferença contém 0. É determinístico, então nunca falha por azar;
- **suíte noturna** (``CF_NOTURNO=1``): mais partidas e equivalência, isto é, o
  intervalo de 95% da diferença inteiro dentro de ±0,02, a margem do REQ-01.

Relações:

- **MR-1, exata:** trocar os nomes de categorias entre si (no catálogo inteiro)
  dá as mesmas partidas: o motor e os bots não dependem do nome da categoria;
- **MR-2, estatística:** permutar as faces do dado do Critical Failure entre as
  categorias não muda a taxa de vitória por posição (o dado é uniforme);
- **MR-3, exata:** com bots idênticos, trocar a ordem dos assentos não muda nada.
  A versão com estilos diferentes e o sentido da mesa invertido não é uma
  invariância: o Backlog é comprado em sequência, e quem joga antes muda o que
  sobra (efeito de vizinho de cerca de 3 pontos). Ela virou medida da suíte
  noturna, sem veredito (autor, 2026-11-11).
"""

from __future__ import annotations

import copy
import os
import shutil
from collections.abc import Callable
from pathlib import Path
from typing import Any

import numpy as np
import yaml
from conftest import CONFIGS

from critical_failure.bots.fabrica import criar_bot
from critical_failure.metricas.estatistica import intervalo_da_diferenca
from critical_failure.partida import jogar_partida
from critical_failure.regras.familias import motor_de

NOTURNO = bool(os.environ.get("CF_NOTURNO"))
PERFIL = {"conhecimento": "experiente", "blefe": "metade", "contestacao": "limiar"}
MARGEM_NOTURNA = 0.02


def regras() -> dict[str, Any]:
    dados: dict[str, Any] = yaml.safe_load((CONFIGS / "regras_v2_2_1.yaml").read_text(encoding="utf-8"))
    return dados


def catalogo_bruto() -> dict[str, Any]:
    dados: dict[str, Any] = yaml.safe_load((CONFIGS / "catalogo_v2.yaml").read_text(encoding="utf-8"))
    return dados


def configs_com_catalogo(pasta: Path, transformar: Callable[[dict[str, Any]], dict[str, Any]]) -> Path:
    """Copia os YAML de ``configs/`` para ``pasta`` e grava lá o catálogo transformado."""
    pasta.mkdir(parents=True, exist_ok=True)
    for arquivo in CONFIGS.glob("*.yaml"):
        shutil.copy(arquivo, pasta / arquivo.name)
    novo = transformar(copy.deepcopy(catalogo_bruto()))
    (pasta / "catalogo_v2.yaml").write_text(yaml.safe_dump(novo, allow_unicode=True), encoding="utf-8")
    return pasta


def trocar_nomes(bruto: dict[str, Any], troca: dict[str, str]) -> dict[str, Any]:
    def novo(nome: str | None) -> str | None:
        return troca.get(nome, nome) if nome is not None else None

    for categoria in bruto["categorias"]:
        categoria["nome"] = novo(categoria["nome"])
    for teste in bruto["testes"]:
        teste["categoria"] = novo(teste["categoria"])
    for incidente in bruto["incidentes"]:
        incidente["chave"] = novo(incidente["chave"])
        incidente["secundaria"] = novo(incidente.get("secundaria"))
    return bruto


def girar_faces(bruto: dict[str, Any]) -> dict[str, Any]:
    """Cada categoria do jogo base passa a sair na face do dado da categoria seguinte."""
    base = [c for c in bruto["categorias"] if c["conjunto"] == "base"]
    faces = [c["face_do_dado"] for c in base]
    for categoria, face in zip(base, faces[1:] + faces[:1], strict=True):
        categoria["face_do_dado"] = face
    return bruto


def bots_mistos(ordem: list[str]) -> list[Any]:
    tabela = {
        "construtor": lambda: criar_bot("construtor", PERFIL),
        "heuristico": lambda: criar_bot("heuristico", PERFIL),
        "cacador": lambda: criar_bot("cacador", {**PERFIL, "alvo": "lider"}),
        "aleatorio": lambda: criar_bot("aleatorio", {"explicacao_correta": 0.85, "precisao_auditor": 0.95}),
    }
    return [tabela[nome]() for nome in ordem]


def fatias(vencedores: tuple[int, ...], assento: int) -> float:
    return 1 / len(vencedores) if assento in vencedores else 0.0


def conferir_igualdade(a: np.ndarray[Any, Any], b: np.ndarray[Any, Any], semente: int) -> None:
    """Nível 1: o intervalo de 99% da diferença contém 0. Nível 2 (noturno): cabe em ±0,02."""
    rng = np.random.default_rng(semente)
    if NOTURNO:
        baixo, alto = intervalo_da_diferenca(a, b, rng, confianca=0.95)
        assert baixo > -MARGEM_NOTURNA and alto < MARGEM_NOTURNA, (baixo, alto)
    else:
        baixo, alto = intervalo_da_diferenca(a, b, rng, confianca=0.99)
        assert baixo <= 0 <= alto, (baixo, alto)


# ---------------------------------------------------------------- MR-1: exata


def test_mr1_trocar_nomes_de_categorias_da_as_mesmas_partidas(tmp_path: Path) -> None:
    troca = {"Desempenho": "Flexibilidade", "Flexibilidade": "Desempenho", "Interação": "Confiabilidade"}
    troca["Confiabilidade"] = "Interação"
    pasta = configs_com_catalogo(tmp_path / "configs", lambda b: trocar_nomes(b, troca))
    original, trocado = motor_de(regras(), CONFIGS), motor_de(regras(), pasta)
    ordem = ["heuristico", "construtor", "cacador", "aleatorio"]
    for partida in range(200 if NOTURNO else 12):
        r1 = jogar_partida(original, bots_mistos(ordem), 31, partida)
        r2 = jogar_partida(trocado, bots_mistos(ordem), 31, partida)
        assert (r1.placar, r1.vencedores, r1.criterio, r1.eventos) == (
            r2.placar,
            r2.vencedores,
            r2.criterio,
            r2.eventos,
        )
        nomes = [(t, n) for t, n in r1.tipos_de_evento]
        assert nomes == list(r2.tipos_de_evento)


# ---------------------------------------------------------------- MR-2: estatística


def _bloco_de_posicoes(pasta: str, semente: int, partidas: range) -> list[list[float]]:
    """Joga um bloco de partidas de 4 Heurísticos (função de módulo, para rodar em outro processo)."""
    motor = motor_de(regras(), Path(pasta))
    linhas = []
    for partida in partidas:
        r = jogar_partida(motor, bots_mistos(["heuristico"] * 4), semente, partida)
        linhas.append([fatias(r.vencedores, assento) for assento in range(4)])
    return linhas


def taxas_por_posicao(pasta: Path, partidas: int, semente: int) -> np.ndarray[Any, Any]:
    """Uma linha por partida, uma coluna por posição: a fatia de vitória de cada assento.

    Na suíte noturna, as partidas são divididas em blocos e jogadas em 4 processos; o
    resultado é o mesmo, porque cada partida depende só da semente e do seu índice.
    """
    blocos = [range(inicio, min(inicio + 500, partidas)) for inicio in range(0, partidas, 500)]
    if NOTURNO:
        from concurrent.futures import ProcessPoolExecutor

        with ProcessPoolExecutor(max_workers=4) as executor:
            partes = list(executor.map(_bloco_de_posicoes, [str(pasta)] * len(blocos), [semente] * len(blocos), blocos))
    else:
        partes = [_bloco_de_posicoes(str(pasta), semente, bloco) for bloco in blocos]
    return np.array([linha for parte in partes for linha in parte])


def test_mr2_permutar_as_faces_do_dado_nao_muda_a_vitoria_por_posicao(tmp_path: Path) -> None:
    pasta = configs_com_catalogo(tmp_path / "configs", girar_faces)
    partidas = 30_000 if NOTURNO else 150  # autor, 2026-11-11: 30 mil por lado na suíte noturna
    a = taxas_por_posicao(CONFIGS, partidas, 41)
    b = taxas_por_posicao(pasta, partidas, 41)
    for posicao in range(4):
        conferir_igualdade(a[:, posicao], b[:, posicao], semente=posicao)


# ---------------------------------------------------------------- MR-3: exata, com bots idênticos


def test_mr3_trocar_a_ordem_dos_assentos_com_bots_identicos_nao_muda_a_vitoria_por_bot() -> None:
    """A relação do prompt: com bots idênticos, quem senta onde não muda nada.

    Cada bot é rotulado; trocar a ordem dos rótulos à mesa dá exatamente as mesmas partidas, e a
    taxa de vitória de cada assento é a mesma. A versão com estilos diferentes e o sentido da mesa
    invertido não é uma invariância do jogo: achou um efeito de vizinho de cerca de 3 pontos (o
    Backlog é comprado em sequência), que virou medida da suíte noturna (autor, 2026-11-11).
    """
    motor = motor_de(regras(), CONFIGS)
    for partida in range(100 if NOTURNO else 10):
        bots = bots_mistos(["heuristico"] * 4)
        invertidos = list(reversed(bots_mistos(["heuristico"] * 4)))
        r1 = jogar_partida(motor, bots, 59, partida)
        r2 = jogar_partida(motor, invertidos, 59, partida)
        assert (r1.placar, r1.vencedores, r1.eventos) == (r2.placar, r2.vencedores, r2.eventos)


def test_catalogo_transformado_continua_valido(tmp_path: Path) -> None:
    """A transformação da MR-2 muda de fato o dado: as mesmas faces, com outras categorias."""
    pasta = configs_com_catalogo(tmp_path / "configs", girar_faces)
    original, girado = motor_de(regras(), CONFIGS).catalogo, motor_de(regras(), pasta).catalogo
    assert sorted(original.faces) != sorted(girado.faces)
    assert sorted(face for face, _ in original.faces) == sorted(face for face, _ in girado.faces)
    assert sorted(nome for _, nome in original.faces) == sorted(nome for _, nome in girado.faces)

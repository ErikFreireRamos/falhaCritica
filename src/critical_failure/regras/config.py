"""Configuração das regras da família v2.

Todo número de regra vive no YAML, como ``{valor: ..., regra: R-x.y}``. Este
módulo valida o arquivo, confere os componentes declarados contra o catálogo e
calcula o hash da configuração resolvida, que vai para o cabeçalho de cada
registro de auditoria.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Generic, Literal, TypeVar

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError, model_validator

from critical_failure.nucleo.canonico import sha256
from critical_failure.nucleo.catalogo import (
    CONJUNTO_BASE,
    CONJUNTO_MODULO,
    Catalogo,
    ler_catalogo_bruto,
    montar_catalogo,
)
from critical_failure.nucleo.erros import ConfiguracaoInvalida

T = TypeVar("T")

VAGAS_DO_RADAR = ("agora", "proximo")
"""O motor tem exatamente estas vagas; ``radar.vagas`` precisa coincidir."""

PAPEIS_DA_DISPUTA = ("atacante", "defensor", "auditor")
"""Uma disputa precisa de três pessoas diferentes (R-7.1.4)."""


class _Base(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", strict=True)


class P(_Base, Generic[T]):  # noqa: UP046 - o pydantic e o seu plugin do mypy esperam Generic aqui
    """Um parâmetro: o valor e a regra da especificação que o define."""

    valor: T
    regra: str


Inteiro = P[int]
Logico = P[bool]


class Jogadores(_Base):
    minimo: Inteiro
    maximo: Inteiro


class Categorias(_Base):
    base: Inteiro
    modulo: Inteiro


class Baralho(_Base):
    cartas_base: Inteiro
    testes_base: Inteiro
    cartas_por_categoria: Inteiro
    cartas_modulo: Inteiro
    testes_modulo: Inteiro
    cartas_com_modulo: Inteiro
    testes_com_modulo: Inteiro


class Incidentes(_Base):
    base: Inteiro
    por_categoria: Inteiro
    severos_base: Inteiro
    modulo: Inteiro
    com_modulo: Inteiro


class Banco(_Base):
    fichas_valor_1: Inteiro
    fichas_valor_5: Inteiro
    cubos_alerta: Inteiro


class Dado(_Base):
    faces: Inteiro


class Radar(_Base):
    vagas: Inteiro


class Fichas(_Base):
    iniciais: Inteiro
    minimo: Inteiro


class LinhaDoTempo(_Base):
    incidentes: Inteiro


class Sistema(_Base):
    cartas_iniciais: Inteiro
    teto: Inteiro


class Backlog(_Base):
    tamanho: Inteiro


class Planejamento(_Base):
    compras: Inteiro


class Alertas(_Base):
    limpeza_no_planejamento: Logico


class Falhou(_Base):
    atacante_ganha: Inteiro


class ContestacaoVerdade(_Base):
    atacante_paga: Inteiro


class ContestacaoBlefe(_Base):
    defensor_paga: Inteiro
    atacante_ganha_do_banco: Inteiro


class Disputa(_Base):
    tempo_defesa_s: Inteiro
    falhou: Falhou
    contestacao_verdade: ContestacaoVerdade
    contestacao_blefe: ContestacaoBlefe


class Diagnostico(_Base):
    acerto: Inteiro


class LicaoAprendida(_Base):
    cartas: Inteiro


class DanoIncidente(_Base):
    sem_cobertura: Inteiro
    alerta: Inteiro
    severo_sem_teste_chave: Inteiro


class DanoCriticalFailure(_Base):
    sempre: Inteiro
    sem_cobertura_profunda: Inteiro
    sem_cobertura: Inteiro
    alerta: Inteiro


class Dano(_Base):
    incidente: DanoIncidente
    critical_failure: DanoCriticalFailure


class Final(_Base):
    categoria_distinta: Inteiro
    cobertura_profunda: Inteiro
    alerta_ativo: Inteiro


class CoberturaProfunda(_Base):
    testes_distintos: Inteiro


class Interpretacoes(_Base):
    """Decisões do autor sobre pontos ambíguos (docs/AMBIGUIDADES.md).

    Onde o tipo aceita um valor só, a alternativa não está implementada.
    """

    producao_ordem: P[Literal["diagnostico_primeiro", "dano_primeiro"]]
    quem_passou_pode_ser_alvo: Logico
    baralho_esgotado: P[Literal["pular_compra"]]
    carta_repetida: P[Literal["fundo"]]
    primeiro_jogador: P[Literal["assento_0"]]
    revelacao: P[Literal["minima"]]
    critical_failure_limpa_alertas: Logico
    final_ordem: P[Literal["saldo", "perdas_primeiro"]]
    empate: P[Literal["dividido"]]


class Variantes(_Base):
    """Variantes de playtest (VAR-xx), ligadas por experimento. Sem o bloco, vale a regra da versão.

    Mecânica decidida pelo autor em 2026-11-10 (docs/DIARIO_DE_BORDO.md).
    """

    custo_extra_da_explicacao: Inteiro
    """VAR-02: fichas que o defensor perde para o banco, além do "Falhou", quando a explicação não confere."""
    auditor_externo: Logico
    """VAR-03: o Auditor não é jogador; o motor julga a explicação com a precisão abaixo."""
    auditor_externo_acertos: Inteiro
    auditor_externo_julgamentos: Inteiro
    """VAR-03 (MOD-02): o Auditor externo acerta ``acertos`` em cada ``julgamentos`` explicações."""
    vizinhos_designados: P[list[Literal["esquerda", "direita"]]]
    """VAR-04: o alvo de cada ciclo, em ordem; vazio é alvo livre."""
    limite_de_testes_recebidos: Inteiro
    """VAR-05: quem já recebeu tantos testes no ciclo não pode ser alvo; 0 é sem limite."""
    palpite_da_plateia: Logico
    """VAR-06: antes da contestação, quem está fora da disputa vota verdade ou blefe (AMB-30)."""
    premio_do_palpite: Inteiro
    """VAR-06: fichas do banco para quem acertou o palpite, se houver contestação (AMB-31)."""


class Ablacoes(_Base):
    """Ablações (Experimento 3): volta uma regra da 2.1 no lugar da regra da 2.2. Sem o bloco, vale a da versão."""

    bug_duplicado_permitido: Logico
    """VAR-10: pode testar categoria em que o alvo já tem Alerta (2.1); o atacante ganha a ficha, sem cubo novo."""
    testes_por_ciclo: Inteiro
    """VAR-11: quantos testes cada jogador pode fazer por ciclo (2.1: 1); 0 é sem limite (2.2)."""


class RegrasV2(_Base):
    esquema: Literal["cf-regras/1"]
    familia: Literal["v2"]
    versao: str
    texto: str
    correcoes: list[str]
    catalogo: str
    modulo_seguranca_operacional: Logico
    jogadores: Jogadores
    ciclos: Inteiro
    categorias: Categorias
    baralho: Baralho
    incidentes: Incidentes
    banco: Banco
    dado: Dado
    radar: Radar
    fichas: Fichas
    linha_do_tempo: LinhaDoTempo
    sistema: Sistema
    backlog: Backlog
    planejamento: Planejamento
    alertas: Alertas
    disputa: Disputa
    diagnostico: Diagnostico
    licao_aprendida: LicaoAprendida
    dano: Dano
    final: Final
    cobertura_profunda: CoberturaProfunda
    interpretacoes: Interpretacoes
    variantes: Variantes | None = None
    ablacoes: Ablacoes | None = None

    @model_validator(mode="after")
    def _coerencia(self) -> RegrasV2:
        negativos = [chave for chave, (valor, _) in self.parametros().items() if _negativo(valor)]
        if negativos:
            raise ValueError(f"parâmetros negativos: {negativos}")
        if self.jogadores.minimo.valor > self.jogadores.maximo.valor:
            raise ValueError("jogadores.minimo é maior que jogadores.maximo")
        if self.jogadores.minimo.valor < len(PAPEIS_DA_DISPUTA):
            raise ValueError("jogadores.minimo é pequeno demais para haver atacante, defensor e Auditor")
        if self.linha_do_tempo.incidentes.valor != self.ciclos.valor:
            raise ValueError("linha_do_tempo.incidentes precisa ser igual a ciclos (um incidente por ciclo)")
        if self.radar.vagas.valor != len(VAGAS_DO_RADAR):
            raise ValueError(f"radar.vagas precisa ser {len(VAGAS_DO_RADAR)}: o motor tem as vagas Agora e Próximo")
        positivos = {
            "ciclos": self.ciclos.valor,
            "sistema.teto": self.sistema.teto.valor,
            "cobertura_profunda.testes_distintos": self.cobertura_profunda.testes_distintos.valor,
            "dado.faces": self.dado.faces.valor,
        }
        zerados = [chave for chave, valor in positivos.items() if valor < 1]
        if zerados:
            raise ValueError(f"parâmetros que precisam ser positivos: {zerados}")
        if self.sistema.cartas_iniciais.valor > self.sistema.teto.valor:
            raise ValueError("sistema.cartas_iniciais é maior que sistema.teto")
        v = self.variantes
        if v is not None:
            if not 0 < v.auditor_externo_acertos.valor <= v.auditor_externo_julgamentos.valor:
                raise ValueError("variantes: o Auditor externo precisa de 0 < acertos <= julgamentos")
            if v.palpite_da_plateia.valor and v.auditor_externo.valor:
                raise ValueError("variantes: palpite da plateia e Auditor externo juntos não foram definidos")
        return self

    def resolvida(self) -> dict[str, Any]:
        """Configuração completa, pronta para o cabeçalho do registro.

        Sem variantes nem ablações, os blocos ficam de fora: o hash das versões já usadas não muda.
        """
        dados = self.model_dump(mode="json")
        for bloco in ("variantes", "ablacoes"):
            if dados.get(bloco) is None:
                dados.pop(bloco, None)
        return dados

    def hash(self) -> str:
        return sha256(self.resolvida())

    def parametros(self) -> dict[str, tuple[Any, str]]:
        """Todos os parâmetros como ``{"dano.incidente.alerta": (1, "R-8.1.2")}``."""
        achados: dict[str, tuple[Any, str]] = {}

        def descer(prefixo: str, no: Any) -> None:
            if isinstance(no, dict):
                if set(no) == {"valor", "regra"}:
                    achados[prefixo] = (no["valor"], no["regra"])
                    return
                for chave, filho in no.items():
                    descer(f"{prefixo}.{chave}" if prefixo else chave, filho)

        descer("", self.model_dump())
        return achados


def _negativo(valor: Any) -> bool:
    return isinstance(valor, int) and not isinstance(valor, bool) and valor < 0


def ler_regras(dados: Any) -> RegrasV2:
    """Valida um dicionário já lido do YAML (ou do cabeçalho de um registro)."""
    try:
        return RegrasV2.model_validate(dados)
    except ValidationError as erro:
        raise ConfiguracaoInvalida(f"arquivo de regras inválido: {erro}") from erro


def carregar_regras(caminho: Path) -> RegrasV2:
    try:
        dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as erro:
        raise ConfiguracaoInvalida(f"não foi possível ler {caminho}: {erro}") from erro
    return ler_regras(dados)


def conferir_componentes(regras: RegrasV2, bruto: dict[str, Any]) -> None:
    """Confere as quantidades declaradas no YAML contra o catálogo (R-2.0.1, R-2.0.2, R-11.7)."""
    try:
        testes, incidentes, categorias = bruto["testes"], bruto["incidentes"], bruto["categorias"]
        cartas = Counter[str]()
        cartas_por_categoria = Counter[str]()
        n_testes = Counter[str]()
        for t in testes:
            cartas[t["conjunto"]] += int(t["copias"])
            n_testes[t["conjunto"]] += 1
            cartas_por_categoria[t["categoria"]] += int(t["copias"])
        n_incidentes = Counter(i["conjunto"] for i in incidentes)
        por_chave = Counter(i["chave"] for i in incidentes if i["conjunto"] == CONJUNTO_BASE)
        severos_base = sum(1 for i in incidentes if i["conjunto"] == CONJUNTO_BASE and i["severo"])
        n_categorias = Counter(c["conjunto"] for c in categorias)
    except (KeyError, TypeError, ValueError) as erro:
        raise ConfiguracaoInvalida(f"catálogo malformado: {erro!r}") from erro

    b, i = regras.baralho, regras.incidentes
    esperado: list[tuple[str, int, int]] = [
        ("baralho.cartas_base", b.cartas_base.valor, cartas[CONJUNTO_BASE]),
        ("baralho.testes_base", b.testes_base.valor, n_testes[CONJUNTO_BASE]),
        ("baralho.cartas_modulo", b.cartas_modulo.valor, cartas[CONJUNTO_MODULO]),
        ("baralho.testes_modulo", b.testes_modulo.valor, n_testes[CONJUNTO_MODULO]),
        ("baralho.cartas_com_modulo", b.cartas_com_modulo.valor, sum(cartas.values())),
        ("baralho.testes_com_modulo", b.testes_com_modulo.valor, sum(n_testes.values())),
        ("categorias.base", regras.categorias.base.valor, n_categorias[CONJUNTO_BASE]),
        ("categorias.modulo", regras.categorias.modulo.valor, n_categorias[CONJUNTO_MODULO]),
        ("incidentes.base", i.base.valor, n_incidentes[CONJUNTO_BASE]),
        ("incidentes.modulo", i.modulo.valor, n_incidentes[CONJUNTO_MODULO]),
        ("incidentes.com_modulo", i.com_modulo.valor, sum(n_incidentes.values())),
        ("incidentes.severos_base", i.severos_base.valor, severos_base),
        ("dado.faces", regras.dado.faces.valor, len(categorias)),
    ]
    for categoria in categorias:
        nome = categoria["nome"]
        esperado.append(
            (f"baralho.cartas_por_categoria ({nome})", b.cartas_por_categoria.valor, cartas_por_categoria[nome])
        )
        if categoria["conjunto"] == CONJUNTO_BASE:
            esperado.append((f"incidentes.por_categoria ({nome})", i.por_categoria.valor, por_chave[nome]))
    erros = [f"{chave}: declarado {dito}, catálogo {real}" for chave, dito, real in esperado if dito != real]
    if erros:
        raise ConfiguracaoInvalida("componentes não batem com o catálogo: " + "; ".join(erros))


def carregar_jogo(caminho_regras: Path) -> tuple[RegrasV2, Catalogo]:
    """Carrega as regras e o catálogo que elas apontam, já conferidos entre si."""
    regras = carregar_regras(caminho_regras)
    return regras, catalogo_das_regras(regras, caminho_regras.parent)


def catalogo_das_regras(regras: RegrasV2, pasta: Path) -> Catalogo:
    bruto = ler_catalogo_bruto(pasta / regras.catalogo)
    conferir_componentes(regras, bruto)
    catalogo = montar_catalogo(bruto, regras.modulo_seguranca_operacional.valor)
    disponiveis = len(catalogo.incidentes)
    if regras.linha_do_tempo.incidentes.valor > disponiveis:
        raise ConfiguracaoInvalida("há menos incidentes no catálogo do que a Linha do Tempo pede")
    return catalogo

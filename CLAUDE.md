# Critical Failure — simulador de partidas (TCC)

Simulador do jogo de cartas Critical Failure, parte do TCC de Erik Freire Ramos (Ciência da Computação, UFPB; orientadora: profa. Yuska Paola Costa Aguiar). O jogo é tratado como sistema sob teste: bots jogam milhares de partidas para verificar requisitos de balanceamento. Tudo o que o simulador produz vai para o texto do TCC.

## Quem decide é o autor

Não decida sozinho. Pare, apresente as opções com uma sugestão e deixe o autor escolher.

- **Sempre pergunte antes:** regra ou ambiguidade de regra, valor de parâmetro, zona de aceite de requisito, modelo e parâmetros dos bots, critério de métrica, escopo, ordem das fases, estrutura do projeto, dependência nova.
- **Siga sem perguntar:** só o que já foi aprovado e detalhes internos que não mudam comportamento (nomes de funções, organização de arquivos dentro da estrutura aprovada).
- Na dúvida se algo é decisão ou detalhe, pergunte.
- Toda decisão do autor entra em `docs/DIARIO_DE_BORDO.md` com data, opções e escolha.
- Detalhes internos escolhidos sem perguntar também são informados no diário.
- Princípio do autor para qualquer ponto de pontuação: manter a simplicidade.
- As zonas de aceite de `configs/requisitos.yaml` são confirmadas com o autor antes da primeira medição de cada requisito.
- O objetivo das simulações, nas palavras do autor: comparar bots com estilos de jogo diferentes, dizer qual é o melhor estilo e se o jogo está balanceado.
- Nada de assento humano: o simulador é só para muitas partidas entre bots.
- A v1 é linha de base: só é analisada e observada, nunca ajustada.

## Fontes, em ordem de autoridade

0. `regras/`: o texto das regras em Markdown, um arquivo por versão (`v1.md`, `v2.2.md`, `v2.2.1.md`). Enquanto o jogo estiver em ajuste, é aqui que as regras vivem, e não num PDF. A versão atual é a **v2.2.1**. Uma versão já usada em experimento não é mais editada: mudança de regra cria um arquivo novo (ver `regras/README.md`).
1. `docs/Critical_Failure_-_Regras_Completas_2.2.pdf`: origem da v2.2, transcrita em `regras/v2.2.md`. As correções do autor (`COR-nn`) são posteriores ao PDF e valem sobre ele. Tudo reescrito como itens numerados em `docs/especificacao_v2_2.md`; as correções estão na seção "Correções do autor" e em `docs/HISTORICO_REGRAS.md`.
2. `docs/Critical_Failure_Artigo.pdf`: v1 (seções 4.2 a 4.4, Tabelas 2 a 4). Reescrita em `docs/especificacao_v1.md`.
3. `docs/Briefing_Apresentacao_TCC.md`: **só** os slides 5 e 10 a 13. Os slides 6 a 9 são da versão 2.0 e não valem.
4. `docs/prompt_claude_code_simulador.md`: especificação do simulador. As mudanças aprovadas em relação a ele estão no diário (entrada de 2026-11-09).

Não invente regras. Ponto ambíguo ou omisso vai para `docs/AMBIGUIDADES.md` e é perguntado ao autor.

## Convenções

- **Auditoria obrigatória.** Toda partida pode gerar um registro JSONL (`cf-audit/1`) com cabeçalho, eventos e fim. Cada evento separa `publico` de `oculto`, cita a `regra` que o justificou e traz o `estado_hash`. O registro permite refazer a partida.
- **Nenhum número de regra no código.** Todo valor vem do YAML em `configs/`, com o identificador da regra ao lado. Um teste varre o código das regras atrás de números literais.
- **Determinismo.** Mesma configuração e mesma semente geram registro idêntico byte a byte (exceto a data e hora do cabeçalho), em qualquer plataforma. Para isso: aleatoriedade derivada de `SeedSequence(semente, spawn_key=(partida, fluxo, contador))`; fluxo 0 para o jogo e um por bot; nenhum ponto flutuante no estado do motor; sorteios de bot com pesos inteiros; JSON canônico (chaves ordenadas, UTF-8, LF).
- **Motor puro.** `aplicar(estado, acao) -> (novo_estado, eventos)`. O motor valida a ação. Bots só recebem a `Observacao` e nunca tocam no estado.
- **Teste por regra.** Cada identificador de tipo `regra`, `definicao` ou `componente` tem pelo menos um teste marcado com `@pytest.mark.regra("R-x.y")`.
- **Vocabulário em português**, igual ao das regras: ficha, Alerta, Homologação, Backlog, categoria-chave, sistema, mão.
- **Identificadores:** `R-…` (v2.2), `V1-…` (v1), `AMB-nn`, `COR-nn`, `REQ-nn`, `MET-nn`, `VAR-nn`, `MOD-nn`. A convenção está no início de `docs/especificacao_v2_2.md`.
- **Regra impressa continua acessível.** Toda correção do autor fica atrás de uma chave de configuração, para o simulador medir o efeito da mudança. O padrão é sempre a versão corrigida.
- **Código por família de regras, YAML por versão:** `regras/v2/` com `configs/regras_v2_2.yaml`. Uma nova iteração das regras é um YAML novo e uma entrada em `docs/HISTORICO_REGRAS.md`, sem copiar código.
- **Registro do processo.** Atualize `docs/DIARIO_DE_BORDO.md` em toda sessão de trabalho e `docs/HISTORICO_REGRAS.md` em toda mudança de regra ou parâmetro.
- **Experimento oficial só com a árvore do git limpa.** O cabeçalho e o manifest registram o commit e se havia alteração não commitada. Ordem: commit do código, depois `cf experimento --oficial`, depois commit do manifest, do relatório e do diário.
- **Requisitos só recebem veredito quando confirmados.** Em `configs/requisitos.yaml`, `estado: confirmado` e um `criterio` estruturado. Os outros aparecem só como descrição.
- **Git:** um commit por fase, mensagens em português. A identidade do autor está configurada só neste repositório. **Não acrescentar linha de coautoria** (`Co-Authored-By`) nem outra atribuição ao assistente: o único autor é o Erik.

## Fases

| Fase | Entrega | Parada para revisão |
|---|---|---|
| 0 | Especificações, ambiguidades, requisitos, convenções, diário | sim |
| 1 | Núcleo, v2 (2.2 com módulo), auditoria, `replay`, `narrar`, `folha`, bot Aleatório, testes por regra e de propriedades, CI básica | sim |
| 1b | Executor mínimo, manifest, Parquet, primeiras métricas com intervalo de confiança | resumo |
| 2 | Bots e perfis (as variantes foram para a Fase 4; o assento humano saiu do escopo) | resumo |
| 3 | v1 e Experimentos 1 e 2 | sim |
| 4 | Melhor estilo; depois equilíbrio do blefe (exp. 5), variantes do playtest (exp. 6), ablação (exp. 3) e sensibilidade (exp. 4); relatórios | resumo |
| 5 | Metamórficos, fuzzing, mutação, suíte noturna | resumo |

O estado atual está na última entrada do diário.

## Comandos

```
uv sync                                            # instala o ambiente (Python 3.12)
uv run pytest                                      # todos os testes
uv run ruff format . && uv run ruff check .        # formatação e estilo
uv run mypy                                        # tipos, modo estrito, em src/
uv run python scripts/verificar_especificacao.py   # confere especificações, ambiguidades e requisitos
uv run python scripts/matriz_rastreabilidade.py    # regenera docs/MATRIZ_RASTREABILIDADE.md
uv run python scripts/gerar_catalogo.py            # regenera configs/catalogo_v2.yaml da especificação
uv run python scripts/gerar_dourados.py            # regenera tests/dourados e docs/exemplos

uv run cf jogar --semente 1 --log p.jsonl          # joga uma partida e grava o registro
uv run cf replay p.jsonl                           # refaz e confere cada evento
uv run cf narrar p.jsonl                           # conta a partida em português
uv run cf folha p.jsonl                            # exporta a Folha de registro em 3 CSVs
uv run cf experimento experimentos/X.yaml --oficial  # roda um experimento (exige árvore do git limpa)
uv run cf relatorio resultados/X/<execução>        # refaz o relatório a partir do manifest e do Parquet
```

Antes de commitar: `ruff format`, `ruff check`, `mypy`, a matriz regenerada e `pytest`.

Os registros de `tests/dourados/` só são gerados de novo quando a mudança de comportamento é intencional, e o motivo vai para o diário.

## Estrutura do código

```
src/critical_failure/
  nucleo/        erros, JSON canônico e hash, aleatoriedade por contador, catálogo
  regras/
    config.py    modelo e validação do YAML das regras da v2
    familias.py  escolhe o motor pela família declarada no YAML (v1 ou v2)
    v2/          estado, ações, motor e invariantes da família v2
    v1/          configuração, estado, ações, motor, pontuação, observação e invariantes da v1
  observacao.py  o que cada assento vê (lista de AMB-10)
  bots/          contrato, fábrica, Aleatório e os estilos (Construtor, Caçador, Heurístico);
                 mesa pública e Leitor (MOD-03, MOD-04, MOD-08), estimativas por contagem (MOD-09)
  partida.py     laço da partida: motor, bots e ouvinte de eventos
  auditoria/     registro JSONL, replay, narração (v2 e v1) e Folha (só v2)
  duracao.py     modelo de duração da partida (MOD-05), tempos em configs/duracao.yaml
  experimentos/  arquivo de experimento e executor paralelo (Parquet, registros, manifest)
  metricas/      intervalos de confiança, veredito, medida dos requisitos, matriz de estilos
                 (estilo dominante e dinâmica do replicador) e a análise completa de uma execução
  relatorios/    relatório Markdown de cada execução
  cli.py         comando cf
configs/         regras por versão (v2.2, v2.2.1, v1), catálogo gerado, requisitos, modelo de duração, perfis
experimentos/    um YAML por experimento
resultados/      saída dos experimentos; só manifest.json e relatorio.md vão para o git
regras/          texto das regras por versão
tests/           testes por regra, propriedades, convenções e registros de referência
scripts/         verificador, matriz, catálogo e registros de referência
```

Os motores (`regras/v2/` e `regras/v1/`, menos o `config.py` da v1) não podem ter número literal além de 0 e 1; um teste confere. Todo evento do motor cita a regra que o justifica, e todo `regra`, `definicao`, `componente` ou `revogada` da especificação precisa de um teste marcado; outro teste confere.

## Ambiente

- Windows, Python 3.12 (`py -3.12`), `uv` instalado. Sem `gh`.
- A pasta fica dentro do OneDrive: o diretório de resultados deve ser configurável.
- `mutmut` não roda no Windows nativo (precisa de `fork`): na Fase 5, usar o Linux da CI ou Docker.

# Histórico de regras

Registro de cada ajuste de regra ou de parâmetro feito durante o TCC. É a trilha do ciclo de Design Science Research: cada iteração parte de uma versão das regras, mede com o simulador ou com pessoas, e decide o que muda.

Uma linha por mudança. A coluna Evidência aponta para o que motivou a mudança: o `manifest.json` de um experimento, a Folha de registro de uma partida real ou uma análise registrada. Nenhuma mudança entra aqui sem decisão do autor registrada em `docs/DIARIO_DE_BORDO.md`.

Interpretações de regras ambíguas não são mudanças de regra e ficam em `docs/AMBIGUIDADES.md`.

## Versões

| Versão | Data | Origem | Arquivo de configuração |
|---|---|---|---|
| v1 | 2025 | Artigo do SBQS 2025, seção 4.3 e Tabela 3; texto em `regras/v1.md` | `configs/regras_v1.yaml` (Fase 3) |
| v2.2 | 2026-10-17 | `docs/Critical_Failure_-_Regras_Completas_2.2.pdf`; transcrição em `regras/v2.2.md` | `configs/regras_v2_2.yaml` |
| v2.2.1 | 2026-11-09 | v2.2 mais as correções COR-01 e COR-02 e os esclarecimentos AMB-01 a AMB-15; texto em `regras/v2.2.1.md` | `configs/regras_v2_2_1.yaml` |
| v2.2.2 | 2026-11-14 | v2.2.1 mais a recomendação de 4 jogadores (COR-03), que só muda o texto; texto em `regras/v2.2.2.md` | `configs/regras_v2_2_2.yaml` |

A v2.2.2 é a versão atual. As partidas da v2.2.2 são as mesmas da v2.2.1, usada em todos os experimentos das Fases 1b a 5: só o texto e o rótulo mudam. O autor decidiu corrigir a própria 2.2 em vez de abrir uma 2.3 e, ao criar a pasta `regras/`, escolheu dar ao conjunto corrigido o rótulo v2.2.1: continua sendo a 2.2, mas cada conjunto de regras tem um rótulo único. Cada nova rodada de ajustes vira o próximo número (v2.2.2 e assim por diante).

Enquanto as regras estiverem em ajuste, o texto oficial é o Markdown da pasta `regras/`, e não um PDF (decisão do autor em 2026-11-09). O PDF em `docs/` fica como origem da v2.2.

As versões 2.0 e 2.1 são anteriores ao simulador. As mudanças entre elas estão no histórico do próprio PDF 2.2 (p. 31 a 33).

## Mudanças

| Iteração | Data | Correção | Regra ou parâmetro | Antes | Depois | Evidência | Decisão |
|---|---|---|---|---|---|---|---|
| 0 | 2026-11-09 | — | Linha de base | — | Regras do PDF 2.2, sem alteração | — | Ponto de partida do simulador |
| 1 | 2026-11-09 | COR-01 | R-1.2, `jogadores.maximo` | 6 jogadores | 5 jogadores | Análise da especificação, sem simulação: com 6 jogadores a preparação e os 3 Planejamentos pedem 71 cartas e o baralho tem 63 (AMB-06) | Autor: "limite o jogo até 5 jogadores", como correção da própria v2.2 |
| 1 | 2026-11-09 | COR-02 | R-6.9 (nova), R-6.2b (revogada), `alertas.limpeza_no_planejamento` | O Alerta fica até o jogador colocar uma carta da categoria ou até um incidente da categoria | Todos os cubos de Alerta saem no início de cada Planejamento; colocar carta não remove mais Alerta | Nenhuma medição. Decisão do autor ao responder AMB-12; o motivo não foi registrado | Autor: "alertas são zerados na rodada seguinte (próximo planejamento)", confirmada depois de ver as consequências |

| 2 | 2026-11-14 | COR-03 | R-1.2 (texto) | 4 a 5 jogadores, sem recomendação | 4 a 5 jogadores, com 4 recomendado; a contagem não inclui um Auditor externo | `resultados/fase4_exp6_variantes/20261111-004839-cf01dd6/manifest.json`: com 5 jogadores, percentil 90 do tempo parado de 9,0 min por ciclo, contra 5,8 com 4, e mediana de 44 min contra 38 | Autor: "até 5 jogadores com 4 sendo o recomendado (isso não considera o auditor externo)"; versão nova pedida pelo autor, em vez de editar a v2.2.1 |

## Observações sobre a iteração 1

- As duas mudanças foram decididas na Fase 0, antes de existir simulador. A COR-01 nasceu de uma conta feita na leitura das regras; a COR-02 é decisão de projeto do autor.
- Nenhuma das duas tem ainda evidência de simulação. O comportamento impresso continua disponível por configuração justamente para o simulador medir o efeito de cada uma (Experimento 3, ablação).
- Consequências da COR-02 que o autor confirmou: nos ciclos 1 e 2, um Alerta fora da categoria-chave do incidente deixa de custar ao defensor; e os Alertas do ciclo 3 ficam até o fim, custando 1 no Critical Failure, se a categoria for sorteada, e 1 na pontuação final.
- Trechos da v2.2 que a COR-02 tornava obsoletos e que foram reescritos em `regras/v2.2.1.md`, com a marca [COR-02]: o passo 2 e o parágrafo "Teto do sistema" da seção 6, "O Alerta chega antes da Produção" (seção 7.4), a limpeza (seção 8, passo 7), a segunda parte do "Exemplo de dano" (seção 8.1) e a referência rápida (seção 10). A redação é proposta do assistente e aguarda a revisão do autor. A linha "Sem Hotfix" da tabela de parâmetros não foi revista.

## Observações sobre a iteração 2

- A COR-03 não tem chave de configuração: o motor não muda, e uma partida da v2.2.2 é igual, evento por evento, à da v2.2.1 com a mesma semente (há teste). Os resultados dos experimentos com a v2.2.1 valem para a v2.2.2.
- O máximo de 4 jogadores também foi considerado. O autor preferiu manter até 5: como o mínimo é 4, o jogo passaria a ser só para 4.

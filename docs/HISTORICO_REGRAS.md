# Histórico de regras

Registro de cada ajuste de regra ou de parâmetro feito durante o TCC. É a trilha do ciclo de Design Science Research: cada iteração parte de uma versão das regras, mede com o simulador ou com pessoas, e decide o que muda.

Uma linha por mudança. A coluna Evidência aponta para o que motivou a mudança: o `manifest.json` de um experimento, a Folha de registro de uma partida real ou uma análise registrada. Nenhuma mudança entra aqui sem decisão do autor registrada em `docs/DIARIO_DE_BORDO.md`.

Interpretações de regras ambíguas não são mudanças de regra e ficam em `docs/AMBIGUIDADES.md`.

## Versões

| Versão | Data | Origem | Arquivo de configuração |
|---|---|---|---|
| v1 | 2025 | Artigo do SBQS 2025, seção 4.3 e Tabela 3 | `configs/regras_v1.yaml` (Fase 3) |
| v2.2 impressa | 2026-10-17 | `docs/Critical_Failure_-_Regras_Completas_2.2.pdf` | acessível desligando as correções por configuração |
| v2.2 corrigida | 2026-11-09 | PDF 2.2 mais as correções COR-01 e COR-02 | `configs/regras_v2_2.yaml` (Fase 1) |

A v2.2 corrigida é a versão atual. O autor escolheu corrigir a própria v2.2 em vez de abrir uma v2.3; o PDF em `docs/` ainda traz o texto impresso e será atualizado por ele.

As versões 2.0 e 2.1 são anteriores ao simulador. As mudanças entre elas estão no histórico do próprio PDF 2.2 (p. 31 a 33).

## Mudanças

| Iteração | Data | Correção | Regra ou parâmetro | Antes | Depois | Evidência | Decisão |
|---|---|---|---|---|---|---|---|
| 0 | 2026-11-09 | — | Linha de base | — | Regras do PDF 2.2, sem alteração | — | Ponto de partida do simulador |
| 1 | 2026-11-09 | COR-01 | R-1.2, `jogadores.maximo` | 6 jogadores | 5 jogadores | Análise da especificação, sem simulação: com 6 jogadores a preparação e os 3 Planejamentos pedem 71 cartas e o baralho tem 63 (AMB-06) | Autor: "limite o jogo até 5 jogadores", como correção da própria v2.2 |
| 1 | 2026-11-09 | COR-02 | R-6.9 (nova), R-6.2b (revogada), `alertas.limpeza_no_planejamento` | O Alerta fica até o jogador colocar uma carta da categoria ou até um incidente da categoria | Todos os cubos de Alerta saem no início de cada Planejamento; colocar carta não remove mais Alerta | Nenhuma medição. Decisão do autor ao responder AMB-12; o motivo não foi registrado | Autor: "alertas são zerados na rodada seguinte (próximo planejamento)", confirmada depois de ver as consequências |

## Observações sobre a iteração 1

- As duas mudanças foram decididas na Fase 0, antes de existir simulador. A COR-01 nasceu de uma conta feita na leitura das regras; a COR-02 é decisão de projeto do autor.
- Nenhuma das duas tem ainda evidência de simulação. O comportamento impresso continua disponível por configuração justamente para o simulador medir o efeito de cada uma (Experimento 3, ablação).
- Consequências da COR-02 que o autor confirmou: nos ciclos 1 e 2, um Alerta fora da categoria-chave do incidente deixa de custar ao defensor; e os Alertas do ciclo 3 ficam até o fim, custando 1 no Critical Failure, se a categoria for sorteada, e 1 na pontuação final.
- Trechos do PDF que a COR-02 torna obsoletos e que precisam de revisão quando o PDF for atualizado: o parágrafo "Teto do sistema" (p. 6), "O Alerta chega antes da Produção" (p. 8), a segunda parte do "Exemplo de dano" (p. 10) e a linha "Sem Hotfix" da tabela de parâmetros (p. 34).

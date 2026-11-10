# Especificação das regras — Critical Failure v1

**Fonte:** `docs/Critical_Failure_Artigo.pdf` (Oliveira et al., SBQS 2025). As regras estão na seção 4.3 (p. 5 e 6), as cartas na seção 4.2 e na Tabela 3 (p. 5), a pontuação na Tabela 4 (p. 6) e o relato de uso em sala na seção 4.4 (p. 6 e 7).

A v1 é a linha de base do TCC: o simulador precisa reproduzir o desequilíbrio relatado na seção 4.4 antes de comparar com a v2.2. O artigo descreve as regras em prosa e deixa vários pontos em aberto; todos estão em `docs/AMBIGUIDADES.md` (AMB-20 em diante), com a decisão do autor para cada um.

## Como ler

Os identificadores seguem a numeração do artigo: `V1-<seção>.<item>` para o texto e `V1-T<tabela>.<item>` para as tabelas. Uma letra no fim marca a divisão atômica de um mesmo trecho. Os tipos são os mesmos da especificação da v2.2, mais `evidencia`, usado para as observações empíricas da seção 4.4.

Vocabulário em português adotado para a v1: atributo (a cor da carta), teste (o tipo de teste da carta), sistema, mão, falha encontrada, defesa bem-sucedida, declaração, dúvida e contestação.

## Tabela 2 e seção 4.1 — Visão geral

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| V1-T2.1 | componente | O baralho tem 54 cartas. | 4 | `v1.baralho.cartas=54` | V1-T3.1 a V1-T3.18; AMB-21 |
| V1-T2.2 | regra | A partida tem de 3 a 8 jogadores. | 4 | `v1.jogadores.minimo=3`; `v1.jogadores.maximo=8` | AMB-27 |
| V1-T2.3 | nota | O jogo é competitivo e trata de teste não funcional e atributos de qualidade de software. | 4 | — | |
| V1-4.1.1 | definicao | Os 6 atributos de qualidade do jogo são Eficiência de Desempenho, Compatibilidade, Confiabilidade, Segurança, Portabilidade e Usabilidade. | 4 | `v1.atributos=6` | |

## Seção 4.2 — Cartas

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| V1-4.2.1 | definicao | Cada carta de teste tem um atributo de qualidade, identificado pela cor, e um tipo de teste. | 5 | — | AMB-26 |
| V1-4.2.2 | regra | A carta Critical Failure não pode ser usada para construir o sistema de um jogador. | 5 | — | AMB-28 |
| V1-4.2.3 | regra | Usada para testar, a carta Critical Failure causa falha automática: o atacante pega uma carta do sistema testado e a acrescenta ao próprio sistema, sem possibilidade de defesa. | 5 | — | AMB-22; AMB-25; AMB-28 |

### Tabela 3 — Baralho

Quantidades como impressas na Tabela 3 (p. 5), que é o baralho que foi jogado em sala (AMB-21). A tabela tem erros conhecidos, mantidos aqui de propósito: Compatibilidade com 6 cartas, "ScalabilityAvailability" em Confiabilidade e, em Usabilidade, os nomes "Stress" e "Scalability" no lugar de "Accessibility" e "User Error Protection", que são os testes descritos no texto da seção 4.2.

| ID | Atributo | Nome no artigo | Teste na Tabela 3 | Cópias | Pág. | Observação |
|---|---|---|---|---|---|---|
| V1-T3.1 | Eficiência de Desempenho | Performance Efficiency | Load | 3 | 5 | |
| V1-T3.2 | Eficiência de Desempenho | Performance Efficiency | Stress | 3 | 5 | |
| V1-T3.3 | Eficiência de Desempenho | Performance Efficiency | Scalability | 3 | 5 | |
| V1-T3.4 | Compatibilidade | Compatibility | Coexistence | 3 | 5 | |
| V1-T3.5 | Compatibilidade | Compatibility | Interoperability | 3 | 5 | Só 2 testes: o atributo tem 6 cartas |
| V1-T3.6 | Confiabilidade | Reliability | Recovery | 3 | 5 | |
| V1-T3.7 | Confiabilidade | Reliability | Fault Tolerance | 3 | 5 | |
| V1-T3.8 | Confiabilidade | Reliability | ScalabilityAvailability | 3 | 5 | Erro de impressão; no texto da seção 4.2 é Availability |
| V1-T3.9 | Segurança | Security | Confidentiality | 3 | 5 | |
| V1-T3.10 | Segurança | Security | Authentication | 3 | 5 | |
| V1-T3.11 | Segurança | Security | Non-Repudiation | 3 | 5 | |
| V1-T3.12 | Portabilidade | Portability | Adaptability | 3 | 5 | |
| V1-T3.13 | Portabilidade | Portability | Installability | 3 | 5 | |
| V1-T3.14 | Portabilidade | Portability | Replaceability | 3 | 5 | |
| V1-T3.15 | Usabilidade | Usability | A/B | 3 | 5 | |
| V1-T3.16 | Usabilidade | Usability | Stress | 3 | 5 | Nome trocado na tabela |
| V1-T3.17 | Usabilidade | Usability | Scalability | 3 | 5 | Nome trocado na tabela |
| V1-T3.18 | Especial | Special Card | Critical Failure | 3 | 5 | Não tem atributo |

Total: 54 cartas (9 + 6 + 9 + 9 + 9 + 9 + 3).

## Seção 4.3 — Regras

### Preparação

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| V1-4.3.1 | regra | Cada jogador compra do baralho uma mão inicial de 6 cartas. | 6 | `v1.mao_inicial=6` | Evento aleatório do jogo |
| V1-4.3.2 | regra | Define-se a ordem de jogo (por exemplo, sentido horário). | 6 | — | |
| V1-4.3.3 | regra | Cada jogador escolhe 3 das 6 cartas para formar o seu sistema, viradas para baixo. As outras 3 ficam na mão para a fase de testes. | 6 | `v1.sistema_inicial=3`; `v1.cartas_de_teste=3` | AMB-28 |
| V1-4.3.4 | regra | Fase de testes: na sua vez, o jogador faz uma ação de teste e passa a vez ao próximo. | 6 | — | |
| V1-4.3.4a | regra | A fase continua até que todos tenham usado todas as cartas da mão. | 6 | — | |

### Teste

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| V1-4.3.5 | regra | O jogador ativo escolhe uma carta de teste da mão e o sistema de um adversário para testar. | 6 | — | AMB-25; MET-02 |
| V1-4.3.6 | regra | Falha encontrada: se o adversário não tem no sistema uma carta do mesmo atributo da carta de teste, o atacante pega uma carta do sistema do defensor, à sua escolha entre as viradas para baixo, e a acrescenta ao próprio sistema. | 6 | `v1.falha.cartas_tomadas=1` | AMB-22; AMB-23; AMB-25 |
| V1-4.3.7 | regra | Defesa bem-sucedida: se o adversário tem no sistema uma carta do mesmo atributo, o defensor acrescenta a carta de teste do atacante ao próprio sistema. | 6 | — | |

### Blefe e contestação

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| V1-4.3.8 | regra | Declaração: ao ser testado, e antes de qualquer carta ser revelada, o defensor pode declarar se tem ou não uma carta do mesmo atributo. Se disser que tem, pode estar falando a verdade ou blefando. | 6 | — | AMB-20 |
| V1-4.3.9 | regra | Dúvida: o atacante pode duvidar da declaração. Nesse caso, o defensor deve dar a definição de um tipo de teste associado à carta que diz ter. | 6 | — | MOD-07 |
| V1-4.3.10 | regra | Depois de ouvir a definição, o atacante decide se aceita ou se contesta. | 6 | — | MOD-07 |
| V1-4.3.10a | regra | Se o atacante aceita, aplica-se a regra padrão do teste (defesa bem-sucedida ou falha encontrada) conforme a veracidade da declaração. A carta não é revelada. | 6 | `v1.blefe_aceito=declaracao` | Texto do artigo, que é circular. Pela decisão de AMB-20, o simulador aplica a declaração: defesa aceita conta como bem-sucedida, sem verificar |
| V1-4.3.10b | regra | Se o atacante contesta, o defensor revela do sistema a carta que usaria para se defender. | 6 | — | |
| V1-4.3.11 | regra | Contestou, e o defensor falava a verdade: a defesa é bem-sucedida (o defensor fica com a carta de ataque) e, como punição, o defensor pega uma carta do sistema do atacante, à sua escolha e sem ver. | 6 | `v1.contestacao_verdade.cartas_tomadas=1` | AMB-22 |
| V1-4.3.12 | regra | Contestou, e o defensor blefou ou errou: aplica-se a falha encontrada (o atacante pega uma carta do sistema do defensor) e, como recompensa, o atacante pega mais uma carta do sistema do defensor. | 6 | `v1.contestacao_blefe.cartas_extras=1` | AMB-22; AMB-25 |

### Fim da rodada e pontuação

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| V1-4.3.13 | regra | A rodada termina quando todos os jogadores usaram todas as suas cartas de teste. | 6 | — | Igual a V1-4.3.4a |
| V1-4.3.14 | regra | Todos revelam as cartas dos seus sistemas e calculam a pontuação. | 6 | — | |
| V1-4.3.15 | regra | Cada carta no sistema ao fim da rodada vale 1 ponto. | 6 | `v1.pontos.carta=1` | |
| V1-4.3.16 | regra | Um par de cartas do mesmo atributo e de testes diferentes vale 2 pontos de bônus. | 6 | `v1.pontos.par=2` | AMB-24; AMB-26 |
| V1-4.3.17 | regra | Três cartas de atributos diferentes e de testes diferentes valem 2 pontos de bônus. | 6 | `v1.pontos.trio=2` | AMB-24; AMB-26 |
| V1-4.3.18 | regra | É possível pontuar vários pares do mesmo atributo, desde que cada par tenha cartas de testes diferentes. | 6 | — | AMB-24 |
| V1-4.3.19 | regra | Vence a rodada quem tem a maior pontuação total. | 6 | — | AMB-29 |

### Tabela 4 — Pontuação

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| V1-T4.1 | nota | Cada carta individual: +1. | 6 | `v1.pontos.carta=1` | V1-4.3.15 |
| V1-T4.2 | nota | Par de cartas do mesmo atributo e testes diferentes: +2. | 6 | `v1.pontos.par=2` | V1-4.3.16 |
| V1-T4.3 | nota | Três cartas de atributos diferentes e testes diferentes: +2. | 6 | `v1.pontos.trio=2` | V1-4.3.17 |

## Seção 4.4 — Aplicação em sala

Observações que o simulador deve tentar reproduzir (Experimento 1). São evidência, não regra.

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| V1-4.4.1 | evidencia | A turma foi organizada em grupos de cerca de 6 alunos. | 6 | — | AMB-27 |
| V1-4.4.2 | evidencia | Cada grupo jogou 2 rodadas consecutivas, num total de 6 partidas completas. | 6 | — | AMB-27 |
| V1-4.4.3 | evidencia | Das 6 partidas, 4 foram vencidas por jogadores com pontuação significativamente maior que a dos outros. | 7 | — | MET-01 |
| V1-4.4.4 | evidencia | O projeto supunha que os jogadores atacariam os mais fortes (os que têm mais cartas no sistema), mas eles atacaram com frequência os mais fracos, por acharem que teriam menos chance de se defender. | 7 | — | MET-02 |
| V1-4.4.5 | evidencia | Com isso, os jogadores dominantes seguiam com pouca oposição: quem lidera ganha uma vantagem que se acumula. | 7 | — | REQ-02 |
| V1-4.4.6 | evidencia | As regras confundiram os jogadores de primeira viagem, sobretudo a diferença entre as cartas do sistema e as da mão, e a pontuação. | 7 | — | Fora do simulador |

## Diferenças de estrutura em relação à v2.2

Para o núcleo comum do motor (Fase 1) servir às duas versões, estas diferenças precisam caber no mesmo modelo de estado:

- Na v1 as cartas **mudam de dono**: saem do sistema de um jogador para o de outro, e a carta de ataque pode ir para o sistema do defensor. Na v2.2 nenhuma carta troca de jogador.
- Na v1 não há fichas, Alertas, Backlog, Radar, incidentes, Auditor nem ciclos: há uma preparação e uma única fase de testes.
- Na v1 o sistema não tem teto e a pontuação vem só das cartas do sistema ao fim.
- Na v1 a carta Critical Failure é uma carta de ataque na mão; na v2.2 é o evento final.

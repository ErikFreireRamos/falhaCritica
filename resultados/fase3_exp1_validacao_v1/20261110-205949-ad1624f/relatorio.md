# Relatório do experimento `fase3_exp1_validacao_v1`

Validação da v1 com mesas de 6. Matriz 3 x 3 de política de alvo (um Caçador foco contra cinco Caçadores com outra política, com rodízio de assentos) e proporção de partidas desequilibradas em populações de bots idênticos e numa mesa mista.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase3_exp1_validacao_v1.yaml` |
| Commit | `ad1624f` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261112 |
| Partidas | 85000 |
| Falhas | 0 |
| Registros completos gravados | 85 |
| Início | 2026-11-10T20:59:49+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-09: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 85000 | passa |

Nota: o critério pede pelo menos 50000 partidas.

## Taxa de vitória por bot (MET-07)

Sem veredito: a métrica aguarda a confirmação do autor. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| alvo_aleatorio_contra_lider | foco | 6 | 6000 | 0,184 | 0,175 a 0,193 | 0,167 |
| alvo_aleatorio_contra_lider | outros | 6 | 30000 | 0,163 | 0,159 a 0,167 | 0,167 |
| alvo_aleatorio_contra_mais_fraco | foco | 6 | 6000 | 0,286 | 0,275 a 0,297 | 0,167 |
| alvo_aleatorio_contra_mais_fraco | outros | 6 | 30000 | 0,143 | 0,139 a 0,147 | 0,167 |
| alvo_lider_contra_aleatorio | outros | 6 | 30000 | 0,173 | 0,169 a 0,177 | 0,167 |
| alvo_lider_contra_aleatorio | foco | 6 | 6000 | 0,134 | 0,126 a 0,143 | 0,167 |
| alvo_lider_contra_mais_fraco | foco | 6 | 6000 | 0,233 | 0,224 a 0,243 | 0,167 |
| alvo_lider_contra_mais_fraco | outros | 6 | 30000 | 0,153 | 0,149 a 0,157 | 0,167 |
| alvo_mais_fraco_contra_aleatorio | outros | 6 | 30000 | 0,173 | 0,169 a 0,178 | 0,167 |
| alvo_mais_fraco_contra_aleatorio | foco | 6 | 6000 | 0,134 | 0,126 a 0,142 | 0,167 |
| alvo_mais_fraco_contra_lider | foco | 6 | 6000 | 0,179 | 0,168 a 0,189 | 0,167 |
| alvo_mais_fraco_contra_lider | outros | 6 | 30000 | 0,164 | 0,160 a 0,168 | 0,167 |
| estilos_mistos | heuristico | 6 | 6000 | 0,220 | 0,210 a 0,230 | 0,167 |
| estilos_mistos | construtor | 6 | 6000 | 0,214 | 0,203 a 0,224 | 0,167 |
| estilos_mistos | cacador (aleatorio) | 6 | 6000 | 0,189 | 0,180 a 0,199 | 0,167 |
| estilos_mistos | cacador (mais_fraco) | 6 | 6000 | 0,182 | 0,172 a 0,191 | 0,167 |
| estilos_mistos | cacador (lider) | 6 | 6000 | 0,166 | 0,157 a 0,175 | 0,167 |
| estilos_mistos | aleatorio | 6 | 6000 | 0,029 | 0,026 a 0,034 | 0,167 |

## Política de alvo (MET-02)

Sem veredito. Taxa de vitória de 1 bot (o foco) que usa a política da linha, numa mesa em que todos os outros usam a política da coluna. Rodízio de assentos. Referência de quem não leva vantagem: 1/N.

| Foco \ Outros | lider | mais_fraco | aleatorio |
|---|---|---|---|
| lider | — | 0,233 (0,224 a 0,243) | 0,134 (0,126 a 0,143) |
| mais_fraco | 0,179 (0,168 a 0,189) | — | 0,134 (0,126 a 0,142) |
| aleatorio | 0,184 (0,175 a 0,193) | 0,286 (0,275 a 0,297) | — |

Referência 1/N: 0,167.

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| alvo_lider_contra_lider | v1 | 6 | 6000 | **1,50** | 0,993 | 0,991 a 0,995 |
| alvo_lider_contra_lider | v1 | 6 | 6000 | 1,25 | 0,998 | 0,997 a 0,999 |
| alvo_lider_contra_lider | v1 | 6 | 6000 | 2,00 | 0,960 | 0,955 a 0,965 |
| alvo_lider_contra_mais_fraco | v1 | 6 | 6000 | **1,50** | 0,987 | 0,984 a 0,990 |
| alvo_lider_contra_mais_fraco | v1 | 6 | 6000 | 1,25 | 0,998 | 0,997 a 0,999 |
| alvo_lider_contra_mais_fraco | v1 | 6 | 6000 | 2,00 | 0,876 | 0,867 a 0,884 |
| alvo_lider_contra_aleatorio | v1 | 6 | 6000 | **1,50** | 0,999 | 0,998 a 1,000 |
| alvo_lider_contra_aleatorio | v1 | 6 | 6000 | 1,25 | 1,000 | 0,999 a 1,000 |
| alvo_lider_contra_aleatorio | v1 | 6 | 6000 | 2,00 | 0,961 | 0,956 a 0,966 |
| alvo_mais_fraco_contra_lider | v1 | 6 | 6000 | **1,50** | 0,996 | 0,994 a 0,997 |
| alvo_mais_fraco_contra_lider | v1 | 6 | 6000 | 1,25 | 1,000 | 0,999 a 1,000 |
| alvo_mais_fraco_contra_lider | v1 | 6 | 6000 | 2,00 | 0,959 | 0,953 a 0,963 |
| alvo_mais_fraco_contra_mais_fraco | v1 | 6 | 6000 | **1,50** | 0,955 | 0,949 a 0,960 |
| alvo_mais_fraco_contra_mais_fraco | v1 | 6 | 6000 | 1,25 | 0,997 | 0,995 a 0,998 |
| alvo_mais_fraco_contra_mais_fraco | v1 | 6 | 6000 | 2,00 | 0,639 | 0,627 a 0,651 |
| alvo_mais_fraco_contra_aleatorio | v1 | 6 | 6000 | **1,50** | 0,998 | 0,997 a 0,999 |
| alvo_mais_fraco_contra_aleatorio | v1 | 6 | 6000 | 1,25 | 1,000 | 0,999 a 1,000 |
| alvo_mais_fraco_contra_aleatorio | v1 | 6 | 6000 | 2,00 | 0,952 | 0,947 a 0,957 |
| alvo_aleatorio_contra_lider | v1 | 6 | 6000 | **1,50** | 0,995 | 0,993 a 0,997 |
| alvo_aleatorio_contra_lider | v1 | 6 | 6000 | 1,25 | 0,999 | 0,998 a 1,000 |
| alvo_aleatorio_contra_lider | v1 | 6 | 6000 | 2,00 | 0,963 | 0,958 a 0,967 |
| alvo_aleatorio_contra_mais_fraco | v1 | 6 | 6000 | **1,50** | 0,989 | 0,986 a 0,991 |
| alvo_aleatorio_contra_mais_fraco | v1 | 6 | 6000 | 1,25 | 1,000 | 0,999 a 1,000 |
| alvo_aleatorio_contra_mais_fraco | v1 | 6 | 6000 | 2,00 | 0,819 | 0,809 a 0,828 |
| alvo_aleatorio_contra_aleatorio | v1 | 6 | 6000 | **1,50** | 0,999 | 0,998 a 1,000 |
| alvo_aleatorio_contra_aleatorio | v1 | 6 | 6000 | 1,25 | 1,000 | 0,999 a 1,000 |
| alvo_aleatorio_contra_aleatorio | v1 | 6 | 6000 | 2,00 | 0,963 | 0,958 a 0,967 |
| todos_aleatorios | v1 | 6 | 5000 | **1,50** | 0,958 | 0,953 a 0,964 |
| todos_aleatorios | v1 | 6 | 5000 | 1,25 | 0,997 | 0,996 a 0,998 |
| todos_aleatorios | v1 | 6 | 5000 | 2,00 | 0,663 | 0,650 a 0,676 |
| todos_construtores | v1 | 6 | 5000 | **1,50** | 0,998 | 0,997 a 0,999 |
| todos_construtores | v1 | 6 | 5000 | 1,25 | 1,000 | 0,999 a 1,000 |
| todos_construtores | v1 | 6 | 5000 | 2,00 | 0,964 | 0,959 a 0,969 |
| todos_cacadores_lider | v1 | 6 | 5000 | **1,50** | 0,991 | 0,988 a 0,994 |
| todos_cacadores_lider | v1 | 6 | 5000 | 1,25 | 0,999 | 0,997 a 0,999 |
| todos_cacadores_lider | v1 | 6 | 5000 | 2,00 | 0,960 | 0,954 a 0,965 |
| todos_cacadores_mais_fraco | v1 | 6 | 5000 | **1,50** | 0,957 | 0,951 a 0,963 |
| todos_cacadores_mais_fraco | v1 | 6 | 5000 | 1,25 | 0,999 | 0,998 a 1,000 |
| todos_cacadores_mais_fraco | v1 | 6 | 5000 | 2,00 | 0,622 | 0,609 a 0,636 |
| todos_heuristicos | v1 | 6 | 5000 | **1,50** | 0,999 | 0,998 a 1,000 |
| todos_heuristicos | v1 | 6 | 5000 | 1,25 | 1,000 | 0,999 a 1,000 |
| todos_heuristicos | v1 | 6 | 5000 | 2,00 | 0,960 | 0,954 a 0,965 |
| estilos_mistos | v1 | 6 | 6000 | **1,50** | 0,998 | 0,996 a 0,999 |
| estilos_mistos | v1 | 6 | 6000 | 1,25 | 1,000 | 0,999 a 1,000 |
| estilos_mistos | v1 | 6 | 6000 | 2,00 | 0,945 | 0,938 a 0,950 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| alvo_lider_contra_lider_r0 | 1000 | 0 | 18,0 | 6,5 | 1,9% | 0,0% | 0,0% | 0,615 | 27,2 | 8,1 | — |
| alvo_lider_contra_lider_r1 | 1000 | 0 | 18,0 | 6,5 | 1,9% | 0,0% | 0,0% | 0,615 | 27,2 | 8,1 | — |
| alvo_lider_contra_lider_r2 | 1000 | 0 | 18,0 | 6,5 | 1,9% | 0,0% | 0,0% | 0,615 | 27,2 | 8,1 | — |
| alvo_lider_contra_lider_r3 | 1000 | 0 | 18,0 | 6,5 | 1,9% | 0,0% | 0,0% | 0,615 | 27,2 | 8,1 | — |
| alvo_lider_contra_lider_r4 | 1000 | 0 | 18,0 | 6,5 | 1,9% | 0,0% | 0,0% | 0,615 | 27,2 | 8,1 | — |
| alvo_lider_contra_lider_r5 | 1000 | 0 | 18,0 | 6,5 | 1,9% | 0,0% | 0,0% | 0,615 | 27,2 | 8,1 | — |
| alvo_lider_contra_mais_fraco_r0 | 1000 | 0 | 18,0 | 9,0 | 7,4% | 0,0% | 0,0% | 0,329 | 11,9 | 5,6 | — |
| alvo_lider_contra_mais_fraco_r1 | 1000 | 0 | 18,0 | 9,0 | 8,0% | 0,0% | 0,0% | 0,555 | 12,9 | 5,7 | — |
| alvo_lider_contra_mais_fraco_r2 | 1000 | 0 | 18,0 | 9,0 | 6,6% | 0,0% | 0,0% | 0,508 | 12,7 | 5,7 | — |
| alvo_lider_contra_mais_fraco_r3 | 1000 | 0 | 18,0 | 9,0 | 7,2% | 0,0% | 0,0% | 0,524 | 12,8 | 5,7 | — |
| alvo_lider_contra_mais_fraco_r4 | 1000 | 0 | 18,0 | 9,0 | 7,6% | 0,0% | 0,0% | 0,488 | 12,7 | 5,7 | — |
| alvo_lider_contra_mais_fraco_r5 | 1000 | 0 | 18,0 | 9,1 | 6,6% | 0,0% | 0,0% | 0,477 | 13,0 | 5,7 | — |
| alvo_lider_contra_aleatorio_r0 | 1000 | 0 | 18,0 | 9,5 | 7,8% | 0,0% | 0,0% | 0,415 | 17,8 | 7,0 | — |
| alvo_lider_contra_aleatorio_r1 | 1000 | 0 | 18,0 | 9,2 | 4,9% | 0,0% | 0,0% | 0,448 | 18,5 | 7,0 | — |
| alvo_lider_contra_aleatorio_r2 | 1000 | 0 | 18,0 | 9,2 | 6,8% | 0,0% | 0,0% | 0,452 | 18,4 | 7,0 | — |
| alvo_lider_contra_aleatorio_r3 | 1000 | 0 | 18,0 | 9,3 | 6,7% | 0,0% | 0,0% | 0,428 | 18,5 | 7,0 | — |
| alvo_lider_contra_aleatorio_r4 | 1000 | 0 | 18,0 | 9,3 | 5,6% | 0,0% | 0,0% | 0,413 | 18,2 | 7,0 | — |
| alvo_lider_contra_aleatorio_r5 | 1000 | 0 | 18,0 | 9,3 | 7,0% | 0,0% | 0,0% | 0,413 | 18,2 | 7,0 | — |
| alvo_mais_fraco_contra_lider_r0 | 1000 | 0 | 18,0 | 6,9 | 1,5% | 0,0% | 0,0% | 0,595 | 25,6 | 7,9 | — |
| alvo_mais_fraco_contra_lider_r1 | 1000 | 0 | 18,0 | 7,5 | 2,7% | 0,0% | 0,0% | 0,588 | 23,9 | 7,7 | — |
| alvo_mais_fraco_contra_lider_r2 | 1000 | 0 | 18,0 | 7,4 | 1,2% | 0,0% | 0,0% | 0,585 | 24,2 | 7,7 | — |
| alvo_mais_fraco_contra_lider_r3 | 1000 | 0 | 18,0 | 7,2 | 1,7% | 0,0% | 0,0% | 0,564 | 23,8 | 7,7 | — |
| alvo_mais_fraco_contra_lider_r4 | 1000 | 0 | 18,0 | 7,3 | 1,6% | 0,0% | 0,0% | 0,542 | 23,7 | 7,7 | — |
| alvo_mais_fraco_contra_lider_r5 | 1000 | 0 | 18,0 | 7,2 | 3,0% | 0,0% | 0,0% | 0,565 | 23,6 | 7,7 | — |
| alvo_mais_fraco_contra_mais_fraco_r0 | 1000 | 0 | 18,0 | 8,9 | 20,9% | 0,0% | 0,0% | 0,536 | 9,6 | 5,3 | — |
| alvo_mais_fraco_contra_mais_fraco_r1 | 1000 | 0 | 18,0 | 8,9 | 20,9% | 0,0% | 0,0% | 0,536 | 9,6 | 5,3 | — |
| alvo_mais_fraco_contra_mais_fraco_r2 | 1000 | 0 | 18,0 | 8,9 | 20,9% | 0,0% | 0,0% | 0,536 | 9,6 | 5,3 | — |
| alvo_mais_fraco_contra_mais_fraco_r3 | 1000 | 0 | 18,0 | 8,9 | 20,9% | 0,0% | 0,0% | 0,536 | 9,6 | 5,3 | — |
| alvo_mais_fraco_contra_mais_fraco_r4 | 1000 | 0 | 18,0 | 8,9 | 20,9% | 0,0% | 0,0% | 0,536 | 9,6 | 5,3 | — |
| alvo_mais_fraco_contra_mais_fraco_r5 | 1000 | 0 | 18,0 | 8,9 | 20,9% | 0,0% | 0,0% | 0,536 | 9,6 | 5,3 | — |
| alvo_mais_fraco_contra_aleatorio_r0 | 1000 | 0 | 18,0 | 9,6 | 10,1% | 0,0% | 0,0% | 0,414 | 16,2 | 6,6 | — |
| alvo_mais_fraco_contra_aleatorio_r1 | 1000 | 0 | 18,0 | 9,6 | 10,9% | 0,0% | 0,0% | 0,372 | 15,8 | 6,5 | — |
| alvo_mais_fraco_contra_aleatorio_r2 | 1000 | 0 | 18,0 | 9,6 | 11,0% | 0,0% | 0,0% | 0,363 | 15,8 | 6,5 | — |
| alvo_mais_fraco_contra_aleatorio_r3 | 1000 | 0 | 18,0 | 9,6 | 10,1% | 0,0% | 0,0% | 0,382 | 15,8 | 6,5 | — |
| alvo_mais_fraco_contra_aleatorio_r4 | 1000 | 0 | 18,0 | 9,7 | 11,6% | 0,0% | 0,0% | 0,387 | 15,8 | 6,5 | — |
| alvo_mais_fraco_contra_aleatorio_r5 | 1000 | 0 | 18,0 | 9,6 | 10,0% | 0,0% | 0,0% | 0,381 | 15,8 | 6,5 | — |
| alvo_aleatorio_contra_lider_r0 | 1000 | 0 | 18,0 | 6,9 | 1,9% | 0,0% | 0,0% | 0,576 | 26,0 | 8,0 | — |
| alvo_aleatorio_contra_lider_r1 | 1000 | 0 | 18,0 | 7,4 | 2,3% | 0,0% | 0,0% | 0,566 | 24,8 | 7,9 | — |
| alvo_aleatorio_contra_lider_r2 | 1000 | 0 | 18,0 | 7,3 | 2,7% | 0,0% | 0,0% | 0,584 | 25,3 | 7,9 | — |
| alvo_aleatorio_contra_lider_r3 | 1000 | 0 | 18,0 | 7,2 | 2,6% | 0,0% | 0,0% | 0,571 | 24,8 | 7,9 | — |
| alvo_aleatorio_contra_lider_r4 | 1000 | 0 | 18,0 | 7,1 | 1,7% | 0,0% | 0,0% | 0,571 | 25,1 | 7,9 | — |
| alvo_aleatorio_contra_lider_r5 | 1000 | 0 | 18,0 | 7,0 | 2,9% | 0,0% | 0,0% | 0,549 | 24,8 | 7,9 | — |
| alvo_aleatorio_contra_mais_fraco_r0 | 1000 | 0 | 18,0 | 9,0 | 16,9% | 0,0% | 0,0% | 0,388 | 11,0 | 5,4 | — |
| alvo_aleatorio_contra_mais_fraco_r1 | 1000 | 0 | 18,0 | 9,0 | 17,8% | 0,0% | 0,0% | 0,453 | 11,2 | 5,5 | — |
| alvo_aleatorio_contra_mais_fraco_r2 | 1000 | 0 | 18,0 | 9,1 | 16,9% | 0,0% | 0,0% | 0,441 | 11,2 | 5,5 | — |
| alvo_aleatorio_contra_mais_fraco_r3 | 1000 | 0 | 18,0 | 9,0 | 16,7% | 0,0% | 0,0% | 0,437 | 11,2 | 5,5 | — |
| alvo_aleatorio_contra_mais_fraco_r4 | 1000 | 0 | 18,0 | 9,0 | 15,5% | 0,0% | 0,0% | 0,453 | 11,2 | 5,5 | — |
| alvo_aleatorio_contra_mais_fraco_r5 | 1000 | 0 | 18,0 | 9,1 | 16,4% | 0,0% | 0,0% | 0,429 | 11,2 | 5,5 | — |
| alvo_aleatorio_contra_aleatorio_r0 | 1000 | 0 | 18,0 | 9,7 | 9,4% | 0,0% | 0,0% | 0,380 | 16,9 | 6,8 | — |
| alvo_aleatorio_contra_aleatorio_r1 | 1000 | 0 | 18,0 | 9,7 | 9,4% | 0,0% | 0,0% | 0,380 | 16,9 | 6,8 | — |
| alvo_aleatorio_contra_aleatorio_r2 | 1000 | 0 | 18,0 | 9,7 | 9,4% | 0,0% | 0,0% | 0,380 | 16,9 | 6,8 | — |
| alvo_aleatorio_contra_aleatorio_r3 | 1000 | 0 | 18,0 | 9,7 | 9,4% | 0,0% | 0,0% | 0,380 | 16,9 | 6,8 | — |
| alvo_aleatorio_contra_aleatorio_r4 | 1000 | 0 | 18,0 | 9,7 | 9,4% | 0,0% | 0,0% | 0,380 | 16,9 | 6,8 | — |
| alvo_aleatorio_contra_aleatorio_r5 | 1000 | 0 | 18,0 | 9,7 | 9,4% | 0,0% | 0,0% | 0,380 | 16,9 | 6,8 | — |
| todos_aleatorios | 5000 | 0 | 18,0 | 2,0 | 17,6% | 0,0% | 0,0% | 0,321 | 12,7 | 6,7 | — |
| todos_construtores | 5000 | 0 | 18,0 | 9,6 | 10,0% | 0,0% | 0,0% | 0,407 | 17,0 | 6,8 | — |
| todos_cacadores_lider | 5000 | 0 | 18,0 | 6,5 | 1,7% | 0,0% | 0,0% | 0,600 | 27,0 | 8,1 | — |
| todos_cacadores_mais_fraco | 5000 | 0 | 18,0 | 8,9 | 21,7% | 0,0% | 0,0% | 0,554 | 9,6 | 5,3 | — |
| todos_heuristicos | 5000 | 0 | 18,0 | 10,1 | 10,7% | 0,0% | 0,0% | 0,349 | 16,1 | 6,7 | — |
| estilos_mistos_r0 | 1000 | 0 | 18,0 | 8,0 | 6,8% | 0,0% | 0,0% | 0,434 | 16,8 | 6,8 | — |
| estilos_mistos_r1 | 1000 | 0 | 18,0 | 8,1 | 8,0% | 0,0% | 0,0% | 0,440 | 16,9 | 6,8 | — |
| estilos_mistos_r2 | 1000 | 0 | 18,0 | 8,2 | 6,9% | 0,0% | 0,0% | 0,385 | 16,4 | 6,7 | — |
| estilos_mistos_r3 | 1000 | 0 | 18,0 | 7,9 | 5,2% | 0,0% | 0,0% | 0,450 | 17,7 | 6,9 | — |
| estilos_mistos_r4 | 1000 | 0 | 18,0 | 7,9 | 6,1% | 0,0% | 0,0% | 0,442 | 17,0 | 6,8 | — |
| estilos_mistos_r5 | 1000 | 0 | 18,0 | 7,9 | 6,2% | 0,0% | 0,0% | 0,436 | 17,2 | 6,8 | — |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| alvo_lider_contra_lider_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_lider_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_lider_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_lider_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_lider_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_lider_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_mais_fraco_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_mais_fraco_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_mais_fraco_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_mais_fraco_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_mais_fraco_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_mais_fraco_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_aleatorio_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_aleatorio_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_aleatorio_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_aleatorio_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_aleatorio_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_lider_contra_aleatorio_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_lider_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_lider_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_lider_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_lider_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_lider_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_lider_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_mais_fraco_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_mais_fraco_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_mais_fraco_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_mais_fraco_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_mais_fraco_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_mais_fraco_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_aleatorio_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_aleatorio_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_aleatorio_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_aleatorio_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_aleatorio_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_mais_fraco_contra_aleatorio_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_lider_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_lider_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_lider_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_lider_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_lider_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_lider_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_mais_fraco_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_mais_fraco_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_mais_fraco_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_mais_fraco_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_mais_fraco_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_mais_fraco_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_aleatorio_r0 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_aleatorio_r1 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_aleatorio_r2 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_aleatorio_r3 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_aleatorio_r4 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:fbc5495d99cf` |
| alvo_aleatorio_contra_aleatorio_r5 | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:fbc5495d99cf` |
| todos_aleatorios | v1 | 6 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95} | `sha256:fbc5495d99cf` |
| todos_construtores | v1 | 6 | construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| todos_cacadores_lider | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:fbc5495d99cf` |
| todos_cacadores_mais_fraco | v1 | 6 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:fbc5495d99cf` |
| todos_heuristicos | v1 | 6 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| estilos_mistos_r0 | v1 | 6 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| estilos_mistos_r1 | v1 | 6 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| estilos_mistos_r2 | v1 | 6 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| estilos_mistos_r3 | v1 | 6 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| estilos_mistos_r4 | v1 | 6 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| estilos_mistos_r5 | v1 | 6 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |

## Como refazer

No commit `ad1624f`: `cf experimento experimentos/fase3_exp1_validacao_v1.yaml --oficial --processos 4`. O resultado não depende do número de processos.

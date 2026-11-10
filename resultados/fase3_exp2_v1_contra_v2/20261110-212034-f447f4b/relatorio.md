# Relatório do experimento `fase3_exp2_v1_contra_v2`

v1 contra v2.2.1 em mesas mistas de 4 e 5 jogadores, com os mesmos estilos (Aleatório, Construtor, Caçador e Heurístico; com 5 jogadores, dois Caçadores), todos experientes, blefe moderado e contestação pelo limiar. Mede a vantagem do líder (REQ-02), as partidas desequilibradas (MET-01) e a vitória por estilo (MET-07).

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase3_exp2_v1_contra_v2.yaml` |
| Commit | `f447f4b` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261113 |
| Partidas | 40000 |
| Falhas | 0 |
| Registros completos gravados | 44 |
| Início | 2026-11-10T21:20:34+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-02: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| v2_2_1_com_4_jogadores | vantagem do líder em v1_com_4_jogadores menos a vantagem em v2_2_1_com_4_jogadores | 0,305 | 0,290 a 0,319 | 0,050 a 1,000 | 16593 | passa |
| v2_2_1_com_5_jogadores | vantagem do líder em v1_com_5_jogadores menos a vantagem em v2_2_1_com_5_jogadores | 0,328 | 0,316 a 0,342 | 0,050 a 1,000 | 16036 | passa |

Nota: vantagem do líder: v1_com_4_jogadores 0.392 (8262 partidas com líder isolado); v2_2_1_com_4_jogadores 0.087 (8331 partidas).
Nota: vantagem do líder: v1_com_5_jogadores 0.419 (7800 partidas com líder isolado); v2_2_1_com_5_jogadores 0.091 (8236 partidas).

### REQ-09: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 40000 | inconclusivo |

Nota: o critério pede pelo menos 50000 partidas.

## Taxa de vitória por bot (MET-07)

Sem veredito: a métrica aguarda a confirmação do autor. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| v1_com_4_jogadores | heuristico | 4 | 10000 | 0,354 | 0,345 a 0,363 | 0,250 |
| v1_com_4_jogadores | construtor | 4 | 10000 | 0,323 | 0,314 a 0,332 | 0,250 |
| v1_com_4_jogadores | cacador (lider) | 4 | 10000 | 0,260 | 0,252 a 0,269 | 0,250 |
| v1_com_4_jogadores | aleatorio | 4 | 10000 | 0,063 | 0,058 a 0,068 | 0,250 |
| v1_com_5_jogadores | heuristico | 5 | 10000 | 0,262 | 0,254 a 0,271 | 0,200 |
| v1_com_5_jogadores | construtor | 5 | 10000 | 0,259 | 0,251 a 0,268 | 0,200 |
| v1_com_5_jogadores | cacador (mais_fraco) | 5 | 10000 | 0,233 | 0,225 a 0,241 | 0,200 |
| v1_com_5_jogadores | cacador (lider) | 5 | 10000 | 0,200 | 0,193 a 0,208 | 0,200 |
| v1_com_5_jogadores | aleatorio | 5 | 10000 | 0,045 | 0,041 a 0,049 | 0,200 |
| v2_2_1_com_4_jogadores | construtor | 4 | 10000 | 0,455 | 0,445 a 0,464 | 0,250 |
| v2_2_1_com_4_jogadores | heuristico | 4 | 10000 | 0,370 | 0,360 a 0,379 | 0,250 |
| v2_2_1_com_4_jogadores | cacador (lider) | 4 | 10000 | 0,173 | 0,165 a 0,180 | 0,250 |
| v2_2_1_com_4_jogadores | aleatorio | 4 | 10000 | 0,003 | 0,002 a 0,004 | 0,250 |
| v2_2_1_com_5_jogadores | construtor | 5 | 10000 | 0,349 | 0,340 a 0,358 | 0,200 |
| v2_2_1_com_5_jogadores | heuristico | 5 | 10000 | 0,331 | 0,322 a 0,340 | 0,200 |
| v2_2_1_com_5_jogadores | cacador (lider) | 5 | 10000 | 0,173 | 0,165 a 0,180 | 0,200 |
| v2_2_1_com_5_jogadores | cacador (mais_fraco) | 5 | 10000 | 0,146 | 0,139 a 0,153 | 0,200 |
| v2_2_1_com_5_jogadores | aleatorio | 5 | 10000 | 0,001 | 0,001 a 0,002 | 0,200 |

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| v1_com_4_jogadores | v1 | 4 | 10000 | **1,50** | 0,991 | 0,989 a 0,993 |
| v1_com_4_jogadores | v1 | 4 | 10000 | 1,25 | 0,998 | 0,997 a 0,999 |
| v1_com_4_jogadores | v1 | 4 | 10000 | 2,00 | 0,921 | 0,915 a 0,926 |
| v2_2_1_com_4_jogadores | v2 | 4 | 10000 | **1,50** | 0,928 | 0,923 a 0,933 |
| v2_2_1_com_4_jogadores | v2 | 4 | 10000 | 1,25 | 0,994 | 0,993 a 0,996 |
| v2_2_1_com_4_jogadores | v2 | 4 | 10000 | 2,00 | 0,553 | 0,543 a 0,562 |
| v1_com_5_jogadores | v1 | 5 | 10000 | **1,50** | 0,996 | 0,994 a 0,997 |
| v1_com_5_jogadores | v1 | 5 | 10000 | 1,25 | 1,000 | 0,999 a 1,000 |
| v1_com_5_jogadores | v1 | 5 | 10000 | 2,00 | 0,937 | 0,932 a 0,942 |
| v2_2_1_com_5_jogadores | v2 | 5 | 10000 | **1,50** | 0,943 | 0,938 a 0,947 |
| v2_2_1_com_5_jogadores | v2 | 5 | 10000 | 1,25 | 0,998 | 0,997 a 0,999 |
| v2_2_1_com_5_jogadores | v2 | 5 | 10000 | 2,00 | 0,532 | 0,522 a 0,542 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v1_com_4_jogadores_r0 | 2500 | 0 | 12,0 | 5,0 | 6,0% | 0,0% | 0,0% | 0,380 | 16,0 | 7,1 | — |
| v1_com_4_jogadores_r1 | 2500 | 0 | 12,0 | 5,1 | 6,2% | 0,0% | 0,0% | 0,401 | 16,3 | 7,0 | — |
| v1_com_4_jogadores_r2 | 2500 | 0 | 12,0 | 5,0 | 5,7% | 0,0% | 0,0% | 0,373 | 15,9 | 7,0 | — |
| v1_com_4_jogadores_r3 | 2500 | 0 | 12,0 | 4,9 | 5,2% | 0,0% | 0,0% | 0,413 | 16,4 | 7,1 | — |
| v2_2_1_com_4_jogadores_r0 | 2500 | 0 | 25,0 | 9,5 | 1,2% | 0,0% | 0,0% | 0,068 | 14,0 | 8,4 | 42,5 / 45,7 / 48,8 |
| v2_2_1_com_4_jogadores_r1 | 2500 | 0 | 25,2 | 9,5 | 1,4% | 0,0% | 0,0% | 0,098 | 13,9 | 8,5 | 42,7 / 45,9 / 49,1 |
| v2_2_1_com_4_jogadores_r2 | 2500 | 0 | 24,8 | 9,4 | 1,1% | 0,0% | 0,0% | 0,094 | 13,8 | 8,4 | 42,3 / 45,6 / 48,7 |
| v2_2_1_com_4_jogadores_r3 | 2500 | 0 | 24,7 | 9,4 | 1,3% | 0,0% | 0,0% | 0,089 | 14,0 | 8,5 | 42,2 / 45,5 / 48,3 |
| v1_com_5_jogadores_r0 | 2000 | 0 | 15,0 | 6,5 | 7,2% | 0,0% | 0,0% | 0,424 | 16,1 | 6,8 | — |
| v1_com_5_jogadores_r1 | 2000 | 0 | 15,0 | 6,6 | 7,5% | 0,0% | 0,0% | 0,430 | 16,1 | 6,8 | — |
| v1_com_5_jogadores_r2 | 2000 | 0 | 15,0 | 6,6 | 8,1% | 0,0% | 0,0% | 0,374 | 15,8 | 6,8 | — |
| v1_com_5_jogadores_r3 | 2000 | 0 | 15,0 | 6,4 | 6,1% | 0,0% | 0,0% | 0,445 | 16,5 | 6,9 | — |
| v1_com_5_jogadores_r4 | 2000 | 0 | 15,0 | 6,4 | 5,5% | 0,0% | 0,0% | 0,421 | 16,3 | 6,8 | — |
| v2_2_1_com_5_jogadores_r0 | 2000 | 0 | 33,3 | 13,5 | 1,9% | 4,2% | 0,0% | 0,066 | 14,6 | 8,6 | 51,7 / 55,1 / 58,5 |
| v2_2_1_com_5_jogadores_r1 | 2000 | 0 | 33,4 | 13,5 | 1,2% | 3,4% | 0,0% | 0,091 | 14,7 | 8,7 | 51,4 / 55,2 / 58,5 |
| v2_2_1_com_5_jogadores_r2 | 2000 | 0 | 33,1 | 13,4 | 1,5% | 1,3% | 0,0% | 0,112 | 14,5 | 8,6 | 51,3 / 54,8 / 58,4 |
| v2_2_1_com_5_jogadores_r3 | 2000 | 0 | 32,7 | 13,3 | 1,2% | 0,5% | 0,0% | 0,099 | 14,6 | 8,6 | 51,0 / 54,5 / 57,8 |
| v2_2_1_com_5_jogadores_r4 | 2000 | 0 | 33,0 | 13,5 | 1,7% | 2,1% | 0,0% | 0,089 | 14,6 | 8,6 | 51,5 / 54,8 / 58,0 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| v1_com_4_jogadores_r0 | v1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v1_com_4_jogadores_r1 | v1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v1_com_4_jogadores_r2 | v1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v1_com_4_jogadores_r3 | v1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v2_2_1_com_4_jogadores_r0 | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| v2_2_1_com_4_jogadores_r1 | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| v2_2_1_com_4_jogadores_r2 | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| v2_2_1_com_4_jogadores_r3 | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| v1_com_5_jogadores_r0 | v1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v1_com_5_jogadores_r1 | v1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v1_com_5_jogadores_r2 | v1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v1_com_5_jogadores_r3 | v1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v1_com_5_jogadores_r4 | v1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:fbc5495d99cf` |
| v2_2_1_com_5_jogadores_r0 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| v2_2_1_com_5_jogadores_r1 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| v2_2_1_com_5_jogadores_r2 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| v2_2_1_com_5_jogadores_r3 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| v2_2_1_com_5_jogadores_r4 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |

## Como refazer

No commit `f447f4b`: `cf experimento experimentos/fase3_exp2_v1_contra_v2.yaml --oficial --processos 4`. O resultado não depende do número de processos.

# Relatório do experimento `fase4_exp3_ablacao`

Ablação na v2.2.1: cada mudança da v2.2 desfeita sozinha (as correções COR-01 e COR-02, o bug duplicado e o limite de 1 teste por ciclo da 2.1), com mesas de 4 e de 5 (e de 6 para a COR-01), conhecimento iniciante e experiente.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase4_exp3_ablacao.yaml` |
| Commit | `f925943` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261118 |
| Partidas | 36000 |
| Falhas | 0 |
| Registros completos gravados | 36 |
| Início | 2026-11-11T08:09:55+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-06: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | (a) média da razão máximo/média de testes recebidos | 1,361 | 1,353 a 1,370 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_base | (b) fração dos testes contra quem tinha o menor placar | 0,423 | 0,418 a 0,427 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_sem_cor02 | (a) média da razão máximo/média de testes recebidos | 1,334 | 1,326 a 1,342 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_sem_cor02 | (b) fração dos testes contra quem tinha o menor placar | 0,425 | 0,420 a 0,429 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var10_bug_duplicado | (a) média da razão máximo/média de testes recebidos | 1,436 | 1,426 a 1,446 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var10_bug_duplicado | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,420 a 0,429 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var11_1_teste | (a) média da razão máximo/média de testes recebidos | 1,669 | 1,655 a 1,685 | 0,000 a 1,500 | 2000 | falha |
| n4_iniciante_var11_1_teste | (b) fração dos testes contra quem tinha o menor placar | 0,468 | 0,461 a 0,475 | 0,000 a 0,433 | 2000 | falha |
| n5_iniciante_base | (a) média da razão máximo/média de testes recebidos | 1,398 | 1,390 a 1,406 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_base | (b) fração dos testes contra quem tinha o menor placar | 0,342 | 0,338 a 0,346 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_sem_cor02 | (a) média da razão máximo/média de testes recebidos | 1,356 | 1,348 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_sem_cor02 | (b) fração dos testes contra quem tinha o menor placar | 0,344 | 0,340 a 0,347 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var10_bug_duplicado | (a) média da razão máximo/média de testes recebidos | 1,505 | 1,495 a 1,515 | 0,000 a 1,500 | 2000 | inconclusivo |
| n5_iniciante_var10_bug_duplicado | (b) fração dos testes contra quem tinha o menor placar | 0,344 | 0,340 a 0,348 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var11_1_teste | (a) média da razão máximo/média de testes recebidos | 1,763 | 1,747 a 1,779 | 0,000 a 1,500 | 2000 | falha |
| n5_iniciante_var11_1_teste | (b) fração dos testes contra quem tinha o menor placar | 0,397 | 0,391 a 0,403 | 0,000 a 0,350 | 2000 | falha |
| n6_iniciante_sem_cor01 | (a) média da razão máximo/média de testes recebidos | 1,440 | 1,432 a 1,447 | 0,000 a 1,500 | 2000 | passa |
| n6_iniciante_sem_cor01 | (b) fração dos testes contra quem tinha o menor placar | 0,292 | 0,289 a 0,296 | 0,000 a 0,300 | 2000 | passa |
| n4_experiente_base | (a) média da razão máximo/média de testes recebidos | 1,377 | 1,368 a 1,385 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_base | (b) fração dos testes contra quem tinha o menor placar | 0,422 | 0,418 a 0,426 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_sem_cor02 | (a) média da razão máximo/média de testes recebidos | 1,354 | 1,346 a 1,362 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_sem_cor02 | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,420 a 0,429 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_var10_bug_duplicado | (a) média da razão máximo/média de testes recebidos | 1,429 | 1,419 a 1,439 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var10_bug_duplicado | (b) fração dos testes contra quem tinha o menor placar | 0,426 | 0,421 a 0,431 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_var11_1_teste | (a) média da razão máximo/média de testes recebidos | 1,647 | 1,631 a 1,663 | 0,000 a 1,500 | 2000 | falha |
| n4_experiente_var11_1_teste | (b) fração dos testes contra quem tinha o menor placar | 0,474 | 0,467 a 0,481 | 0,000 a 0,433 | 2000 | falha |
| n5_experiente_base | (a) média da razão máximo/média de testes recebidos | 1,433 | 1,425 a 1,441 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_base | (b) fração dos testes contra quem tinha o menor placar | 0,343 | 0,339 a 0,347 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_sem_cor02 | (a) média da razão máximo/média de testes recebidos | 1,408 | 1,399 a 1,417 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_sem_cor02 | (b) fração dos testes contra quem tinha o menor placar | 0,348 | 0,344 a 0,352 | 0,000 a 0,350 | 2000 | inconclusivo |
| n5_experiente_var10_bug_duplicado | (a) média da razão máximo/média de testes recebidos | 1,519 | 1,507 a 1,530 | 0,000 a 1,500 | 2000 | falha |
| n5_experiente_var10_bug_duplicado | (b) fração dos testes contra quem tinha o menor placar | 0,346 | 0,342 a 0,350 | 0,000 a 0,350 | 2000 | inconclusivo |
| n5_experiente_var11_1_teste | (a) média da razão máximo/média de testes recebidos | 1,773 | 1,757 a 1,789 | 0,000 a 1,500 | 2000 | falha |
| n5_experiente_var11_1_teste | (b) fração dos testes contra quem tinha o menor placar | 0,392 | 0,386 a 0,398 | 0,000 a 0,350 | 2000 | falha |
| n6_experiente_sem_cor01 | (a) média da razão máximo/média de testes recebidos | 1,462 | 1,453 a 1,470 | 0,000 a 1,500 | 2000 | passa |
| n6_experiente_sem_cor01 | (b) fração dos testes contra quem tinha o menor placar | 0,291 | 0,288 a 0,294 | 0,000 a 0,300 | 2000 | passa |

Nota: (b): empate no menor placar conta como teste contra o menor.

### REQ-07: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | partidas com alguém em 0 ficha antes do último ciclo | 0,065 | 0,055 a 0,076 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_sem_cor02 | partidas com alguém em 0 ficha antes do último ciclo | 0,065 | 0,055 a 0,077 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var10_bug_duplicado | partidas com alguém em 0 ficha antes do último ciclo | 0,062 | 0,052 a 0,073 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var11_1_teste | partidas com alguém em 0 ficha antes do último ciclo | 0,081 | 0,069 a 0,093 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_base | partidas com alguém em 0 ficha antes do último ciclo | 0,074 | 0,064 a 0,087 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_sem_cor02 | partidas com alguém em 0 ficha antes do último ciclo | 0,076 | 0,066 a 0,089 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var10_bug_duplicado | partidas com alguém em 0 ficha antes do último ciclo | 0,059 | 0,050 a 0,071 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var11_1_teste | partidas com alguém em 0 ficha antes do último ciclo | 0,099 | 0,087 a 0,113 | 0,000 a 0,100 | 2000 | inconclusivo |
| n6_iniciante_sem_cor01 | partidas com alguém em 0 ficha antes do último ciclo | 0,084 | 0,072 a 0,096 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_base | partidas com alguém em 0 ficha antes do último ciclo | 0,046 | 0,038 a 0,056 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_sem_cor02 | partidas com alguém em 0 ficha antes do último ciclo | 0,048 | 0,039 a 0,058 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var10_bug_duplicado | partidas com alguém em 0 ficha antes do último ciclo | 0,040 | 0,032 a 0,049 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var11_1_teste | partidas com alguém em 0 ficha antes do último ciclo | 0,041 | 0,033 a 0,051 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_base | partidas com alguém em 0 ficha antes do último ciclo | 0,051 | 0,042 a 0,061 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_sem_cor02 | partidas com alguém em 0 ficha antes do último ciclo | 0,054 | 0,045 a 0,065 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var10_bug_duplicado | partidas com alguém em 0 ficha antes do último ciclo | 0,043 | 0,035 a 0,052 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var11_1_teste | partidas com alguém em 0 ficha antes do último ciclo | 0,042 | 0,034 a 0,052 | 0,000 a 0,100 | 2000 | passa |
| n6_experiente_sem_cor01 | partidas com alguém em 0 ficha antes do último ciclo | 0,059 | 0,050 a 0,071 | 0,000 a 0,100 | 2000 | passa |

### REQ-08: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | mediana da duração estimada (min) | 38,3 | 38,2 a 38,5 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_sem_cor02 | mediana da duração estimada (min) | 37,9 | 37,8 a 38,1 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var10_bug_duplicado | mediana da duração estimada (min) | 38,2 | 38,1 a 38,4 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var11_1_teste | mediana da duração estimada (min) | 28,2 | 28,2 a 28,2 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_base | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_sem_cor02 | mediana da duração estimada (min) | 44,2 | 44,0 a 44,3 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var10_bug_duplicado | mediana da duração estimada (min) | 43,7 | 43,5 a 43,8 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var11_1_teste | mediana da duração estimada (min) | 31,6 | 31,4 a 31,7 | 40,0 a 50,0 | 2000 | falha |
| n6_iniciante_sem_cor01 | mediana da duração estimada (min) | 50,8 | 50,7 a 50,9 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_base | mediana da duração estimada (min) | 38,8 | 38,7 a 38,9 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_sem_cor02 | mediana da duração estimada (min) | 38,8 | 38,6 a 38,9 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var10_bug_duplicado | mediana da duração estimada (min) | 38,3 | 38,2 a 38,5 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var11_1_teste | mediana da duração estimada (min) | 28,5 | 28,4 a 28,6 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_base | mediana da duração estimada (min) | 44,7 | 44,6 a 44,9 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_sem_cor02 | mediana da duração estimada (min) | 45,1 | 44,9 a 45,2 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var10_bug_duplicado | mediana da duração estimada (min) | 43,7 | 43,5 a 43,8 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var11_1_teste | mediana da duração estimada (min) | 31,8 | 31,7 a 31,9 | 40,0 a 50,0 | 2000 | falha |
| n6_experiente_sem_cor01 | mediana da duração estimada (min) | 51,0 | 50,8 a 51,2 | 40,0 a 50,0 | 2000 | falha |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-09: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 36000 | inconclusivo |

Nota: o critério pede pelo menos 50000 partidas.

### REQ-10: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_sem_cor02 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,7 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_var10_bug_duplicado | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_var11_1_teste | percentil 90 do tempo parado por jogador e ciclo (min) | 3,3 | 3,3 a 3,3 | 0,0 a 5,0 | 2000 | passa |
| n5_iniciante_base | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_sem_cor02 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var10_bug_duplicado | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 8,9 a 9,0 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var11_1_teste | percentil 90 do tempo parado por jogador e ciclo (min) | 4,9 | 4,9 a 4,9 | 0,0 a 5,0 | 2000 | passa |
| n6_iniciante_sem_cor01 | percentil 90 do tempo parado por jogador e ciclo (min) | 12,2 | 12,2 a 12,4 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_base | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_sem_cor02 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,9 | 5,8 a 6,0 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var10_bug_duplicado | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var11_1_teste | percentil 90 do tempo parado por jogador e ciclo (min) | 3,3 | 3,3 a 3,3 | 0,0 a 5,0 | 2000 | passa |
| n5_experiente_base | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,2 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_sem_cor02 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,4 | 9,3 a 9,5 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var10_bug_duplicado | percentil 90 do tempo parado por jogador e ciclo (min) | 8,9 | 8,8 a 8,9 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var11_1_teste | percentil 90 do tempo parado por jogador e ciclo (min) | 4,9 | 4,9 a 4,9 | 0,0 a 5,0 | 2000 | passa |
| n6_experiente_sem_cor01 | percentil 90 do tempo parado por jogador e ciclo (min) | 12,3 | 12,2 a 12,4 | 0,0 a 5,0 | 2000 | falha |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-11: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,564 a 0,585 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_sem_cor02 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,563 a 0,585 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var10_bug_duplicado | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,563 a 0,585 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var11_1_teste | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,563 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,565 a 0,584 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_sem_cor02 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,564 a 0,583 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var10_bug_duplicado | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,564 a 0,583 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var11_1_teste | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,564 a 0,583 | 0,100 a 0,900 | 2000 | passa |
| n6_iniciante_sem_cor01 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,572 | 0,563 a 0,580 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,498 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_sem_cor02 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,520 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var10_bug_duplicado | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var11_1_teste | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,512 | 0,502 a 0,522 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_sem_cor02 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,512 | 0,502 a 0,522 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var10_bug_duplicado | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,512 | 0,502 a 0,522 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var11_1_teste | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,512 | 0,502 a 0,522 | 0,100 a 0,900 | 2000 | passa |
| n6_experiente_sem_cor01 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,498 a 0,516 | 0,100 a 0,900 | 2000 | passa |

### REQ-12: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,073 | 0,051 a 0,095 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_sem_cor02 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,083 | 0,060 a 0,107 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_var10_bug_duplicado | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,081 | 0,058 a 0,102 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_var11_1_teste | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,083 | 0,062 a 0,107 | -0,100 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,051 | 0,034 a 0,070 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_sem_cor02 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,052 | 0,035 a 0,070 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var10_bug_duplicado | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,077 | 0,060 a 0,097 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var11_1_teste | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,077 | 0,059 a 0,095 | -0,100 a 0,100 | 2000 | passa |
| n6_iniciante_sem_cor01 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,062 | 0,046 a 0,077 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,056 | 0,034 a 0,078 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_sem_cor02 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,048 | 0,028 a 0,070 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var10_bug_duplicado | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,054 | 0,032 a 0,078 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var11_1_teste | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,063 | 0,042 a 0,085 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,042 | 0,025 a 0,058 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_sem_cor02 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,062 | 0,045 a 0,081 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var10_bug_duplicado | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,049 | 0,030 a 0,068 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var11_1_teste | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,073 | 0,053 a 0,091 | -0,100 a 0,100 | 2000 | passa |
| n6_experiente_sem_cor01 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,047 | 0,033 a 0,063 | -0,100 a 0,100 | 2000 | passa |

Nota: n4_experiente_base: 2184 assentos começaram cobrindo, 5816 não.
Nota: n4_experiente_sem_cor02: 2184 assentos começaram cobrindo, 5816 não.
Nota: n4_experiente_var10_bug_duplicado: 2184 assentos começaram cobrindo, 5816 não.
Nota: n4_experiente_var11_1_teste: 2184 assentos começaram cobrindo, 5816 não.
Nota: n4_iniciante_base: 2184 assentos começaram cobrindo, 5816 não.
Nota: n4_iniciante_sem_cor02: 2184 assentos começaram cobrindo, 5816 não.
Nota: n4_iniciante_var10_bug_duplicado: 2184 assentos começaram cobrindo, 5816 não.
Nota: n4_iniciante_var11_1_teste: 2184 assentos começaram cobrindo, 5816 não.
Nota: n5_experiente_base: 2744 assentos começaram cobrindo, 7256 não.
Nota: n5_experiente_sem_cor02: 2744 assentos começaram cobrindo, 7256 não.
Nota: n5_experiente_var10_bug_duplicado: 2744 assentos começaram cobrindo, 7256 não.
Nota: n5_experiente_var11_1_teste: 2744 assentos começaram cobrindo, 7256 não.
Nota: n5_iniciante_base: 2744 assentos começaram cobrindo, 7256 não.
Nota: n5_iniciante_sem_cor02: 2744 assentos começaram cobrindo, 7256 não.
Nota: n5_iniciante_var10_bug_duplicado: 2744 assentos começaram cobrindo, 7256 não.
Nota: n5_iniciante_var11_1_teste: 2744 assentos começaram cobrindo, 7256 não.
Nota: n6_experiente_sem_cor01: 3281 assentos começaram cobrindo, 8719 não.
Nota: n6_iniciante_sem_cor01: 3281 assentos começaram cobrindo, 8719 não.

### REQ-13: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | dano de incidente / fichas movimentadas | 0,215 | 0,213 a 0,217 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_sem_cor02 | dano de incidente / fichas movimentadas | 0,247 | 0,244 a 0,249 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var10_bug_duplicado | dano de incidente / fichas movimentadas | 0,203 | 0,201 a 0,205 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var11_1_teste | dano de incidente / fichas movimentadas | 0,230 | 0,227 a 0,233 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_base | dano de incidente / fichas movimentadas | 0,214 | 0,212 a 0,217 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_sem_cor02 | dano de incidente / fichas movimentadas | 0,247 | 0,245 a 0,249 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var10_bug_duplicado | dano de incidente / fichas movimentadas | 0,202 | 0,200 a 0,204 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var11_1_teste | dano de incidente / fichas movimentadas | 0,228 | 0,225 a 0,230 | 0,200 a 0,600 | 2000 | passa |
| n6_iniciante_sem_cor01 | dano de incidente / fichas movimentadas | 0,214 | 0,212 a 0,216 | 0,200 a 0,600 | 2000 | passa |
| n4_experiente_base | dano de incidente / fichas movimentadas | 0,171 | 0,169 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_sem_cor02 | dano de incidente / fichas movimentadas | 0,191 | 0,188 a 0,193 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var10_bug_duplicado | dano de incidente / fichas movimentadas | 0,164 | 0,162 a 0,167 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var11_1_teste | dano de incidente / fichas movimentadas | 0,183 | 0,180 a 0,185 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_base | dano de incidente / fichas movimentadas | 0,172 | 0,170 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_sem_cor02 | dano de incidente / fichas movimentadas | 0,192 | 0,190 a 0,195 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var10_bug_duplicado | dano de incidente / fichas movimentadas | 0,165 | 0,163 a 0,167 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var11_1_teste | dano de incidente / fichas movimentadas | 0,185 | 0,182 a 0,187 | 0,200 a 0,600 | 2000 | falha |
| n6_experiente_sem_cor01 | dano de incidente / fichas movimentadas | 0,174 | 0,172 a 0,176 | 0,200 a 0,600 | 2000 | falha |

Nota: o dano do Critical Failure não conta como dano de incidente.

## Taxa de vitória por bot (MET-07)

Sem veredito. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| n4_experiente_base | blefa_nunca_contesta_limiar | 4 | 4002 | 0,257 | 0,244 a 0,270 | 0,250 |
| n4_experiente_base | blefa_nunca_contesta_nunca | 4 | 2566 | 0,248 | 0,232 a 0,265 | 0,250 |
| n4_experiente_base | blefa_sempre_contesta_nunca | 4 | 1090 | 0,237 | 0,210 a 0,262 | 0,250 |
| n4_experiente_base | blefa_sempre_contesta_limiar | 4 | 342 | 0,219 | 0,174 a 0,263 | 0,250 |
| n4_experiente_sem_cor02 | blefa_nunca_contesta_limiar | 4 | 4002 | 0,252 | 0,239 a 0,266 | 0,250 |
| n4_experiente_sem_cor02 | blefa_sempre_contesta_nunca | 4 | 1090 | 0,252 | 0,228 a 0,278 | 0,250 |
| n4_experiente_sem_cor02 | blefa_nunca_contesta_nunca | 4 | 2566 | 0,252 | 0,235 a 0,267 | 0,250 |
| n4_experiente_sem_cor02 | blefa_sempre_contesta_limiar | 4 | 342 | 0,203 | 0,162 a 0,247 | 0,250 |
| n4_experiente_var10_bug_duplicado | blefa_nunca_contesta_limiar | 4 | 4002 | 0,258 | 0,245 a 0,271 | 0,250 |
| n4_experiente_var10_bug_duplicado | blefa_nunca_contesta_nunca | 4 | 2566 | 0,254 | 0,238 a 0,271 | 0,250 |
| n4_experiente_var10_bug_duplicado | blefa_sempre_contesta_nunca | 4 | 1090 | 0,232 | 0,208 a 0,258 | 0,250 |
| n4_experiente_var10_bug_duplicado | blefa_sempre_contesta_limiar | 4 | 342 | 0,180 | 0,143 a 0,218 | 0,250 |
| n4_experiente_var11_1_teste | blefa_sempre_contesta_nunca | 4 | 1090 | 0,255 | 0,230 a 0,279 | 0,250 |
| n4_experiente_var11_1_teste | blefa_nunca_contesta_nunca | 4 | 2566 | 0,253 | 0,236 a 0,270 | 0,250 |
| n4_experiente_var11_1_teste | blefa_nunca_contesta_limiar | 4 | 4002 | 0,251 | 0,238 a 0,264 | 0,250 |
| n4_experiente_var11_1_teste | blefa_sempre_contesta_limiar | 4 | 342 | 0,200 | 0,158 a 0,242 | 0,250 |
| n4_iniciante_base | blefa_sempre_contesta_nunca | 4 | 1090 | 0,271 | 0,243 a 0,295 | 0,250 |
| n4_iniciante_base | blefa_nunca_contesta_nunca | 4 | 2566 | 0,258 | 0,240 a 0,274 | 0,250 |
| n4_iniciante_base | blefa_nunca_contesta_limiar | 4 | 4002 | 0,242 | 0,229 a 0,255 | 0,250 |
| n4_iniciante_base | blefa_sempre_contesta_limiar | 4 | 342 | 0,227 | 0,183 a 0,269 | 0,250 |
| n4_iniciante_sem_cor02 | blefa_sempre_contesta_nunca | 4 | 1090 | 0,268 | 0,244 a 0,294 | 0,250 |
| n4_iniciante_sem_cor02 | blefa_sempre_contesta_limiar | 4 | 342 | 0,256 | 0,211 a 0,301 | 0,250 |
| n4_iniciante_sem_cor02 | blefa_nunca_contesta_nunca | 4 | 2566 | 0,254 | 0,238 a 0,272 | 0,250 |
| n4_iniciante_sem_cor02 | blefa_nunca_contesta_limiar | 4 | 4002 | 0,242 | 0,230 a 0,254 | 0,250 |
| n4_iniciante_var10_bug_duplicado | blefa_nunca_contesta_nunca | 4 | 2566 | 0,251 | 0,235 a 0,268 | 0,250 |
| n4_iniciante_var10_bug_duplicado | blefa_nunca_contesta_limiar | 4 | 4002 | 0,251 | 0,237 a 0,264 | 0,250 |
| n4_iniciante_var10_bug_duplicado | blefa_sempre_contesta_nunca | 4 | 1090 | 0,246 | 0,220 a 0,271 | 0,250 |
| n4_iniciante_var10_bug_duplicado | blefa_sempre_contesta_limiar | 4 | 342 | 0,243 | 0,197 a 0,287 | 0,250 |
| n4_iniciante_var11_1_teste | blefa_sempre_contesta_nunca | 4 | 1090 | 0,279 | 0,253 a 0,304 | 0,250 |
| n4_iniciante_var11_1_teste | blefa_sempre_contesta_limiar | 4 | 342 | 0,250 | 0,207 a 0,298 | 0,250 |
| n4_iniciante_var11_1_teste | blefa_nunca_contesta_limiar | 4 | 4002 | 0,247 | 0,234 a 0,260 | 0,250 |
| n4_iniciante_var11_1_teste | blefa_nunca_contesta_nunca | 4 | 2566 | 0,243 | 0,226 a 0,257 | 0,250 |
| n5_experiente_base | blefa_nunca_contesta_nunca | 5 | 3123 | 0,203 | 0,190 a 0,218 | 0,200 |
| n5_experiente_base | blefa_nunca_contesta_limiar | 5 | 5366 | 0,203 | 0,193 a 0,214 | 0,200 |
| n5_experiente_base | blefa_sempre_contesta_nunca | 5 | 1371 | 0,184 | 0,163 a 0,205 | 0,200 |
| n5_experiente_base | blefa_sempre_contesta_limiar | 5 | 140 | 0,154 | 0,100 a 0,218 | 0,200 |
| n5_experiente_sem_cor02 | blefa_nunca_contesta_nunca | 5 | 3123 | 0,210 | 0,196 a 0,225 | 0,200 |
| n5_experiente_sem_cor02 | blefa_sempre_contesta_nunca | 5 | 1371 | 0,201 | 0,180 a 0,223 | 0,200 |
| n5_experiente_sem_cor02 | blefa_sempre_contesta_limiar | 5 | 140 | 0,200 | 0,136 a 0,264 | 0,200 |
| n5_experiente_sem_cor02 | blefa_nunca_contesta_limiar | 5 | 5366 | 0,194 | 0,183 a 0,205 | 0,200 |
| n5_experiente_var10_bug_duplicado | blefa_nunca_contesta_limiar | 5 | 5366 | 0,207 | 0,197 a 0,218 | 0,200 |
| n5_experiente_var10_bug_duplicado | blefa_nunca_contesta_nunca | 5 | 3123 | 0,204 | 0,189 a 0,218 | 0,200 |
| n5_experiente_var10_bug_duplicado | blefa_sempre_contesta_limiar | 5 | 140 | 0,186 | 0,129 a 0,257 | 0,200 |
| n5_experiente_var10_bug_duplicado | blefa_sempre_contesta_nunca | 5 | 1371 | 0,165 | 0,146 a 0,186 | 0,200 |
| n5_experiente_var11_1_teste | blefa_sempre_contesta_limiar | 5 | 140 | 0,236 | 0,171 a 0,304 | 0,200 |
| n5_experiente_var11_1_teste | blefa_sempre_contesta_nunca | 5 | 1371 | 0,206 | 0,185 a 0,227 | 0,200 |
| n5_experiente_var11_1_teste | blefa_nunca_contesta_nunca | 5 | 3123 | 0,203 | 0,190 a 0,217 | 0,200 |
| n5_experiente_var11_1_teste | blefa_nunca_contesta_limiar | 5 | 5366 | 0,196 | 0,185 a 0,207 | 0,200 |
| n5_iniciante_base | blefa_sempre_contesta_limiar | 5 | 140 | 0,225 | 0,154 a 0,296 | 0,200 |
| n5_iniciante_base | blefa_nunca_contesta_limiar | 5 | 5366 | 0,207 | 0,196 a 0,218 | 0,200 |
| n5_iniciante_base | blefa_nunca_contesta_nunca | 5 | 3123 | 0,199 | 0,186 a 0,214 | 0,200 |
| n5_iniciante_base | blefa_sempre_contesta_nunca | 5 | 1371 | 0,173 | 0,153 a 0,194 | 0,200 |
| n5_iniciante_sem_cor02 | blefa_nunca_contesta_nunca | 5 | 3123 | 0,212 | 0,197 a 0,226 | 0,200 |
| n5_iniciante_sem_cor02 | blefa_nunca_contesta_limiar | 5 | 5366 | 0,196 | 0,185 a 0,206 | 0,200 |
| n5_iniciante_sem_cor02 | blefa_sempre_contesta_limiar | 5 | 140 | 0,193 | 0,132 a 0,264 | 0,200 |
| n5_iniciante_sem_cor02 | blefa_sempre_contesta_nunca | 5 | 1371 | 0,190 | 0,169 a 0,211 | 0,200 |
| n5_iniciante_var10_bug_duplicado | blefa_nunca_contesta_nunca | 5 | 3123 | 0,206 | 0,193 a 0,221 | 0,200 |
| n5_iniciante_var10_bug_duplicado | blefa_nunca_contesta_limiar | 5 | 5366 | 0,201 | 0,190 a 0,211 | 0,200 |
| n5_iniciante_var10_bug_duplicado | blefa_sempre_contesta_nunca | 5 | 1371 | 0,185 | 0,165 a 0,206 | 0,200 |
| n5_iniciante_var10_bug_duplicado | blefa_sempre_contesta_limiar | 5 | 140 | 0,179 | 0,118 a 0,246 | 0,200 |
| n5_iniciante_var11_1_teste | blefa_sempre_contesta_limiar | 5 | 140 | 0,211 | 0,146 a 0,279 | 0,200 |
| n5_iniciante_var11_1_teste | blefa_sempre_contesta_nunca | 5 | 1371 | 0,204 | 0,184 a 0,225 | 0,200 |
| n5_iniciante_var11_1_teste | blefa_nunca_contesta_limiar | 5 | 5366 | 0,203 | 0,193 a 0,214 | 0,200 |
| n5_iniciante_var11_1_teste | blefa_nunca_contesta_nunca | 5 | 3123 | 0,192 | 0,179 a 0,205 | 0,200 |
| n6_experiente_sem_cor01 | blefa_nunca_contesta_nunca | 6 | 3746 | 0,171 | 0,158 a 0,183 | 0,167 |
| n6_experiente_sem_cor01 | blefa_nunca_contesta_limiar | 6 | 6439 | 0,168 | 0,159 a 0,177 | 0,167 |
| n6_experiente_sem_cor01 | blefa_sempre_contesta_nunca | 6 | 1647 | 0,154 | 0,136 a 0,171 | 0,167 |
| n6_experiente_sem_cor01 | blefa_sempre_contesta_limiar | 6 | 168 | 0,143 | 0,089 a 0,194 | 0,167 |
| n6_iniciante_sem_cor01 | blefa_nunca_contesta_nunca | 6 | 3746 | 0,175 | 0,163 a 0,187 | 0,167 |
| n6_iniciante_sem_cor01 | blefa_nunca_contesta_limiar | 6 | 6439 | 0,168 | 0,159 a 0,177 | 0,167 |
| n6_iniciante_sem_cor01 | blefa_sempre_contesta_nunca | 6 | 1647 | 0,147 | 0,131 a 0,163 | 0,167 |
| n6_iniciante_sem_cor01 | blefa_sempre_contesta_limiar | 6 | 168 | 0,122 | 0,077 a 0,176 | 0,167 |

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903). Na v2 é só descrição: o placar em fichas não está na mesma escala dos pontos da v1, e a comparação entre as versões é feita pelo REQ-02 (autor, 2026-11-10).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| n4_iniciante_base | v2 | 4 | 2000 | **1,50** | 0,755 | 0,736 a 0,774 |
| n4_iniciante_base | v2 | 4 | 2000 | 1,25 | 0,946 | 0,935 a 0,955 |
| n4_iniciante_base | v2 | 4 | 2000 | 2,00 | 0,283 | 0,264 a 0,304 |
| n4_iniciante_sem_cor02 | v2 | 4 | 2000 | **1,50** | 0,870 | 0,855 a 0,884 |
| n4_iniciante_sem_cor02 | v2 | 4 | 2000 | 1,25 | 0,968 | 0,959 a 0,975 |
| n4_iniciante_sem_cor02 | v2 | 4 | 2000 | 2,00 | 0,520 | 0,499 a 0,542 |
| n4_iniciante_var10_bug_duplicado | v2 | 4 | 2000 | **1,50** | 0,720 | 0,700 a 0,739 |
| n4_iniciante_var10_bug_duplicado | v2 | 4 | 2000 | 1,25 | 0,925 | 0,913 a 0,936 |
| n4_iniciante_var10_bug_duplicado | v2 | 4 | 2000 | 2,00 | 0,230 | 0,212 a 0,248 |
| n4_iniciante_var11_1_teste | v2 | 4 | 2000 | **1,50** | 0,607 | 0,585 a 0,628 |
| n4_iniciante_var11_1_teste | v2 | 4 | 2000 | 1,25 | 0,878 | 0,863 a 0,892 |
| n4_iniciante_var11_1_teste | v2 | 4 | 2000 | 2,00 | 0,126 | 0,112 a 0,141 |
| n5_iniciante_base | v2 | 5 | 2000 | **1,50** | 0,769 | 0,751 a 0,787 |
| n5_iniciante_base | v2 | 5 | 2000 | 1,25 | 0,969 | 0,960 a 0,975 |
| n5_iniciante_base | v2 | 5 | 2000 | 2,00 | 0,293 | 0,273 a 0,313 |
| n5_iniciante_sem_cor02 | v2 | 5 | 2000 | **1,50** | 0,895 | 0,881 a 0,908 |
| n5_iniciante_sem_cor02 | v2 | 5 | 2000 | 1,25 | 0,987 | 0,980 a 0,991 |
| n5_iniciante_sem_cor02 | v2 | 5 | 2000 | 2,00 | 0,541 | 0,520 a 0,563 |
| n5_iniciante_var10_bug_duplicado | v2 | 5 | 2000 | **1,50** | 0,700 | 0,680 a 0,720 |
| n5_iniciante_var10_bug_duplicado | v2 | 5 | 2000 | 1,25 | 0,948 | 0,937 a 0,957 |
| n5_iniciante_var10_bug_duplicado | v2 | 5 | 2000 | 2,00 | 0,204 | 0,187 a 0,223 |
| n5_iniciante_var11_1_teste | v2 | 5 | 2000 | **1,50** | 0,623 | 0,602 a 0,644 |
| n5_iniciante_var11_1_teste | v2 | 5 | 2000 | 1,25 | 0,928 | 0,916 a 0,939 |
| n5_iniciante_var11_1_teste | v2 | 5 | 2000 | 2,00 | 0,124 | 0,111 a 0,140 |
| n6_iniciante_sem_cor01 | v2 | 6 | 2000 | **1,50** | 0,795 | 0,777 a 0,812 |
| n6_iniciante_sem_cor01 | v2 | 6 | 2000 | 1,25 | 0,985 | 0,978 a 0,989 |
| n6_iniciante_sem_cor01 | v2 | 6 | 2000 | 2,00 | 0,268 | 0,249 a 0,288 |
| n4_experiente_base | v2 | 4 | 2000 | **1,50** | 0,691 | 0,670 a 0,711 |
| n4_experiente_base | v2 | 4 | 2000 | 1,25 | 0,927 | 0,915 a 0,938 |
| n4_experiente_base | v2 | 4 | 2000 | 2,00 | 0,212 | 0,195 a 0,230 |
| n4_experiente_sem_cor02 | v2 | 4 | 2000 | **1,50** | 0,797 | 0,779 a 0,815 |
| n4_experiente_sem_cor02 | v2 | 4 | 2000 | 1,25 | 0,954 | 0,943 a 0,962 |
| n4_experiente_sem_cor02 | v2 | 4 | 2000 | 2,00 | 0,344 | 0,323 a 0,365 |
| n4_experiente_var10_bug_duplicado | v2 | 4 | 2000 | **1,50** | 0,647 | 0,626 a 0,668 |
| n4_experiente_var10_bug_duplicado | v2 | 4 | 2000 | 1,25 | 0,905 | 0,892 a 0,918 |
| n4_experiente_var10_bug_duplicado | v2 | 4 | 2000 | 2,00 | 0,182 | 0,166 a 0,200 |
| n4_experiente_var11_1_teste | v2 | 4 | 2000 | **1,50** | 0,563 | 0,541 a 0,585 |
| n4_experiente_var11_1_teste | v2 | 4 | 2000 | 1,25 | 0,883 | 0,868 a 0,896 |
| n4_experiente_var11_1_teste | v2 | 4 | 2000 | 2,00 | 0,094 | 0,082 a 0,108 |
| n5_experiente_base | v2 | 5 | 2000 | **1,50** | 0,682 | 0,661 a 0,702 |
| n5_experiente_base | v2 | 5 | 2000 | 1,25 | 0,956 | 0,946 a 0,964 |
| n5_experiente_base | v2 | 5 | 2000 | 2,00 | 0,198 | 0,181 a 0,216 |
| n5_experiente_sem_cor02 | v2 | 5 | 2000 | **1,50** | 0,785 | 0,767 a 0,803 |
| n5_experiente_sem_cor02 | v2 | 5 | 2000 | 1,25 | 0,975 | 0,967 a 0,981 |
| n5_experiente_sem_cor02 | v2 | 5 | 2000 | 2,00 | 0,332 | 0,312 a 0,353 |
| n5_experiente_var10_bug_duplicado | v2 | 5 | 2000 | **1,50** | 0,630 | 0,609 a 0,651 |
| n5_experiente_var10_bug_duplicado | v2 | 5 | 2000 | 1,25 | 0,926 | 0,914 a 0,937 |
| n5_experiente_var10_bug_duplicado | v2 | 5 | 2000 | 2,00 | 0,148 | 0,133 a 0,164 |
| n5_experiente_var11_1_teste | v2 | 5 | 2000 | **1,50** | 0,557 | 0,535 a 0,579 |
| n5_experiente_var11_1_teste | v2 | 5 | 2000 | 1,25 | 0,904 | 0,890 a 0,916 |
| n5_experiente_var11_1_teste | v2 | 5 | 2000 | 2,00 | 0,087 | 0,075 a 0,100 |
| n6_experiente_sem_cor01 | v2 | 6 | 2000 | **1,50** | 0,727 | 0,707 a 0,746 |
| n6_experiente_sem_cor01 | v2 | 6 | 2000 | 1,25 | 0,977 | 0,969 a 0,982 |
| n6_experiente_sem_cor01 | v2 | 6 | 2000 | 2,00 | 0,173 | 0,158 a 0,191 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Sistema cheio no 1º Planejamento | Blefes por partida (bem-sucedidos) | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n4_iniciante_base | 2000 | 0 | 21,7 | 2,0 | 1,8% | 0,0% | 0,0% | 0,164 | 10,8 | 7,3 | 57,4% | 1,94 (23,1%) | 35,0 / 38,3 / 41,9 |
| n4_iniciante_sem_cor02 | 2000 | 0 | 20,3 | 1,8 | 1,1% | 0,0% | 0,0% | 0,153 | 9,1 | 5,7 | 57,4% | 1,71 (23,3%) | 34,3 / 37,9 / 41,4 |
| n4_iniciante_var10_bug_duplicado | 2000 | 0 | 22,8 | 2,1 | 1,2% | 0,0% | 0,0% | 0,154 | 11,4 | 7,9 | 57,4% | 2,26 (22,6%) | 34,7 / 38,2 / 42,1 |
| n4_iniciante_var11_1_teste | 2000 | 0 | 8,6 | 0,8 | 3,0% | 0,0% | 0,0% | 0,213 | 9,3 | 6,8 | 57,4% | 0,79 (24,1%) | 26,6 / 28,2 / 30,2 |
| n5_iniciante_base | 2000 | 0 | 28,2 | 2,4 | 1,5% | 5,2% | 0,0% | 0,175 | 11,3 | 7,4 | 57,4% | 2,31 (23,6%) | 40,8 / 44,5 / 48,3 |
| n5_iniciante_sem_cor02 | 2000 | 0 | 26,5 | 2,3 | 2,1% | 4,6% | 0,0% | 0,171 | 9,5 | 5,6 | 57,4% | 2,00 (24,2%) | 40,6 / 44,2 / 48,0 |
| n5_iniciante_var10_bug_duplicado | 2000 | 0 | 29,0 | 2,5 | 2,1% | 5,2% | 0,0% | 0,163 | 11,9 | 8,1 | 57,4% | 2,53 (21,4%) | 39,9 / 43,7 / 48,0 |
| n5_iniciante_var11_1_teste | 2000 | 0 | 11,0 | 1,0 | 3,4% | 5,4% | 0,0% | 0,243 | 9,7 | 6,8 | 57,4% | 0,94 (21,2%) | 29,7 / 31,6 / 33,7 |
| n6_iniciante_sem_cor01 | 2000 | 0 | 34,5 | 3,1 | 1,6% | 100,0% | 0,1% | 0,164 | 11,6 | 7,4 | 57,2% | 2,86 (22,7%) | 46,8 / 50,8 / 55,1 |
| n4_experiente_base | 2000 | 0 | 22,0 | 3,3 | 1,8% | 0,0% | 0,0% | 0,180 | 12,1 | 8,5 | 51,0% | 2,20 (38,9%) | 35,2 / 38,8 / 42,6 |
| n4_experiente_sem_cor02 | 2000 | 0 | 20,9 | 3,2 | 2,1% | 0,0% | 0,0% | 0,174 | 10,8 | 7,1 | 51,0% | 1,96 (41,0%) | 35,2 / 38,8 / 42,7 |
| n4_experiente_var10_bug_duplicado | 2000 | 0 | 22,8 | 3,3 | 2,5% | 0,0% | 0,0% | 0,181 | 12,7 | 9,1 | 51,0% | 2,41 (37,4%) | 34,7 / 38,3 / 42,5 |
| n4_experiente_var11_1_teste | 2000 | 0 | 8,9 | 1,5 | 4,0% | 0,0% | 0,0% | 0,233 | 10,8 | 8,0 | 51,0% | 0,90 (36,8%) | 26,6 / 28,5 / 30,7 |
| n5_experiente_base | 2000 | 0 | 28,3 | 3,9 | 2,6% | 8,1% | 0,0% | 0,165 | 12,6 | 8,5 | 51,2% | 2,42 (39,0%) | 40,7 / 44,7 / 48,8 |
| n5_experiente_sem_cor02 | 2000 | 0 | 27,0 | 4,0 | 2,1% | 7,1% | 0,0% | 0,188 | 11,1 | 7,1 | 51,2% | 2,22 (39,4%) | 41,1 / 45,1 / 49,2 |
| n5_experiente_var10_bug_duplicado | 2000 | 0 | 29,0 | 3,9 | 2,8% | 7,3% | 0,0% | 0,172 | 13,2 | 9,2 | 51,2% | 2,61 (37,3%) | 39,8 / 43,7 / 48,2 |
| n5_experiente_var11_1_teste | 2000 | 0 | 11,3 | 1,7 | 5,2% | 7,6% | 0,0% | 0,250 | 11,2 | 8,0 | 51,2% | 0,96 (36,2%) | 29,7 / 31,8 / 34,1 |
| n6_experiente_sem_cor01 | 2000 | 0 | 34,4 | 5,1 | 2,5% | 100,0% | 0,1% | 0,175 | 13,0 | 8,6 | 50,7% | 3,04 (37,1%) | 46,8 / 51,0 / 55,6 |

## Equilíbrio dentro da partida (descrição)

Números sem critério de aceite; os vereditos, quando pedidos, estão na seção de requisitos. Razão de testes: máximo sobre a média de testes recebidos na partida (REQ-06a). Contra o menor: fração dos testes contra quem tinha o menor placar (REQ-06b). Zeradas: partidas com alguém em 0 ficha antes do último ciclo (REQ-07). Parado: percentil 90 do tempo parado por jogador e ciclo, pelos tempos provisórios do MOD-05 (REQ-10). Peso do dano: dano de incidente sobre as fichas movimentadas (REQ-13). Dispersão: placar do primeiro menos o do último no fim (REQ-14).

| Cenário | Razão de testes | Contra o menor | Zeradas | Parado p90 (min) | Peso do dano | Dispersão |
|---|---|---|---|---|---|---|
| n4_iniciante_base | 1,36 | 0,423 | 6,5% | 5,8 | 0,215 | 6,8 |
| n4_iniciante_sem_cor02 | 1,33 | 0,425 | 6,5% | 5,8 | 0,247 | 6,7 |
| n4_iniciante_var10_bug_duplicado | 1,44 | 0,424 | 6,2% | 5,8 | 0,203 | 6,9 |
| n4_iniciante_var11_1_teste | 1,67 | 0,468 | 8,1% | 3,3 | 0,230 | 4,8 |
| n5_iniciante_base | 1,40 | 0,342 | 7,4% | 9,2 | 0,214 | 7,6 |
| n5_iniciante_sem_cor02 | 1,36 | 0,344 | 7,6% | 9,0 | 0,247 | 7,4 |
| n5_iniciante_var10_bug_duplicado | 1,50 | 0,344 | 5,9% | 9,0 | 0,202 | 7,6 |
| n5_iniciante_var11_1_teste | 1,76 | 0,397 | 9,9% | 4,9 | 0,228 | 5,5 |
| n6_iniciante_sem_cor01 | 1,44 | 0,292 | 8,3% | 12,2 | 0,214 | 8,2 |
| n4_experiente_base | 1,38 | 0,422 | 4,6% | 5,8 | 0,171 | 7,3 |
| n4_experiente_sem_cor02 | 1,35 | 0,424 | 4,8% | 5,9 | 0,191 | 7,1 |
| n4_experiente_var10_bug_duplicado | 1,43 | 0,426 | 4,0% | 5,8 | 0,164 | 7,4 |
| n4_experiente_var11_1_teste | 1,65 | 0,474 | 4,1% | 3,3 | 0,183 | 5,5 |
| n5_experiente_base | 1,43 | 0,343 | 5,1% | 9,2 | 0,172 | 8,0 |
| n5_experiente_sem_cor02 | 1,41 | 0,348 | 5,5% | 9,4 | 0,192 | 7,7 |
| n5_experiente_var10_bug_duplicado | 1,52 | 0,346 | 4,2% | 8,9 | 0,165 | 8,1 |
| n5_experiente_var11_1_teste | 1,77 | 0,392 | 4,2% | 4,9 | 0,185 | 6,2 |
| n6_experiente_sem_cor01 | 1,46 | 0,291 | 5,9% | 12,3 | 0,174 | 8,7 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| n4_iniciante_base | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_iniciante_sem_cor02 | v2.2.1 com {'alertas.limpeza_no_planejamento': False} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:5d915084ded3` |
| n4_iniciante_var10_bug_duplicado | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': True, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 0, 'regra': 'VAR-11'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b215250ea056` |
| n4_iniciante_var11_1_teste | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| n5_iniciante_base | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_iniciante_sem_cor02 | v2.2.1 com {'alertas.limpeza_no_planejamento': False} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:5d915084ded3` |
| n5_iniciante_var10_bug_duplicado | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': True, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 0, 'regra': 'VAR-11'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b215250ea056` |
| n5_iniciante_var11_1_teste | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| n6_iniciante_sem_cor01 | v2.2.1 com {'jogadores.maximo': 6} | 6 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:395b4d7affed` |
| n4_experiente_base | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_experiente_sem_cor02 | v2.2.1 com {'alertas.limpeza_no_planejamento': False} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:5d915084ded3` |
| n4_experiente_var10_bug_duplicado | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': True, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 0, 'regra': 'VAR-11'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b215250ea056` |
| n4_experiente_var11_1_teste | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| n5_experiente_base | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_experiente_sem_cor02 | v2.2.1 com {'alertas.limpeza_no_planejamento': False} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:5d915084ded3` |
| n5_experiente_var10_bug_duplicado | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': True, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 0, 'regra': 'VAR-11'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b215250ea056` |
| n5_experiente_var11_1_teste | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| n6_experiente_sem_cor01 | v2.2.1 com {'jogadores.maximo': 6} | 6 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:395b4d7affed` |

## Como refazer

No commit `f925943`: `cf experimento experimentos/fase4_exp3_ablacao.yaml --oficial --processos 4`. O resultado não depende do número de processos.

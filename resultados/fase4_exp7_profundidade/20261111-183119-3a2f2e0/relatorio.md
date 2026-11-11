# Relatório do experimento `fase4_exp7_profundidade`

Profundidade do jogo na v2.2.1: testes sem limite por ciclo, 1 e 2 testes por ciclo (VAR-11) e custo do teste a partir do 2º teste do ciclo (VAR-12), com escolhas apertadas, viradas e habilidade em degraus (MET-08 a MET-10).

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase4_exp7_profundidade.yaml` |
| Commit | `3a2f2e0` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261122 |
| Partidas | 80000 |
| Falhas | 0 |
| Registros completos gravados | 140 |
| Início | 2026-11-11T18:31:19+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-06: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | (a) média da razão máximo/média de testes recebidos | 1,357 | 1,350 a 1,365 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_base | (b) fração dos testes contra quem tinha o menor placar | 0,423 | 0,419 a 0,428 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var11_1_teste | (a) média da razão máximo/média de testes recebidos | 1,662 | 1,648 a 1,679 | 0,000 a 1,500 | 2000 | falha |
| n4_iniciante_var11_1_teste | (b) fração dos testes contra quem tinha o menor placar | 0,460 | 0,453 a 0,468 | 0,000 a 0,433 | 2000 | falha |
| n4_iniciante_var11_2_testes | (a) média da razão máximo/média de testes recebidos | 1,475 | 1,464 a 1,485 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var11_2_testes | (b) fração dos testes contra quem tinha o menor placar | 0,437 | 0,431 a 0,441 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_iniciante_var12_custo | (a) média da razão máximo/média de testes recebidos | 1,459 | 1,449 a 1,471 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var12_custo | (b) fração dos testes contra quem tinha o menor placar | 0,436 | 0,431 a 0,441 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_experiente_base | (a) média da razão máximo/média de testes recebidos | 1,374 | 1,366 a 1,383 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_base | (b) fração dos testes contra quem tinha o menor placar | 0,428 | 0,424 a 0,433 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_experiente_var11_1_teste | (a) média da razão máximo/média de testes recebidos | 1,659 | 1,645 a 1,674 | 0,000 a 1,500 | 2000 | falha |
| n4_experiente_var11_1_teste | (b) fração dos testes contra quem tinha o menor placar | 0,468 | 0,461 a 0,474 | 0,000 a 0,433 | 2000 | falha |
| n4_experiente_var11_2_testes | (a) média da razão máximo/média de testes recebidos | 1,468 | 1,458 a 1,478 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var11_2_testes | (b) fração dos testes contra quem tinha o menor placar | 0,441 | 0,436 a 0,447 | 0,000 a 0,433 | 2000 | falha |
| n4_experiente_var12_custo | (a) média da razão máximo/média de testes recebidos | 1,478 | 1,466 a 1,488 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var12_custo | (b) fração dos testes contra quem tinha o menor placar | 0,433 | 0,427 a 0,438 | 0,000 a 0,433 | 2000 | inconclusivo |
| n5_iniciante_base | (a) média da razão máximo/média de testes recebidos | 1,405 | 1,396 a 1,413 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_base | (b) fração dos testes contra quem tinha o menor placar | 0,341 | 0,338 a 0,345 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var11_1_teste | (a) média da razão máximo/média de testes recebidos | 1,762 | 1,746 a 1,778 | 0,000 a 1,500 | 2000 | falha |
| n5_iniciante_var11_1_teste | (b) fração dos testes contra quem tinha o menor placar | 0,392 | 0,386 a 0,398 | 0,000 a 0,350 | 2000 | falha |
| n5_iniciante_var11_2_testes | (a) média da razão máximo/média de testes recebidos | 1,522 | 1,512 a 1,534 | 0,000 a 1,500 | 2000 | falha |
| n5_iniciante_var11_2_testes | (b) fração dos testes contra quem tinha o menor placar | 0,360 | 0,355 a 0,364 | 0,000 a 0,350 | 2000 | falha |
| n5_iniciante_var12_custo | (a) média da razão máximo/média de testes recebidos | 1,501 | 1,492 a 1,511 | 0,000 a 1,500 | 2000 | inconclusivo |
| n5_iniciante_var12_custo | (b) fração dos testes contra quem tinha o menor placar | 0,356 | 0,351 a 0,360 | 0,000 a 0,350 | 2000 | falha |
| n5_experiente_base | (a) média da razão máximo/média de testes recebidos | 1,430 | 1,421 a 1,439 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_base | (b) fração dos testes contra quem tinha o menor placar | 0,339 | 0,336 a 0,343 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_var11_1_teste | (a) média da razão máximo/média de testes recebidos | 1,765 | 1,751 a 1,781 | 0,000 a 1,500 | 2000 | falha |
| n5_experiente_var11_1_teste | (b) fração dos testes contra quem tinha o menor placar | 0,394 | 0,388 a 0,400 | 0,000 a 0,350 | 2000 | falha |
| n5_experiente_var11_2_testes | (a) média da razão máximo/média de testes recebidos | 1,527 | 1,516 a 1,538 | 0,000 a 1,500 | 2000 | falha |
| n5_experiente_var11_2_testes | (b) fração dos testes contra quem tinha o menor placar | 0,359 | 0,355 a 0,363 | 0,000 a 0,350 | 2000 | falha |
| n5_experiente_var12_custo | (a) média da razão máximo/média de testes recebidos | 1,516 | 1,506 a 1,527 | 0,000 a 1,500 | 2000 | falha |
| n5_experiente_var12_custo | (b) fração dos testes contra quem tinha o menor placar | 0,355 | 0,351 a 0,360 | 0,000 a 0,350 | 2000 | falha |

Nota: (b): empate no menor placar conta como teste contra o menor.

### REQ-07: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | partidas com alguém em 0 ficha antes do último ciclo | 0,062 | 0,052 a 0,073 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var11_1_teste | partidas com alguém em 0 ficha antes do último ciclo | 0,085 | 0,074 a 0,098 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var11_2_testes | partidas com alguém em 0 ficha antes do último ciclo | 0,065 | 0,055 a 0,076 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var12_custo | partidas com alguém em 0 ficha antes do último ciclo | 0,166 | 0,150 a 0,183 | 0,000 a 0,100 | 2000 | falha |
| n4_experiente_base | partidas com alguém em 0 ficha antes do último ciclo | 0,047 | 0,039 a 0,057 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var11_1_teste | partidas com alguém em 0 ficha antes do último ciclo | 0,049 | 0,040 a 0,059 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var11_2_testes | partidas com alguém em 0 ficha antes do último ciclo | 0,046 | 0,038 a 0,057 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var12_custo | partidas com alguém em 0 ficha antes do último ciclo | 0,101 | 0,088 a 0,114 | 0,000 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_base | partidas com alguém em 0 ficha antes do último ciclo | 0,073 | 0,062 a 0,085 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var11_1_teste | partidas com alguém em 0 ficha antes do último ciclo | 0,108 | 0,095 a 0,122 | 0,000 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_var11_2_testes | partidas com alguém em 0 ficha antes do último ciclo | 0,085 | 0,074 a 0,098 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var12_custo | partidas com alguém em 0 ficha antes do último ciclo | 0,199 | 0,182 a 0,217 | 0,000 a 0,100 | 2000 | falha |
| n5_experiente_base | partidas com alguém em 0 ficha antes do último ciclo | 0,059 | 0,049 a 0,070 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var11_1_teste | partidas com alguém em 0 ficha antes do último ciclo | 0,048 | 0,039 a 0,058 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var11_2_testes | partidas com alguém em 0 ficha antes do último ciclo | 0,046 | 0,038 a 0,057 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var12_custo | partidas com alguém em 0 ficha antes do último ciclo | 0,145 | 0,130 a 0,161 | 0,000 a 0,100 | 2000 | falha |

### REQ-08: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | mediana da duração estimada (min) | 38,2 | 38,2 a 38,4 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var11_1_teste | mediana da duração estimada (min) | 28,2 | 28,0 a 28,2 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var11_2_testes | mediana da duração estimada (min) | 33,2 | 33,2 a 33,3 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var12_custo | mediana da duração estimada (min) | 33,5 | 33,3 a 33,6 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_base | mediana da duração estimada (min) | 38,5 | 38,3 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var11_1_teste | mediana da duração estimada (min) | 28,3 | 28,2 a 28,5 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var11_2_testes | mediana da duração estimada (min) | 33,5 | 33,4 a 33,6 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var12_custo | mediana da duração estimada (min) | 33,7 | 33,5 a 33,9 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_base | mediana da duração estimada (min) | 44,2 | 44,0 a 44,4 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var11_1_teste | mediana da duração estimada (min) | 31,4 | 31,3 a 31,4 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_var11_2_testes | mediana da duração estimada (min) | 37,8 | 37,7 a 37,9 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_var12_custo | mediana da duração estimada (min) | 38,6 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_base | mediana da duração estimada (min) | 44,6 | 44,4 a 44,8 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var11_1_teste | mediana da duração estimada (min) | 31,8 | 31,7 a 31,9 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_var11_2_testes | mediana da duração estimada (min) | 38,2 | 38,2 a 38,4 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_var12_custo | mediana da duração estimada (min) | 39,1 | 38,9 a 39,2 | 40,0 a 50,0 | 2000 | falha |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-09: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 80000 | passa |

Nota: o critério pede pelo menos 50000 partidas.

### REQ-10: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_var11_1_teste | percentil 90 do tempo parado por jogador e ciclo (min) | 3,3 | 3,3 a 3,3 | 0,0 a 5,0 | 2000 | passa |
| n4_iniciante_var11_2_testes | percentil 90 do tempo parado por jogador e ciclo (min) | 4,4 | 4,4 a 4,7 | 0,0 a 5,0 | 2000 | passa |
| n4_iniciante_var12_custo | percentil 90 do tempo parado por jogador e ciclo (min) | 4,8 | 4,7 a 4,8 | 0,0 a 5,0 | 2000 | passa |
| n4_experiente_base | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var11_1_teste | percentil 90 do tempo parado por jogador e ciclo (min) | 3,3 | 3,3 a 3,3 | 0,0 a 5,0 | 2000 | passa |
| n4_experiente_var11_2_testes | percentil 90 do tempo parado por jogador e ciclo (min) | 4,6 | 4,6 a 4,7 | 0,0 a 5,0 | 2000 | passa |
| n4_experiente_var12_custo | percentil 90 do tempo parado por jogador e ciclo (min) | 4,8 | 4,7 a 4,8 | 0,0 a 5,0 | 2000 | passa |
| n5_iniciante_base | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var11_1_teste | percentil 90 do tempo parado por jogador e ciclo (min) | 4,9 | 4,9 a 4,9 | 0,0 a 5,0 | 2000 | passa |
| n5_iniciante_var11_2_testes | percentil 90 do tempo parado por jogador e ciclo (min) | 6,9 | 6,9 a 7,0 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var12_custo | percentil 90 do tempo parado por jogador e ciclo (min) | 7,3 | 7,3 a 7,6 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_base | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var11_1_teste | percentil 90 do tempo parado por jogador e ciclo (min) | 4,9 | 4,9 a 4,9 | 0,0 a 5,0 | 2000 | passa |
| n5_experiente_var11_2_testes | percentil 90 do tempo parado por jogador e ciclo (min) | 6,9 | 6,9 a 7,0 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var12_custo | percentil 90 do tempo parado por jogador e ciclo (min) | 7,5 | 7,4 a 7,6 | 0,0 a 5,0 | 2000 | falha |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-11: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,563 a 0,585 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var11_1_teste | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,574 a 0,596 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var11_2_testes | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,576 | 0,565 a 0,587 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var12_custo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,574 a 0,595 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,515 | 0,505 a 0,526 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var11_1_teste | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,527 | 0,515 a 0,539 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var11_2_testes | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,518 | 0,507 a 0,530 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var12_custo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,527 | 0,516 a 0,538 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,572 | 0,562 a 0,582 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var11_1_teste | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,578 | 0,568 a 0,588 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var11_2_testes | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,572 | 0,562 a 0,582 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var12_custo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,578 | 0,568 a 0,588 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,505 | 0,495 a 0,514 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var11_1_teste | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,513 | 0,504 a 0,523 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var11_2_testes | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,506 | 0,495 a 0,515 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var12_custo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,513 | 0,503 a 0,523 | 0,100 a 0,900 | 2000 | passa |

### REQ-12: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,068 | 0,047 a 0,090 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var11_1_teste | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,100 | 0,078 a 0,121 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_var11_2_testes | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,069 | 0,046 a 0,091 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var12_custo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,085 | 0,063 a 0,107 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_experiente_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,033 | 0,012 a 0,054 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var11_1_teste | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,066 | 0,043 a 0,086 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var11_2_testes | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,052 | 0,029 a 0,075 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var12_custo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,053 | 0,031 a 0,076 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,084 | 0,066 a 0,101 | -0,100 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_var11_1_teste | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,086 | 0,067 a 0,105 | -0,100 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_var11_2_testes | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,080 | 0,060 a 0,098 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var12_custo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,077 | 0,057 a 0,095 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,052 | 0,034 a 0,072 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var11_1_teste | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,075 | 0,057 a 0,094 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var11_2_testes | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,049 | 0,029 a 0,067 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var12_custo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,062 | 0,045 a 0,081 | -0,100 a 0,100 | 2000 | passa |

Nota: n4_experiente_base: 2093 assentos começaram cobrindo, 5907 não.
Nota: n4_experiente_var11_1_teste: 2093 assentos começaram cobrindo, 5907 não.
Nota: n4_experiente_var11_2_testes: 2093 assentos começaram cobrindo, 5907 não.
Nota: n4_experiente_var12_custo: 2093 assentos começaram cobrindo, 5907 não.
Nota: n4_iniciante_base: 2093 assentos começaram cobrindo, 5907 não.
Nota: n4_iniciante_var11_1_teste: 2093 assentos começaram cobrindo, 5907 não.
Nota: n4_iniciante_var11_2_testes: 2093 assentos começaram cobrindo, 5907 não.
Nota: n4_iniciante_var12_custo: 2093 assentos começaram cobrindo, 5907 não.
Nota: n5_experiente_base: 2624 assentos começaram cobrindo, 7376 não.
Nota: n5_experiente_var11_1_teste: 2624 assentos começaram cobrindo, 7376 não.
Nota: n5_experiente_var11_2_testes: 2624 assentos começaram cobrindo, 7376 não.
Nota: n5_experiente_var12_custo: 2624 assentos começaram cobrindo, 7376 não.
Nota: n5_iniciante_base: 2624 assentos começaram cobrindo, 7376 não.
Nota: n5_iniciante_var11_1_teste: 2624 assentos começaram cobrindo, 7376 não.
Nota: n5_iniciante_var11_2_testes: 2624 assentos começaram cobrindo, 7376 não.
Nota: n5_iniciante_var12_custo: 2624 assentos começaram cobrindo, 7376 não.

### REQ-13: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | dano de incidente / fichas movimentadas | 0,217 | 0,215 a 0,220 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var11_1_teste | dano de incidente / fichas movimentadas | 0,231 | 0,229 a 0,234 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var11_2_testes | dano de incidente / fichas movimentadas | 0,222 | 0,219 a 0,224 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var12_custo | dano de incidente / fichas movimentadas | 0,200 | 0,198 a 0,202 | 0,200 a 0,600 | 2000 | inconclusivo |
| n4_experiente_base | dano de incidente / fichas movimentadas | 0,174 | 0,172 a 0,176 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var11_1_teste | dano de incidente / fichas movimentadas | 0,186 | 0,184 a 0,189 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var11_2_testes | dano de incidente / fichas movimentadas | 0,178 | 0,176 a 0,181 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var12_custo | dano de incidente / fichas movimentadas | 0,162 | 0,160 a 0,164 | 0,200 a 0,600 | 2000 | falha |
| n5_iniciante_base | dano de incidente / fichas movimentadas | 0,218 | 0,216 a 0,220 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var11_1_teste | dano de incidente / fichas movimentadas | 0,233 | 0,230 a 0,235 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var11_2_testes | dano de incidente / fichas movimentadas | 0,223 | 0,221 a 0,225 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var12_custo | dano de incidente / fichas movimentadas | 0,198 | 0,196 a 0,200 | 0,200 a 0,600 | 2000 | inconclusivo |
| n5_experiente_base | dano de incidente / fichas movimentadas | 0,174 | 0,172 a 0,176 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var11_1_teste | dano de incidente / fichas movimentadas | 0,186 | 0,184 a 0,189 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var11_2_testes | dano de incidente / fichas movimentadas | 0,179 | 0,177 a 0,181 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var12_custo | dano de incidente / fichas movimentadas | 0,160 | 0,158 a 0,162 | 0,200 a 0,600 | 2000 | falha |

Nota: o dano do Critical Failure não conta como dano de incidente.

## Taxa de vitória por bot (MET-07)

Sem veredito. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| degraus_n4_base_t1 | foco | 4 | 2000 | 0,329 | 0,308 a 0,349 | 0,250 |
| degraus_n4_base_t1 | descuidado_t1 | 4 | 6000 | 0,224 | 0,214 a 0,235 | 0,250 |
| degraus_n4_base_t2 | foco | 4 | 2000 | 0,394 | 0,373 a 0,414 | 0,250 |
| degraus_n4_base_t2 | descuidado_t2 | 4 | 6000 | 0,202 | 0,193 a 0,212 | 0,250 |
| degraus_n4_base_t4 | foco | 4 | 2000 | 0,469 | 0,446 a 0,489 | 0,250 |
| degraus_n4_base_t4 | descuidado_t4 | 4 | 6000 | 0,177 | 0,168 a 0,186 | 0,250 |
| degraus_n4_var11_1_teste_t1 | foco | 4 | 2000 | 0,303 | 0,285 a 0,324 | 0,250 |
| degraus_n4_var11_1_teste_t1 | descuidado_t1 | 4 | 6000 | 0,232 | 0,222 a 0,243 | 0,250 |
| degraus_n4_var11_1_teste_t2 | foco | 4 | 2000 | 0,378 | 0,355 a 0,399 | 0,250 |
| degraus_n4_var11_1_teste_t2 | descuidado_t2 | 4 | 6000 | 0,207 | 0,198 a 0,218 | 0,250 |
| degraus_n4_var11_1_teste_t4 | foco | 4 | 2000 | 0,401 | 0,381 a 0,421 | 0,250 |
| degraus_n4_var11_1_teste_t4 | descuidado_t4 | 4 | 6000 | 0,200 | 0,190 a 0,209 | 0,250 |
| degraus_n4_var11_2_testes_t1 | foco | 4 | 2000 | 0,318 | 0,296 a 0,338 | 0,250 |
| degraus_n4_var11_2_testes_t1 | descuidado_t1 | 4 | 6000 | 0,228 | 0,217 a 0,239 | 0,250 |
| degraus_n4_var11_2_testes_t2 | foco | 4 | 2000 | 0,378 | 0,358 a 0,398 | 0,250 |
| degraus_n4_var11_2_testes_t2 | descuidado_t2 | 4 | 6000 | 0,207 | 0,197 a 0,218 | 0,250 |
| degraus_n4_var11_2_testes_t4 | foco | 4 | 2000 | 0,419 | 0,398 a 0,440 | 0,250 |
| degraus_n4_var11_2_testes_t4 | descuidado_t4 | 4 | 6000 | 0,194 | 0,184 a 0,203 | 0,250 |
| degraus_n4_var12_custo_t1 | foco | 4 | 2000 | 0,321 | 0,301 a 0,343 | 0,250 |
| degraus_n4_var12_custo_t1 | descuidado_t1 | 4 | 6000 | 0,226 | 0,215 a 0,237 | 0,250 |
| degraus_n4_var12_custo_t2 | foco | 4 | 2000 | 0,402 | 0,379 a 0,422 | 0,250 |
| degraus_n4_var12_custo_t2 | descuidado_t2 | 4 | 6000 | 0,199 | 0,189 a 0,210 | 0,250 |
| degraus_n4_var12_custo_t4 | foco | 4 | 2000 | 0,465 | 0,443 a 0,488 | 0,250 |
| degraus_n4_var12_custo_t4 | descuidado_t4 | 4 | 6000 | 0,178 | 0,169 a 0,188 | 0,250 |
| degraus_n5_base_t1 | foco | 5 | 2000 | 0,286 | 0,267 a 0,306 | 0,200 |
| degraus_n5_base_t1 | descuidado_t1 | 5 | 8000 | 0,179 | 0,170 a 0,187 | 0,200 |
| degraus_n5_base_t2 | foco | 5 | 2000 | 0,365 | 0,344 a 0,385 | 0,200 |
| degraus_n5_base_t2 | descuidado_t2 | 5 | 8000 | 0,159 | 0,151 a 0,167 | 0,200 |
| degraus_n5_base_t4 | foco | 5 | 2000 | 0,419 | 0,396 a 0,441 | 0,200 |
| degraus_n5_base_t4 | descuidado_t4 | 5 | 8000 | 0,145 | 0,137 a 0,153 | 0,200 |
| degraus_n5_var11_1_teste_t1 | foco | 5 | 2000 | 0,257 | 0,238 a 0,277 | 0,200 |
| degraus_n5_var11_1_teste_t1 | descuidado_t1 | 5 | 8000 | 0,186 | 0,177 a 0,194 | 0,200 |
| degraus_n5_var11_1_teste_t2 | foco | 5 | 2000 | 0,310 | 0,291 a 0,332 | 0,200 |
| degraus_n5_var11_1_teste_t2 | descuidado_t2 | 5 | 8000 | 0,172 | 0,164 a 0,180 | 0,200 |
| degraus_n5_var11_1_teste_t4 | foco | 5 | 2000 | 0,356 | 0,334 a 0,377 | 0,200 |
| degraus_n5_var11_1_teste_t4 | descuidado_t4 | 5 | 8000 | 0,161 | 0,153 a 0,169 | 0,200 |
| degraus_n5_var11_2_testes_t1 | foco | 5 | 2000 | 0,273 | 0,251 a 0,293 | 0,200 |
| degraus_n5_var11_2_testes_t1 | descuidado_t1 | 5 | 8000 | 0,182 | 0,173 a 0,190 | 0,200 |
| degraus_n5_var11_2_testes_t2 | foco | 5 | 2000 | 0,336 | 0,315 a 0,357 | 0,200 |
| degraus_n5_var11_2_testes_t2 | descuidado_t2 | 5 | 8000 | 0,166 | 0,158 a 0,174 | 0,200 |
| degraus_n5_var11_2_testes_t4 | foco | 5 | 2000 | 0,384 | 0,364 a 0,405 | 0,200 |
| degraus_n5_var11_2_testes_t4 | descuidado_t4 | 5 | 8000 | 0,154 | 0,146 a 0,162 | 0,200 |
| degraus_n5_var12_custo_t1 | foco | 5 | 2000 | 0,296 | 0,277 a 0,317 | 0,200 |
| degraus_n5_var12_custo_t1 | descuidado_t1 | 5 | 8000 | 0,176 | 0,168 a 0,185 | 0,200 |
| degraus_n5_var12_custo_t2 | foco | 5 | 2000 | 0,356 | 0,336 a 0,377 | 0,200 |
| degraus_n5_var12_custo_t2 | descuidado_t2 | 5 | 8000 | 0,161 | 0,154 a 0,169 | 0,200 |
| degraus_n5_var12_custo_t4 | foco | 5 | 2000 | 0,420 | 0,397 a 0,442 | 0,200 |
| degraus_n5_var12_custo_t4 | descuidado_t4 | 5 | 8000 | 0,145 | 0,138 a 0,153 | 0,200 |
| n4_experiente_base | blefa_nunca_contesta_nunca | 4 | 2665 | 0,254 | 0,238 a 0,270 | 0,250 |
| n4_experiente_base | blefa_sempre_contesta_nunca | 4 | 1037 | 0,253 | 0,227 a 0,281 | 0,250 |
| n4_experiente_base | blefa_nunca_contesta_limiar | 4 | 3979 | 0,248 | 0,235 a 0,263 | 0,250 |
| n4_experiente_base | blefa_sempre_contesta_limiar | 4 | 319 | 0,226 | 0,182 a 0,273 | 0,250 |
| n4_experiente_var11_1_teste | blefa_nunca_contesta_nunca | 4 | 2665 | 0,267 | 0,250 a 0,282 | 0,250 |
| n4_experiente_var11_1_teste | blefa_sempre_contesta_limiar | 4 | 319 | 0,248 | 0,201 a 0,293 | 0,250 |
| n4_experiente_var11_1_teste | blefa_nunca_contesta_limiar | 4 | 3979 | 0,243 | 0,230 a 0,256 | 0,250 |
| n4_experiente_var11_1_teste | blefa_sempre_contesta_nunca | 4 | 1037 | 0,237 | 0,212 a 0,262 | 0,250 |
| n4_experiente_var11_2_testes | blefa_nunca_contesta_nunca | 4 | 2665 | 0,253 | 0,237 a 0,269 | 0,250 |
| n4_experiente_var11_2_testes | blefa_sempre_contesta_nunca | 4 | 1037 | 0,252 | 0,227 a 0,280 | 0,250 |
| n4_experiente_var11_2_testes | blefa_nunca_contesta_limiar | 4 | 3979 | 0,250 | 0,236 a 0,263 | 0,250 |
| n4_experiente_var11_2_testes | blefa_sempre_contesta_limiar | 4 | 319 | 0,215 | 0,172 a 0,262 | 0,250 |
| n4_experiente_var12_custo | blefa_nunca_contesta_nunca | 4 | 2665 | 0,257 | 0,239 a 0,274 | 0,250 |
| n4_experiente_var12_custo | blefa_nunca_contesta_limiar | 4 | 3979 | 0,251 | 0,238 a 0,263 | 0,250 |
| n4_experiente_var12_custo | blefa_sempre_contesta_nunca | 4 | 1037 | 0,241 | 0,215 a 0,265 | 0,250 |
| n4_experiente_var12_custo | blefa_sempre_contesta_limiar | 4 | 319 | 0,213 | 0,169 a 0,262 | 0,250 |
| n4_iniciante_base | blefa_sempre_contesta_limiar | 4 | 319 | 0,274 | 0,227 a 0,324 | 0,250 |
| n4_iniciante_base | blefa_nunca_contesta_nunca | 4 | 2665 | 0,258 | 0,241 a 0,274 | 0,250 |
| n4_iniciante_base | blefa_nunca_contesta_limiar | 4 | 3979 | 0,247 | 0,234 a 0,261 | 0,250 |
| n4_iniciante_base | blefa_sempre_contesta_nunca | 4 | 1037 | 0,234 | 0,208 a 0,259 | 0,250 |
| n4_iniciante_var11_1_teste | blefa_sempre_contesta_nunca | 4 | 1037 | 0,265 | 0,237 a 0,292 | 0,250 |
| n4_iniciante_var11_1_teste | blefa_nunca_contesta_nunca | 4 | 2665 | 0,251 | 0,236 a 0,267 | 0,250 |
| n4_iniciante_var11_1_teste | blefa_nunca_contesta_limiar | 4 | 3979 | 0,247 | 0,235 a 0,260 | 0,250 |
| n4_iniciante_var11_1_teste | blefa_sempre_contesta_limiar | 4 | 319 | 0,223 | 0,177 a 0,271 | 0,250 |
| n4_iniciante_var11_2_testes | blefa_sempre_contesta_nunca | 4 | 1037 | 0,254 | 0,228 a 0,280 | 0,250 |
| n4_iniciante_var11_2_testes | blefa_nunca_contesta_nunca | 4 | 2665 | 0,251 | 0,236 a 0,267 | 0,250 |
| n4_iniciante_var11_2_testes | blefa_nunca_contesta_limiar | 4 | 3979 | 0,249 | 0,236 a 0,262 | 0,250 |
| n4_iniciante_var11_2_testes | blefa_sempre_contesta_limiar | 4 | 319 | 0,238 | 0,190 a 0,290 | 0,250 |
| n4_iniciante_var12_custo | blefa_sempre_contesta_nunca | 4 | 1037 | 0,258 | 0,233 a 0,284 | 0,250 |
| n4_iniciante_var12_custo | blefa_nunca_contesta_nunca | 4 | 2665 | 0,249 | 0,234 a 0,265 | 0,250 |
| n4_iniciante_var12_custo | blefa_nunca_contesta_limiar | 4 | 3979 | 0,249 | 0,236 a 0,262 | 0,250 |
| n4_iniciante_var12_custo | blefa_sempre_contesta_limiar | 4 | 319 | 0,240 | 0,196 a 0,285 | 0,250 |
| n5_experiente_base | blefa_nunca_contesta_nunca | 5 | 3202 | 0,205 | 0,192 a 0,220 | 0,200 |
| n5_experiente_base | blefa_nunca_contesta_limiar | 5 | 5379 | 0,202 | 0,191 a 0,214 | 0,200 |
| n5_experiente_base | blefa_sempre_contesta_nunca | 5 | 1286 | 0,181 | 0,162 a 0,202 | 0,200 |
| n5_experiente_base | blefa_sempre_contesta_limiar | 5 | 133 | 0,173 | 0,113 a 0,233 | 0,200 |
| n5_experiente_var11_1_teste | blefa_sempre_contesta_nunca | 5 | 1286 | 0,209 | 0,188 a 0,233 | 0,200 |
| n5_experiente_var11_1_teste | blefa_nunca_contesta_limiar | 5 | 5379 | 0,199 | 0,189 a 0,209 | 0,200 |
| n5_experiente_var11_1_teste | blefa_nunca_contesta_nunca | 5 | 3202 | 0,199 | 0,186 a 0,212 | 0,200 |
| n5_experiente_var11_1_teste | blefa_sempre_contesta_limiar | 5 | 133 | 0,169 | 0,109 a 0,233 | 0,200 |
| n5_experiente_var11_2_testes | blefa_nunca_contesta_nunca | 5 | 3202 | 0,203 | 0,190 a 0,216 | 0,200 |
| n5_experiente_var11_2_testes | blefa_nunca_contesta_limiar | 5 | 5379 | 0,203 | 0,192 a 0,213 | 0,200 |
| n5_experiente_var11_2_testes | blefa_sempre_contesta_limiar | 5 | 133 | 0,192 | 0,124 a 0,263 | 0,200 |
| n5_experiente_var11_2_testes | blefa_sempre_contesta_nunca | 5 | 1286 | 0,181 | 0,159 a 0,200 | 0,200 |
| n5_experiente_var12_custo | blefa_sempre_contesta_limiar | 5 | 133 | 0,211 | 0,143 a 0,274 | 0,200 |
| n5_experiente_var12_custo | blefa_nunca_contesta_limiar | 5 | 5379 | 0,207 | 0,196 a 0,218 | 0,200 |
| n5_experiente_var12_custo | blefa_nunca_contesta_nunca | 5 | 3202 | 0,195 | 0,181 a 0,208 | 0,200 |
| n5_experiente_var12_custo | blefa_sempre_contesta_nunca | 5 | 1286 | 0,182 | 0,160 a 0,201 | 0,200 |
| n5_iniciante_base | blefa_nunca_contesta_nunca | 5 | 3202 | 0,215 | 0,202 a 0,230 | 0,200 |
| n5_iniciante_base | blefa_nunca_contesta_limiar | 5 | 5379 | 0,202 | 0,191 a 0,212 | 0,200 |
| n5_iniciante_base | blefa_sempre_contesta_nunca | 5 | 1286 | 0,163 | 0,144 a 0,183 | 0,200 |
| n5_iniciante_base | blefa_sempre_contesta_limiar | 5 | 133 | 0,120 | 0,068 a 0,180 | 0,200 |
| n5_iniciante_var11_1_teste | blefa_sempre_contesta_limiar | 5 | 133 | 0,211 | 0,143 a 0,278 | 0,200 |
| n5_iniciante_var11_1_teste | blefa_nunca_contesta_nunca | 5 | 3202 | 0,203 | 0,190 a 0,217 | 0,200 |
| n5_iniciante_var11_1_teste | blefa_sempre_contesta_nunca | 5 | 1286 | 0,201 | 0,179 a 0,225 | 0,200 |
| n5_iniciante_var11_1_teste | blefa_nunca_contesta_limiar | 5 | 5379 | 0,198 | 0,187 a 0,208 | 0,200 |
| n5_iniciante_var11_2_testes | blefa_nunca_contesta_nunca | 5 | 3202 | 0,208 | 0,195 a 0,222 | 0,200 |
| n5_iniciante_var11_2_testes | blefa_nunca_contesta_limiar | 5 | 5379 | 0,197 | 0,187 a 0,208 | 0,200 |
| n5_iniciante_var11_2_testes | blefa_sempre_contesta_nunca | 5 | 1286 | 0,196 | 0,175 a 0,218 | 0,200 |
| n5_iniciante_var11_2_testes | blefa_sempre_contesta_limiar | 5 | 133 | 0,165 | 0,105 a 0,226 | 0,200 |
| n5_iniciante_var12_custo | blefa_nunca_contesta_nunca | 5 | 3202 | 0,207 | 0,194 a 0,221 | 0,200 |
| n5_iniciante_var12_custo | blefa_nunca_contesta_limiar | 5 | 5379 | 0,199 | 0,188 a 0,210 | 0,200 |
| n5_iniciante_var12_custo | blefa_sempre_contesta_limiar | 5 | 133 | 0,195 | 0,128 a 0,263 | 0,200 |
| n5_iniciante_var12_custo | blefa_sempre_contesta_nunca | 5 | 1286 | 0,187 | 0,168 a 0,208 | 0,200 |

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903). Na v2 é só descrição: o placar em fichas não está na mesma escala dos pontos da v1, e a comparação entre as versões é feita pelo REQ-02 (autor, 2026-11-10).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| n4_iniciante_base | v2 | 4 | 2000 | **1,50** | 0,740 | 0,720 a 0,759 |
| n4_iniciante_base | v2 | 4 | 2000 | 1,25 | 0,937 | 0,925 a 0,947 |
| n4_iniciante_base | v2 | 4 | 2000 | 2,00 | 0,307 | 0,288 a 0,328 |
| n4_iniciante_var11_1_teste | v2 | 4 | 2000 | **1,50** | 0,626 | 0,605 a 0,647 |
| n4_iniciante_var11_1_teste | v2 | 4 | 2000 | 1,25 | 0,895 | 0,881 a 0,908 |
| n4_iniciante_var11_1_teste | v2 | 4 | 2000 | 2,00 | 0,131 | 0,117 a 0,146 |
| n4_iniciante_var11_2_testes | v2 | 4 | 2000 | **1,50** | 0,701 | 0,681 a 0,721 |
| n4_iniciante_var11_2_testes | v2 | 4 | 2000 | 1,25 | 0,918 | 0,905 a 0,929 |
| n4_iniciante_var11_2_testes | v2 | 4 | 2000 | 2,00 | 0,213 | 0,196 a 0,231 |
| n4_iniciante_var12_custo | v2 | 4 | 2000 | **1,50** | 0,743 | 0,723 a 0,761 |
| n4_iniciante_var12_custo | v2 | 4 | 2000 | 1,25 | 0,933 | 0,922 a 0,944 |
| n4_iniciante_var12_custo | v2 | 4 | 2000 | 2,00 | 0,289 | 0,270 a 0,310 |
| n4_experiente_base | v2 | 4 | 2000 | **1,50** | 0,679 | 0,659 a 0,700 |
| n4_experiente_base | v2 | 4 | 2000 | 1,25 | 0,923 | 0,911 a 0,934 |
| n4_experiente_base | v2 | 4 | 2000 | 2,00 | 0,222 | 0,204 a 0,241 |
| n4_experiente_var11_1_teste | v2 | 4 | 2000 | **1,50** | 0,539 | 0,518 a 0,561 |
| n4_experiente_var11_1_teste | v2 | 4 | 2000 | 1,25 | 0,886 | 0,871 a 0,899 |
| n4_experiente_var11_1_teste | v2 | 4 | 2000 | 2,00 | 0,101 | 0,088 a 0,114 |
| n4_experiente_var11_2_testes | v2 | 4 | 2000 | **1,50** | 0,628 | 0,607 a 0,649 |
| n4_experiente_var11_2_testes | v2 | 4 | 2000 | 1,25 | 0,890 | 0,876 a 0,903 |
| n4_experiente_var11_2_testes | v2 | 4 | 2000 | 2,00 | 0,142 | 0,127 a 0,158 |
| n4_experiente_var12_custo | v2 | 4 | 2000 | **1,50** | 0,723 | 0,702 a 0,742 |
| n4_experiente_var12_custo | v2 | 4 | 2000 | 1,25 | 0,929 | 0,917 a 0,939 |
| n4_experiente_var12_custo | v2 | 4 | 2000 | 2,00 | 0,243 | 0,225 a 0,263 |
| n5_iniciante_base | v2 | 5 | 2000 | **1,50** | 0,779 | 0,761 a 0,797 |
| n5_iniciante_base | v2 | 5 | 2000 | 1,25 | 0,972 | 0,963 a 0,978 |
| n5_iniciante_base | v2 | 5 | 2000 | 2,00 | 0,311 | 0,292 a 0,332 |
| n5_iniciante_var11_1_teste | v2 | 5 | 2000 | **1,50** | 0,632 | 0,611 a 0,653 |
| n5_iniciante_var11_1_teste | v2 | 5 | 2000 | 1,25 | 0,927 | 0,915 a 0,938 |
| n5_iniciante_var11_1_teste | v2 | 5 | 2000 | 2,00 | 0,124 | 0,111 a 0,140 |
| n5_iniciante_var11_2_testes | v2 | 5 | 2000 | **1,50** | 0,718 | 0,697 a 0,737 |
| n5_iniciante_var11_2_testes | v2 | 5 | 2000 | 1,25 | 0,959 | 0,949 a 0,967 |
| n5_iniciante_var11_2_testes | v2 | 5 | 2000 | 2,00 | 0,221 | 0,203 a 0,239 |
| n5_iniciante_var12_custo | v2 | 5 | 2000 | **1,50** | 0,781 | 0,762 a 0,799 |
| n5_iniciante_var12_custo | v2 | 5 | 2000 | 1,25 | 0,974 | 0,966 a 0,980 |
| n5_iniciante_var12_custo | v2 | 5 | 2000 | 2,00 | 0,319 | 0,298 a 0,339 |
| n5_experiente_base | v2 | 5 | 2000 | **1,50** | 0,689 | 0,668 a 0,709 |
| n5_experiente_base | v2 | 5 | 2000 | 1,25 | 0,949 | 0,938 a 0,957 |
| n5_experiente_base | v2 | 5 | 2000 | 2,00 | 0,196 | 0,179 a 0,214 |
| n5_experiente_var11_1_teste | v2 | 5 | 2000 | **1,50** | 0,551 | 0,530 a 0,573 |
| n5_experiente_var11_1_teste | v2 | 5 | 2000 | 1,25 | 0,927 | 0,915 a 0,938 |
| n5_experiente_var11_1_teste | v2 | 5 | 2000 | 2,00 | 0,093 | 0,081 a 0,107 |
| n5_experiente_var11_2_testes | v2 | 5 | 2000 | **1,50** | 0,635 | 0,614 a 0,656 |
| n5_experiente_var11_2_testes | v2 | 5 | 2000 | 1,25 | 0,945 | 0,934 a 0,954 |
| n5_experiente_var11_2_testes | v2 | 5 | 2000 | 2,00 | 0,146 | 0,131 a 0,162 |
| n5_experiente_var12_custo | v2 | 5 | 2000 | **1,50** | 0,759 | 0,740 a 0,778 |
| n5_experiente_var12_custo | v2 | 5 | 2000 | 1,25 | 0,965 | 0,955 a 0,972 |
| n5_experiente_var12_custo | v2 | 5 | 2000 | 2,00 | 0,259 | 0,240 a 0,279 |
| degraus_n4_base_t1 | v2 | 4 | 2000 | **1,50** | 0,785 | 0,766 a 0,802 |
| degraus_n4_base_t1 | v2 | 4 | 2000 | 1,25 | 0,958 | 0,948 a 0,966 |
| degraus_n4_base_t1 | v2 | 4 | 2000 | 2,00 | 0,343 | 0,322 a 0,364 |
| degraus_n4_base_t2 | v2 | 4 | 2000 | **1,50** | 0,802 | 0,784 a 0,819 |
| degraus_n4_base_t2 | v2 | 4 | 2000 | 1,25 | 0,957 | 0,947 a 0,965 |
| degraus_n4_base_t2 | v2 | 4 | 2000 | 2,00 | 0,397 | 0,376 a 0,419 |
| degraus_n4_base_t4 | v2 | 4 | 2000 | **1,50** | 0,849 | 0,833 a 0,864 |
| degraus_n4_base_t4 | v2 | 4 | 2000 | 1,25 | 0,971 | 0,963 a 0,977 |
| degraus_n4_base_t4 | v2 | 4 | 2000 | 2,00 | 0,454 | 0,432 a 0,475 |
| degraus_n4_var11_1_teste_t1 | v2 | 4 | 2000 | **1,50** | 0,658 | 0,637 a 0,679 |
| degraus_n4_var11_1_teste_t1 | v2 | 4 | 2000 | 1,25 | 0,912 | 0,899 a 0,924 |
| degraus_n4_var11_1_teste_t1 | v2 | 4 | 2000 | 2,00 | 0,150 | 0,136 a 0,167 |
| degraus_n4_var11_1_teste_t2 | v2 | 4 | 2000 | **1,50** | 0,706 | 0,685 a 0,725 |
| degraus_n4_var11_1_teste_t2 | v2 | 4 | 2000 | 1,25 | 0,932 | 0,921 a 0,943 |
| degraus_n4_var11_1_teste_t2 | v2 | 4 | 2000 | 2,00 | 0,210 | 0,193 a 0,229 |
| degraus_n4_var11_1_teste_t4 | v2 | 4 | 2000 | **1,50** | 0,722 | 0,702 a 0,741 |
| degraus_n4_var11_1_teste_t4 | v2 | 4 | 2000 | 1,25 | 0,933 | 0,922 a 0,944 |
| degraus_n4_var11_1_teste_t4 | v2 | 4 | 2000 | 2,00 | 0,222 | 0,204 a 0,240 |
| degraus_n4_var11_2_testes_t1 | v2 | 4 | 2000 | **1,50** | 0,727 | 0,707 a 0,746 |
| degraus_n4_var11_2_testes_t1 | v2 | 4 | 2000 | 1,25 | 0,935 | 0,924 a 0,945 |
| degraus_n4_var11_2_testes_t1 | v2 | 4 | 2000 | 2,00 | 0,253 | 0,234 a 0,272 |
| degraus_n4_var11_2_testes_t2 | v2 | 4 | 2000 | **1,50** | 0,769 | 0,750 a 0,787 |
| degraus_n4_var11_2_testes_t2 | v2 | 4 | 2000 | 1,25 | 0,951 | 0,940 a 0,959 |
| degraus_n4_var11_2_testes_t2 | v2 | 4 | 2000 | 2,00 | 0,309 | 0,290 a 0,330 |
| degraus_n4_var11_2_testes_t4 | v2 | 4 | 2000 | **1,50** | 0,794 | 0,776 a 0,812 |
| degraus_n4_var11_2_testes_t4 | v2 | 4 | 2000 | 1,25 | 0,960 | 0,950 a 0,967 |
| degraus_n4_var11_2_testes_t4 | v2 | 4 | 2000 | 2,00 | 0,346 | 0,326 a 0,368 |
| degraus_n4_var12_custo_t1 | v2 | 4 | 2000 | **1,50** | 0,802 | 0,784 a 0,819 |
| degraus_n4_var12_custo_t1 | v2 | 4 | 2000 | 1,25 | 0,962 | 0,952 a 0,969 |
| degraus_n4_var12_custo_t1 | v2 | 4 | 2000 | 2,00 | 0,370 | 0,349 a 0,391 |
| degraus_n4_var12_custo_t2 | v2 | 4 | 2000 | **1,50** | 0,840 | 0,823 a 0,855 |
| degraus_n4_var12_custo_t2 | v2 | 4 | 2000 | 1,25 | 0,964 | 0,955 a 0,971 |
| degraus_n4_var12_custo_t2 | v2 | 4 | 2000 | 2,00 | 0,433 | 0,411 a 0,455 |
| degraus_n4_var12_custo_t4 | v2 | 4 | 2000 | **1,50** | 0,884 | 0,870 a 0,898 |
| degraus_n4_var12_custo_t4 | v2 | 4 | 2000 | 1,25 | 0,976 | 0,968 a 0,982 |
| degraus_n4_var12_custo_t4 | v2 | 4 | 2000 | 2,00 | 0,517 | 0,495 a 0,539 |
| degraus_n5_base_t1 | v2 | 5 | 2000 | **1,50** | 0,794 | 0,776 a 0,812 |
| degraus_n5_base_t1 | v2 | 5 | 2000 | 1,25 | 0,976 | 0,968 a 0,982 |
| degraus_n5_base_t1 | v2 | 5 | 2000 | 2,00 | 0,329 | 0,309 a 0,350 |
| degraus_n5_base_t2 | v2 | 5 | 2000 | **1,50** | 0,836 | 0,819 a 0,851 |
| degraus_n5_base_t2 | v2 | 5 | 2000 | 1,25 | 0,977 | 0,969 a 0,982 |
| degraus_n5_base_t2 | v2 | 5 | 2000 | 2,00 | 0,397 | 0,375 a 0,418 |
| degraus_n5_base_t4 | v2 | 5 | 2000 | **1,50** | 0,866 | 0,850 a 0,880 |
| degraus_n5_base_t4 | v2 | 5 | 2000 | 1,25 | 0,980 | 0,973 a 0,985 |
| degraus_n5_base_t4 | v2 | 5 | 2000 | 2,00 | 0,449 | 0,427 a 0,470 |
| degraus_n5_var11_1_teste_t1 | v2 | 5 | 2000 | **1,50** | 0,654 | 0,633 a 0,675 |
| degraus_n5_var11_1_teste_t1 | v2 | 5 | 2000 | 1,25 | 0,942 | 0,930 a 0,951 |
| degraus_n5_var11_1_teste_t1 | v2 | 5 | 2000 | 2,00 | 0,142 | 0,128 a 0,159 |
| degraus_n5_var11_1_teste_t2 | v2 | 5 | 2000 | **1,50** | 0,691 | 0,670 a 0,711 |
| degraus_n5_var11_1_teste_t2 | v2 | 5 | 2000 | 1,25 | 0,953 | 0,943 a 0,961 |
| degraus_n5_var11_1_teste_t2 | v2 | 5 | 2000 | 2,00 | 0,188 | 0,171 a 0,205 |
| degraus_n5_var11_1_teste_t4 | v2 | 5 | 2000 | **1,50** | 0,742 | 0,722 a 0,760 |
| degraus_n5_var11_1_teste_t4 | v2 | 5 | 2000 | 1,25 | 0,962 | 0,953 a 0,970 |
| degraus_n5_var11_1_teste_t4 | v2 | 5 | 2000 | 2,00 | 0,238 | 0,220 a 0,257 |
| degraus_n5_var11_2_testes_t1 | v2 | 5 | 2000 | **1,50** | 0,751 | 0,732 a 0,769 |
| degraus_n5_var11_2_testes_t1 | v2 | 5 | 2000 | 1,25 | 0,968 | 0,959 a 0,975 |
| degraus_n5_var11_2_testes_t1 | v2 | 5 | 2000 | 2,00 | 0,233 | 0,215 a 0,252 |
| degraus_n5_var11_2_testes_t2 | v2 | 5 | 2000 | **1,50** | 0,791 | 0,773 a 0,808 |
| degraus_n5_var11_2_testes_t2 | v2 | 5 | 2000 | 1,25 | 0,981 | 0,973 a 0,986 |
| degraus_n5_var11_2_testes_t2 | v2 | 5 | 2000 | 2,00 | 0,298 | 0,279 a 0,319 |
| degraus_n5_var11_2_testes_t4 | v2 | 5 | 2000 | **1,50** | 0,824 | 0,806 a 0,840 |
| degraus_n5_var11_2_testes_t4 | v2 | 5 | 2000 | 1,25 | 0,975 | 0,967 a 0,981 |
| degraus_n5_var11_2_testes_t4 | v2 | 5 | 2000 | 2,00 | 0,347 | 0,327 a 0,369 |
| degraus_n5_var12_custo_t1 | v2 | 5 | 2000 | **1,50** | 0,869 | 0,854 a 0,883 |
| degraus_n5_var12_custo_t1 | v2 | 5 | 2000 | 1,25 | 0,987 | 0,981 a 0,991 |
| degraus_n5_var12_custo_t1 | v2 | 5 | 2000 | 2,00 | 0,431 | 0,410 a 0,453 |
| degraus_n5_var12_custo_t2 | v2 | 5 | 2000 | **1,50** | 0,894 | 0,880 a 0,907 |
| degraus_n5_var12_custo_t2 | v2 | 5 | 2000 | 1,25 | 0,989 | 0,983 a 0,992 |
| degraus_n5_var12_custo_t2 | v2 | 5 | 2000 | 2,00 | 0,505 | 0,484 a 0,527 |
| degraus_n5_var12_custo_t4 | v2 | 5 | 2000 | **1,50** | 0,895 | 0,881 a 0,908 |
| degraus_n5_var12_custo_t4 | v2 | 5 | 2000 | 1,25 | 0,989 | 0,983 a 0,993 |
| degraus_n5_var12_custo_t4 | v2 | 5 | 2000 | 2,00 | 0,557 | 0,535 a 0,579 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Sistema cheio no 1º Planejamento | Blefes por partida (bem-sucedidos) | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n4_iniciante_base | 2000 | 0 | 21,8 | 1,9 | 1,6% | 0,0% | 0,0% | 0,150 | 10,7 | 7,2 | 57,4% | 1,92 (25,1%) | 34,8 / 38,2 / 41,9 |
| n4_iniciante_var11_1_teste | 2000 | 0 | 8,6 | 0,8 | 3,2% | 0,0% | 0,0% | 0,228 | 9,3 | 6,8 | 58,5% | 0,80 (24,0%) | 26,3 / 28,2 / 30,2 |
| n4_iniciante_var11_2_testes | 2000 | 0 | 15,4 | 1,4 | 1,9% | 0,0% | 0,0% | 0,178 | 10,1 | 7,1 | 57,6% | 1,40 (24,7%) | 30,7 / 33,2 / 36,1 |
| n4_iniciante_var12_custo | 2000 | 0 | 15,6 | 1,4 | 2,2% | 0,0% | 0,0% | 0,182 | 8,3 | 5,6 | 58,5% | 1,41 (24,9%) | 30,2 / 33,5 / 36,8 |
| n4_experiente_base | 2000 | 0 | 21,9 | 3,2 | 2,9% | 0,0% | 0,0% | 0,189 | 12,1 | 8,5 | 51,5% | 2,00 (40,2%) | 34,9 / 38,5 / 42,4 |
| n4_experiente_var11_1_teste | 2000 | 0 | 8,8 | 1,4 | 5,5% | 0,0% | 0,0% | 0,223 | 10,8 | 8,0 | 52,7% | 0,84 (39,7%) | 26,6 / 28,3 / 30,5 |
| n4_experiente_var11_2_testes | 2000 | 0 | 15,7 | 2,4 | 2,8% | 0,0% | 0,0% | 0,214 | 11,5 | 8,3 | 51,8% | 1,46 (38,8%) | 30,8 / 33,5 / 36,5 |
| n4_experiente_var12_custo | 2000 | 0 | 15,9 | 2,3 | 3,0% | 0,0% | 0,0% | 0,209 | 9,7 | 6,7 | 52,7% | 1,50 (39,4%) | 30,3 / 33,7 / 37,4 |
| n5_iniciante_base | 2000 | 0 | 28,1 | 2,4 | 1,1% | 6,3% | 0,0% | 0,170 | 11,2 | 7,3 | 57,2% | 2,17 (23,0%) | 40,4 / 44,2 / 48,2 |
| n5_iniciante_var11_1_teste | 2000 | 0 | 11,0 | 1,0 | 3,5% | 5,1% | 0,0% | 0,225 | 9,6 | 6,8 | 57,8% | 0,86 (24,5%) | 29,7 / 31,4 / 33,6 |
| n5_iniciante_var11_2_testes | 2000 | 0 | 19,9 | 1,7 | 2,3% | 5,7% | 0,0% | 0,203 | 10,5 | 7,1 | 57,2% | 1,56 (22,6%) | 35,0 / 37,8 / 41,0 |
| n5_iniciante_var12_custo | 2000 | 0 | 20,9 | 1,8 | 1,8% | 5,9% | 0,0% | 0,191 | 8,5 | 5,5 | 57,8% | 1,64 (23,3%) | 35,1 / 38,6 / 42,7 |
| n5_experiente_base | 2000 | 0 | 28,2 | 3,9 | 2,2% | 8,3% | 0,0% | 0,179 | 12,6 | 8,5 | 50,5% | 2,30 (39,1%) | 40,6 / 44,6 / 48,8 |
| n5_experiente_var11_1_teste | 2000 | 0 | 11,3 | 1,7 | 5,5% | 7,8% | 0,0% | 0,274 | 11,2 | 8,0 | 51,3% | 0,93 (38,0%) | 29,8 / 31,8 / 34,0 |
| n5_experiente_var11_2_testes | 2000 | 0 | 20,3 | 2,9 | 3,3% | 8,2% | 0,0% | 0,209 | 12,0 | 8,4 | 50,6% | 1,68 (38,3%) | 35,3 / 38,2 / 41,5 |
| n5_experiente_var12_custo | 2000 | 0 | 21,3 | 3,0 | 4,2% | 8,2% | 0,0% | 0,216 | 10,0 | 6,6 | 51,3% | 1,77 (39,3%) | 35,3 / 39,1 / 43,2 |
| degraus_n4_base_t1_r0 | 500 | 0 | 21,6 | 7,9 | 1,4% | 0,0% | 0,0% | 0,143 | 12,6 | 8,3 | 43,0% | 5,35 (2,2%) | 38,2 / 42,0 / 45,5 |
| degraus_n4_base_t1_r1 | 500 | 0 | 21,4 | 7,8 | 1,2% | 0,0% | 0,0% | 0,162 | 12,7 | 8,4 | 43,8% | 5,19 (1,8%) | 38,2 / 41,8 / 45,1 |
| degraus_n4_base_t1_r2 | 500 | 0 | 21,5 | 7,9 | 1,8% | 0,0% | 0,0% | 0,168 | 12,6 | 8,4 | 43,0% | 5,34 (1,8%) | 38,5 / 41,9 / 45,4 |
| degraus_n4_base_t1_r3 | 500 | 0 | 21,6 | 8,0 | 1,4% | 0,0% | 0,0% | 0,144 | 12,7 | 8,4 | 43,3% | 5,47 (1,7%) | 38,7 / 42,2 / 45,4 |
| degraus_n4_base_t2_r0 | 500 | 0 | 21,5 | 7,9 | 1,6% | 0,0% | 0,0% | 0,153 | 12,6 | 8,2 | 36,4% | 5,36 (2,4%) | 38,2 / 42,1 / 45,4 |
| degraus_n4_base_t2_r1 | 500 | 0 | 21,3 | 7,7 | 2,0% | 0,0% | 0,0% | 0,163 | 12,5 | 8,1 | 38,7% | 5,23 (2,6%) | 38,1 / 41,8 / 45,3 |
| degraus_n4_base_t2_r2 | 500 | 0 | 21,5 | 7,6 | 2,6% | 0,0% | 0,0% | 0,201 | 12,5 | 8,2 | 36,6% | 5,28 (1,8%) | 38,1 / 42,0 / 45,3 |
| degraus_n4_base_t2_r3 | 500 | 0 | 21,6 | 7,8 | 1,6% | 0,0% | 0,0% | 0,188 | 12,7 | 8,1 | 37,7% | 5,31 (2,3%) | 38,2 / 42,1 / 45,6 |
| degraus_n4_base_t4_r0 | 500 | 0 | 21,7 | 8,0 | 1,8% | 0,0% | 0,0% | 0,103 | 12,5 | 7,9 | 32,7% | 5,61 (2,2%) | 38,2 / 42,0 / 46,0 |
| degraus_n4_base_t4_r1 | 500 | 0 | 21,5 | 7,9 | 0,8% | 0,0% | 0,0% | 0,185 | 12,5 | 7,9 | 34,5% | 5,45 (1,6%) | 37,8 / 41,9 / 45,5 |
| degraus_n4_base_t4_r2 | 500 | 0 | 21,7 | 7,8 | 1,8% | 0,0% | 0,0% | 0,143 | 12,4 | 7,9 | 33,4% | 5,43 (2,7%) | 38,1 / 42,0 / 45,8 |
| degraus_n4_base_t4_r3 | 500 | 0 | 21,7 | 7,9 | 1,4% | 0,0% | 0,0% | 0,145 | 12,7 | 7,9 | 34,6% | 5,53 (1,9%) | 38,2 / 42,0 / 46,0 |
| degraus_n4_var11_1_teste_t1_r0 | 500 | 0 | 9,0 | 3,6 | 4,0% | 0,0% | 0,0% | 0,224 | 11,0 | 7,9 | 43,8% | 2,35 (2,1%) | 28,5 / 30,4 / 32,2 |
| degraus_n4_var11_1_teste_t1_r1 | 500 | 0 | 9,0 | 3,6 | 4,2% | 0,0% | 0,0% | 0,256 | 11,1 | 7,9 | 45,1% | 2,39 (2,2%) | 28,2 / 30,3 / 32,3 |
| degraus_n4_var11_1_teste_t1_r2 | 500 | 0 | 9,1 | 3,7 | 3,8% | 0,0% | 0,0% | 0,217 | 11,1 | 7,9 | 43,5% | 2,37 (2,4%) | 28,2 / 30,3 / 32,2 |
| degraus_n4_var11_1_teste_t1_r3 | 500 | 0 | 9,0 | 3,5 | 2,8% | 0,0% | 0,0% | 0,228 | 11,0 | 7,9 | 44,2% | 2,29 (2,3%) | 28,2 / 30,2 / 32,2 |
| degraus_n4_var11_1_teste_t2_r0 | 500 | 0 | 9,2 | 3,6 | 3,4% | 0,0% | 0,0% | 0,205 | 10,9 | 7,7 | 37,4% | 2,37 (3,2%) | 28,5 / 30,5 / 32,5 |
| degraus_n4_var11_1_teste_t2_r1 | 500 | 0 | 9,1 | 3,6 | 1,8% | 0,0% | 0,0% | 0,223 | 11,0 | 7,6 | 39,9% | 2,40 (3,3%) | 28,4 / 30,3 / 32,4 |
| degraus_n4_var11_1_teste_t2_r2 | 500 | 0 | 9,2 | 3,7 | 2,8% | 0,0% | 0,0% | 0,256 | 11,1 | 7,7 | 37,5% | 2,53 (3,6%) | 28,5 / 30,4 / 32,6 |
| degraus_n4_var11_1_teste_t2_r3 | 500 | 0 | 9,2 | 3,6 | 4,0% | 0,0% | 0,0% | 0,239 | 10,8 | 7,6 | 38,5% | 2,31 (3,5%) | 28,5 / 30,4 / 32,3 |
| degraus_n4_var11_1_teste_t4_r0 | 500 | 0 | 9,4 | 3,6 | 4,0% | 0,0% | 0,0% | 0,237 | 10,7 | 7,4 | 33,3% | 2,40 (3,2%) | 28,5 / 30,7 / 32,8 |
| degraus_n4_var11_1_teste_t4_r1 | 500 | 0 | 9,3 | 3,5 | 5,2% | 0,0% | 0,0% | 0,221 | 10,8 | 7,5 | 35,3% | 2,43 (3,3%) | 28,5 / 30,5 / 32,3 |
| degraus_n4_var11_1_teste_t4_r2 | 500 | 0 | 9,4 | 3,7 | 4,0% | 0,0% | 0,0% | 0,247 | 10,8 | 7,5 | 33,7% | 2,48 (3,4%) | 28,5 / 30,6 / 32,9 |
| degraus_n4_var11_1_teste_t4_r3 | 500 | 0 | 9,3 | 3,6 | 3,0% | 0,0% | 0,0% | 0,223 | 10,5 | 7,4 | 34,9% | 2,47 (4,2%) | 28,5 / 30,6 / 32,5 |
| degraus_n4_var11_2_testes_t1_r0 | 500 | 0 | 15,7 | 6,1 | 2,4% | 0,0% | 0,0% | 0,175 | 12,0 | 8,2 | 43,1% | 4,12 (2,8%) | 33,7 / 36,5 / 39,3 |
| degraus_n4_var11_2_testes_t1_r1 | 500 | 0 | 15,7 | 5,9 | 2,8% | 0,0% | 0,0% | 0,214 | 12,0 | 8,3 | 43,8% | 3,87 (2,2%) | 33,6 / 36,2 / 39,3 |
| degraus_n4_var11_2_testes_t1_r2 | 500 | 0 | 15,6 | 6,1 | 1,4% | 0,0% | 0,0% | 0,198 | 12,0 | 8,3 | 42,9% | 4,07 (2,2%) | 33,7 / 36,4 / 39,3 |
| degraus_n4_var11_2_testes_t1_r3 | 500 | 0 | 15,7 | 6,1 | 2,4% | 0,0% | 0,0% | 0,160 | 12,0 | 8,3 | 43,3% | 4,11 (2,1%) | 33,7 / 36,7 / 39,1 |
| degraus_n4_var11_2_testes_t2_r0 | 500 | 0 | 16,0 | 6,0 | 2,8% | 0,0% | 0,0% | 0,188 | 11,7 | 8,0 | 36,8% | 4,11 (2,9%) | 33,7 / 36,9 / 39,7 |
| degraus_n4_var11_2_testes_t2_r1 | 500 | 0 | 15,8 | 6,0 | 2,2% | 0,0% | 0,0% | 0,186 | 11,9 | 8,0 | 39,1% | 4,06 (2,0%) | 33,7 / 36,5 / 39,7 |
| degraus_n4_var11_2_testes_t2_r2 | 500 | 0 | 15,9 | 6,0 | 1,4% | 0,0% | 0,0% | 0,193 | 12,0 | 8,1 | 36,8% | 4,10 (2,4%) | 33,9 / 36,7 / 39,7 |
| degraus_n4_var11_2_testes_t2_r3 | 500 | 0 | 15,9 | 5,9 | 1,0% | 0,0% | 0,0% | 0,189 | 11,9 | 7,9 | 38,0% | 4,05 (2,8%) | 33,7 / 36,5 / 39,4 |
| degraus_n4_var11_2_testes_t4_r0 | 500 | 0 | 16,1 | 6,1 | 3,2% | 0,0% | 0,0% | 0,170 | 11,7 | 7,8 | 33,1% | 4,32 (2,9%) | 33,8 / 36,9 / 40,3 |
| degraus_n4_var11_2_testes_t4_r1 | 500 | 0 | 16,0 | 6,1 | 1,4% | 0,0% | 0,0% | 0,200 | 11,9 | 7,8 | 34,6% | 4,17 (2,8%) | 33,9 / 36,8 / 39,5 |
| degraus_n4_var11_2_testes_t4_r2 | 500 | 0 | 16,1 | 6,0 | 1,8% | 0,0% | 0,0% | 0,231 | 11,8 | 7,8 | 33,4% | 4,17 (2,4%) | 34,0 / 36,8 / 39,7 |
| degraus_n4_var11_2_testes_t4_r3 | 500 | 0 | 16,1 | 6,1 | 0,6% | 0,0% | 0,0% | 0,186 | 11,8 | 7,7 | 34,7% | 4,20 (2,5%) | 33,7 / 36,8 / 39,9 |
| degraus_n4_var12_custo_t1_r0 | 500 | 0 | 17,7 | 6,6 | 3,4% | 0,0% | 0,0% | 0,193 | 9,8 | 6,4 | 43,8% | 4,43 (2,2%) | 34,7 / 38,3 / 42,1 |
| degraus_n4_var12_custo_t1_r1 | 500 | 0 | 17,6 | 6,6 | 2,6% | 0,0% | 0,0% | 0,206 | 9,9 | 6,5 | 45,1% | 4,41 (2,4%) | 34,3 / 38,3 / 42,2 |
| degraus_n4_var12_custo_t1_r2 | 500 | 0 | 17,7 | 6,6 | 1,8% | 0,0% | 0,0% | 0,179 | 9,8 | 6,5 | 43,5% | 4,36 (2,7%) | 34,7 / 38,3 / 42,1 |
| degraus_n4_var12_custo_t1_r3 | 500 | 0 | 17,6 | 6,5 | 1,2% | 0,0% | 0,0% | 0,232 | 9,9 | 6,5 | 44,2% | 4,36 (2,8%) | 34,5 / 38,2 / 41,9 |
| degraus_n4_var12_custo_t2_r0 | 500 | 0 | 18,8 | 6,8 | 2,8% | 0,0% | 0,0% | 0,178 | 9,6 | 6,1 | 37,4% | 4,58 (2,4%) | 35,2 / 39,5 / 43,1 |
| degraus_n4_var12_custo_t2_r1 | 500 | 0 | 18,7 | 6,8 | 2,4% | 0,0% | 0,0% | 0,166 | 9,6 | 6,1 | 39,9% | 4,67 (2,7%) | 35,6 / 39,2 / 43,0 |
| degraus_n4_var12_custo_t2_r2 | 500 | 0 | 18,7 | 6,8 | 0,6% | 0,0% | 0,0% | 0,203 | 9,7 | 6,1 | 37,5% | 4,71 (2,3%) | 35,8 / 39,2 / 42,9 |
| degraus_n4_var12_custo_t2_r3 | 500 | 0 | 18,6 | 6,7 | 1,8% | 0,0% | 0,0% | 0,210 | 9,6 | 6,1 | 38,5% | 4,58 (2,8%) | 35,2 / 39,2 / 42,9 |
| degraus_n4_var12_custo_t4_r0 | 500 | 0 | 19,3 | 7,1 | 0,6% | 0,0% | 0,0% | 0,194 | 9,7 | 5,9 | 33,3% | 4,95 (2,5%) | 36,1 / 39,8 / 43,8 |
| degraus_n4_var12_custo_t4_r1 | 500 | 0 | 19,4 | 7,1 | 2,2% | 0,0% | 0,0% | 0,172 | 9,6 | 5,9 | 35,3% | 4,96 (1,9%) | 36,2 / 39,9 / 43,7 |
| degraus_n4_var12_custo_t4_r2 | 500 | 0 | 19,4 | 6,9 | 2,6% | 0,0% | 0,0% | 0,203 | 9,6 | 5,9 | 33,7% | 4,82 (2,2%) | 36,2 / 40,1 / 43,5 |
| degraus_n4_var12_custo_t4_r3 | 500 | 0 | 19,2 | 7,1 | 2,2% | 0,0% | 0,0% | 0,188 | 9,8 | 5,9 | 34,9% | 4,96 (2,5%) | 36,2 / 39,8 / 43,7 |
| degraus_n5_base_t1_r0 | 400 | 0 | 27,8 | 9,9 | 1,8% | 10,8% | 0,0% | 0,175 | 13,2 | 8,4 | 42,0% | 7,08 (3,4%) | 45,8 / 49,5 / 52,8 |
| degraus_n5_base_t1_r1 | 400 | 0 | 27,8 | 10,0 | 1,2% | 8,8% | 0,0% | 0,124 | 13,1 | 8,4 | 42,8% | 6,89 (3,5%) | 45,5 / 49,2 / 53,1 |
| degraus_n5_base_t1_r2 | 400 | 0 | 27,9 | 9,9 | 1,8% | 8,8% | 0,0% | 0,172 | 13,0 | 8,4 | 42,8% | 6,96 (3,3%) | 45,6 / 49,3 / 53,0 |
| degraus_n5_base_t1_r3 | 400 | 0 | 27,8 | 9,9 | 1,5% | 9,0% | 0,0% | 0,173 | 13,2 | 8,4 | 42,2% | 6,96 (3,2%) | 45,5 / 49,4 / 52,8 |
| degraus_n5_base_t1_r4 | 400 | 0 | 27,8 | 9,8 | 1,8% | 9,5% | 0,0% | 0,149 | 13,2 | 8,5 | 42,1% | 7,10 (3,5%) | 45,3 / 49,4 / 52,5 |
| degraus_n5_base_t2_r0 | 400 | 0 | 28,0 | 9,9 | 2,2% | 11,0% | 0,0% | 0,149 | 13,2 | 8,2 | 35,2% | 7,24 (3,8%) | 45,3 / 49,5 / 53,6 |
| degraus_n5_base_t2_r1 | 400 | 0 | 27,9 | 9,8 | 2,5% | 7,0% | 0,0% | 0,121 | 13,1 | 8,2 | 36,2% | 7,15 (3,8%) | 45,7 / 49,2 / 53,3 |
| degraus_n5_base_t2_r2 | 400 | 0 | 27,9 | 9,8 | 2,2% | 11,8% | 0,0% | 0,176 | 13,1 | 8,2 | 36,1% | 7,06 (4,0%) | 45,1 / 49,6 / 53,5 |
| degraus_n5_base_t2_r3 | 400 | 0 | 28,1 | 9,9 | 2,5% | 12,2% | 0,0% | 0,140 | 13,0 | 8,1 | 35,9% | 7,10 (3,5%) | 45,7 / 49,8 / 53,5 |
| degraus_n5_base_t2_r4 | 400 | 0 | 27,8 | 9,9 | 1,5% | 13,8% | 0,0% | 0,146 | 13,3 | 8,2 | 36,4% | 7,09 (3,4%) | 45,4 / 49,5 / 52,8 |
| degraus_n5_base_t4_r0 | 400 | 0 | 28,3 | 10,0 | 2,2% | 11,5% | 0,0% | 0,127 | 12,9 | 7,9 | 31,2% | 7,29 (3,5%) | 45,3 / 49,9 / 53,3 |
| degraus_n5_base_t4_r1 | 400 | 0 | 28,2 | 9,7 | 2,2% | 9,5% | 0,0% | 0,170 | 13,1 | 8,0 | 32,5% | 7,08 (3,7%) | 45,2 / 49,4 / 53,7 |
| degraus_n5_base_t4_r2 | 400 | 0 | 28,2 | 9,8 | 1,5% | 12,2% | 0,0% | 0,222 | 12,9 | 7,9 | 32,7% | 7,01 (4,0%) | 45,7 / 49,4 / 53,4 |
| degraus_n5_base_t4_r3 | 400 | 0 | 28,3 | 9,9 | 2,2% | 12,2% | 0,0% | 0,133 | 12,9 | 8,0 | 32,9% | 7,17 (3,6%) | 45,3 / 49,7 / 53,8 |
| degraus_n5_base_t4_r4 | 400 | 0 | 28,4 | 9,7 | 2,2% | 13,2% | 0,0% | 0,170 | 13,0 | 7,9 | 33,1% | 7,11 (3,7%) | 45,5 / 49,5 / 53,4 |
| degraus_n5_var11_1_teste_t1_r0 | 400 | 0 | 11,6 | 4,7 | 6,5% | 13,0% | 0,0% | 0,251 | 11,3 | 7,9 | 43,2% | 3,02 (3,2%) | 32,2 / 34,4 / 36,8 |
| degraus_n5_var11_1_teste_t1_r1 | 400 | 0 | 11,6 | 4,6 | 6,2% | 8,0% | 0,0% | 0,246 | 11,4 | 7,9 | 44,6% | 3,04 (3,5%) | 32,4 / 34,3 / 36,6 |
| degraus_n5_var11_1_teste_t1_r2 | 400 | 0 | 11,6 | 4,6 | 4,5% | 9,0% | 0,0% | 0,234 | 11,5 | 8,0 | 44,1% | 3,08 (4,0%) | 32,2 / 34,4 / 36,5 |
| degraus_n5_var11_1_teste_t1_r3 | 400 | 0 | 11,6 | 4,6 | 3,8% | 9,5% | 0,0% | 0,163 | 11,4 | 7,9 | 43,6% | 2,96 (3,0%) | 32,1 / 34,3 / 36,7 |
| degraus_n5_var11_1_teste_t1_r4 | 400 | 0 | 11,7 | 4,7 | 4,0% | 8,8% | 0,0% | 0,203 | 11,4 | 7,9 | 43,3% | 3,15 (3,8%) | 32,2 / 34,4 / 36,7 |
| degraus_n5_var11_1_teste_t2_r0 | 400 | 0 | 12,0 | 4,6 | 5,5% | 10,8% | 0,0% | 0,214 | 11,4 | 7,6 | 35,6% | 3,21 (3,3%) | 32,4 / 34,8 / 37,2 |
| degraus_n5_var11_1_teste_t2_r1 | 400 | 0 | 11,9 | 4,7 | 4,8% | 9,2% | 0,0% | 0,219 | 11,2 | 7,7 | 36,6% | 3,26 (3,8%) | 32,4 / 34,7 / 37,2 |
| degraus_n5_var11_1_teste_t2_r2 | 400 | 0 | 12,0 | 4,6 | 2,8% | 11,8% | 0,0% | 0,195 | 11,2 | 7,7 | 36,8% | 3,22 (2,9%) | 32,6 / 34,8 / 37,2 |
| degraus_n5_var11_1_teste_t2_r3 | 400 | 0 | 11,9 | 4,7 | 4,2% | 13,0% | 0,0% | 0,214 | 11,3 | 7,6 | 36,4% | 3,15 (4,7%) | 32,5 / 34,8 / 37,0 |
| degraus_n5_var11_1_teste_t2_r4 | 400 | 0 | 11,9 | 4,5 | 4,8% | 13,0% | 0,0% | 0,186 | 11,2 | 7,6 | 36,8% | 3,17 (5,6%) | 32,2 / 34,7 / 36,9 |
| degraus_n5_var11_1_teste_t4_r0 | 400 | 0 | 12,2 | 4,6 | 3,5% | 12,2% | 0,0% | 0,203 | 11,0 | 7,4 | 31,3% | 3,18 (3,8%) | 32,8 / 34,9 / 37,0 |
| degraus_n5_var11_1_teste_t4_r1 | 400 | 0 | 12,1 | 4,6 | 3,0% | 6,8% | 0,0% | 0,204 | 11,3 | 7,5 | 32,9% | 3,38 (5,0%) | 32,8 / 34,7 / 36,8 |
| degraus_n5_var11_1_teste_t4_r2 | 400 | 0 | 12,1 | 4,7 | 2,2% | 13,2% | 0,0% | 0,242 | 11,0 | 7,4 | 33,2% | 3,28 (3,4%) | 32,6 / 34,9 / 36,9 |
| degraus_n5_var11_1_teste_t4_r3 | 400 | 0 | 12,2 | 4,6 | 5,0% | 14,2% | 0,0% | 0,287 | 11,2 | 7,4 | 33,0% | 3,18 (5,2%) | 32,5 / 34,8 / 37,2 |
| degraus_n5_var11_1_teste_t4_r4 | 400 | 0 | 12,0 | 4,6 | 2,8% | 11,2% | 0,0% | 0,224 | 11,2 | 7,4 | 33,4% | 3,13 (3,9%) | 32,4 / 34,8 / 37,2 |
| degraus_n5_var11_2_testes_t1_r0 | 400 | 0 | 20,5 | 7,8 | 2,5% | 9,5% | 0,0% | 0,143 | 12,4 | 8,3 | 42,0% | 5,45 (3,3%) | 39,4 / 42,6 / 45,8 |
| degraus_n5_var11_2_testes_t1_r1 | 400 | 0 | 20,4 | 7,8 | 3,8% | 9,5% | 0,0% | 0,183 | 12,5 | 8,3 | 42,9% | 5,32 (3,5%) | 39,2 / 42,4 / 45,2 |
| degraus_n5_var11_2_testes_t1_r2 | 400 | 0 | 20,4 | 7,7 | 5,2% | 7,8% | 0,0% | 0,178 | 12,5 | 8,3 | 42,8% | 5,35 (3,3%) | 39,4 / 42,5 / 45,6 |
| degraus_n5_var11_2_testes_t1_r3 | 400 | 0 | 20,4 | 7,7 | 2,2% | 10,5% | 0,0% | 0,199 | 12,5 | 8,3 | 42,3% | 5,26 (3,4%) | 39,2 / 42,4 / 45,8 |
| degraus_n5_var11_2_testes_t1_r4 | 400 | 0 | 20,3 | 7,7 | 2,0% | 11,2% | 0,0% | 0,166 | 12,5 | 8,3 | 42,2% | 5,31 (2,4%) | 38,9 / 42,5 / 45,3 |
| degraus_n5_var11_2_testes_t2_r0 | 400 | 0 | 20,8 | 7,7 | 1,8% | 11,2% | 0,0% | 0,177 | 12,5 | 8,0 | 35,3% | 5,37 (3,4%) | 39,5 / 42,9 / 46,2 |
| degraus_n5_var11_2_testes_t2_r1 | 400 | 0 | 20,7 | 7,7 | 1,5% | 7,2% | 0,0% | 0,144 | 12,5 | 8,1 | 36,2% | 5,52 (3,6%) | 39,8 / 42,7 / 46,0 |
| degraus_n5_var11_2_testes_t2_r2 | 400 | 0 | 20,7 | 7,9 | 2,0% | 10,0% | 0,0% | 0,226 | 12,3 | 8,0 | 36,2% | 5,47 (3,6%) | 39,5 / 43,0 / 45,9 |
| degraus_n5_var11_2_testes_t2_r3 | 400 | 0 | 20,8 | 7,7 | 2,8% | 11,8% | 0,0% | 0,190 | 12,3 | 8,0 | 35,8% | 5,45 (3,8%) | 39,8 / 42,8 / 46,3 |
| degraus_n5_var11_2_testes_t2_r4 | 400 | 0 | 20,7 | 7,7 | 2,5% | 13,8% | 0,0% | 0,170 | 12,4 | 8,0 | 36,4% | 5,40 (3,2%) | 39,2 / 42,8 / 46,0 |
| degraus_n5_var11_2_testes_t4_r0 | 400 | 0 | 21,3 | 7,8 | 2,5% | 12,2% | 0,0% | 0,216 | 12,2 | 7,8 | 31,2% | 5,73 (4,0%) | 39,9 / 43,4 / 46,5 |
| degraus_n5_var11_2_testes_t4_r1 | 400 | 0 | 21,1 | 7,6 | 4,0% | 11,5% | 0,0% | 0,176 | 12,3 | 7,8 | 32,6% | 5,46 (3,7%) | 39,8 / 43,1 / 46,4 |
| degraus_n5_var11_2_testes_t4_r2 | 400 | 0 | 21,1 | 7,7 | 3,5% | 12,5% | 0,0% | 0,247 | 12,2 | 7,7 | 32,8% | 5,43 (3,4%) | 39,8 / 43,1 / 46,2 |
| degraus_n5_var11_2_testes_t4_r3 | 400 | 0 | 20,9 | 7,7 | 3,8% | 17,8% | 0,0% | 0,212 | 12,3 | 7,8 | 32,9% | 5,56 (3,1%) | 39,5 / 42,9 / 46,2 |
| degraus_n5_var11_2_testes_t4_r4 | 400 | 0 | 21,0 | 7,7 | 1,8% | 13,2% | 0,0% | 0,196 | 12,3 | 7,8 | 33,1% | 5,49 (4,0%) | 39,3 / 43,0 / 46,2 |
| degraus_n5_var12_custo_t1_r0 | 400 | 0 | 23,4 | 8,5 | 1,2% | 12,0% | 0,0% | 0,169 | 10,3 | 6,3 | 43,2% | 5,98 (3,6%) | 41,2 / 45,0 / 49,1 |
| degraus_n5_var12_custo_t1_r1 | 400 | 0 | 23,8 | 8,5 | 1,8% | 10,2% | 0,0% | 0,244 | 10,2 | 6,3 | 44,6% | 5,92 (3,8%) | 41,5 / 45,8 / 49,5 |
| degraus_n5_var12_custo_t1_r2 | 400 | 0 | 23,5 | 8,6 | 3,0% | 7,8% | 0,0% | 0,203 | 10,2 | 6,3 | 44,1% | 6,08 (3,0%) | 41,2 / 45,5 / 49,6 |
| degraus_n5_var12_custo_t1_r3 | 400 | 0 | 23,5 | 8,3 | 3,0% | 9,8% | 0,0% | 0,198 | 10,3 | 6,4 | 43,6% | 5,88 (3,6%) | 41,4 / 45,2 / 49,3 |
| degraus_n5_var12_custo_t1_r4 | 400 | 0 | 23,6 | 8,6 | 1,5% | 9,0% | 0,0% | 0,155 | 10,3 | 6,3 | 43,3% | 6,03 (3,5%) | 41,4 / 45,3 / 49,7 |
| degraus_n5_var12_custo_t2_r0 | 400 | 0 | 25,1 | 8,9 | 2,8% | 12,5% | 0,0% | 0,201 | 10,2 | 6,0 | 35,6% | 6,46 (3,9%) | 42,2 / 46,8 / 51,1 |
| degraus_n5_var12_custo_t2_r1 | 400 | 0 | 25,0 | 8,9 | 2,0% | 8,8% | 0,0% | 0,171 | 10,1 | 6,0 | 36,6% | 6,36 (3,5%) | 42,5 / 46,7 / 51,1 |
| degraus_n5_var12_custo_t2_r2 | 400 | 0 | 24,9 | 8,9 | 2,5% | 10,8% | 0,0% | 0,149 | 10,1 | 6,0 | 36,8% | 6,37 (3,5%) | 42,8 / 46,6 / 50,8 |
| degraus_n5_var12_custo_t2_r3 | 400 | 0 | 25,0 | 8,9 | 2,8% | 11,2% | 0,0% | 0,172 | 10,0 | 6,0 | 36,4% | 6,38 (3,8%) | 43,2 / 46,6 / 50,5 |
| degraus_n5_var12_custo_t2_r4 | 400 | 0 | 25,0 | 8,8 | 2,2% | 12,2% | 0,0% | 0,211 | 10,0 | 6,0 | 36,8% | 6,33 (3,3%) | 41,8 / 46,9 / 51,1 |
| degraus_n5_var12_custo_t4_r0 | 400 | 0 | 25,9 | 9,1 | 2,8% | 14,2% | 0,0% | 0,174 | 10,0 | 5,8 | 31,3% | 6,57 (3,7%) | 43,2 / 47,5 / 51,3 |
| degraus_n5_var12_custo_t4_r1 | 400 | 0 | 25,8 | 9,1 | 2,0% | 10,0% | 0,0% | 0,182 | 9,9 | 5,8 | 32,9% | 6,65 (4,1%) | 43,4 / 47,2 / 51,3 |
| degraus_n5_var12_custo_t4_r2 | 400 | 0 | 25,6 | 9,1 | 2,2% | 12,0% | 0,0% | 0,253 | 9,9 | 5,8 | 33,2% | 6,45 (3,4%) | 43,2 / 47,2 / 50,9 |
| degraus_n5_var12_custo_t4_r3 | 400 | 0 | 26,0 | 9,2 | 3,0% | 13,2% | 0,0% | 0,203 | 9,8 | 5,8 | 33,0% | 6,64 (3,5%) | 43,8 / 47,8 / 51,5 |
| degraus_n5_var12_custo_t4_r4 | 400 | 0 | 25,8 | 9,1 | 1,8% | 14,5% | 0,0% | 0,208 | 9,9 | 5,7 | 33,4% | 6,64 (3,1%) | 42,9 / 47,4 / 51,6 |

## Equilíbrio dentro da partida (descrição)

Números sem critério de aceite; os vereditos, quando pedidos, estão na seção de requisitos. Razão de testes: máximo sobre a média de testes recebidos na partida (REQ-06a). Contra o menor: fração dos testes contra quem tinha o menor placar (REQ-06b). Zeradas: partidas com alguém em 0 ficha antes do último ciclo (REQ-07). Parado: percentil 90 do tempo parado por jogador e ciclo, pelos tempos provisórios do MOD-05 (REQ-10). Peso do dano: dano de incidente sobre as fichas movimentadas (REQ-13). Dispersão: placar do primeiro menos o do último no fim (REQ-14).

| Cenário | Razão de testes | Contra o menor | Zeradas | Parado p90 (min) | Peso do dano | Dispersão |
|---|---|---|---|---|---|---|
| n4_iniciante_base | 1,36 | 0,423 | 6,2% | 5,8 | 0,217 | 6,6 |
| n4_iniciante_var11_1_teste | 1,66 | 0,460 | 8,5% | 3,3 | 0,231 | 4,8 |
| n4_iniciante_var11_2_testes | 1,47 | 0,437 | 6,5% | 4,4 | 0,222 | 5,9 |
| n4_iniciante_var12_custo | 1,46 | 0,436 | 16,6% | 4,8 | 0,200 | 4,9 |
| n4_experiente_base | 1,37 | 0,428 | 4,7% | 5,8 | 0,174 | 7,1 |
| n4_experiente_var11_1_teste | 1,66 | 0,468 | 4,9% | 3,3 | 0,186 | 5,5 |
| n4_experiente_var11_2_testes | 1,47 | 0,441 | 4,7% | 4,6 | 0,178 | 6,3 |
| n4_experiente_var12_custo | 1,48 | 0,433 | 10,1% | 4,8 | 0,162 | 5,7 |
| n5_iniciante_base | 1,40 | 0,341 | 7,3% | 9,0 | 0,218 | 7,6 |
| n5_iniciante_var11_1_teste | 1,76 | 0,392 | 10,8% | 4,9 | 0,233 | 5,4 |
| n5_iniciante_var11_2_testes | 1,52 | 0,360 | 8,5% | 6,9 | 0,223 | 6,6 |
| n5_iniciante_var12_custo | 1,50 | 0,356 | 19,9% | 7,3 | 0,198 | 5,4 |
| n5_experiente_base | 1,43 | 0,339 | 5,9% | 9,2 | 0,174 | 8,0 |
| n5_experiente_var11_1_teste | 1,77 | 0,394 | 4,8% | 4,9 | 0,186 | 6,3 |
| n5_experiente_var11_2_testes | 1,53 | 0,359 | 4,7% | 6,9 | 0,179 | 7,2 |
| n5_experiente_var12_custo | 1,52 | 0,355 | 14,5% | 7,5 | 0,160 | 6,3 |
| degraus_n4_base_t1_r0 | 1,38 | 0,415 | 9,8% | 6,5 | 0,160 | 8,2 |
| degraus_n4_base_t1_r1 | 1,39 | 0,419 | 8,2% | 6,5 | 0,157 | 8,3 |
| degraus_n4_base_t1_r2 | 1,38 | 0,408 | 7,2% | 6,5 | 0,157 | 8,2 |
| degraus_n4_base_t1_r3 | 1,39 | 0,413 | 9,8% | 6,5 | 0,159 | 8,5 |
| degraus_n4_base_t2_r0 | 1,38 | 0,411 | 12,4% | 6,2 | 0,172 | 8,6 |
| degraus_n4_base_t2_r1 | 1,38 | 0,416 | 11,4% | 6,2 | 0,173 | 8,4 |
| degraus_n4_base_t2_r2 | 1,40 | 0,418 | 12,2% | 6,3 | 0,171 | 8,3 |
| degraus_n4_base_t2_r3 | 1,38 | 0,407 | 12,2% | 6,5 | 0,175 | 8,8 |
| degraus_n4_base_t4_r0 | 1,39 | 0,424 | 11,2% | 6,3 | 0,183 | 8,8 |
| degraus_n4_base_t4_r1 | 1,39 | 0,411 | 14,0% | 6,2 | 0,181 | 8,8 |
| degraus_n4_base_t4_r2 | 1,37 | 0,413 | 14,4% | 6,3 | 0,181 | 8,6 |
| degraus_n4_base_t4_r3 | 1,39 | 0,420 | 12,8% | 6,3 | 0,183 | 9,1 |
| degraus_n4_var11_1_teste_t1_r0 | 1,65 | 0,459 | 9,0% | 4,0 | 0,181 | 6,0 |
| degraus_n4_var11_1_teste_t1_r1 | 1,64 | 0,458 | 6,2% | 4,0 | 0,178 | 6,2 |
| degraus_n4_var11_1_teste_t1_r2 | 1,63 | 0,469 | 7,2% | 4,0 | 0,180 | 6,2 |
| degraus_n4_var11_1_teste_t1_r3 | 1,66 | 0,460 | 7,4% | 4,0 | 0,182 | 6,0 |
| degraus_n4_var11_1_teste_t2_r0 | 1,64 | 0,455 | 9,2% | 4,0 | 0,195 | 6,2 |
| degraus_n4_var11_1_teste_t2_r1 | 1,68 | 0,452 | 7,8% | 4,0 | 0,194 | 6,4 |
| degraus_n4_var11_1_teste_t2_r2 | 1,67 | 0,472 | 10,4% | 4,0 | 0,193 | 6,5 |
| degraus_n4_var11_1_teste_t2_r3 | 1,63 | 0,467 | 11,6% | 4,0 | 0,197 | 6,1 |
| degraus_n4_var11_1_teste_t4_r0 | 1,65 | 0,456 | 8,8% | 4,0 | 0,207 | 6,3 |
| degraus_n4_var11_1_teste_t4_r1 | 1,66 | 0,469 | 10,4% | 4,0 | 0,206 | 6,4 |
| degraus_n4_var11_1_teste_t4_r2 | 1,62 | 0,460 | 10,6% | 4,0 | 0,204 | 6,4 |
| degraus_n4_var11_1_teste_t4_r3 | 1,63 | 0,464 | 12,2% | 4,0 | 0,208 | 6,1 |
| degraus_n4_var11_2_testes_t1_r0 | 1,46 | 0,435 | 9,0% | 5,2 | 0,167 | 7,3 |
| degraus_n4_var11_2_testes_t1_r1 | 1,46 | 0,433 | 7,8% | 5,1 | 0,165 | 7,3 |
| degraus_n4_var11_2_testes_t1_r2 | 1,46 | 0,427 | 6,8% | 5,2 | 0,165 | 7,3 |
| degraus_n4_var11_2_testes_t1_r3 | 1,48 | 0,437 | 8,8% | 5,2 | 0,167 | 7,3 |
| degraus_n4_var11_2_testes_t2_r0 | 1,46 | 0,429 | 11,0% | 5,2 | 0,181 | 7,3 |
| degraus_n4_var11_2_testes_t2_r1 | 1,47 | 0,435 | 10,8% | 5,2 | 0,179 | 7,5 |
| degraus_n4_var11_2_testes_t2_r2 | 1,45 | 0,431 | 12,6% | 5,2 | 0,179 | 7,6 |
| degraus_n4_var11_2_testes_t2_r3 | 1,46 | 0,430 | 14,6% | 5,1 | 0,184 | 7,6 |
| degraus_n4_var11_2_testes_t4_r0 | 1,45 | 0,435 | 10,2% | 5,1 | 0,192 | 7,5 |
| degraus_n4_var11_2_testes_t4_r1 | 1,48 | 0,434 | 15,6% | 5,1 | 0,188 | 7,8 |
| degraus_n4_var11_2_testes_t4_r2 | 1,47 | 0,434 | 12,8% | 5,2 | 0,190 | 7,7 |
| degraus_n4_var11_2_testes_t4_r3 | 1,45 | 0,427 | 11,6% | 5,1 | 0,192 | 7,7 |
| degraus_n4_var12_custo_t1_r0 | 1,43 | 0,421 | 20,4% | 5,6 | 0,146 | 6,3 |
| degraus_n4_var12_custo_t1_r1 | 1,43 | 0,414 | 19,6% | 5,6 | 0,146 | 6,3 |
| degraus_n4_var12_custo_t1_r2 | 1,43 | 0,419 | 23,0% | 5,6 | 0,146 | 6,2 |
| degraus_n4_var12_custo_t1_r3 | 1,45 | 0,423 | 19,4% | 5,6 | 0,149 | 6,4 |
| degraus_n4_var12_custo_t2_r0 | 1,46 | 0,424 | 29,2% | 5,7 | 0,157 | 6,4 |
| degraus_n4_var12_custo_t2_r1 | 1,43 | 0,412 | 27,2% | 5,7 | 0,155 | 6,4 |
| degraus_n4_var12_custo_t2_r2 | 1,44 | 0,417 | 26,8% | 5,8 | 0,155 | 6,4 |
| degraus_n4_var12_custo_t2_r3 | 1,42 | 0,412 | 30,8% | 5,7 | 0,158 | 6,4 |
| degraus_n4_var12_custo_t4_r0 | 1,43 | 0,426 | 35,8% | 5,7 | 0,163 | 6,8 |
| degraus_n4_var12_custo_t4_r1 | 1,41 | 0,424 | 32,2% | 5,9 | 0,161 | 6,7 |
| degraus_n4_var12_custo_t4_r2 | 1,43 | 0,426 | 31,0% | 5,8 | 0,161 | 6,7 |
| degraus_n4_var12_custo_t4_r3 | 1,43 | 0,420 | 35,0% | 5,8 | 0,163 | 6,8 |
| degraus_n5_base_t1_r0 | 1,41 | 0,329 | 16,8% | 10,3 | 0,160 | 9,2 |
| degraus_n5_base_t1_r1 | 1,43 | 0,328 | 13,5% | 10,3 | 0,161 | 9,1 |
| degraus_n5_base_t1_r2 | 1,43 | 0,332 | 15,2% | 10,3 | 0,161 | 9,1 |
| degraus_n5_base_t1_r3 | 1,45 | 0,325 | 13,0% | 10,3 | 0,160 | 9,2 |
| degraus_n5_base_t1_r4 | 1,44 | 0,332 | 12,0% | 10,2 | 0,160 | 9,1 |
| degraus_n5_base_t2_r0 | 1,43 | 0,327 | 15,0% | 10,2 | 0,175 | 9,6 |
| degraus_n5_base_t2_r1 | 1,43 | 0,328 | 16,5% | 10,1 | 0,172 | 9,4 |
| degraus_n5_base_t2_r2 | 1,42 | 0,338 | 13,8% | 10,1 | 0,172 | 9,4 |
| degraus_n5_base_t2_r3 | 1,43 | 0,323 | 16,2% | 10,2 | 0,173 | 9,2 |
| degraus_n5_base_t2_r4 | 1,45 | 0,340 | 15,0% | 10,2 | 0,173 | 9,6 |
| degraus_n5_base_t4_r0 | 1,43 | 0,336 | 16,5% | 9,9 | 0,184 | 9,5 |
| degraus_n5_base_t4_r1 | 1,46 | 0,342 | 16,8% | 9,9 | 0,181 | 9,6 |
| degraus_n5_base_t4_r2 | 1,43 | 0,343 | 17,8% | 10,1 | 0,183 | 9,4 |
| degraus_n5_base_t4_r3 | 1,44 | 0,332 | 16,2% | 10,1 | 0,184 | 9,4 |
| degraus_n5_base_t4_r4 | 1,45 | 0,339 | 15,5% | 10,1 | 0,184 | 9,6 |
| degraus_n5_var11_1_teste_t1_r0 | 1,75 | 0,388 | 8,5% | 5,7 | 0,182 | 6,7 |
| degraus_n5_var11_1_teste_t1_r1 | 1,78 | 0,373 | 11,5% | 5,6 | 0,183 | 6,7 |
| degraus_n5_var11_1_teste_t1_r2 | 1,77 | 0,382 | 10,5% | 5,6 | 0,182 | 6,8 |
| degraus_n5_var11_1_teste_t1_r3 | 1,75 | 0,386 | 9,5% | 5,6 | 0,181 | 6,8 |
| degraus_n5_var11_1_teste_t1_r4 | 1,74 | 0,384 | 10,0% | 5,6 | 0,181 | 6,8 |
| degraus_n5_var11_1_teste_t2_r0 | 1,74 | 0,377 | 13,8% | 5,7 | 0,198 | 7,0 |
| degraus_n5_var11_1_teste_t2_r1 | 1,77 | 0,380 | 10,5% | 5,6 | 0,193 | 6,8 |
| degraus_n5_var11_1_teste_t2_r2 | 1,76 | 0,376 | 11,2% | 5,6 | 0,194 | 6,7 |
| degraus_n5_var11_1_teste_t2_r3 | 1,76 | 0,389 | 10,8% | 5,8 | 0,195 | 6,9 |
| degraus_n5_var11_1_teste_t2_r4 | 1,72 | 0,385 | 12,8% | 5,6 | 0,199 | 6,8 |
| degraus_n5_var11_1_teste_t4_r0 | 1,73 | 0,378 | 11,5% | 5,6 | 0,209 | 6,9 |
| degraus_n5_var11_1_teste_t4_r1 | 1,73 | 0,393 | 11,0% | 5,6 | 0,204 | 7,0 |
| degraus_n5_var11_1_teste_t4_r2 | 1,73 | 0,394 | 12,0% | 5,6 | 0,204 | 6,8 |
| degraus_n5_var11_1_teste_t4_r3 | 1,75 | 0,399 | 15,0% | 5,6 | 0,208 | 7,0 |
| degraus_n5_var11_1_teste_t4_r4 | 1,75 | 0,407 | 12,5% | 5,6 | 0,210 | 7,1 |
| degraus_n5_var11_2_testes_t1_r0 | 1,52 | 0,348 | 12,8% | 8,0 | 0,167 | 8,1 |
| degraus_n5_var11_2_testes_t1_r1 | 1,53 | 0,355 | 14,0% | 7,9 | 0,169 | 8,3 |
| degraus_n5_var11_2_testes_t1_r2 | 1,54 | 0,348 | 11,8% | 7,9 | 0,168 | 8,2 |
| degraus_n5_var11_2_testes_t1_r3 | 1,54 | 0,341 | 14,0% | 7,9 | 0,168 | 8,1 |
| degraus_n5_var11_2_testes_t1_r4 | 1,53 | 0,342 | 12,5% | 7,8 | 0,167 | 8,2 |
| degraus_n5_var11_2_testes_t2_r0 | 1,53 | 0,353 | 15,0% | 7,9 | 0,181 | 8,5 |
| degraus_n5_var11_2_testes_t2_r1 | 1,53 | 0,347 | 17,2% | 7,8 | 0,179 | 8,4 |
| degraus_n5_var11_2_testes_t2_r2 | 1,53 | 0,346 | 13,2% | 7,8 | 0,179 | 8,4 |
| degraus_n5_var11_2_testes_t2_r3 | 1,52 | 0,340 | 13,0% | 7,9 | 0,182 | 8,2 |
| degraus_n5_var11_2_testes_t2_r4 | 1,52 | 0,353 | 11,8% | 7,9 | 0,181 | 8,4 |
| degraus_n5_var11_2_testes_t4_r0 | 1,53 | 0,351 | 16,5% | 7,8 | 0,193 | 8,4 |
| degraus_n5_var11_2_testes_t4_r1 | 1,54 | 0,354 | 15,5% | 7,8 | 0,190 | 8,4 |
| degraus_n5_var11_2_testes_t4_r2 | 1,54 | 0,351 | 17,0% | 7,9 | 0,192 | 8,4 |
| degraus_n5_var11_2_testes_t4_r3 | 1,55 | 0,343 | 18,2% | 7,8 | 0,193 | 8,5 |
| degraus_n5_var11_2_testes_t4_r4 | 1,55 | 0,359 | 13,5% | 7,8 | 0,191 | 8,4 |
| degraus_n5_var12_custo_t1_r0 | 1,49 | 0,341 | 31,2% | 9,0 | 0,147 | 7,2 |
| degraus_n5_var12_custo_t1_r1 | 1,48 | 0,333 | 31,2% | 9,3 | 0,146 | 7,2 |
| degraus_n5_var12_custo_t1_r2 | 1,49 | 0,329 | 30,8% | 9,2 | 0,145 | 7,1 |
| degraus_n5_var12_custo_t1_r3 | 1,49 | 0,336 | 29,0% | 9,1 | 0,144 | 7,1 |
| degraus_n5_var12_custo_t1_r4 | 1,49 | 0,338 | 30,5% | 9,2 | 0,145 | 7,1 |
| degraus_n5_var12_custo_t2_r0 | 1,48 | 0,337 | 40,0% | 9,4 | 0,154 | 7,3 |
| degraus_n5_var12_custo_t2_r1 | 1,48 | 0,335 | 35,2% | 9,4 | 0,152 | 7,4 |
| degraus_n5_var12_custo_t2_r2 | 1,47 | 0,342 | 36,2% | 9,4 | 0,153 | 7,2 |
| degraus_n5_var12_custo_t2_r3 | 1,47 | 0,340 | 37,8% | 9,3 | 0,153 | 7,2 |
| degraus_n5_var12_custo_t2_r4 | 1,47 | 0,345 | 38,2% | 9,4 | 0,155 | 7,2 |
| degraus_n5_var12_custo_t4_r0 | 1,48 | 0,341 | 44,0% | 9,3 | 0,162 | 7,4 |
| degraus_n5_var12_custo_t4_r1 | 1,47 | 0,344 | 44,0% | 9,4 | 0,158 | 7,3 |
| degraus_n5_var12_custo_t4_r2 | 1,46 | 0,343 | 44,0% | 9,3 | 0,161 | 7,3 |
| degraus_n5_var12_custo_t4_r3 | 1,46 | 0,332 | 42,2% | 9,5 | 0,161 | 7,1 |
| degraus_n5_var12_custo_t4_r4 | 1,49 | 0,346 | 45,8% | 9,4 | 0,162 | 7,3 |

## Profundidade (descrição)

Números sem critério de aceite (autor, 2026-11-11), com o intervalo de 95% entre parênteses. Defesas: testes por partida divididos por N, porque cada teste é uma defesa. Com escolha: decisões com 2 ou mais opções legais, por jogador e por partida (MET-08). Apertadas: fração das decisões que o Heurístico avalia por valor (compra, colocação e ação na Homologação) em que a segunda melhor opção fica a menos do limiar da melhor (MET-08). Trocas de líder: vezes por partida em que o líder isolado passa a ser outro jogador, conferidas a cada mudança de placar (MET-09). Recuperação: nas partidas com líder isolado no fim do ciclo 1, a fração da vitória que ficou com outro jogador (MET-09). Foco ÷ 1/N: a taxa de vitória do Heurístico normal numa mesa de Heurísticos mais descuidados, dividida por 1/N; 1 é jogar tão bem quanto eles (MET-10).

| Cenário | Partidas | Defesas por jogador | Com escolha por jogador | Apertadas | Trocas de líder | Recuperação | Foco ÷ 1/N |
|---|---|---|---|---|---|---|---|
| n4_iniciante_base | 2000 | 5,44 (5,41 a 5,46) | 32,6 (32,5 a 32,7) | 0,828 (0,826 a 0,830) | 3,50 (3,41 a 3,58) | 0,600 (0,572 a 0,628) | — |
| n4_iniciante_var11_1_teste | 2000 | 2,15 (2,13 a 2,16) | 22,2 (22,2 a 22,3) | 0,849 (0,847 a 0,851) | 3,59 (3,51 a 3,67) | 0,522 (0,497 a 0,549) | — |
| n4_iniciante_var11_2_testes | 2000 | 3,85 (3,83 a 3,87) | 27,4 (27,3 a 27,5) | 0,847 (0,845 a 0,849) | 3,53 (3,44 a 3,62) | 0,572 (0,543 a 0,596) | — |
| n4_iniciante_var12_custo | 2000 | 3,89 (3,86 a 3,92) | 28,9 (28,8 a 29,0) | 0,814 (0,812 a 0,817) | 3,83 (3,73 a 3,94) | 0,568 (0,542 a 0,596) | — |
| n4_experiente_base | 2000 | 5,49 (5,46 a 5,51) | 33,7 (33,6 a 33,8) | 0,812 (0,809 a 0,814) | 3,60 (3,51 a 3,69) | 0,561 (0,533 a 0,589) | — |
| n4_experiente_var11_1_teste | 2000 | 2,21 (2,19 a 2,22) | 22,9 (22,8 a 22,9) | 0,815 (0,812 a 0,817) | 3,54 (3,46 a 3,62) | 0,527 (0,496 a 0,556) | — |
| n4_experiente_var11_2_testes | 2000 | 3,93 (3,91 a 3,95) | 28,4 (28,3 a 28,4) | 0,822 (0,820 a 0,824) | 3,62 (3,53 a 3,71) | 0,536 (0,508 a 0,567) | — |
| n4_experiente_var12_custo | 2000 | 3,96 (3,93 a 4,00) | 29,9 (29,8 a 30,0) | 0,788 (0,785 a 0,790) | 3,88 (3,77 a 3,97) | 0,541 (0,511 a 0,571) | — |
| n5_iniciante_base | 2000 | 5,62 (5,60 a 5,64) | 32,7 (32,6 a 32,8) | 0,830 (0,828 a 0,831) | 3,96 (3,87 a 4,05) | 0,630 (0,602 a 0,655) | — |
| n5_iniciante_var11_1_teste | 2000 | 2,20 (2,19 a 2,21) | 22,2 (22,2 a 22,3) | 0,844 (0,842 a 0,846) | 3,98 (3,89 a 4,06) | 0,575 (0,547 a 0,604) | — |
| n5_iniciante_var11_2_testes | 2000 | 3,98 (3,96 a 3,99) | 27,5 (27,4 a 27,5) | 0,845 (0,843 a 0,847) | 3,99 (3,89 a 4,08) | 0,597 (0,570 a 0,626) | — |
| n5_iniciante_var12_custo | 2000 | 4,18 (4,16 a 4,21) | 29,4 (29,4 a 29,5) | 0,806 (0,804 a 0,808) | 4,34 (4,25 a 4,45) | 0,609 (0,582 a 0,637) | — |
| n5_experiente_base | 2000 | 5,65 (5,63 a 5,67) | 33,7 (33,7 a 33,8) | 0,815 (0,813 a 0,817) | 4,16 (4,06 a 4,24) | 0,621 (0,594 a 0,651) | — |
| n5_experiente_var11_1_teste | 2000 | 2,26 (2,25 a 2,27) | 22,8 (22,8 a 22,9) | 0,814 (0,812 a 0,817) | 3,88 (3,81 a 3,97) | 0,526 (0,494 a 0,556) | — |
| n5_experiente_var11_2_testes | 2000 | 4,05 (4,04 a 4,07) | 28,4 (28,3 a 28,5) | 0,821 (0,819 a 0,824) | 4,01 (3,92 a 4,10) | 0,591 (0,560 a 0,619) | — |
| n5_experiente_var12_custo | 2000 | 4,26 (4,24 a 4,29) | 30,4 (30,3 a 30,5) | 0,785 (0,782 a 0,787) | 4,32 (4,22 a 4,41) | 0,584 (0,557 a 0,613) | — |
| degraus_n4_base_t1 | 2000 | 5,38 (5,35 a 5,40) | — | — | — | — | 1,31 (1,24 a 1,40) |
| degraus_n4_base_t2 | 2000 | 5,37 (5,34 a 5,40) | — | — | — | — | 1,58 (1,49 a 1,66) |
| degraus_n4_base_t4 | 2000 | 5,41 (5,38 a 5,44) | — | — | — | — | 1,88 (1,78 a 1,96) |
| degraus_n4_var11_1_teste_t1 | 2000 | 2,25 (2,24 a 2,27) | — | — | — | — | 1,21 (1,14 a 1,29) |
| degraus_n4_var11_1_teste_t2 | 2000 | 2,29 (2,28 a 2,31) | — | — | — | — | 1,51 (1,42 a 1,59) |
| degraus_n4_var11_1_teste_t4 | 2000 | 2,34 (2,33 a 2,36) | — | — | — | — | 1,60 (1,52 a 1,68) |
| degraus_n4_var11_2_testes_t1 | 2000 | 3,91 (3,89 a 3,93) | — | — | — | — | 1,27 (1,19 a 1,36) |
| degraus_n4_var11_2_testes_t2 | 2000 | 3,97 (3,95 a 3,99) | — | — | — | — | 1,51 (1,43 a 1,60) |
| degraus_n4_var11_2_testes_t4 | 2000 | 4,02 (4,00 a 4,04) | — | — | — | — | 1,68 (1,59 a 1,76) |
| degraus_n4_var12_custo_t1 | 2000 | 4,41 (4,38 a 4,44) | — | — | — | — | 1,29 (1,20 a 1,37) |
| degraus_n4_var12_custo_t2 | 2000 | 4,67 (4,64 a 4,70) | — | — | — | — | 1,61 (1,52 a 1,69) |
| degraus_n4_var12_custo_t4 | 2000 | 4,83 (4,80 a 4,86) | — | — | — | — | 1,86 (1,77 a 1,94) |
| degraus_n5_base_t1 | 2000 | 5,56 (5,54 a 5,58) | — | — | — | — | 1,43 (1,33 a 1,53) |
| degraus_n5_base_t2 | 2000 | 5,59 (5,56 a 5,61) | — | — | — | — | 1,83 (1,73 a 1,94) |
| degraus_n5_base_t4 | 2000 | 5,65 (5,63 a 5,68) | — | — | — | — | 2,10 (1,99 a 2,21) |
| degraus_n5_var11_1_teste_t1 | 2000 | 2,32 (2,31 a 2,33) | — | — | — | — | 1,28 (1,19 a 1,38) |
| degraus_n5_var11_1_teste_t2 | 2000 | 2,39 (2,37 a 2,40) | — | — | — | — | 1,55 (1,45 a 1,65) |
| degraus_n5_var11_1_teste_t4 | 2000 | 2,42 (2,41 a 2,44) | — | — | — | — | 1,78 (1,67 a 1,88) |
| degraus_n5_var11_2_testes_t1 | 2000 | 4,08 (4,06 a 4,09) | — | — | — | — | 1,36 (1,27 a 1,46) |
| degraus_n5_var11_2_testes_t2 | 2000 | 4,15 (4,13 a 4,17) | — | — | — | — | 1,68 (1,58 a 1,78) |
| degraus_n5_var11_2_testes_t4 | 2000 | 4,21 (4,19 a 4,23) | — | — | — | — | 1,92 (1,82 a 2,03) |
| degraus_n5_var12_custo_t1 | 2000 | 4,71 (4,68 a 4,74) | — | — | — | — | 1,48 (1,39 a 1,58) |
| degraus_n5_var12_custo_t2 | 2000 | 5,00 (4,97 a 5,02) | — | — | — | — | 1,78 (1,68 a 1,88) |
| degraus_n5_var12_custo_t4 | 2000 | 5,16 (5,13 a 5,19) | — | — | — | — | 2,10 (1,99 a 2,21) |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| n4_iniciante_base | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_iniciante_var11_1_teste | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| n4_iniciante_var11_2_testes | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| n4_iniciante_var12_custo | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| n4_experiente_base | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_experiente_var11_1_teste | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| n4_experiente_var11_2_testes | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| n4_experiente_var12_custo | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| n5_iniciante_base | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_iniciante_var11_1_teste | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| n5_iniciante_var11_2_testes | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| n5_iniciante_var12_custo | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| n5_experiente_base | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_experiente_var11_1_teste | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| n5_experiente_var11_2_testes | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| n5_experiente_var12_custo | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_base_t1_r0 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t1_r1 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t1_r2 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t1_r3 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t2_r0 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t2_r1 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t2_r2 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t2_r3 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t4_r0 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t4_r1 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t4_r2 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_base_t4_r3 | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n4_var11_1_teste_t1_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t1_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t1_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t1_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t2_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t2_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t2_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t2_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t4_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t4_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t4_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_1_teste_t4_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n4_var11_2_testes_t1_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t1_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t1_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t1_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t2_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t2_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t2_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t2_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t4_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t4_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t4_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var11_2_testes_t4_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n4_var12_custo_t1_r0 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t1_r1 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t1_r2 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t1_r3 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t2_r0 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t2_r1 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t2_r2 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t2_r3 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t4_r0 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t4_r1 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t4_r2 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n4_var12_custo_t4_r3 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_base_t1_r0 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t1_r1 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t1_r2 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t1_r3 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t1_r4 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t2_r0 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t2_r1 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t2_r2 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t2_r3 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t2_r4 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t4_r0 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t4_r1 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t4_r2 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t4_r3 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_base_t4_r4 | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| degraus_n5_var11_1_teste_t1_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t1_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t1_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t1_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t1_r4 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t2_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t2_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t2_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t2_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t2_r4 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t4_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t4_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t4_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t4_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_1_teste_t4_r4 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 1, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:797e1906a47b` |
| degraus_n5_var11_2_testes_t1_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t1_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t1_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t1_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t1_r4 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t2_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t2_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t2_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t2_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t2_r4 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t4_r0 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t4_r1 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t4_r2 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t4_r3 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var11_2_testes_t4_r4 | v2.2.1 com {'ablacoes': {'bug_duplicado_permitido': {'valor': False, 'regra': 'VAR-10'}, 'testes_por_ciclo': {'valor': 2, 'regra': 'VAR-11'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:1160a3be9da7` |
| degraus_n5_var12_custo_t1_r0 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t1_r1 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t1_r2 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t1_r3 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t1_r4 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 1}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t2_r0 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t2_r1 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t2_r2 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t2_r3 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t2_r4 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 2}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t4_r0 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t4_r1 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t4_r2 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t4_r3 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |
| degraus_n5_var12_custo_t4_r4 | v2.2.1 com {'propostas': {'custo_do_teste': {'valor': 1, 'regra': 'VAR-12'}, 'teste_pago_a_partir_do': {'valor': 2, 'regra': 'VAR-12'}}} | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'temperatura': 4}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:6424ce9f19c0` |

## Como refazer

No commit `3a2f2e0`: `cf experimento experimentos/fase4_exp7_profundidade.yaml --oficial --processos 4`. O resultado não depende do número de processos.

# Relatório do experimento `fase4_exp4b_combinacoes`

Combinações de fichas iniciais (5 e 6) e dano de incidente sem cobertura (2 e 3) na v2.2.1, com mesas de 4 e de 5 e conhecimento iniciante e experiente.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase4_exp4b_combinacoes.yaml` |
| Commit | `b263c34` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261120 |
| Partidas | 32000 |
| Falhas | 0 |
| Registros completos gravados | 32 |
| Início | 2026-11-11T13:44:24+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-06: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | (a) média da razão máximo/média de testes recebidos | 1,366 | 1,358 a 1,374 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_fichas_5_dano_2 | (b) fração dos testes contra quem tinha o menor placar | 0,418 | 0,414 a 0,423 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_fichas_5_dano_3 | (a) média da razão máximo/média de testes recebidos | 1,361 | 1,353 a 1,369 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_fichas_5_dano_3 | (b) fração dos testes contra quem tinha o menor placar | 0,403 | 0,399 a 0,408 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_fichas_6_dano_2 | (a) média da razão máximo/média de testes recebidos | 1,366 | 1,357 a 1,374 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_fichas_6_dano_2 | (b) fração dos testes contra quem tinha o menor placar | 0,418 | 0,414 a 0,423 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_fichas_6_dano_3 | (a) média da razão máximo/média de testes recebidos | 1,361 | 1,353 a 1,369 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_fichas_6_dano_3 | (b) fração dos testes contra quem tinha o menor placar | 0,403 | 0,398 a 0,407 | 0,000 a 0,433 | 2000 | passa |
| n5_iniciante_fichas_5_dano_2 | (a) média da razão máximo/média de testes recebidos | 1,404 | 1,396 a 1,413 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_fichas_5_dano_2 | (b) fração dos testes contra quem tinha o menor placar | 0,340 | 0,336 a 0,344 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_fichas_5_dano_3 | (a) média da razão máximo/média de testes recebidos | 1,410 | 1,401 a 1,418 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_fichas_5_dano_3 | (b) fração dos testes contra quem tinha o menor placar | 0,329 | 0,326 a 0,333 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_fichas_6_dano_2 | (a) média da razão máximo/média de testes recebidos | 1,404 | 1,396 a 1,412 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_fichas_6_dano_2 | (b) fração dos testes contra quem tinha o menor placar | 0,340 | 0,336 a 0,343 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_fichas_6_dano_3 | (a) média da razão máximo/média de testes recebidos | 1,410 | 1,402 a 1,417 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_fichas_6_dano_3 | (b) fração dos testes contra quem tinha o menor placar | 0,328 | 0,324 a 0,332 | 0,000 a 0,350 | 2000 | passa |
| n4_experiente_fichas_5_dano_2 | (a) média da razão máximo/média de testes recebidos | 1,368 | 1,359 a 1,376 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_fichas_5_dano_2 | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,416 a 0,425 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_fichas_5_dano_3 | (a) média da razão máximo/média de testes recebidos | 1,376 | 1,368 a 1,384 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_fichas_5_dano_3 | (b) fração dos testes contra quem tinha o menor placar | 0,418 | 0,413 a 0,423 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_fichas_6_dano_2 | (a) média da razão máximo/média de testes recebidos | 1,368 | 1,359 a 1,376 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_fichas_6_dano_2 | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,416 a 0,425 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_fichas_6_dano_3 | (a) média da razão máximo/média de testes recebidos | 1,376 | 1,368 a 1,384 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_fichas_6_dano_3 | (b) fração dos testes contra quem tinha o menor placar | 0,418 | 0,413 a 0,422 | 0,000 a 0,433 | 2000 | passa |
| n5_experiente_fichas_5_dano_2 | (a) média da razão máximo/média de testes recebidos | 1,422 | 1,413 a 1,430 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_fichas_5_dano_2 | (b) fração dos testes contra quem tinha o menor placar | 0,345 | 0,341 a 0,349 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_fichas_5_dano_3 | (a) média da razão máximo/média de testes recebidos | 1,430 | 1,421 a 1,438 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_fichas_5_dano_3 | (b) fração dos testes contra quem tinha o menor placar | 0,334 | 0,330 a 0,338 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_fichas_6_dano_2 | (a) média da razão máximo/média de testes recebidos | 1,422 | 1,413 a 1,431 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_fichas_6_dano_2 | (b) fração dos testes contra quem tinha o menor placar | 0,345 | 0,341 a 0,349 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_fichas_6_dano_3 | (a) média da razão máximo/média de testes recebidos | 1,430 | 1,421 a 1,438 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_fichas_6_dano_3 | (b) fração dos testes contra quem tinha o menor placar | 0,334 | 0,330 a 0,337 | 0,000 a 0,350 | 2000 | passa |

Nota: (b): empate no menor placar conta como teste contra o menor.

### REQ-07: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,073 | 0,063 a 0,086 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_fichas_5_dano_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,292 | 0,272 a 0,312 | 0,000 a 0,100 | 2000 | falha |
| n4_iniciante_fichas_6_dano_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,019 | 0,014 a 0,027 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_fichas_6_dano_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,150 | 0,136 a 0,167 | 0,000 a 0,100 | 2000 | falha |
| n5_iniciante_fichas_5_dano_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,068 | 0,058 a 0,080 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_5_dano_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,338 | 0,317 a 0,359 | 0,000 a 0,100 | 2000 | falha |
| n5_iniciante_fichas_6_dano_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,015 | 0,011 a 0,022 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_6_dano_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,168 | 0,152 a 0,184 | 0,000 a 0,100 | 2000 | falha |
| n4_experiente_fichas_5_dano_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,047 | 0,039 a 0,057 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_fichas_5_dano_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,197 | 0,180 a 0,214 | 0,000 a 0,100 | 2000 | falha |
| n4_experiente_fichas_6_dano_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,014 | 0,010 a 0,020 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_fichas_6_dano_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,086 | 0,074 a 0,099 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_fichas_5_dano_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,042 | 0,034 a 0,052 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_fichas_5_dano_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,239 | 0,221 a 0,259 | 0,000 a 0,100 | 2000 | falha |
| n5_experiente_fichas_6_dano_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,016 | 0,011 a 0,022 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_fichas_6_dano_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,101 | 0,088 a 0,114 | 0,000 a 0,100 | 2000 | inconclusivo |

### REQ-08: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | mediana da duração estimada (min) | 38,5 | 38,3 a 38,7 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_fichas_5_dano_3 | mediana da duração estimada (min) | 38,6 | 38,4 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_fichas_6_dano_2 | mediana da duração estimada (min) | 38,5 | 38,3 a 38,7 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_fichas_6_dano_3 | mediana da duração estimada (min) | 38,6 | 38,4 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_fichas_5_dano_2 | mediana da duração estimada (min) | 44,3 | 44,1 a 44,5 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_fichas_5_dano_3 | mediana da duração estimada (min) | 44,5 | 44,4 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_fichas_6_dano_2 | mediana da duração estimada (min) | 44,3 | 44,1 a 44,5 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_fichas_6_dano_3 | mediana da duração estimada (min) | 44,5 | 44,4 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n4_experiente_fichas_5_dano_2 | mediana da duração estimada (min) | 38,8 | 38,6 a 38,9 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_fichas_5_dano_3 | mediana da duração estimada (min) | 38,8 | 38,7 a 39,0 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_fichas_6_dano_2 | mediana da duração estimada (min) | 38,8 | 38,6 a 38,9 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_fichas_6_dano_3 | mediana da duração estimada (min) | 38,8 | 38,7 a 39,0 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_fichas_5_dano_2 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,6 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_fichas_5_dano_3 | mediana da duração estimada (min) | 44,6 | 44,4 a 44,8 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_fichas_6_dano_2 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_fichas_6_dano_3 | mediana da duração estimada (min) | 44,6 | 44,4 a 44,8 | 40,0 a 50,0 | 2000 | passa |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-09: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 32000 | inconclusivo |

Nota: o critério pede pelo menos 50000 partidas.

### REQ-10: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_fichas_5_dano_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 6,0 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_fichas_6_dano_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_fichas_6_dano_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 6,0 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_fichas_5_dano_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_fichas_5_dano_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,2 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_fichas_6_dano_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_fichas_6_dano_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,2 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_fichas_5_dano_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_fichas_5_dano_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 6,0 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_fichas_6_dano_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_fichas_6_dano_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 6,0 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_fichas_5_dano_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_fichas_5_dano_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,2 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_fichas_6_dano_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_fichas_6_dano_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,2 a 9,2 | 0,0 a 5,0 | 2000 | falha |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-11: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,564 a 0,585 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_fichas_5_dano_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,620 | 0,609 a 0,630 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_fichas_6_dano_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,562 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_fichas_6_dano_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,620 | 0,609 a 0,632 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_fichas_5_dano_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,573 | 0,562 a 0,582 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_fichas_5_dano_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,610 | 0,600 a 0,619 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_fichas_6_dano_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,573 | 0,563 a 0,582 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_fichas_6_dano_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,610 | 0,601 a 0,619 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_fichas_5_dano_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,516 | 0,504 a 0,527 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_fichas_5_dano_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,521 | 0,511 a 0,533 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_fichas_6_dano_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,516 | 0,505 a 0,527 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_fichas_6_dano_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,521 | 0,510 a 0,532 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_fichas_5_dano_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,508 | 0,498 a 0,517 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_fichas_5_dano_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,519 | 0,508 a 0,529 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_fichas_6_dano_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,508 | 0,497 a 0,518 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_fichas_6_dano_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,519 | 0,509 a 0,528 | 0,100 a 0,900 | 2000 | passa |

### REQ-12: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,083 | 0,062 a 0,106 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_fichas_5_dano_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,083 | 0,063 a 0,104 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_fichas_6_dano_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,083 | 0,060 a 0,105 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_fichas_6_dano_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,084 | 0,063 a 0,106 | -0,100 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_fichas_5_dano_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,069 | 0,050 a 0,088 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_5_dano_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,072 | 0,052 a 0,090 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_6_dano_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,069 | 0,050 a 0,088 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_6_dano_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,072 | 0,054 a 0,091 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_fichas_5_dano_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,064 | 0,045 a 0,085 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_fichas_5_dano_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,055 | 0,033 a 0,078 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_fichas_6_dano_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,064 | 0,042 a 0,086 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_fichas_6_dano_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,056 | 0,033 a 0,078 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_fichas_5_dano_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,064 | 0,046 a 0,083 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_fichas_5_dano_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,061 | 0,042 a 0,080 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_fichas_6_dano_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,064 | 0,046 a 0,081 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_fichas_6_dano_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,061 | 0,043 a 0,080 | -0,100 a 0,100 | 2000 | passa |

Nota: n4_experiente_fichas_5_dano_2: 2159 assentos começaram cobrindo, 5841 não.
Nota: n4_experiente_fichas_5_dano_3: 2159 assentos começaram cobrindo, 5841 não.
Nota: n4_experiente_fichas_6_dano_2: 2159 assentos começaram cobrindo, 5841 não.
Nota: n4_experiente_fichas_6_dano_3: 2159 assentos começaram cobrindo, 5841 não.
Nota: n4_iniciante_fichas_5_dano_2: 2159 assentos começaram cobrindo, 5841 não.
Nota: n4_iniciante_fichas_5_dano_3: 2159 assentos começaram cobrindo, 5841 não.
Nota: n4_iniciante_fichas_6_dano_2: 2159 assentos começaram cobrindo, 5841 não.
Nota: n4_iniciante_fichas_6_dano_3: 2159 assentos começaram cobrindo, 5841 não.
Nota: n5_experiente_fichas_5_dano_2: 2688 assentos começaram cobrindo, 7312 não.
Nota: n5_experiente_fichas_5_dano_3: 2688 assentos começaram cobrindo, 7312 não.
Nota: n5_experiente_fichas_6_dano_2: 2688 assentos começaram cobrindo, 7312 não.
Nota: n5_experiente_fichas_6_dano_3: 2688 assentos começaram cobrindo, 7312 não.
Nota: n5_iniciante_fichas_5_dano_2: 2688 assentos começaram cobrindo, 7312 não.
Nota: n5_iniciante_fichas_5_dano_3: 2688 assentos começaram cobrindo, 7312 não.
Nota: n5_iniciante_fichas_6_dano_2: 2688 assentos começaram cobrindo, 7312 não.
Nota: n5_iniciante_fichas_6_dano_3: 2688 assentos começaram cobrindo, 7312 não.

### REQ-13: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | dano de incidente / fichas movimentadas | 0,216 | 0,213 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_fichas_5_dano_3 | dano de incidente / fichas movimentadas | 0,264 | 0,261 a 0,267 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_fichas_6_dano_2 | dano de incidente / fichas movimentadas | 0,215 | 0,212 a 0,217 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_fichas_6_dano_3 | dano de incidente / fichas movimentadas | 0,264 | 0,261 a 0,267 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_fichas_5_dano_2 | dano de incidente / fichas movimentadas | 0,215 | 0,212 a 0,217 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_fichas_5_dano_3 | dano de incidente / fichas movimentadas | 0,263 | 0,261 a 0,266 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_fichas_6_dano_2 | dano de incidente / fichas movimentadas | 0,214 | 0,212 a 0,216 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_fichas_6_dano_3 | dano de incidente / fichas movimentadas | 0,264 | 0,261 a 0,266 | 0,200 a 0,600 | 2000 | passa |
| n4_experiente_fichas_5_dano_2 | dano de incidente / fichas movimentadas | 0,171 | 0,169 a 0,173 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_fichas_5_dano_3 | dano de incidente / fichas movimentadas | 0,216 | 0,213 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_experiente_fichas_6_dano_2 | dano de incidente / fichas movimentadas | 0,171 | 0,169 a 0,173 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_fichas_6_dano_3 | dano de incidente / fichas movimentadas | 0,216 | 0,213 a 0,219 | 0,200 a 0,600 | 2000 | passa |
| n5_experiente_fichas_5_dano_2 | dano de incidente / fichas movimentadas | 0,173 | 0,171 a 0,175 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_fichas_5_dano_3 | dano de incidente / fichas movimentadas | 0,219 | 0,217 a 0,221 | 0,200 a 0,600 | 2000 | passa |
| n5_experiente_fichas_6_dano_2 | dano de incidente / fichas movimentadas | 0,173 | 0,170 a 0,175 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_fichas_6_dano_3 | dano de incidente / fichas movimentadas | 0,219 | 0,217 a 0,222 | 0,200 a 0,600 | 2000 | passa |

Nota: o dano do Critical Failure não conta como dano de incidente.

## Taxa de vitória por bot (MET-07)

Sem veredito. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| n4_experiente_fichas_5_dano_2 | blefa_nunca_contesta_nunca | 4 | 2504 | 0,268 | 0,252 a 0,286 | 0,250 |
| n4_experiente_fichas_5_dano_2 | blefa_nunca_contesta_limiar | 4 | 4101 | 0,250 | 0,237 a 0,263 | 0,250 |
| n4_experiente_fichas_5_dano_2 | blefa_sempre_contesta_limiar | 4 | 330 | 0,220 | 0,176 a 0,267 | 0,250 |
| n4_experiente_fichas_5_dano_2 | blefa_sempre_contesta_nunca | 4 | 1065 | 0,216 | 0,191 a 0,239 | 0,250 |
| n4_experiente_fichas_5_dano_3 | blefa_nunca_contesta_nunca | 4 | 2504 | 0,261 | 0,244 a 0,280 | 0,250 |
| n4_experiente_fichas_5_dano_3 | blefa_nunca_contesta_limiar | 4 | 4101 | 0,249 | 0,236 a 0,263 | 0,250 |
| n4_experiente_fichas_5_dano_3 | blefa_sempre_contesta_limiar | 4 | 330 | 0,247 | 0,203 a 0,294 | 0,250 |
| n4_experiente_fichas_5_dano_3 | blefa_sempre_contesta_nunca | 4 | 1065 | 0,227 | 0,202 a 0,250 | 0,250 |
| n4_experiente_fichas_6_dano_2 | blefa_nunca_contesta_nunca | 4 | 2504 | 0,268 | 0,253 a 0,285 | 0,250 |
| n4_experiente_fichas_6_dano_2 | blefa_nunca_contesta_limiar | 4 | 4101 | 0,250 | 0,237 a 0,263 | 0,250 |
| n4_experiente_fichas_6_dano_2 | blefa_sempre_contesta_limiar | 4 | 330 | 0,220 | 0,176 a 0,265 | 0,250 |
| n4_experiente_fichas_6_dano_2 | blefa_sempre_contesta_nunca | 4 | 1065 | 0,216 | 0,192 a 0,242 | 0,250 |
| n4_experiente_fichas_6_dano_3 | blefa_nunca_contesta_nunca | 4 | 2504 | 0,262 | 0,245 a 0,280 | 0,250 |
| n4_experiente_fichas_6_dano_3 | blefa_nunca_contesta_limiar | 4 | 4101 | 0,249 | 0,236 a 0,263 | 0,250 |
| n4_experiente_fichas_6_dano_3 | blefa_sempre_contesta_limiar | 4 | 330 | 0,244 | 0,198 a 0,294 | 0,250 |
| n4_experiente_fichas_6_dano_3 | blefa_sempre_contesta_nunca | 4 | 1065 | 0,226 | 0,199 a 0,251 | 0,250 |
| n4_iniciante_fichas_5_dano_2 | blefa_nunca_contesta_limiar | 4 | 4101 | 0,258 | 0,244 a 0,271 | 0,250 |
| n4_iniciante_fichas_5_dano_2 | blefa_sempre_contesta_nunca | 4 | 1065 | 0,245 | 0,219 a 0,271 | 0,250 |
| n4_iniciante_fichas_5_dano_2 | blefa_nunca_contesta_nunca | 4 | 2504 | 0,243 | 0,226 a 0,259 | 0,250 |
| n4_iniciante_fichas_5_dano_2 | blefa_sempre_contesta_limiar | 4 | 330 | 0,226 | 0,180 a 0,270 | 0,250 |
| n4_iniciante_fichas_5_dano_3 | blefa_nunca_contesta_limiar | 4 | 4101 | 0,261 | 0,248 a 0,274 | 0,250 |
| n4_iniciante_fichas_5_dano_3 | blefa_sempre_contesta_limiar | 4 | 330 | 0,248 | 0,202 a 0,295 | 0,250 |
| n4_iniciante_fichas_5_dano_3 | blefa_nunca_contesta_nunca | 4 | 2504 | 0,239 | 0,222 a 0,254 | 0,250 |
| n4_iniciante_fichas_5_dano_3 | blefa_sempre_contesta_nunca | 4 | 1065 | 0,236 | 0,211 a 0,262 | 0,250 |
| n4_iniciante_fichas_6_dano_2 | blefa_nunca_contesta_limiar | 4 | 4101 | 0,258 | 0,245 a 0,271 | 0,250 |
| n4_iniciante_fichas_6_dano_2 | blefa_sempre_contesta_nunca | 4 | 1065 | 0,244 | 0,219 a 0,269 | 0,250 |
| n4_iniciante_fichas_6_dano_2 | blefa_nunca_contesta_nunca | 4 | 2504 | 0,243 | 0,225 a 0,260 | 0,250 |
| n4_iniciante_fichas_6_dano_2 | blefa_sempre_contesta_limiar | 4 | 330 | 0,229 | 0,186 a 0,274 | 0,250 |
| n4_iniciante_fichas_6_dano_3 | blefa_nunca_contesta_limiar | 4 | 4101 | 0,260 | 0,246 a 0,274 | 0,250 |
| n4_iniciante_fichas_6_dano_3 | blefa_sempre_contesta_limiar | 4 | 330 | 0,245 | 0,203 a 0,292 | 0,250 |
| n4_iniciante_fichas_6_dano_3 | blefa_nunca_contesta_nunca | 4 | 2504 | 0,239 | 0,222 a 0,255 | 0,250 |
| n4_iniciante_fichas_6_dano_3 | blefa_sempre_contesta_nunca | 4 | 1065 | 0,238 | 0,213 a 0,265 | 0,250 |
| n5_experiente_fichas_5_dano_2 | blefa_nunca_contesta_nunca | 5 | 3033 | 0,215 | 0,201 a 0,228 | 0,200 |
| n5_experiente_fichas_5_dano_2 | blefa_nunca_contesta_limiar | 5 | 5504 | 0,203 | 0,193 a 0,213 | 0,200 |
| n5_experiente_fichas_5_dano_2 | blefa_sempre_contesta_nunca | 5 | 1309 | 0,165 | 0,146 a 0,185 | 0,200 |
| n5_experiente_fichas_5_dano_2 | blefa_sempre_contesta_limiar | 5 | 154 | 0,104 | 0,058 a 0,149 | 0,200 |
| n5_experiente_fichas_5_dano_3 | blefa_nunca_contesta_nunca | 5 | 3033 | 0,218 | 0,203 a 0,232 | 0,200 |
| n5_experiente_fichas_5_dano_3 | blefa_nunca_contesta_limiar | 5 | 5504 | 0,197 | 0,187 a 0,207 | 0,200 |
| n5_experiente_fichas_5_dano_3 | blefa_sempre_contesta_nunca | 5 | 1309 | 0,177 | 0,155 a 0,197 | 0,200 |
| n5_experiente_fichas_5_dano_3 | blefa_sempre_contesta_limiar | 5 | 154 | 0,143 | 0,091 a 0,198 | 0,200 |
| n5_experiente_fichas_6_dano_2 | blefa_nunca_contesta_nunca | 5 | 3033 | 0,215 | 0,200 a 0,227 | 0,200 |
| n5_experiente_fichas_6_dano_2 | blefa_nunca_contesta_limiar | 5 | 5504 | 0,203 | 0,193 a 0,213 | 0,200 |
| n5_experiente_fichas_6_dano_2 | blefa_sempre_contesta_nunca | 5 | 1309 | 0,165 | 0,145 a 0,184 | 0,200 |
| n5_experiente_fichas_6_dano_2 | blefa_sempre_contesta_limiar | 5 | 154 | 0,104 | 0,065 a 0,156 | 0,200 |
| n5_experiente_fichas_6_dano_3 | blefa_nunca_contesta_nunca | 5 | 3033 | 0,218 | 0,203 a 0,233 | 0,200 |
| n5_experiente_fichas_6_dano_3 | blefa_nunca_contesta_limiar | 5 | 5504 | 0,197 | 0,186 a 0,207 | 0,200 |
| n5_experiente_fichas_6_dano_3 | blefa_sempre_contesta_nunca | 5 | 1309 | 0,177 | 0,156 a 0,197 | 0,200 |
| n5_experiente_fichas_6_dano_3 | blefa_sempre_contesta_limiar | 5 | 154 | 0,143 | 0,091 a 0,198 | 0,200 |
| n5_iniciante_fichas_5_dano_2 | blefa_nunca_contesta_limiar | 5 | 5504 | 0,206 | 0,197 a 0,217 | 0,200 |
| n5_iniciante_fichas_5_dano_2 | blefa_nunca_contesta_nunca | 5 | 3033 | 0,200 | 0,186 a 0,214 | 0,200 |
| n5_iniciante_fichas_5_dano_2 | blefa_sempre_contesta_nunca | 5 | 1309 | 0,177 | 0,155 a 0,198 | 0,200 |
| n5_iniciante_fichas_5_dano_2 | blefa_sempre_contesta_limiar | 5 | 154 | 0,172 | 0,114 a 0,237 | 0,200 |
| n5_iniciante_fichas_5_dano_3 | blefa_nunca_contesta_limiar | 5 | 5504 | 0,207 | 0,196 a 0,217 | 0,200 |
| n5_iniciante_fichas_5_dano_3 | blefa_nunca_contesta_nunca | 5 | 3033 | 0,201 | 0,187 a 0,216 | 0,200 |
| n5_iniciante_fichas_5_dano_3 | blefa_sempre_contesta_limiar | 5 | 154 | 0,182 | 0,130 a 0,240 | 0,200 |
| n5_iniciante_fichas_5_dano_3 | blefa_sempre_contesta_nunca | 5 | 1309 | 0,172 | 0,153 a 0,191 | 0,200 |
| n5_iniciante_fichas_6_dano_2 | blefa_nunca_contesta_limiar | 5 | 5504 | 0,206 | 0,196 a 0,217 | 0,200 |
| n5_iniciante_fichas_6_dano_2 | blefa_nunca_contesta_nunca | 5 | 3033 | 0,200 | 0,186 a 0,214 | 0,200 |
| n5_iniciante_fichas_6_dano_2 | blefa_sempre_contesta_nunca | 5 | 1309 | 0,177 | 0,157 a 0,197 | 0,200 |
| n5_iniciante_fichas_6_dano_2 | blefa_sempre_contesta_limiar | 5 | 154 | 0,172 | 0,114 a 0,237 | 0,200 |
| n5_iniciante_fichas_6_dano_3 | blefa_nunca_contesta_limiar | 5 | 5504 | 0,207 | 0,197 a 0,217 | 0,200 |
| n5_iniciante_fichas_6_dano_3 | blefa_nunca_contesta_nunca | 5 | 3033 | 0,201 | 0,187 a 0,215 | 0,200 |
| n5_iniciante_fichas_6_dano_3 | blefa_sempre_contesta_limiar | 5 | 154 | 0,182 | 0,123 a 0,240 | 0,200 |
| n5_iniciante_fichas_6_dano_3 | blefa_sempre_contesta_nunca | 5 | 1309 | 0,172 | 0,152 a 0,194 | 0,200 |

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903). Na v2 é só descrição: o placar em fichas não está na mesma escala dos pontos da v1, e a comparação entre as versões é feita pelo REQ-02 (autor, 2026-11-10).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | v2 | 4 | 2000 | **1,50** | 0,760 | 0,741 a 0,778 |
| n4_iniciante_fichas_5_dano_2 | v2 | 4 | 2000 | 1,25 | 0,947 | 0,936 a 0,956 |
| n4_iniciante_fichas_5_dano_2 | v2 | 4 | 2000 | 2,00 | 0,303 | 0,283 a 0,324 |
| n4_iniciante_fichas_5_dano_3 | v2 | 4 | 2000 | **1,50** | 0,821 | 0,803 a 0,837 |
| n4_iniciante_fichas_5_dano_3 | v2 | 4 | 2000 | 1,25 | 0,955 | 0,945 a 0,963 |
| n4_iniciante_fichas_5_dano_3 | v2 | 4 | 2000 | 2,00 | 0,415 | 0,394 a 0,437 |
| n4_iniciante_fichas_6_dano_2 | v2 | 4 | 2000 | **1,50** | 0,707 | 0,687 a 0,727 |
| n4_iniciante_fichas_6_dano_2 | v2 | 4 | 2000 | 1,25 | 0,930 | 0,919 a 0,941 |
| n4_iniciante_fichas_6_dano_2 | v2 | 4 | 2000 | 2,00 | 0,236 | 0,218 a 0,255 |
| n4_iniciante_fichas_6_dano_3 | v2 | 4 | 2000 | **1,50** | 0,794 | 0,776 a 0,811 |
| n4_iniciante_fichas_6_dano_3 | v2 | 4 | 2000 | 1,25 | 0,945 | 0,934 a 0,954 |
| n4_iniciante_fichas_6_dano_3 | v2 | 4 | 2000 | 2,00 | 0,352 | 0,332 a 0,374 |
| n5_iniciante_fichas_5_dano_2 | v2 | 5 | 2000 | **1,50** | 0,751 | 0,732 a 0,770 |
| n5_iniciante_fichas_5_dano_2 | v2 | 5 | 2000 | 1,25 | 0,968 | 0,959 a 0,975 |
| n5_iniciante_fichas_5_dano_2 | v2 | 5 | 2000 | 2,00 | 0,281 | 0,262 a 0,301 |
| n5_iniciante_fichas_5_dano_3 | v2 | 5 | 2000 | **1,50** | 0,870 | 0,855 a 0,884 |
| n5_iniciante_fichas_5_dano_3 | v2 | 5 | 2000 | 1,25 | 0,980 | 0,973 a 0,985 |
| n5_iniciante_fichas_5_dano_3 | v2 | 5 | 2000 | 2,00 | 0,460 | 0,438 a 0,482 |
| n5_iniciante_fichas_6_dano_2 | v2 | 5 | 2000 | **1,50** | 0,689 | 0,668 a 0,709 |
| n5_iniciante_fichas_6_dano_2 | v2 | 5 | 2000 | 1,25 | 0,955 | 0,945 a 0,963 |
| n5_iniciante_fichas_6_dano_2 | v2 | 5 | 2000 | 2,00 | 0,203 | 0,185 a 0,221 |
| n5_iniciante_fichas_6_dano_3 | v2 | 5 | 2000 | **1,50** | 0,835 | 0,818 a 0,851 |
| n5_iniciante_fichas_6_dano_3 | v2 | 5 | 2000 | 1,25 | 0,974 | 0,966 a 0,980 |
| n5_iniciante_fichas_6_dano_3 | v2 | 5 | 2000 | 2,00 | 0,381 | 0,360 a 0,402 |
| n4_experiente_fichas_5_dano_2 | v2 | 4 | 2000 | **1,50** | 0,678 | 0,658 a 0,699 |
| n4_experiente_fichas_5_dano_2 | v2 | 4 | 2000 | 1,25 | 0,920 | 0,907 a 0,931 |
| n4_experiente_fichas_5_dano_2 | v2 | 4 | 2000 | 2,00 | 0,214 | 0,197 a 0,233 |
| n4_experiente_fichas_5_dano_3 | v2 | 4 | 2000 | **1,50** | 0,774 | 0,755 a 0,792 |
| n4_experiente_fichas_5_dano_3 | v2 | 4 | 2000 | 1,25 | 0,953 | 0,942 a 0,961 |
| n4_experiente_fichas_5_dano_3 | v2 | 4 | 2000 | 2,00 | 0,306 | 0,287 a 0,327 |
| n4_experiente_fichas_6_dano_2 | v2 | 4 | 2000 | **1,50** | 0,614 | 0,592 a 0,635 |
| n4_experiente_fichas_6_dano_2 | v2 | 4 | 2000 | 1,25 | 0,892 | 0,878 a 0,905 |
| n4_experiente_fichas_6_dano_2 | v2 | 4 | 2000 | 2,00 | 0,162 | 0,147 a 0,179 |
| n4_experiente_fichas_6_dano_3 | v2 | 4 | 2000 | **1,50** | 0,717 | 0,696 a 0,736 |
| n4_experiente_fichas_6_dano_3 | v2 | 4 | 2000 | 1,25 | 0,941 | 0,930 a 0,951 |
| n4_experiente_fichas_6_dano_3 | v2 | 4 | 2000 | 2,00 | 0,251 | 0,232 a 0,270 |
| n5_experiente_fichas_5_dano_2 | v2 | 5 | 2000 | **1,50** | 0,686 | 0,666 a 0,706 |
| n5_experiente_fichas_5_dano_2 | v2 | 5 | 2000 | 1,25 | 0,953 | 0,942 a 0,961 |
| n5_experiente_fichas_5_dano_2 | v2 | 5 | 2000 | 2,00 | 0,199 | 0,182 a 0,217 |
| n5_experiente_fichas_5_dano_3 | v2 | 5 | 2000 | **1,50** | 0,804 | 0,787 a 0,821 |
| n5_experiente_fichas_5_dano_3 | v2 | 5 | 2000 | 1,25 | 0,980 | 0,972 a 0,985 |
| n5_experiente_fichas_5_dano_3 | v2 | 5 | 2000 | 2,00 | 0,336 | 0,316 a 0,357 |
| n5_experiente_fichas_6_dano_2 | v2 | 5 | 2000 | **1,50** | 0,619 | 0,597 a 0,640 |
| n5_experiente_fichas_6_dano_2 | v2 | 5 | 2000 | 1,25 | 0,930 | 0,918 a 0,940 |
| n5_experiente_fichas_6_dano_2 | v2 | 5 | 2000 | 2,00 | 0,142 | 0,127 a 0,158 |
| n5_experiente_fichas_6_dano_3 | v2 | 5 | 2000 | **1,50** | 0,758 | 0,739 a 0,776 |
| n5_experiente_fichas_6_dano_3 | v2 | 5 | 2000 | 1,25 | 0,971 | 0,963 a 0,977 |
| n5_experiente_fichas_6_dano_3 | v2 | 5 | 2000 | 2,00 | 0,279 | 0,259 a 0,299 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Sistema cheio no 1º Planejamento | Blefes por partida (bem-sucedidos) | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | 2000 | 0 | 21,8 | 2,0 | 1,1% | 0,0% | 0,0% | 0,176 | 10,8 | 7,3 | 57,4% | 1,97 (22,9%) | 35,0 / 38,5 / 41,9 |
| n4_iniciante_fichas_5_dano_3 | 2000 | 0 | 21,7 | 2,1 | 1,1% | 0,0% | 0,0% | 0,196 | 10,2 | 6,6 | 62,0% | 1,89 (20,8%) | 35,0 / 38,6 / 42,1 |
| n4_iniciante_fichas_6_dano_2 | 2000 | 0 | 21,8 | 2,0 | 1,1% | 0,0% | 0,0% | 0,176 | 11,8 | 8,2 | 57,4% | 1,97 (22,9%) | 35,0 / 38,5 / 41,9 |
| n4_iniciante_fichas_6_dano_3 | 2000 | 0 | 21,7 | 2,1 | 1,1% | 0,0% | 0,0% | 0,197 | 11,2 | 7,4 | 62,0% | 1,89 (20,8%) | 35,0 / 38,6 / 42,1 |
| n5_iniciante_fichas_5_dano_2 | 2000 | 0 | 28,1 | 2,4 | 2,1% | 5,0% | 0,0% | 0,147 | 11,2 | 7,4 | 57,3% | 2,17 (22,4%) | 40,7 / 44,3 / 48,2 |
| n5_iniciante_fichas_5_dano_3 | 2000 | 0 | 28,1 | 2,5 | 1,7% | 4,3% | 0,0% | 0,190 | 10,8 | 6,6 | 61,0% | 2,17 (21,7%) | 40,9 / 44,5 / 48,3 |
| n5_iniciante_fichas_6_dano_2 | 2000 | 0 | 28,1 | 2,4 | 2,1% | 5,0% | 0,0% | 0,147 | 12,2 | 8,3 | 57,3% | 2,17 (22,4%) | 40,7 / 44,3 / 48,2 |
| n5_iniciante_fichas_6_dano_3 | 2000 | 0 | 28,1 | 2,5 | 1,8% | 4,3% | 0,0% | 0,190 | 11,8 | 7,4 | 61,0% | 2,17 (21,7%) | 40,9 / 44,5 / 48,3 |
| n4_experiente_fichas_5_dano_2 | 2000 | 0 | 22,0 | 3,4 | 2,4% | 0,0% | 0,0% | 0,167 | 12,1 | 8,5 | 51,6% | 2,13 (36,9%) | 34,9 / 38,8 / 42,6 |
| n4_experiente_fichas_5_dano_3 | 2000 | 0 | 21,9 | 3,4 | 1,8% | 0,0% | 0,0% | 0,209 | 11,6 | 7,8 | 52,1% | 2,08 (37,8%) | 35,1 / 38,8 / 42,8 |
| n4_experiente_fichas_6_dano_2 | 2000 | 0 | 22,0 | 3,4 | 2,4% | 0,0% | 0,0% | 0,167 | 13,1 | 9,5 | 51,6% | 2,13 (36,9%) | 34,9 / 38,8 / 42,6 |
| n4_experiente_fichas_6_dano_3 | 2000 | 0 | 21,9 | 3,4 | 1,9% | 0,0% | 0,0% | 0,210 | 12,6 | 8,7 | 52,1% | 2,08 (37,8%) | 35,1 / 38,8 / 42,8 |
| n5_experiente_fichas_5_dano_2 | 2000 | 0 | 28,1 | 4,0 | 2,3% | 8,2% | 0,0% | 0,188 | 12,6 | 8,6 | 50,8% | 2,37 (37,0%) | 40,5 / 44,5 / 48,7 |
| n5_experiente_fichas_5_dano_3 | 2000 | 0 | 28,2 | 4,1 | 2,3% | 7,4% | 0,0% | 0,215 | 12,1 | 7,8 | 51,9% | 2,36 (37,6%) | 40,8 / 44,6 / 48,8 |
| n5_experiente_fichas_6_dano_2 | 2000 | 0 | 28,1 | 4,0 | 2,3% | 8,2% | 0,0% | 0,188 | 13,6 | 9,5 | 50,8% | 2,37 (37,0%) | 40,5 / 44,5 / 48,7 |
| n5_experiente_fichas_6_dano_3 | 2000 | 0 | 28,2 | 4,1 | 2,3% | 7,4% | 0,0% | 0,215 | 13,1 | 8,6 | 51,9% | 2,36 (37,6%) | 40,8 / 44,6 / 48,8 |

## Equilíbrio dentro da partida (descrição)

Números sem critério de aceite; os vereditos, quando pedidos, estão na seção de requisitos. Razão de testes: máximo sobre a média de testes recebidos na partida (REQ-06a). Contra o menor: fração dos testes contra quem tinha o menor placar (REQ-06b). Zeradas: partidas com alguém em 0 ficha antes do último ciclo (REQ-07). Parado: percentil 90 do tempo parado por jogador e ciclo, pelos tempos provisórios do MOD-05 (REQ-10). Peso do dano: dano de incidente sobre as fichas movimentadas (REQ-13). Dispersão: placar do primeiro menos o do último no fim (REQ-14).

| Cenário | Razão de testes | Contra o menor | Zeradas | Parado p90 (min) | Peso do dano | Dispersão |
|---|---|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | 1,37 | 0,418 | 7,3% | 5,8 | 0,216 | 6,8 |
| n4_iniciante_fichas_5_dano_3 | 1,36 | 0,403 | 29,2% | 5,8 | 0,264 | 6,8 |
| n4_iniciante_fichas_6_dano_2 | 1,37 | 0,418 | 1,9% | 5,8 | 0,215 | 7,1 |
| n4_iniciante_fichas_6_dano_3 | 1,36 | 0,403 | 15,0% | 5,8 | 0,264 | 7,3 |
| n5_iniciante_fichas_5_dano_2 | 1,40 | 0,340 | 6,8% | 9,2 | 0,215 | 7,6 |
| n5_iniciante_fichas_5_dano_3 | 1,41 | 0,329 | 33,8% | 9,2 | 0,263 | 7,8 |
| n5_iniciante_fichas_6_dano_2 | 1,40 | 0,340 | 1,6% | 9,2 | 0,214 | 7,9 |
| n5_iniciante_fichas_6_dano_3 | 1,41 | 0,328 | 16,8% | 9,2 | 0,264 | 8,3 |
| n4_experiente_fichas_5_dano_2 | 1,37 | 0,420 | 4,7% | 5,8 | 0,171 | 7,1 |
| n4_experiente_fichas_5_dano_3 | 1,38 | 0,418 | 19,7% | 5,8 | 0,216 | 7,4 |
| n4_experiente_fichas_6_dano_2 | 1,37 | 0,420 | 1,4% | 5,8 | 0,171 | 7,3 |
| n4_experiente_fichas_6_dano_3 | 1,38 | 0,418 | 8,6% | 5,8 | 0,216 | 7,8 |
| n5_experiente_fichas_5_dano_2 | 1,42 | 0,345 | 4,2% | 9,2 | 0,173 | 8,0 |
| n5_experiente_fichas_5_dano_3 | 1,43 | 0,334 | 23,9% | 9,2 | 0,219 | 8,3 |
| n5_experiente_fichas_6_dano_2 | 1,42 | 0,345 | 1,6% | 9,2 | 0,173 | 8,3 |
| n5_experiente_fichas_6_dano_3 | 1,43 | 0,334 | 10,1% | 9,2 | 0,219 | 8,8 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| n4_iniciante_fichas_5_dano_2 | v2.2.1 com {'fichas.iniciais': 5, 'dano.incidente.sem_cobertura': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_iniciante_fichas_5_dano_3 | v2.2.1 com {'fichas.iniciais': 5, 'dano.incidente.sem_cobertura': 3} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:61b09722477f` |
| n4_iniciante_fichas_6_dano_2 | v2.2.1 com {'fichas.iniciais': 6, 'dano.incidente.sem_cobertura': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:30ca332f7f8c` |
| n4_iniciante_fichas_6_dano_3 | v2.2.1 com {'fichas.iniciais': 6, 'dano.incidente.sem_cobertura': 3} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:97ff489d1678` |
| n5_iniciante_fichas_5_dano_2 | v2.2.1 com {'fichas.iniciais': 5, 'dano.incidente.sem_cobertura': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_iniciante_fichas_5_dano_3 | v2.2.1 com {'fichas.iniciais': 5, 'dano.incidente.sem_cobertura': 3} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:61b09722477f` |
| n5_iniciante_fichas_6_dano_2 | v2.2.1 com {'fichas.iniciais': 6, 'dano.incidente.sem_cobertura': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:30ca332f7f8c` |
| n5_iniciante_fichas_6_dano_3 | v2.2.1 com {'fichas.iniciais': 6, 'dano.incidente.sem_cobertura': 3} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:97ff489d1678` |
| n4_experiente_fichas_5_dano_2 | v2.2.1 com {'fichas.iniciais': 5, 'dano.incidente.sem_cobertura': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_experiente_fichas_5_dano_3 | v2.2.1 com {'fichas.iniciais': 5, 'dano.incidente.sem_cobertura': 3} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:61b09722477f` |
| n4_experiente_fichas_6_dano_2 | v2.2.1 com {'fichas.iniciais': 6, 'dano.incidente.sem_cobertura': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:30ca332f7f8c` |
| n4_experiente_fichas_6_dano_3 | v2.2.1 com {'fichas.iniciais': 6, 'dano.incidente.sem_cobertura': 3} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:97ff489d1678` |
| n5_experiente_fichas_5_dano_2 | v2.2.1 com {'fichas.iniciais': 5, 'dano.incidente.sem_cobertura': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_experiente_fichas_5_dano_3 | v2.2.1 com {'fichas.iniciais': 5, 'dano.incidente.sem_cobertura': 3} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:61b09722477f` |
| n5_experiente_fichas_6_dano_2 | v2.2.1 com {'fichas.iniciais': 6, 'dano.incidente.sem_cobertura': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:30ca332f7f8c` |
| n5_experiente_fichas_6_dano_3 | v2.2.1 com {'fichas.iniciais': 6, 'dano.incidente.sem_cobertura': 3} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:97ff489d1678` |

## Como refazer

No commit `b263c34`: `cf experimento experimentos/fase4_exp4b_combinacoes.yaml --oficial --processos 4`. O resultado não depende do número de processos.

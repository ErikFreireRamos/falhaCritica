# Relatório do experimento `fase4_exp4_sensibilidade`

Sensibilidade na v2.2.1: fichas iniciais, dano de incidente e tempos do modelo de duração, um de cada vez, com mesas de 4 e de 5 e conhecimento iniciante e experiente.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase4_exp4_sensibilidade.yaml` |
| Commit | `73762b5` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261119 |
| Partidas | 88000 |
| Falhas | 0 |
| Registros completos gravados | 88 |
| Início | 2026-11-11T08:20:54+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-06: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | (a) média da razão máximo/média de testes recebidos | 1,355 | 1,347 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_base | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,415 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_fichas_3 | (a) média da razão máximo/média de testes recebidos | 1,355 | 1,347 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_fichas_3 | (b) fração dos testes contra quem tinha o menor placar | 0,421 | 0,417 a 0,426 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_fichas_4 | (a) média da razão máximo/média de testes recebidos | 1,355 | 1,347 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_fichas_4 | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,416 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_fichas_6 | (a) média da razão máximo/média de testes recebidos | 1,355 | 1,347 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_fichas_6 | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,415 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_fichas_7 | (a) média da razão máximo/média de testes recebidos | 1,355 | 1,347 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_fichas_7 | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,415 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_1 | (a) média da razão máximo/média de testes recebidos | 1,370 | 1,362 a 1,379 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_1 | (b) fração dos testes contra quem tinha o menor placar | 0,438 | 0,434 a 0,443 | 0,000 a 0,433 | 2000 | falha |
| n4_iniciante_dano_sem_cobertura_3 | (a) média da razão máximo/média de testes recebidos | 1,358 | 1,349 a 1,366 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_3 | (b) fração dos testes contra quem tinha o menor placar | 0,409 | 0,404 a 0,413 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_dano_alerta_0 | (a) média da razão máximo/média de testes recebidos | 1,353 | 1,345 a 1,361 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_dano_alerta_0 | (b) fração dos testes contra quem tinha o menor placar | 0,422 | 0,417 a 0,427 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_dano_alerta_2 | (a) média da razão máximo/média de testes recebidos | 1,364 | 1,356 a 1,372 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_dano_alerta_2 | (b) fração dos testes contra quem tinha o menor placar | 0,419 | 0,415 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_tempos_menos_25 | (a) média da razão máximo/média de testes recebidos | 1,355 | 1,346 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_tempos_menos_25 | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,415 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_tempos_mais_25 | (a) média da razão máximo/média de testes recebidos | 1,355 | 1,347 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_tempos_mais_25 | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,415 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n5_iniciante_base | (a) média da razão máximo/média de testes recebidos | 1,407 | 1,399 a 1,415 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_base | (b) fração dos testes contra quem tinha o menor placar | 0,337 | 0,333 a 0,340 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_fichas_3 | (a) média da razão máximo/média de testes recebidos | 1,407 | 1,399 a 1,415 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_fichas_3 | (b) fração dos testes contra quem tinha o menor placar | 0,339 | 0,336 a 0,343 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_fichas_4 | (a) média da razão máximo/média de testes recebidos | 1,407 | 1,399 a 1,414 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_fichas_4 | (b) fração dos testes contra quem tinha o menor placar | 0,337 | 0,333 a 0,340 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_fichas_6 | (a) média da razão máximo/média de testes recebidos | 1,407 | 1,399 a 1,415 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_fichas_6 | (b) fração dos testes contra quem tinha o menor placar | 0,337 | 0,333 a 0,340 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_fichas_7 | (a) média da razão máximo/média de testes recebidos | 1,407 | 1,398 a 1,414 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_fichas_7 | (b) fração dos testes contra quem tinha o menor placar | 0,337 | 0,333 a 0,340 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_1 | (a) média da razão máximo/média de testes recebidos | 1,403 | 1,396 a 1,412 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_1 | (b) fração dos testes contra quem tinha o menor placar | 0,362 | 0,358 a 0,366 | 0,000 a 0,350 | 2000 | falha |
| n5_iniciante_dano_sem_cobertura_3 | (a) média da razão máximo/média de testes recebidos | 1,414 | 1,406 a 1,422 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_3 | (b) fração dos testes contra quem tinha o menor placar | 0,331 | 0,328 a 0,335 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_dano_alerta_0 | (a) média da razão máximo/média de testes recebidos | 1,405 | 1,397 a 1,413 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_dano_alerta_0 | (b) fração dos testes contra quem tinha o menor placar | 0,342 | 0,338 a 0,345 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_dano_alerta_2 | (a) média da razão máximo/média de testes recebidos | 1,404 | 1,396 a 1,412 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_dano_alerta_2 | (b) fração dos testes contra quem tinha o menor placar | 0,334 | 0,330 a 0,338 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_tempos_menos_25 | (a) média da razão máximo/média de testes recebidos | 1,407 | 1,399 a 1,415 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_tempos_menos_25 | (b) fração dos testes contra quem tinha o menor placar | 0,337 | 0,333 a 0,340 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_tempos_mais_25 | (a) média da razão máximo/média de testes recebidos | 1,407 | 1,398 a 1,415 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_tempos_mais_25 | (b) fração dos testes contra quem tinha o menor placar | 0,337 | 0,333 a 0,340 | 0,000 a 0,350 | 2000 | passa |
| n4_experiente_base | (a) média da razão máximo/média de testes recebidos | 1,383 | 1,374 a 1,392 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_base | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,419 a 0,428 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_fichas_3 | (a) média da razão máximo/média de testes recebidos | 1,383 | 1,375 a 1,392 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_fichas_3 | (b) fração dos testes contra quem tinha o menor placar | 0,425 | 0,420 a 0,429 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_fichas_4 | (a) média da razão máximo/média de testes recebidos | 1,383 | 1,375 a 1,392 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_fichas_4 | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,419 a 0,428 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_fichas_6 | (a) média da razão máximo/média de testes recebidos | 1,383 | 1,375 a 1,392 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_fichas_6 | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,419 a 0,428 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_fichas_7 | (a) média da razão máximo/média de testes recebidos | 1,383 | 1,375 a 1,392 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_fichas_7 | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,419 a 0,428 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_1 | (a) média da razão máximo/média de testes recebidos | 1,361 | 1,352 a 1,370 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_1 | (b) fração dos testes contra quem tinha o menor placar | 0,438 | 0,433 a 0,442 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_experiente_dano_sem_cobertura_3 | (a) média da razão máximo/média de testes recebidos | 1,373 | 1,365 a 1,381 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_3 | (b) fração dos testes contra quem tinha o menor placar | 0,415 | 0,411 a 0,420 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_dano_alerta_0 | (a) média da razão máximo/média de testes recebidos | 1,379 | 1,370 a 1,387 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_dano_alerta_0 | (b) fração dos testes contra quem tinha o menor placar | 0,422 | 0,417 a 0,426 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_dano_alerta_2 | (a) média da razão máximo/média de testes recebidos | 1,376 | 1,368 a 1,384 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_dano_alerta_2 | (b) fração dos testes contra quem tinha o menor placar | 0,422 | 0,417 a 0,427 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_tempos_menos_25 | (a) média da razão máximo/média de testes recebidos | 1,383 | 1,375 a 1,392 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_tempos_menos_25 | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,419 a 0,429 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_tempos_mais_25 | (a) média da razão máximo/média de testes recebidos | 1,383 | 1,375 a 1,392 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_tempos_mais_25 | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,419 a 0,428 | 0,000 a 0,433 | 2000 | passa |
| n5_experiente_base | (a) média da razão máximo/média de testes recebidos | 1,429 | 1,420 a 1,437 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_base | (b) fração dos testes contra quem tinha o menor placar | 0,346 | 0,342 a 0,350 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_fichas_3 | (a) média da razão máximo/média de testes recebidos | 1,429 | 1,420 a 1,437 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_fichas_3 | (b) fração dos testes contra quem tinha o menor placar | 0,348 | 0,344 a 0,351 | 0,000 a 0,350 | 2000 | inconclusivo |
| n5_experiente_fichas_4 | (a) média da razão máximo/média de testes recebidos | 1,429 | 1,420 a 1,437 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_fichas_4 | (b) fração dos testes contra quem tinha o menor placar | 0,346 | 0,342 a 0,350 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_fichas_6 | (a) média da razão máximo/média de testes recebidos | 1,429 | 1,420 a 1,437 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_fichas_6 | (b) fração dos testes contra quem tinha o menor placar | 0,346 | 0,342 a 0,350 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_fichas_7 | (a) média da razão máximo/média de testes recebidos | 1,429 | 1,420 a 1,437 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_fichas_7 | (b) fração dos testes contra quem tinha o menor placar | 0,346 | 0,342 a 0,350 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_1 | (a) média da razão máximo/média de testes recebidos | 1,426 | 1,418 a 1,435 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_1 | (b) fração dos testes contra quem tinha o menor placar | 0,357 | 0,353 a 0,361 | 0,000 a 0,350 | 2000 | falha |
| n5_experiente_dano_sem_cobertura_3 | (a) média da razão máximo/média de testes recebidos | 1,423 | 1,415 a 1,432 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_3 | (b) fração dos testes contra quem tinha o menor placar | 0,332 | 0,329 a 0,336 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_dano_alerta_0 | (a) média da razão máximo/média de testes recebidos | 1,427 | 1,417 a 1,436 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_dano_alerta_0 | (b) fração dos testes contra quem tinha o menor placar | 0,343 | 0,339 a 0,347 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_dano_alerta_2 | (a) média da razão máximo/média de testes recebidos | 1,431 | 1,422 a 1,440 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_dano_alerta_2 | (b) fração dos testes contra quem tinha o menor placar | 0,341 | 0,337 a 0,344 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_tempos_menos_25 | (a) média da razão máximo/média de testes recebidos | 1,429 | 1,421 a 1,437 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_tempos_menos_25 | (b) fração dos testes contra quem tinha o menor placar | 0,346 | 0,342 a 0,350 | 0,000 a 0,350 | 2000 | inconclusivo |
| n5_experiente_tempos_mais_25 | (a) média da razão máximo/média de testes recebidos | 1,429 | 1,420 a 1,438 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_tempos_mais_25 | (b) fração dos testes contra quem tinha o menor placar | 0,346 | 0,342 a 0,350 | 0,000 a 0,350 | 2000 | passa |

Nota: (b): empate no menor placar conta como teste contra o menor.

### REQ-07: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | partidas com alguém em 0 ficha antes do último ciclo | 0,060 | 0,051 a 0,072 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_fichas_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,459 | 0,437 a 0,480 | 0,000 a 0,100 | 2000 | falha |
| n4_iniciante_fichas_4 | partidas com alguém em 0 ficha antes do último ciclo | 0,174 | 0,158 a 0,192 | 0,000 a 0,100 | 2000 | falha |
| n4_iniciante_fichas_6 | partidas com alguém em 0 ficha antes do último ciclo | 0,018 | 0,013 a 0,024 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_fichas_7 | partidas com alguém em 0 ficha antes do último ciclo | 0,004 | 0,002 a 0,008 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_1 | partidas com alguém em 0 ficha antes do último ciclo | 0,005 | 0,003 a 0,010 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,268 | 0,249 a 0,287 | 0,000 a 0,100 | 2000 | falha |
| n4_iniciante_dano_alerta_0 | partidas com alguém em 0 ficha antes do último ciclo | 0,032 | 0,025 a 0,041 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_dano_alerta_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,127 | 0,113 a 0,142 | 0,000 a 0,100 | 2000 | falha |
| n4_iniciante_tempos_menos_25 | partidas com alguém em 0 ficha antes do último ciclo | 0,060 | 0,051 a 0,072 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_tempos_mais_25 | partidas com alguém em 0 ficha antes do último ciclo | 0,060 | 0,051 a 0,072 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_base | partidas com alguém em 0 ficha antes do último ciclo | 0,082 | 0,071 a 0,095 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,521 | 0,500 a 0,543 | 0,000 a 0,100 | 2000 | falha |
| n5_iniciante_fichas_4 | partidas com alguém em 0 ficha antes do último ciclo | 0,227 | 0,209 a 0,245 | 0,000 a 0,100 | 2000 | falha |
| n5_iniciante_fichas_6 | partidas com alguém em 0 ficha antes do último ciclo | 0,022 | 0,016 a 0,029 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_7 | partidas com alguém em 0 ficha antes do último ciclo | 0,005 | 0,003 a 0,010 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_1 | partidas com alguém em 0 ficha antes do último ciclo | 0,006 | 0,003 a 0,010 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,318 | 0,297 a 0,338 | 0,000 a 0,100 | 2000 | falha |
| n5_iniciante_dano_alerta_0 | partidas com alguém em 0 ficha antes do último ciclo | 0,042 | 0,034 a 0,052 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_dano_alerta_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,168 | 0,152 a 0,185 | 0,000 a 0,100 | 2000 | falha |
| n5_iniciante_tempos_menos_25 | partidas com alguém em 0 ficha antes do último ciclo | 0,082 | 0,071 a 0,095 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_tempos_mais_25 | partidas com alguém em 0 ficha antes do último ciclo | 0,082 | 0,071 a 0,095 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_base | partidas com alguém em 0 ficha antes do último ciclo | 0,042 | 0,034 a 0,052 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_fichas_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,339 | 0,319 a 0,360 | 0,000 a 0,100 | 2000 | falha |
| n4_experiente_fichas_4 | partidas com alguém em 0 ficha antes do último ciclo | 0,133 | 0,118 a 0,148 | 0,000 a 0,100 | 2000 | falha |
| n4_experiente_fichas_6 | partidas com alguém em 0 ficha antes do último ciclo | 0,010 | 0,006 a 0,015 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_fichas_7 | partidas com alguém em 0 ficha antes do último ciclo | 0,003 | 0,001 a 0,007 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_1 | partidas com alguém em 0 ficha antes do último ciclo | 0,005 | 0,003 a 0,009 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,191 | 0,174 a 0,208 | 0,000 a 0,100 | 2000 | falha |
| n4_experiente_dano_alerta_0 | partidas com alguém em 0 ficha antes do último ciclo | 0,021 | 0,016 a 0,028 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_dano_alerta_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,102 | 0,089 a 0,116 | 0,000 a 0,100 | 2000 | inconclusivo |
| n4_experiente_tempos_menos_25 | partidas com alguém em 0 ficha antes do último ciclo | 0,042 | 0,034 a 0,052 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_tempos_mais_25 | partidas com alguém em 0 ficha antes do último ciclo | 0,042 | 0,034 a 0,052 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_base | partidas com alguém em 0 ficha antes do último ciclo | 0,050 | 0,041 a 0,060 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_fichas_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,399 | 0,378 a 0,421 | 0,000 a 0,100 | 2000 | falha |
| n5_experiente_fichas_4 | partidas com alguém em 0 ficha antes do último ciclo | 0,155 | 0,140 a 0,172 | 0,000 a 0,100 | 2000 | falha |
| n5_experiente_fichas_6 | partidas com alguém em 0 ficha antes do último ciclo | 0,015 | 0,011 a 0,022 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_fichas_7 | partidas com alguém em 0 ficha antes do último ciclo | 0,003 | 0,001 a 0,007 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_1 | partidas com alguém em 0 ficha antes do último ciclo | 0,006 | 0,003 a 0,010 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_3 | partidas com alguém em 0 ficha antes do último ciclo | 0,245 | 0,227 a 0,264 | 0,000 a 0,100 | 2000 | falha |
| n5_experiente_dano_alerta_0 | partidas com alguém em 0 ficha antes do último ciclo | 0,026 | 0,020 a 0,034 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_dano_alerta_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,127 | 0,113 a 0,142 | 0,000 a 0,100 | 2000 | falha |
| n5_experiente_tempos_menos_25 | partidas com alguém em 0 ficha antes do último ciclo | 0,050 | 0,041 a 0,060 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_tempos_mais_25 | partidas com alguém em 0 ficha antes do último ciclo | 0,050 | 0,041 a 0,060 | 0,000 a 0,100 | 2000 | passa |

### REQ-08: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_fichas_3 | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_fichas_4 | mediana da duração estimada (min) | 38,4 | 38,3 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_fichas_6 | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_fichas_7 | mediana da duração estimada (min) | 38,4 | 38,3 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_dano_sem_cobertura_1 | mediana da duração estimada (min) | 38,2 | 38,2 a 38,4 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_dano_sem_cobertura_3 | mediana da duração estimada (min) | 38,6 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_dano_alerta_0 | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_dano_alerta_2 | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_tempos_menos_25 | mediana da duração estimada (min) | 28,9 | 28,9 a 29,1 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_tempos_mais_25 | mediana da duração estimada (min) | 48,1 | 47,9 a 48,3 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_base | mediana da duração estimada (min) | 44,2 | 44,2 a 44,4 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_fichas_3 | mediana da duração estimada (min) | 44,2 | 44,2 a 44,4 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_fichas_4 | mediana da duração estimada (min) | 44,2 | 44,2 a 44,4 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_fichas_6 | mediana da duração estimada (min) | 44,2 | 44,2 a 44,4 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_fichas_7 | mediana da duração estimada (min) | 44,2 | 44,2 a 44,4 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_1 | mediana da duração estimada (min) | 44,1 | 43,9 a 44,2 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_3 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,6 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_dano_alerta_0 | mediana da duração estimada (min) | 44,3 | 44,2 a 44,5 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_dano_alerta_2 | mediana da duração estimada (min) | 44,3 | 44,2 a 44,5 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_tempos_menos_25 | mediana da duração estimada (min) | 33,4 | 33,2 a 33,5 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_tempos_mais_25 | mediana da duração estimada (min) | 55,4 | 55,2 a 55,6 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_base | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_fichas_3 | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_fichas_4 | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_fichas_6 | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_fichas_7 | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_dano_sem_cobertura_1 | mediana da duração estimada (min) | 38,6 | 38,4 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_dano_sem_cobertura_3 | mediana da duração estimada (min) | 38,8 | 38,6 a 38,9 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_dano_alerta_0 | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_dano_alerta_2 | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_tempos_menos_25 | mediana da duração estimada (min) | 29,1 | 29,0 a 29,2 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_tempos_mais_25 | mediana da duração estimada (min) | 48,4 | 48,2 a 48,5 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_base | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_fichas_3 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_fichas_4 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_fichas_6 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_fichas_7 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_1 | mediana da duração estimada (min) | 44,4 | 44,2 a 44,6 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_3 | mediana da duração estimada (min) | 44,6 | 44,4 a 44,8 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_dano_alerta_0 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,8 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_dano_alerta_2 | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_tempos_menos_25 | mediana da duração estimada (min) | 33,5 | 33,4 a 33,7 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_tempos_mais_25 | mediana da duração estimada (min) | 55,7 | 55,5 a 55,9 | 40,0 a 50,0 | 2000 | falha |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-09: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 88000 | passa |

Nota: o critério pede pelo menos 50000 partidas.

### REQ-10: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_fichas_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_fichas_4 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_fichas_6 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_fichas_7 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_dano_sem_cobertura_1 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,7 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_dano_sem_cobertura_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_dano_alerta_0 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_dano_alerta_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_tempos_menos_25 | percentil 90 do tempo parado por jogador e ciclo (min) | 4,3 | 4,3 a 4,3 | 0,0 a 5,0 | 2000 | passa |
| n4_iniciante_tempos_mais_25 | percentil 90 do tempo parado por jogador e ciclo (min) | 7,2 | 7,2 a 7,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_base | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_fichas_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_fichas_4 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_fichas_6 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_fichas_7 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_dano_sem_cobertura_1 | percentil 90 do tempo parado por jogador e ciclo (min) | 8,9 | 8,9 a 9,0 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_dano_sem_cobertura_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,2 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_dano_alerta_0 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_dano_alerta_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_tempos_menos_25 | percentil 90 do tempo parado por jogador e ciclo (min) | 6,8 | 6,8 a 6,9 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_tempos_mais_25 | percentil 90 do tempo parado por jogador e ciclo (min) | 11,3 | 11,3 a 11,5 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_base | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_fichas_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_fichas_4 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_fichas_6 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_fichas_7 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_dano_sem_cobertura_1 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_dano_sem_cobertura_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_dano_alerta_0 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_dano_alerta_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_tempos_menos_25 | percentil 90 do tempo parado por jogador e ciclo (min) | 4,3 | 4,3 a 4,3 | 0,0 a 5,0 | 2000 | passa |
| n4_experiente_tempos_mais_25 | percentil 90 do tempo parado por jogador e ciclo (min) | 7,2 | 7,2 a 7,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_base | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_fichas_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_fichas_4 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_fichas_6 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_fichas_7 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_dano_sem_cobertura_1 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 8,9 a 9,1 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_dano_sem_cobertura_3 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_dano_alerta_0 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_dano_alerta_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 9,1 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_tempos_menos_25 | percentil 90 do tempo parado por jogador e ciclo (min) | 6,9 | 6,8 a 7,0 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_tempos_mais_25 | percentil 90 do tempo parado por jogador e ciclo (min) | 11,5 | 11,4 a 11,6 | 0,0 a 5,0 | 2000 | falha |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-11: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,586 | 0,575 a 0,597 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_fichas_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,586 | 0,576 a 0,597 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_fichas_4 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,586 | 0,576 a 0,596 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_fichas_6 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,586 | 0,576 a 0,596 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_fichas_7 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,586 | 0,576 a 0,597 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_1 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,522 | 0,511 a 0,534 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,622 | 0,611 a 0,633 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_dano_alerta_0 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,603 | 0,592 a 0,614 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_dano_alerta_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,566 | 0,555 a 0,577 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_tempos_menos_25 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,586 | 0,576 a 0,597 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_tempos_mais_25 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,586 | 0,576 a 0,597 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,575 a 0,594 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_fichas_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,575 a 0,594 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_fichas_4 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,576 a 0,593 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_fichas_6 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,575 a 0,594 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_fichas_7 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,574 a 0,594 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_1 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,519 | 0,510 a 0,529 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,619 | 0,609 a 0,629 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_dano_alerta_0 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,596 | 0,586 a 0,605 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_dano_alerta_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,571 | 0,560 a 0,580 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_tempos_menos_25 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,575 a 0,593 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_tempos_mais_25 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,585 | 0,575 a 0,594 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,500 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_fichas_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_fichas_4 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_fichas_6 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_fichas_7 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_1 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,501 | 0,491 a 0,512 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,524 | 0,513 a 0,534 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_dano_alerta_0 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,531 | 0,519 a 0,541 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_dano_alerta_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,494 | 0,484 a 0,505 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_tempos_menos_25 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,522 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_tempos_mais_25 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,510 | 0,499 a 0,521 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,518 | 0,508 a 0,527 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_fichas_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,518 | 0,508 a 0,527 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_fichas_4 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,518 | 0,508 a 0,527 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_fichas_6 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,518 | 0,508 a 0,527 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_fichas_7 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,518 | 0,508 a 0,527 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_1 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,496 | 0,486 a 0,506 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_3 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,529 | 0,520 a 0,539 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_dano_alerta_0 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,531 | 0,522 a 0,542 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_dano_alerta_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,497 a 0,516 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_tempos_menos_25 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,518 | 0,508 a 0,528 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_tempos_mais_25 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,518 | 0,509 a 0,528 | 0,100 a 0,900 | 2000 | passa |

### REQ-12: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,078 | 0,055 a 0,099 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_fichas_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,077 | 0,055 a 0,099 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_fichas_4 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,078 | 0,056 a 0,099 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_fichas_6 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,078 | 0,056 a 0,100 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_fichas_7 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,078 | 0,057 a 0,101 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_dano_sem_cobertura_1 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,045 | 0,023 a 0,065 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,100 | 0,077 a 0,124 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_dano_alerta_0 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,084 | 0,062 a 0,106 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_dano_alerta_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,078 | 0,055 a 0,099 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_tempos_menos_25 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,078 | 0,057 a 0,101 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_tempos_mais_25 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,078 | 0,055 a 0,099 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,068 | 0,050 a 0,087 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,067 | 0,049 a 0,085 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_4 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,068 | 0,049 a 0,086 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_6 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,068 | 0,050 a 0,086 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_fichas_7 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,068 | 0,050 a 0,087 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_1 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,042 | 0,024 a 0,059 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,086 | 0,067 a 0,105 | -0,100 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_dano_alerta_0 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,071 | 0,052 a 0,089 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_dano_alerta_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,071 | 0,052 a 0,091 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_tempos_menos_25 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,068 | 0,049 a 0,088 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_tempos_mais_25 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,068 | 0,050 a 0,087 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,034 | 0,013 a 0,056 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_fichas_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,031 | 0,011 a 0,054 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_fichas_4 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,034 | 0,011 a 0,057 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_fichas_6 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,034 | 0,011 a 0,057 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_fichas_7 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,034 | 0,013 a 0,055 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_1 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,039 | 0,015 a 0,062 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_dano_sem_cobertura_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,060 | 0,039 a 0,084 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_dano_alerta_0 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,031 | 0,009 a 0,053 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_dano_alerta_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,027 | 0,005 a 0,049 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_tempos_menos_25 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,034 | 0,012 a 0,055 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_tempos_mais_25 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,034 | 0,012 a 0,055 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,066 | 0,048 a 0,084 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_fichas_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,065 | 0,046 a 0,083 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_fichas_4 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,066 | 0,048 a 0,085 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_fichas_6 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,066 | 0,048 a 0,084 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_fichas_7 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,066 | 0,048 a 0,082 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_1 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,036 | 0,018 a 0,054 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_dano_sem_cobertura_3 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,074 | 0,056 a 0,092 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_dano_alerta_0 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,069 | 0,048 a 0,088 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_dano_alerta_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,071 | 0,053 a 0,089 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_tempos_menos_25 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,066 | 0,047 a 0,084 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_tempos_mais_25 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,066 | 0,048 a 0,084 | -0,100 a 0,100 | 2000 | passa |

Nota: n4_experiente_base: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_dano_alerta_0: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_dano_alerta_2: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_dano_sem_cobertura_1: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_dano_sem_cobertura_3: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_fichas_3: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_fichas_4: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_fichas_6: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_fichas_7: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_tempos_mais_25: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_experiente_tempos_menos_25: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_base: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_dano_alerta_0: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_dano_alerta_2: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_dano_sem_cobertura_1: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_dano_sem_cobertura_3: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_fichas_3: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_fichas_4: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_fichas_6: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_fichas_7: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_tempos_mais_25: 2094 assentos começaram cobrindo, 5906 não.
Nota: n4_iniciante_tempos_menos_25: 2094 assentos começaram cobrindo, 5906 não.
Nota: n5_experiente_base: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_dano_alerta_0: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_dano_alerta_2: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_dano_sem_cobertura_1: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_dano_sem_cobertura_3: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_fichas_3: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_fichas_4: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_fichas_6: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_fichas_7: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_tempos_mais_25: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_experiente_tempos_menos_25: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_base: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_dano_alerta_0: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_dano_alerta_2: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_dano_sem_cobertura_1: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_dano_sem_cobertura_3: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_fichas_3: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_fichas_4: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_fichas_6: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_fichas_7: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_tempos_mais_25: 2647 assentos começaram cobrindo, 7353 não.
Nota: n5_iniciante_tempos_menos_25: 2647 assentos começaram cobrindo, 7353 não.

### REQ-13: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | dano de incidente / fichas movimentadas | 0,216 | 0,213 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_fichas_3 | dano de incidente / fichas movimentadas | 0,216 | 0,213 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_fichas_4 | dano de incidente / fichas movimentadas | 0,216 | 0,214 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_fichas_6 | dano de incidente / fichas movimentadas | 0,215 | 0,213 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_fichas_7 | dano de incidente / fichas movimentadas | 0,215 | 0,212 a 0,217 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_dano_sem_cobertura_1 | dano de incidente / fichas movimentadas | 0,156 | 0,154 a 0,158 | 0,200 a 0,600 | 2000 | falha |
| n4_iniciante_dano_sem_cobertura_3 | dano de incidente / fichas movimentadas | 0,266 | 0,263 a 0,268 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_dano_alerta_0 | dano de incidente / fichas movimentadas | 0,187 | 0,185 a 0,189 | 0,200 a 0,600 | 2000 | falha |
| n4_iniciante_dano_alerta_2 | dano de incidente / fichas movimentadas | 0,243 | 0,241 a 0,246 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_tempos_menos_25 | dano de incidente / fichas movimentadas | 0,216 | 0,214 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_tempos_mais_25 | dano de incidente / fichas movimentadas | 0,216 | 0,214 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_base | dano de incidente / fichas movimentadas | 0,214 | 0,212 a 0,216 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_fichas_3 | dano de incidente / fichas movimentadas | 0,214 | 0,212 a 0,216 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_fichas_4 | dano de incidente / fichas movimentadas | 0,215 | 0,212 a 0,217 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_fichas_6 | dano de incidente / fichas movimentadas | 0,214 | 0,211 a 0,216 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_fichas_7 | dano de incidente / fichas movimentadas | 0,213 | 0,211 a 0,215 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_dano_sem_cobertura_1 | dano de incidente / fichas movimentadas | 0,155 | 0,153 a 0,157 | 0,200 a 0,600 | 2000 | falha |
| n5_iniciante_dano_sem_cobertura_3 | dano de incidente / fichas movimentadas | 0,265 | 0,262 a 0,267 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_dano_alerta_0 | dano de incidente / fichas movimentadas | 0,184 | 0,181 a 0,185 | 0,200 a 0,600 | 2000 | falha |
| n5_iniciante_dano_alerta_2 | dano de incidente / fichas movimentadas | 0,242 | 0,240 a 0,245 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_tempos_menos_25 | dano de incidente / fichas movimentadas | 0,214 | 0,212 a 0,216 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_tempos_mais_25 | dano de incidente / fichas movimentadas | 0,214 | 0,212 a 0,217 | 0,200 a 0,600 | 2000 | passa |
| n4_experiente_base | dano de incidente / fichas movimentadas | 0,172 | 0,170 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_fichas_3 | dano de incidente / fichas movimentadas | 0,172 | 0,169 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_fichas_4 | dano de incidente / fichas movimentadas | 0,172 | 0,170 a 0,175 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_fichas_6 | dano de incidente / fichas movimentadas | 0,172 | 0,170 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_fichas_7 | dano de incidente / fichas movimentadas | 0,172 | 0,169 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_dano_sem_cobertura_1 | dano de incidente / fichas movimentadas | 0,125 | 0,123 a 0,127 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_dano_sem_cobertura_3 | dano de incidente / fichas movimentadas | 0,216 | 0,214 a 0,219 | 0,200 a 0,600 | 2000 | passa |
| n4_experiente_dano_alerta_0 | dano de incidente / fichas movimentadas | 0,154 | 0,152 a 0,156 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_dano_alerta_2 | dano de incidente / fichas movimentadas | 0,192 | 0,190 a 0,195 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_tempos_menos_25 | dano de incidente / fichas movimentadas | 0,172 | 0,170 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_tempos_mais_25 | dano de incidente / fichas movimentadas | 0,172 | 0,170 a 0,175 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_base | dano de incidente / fichas movimentadas | 0,175 | 0,173 a 0,177 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_fichas_3 | dano de incidente / fichas movimentadas | 0,175 | 0,172 a 0,177 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_fichas_4 | dano de incidente / fichas movimentadas | 0,175 | 0,173 a 0,177 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_fichas_6 | dano de incidente / fichas movimentadas | 0,174 | 0,172 a 0,177 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_fichas_7 | dano de incidente / fichas movimentadas | 0,174 | 0,172 a 0,176 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_dano_sem_cobertura_1 | dano de incidente / fichas movimentadas | 0,125 | 0,123 a 0,127 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_dano_sem_cobertura_3 | dano de incidente / fichas movimentadas | 0,219 | 0,216 a 0,221 | 0,200 a 0,600 | 2000 | passa |
| n5_experiente_dano_alerta_0 | dano de incidente / fichas movimentadas | 0,155 | 0,153 a 0,157 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_dano_alerta_2 | dano de incidente / fichas movimentadas | 0,195 | 0,193 a 0,198 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_tempos_menos_25 | dano de incidente / fichas movimentadas | 0,175 | 0,172 a 0,177 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_tempos_mais_25 | dano de incidente / fichas movimentadas | 0,175 | 0,172 a 0,177 | 0,200 a 0,600 | 2000 | falha |

Nota: o dano do Critical Failure não conta como dano de incidente.

## Taxa de vitória por bot (MET-07)

Sem veredito. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| n4_experiente_base | blefa_sempre_contesta_limiar | 4 | 302 | 0,257 | 0,209 a 0,308 | 0,250 |
| n4_experiente_base | blefa_nunca_contesta_nunca | 4 | 2683 | 0,255 | 0,238 a 0,272 | 0,250 |
| n4_experiente_base | blefa_nunca_contesta_limiar | 4 | 3952 | 0,249 | 0,236 a 0,264 | 0,250 |
| n4_experiente_base | blefa_sempre_contesta_nunca | 4 | 1063 | 0,237 | 0,212 a 0,262 | 0,250 |
| n4_experiente_dano_alerta_0 | blefa_sempre_contesta_limiar | 4 | 302 | 0,263 | 0,215 a 0,313 | 0,250 |
| n4_experiente_dano_alerta_0 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,252 | 0,239 a 0,265 | 0,250 |
| n4_experiente_dano_alerta_0 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,250 | 0,235 a 0,267 | 0,250 |
| n4_experiente_dano_alerta_0 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,237 | 0,213 a 0,262 | 0,250 |
| n4_experiente_dano_alerta_2 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,261 | 0,234 a 0,288 | 0,250 |
| n4_experiente_dano_alerta_2 | blefa_sempre_contesta_limiar | 4 | 302 | 0,253 | 0,205 a 0,303 | 0,250 |
| n4_experiente_dano_alerta_2 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,253 | 0,237 a 0,270 | 0,250 |
| n4_experiente_dano_alerta_2 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,245 | 0,232 a 0,257 | 0,250 |
| n4_experiente_dano_sem_cobertura_1 | blefa_sempre_contesta_limiar | 4 | 302 | 0,272 | 0,220 a 0,321 | 0,250 |
| n4_experiente_dano_sem_cobertura_1 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,254 | 0,240 a 0,267 | 0,250 |
| n4_experiente_dano_sem_cobertura_1 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,245 | 0,230 a 0,261 | 0,250 |
| n4_experiente_dano_sem_cobertura_1 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,243 | 0,217 a 0,271 | 0,250 |
| n4_experiente_dano_sem_cobertura_3 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,263 | 0,247 a 0,280 | 0,250 |
| n4_experiente_dano_sem_cobertura_3 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,259 | 0,234 a 0,288 | 0,250 |
| n4_experiente_dano_sem_cobertura_3 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,242 | 0,229 a 0,256 | 0,250 |
| n4_experiente_dano_sem_cobertura_3 | blefa_sempre_contesta_limiar | 4 | 302 | 0,197 | 0,156 a 0,243 | 0,250 |
| n4_experiente_fichas_3 | blefa_sempre_contesta_limiar | 4 | 302 | 0,257 | 0,207 a 0,306 | 0,250 |
| n4_experiente_fichas_3 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,254 | 0,238 a 0,270 | 0,250 |
| n4_experiente_fichas_3 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,250 | 0,237 a 0,263 | 0,250 |
| n4_experiente_fichas_3 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,238 | 0,213 a 0,265 | 0,250 |
| n4_experiente_fichas_4 | blefa_sempre_contesta_limiar | 4 | 302 | 0,257 | 0,209 a 0,303 | 0,250 |
| n4_experiente_fichas_4 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,255 | 0,238 a 0,271 | 0,250 |
| n4_experiente_fichas_4 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,250 | 0,237 a 0,264 | 0,250 |
| n4_experiente_fichas_4 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,237 | 0,211 a 0,263 | 0,250 |
| n4_experiente_fichas_6 | blefa_sempre_contesta_limiar | 4 | 302 | 0,257 | 0,210 a 0,303 | 0,250 |
| n4_experiente_fichas_6 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,255 | 0,239 a 0,272 | 0,250 |
| n4_experiente_fichas_6 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,249 | 0,235 a 0,263 | 0,250 |
| n4_experiente_fichas_6 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,237 | 0,211 a 0,262 | 0,250 |
| n4_experiente_fichas_7 | blefa_sempre_contesta_limiar | 4 | 302 | 0,257 | 0,209 a 0,306 | 0,250 |
| n4_experiente_fichas_7 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,255 | 0,239 a 0,271 | 0,250 |
| n4_experiente_fichas_7 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,249 | 0,236 a 0,263 | 0,250 |
| n4_experiente_fichas_7 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,237 | 0,213 a 0,262 | 0,250 |
| n4_experiente_tempos_mais_25 | blefa_sempre_contesta_limiar | 4 | 302 | 0,257 | 0,212 a 0,301 | 0,250 |
| n4_experiente_tempos_mais_25 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,255 | 0,238 a 0,271 | 0,250 |
| n4_experiente_tempos_mais_25 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,249 | 0,236 a 0,263 | 0,250 |
| n4_experiente_tempos_mais_25 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,237 | 0,213 a 0,263 | 0,250 |
| n4_experiente_tempos_menos_25 | blefa_sempre_contesta_limiar | 4 | 302 | 0,257 | 0,207 a 0,306 | 0,250 |
| n4_experiente_tempos_menos_25 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,255 | 0,240 a 0,272 | 0,250 |
| n4_experiente_tempos_menos_25 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,249 | 0,236 a 0,264 | 0,250 |
| n4_experiente_tempos_menos_25 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,237 | 0,214 a 0,264 | 0,250 |
| n4_iniciante_base | blefa_sempre_contesta_nunca | 4 | 1063 | 0,267 | 0,239 a 0,293 | 0,250 |
| n4_iniciante_base | blefa_nunca_contesta_nunca | 4 | 2683 | 0,253 | 0,236 a 0,269 | 0,250 |
| n4_iniciante_base | blefa_nunca_contesta_limiar | 4 | 3952 | 0,245 | 0,232 a 0,258 | 0,250 |
| n4_iniciante_base | blefa_sempre_contesta_limiar | 4 | 302 | 0,227 | 0,180 a 0,276 | 0,250 |
| n4_iniciante_dano_alerta_0 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,263 | 0,236 a 0,288 | 0,250 |
| n4_iniciante_dano_alerta_0 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,254 | 0,238 a 0,272 | 0,250 |
| n4_iniciante_dano_alerta_0 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,244 | 0,231 a 0,257 | 0,250 |
| n4_iniciante_dano_alerta_0 | blefa_sempre_contesta_limiar | 4 | 302 | 0,243 | 0,194 a 0,293 | 0,250 |
| n4_iniciante_dano_alerta_2 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,262 | 0,246 a 0,278 | 0,250 |
| n4_iniciante_dano_alerta_2 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,261 | 0,236 a 0,289 | 0,250 |
| n4_iniciante_dano_alerta_2 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,242 | 0,228 a 0,256 | 0,250 |
| n4_iniciante_dano_alerta_2 | blefa_sempre_contesta_limiar | 4 | 302 | 0,210 | 0,162 a 0,258 | 0,250 |
| n4_iniciante_dano_sem_cobertura_1 | blefa_sempre_contesta_limiar | 4 | 302 | 0,268 | 0,222 a 0,320 | 0,250 |
| n4_iniciante_dano_sem_cobertura_1 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,256 | 0,240 a 0,272 | 0,250 |
| n4_iniciante_dano_sem_cobertura_1 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,247 | 0,222 a 0,273 | 0,250 |
| n4_iniciante_dano_sem_cobertura_1 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,245 | 0,232 a 0,258 | 0,250 |
| n4_iniciante_dano_sem_cobertura_3 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,257 | 0,241 a 0,274 | 0,250 |
| n4_iniciante_dano_sem_cobertura_3 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,256 | 0,231 a 0,282 | 0,250 |
| n4_iniciante_dano_sem_cobertura_3 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,244 | 0,231 a 0,258 | 0,250 |
| n4_iniciante_dano_sem_cobertura_3 | blefa_sempre_contesta_limiar | 4 | 302 | 0,242 | 0,192 a 0,291 | 0,250 |
| n4_iniciante_fichas_3 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,262 | 0,237 a 0,288 | 0,250 |
| n4_iniciante_fichas_3 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,253 | 0,237 a 0,270 | 0,250 |
| n4_iniciante_fichas_3 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,246 | 0,234 a 0,260 | 0,250 |
| n4_iniciante_fichas_3 | blefa_sempre_contesta_limiar | 4 | 302 | 0,227 | 0,180 a 0,277 | 0,250 |
| n4_iniciante_fichas_4 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,267 | 0,240 a 0,295 | 0,250 |
| n4_iniciante_fichas_4 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,253 | 0,236 a 0,269 | 0,250 |
| n4_iniciante_fichas_4 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,245 | 0,231 a 0,259 | 0,250 |
| n4_iniciante_fichas_4 | blefa_sempre_contesta_limiar | 4 | 302 | 0,227 | 0,185 a 0,276 | 0,250 |
| n4_iniciante_fichas_6 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,267 | 0,241 a 0,295 | 0,250 |
| n4_iniciante_fichas_6 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,252 | 0,235 a 0,269 | 0,250 |
| n4_iniciante_fichas_6 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,246 | 0,232 a 0,259 | 0,250 |
| n4_iniciante_fichas_6 | blefa_sempre_contesta_limiar | 4 | 302 | 0,227 | 0,180 a 0,275 | 0,250 |
| n4_iniciante_fichas_7 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,267 | 0,243 a 0,293 | 0,250 |
| n4_iniciante_fichas_7 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,252 | 0,236 a 0,268 | 0,250 |
| n4_iniciante_fichas_7 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,246 | 0,232 a 0,259 | 0,250 |
| n4_iniciante_fichas_7 | blefa_sempre_contesta_limiar | 4 | 302 | 0,227 | 0,182 a 0,275 | 0,250 |
| n4_iniciante_tempos_mais_25 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,267 | 0,239 a 0,292 | 0,250 |
| n4_iniciante_tempos_mais_25 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,253 | 0,237 a 0,268 | 0,250 |
| n4_iniciante_tempos_mais_25 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,245 | 0,232 a 0,259 | 0,250 |
| n4_iniciante_tempos_mais_25 | blefa_sempre_contesta_limiar | 4 | 302 | 0,227 | 0,182 a 0,275 | 0,250 |
| n4_iniciante_tempos_menos_25 | blefa_sempre_contesta_nunca | 4 | 1063 | 0,267 | 0,238 a 0,293 | 0,250 |
| n4_iniciante_tempos_menos_25 | blefa_nunca_contesta_nunca | 4 | 2683 | 0,253 | 0,237 a 0,269 | 0,250 |
| n4_iniciante_tempos_menos_25 | blefa_nunca_contesta_limiar | 4 | 3952 | 0,245 | 0,231 a 0,258 | 0,250 |
| n4_iniciante_tempos_menos_25 | blefa_sempre_contesta_limiar | 4 | 302 | 0,227 | 0,180 a 0,275 | 0,250 |
| n5_experiente_base | blefa_nunca_contesta_nunca | 5 | 3198 | 0,213 | 0,199 a 0,228 | 0,200 |
| n5_experiente_base | blefa_sempre_contesta_limiar | 5 | 136 | 0,210 | 0,140 a 0,276 | 0,200 |
| n5_experiente_base | blefa_nunca_contesta_limiar | 5 | 5402 | 0,195 | 0,183 a 0,205 | 0,200 |
| n5_experiente_base | blefa_sempre_contesta_nunca | 5 | 1264 | 0,187 | 0,165 a 0,208 | 0,200 |
| n5_experiente_dano_alerta_0 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,207 | 0,192 a 0,221 | 0,200 |
| n5_experiente_dano_alerta_0 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,201 | 0,190 a 0,212 | 0,200 |
| n5_experiente_dano_alerta_0 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,182 | 0,161 a 0,203 | 0,200 |
| n5_experiente_dano_alerta_0 | blefa_sempre_contesta_limiar | 5 | 136 | 0,169 | 0,107 a 0,239 | 0,200 |
| n5_experiente_dano_alerta_2 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,211 | 0,197 a 0,224 | 0,200 |
| n5_experiente_dano_alerta_2 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,196 | 0,186 a 0,206 | 0,200 |
| n5_experiente_dano_alerta_2 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,190 | 0,170 a 0,212 | 0,200 |
| n5_experiente_dano_alerta_2 | blefa_sempre_contesta_limiar | 5 | 136 | 0,184 | 0,118 a 0,250 | 0,200 |
| n5_experiente_dano_sem_cobertura_1 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,205 | 0,192 a 0,219 | 0,200 |
| n5_experiente_dano_sem_cobertura_1 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,199 | 0,189 a 0,210 | 0,200 |
| n5_experiente_dano_sem_cobertura_1 | blefa_sempre_contesta_limiar | 5 | 136 | 0,195 | 0,132 a 0,261 | 0,200 |
| n5_experiente_dano_sem_cobertura_1 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,190 | 0,167 a 0,212 | 0,200 |
| n5_experiente_dano_sem_cobertura_3 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,216 | 0,203 a 0,231 | 0,200 |
| n5_experiente_dano_sem_cobertura_3 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,196 | 0,174 a 0,217 | 0,200 |
| n5_experiente_dano_sem_cobertura_3 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,192 | 0,182 a 0,202 | 0,200 |
| n5_experiente_dano_sem_cobertura_3 | blefa_sempre_contesta_limiar | 5 | 136 | 0,188 | 0,121 a 0,254 | 0,200 |
| n5_experiente_fichas_3 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,213 | 0,198 a 0,228 | 0,200 |
| n5_experiente_fichas_3 | blefa_sempre_contesta_limiar | 5 | 136 | 0,210 | 0,147 a 0,283 | 0,200 |
| n5_experiente_fichas_3 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,195 | 0,185 a 0,206 | 0,200 |
| n5_experiente_fichas_3 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,187 | 0,167 a 0,209 | 0,200 |
| n5_experiente_fichas_4 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,213 | 0,198 a 0,227 | 0,200 |
| n5_experiente_fichas_4 | blefa_sempre_contesta_limiar | 5 | 136 | 0,210 | 0,147 a 0,276 | 0,200 |
| n5_experiente_fichas_4 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,195 | 0,184 a 0,205 | 0,200 |
| n5_experiente_fichas_4 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,187 | 0,166 a 0,208 | 0,200 |
| n5_experiente_fichas_6 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,213 | 0,199 a 0,227 | 0,200 |
| n5_experiente_fichas_6 | blefa_sempre_contesta_limiar | 5 | 136 | 0,210 | 0,140 a 0,279 | 0,200 |
| n5_experiente_fichas_6 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,195 | 0,185 a 0,205 | 0,200 |
| n5_experiente_fichas_6 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,187 | 0,166 a 0,207 | 0,200 |
| n5_experiente_fichas_7 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,213 | 0,200 a 0,229 | 0,200 |
| n5_experiente_fichas_7 | blefa_sempre_contesta_limiar | 5 | 136 | 0,210 | 0,143 a 0,287 | 0,200 |
| n5_experiente_fichas_7 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,195 | 0,184 a 0,206 | 0,200 |
| n5_experiente_fichas_7 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,187 | 0,165 a 0,208 | 0,200 |
| n5_experiente_tempos_mais_25 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,213 | 0,199 a 0,227 | 0,200 |
| n5_experiente_tempos_mais_25 | blefa_sempre_contesta_limiar | 5 | 136 | 0,210 | 0,143 a 0,279 | 0,200 |
| n5_experiente_tempos_mais_25 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,195 | 0,185 a 0,205 | 0,200 |
| n5_experiente_tempos_mais_25 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,187 | 0,165 a 0,210 | 0,200 |
| n5_experiente_tempos_menos_25 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,213 | 0,199 a 0,227 | 0,200 |
| n5_experiente_tempos_menos_25 | blefa_sempre_contesta_limiar | 5 | 136 | 0,210 | 0,143 a 0,279 | 0,200 |
| n5_experiente_tempos_menos_25 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,195 | 0,184 a 0,206 | 0,200 |
| n5_experiente_tempos_menos_25 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,187 | 0,165 a 0,208 | 0,200 |
| n5_iniciante_base | blefa_nunca_contesta_nunca | 5 | 3198 | 0,207 | 0,194 a 0,221 | 0,200 |
| n5_iniciante_base | blefa_nunca_contesta_limiar | 5 | 5402 | 0,204 | 0,193 a 0,215 | 0,200 |
| n5_iniciante_base | blefa_sempre_contesta_limiar | 5 | 136 | 0,191 | 0,125 a 0,257 | 0,200 |
| n5_iniciante_base | blefa_sempre_contesta_nunca | 5 | 1264 | 0,167 | 0,146 a 0,188 | 0,200 |
| n5_iniciante_dano_alerta_0 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,214 | 0,200 a 0,228 | 0,200 |
| n5_iniciante_dano_alerta_0 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,197 | 0,187 a 0,208 | 0,200 |
| n5_iniciante_dano_alerta_0 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,182 | 0,160 a 0,202 | 0,200 |
| n5_iniciante_dano_alerta_0 | blefa_sempre_contesta_limiar | 5 | 136 | 0,162 | 0,103 a 0,221 | 0,200 |
| n5_iniciante_dano_alerta_2 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,214 | 0,199 a 0,229 | 0,200 |
| n5_iniciante_dano_alerta_2 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,199 | 0,189 a 0,210 | 0,200 |
| n5_iniciante_dano_alerta_2 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,171 | 0,151 a 0,190 | 0,200 |
| n5_iniciante_dano_alerta_2 | blefa_sempre_contesta_limiar | 5 | 136 | 0,162 | 0,107 a 0,224 | 0,200 |
| n5_iniciante_dano_sem_cobertura_1 | blefa_sempre_contesta_limiar | 5 | 136 | 0,213 | 0,147 a 0,279 | 0,200 |
| n5_iniciante_dano_sem_cobertura_1 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,205 | 0,192 a 0,219 | 0,200 |
| n5_iniciante_dano_sem_cobertura_1 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,200 | 0,189 a 0,210 | 0,200 |
| n5_iniciante_dano_sem_cobertura_1 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,186 | 0,166 a 0,208 | 0,200 |
| n5_iniciante_dano_sem_cobertura_3 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,207 | 0,194 a 0,222 | 0,200 |
| n5_iniciante_dano_sem_cobertura_3 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,198 | 0,188 a 0,209 | 0,200 |
| n5_iniciante_dano_sem_cobertura_3 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,192 | 0,170 a 0,213 | 0,200 |
| n5_iniciante_dano_sem_cobertura_3 | blefa_sempre_contesta_limiar | 5 | 136 | 0,191 | 0,125 a 0,257 | 0,200 |
| n5_iniciante_fichas_3 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,207 | 0,193 a 0,220 | 0,200 |
| n5_iniciante_fichas_3 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,204 | 0,193 a 0,215 | 0,200 |
| n5_iniciante_fichas_3 | blefa_sempre_contesta_limiar | 5 | 136 | 0,191 | 0,132 a 0,258 | 0,200 |
| n5_iniciante_fichas_3 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,165 | 0,146 a 0,185 | 0,200 |
| n5_iniciante_fichas_4 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,206 | 0,193 a 0,220 | 0,200 |
| n5_iniciante_fichas_4 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,204 | 0,194 a 0,216 | 0,200 |
| n5_iniciante_fichas_4 | blefa_sempre_contesta_limiar | 5 | 136 | 0,191 | 0,132 a 0,258 | 0,200 |
| n5_iniciante_fichas_4 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,167 | 0,146 a 0,187 | 0,200 |
| n5_iniciante_fichas_6 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,207 | 0,193 a 0,220 | 0,200 |
| n5_iniciante_fichas_6 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,204 | 0,193 a 0,215 | 0,200 |
| n5_iniciante_fichas_6 | blefa_sempre_contesta_limiar | 5 | 136 | 0,191 | 0,132 a 0,257 | 0,200 |
| n5_iniciante_fichas_6 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,167 | 0,148 a 0,187 | 0,200 |
| n5_iniciante_fichas_7 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,207 | 0,194 a 0,220 | 0,200 |
| n5_iniciante_fichas_7 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,204 | 0,193 a 0,215 | 0,200 |
| n5_iniciante_fichas_7 | blefa_sempre_contesta_limiar | 5 | 136 | 0,191 | 0,125 a 0,265 | 0,200 |
| n5_iniciante_fichas_7 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,167 | 0,147 a 0,188 | 0,200 |
| n5_iniciante_tempos_mais_25 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,207 | 0,193 a 0,221 | 0,200 |
| n5_iniciante_tempos_mais_25 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,204 | 0,193 a 0,215 | 0,200 |
| n5_iniciante_tempos_mais_25 | blefa_sempre_contesta_limiar | 5 | 136 | 0,191 | 0,125 a 0,257 | 0,200 |
| n5_iniciante_tempos_mais_25 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,167 | 0,146 a 0,187 | 0,200 |
| n5_iniciante_tempos_menos_25 | blefa_nunca_contesta_nunca | 5 | 3198 | 0,207 | 0,193 a 0,222 | 0,200 |
| n5_iniciante_tempos_menos_25 | blefa_nunca_contesta_limiar | 5 | 5402 | 0,204 | 0,194 a 0,214 | 0,200 |
| n5_iniciante_tempos_menos_25 | blefa_sempre_contesta_limiar | 5 | 136 | 0,191 | 0,132 a 0,257 | 0,200 |
| n5_iniciante_tempos_menos_25 | blefa_sempre_contesta_nunca | 5 | 1264 | 0,167 | 0,147 a 0,189 | 0,200 |

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903). Na v2 é só descrição: o placar em fichas não está na mesma escala dos pontos da v1, e a comparação entre as versões é feita pelo REQ-02 (autor, 2026-11-10).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| n4_iniciante_base | v2 | 4 | 2000 | **1,50** | 0,741 | 0,721 a 0,759 |
| n4_iniciante_base | v2 | 4 | 2000 | 1,25 | 0,946 | 0,935 a 0,955 |
| n4_iniciante_base | v2 | 4 | 2000 | 2,00 | 0,289 | 0,270 a 0,309 |
| n4_iniciante_fichas_3 | v2 | 4 | 2000 | **1,50** | 0,825 | 0,807 a 0,841 |
| n4_iniciante_fichas_3 | v2 | 4 | 2000 | 1,25 | 0,958 | 0,948 a 0,966 |
| n4_iniciante_fichas_3 | v2 | 4 | 2000 | 2,00 | 0,380 | 0,358 a 0,401 |
| n4_iniciante_fichas_4 | v2 | 4 | 2000 | **1,50** | 0,801 | 0,783 a 0,818 |
| n4_iniciante_fichas_4 | v2 | 4 | 2000 | 1,25 | 0,955 | 0,945 a 0,963 |
| n4_iniciante_fichas_4 | v2 | 4 | 2000 | 2,00 | 0,340 | 0,319 a 0,361 |
| n4_iniciante_fichas_6 | v2 | 4 | 2000 | **1,50** | 0,679 | 0,659 a 0,700 |
| n4_iniciante_fichas_6 | v2 | 4 | 2000 | 1,25 | 0,928 | 0,916 a 0,939 |
| n4_iniciante_fichas_6 | v2 | 4 | 2000 | 2,00 | 0,234 | 0,216 a 0,254 |
| n4_iniciante_fichas_7 | v2 | 4 | 2000 | **1,50** | 0,612 | 0,590 a 0,633 |
| n4_iniciante_fichas_7 | v2 | 4 | 2000 | 1,25 | 0,898 | 0,884 a 0,911 |
| n4_iniciante_fichas_7 | v2 | 4 | 2000 | 2,00 | 0,173 | 0,157 a 0,190 |
| n4_iniciante_dano_sem_cobertura_1 | v2 | 4 | 2000 | **1,50** | 0,642 | 0,621 a 0,663 |
| n4_iniciante_dano_sem_cobertura_1 | v2 | 4 | 2000 | 1,25 | 0,898 | 0,884 a 0,911 |
| n4_iniciante_dano_sem_cobertura_1 | v2 | 4 | 2000 | 2,00 | 0,168 | 0,152 a 0,185 |
| n4_iniciante_dano_sem_cobertura_3 | v2 | 4 | 2000 | **1,50** | 0,826 | 0,809 a 0,842 |
| n4_iniciante_dano_sem_cobertura_3 | v2 | 4 | 2000 | 1,25 | 0,960 | 0,950 a 0,967 |
| n4_iniciante_dano_sem_cobertura_3 | v2 | 4 | 2000 | 2,00 | 0,409 | 0,388 a 0,431 |
| n4_iniciante_dano_alerta_0 | v2 | 4 | 2000 | **1,50** | 0,703 | 0,682 a 0,722 |
| n4_iniciante_dano_alerta_0 | v2 | 4 | 2000 | 1,25 | 0,921 | 0,909 a 0,932 |
| n4_iniciante_dano_alerta_0 | v2 | 4 | 2000 | 2,00 | 0,239 | 0,221 a 0,259 |
| n4_iniciante_dano_alerta_2 | v2 | 4 | 2000 | **1,50** | 0,792 | 0,774 a 0,809 |
| n4_iniciante_dano_alerta_2 | v2 | 4 | 2000 | 1,25 | 0,956 | 0,946 a 0,964 |
| n4_iniciante_dano_alerta_2 | v2 | 4 | 2000 | 2,00 | 0,347 | 0,327 a 0,369 |
| n4_iniciante_tempos_menos_25 | v2 | 4 | 2000 | **1,50** | 0,741 | 0,721 a 0,759 |
| n4_iniciante_tempos_menos_25 | v2 | 4 | 2000 | 1,25 | 0,946 | 0,935 a 0,955 |
| n4_iniciante_tempos_menos_25 | v2 | 4 | 2000 | 2,00 | 0,289 | 0,270 a 0,309 |
| n4_iniciante_tempos_mais_25 | v2 | 4 | 2000 | **1,50** | 0,741 | 0,721 a 0,759 |
| n4_iniciante_tempos_mais_25 | v2 | 4 | 2000 | 1,25 | 0,946 | 0,935 a 0,955 |
| n4_iniciante_tempos_mais_25 | v2 | 4 | 2000 | 2,00 | 0,289 | 0,270 a 0,309 |
| n5_iniciante_base | v2 | 5 | 2000 | **1,50** | 0,750 | 0,730 a 0,768 |
| n5_iniciante_base | v2 | 5 | 2000 | 1,25 | 0,966 | 0,957 a 0,973 |
| n5_iniciante_base | v2 | 5 | 2000 | 2,00 | 0,293 | 0,273 a 0,313 |
| n5_iniciante_fichas_3 | v2 | 5 | 2000 | **1,50** | 0,847 | 0,831 a 0,862 |
| n5_iniciante_fichas_3 | v2 | 5 | 2000 | 1,25 | 0,978 | 0,970 a 0,983 |
| n5_iniciante_fichas_3 | v2 | 5 | 2000 | 2,00 | 0,412 | 0,391 a 0,434 |
| n5_iniciante_fichas_4 | v2 | 5 | 2000 | **1,50** | 0,814 | 0,796 a 0,830 |
| n5_iniciante_fichas_4 | v2 | 5 | 2000 | 1,25 | 0,974 | 0,966 a 0,980 |
| n5_iniciante_fichas_4 | v2 | 5 | 2000 | 2,00 | 0,353 | 0,332 a 0,374 |
| n5_iniciante_fichas_6 | v2 | 5 | 2000 | **1,50** | 0,696 | 0,675 a 0,715 |
| n5_iniciante_fichas_6 | v2 | 5 | 2000 | 1,25 | 0,952 | 0,942 a 0,961 |
| n5_iniciante_fichas_6 | v2 | 5 | 2000 | 2,00 | 0,211 | 0,194 a 0,229 |
| n5_iniciante_fichas_7 | v2 | 5 | 2000 | **1,50** | 0,616 | 0,594 a 0,637 |
| n5_iniciante_fichas_7 | v2 | 5 | 2000 | 1,25 | 0,930 | 0,918 a 0,940 |
| n5_iniciante_fichas_7 | v2 | 5 | 2000 | 2,00 | 0,147 | 0,133 a 0,164 |
| n5_iniciante_dano_sem_cobertura_1 | v2 | 5 | 2000 | **1,50** | 0,623 | 0,601 a 0,643 |
| n5_iniciante_dano_sem_cobertura_1 | v2 | 5 | 2000 | 1,25 | 0,936 | 0,925 a 0,946 |
| n5_iniciante_dano_sem_cobertura_1 | v2 | 5 | 2000 | 2,00 | 0,152 | 0,137 a 0,168 |
| n5_iniciante_dano_sem_cobertura_3 | v2 | 5 | 2000 | **1,50** | 0,848 | 0,831 a 0,863 |
| n5_iniciante_dano_sem_cobertura_3 | v2 | 5 | 2000 | 1,25 | 0,983 | 0,976 a 0,987 |
| n5_iniciante_dano_sem_cobertura_3 | v2 | 5 | 2000 | 2,00 | 0,423 | 0,402 a 0,445 |
| n5_iniciante_dano_alerta_0 | v2 | 5 | 2000 | **1,50** | 0,702 | 0,682 a 0,722 |
| n5_iniciante_dano_alerta_0 | v2 | 5 | 2000 | 1,25 | 0,948 | 0,937 a 0,957 |
| n5_iniciante_dano_alerta_0 | v2 | 5 | 2000 | 2,00 | 0,241 | 0,223 a 0,261 |
| n5_iniciante_dano_alerta_2 | v2 | 5 | 2000 | **1,50** | 0,813 | 0,795 a 0,829 |
| n5_iniciante_dano_alerta_2 | v2 | 5 | 2000 | 1,25 | 0,978 | 0,970 a 0,983 |
| n5_iniciante_dano_alerta_2 | v2 | 5 | 2000 | 2,00 | 0,368 | 0,348 a 0,390 |
| n5_iniciante_tempos_menos_25 | v2 | 5 | 2000 | **1,50** | 0,750 | 0,730 a 0,768 |
| n5_iniciante_tempos_menos_25 | v2 | 5 | 2000 | 1,25 | 0,966 | 0,957 a 0,973 |
| n5_iniciante_tempos_menos_25 | v2 | 5 | 2000 | 2,00 | 0,293 | 0,273 a 0,313 |
| n5_iniciante_tempos_mais_25 | v2 | 5 | 2000 | **1,50** | 0,750 | 0,730 a 0,768 |
| n5_iniciante_tempos_mais_25 | v2 | 5 | 2000 | 1,25 | 0,966 | 0,957 a 0,973 |
| n5_iniciante_tempos_mais_25 | v2 | 5 | 2000 | 2,00 | 0,293 | 0,273 a 0,313 |
| n4_experiente_base | v2 | 4 | 2000 | **1,50** | 0,695 | 0,674 a 0,715 |
| n4_experiente_base | v2 | 4 | 2000 | 1,25 | 0,916 | 0,903 a 0,927 |
| n4_experiente_base | v2 | 4 | 2000 | 2,00 | 0,229 | 0,211 a 0,247 |
| n4_experiente_fichas_3 | v2 | 4 | 2000 | **1,50** | 0,790 | 0,772 a 0,808 |
| n4_experiente_fichas_3 | v2 | 4 | 2000 | 1,25 | 0,950 | 0,940 a 0,959 |
| n4_experiente_fichas_3 | v2 | 4 | 2000 | 2,00 | 0,326 | 0,305 a 0,346 |
| n4_experiente_fichas_4 | v2 | 4 | 2000 | **1,50** | 0,747 | 0,727 a 0,766 |
| n4_experiente_fichas_4 | v2 | 4 | 2000 | 1,25 | 0,938 | 0,927 a 0,948 |
| n4_experiente_fichas_4 | v2 | 4 | 2000 | 2,00 | 0,281 | 0,262 a 0,301 |
| n4_experiente_fichas_6 | v2 | 4 | 2000 | **1,50** | 0,621 | 0,599 a 0,642 |
| n4_experiente_fichas_6 | v2 | 4 | 2000 | 1,25 | 0,893 | 0,879 a 0,906 |
| n4_experiente_fichas_6 | v2 | 4 | 2000 | 2,00 | 0,172 | 0,156 a 0,189 |
| n4_experiente_fichas_7 | v2 | 4 | 2000 | **1,50** | 0,555 | 0,533 a 0,577 |
| n4_experiente_fichas_7 | v2 | 4 | 2000 | 1,25 | 0,864 | 0,848 a 0,878 |
| n4_experiente_fichas_7 | v2 | 4 | 2000 | 2,00 | 0,124 | 0,111 a 0,140 |
| n4_experiente_dano_sem_cobertura_1 | v2 | 4 | 2000 | **1,50** | 0,556 | 0,534 a 0,578 |
| n4_experiente_dano_sem_cobertura_1 | v2 | 4 | 2000 | 1,25 | 0,875 | 0,859 a 0,888 |
| n4_experiente_dano_sem_cobertura_1 | v2 | 4 | 2000 | 2,00 | 0,122 | 0,109 a 0,138 |
| n4_experiente_dano_sem_cobertura_3 | v2 | 4 | 2000 | **1,50** | 0,785 | 0,766 a 0,802 |
| n4_experiente_dano_sem_cobertura_3 | v2 | 4 | 2000 | 1,25 | 0,951 | 0,940 a 0,959 |
| n4_experiente_dano_sem_cobertura_3 | v2 | 4 | 2000 | 2,00 | 0,342 | 0,321 a 0,363 |
| n4_experiente_dano_alerta_0 | v2 | 4 | 2000 | **1,50** | 0,625 | 0,604 a 0,646 |
| n4_experiente_dano_alerta_0 | v2 | 4 | 2000 | 1,25 | 0,905 | 0,892 a 0,918 |
| n4_experiente_dano_alerta_0 | v2 | 4 | 2000 | 2,00 | 0,154 | 0,139 a 0,171 |
| n4_experiente_dano_alerta_2 | v2 | 4 | 2000 | **1,50** | 0,720 | 0,699 a 0,739 |
| n4_experiente_dano_alerta_2 | v2 | 4 | 2000 | 1,25 | 0,929 | 0,917 a 0,939 |
| n4_experiente_dano_alerta_2 | v2 | 4 | 2000 | 2,00 | 0,254 | 0,235 a 0,274 |
| n4_experiente_tempos_menos_25 | v2 | 4 | 2000 | **1,50** | 0,695 | 0,674 a 0,715 |
| n4_experiente_tempos_menos_25 | v2 | 4 | 2000 | 1,25 | 0,916 | 0,903 a 0,927 |
| n4_experiente_tempos_menos_25 | v2 | 4 | 2000 | 2,00 | 0,229 | 0,211 a 0,247 |
| n4_experiente_tempos_mais_25 | v2 | 4 | 2000 | **1,50** | 0,695 | 0,674 a 0,715 |
| n4_experiente_tempos_mais_25 | v2 | 4 | 2000 | 1,25 | 0,916 | 0,903 a 0,927 |
| n4_experiente_tempos_mais_25 | v2 | 4 | 2000 | 2,00 | 0,229 | 0,211 a 0,247 |
| n5_experiente_base | v2 | 5 | 2000 | **1,50** | 0,680 | 0,660 a 0,701 |
| n5_experiente_base | v2 | 5 | 2000 | 1,25 | 0,951 | 0,940 a 0,959 |
| n5_experiente_base | v2 | 5 | 2000 | 2,00 | 0,200 | 0,183 a 0,218 |
| n5_experiente_fichas_3 | v2 | 5 | 2000 | **1,50** | 0,793 | 0,775 a 0,810 |
| n5_experiente_fichas_3 | v2 | 5 | 2000 | 1,25 | 0,971 | 0,963 a 0,977 |
| n5_experiente_fichas_3 | v2 | 5 | 2000 | 2,00 | 0,318 | 0,298 a 0,339 |
| n5_experiente_fichas_4 | v2 | 5 | 2000 | **1,50** | 0,740 | 0,720 a 0,759 |
| n5_experiente_fichas_4 | v2 | 5 | 2000 | 1,25 | 0,964 | 0,954 a 0,971 |
| n5_experiente_fichas_4 | v2 | 5 | 2000 | 2,00 | 0,260 | 0,241 a 0,279 |
| n5_experiente_fichas_6 | v2 | 5 | 2000 | **1,50** | 0,612 | 0,590 a 0,633 |
| n5_experiente_fichas_6 | v2 | 5 | 2000 | 1,25 | 0,934 | 0,922 a 0,944 |
| n5_experiente_fichas_6 | v2 | 5 | 2000 | 2,00 | 0,139 | 0,125 a 0,155 |
| n5_experiente_fichas_7 | v2 | 5 | 2000 | **1,50** | 0,529 | 0,507 a 0,551 |
| n5_experiente_fichas_7 | v2 | 5 | 2000 | 1,25 | 0,908 | 0,895 a 0,920 |
| n5_experiente_fichas_7 | v2 | 5 | 2000 | 2,00 | 0,094 | 0,082 a 0,108 |
| n5_experiente_dano_sem_cobertura_1 | v2 | 5 | 2000 | **1,50** | 0,521 | 0,500 a 0,543 |
| n5_experiente_dano_sem_cobertura_1 | v2 | 5 | 2000 | 1,25 | 0,916 | 0,903 a 0,927 |
| n5_experiente_dano_sem_cobertura_1 | v2 | 5 | 2000 | 2,00 | 0,090 | 0,078 a 0,103 |
| n5_experiente_dano_sem_cobertura_3 | v2 | 5 | 2000 | **1,50** | 0,811 | 0,794 a 0,828 |
| n5_experiente_dano_sem_cobertura_3 | v2 | 5 | 2000 | 1,25 | 0,979 | 0,971 a 0,984 |
| n5_experiente_dano_sem_cobertura_3 | v2 | 5 | 2000 | 2,00 | 0,347 | 0,327 a 0,369 |
| n5_experiente_dano_alerta_0 | v2 | 5 | 2000 | **1,50** | 0,640 | 0,619 a 0,661 |
| n5_experiente_dano_alerta_0 | v2 | 5 | 2000 | 1,25 | 0,941 | 0,930 a 0,951 |
| n5_experiente_dano_alerta_0 | v2 | 5 | 2000 | 2,00 | 0,146 | 0,132 a 0,163 |
| n5_experiente_dano_alerta_2 | v2 | 5 | 2000 | **1,50** | 0,743 | 0,723 a 0,761 |
| n5_experiente_dano_alerta_2 | v2 | 5 | 2000 | 1,25 | 0,966 | 0,957 a 0,973 |
| n5_experiente_dano_alerta_2 | v2 | 5 | 2000 | 2,00 | 0,242 | 0,224 a 0,262 |
| n5_experiente_tempos_menos_25 | v2 | 5 | 2000 | **1,50** | 0,680 | 0,660 a 0,701 |
| n5_experiente_tempos_menos_25 | v2 | 5 | 2000 | 1,25 | 0,951 | 0,940 a 0,959 |
| n5_experiente_tempos_menos_25 | v2 | 5 | 2000 | 2,00 | 0,200 | 0,183 a 0,218 |
| n5_experiente_tempos_mais_25 | v2 | 5 | 2000 | **1,50** | 0,680 | 0,660 a 0,701 |
| n5_experiente_tempos_mais_25 | v2 | 5 | 2000 | 1,25 | 0,951 | 0,940 a 0,959 |
| n5_experiente_tempos_mais_25 | v2 | 5 | 2000 | 2,00 | 0,200 | 0,183 a 0,218 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Sistema cheio no 1º Planejamento | Blefes por partida (bem-sucedidos) | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n4_iniciante_base | 2000 | 0 | 21,8 | 1,9 | 1,4% | 0,0% | 0,0% | 0,177 | 10,7 | 7,3 | 58,6% | 1,93 (23,5%) | 34,9 / 38,4 / 42,1 |
| n4_iniciante_fichas_3 | 2000 | 0 | 21,8 | 1,9 | 1,5% | 0,0% | 0,0% | 0,174 | 8,7 | 5,6 | 58,6% | 1,93 (23,5%) | 34,9 / 38,4 / 42,1 |
| n4_iniciante_fichas_4 | 2000 | 0 | 21,8 | 1,9 | 1,4% | 0,0% | 0,0% | 0,175 | 9,7 | 6,4 | 58,6% | 1,93 (23,5%) | 34,9 / 38,4 / 42,1 |
| n4_iniciante_fichas_6 | 2000 | 0 | 21,8 | 1,9 | 1,4% | 0,0% | 0,0% | 0,177 | 11,7 | 8,2 | 58,6% | 1,93 (23,5%) | 34,9 / 38,4 / 42,1 |
| n4_iniciante_fichas_7 | 2000 | 0 | 21,8 | 1,9 | 1,4% | 0,0% | 0,0% | 0,177 | 12,7 | 9,1 | 58,6% | 1,93 (23,5%) | 34,9 / 38,4 / 42,1 |
| n4_iniciante_dano_sem_cobertura_1 | 2000 | 0 | 21,9 | 1,9 | 1,7% | 0,0% | 0,0% | 0,125 | 11,5 | 8,2 | 52,2% | 2,02 (24,6%) | 34,7 / 38,2 / 41,9 |
| n4_iniciante_dano_sem_cobertura_3 | 2000 | 0 | 21,8 | 2,0 | 1,1% | 0,0% | 0,0% | 0,182 | 10,1 | 6,5 | 62,2% | 1,91 (24,4%) | 35,1 / 38,6 / 42,2 |
| n4_iniciante_dano_alerta_0 | 2000 | 0 | 21,8 | 1,9 | 1,4% | 0,0% | 0,0% | 0,196 | 11,1 | 7,7 | 60,3% | 1,92 (24,5%) | 34,9 / 38,4 / 42,1 |
| n4_iniciante_dano_alerta_2 | 2000 | 0 | 21,8 | 2,0 | 1,1% | 0,0% | 0,0% | 0,165 | 10,4 | 6,9 | 56,6% | 1,93 (23,7%) | 34,9 / 38,4 / 41,9 |
| n4_iniciante_tempos_menos_25 | 2000 | 0 | 21,8 | 1,9 | 1,4% | 0,0% | 0,0% | 0,177 | 10,7 | 7,3 | 58,6% | 1,93 (23,5%) | 26,3 / 28,9 / 31,7 |
| n4_iniciante_tempos_mais_25 | 2000 | 0 | 21,8 | 1,9 | 1,4% | 0,0% | 0,0% | 0,177 | 10,7 | 7,3 | 58,6% | 1,93 (23,5%) | 43,7 / 48,1 / 52,7 |
| n5_iniciante_base | 2000 | 0 | 28,1 | 2,4 | 1,8% | 5,3% | 0,0% | 0,181 | 11,2 | 7,4 | 58,5% | 2,14 (22,3%) | 40,6 / 44,2 / 48,2 |
| n5_iniciante_fichas_3 | 2000 | 0 | 28,1 | 2,4 | 1,8% | 5,3% | 0,0% | 0,179 | 9,2 | 5,7 | 58,5% | 2,14 (22,3%) | 40,6 / 44,2 / 48,2 |
| n5_iniciante_fichas_4 | 2000 | 0 | 28,1 | 2,4 | 1,8% | 5,3% | 0,0% | 0,180 | 10,2 | 6,5 | 58,5% | 2,14 (22,3%) | 40,6 / 44,2 / 48,2 |
| n5_iniciante_fichas_6 | 2000 | 0 | 28,1 | 2,4 | 1,8% | 5,3% | 0,0% | 0,182 | 12,2 | 8,3 | 58,5% | 2,14 (22,3%) | 40,6 / 44,2 / 48,2 |
| n5_iniciante_fichas_7 | 2000 | 0 | 28,1 | 2,4 | 1,8% | 5,3% | 0,0% | 0,182 | 13,2 | 9,2 | 58,5% | 2,14 (22,3%) | 40,6 / 44,2 / 48,2 |
| n5_iniciante_dano_sem_cobertura_1 | 2000 | 0 | 28,3 | 2,4 | 2,1% | 6,3% | 0,0% | 0,139 | 11,9 | 8,3 | 51,9% | 2,16 (22,9%) | 40,4 / 44,1 / 47,8 |
| n5_iniciante_dano_sem_cobertura_3 | 2000 | 0 | 28,1 | 2,4 | 1,6% | 5,3% | 0,0% | 0,172 | 10,7 | 6,6 | 61,9% | 2,09 (22,0%) | 40,8 / 44,5 / 48,3 |
| n5_iniciante_dano_alerta_0 | 2000 | 0 | 28,1 | 2,4 | 2,1% | 5,9% | 0,0% | 0,207 | 11,7 | 7,9 | 59,6% | 2,12 (22,7%) | 40,7 / 44,3 / 48,1 |
| n5_iniciante_dano_alerta_2 | 2000 | 0 | 28,2 | 2,4 | 1,8% | 5,4% | 0,0% | 0,171 | 11,0 | 7,0 | 57,1% | 2,14 (22,3%) | 40,7 / 44,3 / 48,2 |
| n5_iniciante_tempos_menos_25 | 2000 | 0 | 28,1 | 2,4 | 1,8% | 5,3% | 0,0% | 0,181 | 11,2 | 7,4 | 58,5% | 2,14 (22,3%) | 30,6 / 33,4 / 36,4 |
| n5_iniciante_tempos_mais_25 | 2000 | 0 | 28,1 | 2,4 | 1,8% | 5,3% | 0,0% | 0,181 | 11,2 | 7,4 | 58,5% | 2,14 (22,3%) | 50,8 / 55,4 / 60,4 |
| n4_experiente_base | 2000 | 0 | 22,0 | 3,2 | 2,5% | 0,0% | 0,0% | 0,206 | 12,2 | 8,5 | 51,0% | 2,12 (41,0%) | 34,9 / 38,7 / 42,4 |
| n4_experiente_fichas_3 | 2000 | 0 | 22,0 | 3,2 | 2,5% | 0,0% | 0,0% | 0,204 | 10,2 | 6,8 | 51,0% | 2,12 (41,0%) | 34,9 / 38,7 / 42,4 |
| n4_experiente_fichas_4 | 2000 | 0 | 22,0 | 3,2 | 2,5% | 0,0% | 0,0% | 0,206 | 11,2 | 7,6 | 51,0% | 2,12 (41,0%) | 34,9 / 38,7 / 42,4 |
| n4_experiente_fichas_6 | 2000 | 0 | 22,0 | 3,2 | 2,5% | 0,0% | 0,0% | 0,206 | 13,2 | 9,4 | 51,0% | 2,12 (41,0%) | 34,9 / 38,7 / 42,4 |
| n4_experiente_fichas_7 | 2000 | 0 | 22,0 | 3,2 | 2,5% | 0,0% | 0,0% | 0,206 | 14,2 | 10,4 | 51,0% | 2,12 (41,0%) | 34,9 / 38,7 / 42,4 |
| n4_experiente_dano_sem_cobertura_1 | 2000 | 0 | 22,1 | 3,2 | 2,4% | 0,0% | 0,0% | 0,164 | 12,7 | 9,3 | 50,1% | 2,10 (39,3%) | 35,0 / 38,6 / 42,6 |
| n4_experiente_dano_sem_cobertura_3 | 2000 | 0 | 22,1 | 3,3 | 1,5% | 0,0% | 0,0% | 0,207 | 11,7 | 7,8 | 52,4% | 2,08 (40,9%) | 35,2 / 38,8 / 42,7 |
| n4_experiente_dano_alerta_0 | 2000 | 0 | 21,9 | 3,2 | 2,9% | 0,0% | 0,0% | 0,164 | 12,2 | 8,8 | 53,1% | 2,06 (40,0%) | 34,9 / 38,7 / 42,3 |
| n4_experiente_dano_alerta_2 | 2000 | 0 | 22,0 | 3,3 | 2,9% | 0,0% | 0,0% | 0,194 | 11,9 | 8,2 | 49,4% | 2,11 (40,5%) | 34,9 / 38,7 / 42,5 |
| n4_experiente_tempos_menos_25 | 2000 | 0 | 22,0 | 3,2 | 2,5% | 0,0% | 0,0% | 0,206 | 12,2 | 8,5 | 51,0% | 2,12 (41,0%) | 26,3 / 29,1 / 31,9 |
| n4_experiente_tempos_mais_25 | 2000 | 0 | 22,0 | 3,2 | 2,5% | 0,0% | 0,0% | 0,206 | 12,2 | 8,5 | 51,0% | 2,12 (41,0%) | 43,7 / 48,4 / 53,1 |
| n5_experiente_base | 2000 | 0 | 28,3 | 3,9 | 2,6% | 8,1% | 0,0% | 0,189 | 12,5 | 8,5 | 51,8% | 2,29 (38,5%) | 40,8 / 44,5 / 48,5 |
| n5_experiente_fichas_3 | 2000 | 0 | 28,3 | 3,9 | 2,7% | 8,1% | 0,0% | 0,188 | 10,5 | 6,8 | 51,8% | 2,29 (38,5%) | 40,8 / 44,5 / 48,5 |
| n5_experiente_fichas_4 | 2000 | 0 | 28,3 | 3,9 | 2,6% | 8,1% | 0,0% | 0,189 | 11,5 | 7,6 | 51,8% | 2,29 (38,5%) | 40,8 / 44,5 / 48,5 |
| n5_experiente_fichas_6 | 2000 | 0 | 28,3 | 3,9 | 2,6% | 8,1% | 0,0% | 0,189 | 13,5 | 9,5 | 51,8% | 2,29 (38,5%) | 40,8 / 44,5 / 48,5 |
| n5_experiente_fichas_7 | 2000 | 0 | 28,3 | 3,9 | 2,6% | 8,1% | 0,0% | 0,189 | 14,5 | 10,4 | 51,8% | 2,29 (38,5%) | 40,8 / 44,5 / 48,5 |
| n5_experiente_dano_sem_cobertura_1 | 2000 | 0 | 28,3 | 3,8 | 2,4% | 9,9% | 0,0% | 0,136 | 13,0 | 9,4 | 49,6% | 2,30 (37,8%) | 40,4 / 44,4 / 48,4 |
| n5_experiente_dano_sem_cobertura_3 | 2000 | 0 | 28,2 | 4,1 | 2,3% | 7,8% | 0,0% | 0,198 | 12,2 | 7,8 | 52,9% | 2,28 (37,8%) | 40,8 / 44,6 / 48,6 |
| n5_experiente_dano_alerta_0 | 2000 | 0 | 28,3 | 3,8 | 2,9% | 9,7% | 0,0% | 0,204 | 12,7 | 8,9 | 53,1% | 2,30 (38,9%) | 40,6 / 44,5 / 48,6 |
| n5_experiente_dano_alerta_2 | 2000 | 0 | 28,3 | 3,9 | 2,8% | 7,0% | 0,0% | 0,191 | 12,3 | 8,2 | 50,7% | 2,32 (39,2%) | 40,7 / 44,5 / 48,5 |
| n5_experiente_tempos_menos_25 | 2000 | 0 | 28,3 | 3,9 | 2,6% | 8,1% | 0,0% | 0,189 | 12,5 | 8,5 | 51,8% | 2,29 (38,5%) | 30,7 / 33,5 / 36,6 |
| n5_experiente_tempos_mais_25 | 2000 | 0 | 28,3 | 3,9 | 2,6% | 8,1% | 0,0% | 0,189 | 12,5 | 8,5 | 51,8% | 2,29 (38,5%) | 51,0 / 55,7 / 60,7 |

## Equilíbrio dentro da partida (descrição)

Números sem critério de aceite; os vereditos, quando pedidos, estão na seção de requisitos. Razão de testes: máximo sobre a média de testes recebidos na partida (REQ-06a). Contra o menor: fração dos testes contra quem tinha o menor placar (REQ-06b). Zeradas: partidas com alguém em 0 ficha antes do último ciclo (REQ-07). Parado: percentil 90 do tempo parado por jogador e ciclo, pelos tempos provisórios do MOD-05 (REQ-10). Peso do dano: dano de incidente sobre as fichas movimentadas (REQ-13). Dispersão: placar do primeiro menos o do último no fim (REQ-14).

| Cenário | Razão de testes | Contra o menor | Zeradas | Parado p90 (min) | Peso do dano | Dispersão |
|---|---|---|---|---|---|---|
| n4_iniciante_base | 1,35 | 0,420 | 6,0% | 5,8 | 0,216 | 6,7 |
| n4_iniciante_fichas_3 | 1,35 | 0,421 | 45,9% | 5,8 | 0,216 | 5,7 |
| n4_iniciante_fichas_4 | 1,35 | 0,420 | 17,4% | 5,8 | 0,216 | 6,3 |
| n4_iniciante_fichas_6 | 1,35 | 0,420 | 1,8% | 5,8 | 0,215 | 7,0 |
| n4_iniciante_fichas_7 | 1,35 | 0,420 | 0,4% | 5,8 | 0,215 | 7,2 |
| n4_iniciante_dano_sem_cobertura_1 | 1,37 | 0,438 | 0,5% | 5,8 | 0,156 | 6,5 |
| n4_iniciante_dano_sem_cobertura_3 | 1,36 | 0,409 | 26,8% | 5,8 | 0,266 | 6,8 |
| n4_iniciante_dano_alerta_0 | 1,35 | 0,422 | 3,2% | 5,8 | 0,187 | 6,7 |
| n4_iniciante_dano_alerta_2 | 1,36 | 0,419 | 12,7% | 5,8 | 0,243 | 6,7 |
| n4_iniciante_tempos_menos_25 | 1,35 | 0,420 | 6,0% | 4,3 | 0,216 | 6,7 |
| n4_iniciante_tempos_mais_25 | 1,35 | 0,420 | 6,0% | 7,2 | 0,216 | 6,7 |
| n5_iniciante_base | 1,41 | 0,337 | 8,2% | 9,0 | 0,214 | 7,6 |
| n5_iniciante_fichas_3 | 1,41 | 0,339 | 52,1% | 9,0 | 0,214 | 6,5 |
| n5_iniciante_fichas_4 | 1,41 | 0,337 | 22,7% | 9,0 | 0,215 | 7,1 |
| n5_iniciante_fichas_6 | 1,41 | 0,337 | 2,2% | 9,0 | 0,214 | 7,9 |
| n5_iniciante_fichas_7 | 1,41 | 0,337 | 0,5% | 9,0 | 0,213 | 8,1 |
| n5_iniciante_dano_sem_cobertura_1 | 1,40 | 0,362 | 0,6% | 8,9 | 0,155 | 7,2 |
| n5_iniciante_dano_sem_cobertura_3 | 1,41 | 0,331 | 31,8% | 9,2 | 0,265 | 7,6 |
| n5_iniciante_dano_alerta_0 | 1,40 | 0,342 | 4,2% | 9,2 | 0,184 | 7,6 |
| n5_iniciante_dano_alerta_2 | 1,40 | 0,334 | 16,8% | 9,0 | 0,242 | 7,6 |
| n5_iniciante_tempos_menos_25 | 1,41 | 0,337 | 8,2% | 6,8 | 0,214 | 7,6 |
| n5_iniciante_tempos_mais_25 | 1,41 | 0,337 | 8,2% | 11,3 | 0,214 | 7,6 |
| n4_experiente_base | 1,38 | 0,424 | 4,2% | 5,8 | 0,172 | 7,3 |
| n4_experiente_fichas_3 | 1,38 | 0,425 | 33,9% | 5,8 | 0,172 | 6,4 |
| n4_experiente_fichas_4 | 1,38 | 0,424 | 13,2% | 5,8 | 0,172 | 6,9 |
| n4_experiente_fichas_6 | 1,38 | 0,424 | 1,0% | 5,8 | 0,172 | 7,5 |
| n4_experiente_fichas_7 | 1,38 | 0,424 | 0,3% | 5,8 | 0,172 | 7,6 |
| n4_experiente_dano_sem_cobertura_1 | 1,36 | 0,438 | 0,5% | 5,8 | 0,125 | 6,7 |
| n4_experiente_dano_sem_cobertura_3 | 1,37 | 0,415 | 19,1% | 5,8 | 0,216 | 7,5 |
| n4_experiente_dano_alerta_0 | 1,38 | 0,422 | 2,1% | 5,8 | 0,154 | 7,0 |
| n4_experiente_dano_alerta_2 | 1,38 | 0,422 | 10,2% | 5,8 | 0,192 | 7,3 |
| n4_experiente_tempos_menos_25 | 1,38 | 0,424 | 4,2% | 4,3 | 0,172 | 7,3 |
| n4_experiente_tempos_mais_25 | 1,38 | 0,424 | 4,2% | 7,2 | 0,172 | 7,3 |
| n5_experiente_base | 1,43 | 0,346 | 5,0% | 9,2 | 0,175 | 8,0 |
| n5_experiente_fichas_3 | 1,43 | 0,348 | 39,9% | 9,2 | 0,175 | 7,1 |
| n5_experiente_fichas_4 | 1,43 | 0,346 | 15,5% | 9,2 | 0,175 | 7,6 |
| n5_experiente_fichas_6 | 1,43 | 0,346 | 1,6% | 9,2 | 0,174 | 8,2 |
| n5_experiente_fichas_7 | 1,43 | 0,346 | 0,3% | 9,2 | 0,174 | 8,4 |
| n5_experiente_dano_sem_cobertura_1 | 1,43 | 0,357 | 0,6% | 9,0 | 0,125 | 7,4 |
| n5_experiente_dano_sem_cobertura_3 | 1,42 | 0,332 | 24,5% | 9,2 | 0,219 | 8,4 |
| n5_experiente_dano_alerta_0 | 1,43 | 0,343 | 2,6% | 9,2 | 0,155 | 7,8 |
| n5_experiente_dano_alerta_2 | 1,43 | 0,341 | 12,7% | 9,1 | 0,195 | 8,1 |
| n5_experiente_tempos_menos_25 | 1,43 | 0,346 | 5,0% | 6,9 | 0,175 | 8,0 |
| n5_experiente_tempos_mais_25 | 1,43 | 0,346 | 5,0% | 11,5 | 0,175 | 8,0 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| n4_iniciante_base | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_iniciante_fichas_3 | v2.2.1 com {'fichas.iniciais': 3} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:6d2fdb63621d` |
| n4_iniciante_fichas_4 | v2.2.1 com {'fichas.iniciais': 4} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:f0862f1f0307` |
| n4_iniciante_fichas_6 | v2.2.1 com {'fichas.iniciais': 6} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:30ca332f7f8c` |
| n4_iniciante_fichas_7 | v2.2.1 com {'fichas.iniciais': 7} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:df8924061648` |
| n4_iniciante_dano_sem_cobertura_1 | v2.2.1 com {'dano.incidente.sem_cobertura': 1} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:7a73914a61cc` |
| n4_iniciante_dano_sem_cobertura_3 | v2.2.1 com {'dano.incidente.sem_cobertura': 3} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:61b09722477f` |
| n4_iniciante_dano_alerta_0 | v2.2.1 com {'dano.incidente.alerta': 0} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:d27bb5392847` |
| n4_iniciante_dano_alerta_2 | v2.2.1 com {'dano.incidente.alerta': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:de4613fed1a8` |
| n4_iniciante_tempos_menos_25 | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_iniciante_tempos_mais_25 | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_iniciante_base | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_iniciante_fichas_3 | v2.2.1 com {'fichas.iniciais': 3} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:6d2fdb63621d` |
| n5_iniciante_fichas_4 | v2.2.1 com {'fichas.iniciais': 4} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:f0862f1f0307` |
| n5_iniciante_fichas_6 | v2.2.1 com {'fichas.iniciais': 6} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:30ca332f7f8c` |
| n5_iniciante_fichas_7 | v2.2.1 com {'fichas.iniciais': 7} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:df8924061648` |
| n5_iniciante_dano_sem_cobertura_1 | v2.2.1 com {'dano.incidente.sem_cobertura': 1} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:7a73914a61cc` |
| n5_iniciante_dano_sem_cobertura_3 | v2.2.1 com {'dano.incidente.sem_cobertura': 3} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:61b09722477f` |
| n5_iniciante_dano_alerta_0 | v2.2.1 com {'dano.incidente.alerta': 0} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:d27bb5392847` |
| n5_iniciante_dano_alerta_2 | v2.2.1 com {'dano.incidente.alerta': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:de4613fed1a8` |
| n5_iniciante_tempos_menos_25 | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_iniciante_tempos_mais_25 | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_experiente_base | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_experiente_fichas_3 | v2.2.1 com {'fichas.iniciais': 3} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:6d2fdb63621d` |
| n4_experiente_fichas_4 | v2.2.1 com {'fichas.iniciais': 4} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:f0862f1f0307` |
| n4_experiente_fichas_6 | v2.2.1 com {'fichas.iniciais': 6} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:30ca332f7f8c` |
| n4_experiente_fichas_7 | v2.2.1 com {'fichas.iniciais': 7} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:df8924061648` |
| n4_experiente_dano_sem_cobertura_1 | v2.2.1 com {'dano.incidente.sem_cobertura': 1} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:7a73914a61cc` |
| n4_experiente_dano_sem_cobertura_3 | v2.2.1 com {'dano.incidente.sem_cobertura': 3} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:61b09722477f` |
| n4_experiente_dano_alerta_0 | v2.2.1 com {'dano.incidente.alerta': 0} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:d27bb5392847` |
| n4_experiente_dano_alerta_2 | v2.2.1 com {'dano.incidente.alerta': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:de4613fed1a8` |
| n4_experiente_tempos_menos_25 | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_experiente_tempos_mais_25 | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_experiente_base | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_experiente_fichas_3 | v2.2.1 com {'fichas.iniciais': 3} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:6d2fdb63621d` |
| n5_experiente_fichas_4 | v2.2.1 com {'fichas.iniciais': 4} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:f0862f1f0307` |
| n5_experiente_fichas_6 | v2.2.1 com {'fichas.iniciais': 6} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:30ca332f7f8c` |
| n5_experiente_fichas_7 | v2.2.1 com {'fichas.iniciais': 7} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:df8924061648` |
| n5_experiente_dano_sem_cobertura_1 | v2.2.1 com {'dano.incidente.sem_cobertura': 1} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:7a73914a61cc` |
| n5_experiente_dano_sem_cobertura_3 | v2.2.1 com {'dano.incidente.sem_cobertura': 3} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:61b09722477f` |
| n5_experiente_dano_alerta_0 | v2.2.1 com {'dano.incidente.alerta': 0} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:d27bb5392847` |
| n5_experiente_dano_alerta_2 | v2.2.1 com {'dano.incidente.alerta': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:de4613fed1a8` |
| n5_experiente_tempos_menos_25 | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_experiente_tempos_mais_25 | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |

## Como refazer

No commit `73762b5`: `cf experimento experimentos/fase4_exp4_sensibilidade.yaml --oficial --processos 4`. O resultado não depende do número de processos.

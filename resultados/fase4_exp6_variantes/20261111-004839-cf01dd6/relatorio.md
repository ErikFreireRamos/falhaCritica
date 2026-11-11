# Relatório do experimento `fase4_exp6_variantes`

Variantes do playtest, uma de cada vez a partir da v2.2.1, com Heurísticos de conhecimento iniciante e experiente e mesas de 4 e de 5: duração, distribuição de ataques, fichas, tempo parado, os dois estilos, o primeiro incidente e o peso dos incidentes.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase4_exp6_variantes.yaml` |
| Commit | `cf01dd6` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261116 |
| Partidas | 80000 |
| Falhas | 0 |
| Registros completos gravados | 80 |
| Início | 2026-11-11T00:48:39+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-06: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | (a) média da razão máximo/média de testes recebidos | 1,360 | 1,352 a 1,368 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_base | (b) fração dos testes contra quem tinha o menor placar | 0,417 | 0,413 a 0,422 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var01_sem_punicao | (a) média da razão máximo/média de testes recebidos | 1,360 | 1,351 a 1,368 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var01_sem_punicao | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,416 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var01_2_fichas | (a) média da razão máximo/média de testes recebidos | 1,360 | 1,352 a 1,368 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var01_2_fichas | (b) fração dos testes contra quem tinha o menor placar | 0,415 | 0,410 a 0,419 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var02_custo_extra | (a) média da razão máximo/média de testes recebidos | 1,360 | 1,351 a 1,368 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var02_custo_extra | (b) fração dos testes contra quem tinha o menor placar | 0,405 | 0,401 a 0,409 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var03_auditor_externo | (a) média da razão máximo/média de testes recebidos | 1,354 | 1,347 a 1,363 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var03_auditor_externo | (b) fração dos testes contra quem tinha o menor placar | 0,415 | 0,411 a 0,420 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var04_vizinho | (a) média da razão máximo/média de testes recebidos | 1,492 | 1,481 a 1,504 | 0,000 a 1,500 | 2000 | inconclusivo |
| n4_iniciante_var04_vizinho | (b) fração dos testes contra quem tinha o menor placar | 0,433 | 0,427 a 0,438 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_iniciante_var05_limite_2 | (a) média da razão máximo/média de testes recebidos | 1,157 | 1,151 a 1,162 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var05_limite_2 | (b) fração dos testes contra quem tinha o menor placar | 0,436 | 0,432 a 0,440 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_iniciante_var06_palpite | (a) média da razão máximo/média de testes recebidos | 1,360 | 1,351 a 1,367 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var06_palpite | (b) fração dos testes contra quem tinha o menor placar | 0,417 | 0,413 a 0,422 | 0,000 a 0,433 | 2000 | passa |
| n4_iniciante_var07_2_compras | (a) média da razão máximo/média de testes recebidos | 1,542 | 1,529 a 1,555 | 0,000 a 1,500 | 2000 | falha |
| n4_iniciante_var07_2_compras | (b) fração dos testes contra quem tinha o menor placar | 0,437 | 0,430 a 0,443 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_iniciante_var09_modulo | (a) média da razão máximo/média de testes recebidos | 1,364 | 1,356 a 1,373 | 0,000 a 1,500 | 2000 | passa |
| n4_iniciante_var09_modulo | (b) fração dos testes contra quem tinha o menor placar | 0,419 | 0,415 a 0,423 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_base | (a) média da razão máximo/média de testes recebidos | 1,375 | 1,367 a 1,384 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_base | (b) fração dos testes contra quem tinha o menor placar | 0,421 | 0,417 a 0,426 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_var01_sem_punicao | (a) média da razão máximo/média de testes recebidos | 1,375 | 1,367 a 1,384 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var01_sem_punicao | (b) fração dos testes contra quem tinha o menor placar | 0,424 | 0,419 a 0,428 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_var01_2_fichas | (a) média da razão máximo/média de testes recebidos | 1,375 | 1,367 a 1,384 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var01_2_fichas | (b) fração dos testes contra quem tinha o menor placar | 0,418 | 0,413 a 0,422 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_var02_custo_extra | (a) média da razão máximo/média de testes recebidos | 1,375 | 1,366 a 1,384 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var02_custo_extra | (b) fração dos testes contra quem tinha o menor placar | 0,415 | 0,410 a 0,419 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_var03_auditor_externo | (a) média da razão máximo/média de testes recebidos | 1,371 | 1,363 a 1,379 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var03_auditor_externo | (b) fração dos testes contra quem tinha o menor placar | 0,422 | 0,417 a 0,426 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_var04_vizinho | (a) média da razão máximo/média de testes recebidos | 1,494 | 1,482 a 1,505 | 0,000 a 1,500 | 2000 | inconclusivo |
| n4_experiente_var04_vizinho | (b) fração dos testes contra quem tinha o menor placar | 0,431 | 0,424 a 0,437 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_experiente_var05_limite_2 | (a) média da razão máximo/média de testes recebidos | 1,172 | 1,166 a 1,177 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var05_limite_2 | (b) fração dos testes contra quem tinha o menor placar | 0,445 | 0,442 a 0,449 | 0,000 a 0,433 | 2000 | falha |
| n4_experiente_var06_palpite | (a) média da razão máximo/média de testes recebidos | 1,375 | 1,367 a 1,383 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var06_palpite | (b) fração dos testes contra quem tinha o menor placar | 0,420 | 0,415 a 0,424 | 0,000 a 0,433 | 2000 | passa |
| n4_experiente_var07_2_compras | (a) média da razão máximo/média de testes recebidos | 1,558 | 1,545 a 1,571 | 0,000 a 1,500 | 2000 | falha |
| n4_experiente_var07_2_compras | (b) fração dos testes contra quem tinha o menor placar | 0,438 | 0,432 a 0,445 | 0,000 a 0,433 | 2000 | inconclusivo |
| n4_experiente_var09_modulo | (a) média da razão máximo/média de testes recebidos | 1,366 | 1,358 a 1,373 | 0,000 a 1,500 | 2000 | passa |
| n4_experiente_var09_modulo | (b) fração dos testes contra quem tinha o menor placar | 0,426 | 0,422 a 0,430 | 0,000 a 0,433 | 2000 | passa |
| n5_iniciante_base | (a) média da razão máximo/média de testes recebidos | 1,401 | 1,393 a 1,409 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_base | (b) fração dos testes contra quem tinha o menor placar | 0,340 | 0,337 a 0,344 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var01_sem_punicao | (a) média da razão máximo/média de testes recebidos | 1,401 | 1,392 a 1,409 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_var01_sem_punicao | (b) fração dos testes contra quem tinha o menor placar | 0,342 | 0,338 a 0,346 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var01_2_fichas | (a) média da razão máximo/média de testes recebidos | 1,401 | 1,392 a 1,409 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_var01_2_fichas | (b) fração dos testes contra quem tinha o menor placar | 0,338 | 0,335 a 0,342 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var02_custo_extra | (a) média da razão máximo/média de testes recebidos | 1,401 | 1,393 a 1,409 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_var02_custo_extra | (b) fração dos testes contra quem tinha o menor placar | 0,326 | 0,322 a 0,329 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var03_auditor_externo | (a) média da razão máximo/média de testes recebidos | 1,398 | 1,390 a 1,406 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_var03_auditor_externo | (b) fração dos testes contra quem tinha o menor placar | 0,342 | 0,338 a 0,346 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var04_vizinho | (a) média da razão máximo/média de testes recebidos | 1,552 | 1,541 a 1,564 | 0,000 a 1,500 | 2000 | falha |
| n5_iniciante_var04_vizinho | (b) fração dos testes contra quem tinha o menor placar | 0,349 | 0,345 a 0,354 | 0,000 a 0,350 | 2000 | inconclusivo |
| n5_iniciante_var05_limite_2 | (a) média da razão máximo/média de testes recebidos | 1,175 | 1,169 a 1,179 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_var05_limite_2 | (b) fração dos testes contra quem tinha o menor placar | 0,360 | 0,357 a 0,363 | 0,000 a 0,350 | 2000 | falha |
| n5_iniciante_var06_palpite | (a) média da razão máximo/média de testes recebidos | 1,401 | 1,393 a 1,409 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_var06_palpite | (b) fração dos testes contra quem tinha o menor placar | 0,339 | 0,334 a 0,343 | 0,000 a 0,350 | 2000 | passa |
| n5_iniciante_var07_2_compras | (a) média da razão máximo/média de testes recebidos | 1,612 | 1,599 a 1,625 | 0,000 a 1,500 | 2000 | falha |
| n5_iniciante_var07_2_compras | (b) fração dos testes contra quem tinha o menor placar | 0,359 | 0,354 a 0,365 | 0,000 a 0,350 | 2000 | falha |
| n5_iniciante_var09_modulo | (a) média da razão máximo/média de testes recebidos | 1,404 | 1,396 a 1,413 | 0,000 a 1,500 | 2000 | passa |
| n5_iniciante_var09_modulo | (b) fração dos testes contra quem tinha o menor placar | 0,343 | 0,339 a 0,347 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_base | (a) média da razão máximo/média de testes recebidos | 1,424 | 1,416 a 1,433 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_base | (b) fração dos testes contra quem tinha o menor placar | 0,347 | 0,343 a 0,351 | 0,000 a 0,350 | 2000 | inconclusivo |
| n5_experiente_var01_sem_punicao | (a) média da razão máximo/média de testes recebidos | 1,424 | 1,415 a 1,432 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_var01_sem_punicao | (b) fração dos testes contra quem tinha o menor placar | 0,348 | 0,344 a 0,353 | 0,000 a 0,350 | 2000 | inconclusivo |
| n5_experiente_var01_2_fichas | (a) média da razão máximo/média de testes recebidos | 1,425 | 1,416 a 1,433 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_var01_2_fichas | (b) fração dos testes contra quem tinha o menor placar | 0,344 | 0,340 a 0,348 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_var02_custo_extra | (a) média da razão máximo/média de testes recebidos | 1,424 | 1,416 a 1,432 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_var02_custo_extra | (b) fração dos testes contra quem tinha o menor placar | 0,340 | 0,337 a 0,344 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_var03_auditor_externo | (a) média da razão máximo/média de testes recebidos | 1,423 | 1,415 a 1,432 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_var03_auditor_externo | (b) fração dos testes contra quem tinha o menor placar | 0,344 | 0,340 a 0,347 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_var04_vizinho | (a) média da razão máximo/média de testes recebidos | 1,552 | 1,542 a 1,565 | 0,000 a 1,500 | 2000 | falha |
| n5_experiente_var04_vizinho | (b) fração dos testes contra quem tinha o menor placar | 0,348 | 0,343 a 0,352 | 0,000 a 0,350 | 2000 | inconclusivo |
| n5_experiente_var05_limite_2 | (a) média da razão máximo/média de testes recebidos | 1,196 | 1,191 a 1,201 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_var05_limite_2 | (b) fração dos testes contra quem tinha o menor placar | 0,365 | 0,362 a 0,368 | 0,000 a 0,350 | 2000 | falha |
| n5_experiente_var06_palpite | (a) média da razão máximo/média de testes recebidos | 1,424 | 1,415 a 1,432 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_var06_palpite | (b) fração dos testes contra quem tinha o menor placar | 0,344 | 0,341 a 0,348 | 0,000 a 0,350 | 2000 | passa |
| n5_experiente_var07_2_compras | (a) média da razão máximo/média de testes recebidos | 1,637 | 1,624 a 1,651 | 0,000 a 1,500 | 2000 | falha |
| n5_experiente_var07_2_compras | (b) fração dos testes contra quem tinha o menor placar | 0,362 | 0,357 a 0,367 | 0,000 a 0,350 | 2000 | falha |
| n5_experiente_var09_modulo | (a) média da razão máximo/média de testes recebidos | 1,426 | 1,417 a 1,434 | 0,000 a 1,500 | 2000 | passa |
| n5_experiente_var09_modulo | (b) fração dos testes contra quem tinha o menor placar | 0,345 | 0,341 a 0,350 | 0,000 a 0,350 | 2000 | passa |

Nota: (b): empate no menor placar conta como teste contra o menor.

### REQ-07: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | partidas com alguém em 0 ficha antes do último ciclo | 0,073 | 0,063 a 0,086 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var01_sem_punicao | partidas com alguém em 0 ficha antes do último ciclo | 0,066 | 0,055 a 0,077 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var01_2_fichas | partidas com alguém em 0 ficha antes do último ciclo | 0,091 | 0,079 a 0,104 | 0,000 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_var02_custo_extra | partidas com alguém em 0 ficha antes do último ciclo | 0,195 | 0,178 a 0,212 | 0,000 a 0,100 | 2000 | falha |
| n4_iniciante_var03_auditor_externo | partidas com alguém em 0 ficha antes do último ciclo | 0,060 | 0,050 a 0,071 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var04_vizinho | partidas com alguém em 0 ficha antes do último ciclo | 0,079 | 0,068 a 0,092 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var05_limite_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,081 | 0,069 a 0,093 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var06_palpite | partidas com alguém em 0 ficha antes do último ciclo | 0,070 | 0,059 a 0,081 | 0,000 a 0,100 | 2000 | passa |
| n4_iniciante_var07_2_compras | partidas com alguém em 0 ficha antes do último ciclo | 0,100 | 0,087 a 0,113 | 0,000 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_var09_modulo | partidas com alguém em 0 ficha antes do último ciclo | 0,074 | 0,063 a 0,086 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_base | partidas com alguém em 0 ficha antes do último ciclo | 0,032 | 0,025 a 0,040 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var01_sem_punicao | partidas com alguém em 0 ficha antes do último ciclo | 0,029 | 0,023 a 0,038 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var01_2_fichas | partidas com alguém em 0 ficha antes do último ciclo | 0,061 | 0,051 a 0,072 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var02_custo_extra | partidas com alguém em 0 ficha antes do último ciclo | 0,052 | 0,043 a 0,063 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var03_auditor_externo | partidas com alguém em 0 ficha antes do último ciclo | 0,038 | 0,030 a 0,047 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var04_vizinho | partidas com alguém em 0 ficha antes do último ciclo | 0,033 | 0,026 a 0,041 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var05_limite_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,031 | 0,024 a 0,040 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var06_palpite | partidas com alguém em 0 ficha antes do último ciclo | 0,029 | 0,023 a 0,038 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var07_2_compras | partidas com alguém em 0 ficha antes do último ciclo | 0,041 | 0,033 a 0,050 | 0,000 a 0,100 | 2000 | passa |
| n4_experiente_var09_modulo | partidas com alguém em 0 ficha antes do último ciclo | 0,048 | 0,039 a 0,058 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_base | partidas com alguém em 0 ficha antes do último ciclo | 0,069 | 0,058 a 0,080 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var01_sem_punicao | partidas com alguém em 0 ficha antes do último ciclo | 0,063 | 0,053 a 0,075 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var01_2_fichas | partidas com alguém em 0 ficha antes do último ciclo | 0,091 | 0,080 a 0,105 | 0,000 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_var02_custo_extra | partidas com alguém em 0 ficha antes do último ciclo | 0,211 | 0,194 a 0,230 | 0,000 a 0,100 | 2000 | falha |
| n5_iniciante_var03_auditor_externo | partidas com alguém em 0 ficha antes do último ciclo | 0,081 | 0,069 a 0,093 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var04_vizinho | partidas com alguém em 0 ficha antes do último ciclo | 0,089 | 0,077 a 0,102 | 0,000 a 0,100 | 2000 | inconclusivo |
| n5_iniciante_var05_limite_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,085 | 0,074 a 0,098 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var06_palpite | partidas com alguém em 0 ficha antes do último ciclo | 0,063 | 0,053 a 0,075 | 0,000 a 0,100 | 2000 | passa |
| n5_iniciante_var07_2_compras | partidas com alguém em 0 ficha antes do último ciclo | 0,117 | 0,104 a 0,132 | 0,000 a 0,100 | 2000 | falha |
| n5_iniciante_var09_modulo | partidas com alguém em 0 ficha antes do último ciclo | 0,090 | 0,078 a 0,103 | 0,000 a 0,100 | 2000 | inconclusivo |
| n5_experiente_base | partidas com alguém em 0 ficha antes do último ciclo | 0,058 | 0,049 a 0,069 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var01_sem_punicao | partidas com alguém em 0 ficha antes do último ciclo | 0,052 | 0,043 a 0,063 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var01_2_fichas | partidas com alguém em 0 ficha antes do último ciclo | 0,080 | 0,069 a 0,093 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var02_custo_extra | partidas com alguém em 0 ficha antes do último ciclo | 0,091 | 0,080 a 0,105 | 0,000 a 0,100 | 2000 | inconclusivo |
| n5_experiente_var03_auditor_externo | partidas com alguém em 0 ficha antes do último ciclo | 0,057 | 0,048 a 0,068 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var04_vizinho | partidas com alguém em 0 ficha antes do último ciclo | 0,047 | 0,039 a 0,057 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var05_limite_2 | partidas com alguém em 0 ficha antes do último ciclo | 0,051 | 0,043 a 0,062 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var06_palpite | partidas com alguém em 0 ficha antes do último ciclo | 0,051 | 0,043 a 0,062 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var07_2_compras | partidas com alguém em 0 ficha antes do último ciclo | 0,038 | 0,030 a 0,047 | 0,000 a 0,100 | 2000 | passa |
| n5_experiente_var09_modulo | partidas com alguém em 0 ficha antes do último ciclo | 0,054 | 0,045 a 0,065 | 0,000 a 0,100 | 2000 | passa |

### REQ-08: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var01_sem_punicao | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var01_2_fichas | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var02_custo_extra | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var03_auditor_externo | mediana da duração estimada (min) | 38,5 | 38,3 a 38,7 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var04_vizinho | mediana da duração estimada (min) | 34,6 | 34,4 a 34,7 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var05_limite_2 | mediana da duração estimada (min) | 34,0 | 33,9 a 34,2 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var06_palpite | mediana da duração estimada (min) | 38,4 | 38,2 a 38,6 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var07_2_compras | mediana da duração estimada (min) | 30,3 | 30,2 a 30,5 | 40,0 a 50,0 | 2000 | falha |
| n4_iniciante_var09_modulo | mediana da duração estimada (min) | 37,6 | 37,4 a 37,7 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_base | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var01_sem_punicao | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var01_2_fichas | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var02_custo_extra | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var03_auditor_externo | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var04_vizinho | mediana da duração estimada (min) | 34,9 | 34,8 a 35,1 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var05_limite_2 | mediana da duração estimada (min) | 34,3 | 34,2 a 34,4 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var06_palpite | mediana da duração estimada (min) | 38,7 | 38,5 a 38,8 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var07_2_compras | mediana da duração estimada (min) | 30,4 | 30,2 a 30,5 | 40,0 a 50,0 | 2000 | falha |
| n4_experiente_var09_modulo | mediana da duração estimada (min) | 37,7 | 37,5 a 37,9 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_base | mediana da duração estimada (min) | 44,2 | 44,1 a 44,5 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var01_sem_punicao | mediana da duração estimada (min) | 44,2 | 44,1 a 44,4 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var01_2_fichas | mediana da duração estimada (min) | 44,2 | 44,1 a 44,5 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var02_custo_extra | mediana da duração estimada (min) | 44,2 | 44,1 a 44,5 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var03_auditor_externo | mediana da duração estimada (min) | 44,4 | 44,2 a 44,6 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var04_vizinho | mediana da duração estimada (min) | 39,0 | 38,9 a 39,2 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_var05_limite_2 | mediana da duração estimada (min) | 38,9 | 38,8 a 39,0 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_var06_palpite | mediana da duração estimada (min) | 44,2 | 44,1 a 44,5 | 40,0 a 50,0 | 2000 | passa |
| n5_iniciante_var07_2_compras | mediana da duração estimada (min) | 34,2 | 34,2 a 34,3 | 40,0 a 50,0 | 2000 | falha |
| n5_iniciante_var09_modulo | mediana da duração estimada (min) | 43,3 | 43,2 a 43,5 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_base | mediana da duração estimada (min) | 44,6 | 44,4 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var01_sem_punicao | mediana da duração estimada (min) | 44,5 | 44,3 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var01_2_fichas | mediana da duração estimada (min) | 44,6 | 44,4 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var02_custo_extra | mediana da duração estimada (min) | 44,6 | 44,4 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var03_auditor_externo | mediana da duração estimada (min) | 44,6 | 44,5 a 44,8 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var04_vizinho | mediana da duração estimada (min) | 39,5 | 39,3 a 39,7 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_var05_limite_2 | mediana da duração estimada (min) | 39,3 | 39,2 a 39,4 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_var06_palpite | mediana da duração estimada (min) | 44,6 | 44,4 a 44,7 | 40,0 a 50,0 | 2000 | passa |
| n5_experiente_var07_2_compras | mediana da duração estimada (min) | 34,2 | 34,0 a 34,2 | 40,0 a 50,0 | 2000 | falha |
| n5_experiente_var09_modulo | mediana da duração estimada (min) | 43,5 | 43,3 a 43,8 | 40,0 a 50,0 | 2000 | passa |

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
| n4_iniciante_var01_sem_punicao | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_var01_2_fichas | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_var02_custo_extra | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_var03_auditor_externo | percentil 90 do tempo parado por jogador e ciclo (min) | 7,3 | 7,3 a 7,4 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_var04_vizinho | percentil 90 do tempo parado por jogador e ciclo (min) | 5,0 | 5,0 a 5,0 | 0,0 a 5,0 | 2000 | passa |
| n4_iniciante_var05_limite_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 4,7 | 4,7 a 4,8 | 0,0 a 5,0 | 2000 | passa |
| n4_iniciante_var06_palpite | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,8 | 0,0 a 5,0 | 2000 | falha |
| n4_iniciante_var07_2_compras | percentil 90 do tempo parado por jogador e ciclo (min) | 4,1 | 4,0 a 4,1 | 0,0 a 5,0 | 2000 | passa |
| n4_iniciante_var09_modulo | percentil 90 do tempo parado por jogador e ciclo (min) | 5,7 | 5,6 a 5,7 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_base | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var01_sem_punicao | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var01_2_fichas | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var02_custo_extra | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var03_auditor_externo | percentil 90 do tempo parado por jogador e ciclo (min) | 7,4 | 7,4 a 7,6 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var04_vizinho | percentil 90 do tempo parado por jogador e ciclo (min) | 5,0 | 5,0 a 5,1 | 0,0 a 5,0 | 2000 | inconclusivo |
| n4_experiente_var05_limite_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 4,7 | 4,7 a 4,7 | 0,0 a 5,0 | 2000 | passa |
| n4_experiente_var06_palpite | percentil 90 do tempo parado por jogador e ciclo (min) | 5,8 | 5,8 a 5,9 | 0,0 a 5,0 | 2000 | falha |
| n4_experiente_var07_2_compras | percentil 90 do tempo parado por jogador e ciclo (min) | 4,0 | 4,0 a 4,1 | 0,0 a 5,0 | 2000 | passa |
| n4_experiente_var09_modulo | percentil 90 do tempo parado por jogador e ciclo (min) | 5,6 | 5,6 a 5,7 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_base | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var01_sem_punicao | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,1 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var01_2_fichas | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,1 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var02_custo_extra | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var03_auditor_externo | percentil 90 do tempo parado por jogador e ciclo (min) | 10,2 | 10,0 a 10,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var04_vizinho | percentil 90 do tempo parado por jogador e ciclo (min) | 7,7 | 7,7 a 7,7 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var05_limite_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 7,0 | 7,0 a 7,0 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var06_palpite | percentil 90 do tempo parado por jogador e ciclo (min) | 9,0 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var07_2_compras | percentil 90 do tempo parado por jogador e ciclo (min) | 6,3 | 6,2 a 6,3 | 0,0 a 5,0 | 2000 | falha |
| n5_iniciante_var09_modulo | percentil 90 do tempo parado por jogador e ciclo (min) | 8,8 | 8,7 a 8,8 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_base | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var01_sem_punicao | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,0 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var01_2_fichas | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var02_custo_extra | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var03_auditor_externo | percentil 90 do tempo parado por jogador e ciclo (min) | 10,2 | 10,2 a 10,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var04_vizinho | percentil 90 do tempo parado por jogador e ciclo (min) | 7,9 | 7,8 a 7,9 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var05_limite_2 | percentil 90 do tempo parado por jogador e ciclo (min) | 7,2 | 7,0 a 7,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var06_palpite | percentil 90 do tempo parado por jogador e ciclo (min) | 9,2 | 9,1 a 9,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var07_2_compras | percentil 90 do tempo parado por jogador e ciclo (min) | 6,2 | 6,2 a 6,2 | 0,0 a 5,0 | 2000 | falha |
| n5_experiente_var09_modulo | percentil 90 do tempo parado por jogador e ciclo (min) | 8,8 | 8,8 a 8,9 | 0,0 a 5,0 | 2000 | falha |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-11: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,575 | 0,564 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var01_sem_punicao | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,575 | 0,565 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var01_2_fichas | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,575 | 0,564 a 0,587 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var02_custo_extra | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,575 | 0,563 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var03_auditor_externo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,575 | 0,565 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var04_vizinho | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,575 | 0,564 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var05_limite_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,575 | 0,564 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var06_palpite | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,575 | 0,564 a 0,586 | 0,100 a 0,900 | 2000 | passa |
| n4_iniciante_var07_2_compras | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,000 | 0,000 a 0,000 | 0,100 a 0,900 | 2000 | falha |
| n4_iniciante_var09_modulo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,548 | 0,537 a 0,559 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,496 a 0,517 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var01_sem_punicao | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,495 a 0,517 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var01_2_fichas | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,495 a 0,518 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var02_custo_extra | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,496 a 0,517 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var03_auditor_externo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,495 a 0,518 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var04_vizinho | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,495 a 0,518 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var05_limite_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,496 a 0,518 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var06_palpite | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,507 | 0,496 a 0,518 | 0,100 a 0,900 | 2000 | passa |
| n4_experiente_var07_2_compras | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,000 | 0,000 a 0,000 | 0,100 a 0,900 | 2000 | falha |
| n4_experiente_var09_modulo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,486 | 0,475 a 0,497 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,564 a 0,584 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var01_sem_punicao | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,565 a 0,584 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var01_2_fichas | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,564 a 0,583 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var02_custo_extra | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,566 a 0,583 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var03_auditor_externo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,565 a 0,584 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var04_vizinho | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,565 a 0,584 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var05_limite_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,564 a 0,584 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var06_palpite | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,574 | 0,565 a 0,584 | 0,100 a 0,900 | 2000 | passa |
| n5_iniciante_var07_2_compras | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,000 | 0,000 a 0,000 | 0,100 a 0,900 | 2000 | falha |
| n5_iniciante_var09_modulo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,545 | 0,535 a 0,555 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_base | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,499 | 0,490 a 0,509 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var01_sem_punicao | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,499 | 0,490 a 0,508 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var01_2_fichas | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,499 | 0,489 a 0,509 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var02_custo_extra | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,499 | 0,490 a 0,510 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var03_auditor_externo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,499 | 0,490 a 0,509 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var04_vizinho | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,499 | 0,490 a 0,509 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var05_limite_2 | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,499 | 0,490 a 0,510 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var06_palpite | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,499 | 0,490 a 0,509 | 0,100 a 0,900 | 2000 | passa |
| n5_experiente_var07_2_compras | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,000 | 0,000 a 0,000 | 0,100 a 0,900 | 2000 | falha |
| n5_experiente_var09_modulo | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,484 | 0,475 a 0,494 | 0,100 a 0,900 | 2000 | passa |

### REQ-12: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,065 | 0,042 a 0,086 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var01_sem_punicao | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,059 | 0,039 a 0,082 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var01_2_fichas | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,058 | 0,037 a 0,082 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var02_custo_extra | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,059 | 0,038 a 0,083 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var03_auditor_externo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,072 | 0,052 a 0,094 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var04_vizinho | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,061 | 0,039 a 0,082 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var05_limite_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,077 | 0,055 a 0,098 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var06_palpite | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,056 | 0,034 a 0,077 | -0,100 a 0,100 | 2000 | passa |
| n4_iniciante_var07_2_compras | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,089 | 0,066 a 0,111 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_iniciante_var09_modulo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,082 | 0,059 a 0,105 | -0,100 a 0,100 | 2000 | inconclusivo |
| n4_experiente_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,030 | 0,008 a 0,050 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var01_sem_punicao | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,028 | 0,007 a 0,051 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var01_2_fichas | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,025 | 0,005 a 0,046 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var02_custo_extra | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,017 | -0,004 a 0,038 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var03_auditor_externo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,049 | 0,028 a 0,069 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var04_vizinho | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,038 | 0,019 a 0,061 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var05_limite_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,027 | 0,003 a 0,047 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var06_palpite | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,025 | 0,003 a 0,047 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var07_2_compras | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,069 | 0,049 a 0,090 | -0,100 a 0,100 | 2000 | passa |
| n4_experiente_var09_modulo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,053 | 0,030 a 0,076 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,063 | 0,044 a 0,082 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var01_sem_punicao | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,058 | 0,042 a 0,077 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var01_2_fichas | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,060 | 0,041 a 0,077 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var02_custo_extra | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,063 | 0,046 a 0,081 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var03_auditor_externo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,046 | 0,026 a 0,064 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var04_vizinho | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,070 | 0,052 a 0,088 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var05_limite_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,076 | 0,058 a 0,095 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var06_palpite | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,063 | 0,045 a 0,081 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var07_2_compras | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,082 | 0,064 a 0,100 | -0,100 a 0,100 | 2000 | passa |
| n5_iniciante_var09_modulo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,076 | 0,057 a 0,094 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_base | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,037 | 0,020 a 0,055 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var01_sem_punicao | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,040 | 0,023 a 0,057 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var01_2_fichas | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,032 | 0,015 a 0,050 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var02_custo_extra | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,033 | 0,013 a 0,050 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var03_auditor_externo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,030 | 0,012 a 0,048 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var04_vizinho | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,048 | 0,030 a 0,066 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var05_limite_2 | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,038 | 0,021 a 0,057 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var06_palpite | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,040 | 0,021 a 0,058 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var07_2_compras | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,059 | 0,041 a 0,077 | -0,100 a 0,100 | 2000 | passa |
| n5_experiente_var09_modulo | vitória de quem começa cobrindo a chave do incidente 1 menos a dos demais | 0,061 | 0,043 a 0,080 | -0,100 a 0,100 | 2000 | passa |

Nota: n4_experiente_base: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var01_2_fichas: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var01_sem_punicao: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var02_custo_extra: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var03_auditor_externo: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var04_vizinho: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var05_limite_2: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var06_palpite: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var07_2_compras: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_experiente_var09_modulo: 1906 assentos começaram cobrindo, 6094 não.
Nota: n4_iniciante_base: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var01_2_fichas: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var01_sem_punicao: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var02_custo_extra: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var03_auditor_externo: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var04_vizinho: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var05_limite_2: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var06_palpite: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var07_2_compras: 2208 assentos começaram cobrindo, 5792 não.
Nota: n4_iniciante_var09_modulo: 1906 assentos começaram cobrindo, 6094 não.
Nota: n5_experiente_base: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var01_2_fichas: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var01_sem_punicao: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var02_custo_extra: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var03_auditor_externo: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var04_vizinho: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var05_limite_2: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var06_palpite: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var07_2_compras: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_experiente_var09_modulo: 2379 assentos começaram cobrindo, 7621 não.
Nota: n5_iniciante_base: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var01_2_fichas: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var01_sem_punicao: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var02_custo_extra: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var03_auditor_externo: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var04_vizinho: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var05_limite_2: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var06_palpite: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var07_2_compras: 2737 assentos começaram cobrindo, 7263 não.
Nota: n5_iniciante_var09_modulo: 2379 assentos começaram cobrindo, 7621 não.

### REQ-13: falha

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_iniciante_base | dano de incidente / fichas movimentadas | 0,215 | 0,213 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var01_sem_punicao | dano de incidente / fichas movimentadas | 0,219 | 0,217 a 0,221 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var01_2_fichas | dano de incidente / fichas movimentadas | 0,212 | 0,209 a 0,214 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var02_custo_extra | dano de incidente / fichas movimentadas | 0,195 | 0,193 a 0,198 | 0,200 a 0,600 | 2000 | falha |
| n4_iniciante_var03_auditor_externo | dano de incidente / fichas movimentadas | 0,215 | 0,213 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var04_vizinho | dano de incidente / fichas movimentadas | 0,223 | 0,221 a 0,225 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var05_limite_2 | dano de incidente / fichas movimentadas | 0,220 | 0,217 a 0,222 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var06_palpite | dano de incidente / fichas movimentadas | 0,213 | 0,211 a 0,216 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var07_2_compras | dano de incidente / fichas movimentadas | 0,237 | 0,234 a 0,239 | 0,200 a 0,600 | 2000 | passa |
| n4_iniciante_var09_modulo | dano de incidente / fichas movimentadas | 0,235 | 0,233 a 0,238 | 0,200 a 0,600 | 2000 | passa |
| n4_experiente_base | dano de incidente / fichas movimentadas | 0,171 | 0,169 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var01_sem_punicao | dano de incidente / fichas movimentadas | 0,176 | 0,174 a 0,178 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var01_2_fichas | dano de incidente / fichas movimentadas | 0,167 | 0,164 a 0,169 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var02_custo_extra | dano de incidente / fichas movimentadas | 0,166 | 0,163 a 0,168 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var03_auditor_externo | dano de incidente / fichas movimentadas | 0,172 | 0,170 a 0,174 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var04_vizinho | dano de incidente / fichas movimentadas | 0,178 | 0,176 a 0,181 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var05_limite_2 | dano de incidente / fichas movimentadas | 0,175 | 0,173 a 0,178 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var06_palpite | dano de incidente / fichas movimentadas | 0,169 | 0,167 a 0,171 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var07_2_compras | dano de incidente / fichas movimentadas | 0,183 | 0,180 a 0,185 | 0,200 a 0,600 | 2000 | falha |
| n4_experiente_var09_modulo | dano de incidente / fichas movimentadas | 0,190 | 0,188 a 0,192 | 0,200 a 0,600 | 2000 | falha |
| n5_iniciante_base | dano de incidente / fichas movimentadas | 0,216 | 0,213 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var01_sem_punicao | dano de incidente / fichas movimentadas | 0,219 | 0,217 a 0,221 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var01_2_fichas | dano de incidente / fichas movimentadas | 0,212 | 0,210 a 0,215 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var02_custo_extra | dano de incidente / fichas movimentadas | 0,196 | 0,194 a 0,198 | 0,200 a 0,600 | 2000 | falha |
| n5_iniciante_var03_auditor_externo | dano de incidente / fichas movimentadas | 0,216 | 0,214 a 0,218 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var04_vizinho | dano de incidente / fichas movimentadas | 0,225 | 0,223 a 0,228 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var05_limite_2 | dano de incidente / fichas movimentadas | 0,219 | 0,217 a 0,222 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var06_palpite | dano de incidente / fichas movimentadas | 0,212 | 0,209 a 0,214 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var07_2_compras | dano de incidente / fichas movimentadas | 0,236 | 0,233 a 0,238 | 0,200 a 0,600 | 2000 | passa |
| n5_iniciante_var09_modulo | dano de incidente / fichas movimentadas | 0,234 | 0,232 a 0,236 | 0,200 a 0,600 | 2000 | passa |
| n5_experiente_base | dano de incidente / fichas movimentadas | 0,173 | 0,171 a 0,175 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var01_sem_punicao | dano de incidente / fichas movimentadas | 0,178 | 0,176 a 0,180 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var01_2_fichas | dano de incidente / fichas movimentadas | 0,169 | 0,167 a 0,171 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var02_custo_extra | dano de incidente / fichas movimentadas | 0,167 | 0,165 a 0,169 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var03_auditor_externo | dano de incidente / fichas movimentadas | 0,173 | 0,171 a 0,175 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var04_vizinho | dano de incidente / fichas movimentadas | 0,180 | 0,178 a 0,182 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var05_limite_2 | dano de incidente / fichas movimentadas | 0,176 | 0,174 a 0,179 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var06_palpite | dano de incidente / fichas movimentadas | 0,168 | 0,166 a 0,170 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var07_2_compras | dano de incidente / fichas movimentadas | 0,185 | 0,183 a 0,187 | 0,200 a 0,600 | 2000 | falha |
| n5_experiente_var09_modulo | dano de incidente / fichas movimentadas | 0,190 | 0,188 a 0,192 | 0,200 a 0,600 | 2000 | falha |

Nota: o dano do Critical Failure não conta como dano de incidente.

## Taxa de vitória por bot (MET-07)

Sem veredito. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| n4_experiente_base | blefa_nunca_contesta_limiar | 4 | 3961 | 0,255 | 0,242 a 0,267 | 0,250 |
| n4_experiente_base | blefa_nunca_contesta_nunca | 4 | 2662 | 0,248 | 0,232 a 0,265 | 0,250 |
| n4_experiente_base | blefa_sempre_contesta_nunca | 4 | 1057 | 0,241 | 0,215 a 0,266 | 0,250 |
| n4_experiente_base | blefa_sempre_contesta_limiar | 4 | 320 | 0,234 | 0,192 a 0,278 | 0,250 |
| n4_experiente_var01_2_fichas | blefa_nunca_contesta_limiar | 4 | 3961 | 0,277 | 0,263 a 0,290 | 0,250 |
| n4_experiente_var01_2_fichas | blefa_nunca_contesta_nunca | 4 | 2662 | 0,245 | 0,230 a 0,261 | 0,250 |
| n4_experiente_var01_2_fichas | blefa_sempre_contesta_limiar | 4 | 320 | 0,200 | 0,161 a 0,244 | 0,250 |
| n4_experiente_var01_2_fichas | blefa_sempre_contesta_nunca | 4 | 1057 | 0,175 | 0,152 a 0,199 | 0,250 |
| n4_experiente_var01_sem_punicao | blefa_sempre_contesta_nunca | 4 | 1057 | 0,348 | 0,319 a 0,376 | 0,250 |
| n4_experiente_var01_sem_punicao | blefa_sempre_contesta_limiar | 4 | 320 | 0,292 | 0,242 a 0,344 | 0,250 |
| n4_experiente_var01_sem_punicao | blefa_nunca_contesta_nunca | 4 | 2662 | 0,252 | 0,235 a 0,268 | 0,250 |
| n4_experiente_var01_sem_punicao | blefa_nunca_contesta_limiar | 4 | 3961 | 0,219 | 0,206 a 0,232 | 0,250 |
| n4_experiente_var02_custo_extra | blefa_nunca_contesta_limiar | 4 | 3961 | 0,260 | 0,247 a 0,273 | 0,250 |
| n4_experiente_var02_custo_extra | blefa_nunca_contesta_nunca | 4 | 2662 | 0,253 | 0,238 a 0,270 | 0,250 |
| n4_experiente_var02_custo_extra | blefa_sempre_contesta_limiar | 4 | 320 | 0,227 | 0,178 a 0,272 | 0,250 |
| n4_experiente_var02_custo_extra | blefa_sempre_contesta_nunca | 4 | 1057 | 0,212 | 0,188 a 0,236 | 0,250 |
| n4_experiente_var03_auditor_externo | blefa_nunca_contesta_nunca | 4 | 2662 | 0,257 | 0,241 a 0,274 | 0,250 |
| n4_experiente_var03_auditor_externo | blefa_nunca_contesta_limiar | 4 | 3961 | 0,253 | 0,240 a 0,267 | 0,250 |
| n4_experiente_var03_auditor_externo | blefa_sempre_contesta_nunca | 4 | 1057 | 0,231 | 0,207 a 0,258 | 0,250 |
| n4_experiente_var03_auditor_externo | blefa_sempre_contesta_limiar | 4 | 320 | 0,209 | 0,166 a 0,255 | 0,250 |
| n4_experiente_var04_vizinho | blefa_sempre_contesta_nunca | 4 | 1057 | 0,266 | 0,238 a 0,292 | 0,250 |
| n4_experiente_var04_vizinho | blefa_sempre_contesta_limiar | 4 | 320 | 0,252 | 0,205 a 0,298 | 0,250 |
| n4_experiente_var04_vizinho | blefa_nunca_contesta_nunca | 4 | 2662 | 0,250 | 0,234 a 0,265 | 0,250 |
| n4_experiente_var04_vizinho | blefa_nunca_contesta_limiar | 4 | 3961 | 0,246 | 0,233 a 0,260 | 0,250 |
| n4_experiente_var05_limite_2 | blefa_sempre_contesta_limiar | 4 | 320 | 0,263 | 0,217 a 0,311 | 0,250 |
| n4_experiente_var05_limite_2 | blefa_nunca_contesta_limiar | 4 | 3961 | 0,250 | 0,237 a 0,264 | 0,250 |
| n4_experiente_var05_limite_2 | blefa_nunca_contesta_nunca | 4 | 2662 | 0,249 | 0,234 a 0,264 | 0,250 |
| n4_experiente_var05_limite_2 | blefa_sempre_contesta_nunca | 4 | 1057 | 0,248 | 0,224 a 0,272 | 0,250 |
| n4_experiente_var06_palpite | blefa_nunca_contesta_nunca | 4 | 2662 | 0,261 | 0,245 a 0,276 | 0,250 |
| n4_experiente_var06_palpite | blefa_nunca_contesta_limiar | 4 | 3961 | 0,249 | 0,236 a 0,263 | 0,250 |
| n4_experiente_var06_palpite | blefa_sempre_contesta_nunca | 4 | 1057 | 0,235 | 0,210 a 0,258 | 0,250 |
| n4_experiente_var06_palpite | blefa_sempre_contesta_limiar | 4 | 320 | 0,222 | 0,180 a 0,269 | 0,250 |
| n4_experiente_var07_2_compras | blefa_sempre_contesta_limiar | 4 | 320 | 0,253 | 0,208 a 0,302 | 0,250 |
| n4_experiente_var07_2_compras | blefa_nunca_contesta_limiar | 4 | 3961 | 0,251 | 0,238 a 0,265 | 0,250 |
| n4_experiente_var07_2_compras | blefa_nunca_contesta_nunca | 4 | 2662 | 0,251 | 0,235 a 0,266 | 0,250 |
| n4_experiente_var07_2_compras | blefa_sempre_contesta_nunca | 4 | 1057 | 0,243 | 0,219 a 0,267 | 0,250 |
| n4_experiente_var09_modulo | blefa_nunca_contesta_limiar | 4 | 3961 | 0,255 | 0,242 a 0,267 | 0,250 |
| n4_experiente_var09_modulo | blefa_sempre_contesta_nunca | 4 | 1057 | 0,249 | 0,226 a 0,276 | 0,250 |
| n4_experiente_var09_modulo | blefa_nunca_contesta_nunca | 4 | 2662 | 0,246 | 0,231 a 0,265 | 0,250 |
| n4_experiente_var09_modulo | blefa_sempre_contesta_limiar | 4 | 320 | 0,220 | 0,175 a 0,266 | 0,250 |
| n4_iniciante_base | blefa_sempre_contesta_nunca | 4 | 1057 | 0,267 | 0,240 a 0,295 | 0,250 |
| n4_iniciante_base | blefa_nunca_contesta_nunca | 4 | 2662 | 0,249 | 0,233 a 0,266 | 0,250 |
| n4_iniciante_base | blefa_nunca_contesta_limiar | 4 | 3961 | 0,247 | 0,234 a 0,259 | 0,250 |
| n4_iniciante_base | blefa_sempre_contesta_limiar | 4 | 320 | 0,237 | 0,194 a 0,280 | 0,250 |
| n4_iniciante_var01_2_fichas | blefa_nunca_contesta_limiar | 4 | 3961 | 0,263 | 0,249 a 0,277 | 0,250 |
| n4_iniciante_var01_2_fichas | blefa_nunca_contesta_nunca | 4 | 2662 | 0,246 | 0,229 a 0,262 | 0,250 |
| n4_iniciante_var01_2_fichas | blefa_sempre_contesta_limiar | 4 | 320 | 0,240 | 0,198 a 0,287 | 0,250 |
| n4_iniciante_var01_2_fichas | blefa_sempre_contesta_nunca | 4 | 1057 | 0,213 | 0,188 a 0,238 | 0,250 |
| n4_iniciante_var01_sem_punicao | blefa_sempre_contesta_nunca | 4 | 1057 | 0,316 | 0,290 a 0,343 | 0,250 |
| n4_iniciante_var01_sem_punicao | blefa_sempre_contesta_limiar | 4 | 320 | 0,275 | 0,230 a 0,322 | 0,250 |
| n4_iniciante_var01_sem_punicao | blefa_nunca_contesta_nunca | 4 | 2662 | 0,255 | 0,238 a 0,272 | 0,250 |
| n4_iniciante_var01_sem_punicao | blefa_nunca_contesta_limiar | 4 | 3961 | 0,227 | 0,215 a 0,241 | 0,250 |
| n4_iniciante_var02_custo_extra | blefa_nunca_contesta_limiar | 4 | 3961 | 0,265 | 0,251 a 0,279 | 0,250 |
| n4_iniciante_var02_custo_extra | blefa_nunca_contesta_nunca | 4 | 2662 | 0,261 | 0,244 a 0,277 | 0,250 |
| n4_iniciante_var02_custo_extra | blefa_sempre_contesta_nunca | 4 | 1057 | 0,192 | 0,170 a 0,216 | 0,250 |
| n4_iniciante_var02_custo_extra | blefa_sempre_contesta_limiar | 4 | 320 | 0,164 | 0,125 a 0,208 | 0,250 |
| n4_iniciante_var03_auditor_externo | blefa_sempre_contesta_nunca | 4 | 1057 | 0,253 | 0,227 a 0,280 | 0,250 |
| n4_iniciante_var03_auditor_externo | blefa_nunca_contesta_nunca | 4 | 2662 | 0,251 | 0,234 a 0,266 | 0,250 |
| n4_iniciante_var03_auditor_externo | blefa_nunca_contesta_limiar | 4 | 3961 | 0,250 | 0,236 a 0,264 | 0,250 |
| n4_iniciante_var03_auditor_externo | blefa_sempre_contesta_limiar | 4 | 320 | 0,228 | 0,180 a 0,272 | 0,250 |
| n4_iniciante_var04_vizinho | blefa_nunca_contesta_nunca | 4 | 2662 | 0,255 | 0,239 a 0,272 | 0,250 |
| n4_iniciante_var04_vizinho | blefa_sempre_contesta_nunca | 4 | 1057 | 0,249 | 0,224 a 0,274 | 0,250 |
| n4_iniciante_var04_vizinho | blefa_nunca_contesta_limiar | 4 | 3961 | 0,248 | 0,234 a 0,262 | 0,250 |
| n4_iniciante_var04_vizinho | blefa_sempre_contesta_limiar | 4 | 320 | 0,230 | 0,186 a 0,277 | 0,250 |
| n4_iniciante_var05_limite_2 | blefa_sempre_contesta_nunca | 4 | 1057 | 0,262 | 0,235 a 0,288 | 0,250 |
| n4_iniciante_var05_limite_2 | blefa_nunca_contesta_limiar | 4 | 3961 | 0,253 | 0,240 a 0,266 | 0,250 |
| n4_iniciante_var05_limite_2 | blefa_nunca_contesta_nunca | 4 | 2662 | 0,244 | 0,228 a 0,260 | 0,250 |
| n4_iniciante_var05_limite_2 | blefa_sempre_contesta_limiar | 4 | 320 | 0,227 | 0,183 a 0,272 | 0,250 |
| n4_iniciante_var06_palpite | blefa_nunca_contesta_nunca | 4 | 2662 | 0,260 | 0,244 a 0,277 | 0,250 |
| n4_iniciante_var06_palpite | blefa_sempre_contesta_nunca | 4 | 1057 | 0,252 | 0,224 a 0,277 | 0,250 |
| n4_iniciante_var06_palpite | blefa_nunca_contesta_limiar | 4 | 3961 | 0,246 | 0,233 a 0,260 | 0,250 |
| n4_iniciante_var06_palpite | blefa_sempre_contesta_limiar | 4 | 320 | 0,206 | 0,164 a 0,248 | 0,250 |
| n4_iniciante_var07_2_compras | blefa_nunca_contesta_limiar | 4 | 3961 | 0,254 | 0,241 a 0,268 | 0,250 |
| n4_iniciante_var07_2_compras | blefa_nunca_contesta_nunca | 4 | 2662 | 0,247 | 0,232 a 0,264 | 0,250 |
| n4_iniciante_var07_2_compras | blefa_sempre_contesta_nunca | 4 | 1057 | 0,244 | 0,219 a 0,270 | 0,250 |
| n4_iniciante_var07_2_compras | blefa_sempre_contesta_limiar | 4 | 320 | 0,239 | 0,197 a 0,283 | 0,250 |
| n4_iniciante_var09_modulo | blefa_sempre_contesta_limiar | 4 | 320 | 0,269 | 0,225 a 0,316 | 0,250 |
| n4_iniciante_var09_modulo | blefa_nunca_contesta_limiar | 4 | 3961 | 0,256 | 0,242 a 0,269 | 0,250 |
| n4_iniciante_var09_modulo | blefa_sempre_contesta_nunca | 4 | 1057 | 0,243 | 0,218 a 0,267 | 0,250 |
| n4_iniciante_var09_modulo | blefa_nunca_contesta_nunca | 4 | 2662 | 0,242 | 0,226 a 0,259 | 0,250 |
| n5_experiente_base | blefa_nunca_contesta_nunca | 5 | 3132 | 0,208 | 0,194 a 0,222 | 0,200 |
| n5_experiente_base | blefa_nunca_contesta_limiar | 5 | 5422 | 0,204 | 0,193 a 0,214 | 0,200 |
| n5_experiente_base | blefa_sempre_contesta_nunca | 5 | 1305 | 0,171 | 0,151 a 0,192 | 0,200 |
| n5_experiente_base | blefa_sempre_contesta_limiar | 5 | 141 | 0,142 | 0,085 a 0,199 | 0,200 |
| n5_experiente_var01_2_fichas | blefa_nunca_contesta_limiar | 5 | 5422 | 0,222 | 0,211 a 0,233 | 0,200 |
| n5_experiente_var01_2_fichas | blefa_nunca_contesta_nunca | 5 | 3132 | 0,200 | 0,185 a 0,214 | 0,200 |
| n5_experiente_var01_2_fichas | blefa_sempre_contesta_limiar | 5 | 141 | 0,135 | 0,082 a 0,199 | 0,200 |
| n5_experiente_var01_2_fichas | blefa_sempre_contesta_nunca | 5 | 1305 | 0,117 | 0,100 a 0,134 | 0,200 |
| n5_experiente_var01_sem_punicao | blefa_sempre_contesta_nunca | 5 | 1305 | 0,263 | 0,239 a 0,285 | 0,200 |
| n5_experiente_var01_sem_punicao | blefa_nunca_contesta_nunca | 5 | 3132 | 0,217 | 0,203 a 0,230 | 0,200 |
| n5_experiente_var01_sem_punicao | blefa_sempre_contesta_limiar | 5 | 141 | 0,188 | 0,124 a 0,252 | 0,200 |
| n5_experiente_var01_sem_punicao | blefa_nunca_contesta_limiar | 5 | 5422 | 0,176 | 0,166 a 0,185 | 0,200 |
| n5_experiente_var02_custo_extra | blefa_nunca_contesta_nunca | 5 | 3132 | 0,213 | 0,199 a 0,227 | 0,200 |
| n5_experiente_var02_custo_extra | blefa_nunca_contesta_limiar | 5 | 5422 | 0,207 | 0,197 a 0,218 | 0,200 |
| n5_experiente_var02_custo_extra | blefa_sempre_contesta_nunca | 5 | 1305 | 0,148 | 0,128 a 0,166 | 0,200 |
| n5_experiente_var02_custo_extra | blefa_sempre_contesta_limiar | 5 | 141 | 0,117 | 0,071 a 0,174 | 0,200 |
| n5_experiente_var03_auditor_externo | blefa_nunca_contesta_nunca | 5 | 3132 | 0,212 | 0,199 a 0,227 | 0,200 |
| n5_experiente_var03_auditor_externo | blefa_nunca_contesta_limiar | 5 | 5422 | 0,197 | 0,186 a 0,207 | 0,200 |
| n5_experiente_var03_auditor_externo | blefa_sempre_contesta_nunca | 5 | 1305 | 0,189 | 0,167 a 0,212 | 0,200 |
| n5_experiente_var03_auditor_externo | blefa_sempre_contesta_limiar | 5 | 141 | 0,163 | 0,106 a 0,227 | 0,200 |
| n5_experiente_var04_vizinho | blefa_sempre_contesta_nunca | 5 | 1305 | 0,213 | 0,190 a 0,235 | 0,200 |
| n5_experiente_var04_vizinho | blefa_nunca_contesta_limiar | 5 | 5422 | 0,198 | 0,188 a 0,209 | 0,200 |
| n5_experiente_var04_vizinho | blefa_nunca_contesta_nunca | 5 | 3132 | 0,198 | 0,186 a 0,211 | 0,200 |
| n5_experiente_var04_vizinho | blefa_sempre_contesta_limiar | 5 | 141 | 0,181 | 0,121 a 0,248 | 0,200 |
| n5_experiente_var05_limite_2 | blefa_nunca_contesta_nunca | 5 | 3132 | 0,210 | 0,197 a 0,225 | 0,200 |
| n5_experiente_var05_limite_2 | blefa_nunca_contesta_limiar | 5 | 5422 | 0,198 | 0,188 a 0,208 | 0,200 |
| n5_experiente_var05_limite_2 | blefa_sempre_contesta_nunca | 5 | 1305 | 0,188 | 0,167 a 0,210 | 0,200 |
| n5_experiente_var05_limite_2 | blefa_sempre_contesta_limiar | 5 | 141 | 0,170 | 0,106 a 0,234 | 0,200 |
| n5_experiente_var06_palpite | blefa_nunca_contesta_nunca | 5 | 3132 | 0,226 | 0,212 a 0,241 | 0,200 |
| n5_experiente_var06_palpite | blefa_nunca_contesta_limiar | 5 | 5422 | 0,195 | 0,184 a 0,206 | 0,200 |
| n5_experiente_var06_palpite | blefa_sempre_contesta_nunca | 5 | 1305 | 0,165 | 0,146 a 0,183 | 0,200 |
| n5_experiente_var06_palpite | blefa_sempre_contesta_limiar | 5 | 141 | 0,121 | 0,071 a 0,174 | 0,200 |
| n5_experiente_var07_2_compras | blefa_sempre_contesta_nunca | 5 | 1305 | 0,216 | 0,194 a 0,239 | 0,200 |
| n5_experiente_var07_2_compras | blefa_nunca_contesta_nunca | 5 | 3132 | 0,199 | 0,187 a 0,215 | 0,200 |
| n5_experiente_var07_2_compras | blefa_nunca_contesta_limiar | 5 | 5422 | 0,197 | 0,187 a 0,207 | 0,200 |
| n5_experiente_var07_2_compras | blefa_sempre_contesta_limiar | 5 | 141 | 0,177 | 0,117 a 0,241 | 0,200 |
| n5_experiente_var09_modulo | blefa_nunca_contesta_limiar | 5 | 5422 | 0,208 | 0,198 a 0,219 | 0,200 |
| n5_experiente_var09_modulo | blefa_nunca_contesta_nunca | 5 | 3132 | 0,194 | 0,179 a 0,207 | 0,200 |
| n5_experiente_var09_modulo | blefa_sempre_contesta_nunca | 5 | 1305 | 0,184 | 0,163 a 0,204 | 0,200 |
| n5_experiente_var09_modulo | blefa_sempre_contesta_limiar | 5 | 141 | 0,174 | 0,121 a 0,241 | 0,200 |
| n5_iniciante_base | blefa_sempre_contesta_nunca | 5 | 1305 | 0,208 | 0,187 a 0,230 | 0,200 |
| n5_iniciante_base | blefa_nunca_contesta_nunca | 5 | 3132 | 0,200 | 0,188 a 0,214 | 0,200 |
| n5_iniciante_base | blefa_nunca_contesta_limiar | 5 | 5422 | 0,200 | 0,190 a 0,210 | 0,200 |
| n5_iniciante_base | blefa_sempre_contesta_limiar | 5 | 141 | 0,110 | 0,064 a 0,167 | 0,200 |
| n5_iniciante_var01_2_fichas | blefa_nunca_contesta_limiar | 5 | 5422 | 0,212 | 0,201 a 0,223 | 0,200 |
| n5_iniciante_var01_2_fichas | blefa_nunca_contesta_nunca | 5 | 3132 | 0,194 | 0,180 a 0,207 | 0,200 |
| n5_iniciante_var01_2_fichas | blefa_sempre_contesta_nunca | 5 | 1305 | 0,176 | 0,156 a 0,197 | 0,200 |
| n5_iniciante_var01_2_fichas | blefa_sempre_contesta_limiar | 5 | 141 | 0,103 | 0,057 a 0,152 | 0,200 |
| n5_iniciante_var01_sem_punicao | blefa_sempre_contesta_nunca | 5 | 1305 | 0,266 | 0,243 a 0,290 | 0,200 |
| n5_iniciante_var01_sem_punicao | blefa_nunca_contesta_nunca | 5 | 3132 | 0,201 | 0,188 a 0,215 | 0,200 |
| n5_iniciante_var01_sem_punicao | blefa_nunca_contesta_limiar | 5 | 5422 | 0,184 | 0,174 a 0,194 | 0,200 |
| n5_iniciante_var01_sem_punicao | blefa_sempre_contesta_limiar | 5 | 141 | 0,181 | 0,117 a 0,248 | 0,200 |
| n5_iniciante_var02_custo_extra | blefa_nunca_contesta_nunca | 5 | 3132 | 0,211 | 0,196 a 0,225 | 0,200 |
| n5_iniciante_var02_custo_extra | blefa_nunca_contesta_limiar | 5 | 5422 | 0,209 | 0,198 a 0,220 | 0,200 |
| n5_iniciante_var02_custo_extra | blefa_sempre_contesta_nunca | 5 | 1305 | 0,147 | 0,127 a 0,165 | 0,200 |
| n5_iniciante_var02_custo_extra | blefa_sempre_contesta_limiar | 5 | 141 | 0,092 | 0,050 a 0,149 | 0,200 |
| n5_iniciante_var03_auditor_externo | blefa_nunca_contesta_limiar | 5 | 5422 | 0,203 | 0,192 a 0,214 | 0,200 |
| n5_iniciante_var03_auditor_externo | blefa_nunca_contesta_nunca | 5 | 3132 | 0,199 | 0,185 a 0,212 | 0,200 |
| n5_iniciante_var03_auditor_externo | blefa_sempre_contesta_limiar | 5 | 141 | 0,199 | 0,142 a 0,262 | 0,200 |
| n5_iniciante_var03_auditor_externo | blefa_sempre_contesta_nunca | 5 | 1305 | 0,190 | 0,169 a 0,213 | 0,200 |
| n5_iniciante_var04_vizinho | blefa_sempre_contesta_nunca | 5 | 1305 | 0,219 | 0,197 a 0,242 | 0,200 |
| n5_iniciante_var04_vizinho | blefa_nunca_contesta_nunca | 5 | 3132 | 0,201 | 0,188 a 0,215 | 0,200 |
| n5_iniciante_var04_vizinho | blefa_nunca_contesta_limiar | 5 | 5422 | 0,196 | 0,186 a 0,206 | 0,200 |
| n5_iniciante_var04_vizinho | blefa_sempre_contesta_limiar | 5 | 141 | 0,170 | 0,113 a 0,234 | 0,200 |
| n5_iniciante_var05_limite_2 | blefa_sempre_contesta_nunca | 5 | 1305 | 0,221 | 0,200 a 0,245 | 0,200 |
| n5_iniciante_var05_limite_2 | blefa_nunca_contesta_limiar | 5 | 5422 | 0,200 | 0,190 a 0,210 | 0,200 |
| n5_iniciante_var05_limite_2 | blefa_nunca_contesta_nunca | 5 | 3132 | 0,192 | 0,179 a 0,206 | 0,200 |
| n5_iniciante_var05_limite_2 | blefa_sempre_contesta_limiar | 5 | 141 | 0,191 | 0,135 a 0,255 | 0,200 |
| n5_iniciante_var06_palpite | blefa_nunca_contesta_nunca | 5 | 3132 | 0,207 | 0,192 a 0,221 | 0,200 |
| n5_iniciante_var06_palpite | blefa_sempre_contesta_nunca | 5 | 1305 | 0,202 | 0,182 a 0,224 | 0,200 |
| n5_iniciante_var06_palpite | blefa_nunca_contesta_limiar | 5 | 5422 | 0,198 | 0,188 a 0,209 | 0,200 |
| n5_iniciante_var06_palpite | blefa_sempre_contesta_limiar | 5 | 141 | 0,103 | 0,057 a 0,152 | 0,200 |
| n5_iniciante_var07_2_compras | blefa_sempre_contesta_nunca | 5 | 1305 | 0,212 | 0,191 a 0,234 | 0,200 |
| n5_iniciante_var07_2_compras | blefa_nunca_contesta_limiar | 5 | 5422 | 0,206 | 0,196 a 0,217 | 0,200 |
| n5_iniciante_var07_2_compras | blefa_nunca_contesta_nunca | 5 | 3132 | 0,186 | 0,173 a 0,199 | 0,200 |
| n5_iniciante_var07_2_compras | blefa_sempre_contesta_limiar | 5 | 141 | 0,170 | 0,113 a 0,234 | 0,200 |
| n5_iniciante_var09_modulo | blefa_sempre_contesta_nunca | 5 | 1305 | 0,207 | 0,185 a 0,230 | 0,200 |
| n5_iniciante_var09_modulo | blefa_nunca_contesta_nunca | 5 | 3132 | 0,200 | 0,186 a 0,213 | 0,200 |
| n5_iniciante_var09_modulo | blefa_nunca_contesta_limiar | 5 | 5422 | 0,200 | 0,189 a 0,210 | 0,200 |
| n5_iniciante_var09_modulo | blefa_sempre_contesta_limiar | 5 | 141 | 0,156 | 0,096 a 0,216 | 0,200 |

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903). Na v2 é só descrição: o placar em fichas não está na mesma escala dos pontos da v1, e a comparação entre as versões é feita pelo REQ-02 (autor, 2026-11-10).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| n4_iniciante_base | v2 | 4 | 2000 | **1,50** | 0,767 | 0,748 a 0,785 |
| n4_iniciante_base | v2 | 4 | 2000 | 1,25 | 0,949 | 0,938 a 0,958 |
| n4_iniciante_base | v2 | 4 | 2000 | 2,00 | 0,300 | 0,280 a 0,320 |
| n4_iniciante_var01_sem_punicao | v2 | 4 | 2000 | **1,50** | 0,757 | 0,738 a 0,775 |
| n4_iniciante_var01_sem_punicao | v2 | 4 | 2000 | 1,25 | 0,944 | 0,933 a 0,953 |
| n4_iniciante_var01_sem_punicao | v2 | 4 | 2000 | 2,00 | 0,283 | 0,264 a 0,303 |
| n4_iniciante_var01_2_fichas | v2 | 4 | 2000 | **1,50** | 0,782 | 0,764 a 0,800 |
| n4_iniciante_var01_2_fichas | v2 | 4 | 2000 | 1,25 | 0,956 | 0,946 a 0,964 |
| n4_iniciante_var01_2_fichas | v2 | 4 | 2000 | 2,00 | 0,335 | 0,315 a 0,356 |
| n4_iniciante_var02_custo_extra | v2 | 4 | 2000 | **1,50** | 0,876 | 0,861 a 0,890 |
| n4_iniciante_var02_custo_extra | v2 | 4 | 2000 | 1,25 | 0,970 | 0,961 a 0,976 |
| n4_iniciante_var02_custo_extra | v2 | 4 | 2000 | 2,00 | 0,457 | 0,435 a 0,478 |
| n4_iniciante_var03_auditor_externo | v2 | 4 | 2000 | **1,50** | 0,748 | 0,729 a 0,767 |
| n4_iniciante_var03_auditor_externo | v2 | 4 | 2000 | 1,25 | 0,937 | 0,925 a 0,947 |
| n4_iniciante_var03_auditor_externo | v2 | 4 | 2000 | 2,00 | 0,294 | 0,274 a 0,314 |
| n4_iniciante_var04_vizinho | v2 | 4 | 2000 | **1,50** | 0,752 | 0,733 a 0,770 |
| n4_iniciante_var04_vizinho | v2 | 4 | 2000 | 1,25 | 0,942 | 0,930 a 0,951 |
| n4_iniciante_var04_vizinho | v2 | 4 | 2000 | 2,00 | 0,281 | 0,262 a 0,302 |
| n4_iniciante_var05_limite_2 | v2 | 4 | 2000 | **1,50** | 0,694 | 0,673 a 0,713 |
| n4_iniciante_var05_limite_2 | v2 | 4 | 2000 | 1,25 | 0,924 | 0,912 a 0,935 |
| n4_iniciante_var05_limite_2 | v2 | 4 | 2000 | 2,00 | 0,228 | 0,210 a 0,246 |
| n4_iniciante_var06_palpite | v2 | 4 | 2000 | **1,50** | 0,766 | 0,747 a 0,784 |
| n4_iniciante_var06_palpite | v2 | 4 | 2000 | 1,25 | 0,947 | 0,936 a 0,956 |
| n4_iniciante_var06_palpite | v2 | 4 | 2000 | 2,00 | 0,294 | 0,274 a 0,314 |
| n4_iniciante_var07_2_compras | v2 | 4 | 2000 | **1,50** | 0,720 | 0,700 a 0,739 |
| n4_iniciante_var07_2_compras | v2 | 4 | 2000 | 1,25 | 0,922 | 0,910 a 0,933 |
| n4_iniciante_var07_2_compras | v2 | 4 | 2000 | 2,00 | 0,234 | 0,216 a 0,253 |
| n4_iniciante_var09_modulo | v2 | 4 | 2000 | **1,50** | 0,784 | 0,766 a 0,802 |
| n4_iniciante_var09_modulo | v2 | 4 | 2000 | 1,25 | 0,955 | 0,944 a 0,963 |
| n4_iniciante_var09_modulo | v2 | 4 | 2000 | 2,00 | 0,333 | 0,313 a 0,354 |
| n4_experiente_base | v2 | 4 | 2000 | **1,50** | 0,670 | 0,649 a 0,690 |
| n4_experiente_base | v2 | 4 | 2000 | 1,25 | 0,915 | 0,902 a 0,927 |
| n4_experiente_base | v2 | 4 | 2000 | 2,00 | 0,212 | 0,195 a 0,230 |
| n4_experiente_var01_sem_punicao | v2 | 4 | 2000 | **1,50** | 0,641 | 0,620 a 0,662 |
| n4_experiente_var01_sem_punicao | v2 | 4 | 2000 | 1,25 | 0,913 | 0,900 a 0,925 |
| n4_experiente_var01_sem_punicao | v2 | 4 | 2000 | 2,00 | 0,180 | 0,164 a 0,198 |
| n4_experiente_var01_2_fichas | v2 | 4 | 2000 | **1,50** | 0,706 | 0,686 a 0,726 |
| n4_experiente_var01_2_fichas | v2 | 4 | 2000 | 1,25 | 0,928 | 0,916 a 0,939 |
| n4_experiente_var01_2_fichas | v2 | 4 | 2000 | 2,00 | 0,259 | 0,240 a 0,279 |
| n4_experiente_var02_custo_extra | v2 | 4 | 2000 | **1,50** | 0,737 | 0,717 a 0,756 |
| n4_experiente_var02_custo_extra | v2 | 4 | 2000 | 1,25 | 0,944 | 0,933 a 0,953 |
| n4_experiente_var02_custo_extra | v2 | 4 | 2000 | 2,00 | 0,276 | 0,257 a 0,296 |
| n4_experiente_var03_auditor_externo | v2 | 4 | 2000 | **1,50** | 0,658 | 0,637 a 0,679 |
| n4_experiente_var03_auditor_externo | v2 | 4 | 2000 | 1,25 | 0,920 | 0,908 a 0,932 |
| n4_experiente_var03_auditor_externo | v2 | 4 | 2000 | 2,00 | 0,192 | 0,175 a 0,210 |
| n4_experiente_var04_vizinho | v2 | 4 | 2000 | **1,50** | 0,644 | 0,623 a 0,665 |
| n4_experiente_var04_vizinho | v2 | 4 | 2000 | 1,25 | 0,893 | 0,879 a 0,906 |
| n4_experiente_var04_vizinho | v2 | 4 | 2000 | 2,00 | 0,177 | 0,161 a 0,194 |
| n4_experiente_var05_limite_2 | v2 | 4 | 2000 | **1,50** | 0,620 | 0,599 a 0,641 |
| n4_experiente_var05_limite_2 | v2 | 4 | 2000 | 1,25 | 0,914 | 0,901 a 0,926 |
| n4_experiente_var05_limite_2 | v2 | 4 | 2000 | 2,00 | 0,159 | 0,143 a 0,175 |
| n4_experiente_var06_palpite | v2 | 4 | 2000 | **1,50** | 0,658 | 0,637 a 0,678 |
| n4_experiente_var06_palpite | v2 | 4 | 2000 | 1,25 | 0,917 | 0,905 a 0,929 |
| n4_experiente_var06_palpite | v2 | 4 | 2000 | 2,00 | 0,190 | 0,173 a 0,208 |
| n4_experiente_var07_2_compras | v2 | 4 | 2000 | **1,50** | 0,621 | 0,600 a 0,642 |
| n4_experiente_var07_2_compras | v2 | 4 | 2000 | 1,25 | 0,900 | 0,886 a 0,912 |
| n4_experiente_var07_2_compras | v2 | 4 | 2000 | 2,00 | 0,160 | 0,145 a 0,177 |
| n4_experiente_var09_modulo | v2 | 4 | 2000 | **1,50** | 0,721 | 0,701 a 0,740 |
| n4_experiente_var09_modulo | v2 | 4 | 2000 | 1,25 | 0,923 | 0,910 a 0,934 |
| n4_experiente_var09_modulo | v2 | 4 | 2000 | 2,00 | 0,248 | 0,230 a 0,267 |
| n5_iniciante_base | v2 | 5 | 2000 | **1,50** | 0,754 | 0,735 a 0,773 |
| n5_iniciante_base | v2 | 5 | 2000 | 1,25 | 0,963 | 0,954 a 0,970 |
| n5_iniciante_base | v2 | 5 | 2000 | 2,00 | 0,267 | 0,248 a 0,287 |
| n5_iniciante_var01_sem_punicao | v2 | 5 | 2000 | **1,50** | 0,736 | 0,716 a 0,755 |
| n5_iniciante_var01_sem_punicao | v2 | 5 | 2000 | 1,25 | 0,957 | 0,947 a 0,965 |
| n5_iniciante_var01_sem_punicao | v2 | 5 | 2000 | 2,00 | 0,256 | 0,237 a 0,275 |
| n5_iniciante_var01_2_fichas | v2 | 5 | 2000 | **1,50** | 0,771 | 0,752 a 0,789 |
| n5_iniciante_var01_2_fichas | v2 | 5 | 2000 | 1,25 | 0,966 | 0,957 a 0,973 |
| n5_iniciante_var01_2_fichas | v2 | 5 | 2000 | 2,00 | 0,302 | 0,283 a 0,323 |
| n5_iniciante_var02_custo_extra | v2 | 5 | 2000 | **1,50** | 0,872 | 0,857 a 0,886 |
| n5_iniciante_var02_custo_extra | v2 | 5 | 2000 | 1,25 | 0,982 | 0,975 a 0,987 |
| n5_iniciante_var02_custo_extra | v2 | 5 | 2000 | 2,00 | 0,463 | 0,441 a 0,484 |
| n5_iniciante_var03_auditor_externo | v2 | 5 | 2000 | **1,50** | 0,768 | 0,749 a 0,786 |
| n5_iniciante_var03_auditor_externo | v2 | 5 | 2000 | 1,25 | 0,971 | 0,962 a 0,977 |
| n5_iniciante_var03_auditor_externo | v2 | 5 | 2000 | 2,00 | 0,288 | 0,269 a 0,308 |
| n5_iniciante_var04_vizinho | v2 | 5 | 2000 | **1,50** | 0,758 | 0,739 a 0,776 |
| n5_iniciante_var04_vizinho | v2 | 5 | 2000 | 1,25 | 0,961 | 0,952 a 0,969 |
| n5_iniciante_var04_vizinho | v2 | 5 | 2000 | 2,00 | 0,290 | 0,271 a 0,311 |
| n5_iniciante_var05_limite_2 | v2 | 5 | 2000 | **1,50** | 0,695 | 0,674 a 0,715 |
| n5_iniciante_var05_limite_2 | v2 | 5 | 2000 | 1,25 | 0,944 | 0,933 a 0,953 |
| n5_iniciante_var05_limite_2 | v2 | 5 | 2000 | 2,00 | 0,195 | 0,178 a 0,212 |
| n5_iniciante_var06_palpite | v2 | 5 | 2000 | **1,50** | 0,746 | 0,726 a 0,765 |
| n5_iniciante_var06_palpite | v2 | 5 | 2000 | 1,25 | 0,960 | 0,950 a 0,967 |
| n5_iniciante_var06_palpite | v2 | 5 | 2000 | 2,00 | 0,260 | 0,241 a 0,280 |
| n5_iniciante_var07_2_compras | v2 | 5 | 2000 | **1,50** | 0,727 | 0,707 a 0,746 |
| n5_iniciante_var07_2_compras | v2 | 5 | 2000 | 1,25 | 0,954 | 0,943 a 0,962 |
| n5_iniciante_var07_2_compras | v2 | 5 | 2000 | 2,00 | 0,240 | 0,222 a 0,260 |
| n5_iniciante_var09_modulo | v2 | 5 | 2000 | **1,50** | 0,806 | 0,788 a 0,823 |
| n5_iniciante_var09_modulo | v2 | 5 | 2000 | 1,25 | 0,973 | 0,964 a 0,979 |
| n5_iniciante_var09_modulo | v2 | 5 | 2000 | 2,00 | 0,334 | 0,314 a 0,355 |
| n5_experiente_base | v2 | 5 | 2000 | **1,50** | 0,691 | 0,670 a 0,710 |
| n5_experiente_base | v2 | 5 | 2000 | 1,25 | 0,954 | 0,943 a 0,962 |
| n5_experiente_base | v2 | 5 | 2000 | 2,00 | 0,199 | 0,182 a 0,217 |
| n5_experiente_var01_sem_punicao | v2 | 5 | 2000 | **1,50** | 0,657 | 0,636 a 0,678 |
| n5_experiente_var01_sem_punicao | v2 | 5 | 2000 | 1,25 | 0,944 | 0,933 a 0,953 |
| n5_experiente_var01_sem_punicao | v2 | 5 | 2000 | 2,00 | 0,176 | 0,160 a 0,194 |
| n5_experiente_var01_2_fichas | v2 | 5 | 2000 | **1,50** | 0,732 | 0,712 a 0,750 |
| n5_experiente_var01_2_fichas | v2 | 5 | 2000 | 1,25 | 0,959 | 0,949 a 0,966 |
| n5_experiente_var01_2_fichas | v2 | 5 | 2000 | 2,00 | 0,249 | 0,231 a 0,268 |
| n5_experiente_var02_custo_extra | v2 | 5 | 2000 | **1,50** | 0,762 | 0,743 a 0,780 |
| n5_experiente_var02_custo_extra | v2 | 5 | 2000 | 1,25 | 0,964 | 0,954 a 0,971 |
| n5_experiente_var02_custo_extra | v2 | 5 | 2000 | 2,00 | 0,269 | 0,250 a 0,288 |
| n5_experiente_var03_auditor_externo | v2 | 5 | 2000 | **1,50** | 0,696 | 0,675 a 0,716 |
| n5_experiente_var03_auditor_externo | v2 | 5 | 2000 | 1,25 | 0,955 | 0,944 a 0,963 |
| n5_experiente_var03_auditor_externo | v2 | 5 | 2000 | 2,00 | 0,194 | 0,177 a 0,211 |
| n5_experiente_var04_vizinho | v2 | 5 | 2000 | **1,50** | 0,634 | 0,613 a 0,655 |
| n5_experiente_var04_vizinho | v2 | 5 | 2000 | 1,25 | 0,938 | 0,927 a 0,948 |
| n5_experiente_var04_vizinho | v2 | 5 | 2000 | 2,00 | 0,150 | 0,136 a 0,167 |
| n5_experiente_var05_limite_2 | v2 | 5 | 2000 | **1,50** | 0,628 | 0,607 a 0,649 |
| n5_experiente_var05_limite_2 | v2 | 5 | 2000 | 1,25 | 0,934 | 0,922 a 0,944 |
| n5_experiente_var05_limite_2 | v2 | 5 | 2000 | 2,00 | 0,150 | 0,135 a 0,166 |
| n5_experiente_var06_palpite | v2 | 5 | 2000 | **1,50** | 0,657 | 0,636 a 0,677 |
| n5_experiente_var06_palpite | v2 | 5 | 2000 | 1,25 | 0,948 | 0,937 a 0,956 |
| n5_experiente_var06_palpite | v2 | 5 | 2000 | 2,00 | 0,169 | 0,153 a 0,186 |
| n5_experiente_var07_2_compras | v2 | 5 | 2000 | **1,50** | 0,623 | 0,602 a 0,644 |
| n5_experiente_var07_2_compras | v2 | 5 | 2000 | 1,25 | 0,935 | 0,924 a 0,945 |
| n5_experiente_var07_2_compras | v2 | 5 | 2000 | 2,00 | 0,131 | 0,117 a 0,146 |
| n5_experiente_var09_modulo | v2 | 5 | 2000 | **1,50** | 0,722 | 0,702 a 0,741 |
| n5_experiente_var09_modulo | v2 | 5 | 2000 | 1,25 | 0,957 | 0,947 a 0,965 |
| n5_experiente_var09_modulo | v2 | 5 | 2000 | 2,00 | 0,234 | 0,216 a 0,254 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Sistema cheio no 1º Planejamento | Blefes por partida (bem-sucedidos) | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n4_iniciante_base | 2000 | 0 | 21,8 | 2,0 | 1,6% | 0,0% | 0,0% | 0,178 | 10,7 | 7,2 | 57,5% | 1,93 (24,1%) | 34,9 / 38,4 / 41,9 |
| n4_iniciante_var01_sem_punicao | 2000 | 0 | 21,8 | 2,0 | 1,9% | 0,0% | 0,0% | 0,170 | 10,6 | 7,2 | 57,5% | 1,93 (24,1%) | 34,9 / 38,4 / 41,9 |
| n4_iniciante_var01_2_fichas | 2000 | 0 | 21,8 | 2,0 | 1,5% | 0,0% | 0,0% | 0,172 | 11,0 | 7,3 | 57,5% | 1,93 (24,1%) | 34,9 / 38,4 / 41,9 |
| n4_iniciante_var02_custo_extra | 2000 | 0 | 21,8 | 2,0 | 1,7% | 0,0% | 0,0% | 0,163 | 9,6 | 6,0 | 57,5% | 1,93 (24,1%) | 34,9 / 38,4 / 41,9 |
| n4_iniciante_var03_auditor_externo | 2000 | 0 | 21,9 | 2,0 | 1,7% | 0,0% | 0,0% | 0,192 | 10,7 | 7,2 | 57,5% | 1,94 (24,5%) | 34,8 / 38,5 / 42,2 |
| n4_iniciante_var04_vizinho | 2000 | 0 | 16,4 | 1,4 | 1,9% | 0,0% | 0,0% | 0,167 | 10,1 | 6,9 | 57,5% | 1,33 (24,9%) | 31,0 / 34,6 / 38,6 |
| n4_iniciante_var05_limite_2 | 2000 | 0 | 16,3 | 1,5 | 2,5% | 0,0% | 0,0% | 0,205 | 10,2 | 7,1 | 57,5% | 1,41 (24,1%) | 31,5 / 34,0 / 36,7 |
| n4_iniciante_var06_palpite | 2000 | 0 | 21,8 | 2,0 | 1,6% | 0,0% | 0,0% | 0,170 | 10,9 | 7,4 | 57,5% | 1,93 (24,1%) | 34,9 / 38,4 / 41,9 |
| n4_iniciante_var07_2_compras | 2000 | 0 | 11,4 | 1,1 | 2,1% | 0,0% | 0,0% | 0,209 | 9,3 | 6,5 | 0,0% | 1,04 (22,3%) | 28,0 / 30,3 / 32,8 |
| n4_iniciante_var09_modulo | 2000 | 0 | 22,1 | 2,0 | 1,1% | 0,0% | 0,0% | 0,187 | 10,2 | 6,8 | 54,8% | 2,24 (22,6%) | 34,2 / 37,6 / 41,5 |
| n4_experiente_base | 2000 | 0 | 22,0 | 3,2 | 1,8% | 0,0% | 0,0% | 0,160 | 12,0 | 8,5 | 50,7% | 2,08 (40,3%) | 34,9 / 38,7 / 42,6 |
| n4_experiente_var01_sem_punicao | 2000 | 0 | 22,0 | 3,2 | 2,6% | 0,0% | 0,0% | 0,166 | 11,9 | 8,5 | 50,7% | 2,08 (40,5%) | 34,9 / 38,7 / 42,6 |
| n4_experiente_var01_2_fichas | 2000 | 0 | 22,0 | 3,2 | 1,8% | 0,0% | 0,0% | 0,157 | 12,4 | 8,5 | 50,7% | 2,08 (40,3%) | 34,9 / 38,7 / 42,6 |
| n4_experiente_var02_custo_extra | 2000 | 0 | 22,0 | 3,2 | 2,1% | 0,0% | 0,0% | 0,157 | 11,6 | 7,9 | 50,7% | 2,08 (40,3%) | 34,9 / 38,7 / 42,6 |
| n4_experiente_var03_auditor_externo | 2000 | 0 | 22,0 | 3,2 | 2,5% | 0,0% | 0,0% | 0,183 | 12,0 | 8,5 | 50,7% | 2,06 (39,7%) | 34,9 / 38,7 / 42,5 |
| n4_experiente_var04_vizinho | 2000 | 0 | 16,7 | 2,3 | 2,7% | 0,0% | 0,0% | 0,193 | 11,4 | 8,2 | 50,7% | 1,42 (41,6%) | 31,2 / 34,9 / 39,0 |
| n4_experiente_var05_limite_2 | 2000 | 0 | 16,6 | 2,5 | 3,5% | 0,0% | 0,0% | 0,193 | 11,6 | 8,4 | 50,7% | 1,52 (38,9%) | 31,7 / 34,3 / 37,1 |
| n4_experiente_var06_palpite | 2000 | 0 | 22,0 | 3,2 | 2,4% | 0,0% | 0,0% | 0,160 | 12,2 | 8,7 | 50,7% | 2,08 (40,3%) | 34,9 / 38,7 / 42,6 |
| n4_experiente_var07_2_compras | 2000 | 0 | 11,4 | 1,8 | 3,6% | 0,0% | 0,0% | 0,187 | 10,8 | 7,8 | 0,0% | 1,10 (36,9%) | 28,0 / 30,4 / 33,0 |
| n4_experiente_var09_modulo | 2000 | 0 | 22,2 | 3,2 | 2,4% | 0,0% | 0,0% | 0,185 | 11,6 | 8,1 | 48,6% | 2,37 (40,3%) | 34,2 / 37,7 / 41,8 |
| n5_iniciante_base | 2000 | 0 | 28,0 | 2,3 | 2,5% | 4,8% | 0,0% | 0,118 | 11,1 | 7,3 | 57,4% | 2,18 (23,4%) | 40,4 / 44,2 / 47,9 |
| n5_iniciante_var01_sem_punicao | 2000 | 0 | 28,0 | 2,2 | 2,1% | 4,9% | 0,0% | 0,135 | 11,0 | 7,3 | 57,4% | 2,17 (24,0%) | 40,3 / 44,2 / 48,0 |
| n5_iniciante_var01_2_fichas | 2000 | 0 | 28,0 | 2,4 | 2,1% | 4,8% | 0,0% | 0,119 | 11,3 | 7,4 | 57,4% | 2,18 (23,1%) | 40,4 / 44,2 / 48,0 |
| n5_iniciante_var02_custo_extra | 2000 | 0 | 28,0 | 2,3 | 1,8% | 4,8% | 0,0% | 0,120 | 10,0 | 6,1 | 57,4% | 2,18 (23,4%) | 40,4 / 44,2 / 47,9 |
| n5_iniciante_var03_auditor_externo | 2000 | 0 | 28,1 | 2,4 | 2,2% | 5,2% | 0,0% | 0,179 | 11,2 | 7,3 | 57,4% | 2,20 (24,1%) | 40,7 / 44,4 / 48,0 |
| n5_iniciante_var04_vizinho | 2000 | 0 | 20,2 | 1,6 | 2,9% | 5,1% | 0,0% | 0,183 | 10,5 | 6,9 | 57,4% | 1,37 (25,4%) | 35,0 / 39,0 / 43,4 |
| n5_iniciante_var05_limite_2 | 2000 | 0 | 21,0 | 1,8 | 2,9% | 5,4% | 0,0% | 0,178 | 10,5 | 7,2 | 57,4% | 1,66 (23,4%) | 36,1 / 38,9 / 41,8 |
| n5_iniciante_var06_palpite | 2000 | 0 | 28,0 | 2,3 | 2,1% | 4,8% | 0,0% | 0,123 | 11,4 | 7,6 | 57,4% | 2,18 (23,4%) | 40,4 / 44,2 / 47,9 |
| n5_iniciante_var07_2_compras | 2000 | 0 | 14,6 | 1,4 | 2,4% | 0,0% | 0,0% | 0,173 | 9,7 | 6,5 | 0,0% | 1,13 (22,3%) | 31,8 / 34,2 / 36,8 |
| n5_iniciante_var09_modulo | 2000 | 0 | 28,5 | 2,5 | 1,5% | 0,0% | 0,0% | 0,158 | 10,8 | 6,9 | 54,5% | 2,49 (22,6%) | 39,8 / 43,3 / 47,3 |
| n5_experiente_base | 2000 | 0 | 28,2 | 3,9 | 3,0% | 7,8% | 0,0% | 0,187 | 12,5 | 8,5 | 49,9% | 2,36 (38,0%) | 40,7 / 44,6 / 48,5 |
| n5_experiente_var01_sem_punicao | 2000 | 0 | 28,2 | 3,8 | 3,6% | 7,8% | 0,0% | 0,183 | 12,3 | 8,5 | 49,9% | 2,36 (38,9%) | 40,7 / 44,5 / 48,4 |
| n5_experiente_var01_2_fichas | 2000 | 0 | 28,2 | 4,0 | 2,4% | 7,7% | 0,0% | 0,179 | 12,9 | 8,6 | 49,9% | 2,36 (37,7%) | 40,7 / 44,6 / 48,5 |
| n5_experiente_var02_custo_extra | 2000 | 0 | 28,2 | 3,9 | 2,6% | 7,8% | 0,0% | 0,176 | 12,1 | 8,0 | 49,9% | 2,36 (38,0%) | 40,7 / 44,6 / 48,5 |
| n5_experiente_var03_auditor_externo | 2000 | 0 | 28,2 | 3,9 | 2,8% | 7,1% | 0,0% | 0,148 | 12,5 | 8,5 | 49,9% | 2,31 (38,2%) | 40,6 / 44,6 / 48,6 |
| n5_experiente_var04_vizinho | 2000 | 0 | 20,7 | 2,6 | 3,0% | 8,2% | 0,0% | 0,185 | 11,7 | 8,1 | 49,9% | 1,48 (41,4%) | 35,2 / 39,5 / 44,0 |
| n5_experiente_var05_limite_2 | 2000 | 0 | 21,4 | 3,1 | 2,9% | 7,9% | 0,0% | 0,199 | 12,1 | 8,4 | 49,9% | 1,74 (37,7%) | 36,2 / 39,3 / 42,2 |
| n5_experiente_var06_palpite | 2000 | 0 | 28,2 | 3,9 | 2,7% | 7,8% | 0,0% | 0,177 | 13,1 | 9,0 | 49,9% | 2,36 (38,0%) | 40,7 / 44,6 / 48,5 |
| n5_experiente_var07_2_compras | 2000 | 0 | 14,5 | 2,2 | 4,9% | 0,0% | 0,0% | 0,149 | 11,1 | 7,8 | 0,0% | 1,17 (36,3%) | 31,8 / 34,2 / 36,8 |
| n5_experiente_var09_modulo | 2000 | 0 | 28,5 | 4,0 | 2,2% | 0,0% | 0,0% | 0,152 | 12,1 | 8,1 | 48,4% | 2,63 (37,0%) | 39,7 / 43,5 / 47,8 |

## Equilíbrio dentro da partida (descrição)

Números sem critério de aceite; os vereditos, quando pedidos, estão na seção de requisitos. Razão de testes: máximo sobre a média de testes recebidos na partida (REQ-06a). Contra o menor: fração dos testes contra quem tinha o menor placar (REQ-06b). Zeradas: partidas com alguém em 0 ficha antes do último ciclo (REQ-07). Parado: percentil 90 do tempo parado por jogador e ciclo, pelos tempos provisórios do MOD-05 (REQ-10). Peso do dano: dano de incidente sobre as fichas movimentadas (REQ-13). Dispersão: placar do primeiro menos o do último no fim (REQ-14).

| Cenário | Razão de testes | Contra o menor | Zeradas | Parado p90 (min) | Peso do dano | Dispersão |
|---|---|---|---|---|---|---|
| n4_iniciante_base | 1,36 | 0,417 | 7,3% | 5,8 | 0,215 | 6,8 |
| n4_iniciante_var01_sem_punicao | 1,36 | 0,420 | 6,6% | 5,8 | 0,219 | 6,6 |
| n4_iniciante_var01_2_fichas | 1,36 | 0,415 | 9,1% | 5,8 | 0,212 | 7,1 |
| n4_iniciante_var02_custo_extra | 1,36 | 0,405 | 19,4% | 5,8 | 0,195 | 6,6 |
| n4_iniciante_var03_auditor_externo | 1,35 | 0,415 | 6,0% | 7,3 | 0,215 | 6,7 |
| n4_iniciante_var04_vizinho | 1,49 | 0,433 | 7,9% | 5,0 | 0,223 | 6,2 |
| n4_iniciante_var05_limite_2 | 1,16 | 0,436 | 8,1% | 4,7 | 0,220 | 5,8 |
| n4_iniciante_var06_palpite | 1,36 | 0,417 | 7,0% | 5,8 | 0,213 | 6,9 |
| n4_iniciante_var07_2_compras | 1,54 | 0,437 | 10,0% | 4,1 | 0,237 | 5,4 |
| n4_iniciante_var09_modulo | 1,36 | 0,419 | 7,4% | 5,7 | 0,235 | 6,6 |
| n4_experiente_base | 1,38 | 0,421 | 3,1% | 5,8 | 0,171 | 7,0 |
| n4_experiente_var01_sem_punicao | 1,38 | 0,424 | 2,9% | 5,8 | 0,176 | 6,8 |
| n4_experiente_var01_2_fichas | 1,38 | 0,418 | 6,1% | 5,8 | 0,167 | 7,6 |
| n4_experiente_var02_custo_extra | 1,38 | 0,415 | 5,2% | 5,8 | 0,166 | 7,2 |
| n4_experiente_var03_auditor_externo | 1,37 | 0,422 | 3,8% | 7,4 | 0,172 | 7,0 |
| n4_experiente_var04_vizinho | 1,49 | 0,431 | 3,2% | 5,0 | 0,178 | 6,5 |
| n4_experiente_var05_limite_2 | 1,17 | 0,445 | 3,1% | 4,7 | 0,175 | 6,5 |
| n4_experiente_var06_palpite | 1,38 | 0,420 | 2,9% | 5,8 | 0,169 | 7,1 |
| n4_experiente_var07_2_compras | 1,56 | 0,438 | 4,0% | 4,0 | 0,183 | 5,9 |
| n4_experiente_var09_modulo | 1,37 | 0,426 | 4,8% | 5,6 | 0,190 | 7,0 |
| n5_iniciante_base | 1,40 | 0,340 | 6,9% | 9,0 | 0,216 | 7,5 |
| n5_iniciante_var01_sem_punicao | 1,40 | 0,342 | 6,3% | 9,0 | 0,219 | 7,3 |
| n5_iniciante_var01_2_fichas | 1,40 | 0,338 | 9,2% | 9,0 | 0,212 | 7,7 |
| n5_iniciante_var02_custo_extra | 1,40 | 0,326 | 21,1% | 9,0 | 0,196 | 7,3 |
| n5_iniciante_var03_auditor_externo | 1,40 | 0,342 | 8,1% | 10,2 | 0,216 | 7,6 |
| n5_iniciante_var04_vizinho | 1,55 | 0,349 | 8,9% | 7,7 | 0,225 | 6,9 |
| n5_iniciante_var05_limite_2 | 1,17 | 0,360 | 8,5% | 7,0 | 0,219 | 6,4 |
| n5_iniciante_var06_palpite | 1,40 | 0,339 | 6,3% | 9,0 | 0,212 | 7,6 |
| n5_iniciante_var07_2_compras | 1,61 | 0,359 | 11,7% | 6,3 | 0,236 | 6,0 |
| n5_iniciante_var09_modulo | 1,40 | 0,343 | 9,0% | 8,8 | 0,234 | 7,4 |
| n5_experiente_base | 1,42 | 0,347 | 5,8% | 9,2 | 0,173 | 8,0 |
| n5_experiente_var01_sem_punicao | 1,42 | 0,348 | 5,2% | 9,2 | 0,178 | 7,7 |
| n5_experiente_var01_2_fichas | 1,42 | 0,344 | 8,0% | 9,2 | 0,169 | 8,5 |
| n5_experiente_var02_custo_extra | 1,42 | 0,340 | 9,2% | 9,2 | 0,167 | 8,1 |
| n5_experiente_var03_auditor_externo | 1,42 | 0,344 | 5,7% | 10,2 | 0,173 | 8,0 |
| n5_experiente_var04_vizinho | 1,55 | 0,348 | 4,7% | 7,9 | 0,180 | 7,1 |
| n5_experiente_var05_limite_2 | 1,20 | 0,365 | 5,1% | 7,2 | 0,176 | 7,2 |
| n5_experiente_var06_palpite | 1,42 | 0,344 | 5,1% | 9,2 | 0,168 | 8,2 |
| n5_experiente_var07_2_compras | 1,64 | 0,362 | 3,8% | 6,2 | 0,185 | 6,6 |
| n5_experiente_var09_modulo | 1,43 | 0,345 | 5,5% | 8,8 | 0,190 | 7,8 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| n4_iniciante_base | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_iniciante_var01_sem_punicao | v2.2.1 com {'disputa.contestacao_blefe.defensor_paga': 0} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b2b4c79b56a2` |
| n4_iniciante_var01_2_fichas | v2.2.1 com {'disputa.contestacao_blefe.defensor_paga': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:fd34363b1b49` |
| n4_iniciante_var02_custo_extra | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 1, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:3a56d57fa7ff` |
| n4_iniciante_var03_auditor_externo | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': True, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b72d9577fc1f` |
| n4_iniciante_var04_vizinho | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': ['esquerda', 'direita', 'esquerda'], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:367dbf658331` |
| n4_iniciante_var05_limite_2 | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 2, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:9fefad9b112c` |
| n4_iniciante_var06_palpite | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': True, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:2e24e4f47b11` |
| n4_iniciante_var07_2_compras | v2.2.1 com {'planejamento.compras': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:981ca389c20a` |
| n4_iniciante_var09_modulo | v2.2.1 com {'modulo_seguranca_operacional': True} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:cf9e3da27587` |
| n4_experiente_base | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_experiente_var01_sem_punicao | v2.2.1 com {'disputa.contestacao_blefe.defensor_paga': 0} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b2b4c79b56a2` |
| n4_experiente_var01_2_fichas | v2.2.1 com {'disputa.contestacao_blefe.defensor_paga': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:fd34363b1b49` |
| n4_experiente_var02_custo_extra | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 1, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:3a56d57fa7ff` |
| n4_experiente_var03_auditor_externo | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': True, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b72d9577fc1f` |
| n4_experiente_var04_vizinho | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': ['esquerda', 'direita', 'esquerda'], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:367dbf658331` |
| n4_experiente_var05_limite_2 | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 2, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:9fefad9b112c` |
| n4_experiente_var06_palpite | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': True, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:2e24e4f47b11` |
| n4_experiente_var07_2_compras | v2.2.1 com {'planejamento.compras': 2} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:981ca389c20a` |
| n4_experiente_var09_modulo | v2.2.1 com {'modulo_seguranca_operacional': True} | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:cf9e3da27587` |
| n5_iniciante_base | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_iniciante_var01_sem_punicao | v2.2.1 com {'disputa.contestacao_blefe.defensor_paga': 0} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b2b4c79b56a2` |
| n5_iniciante_var01_2_fichas | v2.2.1 com {'disputa.contestacao_blefe.defensor_paga': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:fd34363b1b49` |
| n5_iniciante_var02_custo_extra | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 1, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:3a56d57fa7ff` |
| n5_iniciante_var03_auditor_externo | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': True, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b72d9577fc1f` |
| n5_iniciante_var04_vizinho | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': ['esquerda', 'direita', 'esquerda'], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:367dbf658331` |
| n5_iniciante_var05_limite_2 | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 2, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:9fefad9b112c` |
| n5_iniciante_var06_palpite | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': True, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:2e24e4f47b11` |
| n5_iniciante_var07_2_compras | v2.2.1 com {'planejamento.compras': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:981ca389c20a` |
| n5_iniciante_var09_modulo | v2.2.1 com {'modulo_seguranca_operacional': True} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'iniciante', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'iniciante', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:cf9e3da27587` |
| n5_experiente_base | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_experiente_var01_sem_punicao | v2.2.1 com {'disputa.contestacao_blefe.defensor_paga': 0} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b2b4c79b56a2` |
| n5_experiente_var01_2_fichas | v2.2.1 com {'disputa.contestacao_blefe.defensor_paga': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:fd34363b1b49` |
| n5_experiente_var02_custo_extra | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 1, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:3a56d57fa7ff` |
| n5_experiente_var03_auditor_externo | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': True, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:b72d9577fc1f` |
| n5_experiente_var04_vizinho | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': ['esquerda', 'direita', 'esquerda'], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:367dbf658331` |
| n5_experiente_var05_limite_2 | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 2, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': False, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:9fefad9b112c` |
| n5_experiente_var06_palpite | v2.2.1 com {'variantes': {'custo_extra_da_explicacao': {'valor': 0, 'regra': 'VAR-02'}, 'auditor_externo': {'valor': False, 'regra': 'VAR-03'}, 'auditor_externo_acertos': {'valor': 95, 'regra': 'MOD-02'}, 'auditor_externo_julgamentos': {'valor': 100, 'regra': 'MOD-02'}, 'vizinhos_designados': {'valor': [], 'regra': 'VAR-04'}, 'limite_de_testes_recebidos': {'valor': 0, 'regra': 'VAR-05'}, 'palpite_da_plateia': {'valor': True, 'regra': 'VAR-06'}, 'premio_do_palpite': {'valor': 1, 'regra': 'VAR-06'}}} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:2e24e4f47b11` |
| n5_experiente_var07_2_compras | v2.2.1 com {'planejamento.compras': 2} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:981ca389c20a` |
| n5_experiente_var09_modulo | v2.2.1 com {'modulo_seguranca_operacional': True} | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:cf9e3da27587` |

## Como refazer

No commit `cf01dd6`: `cf experimento experimentos/fase4_exp6_variantes.yaml --oficial --processos 4`. O resultado não depende do número de processos.

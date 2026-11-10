# Relatório do experimento `fase4_melhor_estilo`

Melhor estilo de jogo na v2.2.1, com mesas de 4 e de 5. Matriz 6 x 6 de estilos (um bot foco contra N-1 bots de outro estilo, com rodízio de assentos), análise de estilo dominante e dinâmica do replicador; Heurístico contra Aleatórios; mesas só de Heurísticos para os dois estilos de sistema e a equidade de assento.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase4_melhor_estilo.yaml` |
| Commit | `ccd5649` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261114 |
| Partidas | 140000 |
| Falhas | 0 |
| Registros completos gravados | 290 |
| Início | 2026-11-10T22:15:16+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-01: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_todos_heuristicos | taxa de vitória da posição 0 | 0,276 | 0,268 a 0,285 | 0,230 a 0,270 | 10000 | inconclusivo |
| n4_todos_heuristicos | taxa de vitória da posição 1 | 0,256 | 0,248 a 0,264 | 0,230 a 0,270 | 10000 | passa |
| n4_todos_heuristicos | taxa de vitória da posição 2 | 0,244 | 0,236 a 0,252 | 0,230 a 0,270 | 10000 | passa |
| n4_todos_heuristicos | taxa de vitória da posição 3 | 0,224 | 0,216 a 0,233 | 0,230 a 0,270 | 10000 | inconclusivo |
| n5_todos_heuristicos | taxa de vitória da posição 0 | 0,222 | 0,215 a 0,231 | 0,180 a 0,220 | 10000 | inconclusivo |
| n5_todos_heuristicos | taxa de vitória da posição 1 | 0,201 | 0,193 a 0,209 | 0,180 a 0,220 | 10000 | passa |
| n5_todos_heuristicos | taxa de vitória da posição 2 | 0,195 | 0,187 a 0,202 | 0,180 a 0,220 | 10000 | passa |
| n5_todos_heuristicos | taxa de vitória da posição 3 | 0,201 | 0,193 a 0,209 | 0,180 a 0,220 | 10000 | passa |
| n5_todos_heuristicos | taxa de vitória da posição 4 | 0,181 | 0,174 a 0,189 | 0,180 a 0,220 | 10000 | inconclusivo |

### REQ-03: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_heuristico_contra_aleatorio | taxa de vitória do bot foco | 0,938 | 0,927 a 0,949 | 0,375 a 1,000 | 2000 | passa |
| n5_heuristico_contra_aleatorio | taxa de vitória do bot foco | 0,926 | 0,913 a 0,937 | 0,300 a 1,000 | 2000 | passa |

Nota: piso 1.5/N; o teto ficou de fora (autor, 2026-11-10).

### REQ-04: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| estilos_4_jogadores | estilos dominantes (melhor resposta contra todas as mesas) | 0 | — | 0,000 a 0,000 | 60000 | passa |
| estilos_5_jogadores | estilos dominantes (melhor resposta contra todas as mesas) | 0 | — | 0,000 a 0,000 | 60000 | passa |

Nota: estilos_4_jogadores (diferença mínima 0): aleatorio: não dominante; construtor: não dominante; heuristico: não dominante; cacador_lider: não dominante; cacador_mais_fraco: não dominante; cacador_aleatorio: não dominante.
Nota: estilos_5_jogadores (diferença mínima 0): aleatorio: não dominante; construtor: não dominante; heuristico: não dominante; cacador_lider: não dominante; cacador_mais_fraco: não dominante; cacador_aleatorio: não dominante.

### REQ-09: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 140000 | passa |

Nota: o critério pede pelo menos 50000 partidas.

### REQ-11: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_todos_heuristicos | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,514 | 0,509 a 0,518 | 0,100 a 0,900 | 10000 | passa |
| n5_todos_heuristicos | fração de jogadores com o sistema cheio ao fim do 1º Planejamento | 0,508 | 0,504 a 0,513 | 0,100 a 0,900 | 10000 | passa |

## Matriz de estilos (MET-07 e REQ-04)

Taxa de vitória de 1 bot do estilo da linha (o foco) numa mesa em que os outros N-1 são do estilo da coluna, com rodízio de assentos. Na diagonal o foco joga contra bots iguais a ele e vence exatamente 1/N; essas mesas não são rodadas. Em negrito, as melhores respostas a cada mesa: os estilos que nenhum outro supera com clareza (intervalo de 95% da diferença inteiro acima da diferença mínima do REQ-04).

### estilos_4_jogadores (4 jogadores, referência 1/N = 0,250)

| Foco \ Mesa | aleatorio | construtor | heuristico | cacador_lider | cacador_mais_fraco | cacador_aleatorio |
|---|---|---|---|---|---|---|
| aleatorio | 0,250 (1/N) | 0,001 (0,000 a 0,003) | 0,002 (0,001 a 0,004) | 0,055 (0,046 a 0,065) | 0,004 (0,002 a 0,007) | 0,004 (0,002 a 0,007) |
| construtor | **0,973 (0,966 a 0,980)** | **0,250 (1/N)** | **0,239 (0,221 a 0,256)** | **0,531 (0,507 a 0,552)** | 0,383 (0,362 a 0,404) | **0,427 (0,407 a 0,448)** |
| heuristico | 0,938 (0,927 a 0,948) | **0,264 (0,246 a 0,283)** | **0,250 (1/N)** | **0,549 (0,528 a 0,570)** | **0,434 (0,412 a 0,456)** | **0,451 (0,430 a 0,473)** |
| cacador_lider | **0,965 (0,957 a 0,973)** | 0,168 (0,152 a 0,185) | 0,113 (0,100 a 0,127) | 0,250 (1/N) | 0,387 (0,364 a 0,409) | 0,294 (0,274 a 0,315) |
| cacador_mais_fraco | 0,925 (0,914 a 0,936) | 0,134 (0,119 a 0,148) | 0,083 (0,072 a 0,096) | 0,202 (0,187 a 0,219) | 0,250 (1/N) | 0,203 (0,185 a 0,220) |
| cacador_aleatorio | 0,943 (0,933 a 0,954) | 0,146 (0,131 a 0,162) | 0,087 (0,075 a 0,100) | 0,234 (0,216 a 0,253) | 0,325 (0,305 a 0,344) | 0,250 (1/N) |

| Estilo | Situação (REQ-04) | Por quê |
|---|---|---|
| aleatorio | não dominante | construtor se sai melhor contra a mesa de aleatorio |
| construtor | não dominante | heuristico se sai melhor contra a mesa de cacador_mais_fraco |
| heuristico | não dominante | construtor se sai melhor contra a mesa de aleatorio |
| cacador_lider | não dominante | construtor se sai melhor contra a mesa de construtor |
| cacador_mais_fraco | não dominante | construtor se sai melhor contra a mesa de aleatorio |
| cacador_aleatorio | não dominante | construtor se sai melhor contra a mesa de aleatorio |

Dinâmica do replicador (sem veredito; aproximação linear, a partir da população uniforme): heuristico 1,000 (parou de mudar).

### estilos_5_jogadores (5 jogadores, referência 1/N = 0,200)

| Foco \ Mesa | aleatorio | construtor | heuristico | cacador_lider | cacador_mais_fraco | cacador_aleatorio |
|---|---|---|---|---|---|---|
| aleatorio | 0,200 (1/N) | 0,000 (0,000 a 0,000) | 0,002 (0,001 a 0,004) | 0,066 (0,055 a 0,077) | 0,005 (0,002 a 0,009) | 0,002 (0,000 a 0,004) |
| construtor | **0,971 (0,964 a 0,978)** | 0,200 (1/N) | 0,165 (0,148 a 0,181) | **0,530 (0,508 a 0,553)** | 0,352 (0,333 a 0,374) | 0,378 (0,356 a 0,398) |
| heuristico | 0,926 (0,914 a 0,937) | **0,240 (0,223 a 0,259)** | **0,200 (1/N)** | **0,524 (0,502 a 0,546)** | **0,405 (0,384 a 0,426)** | **0,428 (0,407 a 0,449)** |
| cacador_lider | 0,948 (0,938 a 0,958) | 0,145 (0,130 a 0,161) | 0,085 (0,074 a 0,098) | 0,200 (1/N) | 0,357 (0,336 a 0,379) | 0,253 (0,232 a 0,273) |
| cacador_mais_fraco | 0,901 (0,888 a 0,915) | 0,098 (0,084 a 0,110) | 0,048 (0,039 a 0,057) | 0,176 (0,160 a 0,191) | 0,200 (1/N) | 0,164 (0,147 a 0,179) |
| cacador_aleatorio | 0,925 (0,913 a 0,935) | 0,116 (0,102 a 0,129) | 0,072 (0,060 a 0,083) | 0,185 (0,169 a 0,201) | 0,268 (0,249 a 0,286) | 0,200 (1/N) |

| Estilo | Situação (REQ-04) | Por quê |
|---|---|---|
| aleatorio | não dominante | construtor se sai melhor contra a mesa de aleatorio |
| construtor | não dominante | heuristico se sai melhor contra a mesa de construtor |
| heuristico | não dominante | construtor se sai melhor contra a mesa de aleatorio |
| cacador_lider | não dominante | construtor se sai melhor contra a mesa de aleatorio |
| cacador_mais_fraco | não dominante | construtor se sai melhor contra a mesa de aleatorio |
| cacador_aleatorio | não dominante | construtor se sai melhor contra a mesa de aleatorio |

Dinâmica do replicador (sem veredito; aproximação linear, a partir da população uniforme): heuristico 1,000 (parou de mudar).

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903). Na v2 é só descrição: o placar em fichas não está na mesma escala dos pontos da v1, e a comparação entre as versões é feita pelo REQ-02 (autor, 2026-11-10).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| n4_todos_heuristicos | v2 | 4 | 10000 | **1,50** | 0,776 | 0,768 a 0,784 |
| n4_todos_heuristicos | v2 | 4 | 10000 | 1,25 | 0,953 | 0,949 a 0,957 |
| n4_todos_heuristicos | v2 | 4 | 10000 | 2,00 | 0,322 | 0,313 a 0,331 |
| n5_todos_heuristicos | v2 | 5 | 10000 | **1,50** | 0,780 | 0,772 a 0,788 |
| n5_todos_heuristicos | v2 | 5 | 10000 | 1,25 | 0,972 | 0,968 a 0,975 |
| n5_todos_heuristicos | v2 | 5 | 10000 | 2,00 | 0,307 | 0,298 a 0,317 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Sistema cheio no 1º Planejamento | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n4_aleatorio_contra_construtor | 2000 | 0 | 24,6 | 8,6 | 1,8% | 0,0% | 0,0% | 0,172 | 14,3 | 8,9 | 80,8% | 42,9 / 46,0 / 48,8 |
| n4_aleatorio_contra_heuristico | 2000 | 0 | 22,0 | 9,4 | 1,5% | 0,0% | 0,0% | 0,198 | 14,2 | 8,6 | 42,8% | 39,2 / 43,0 / 46,4 |
| n4_aleatorio_contra_cacador_lider | 2000 | 0 | 28,7 | 10,8 | 1,0% | 0,0% | 0,0% | 0,238 | 11,7 | 7,4 | 5,8% | 44,6 / 47,9 / 50,9 |
| n4_aleatorio_contra_cacador_mais_fraco | 2000 | 0 | 28,8 | 13,5 | 2,1% | 0,0% | 0,0% | 0,354 | 15,9 | 9,2 | 5,8% | 45,8 / 49,2 / 52,5 |
| n4_aleatorio_contra_cacador_aleatorio | 2000 | 0 | 28,8 | 12,4 | 1,3% | 0,0% | 0,0% | 0,289 | 14,0 | 8,2 | 5,8% | 45,4 / 48,5 / 51,8 |
| n4_construtor_contra_aleatorio | 2000 | 0 | 22,7 | 9,2 | 0,1% | 0,0% | 0,0% | 0,205 | 17,0 | 7,4 | 42,5% | 40,4 / 44,3 / 47,8 |
| n4_construtor_contra_heuristico | 2000 | 0 | 22,7 | 8,1 | 1,9% | 0,0% | 0,0% | 0,152 | 12,8 | 8,6 | 62,6% | 39,8 / 43,2 / 46,4 |
| n4_construtor_contra_cacador_lider | 2000 | 0 | 29,5 | 10,5 | 1,1% | 0,0% | 0,0% | 0,011 | 12,0 | 7,9 | 25,0% | 46,0 / 48,8 / 51,5 |
| n4_construtor_contra_cacador_mais_fraco | 2000 | 0 | 29,5 | 10,5 | 2,1% | 0,0% | 0,0% | 0,174 | 13,7 | 8,0 | 25,0% | 46,5 / 49,3 / 52,0 |
| n4_construtor_contra_cacador_aleatorio | 2000 | 0 | 29,5 | 10,8 | 1,8% | 0,0% | 0,0% | 0,116 | 12,8 | 7,9 | 25,0% | 46,2 / 49,0 / 51,8 |
| n4_heuristico_contra_aleatorio | 2000 | 0 | 21,7 | 8,7 | 0,1% | 0,0% | 0,0% | 0,302 | 15,6 | 7,2 | 29,8% | 39,1 / 43,0 / 46,8 |
| n4_heuristico_contra_construtor | 2000 | 0 | 24,4 | 7,1 | 2,2% | 0,0% | 0,0% | 0,173 | 12,4 | 8,6 | 87,8% | 42,5 / 45,2 / 47,8 |
| n4_heuristico_contra_cacador_lider | 2000 | 0 | 29,3 | 11,0 | 0,9% | 0,0% | 0,0% | 0,039 | 12,3 | 8,0 | 11,9% | 45,2 / 48,3 / 51,3 |
| n4_heuristico_contra_cacador_mais_fraco | 2000 | 0 | 29,3 | 11,5 | 1,9% | 0,0% | 0,0% | 0,161 | 14,0 | 8,1 | 11,9% | 45,6 / 48,6 / 51,7 |
| n4_heuristico_contra_cacador_aleatorio | 2000 | 0 | 29,2 | 11,6 | 1,5% | 0,0% | 0,0% | 0,103 | 13,1 | 8,0 | 11,9% | 45,2 / 48,4 / 51,4 |
| n4_cacador_lider_contra_aleatorio | 2000 | 0 | 23,7 | 9,7 | 0,1% | 0,0% | 0,0% | 0,652 | 15,7 | 7,0 | 17,5% | 40,9 / 44,8 / 48,3 |
| n4_cacador_lider_contra_construtor | 2000 | 0 | 26,0 | 7,3 | 2,2% | 0,0% | 0,0% | 0,057 | 12,4 | 8,5 | 75,0% | 44,3 / 46,5 / 49,0 |
| n4_cacador_lider_contra_heuristico | 2000 | 0 | 24,4 | 9,3 | 1,6% | 0,0% | 0,0% | 0,052 | 12,9 | 8,5 | 36,1% | 41,1 / 44,3 / 47,4 |
| n4_cacador_lider_contra_cacador_mais_fraco | 2000 | 0 | 31,5 | 12,8 | 1,2% | 0,0% | 0,0% | 0,257 | 13,4 | 7,9 | 0,0% | 47,0 / 50,2 / 53,2 |
| n4_cacador_lider_contra_cacador_aleatorio | 2000 | 0 | 31,5 | 12,8 | 1,9% | 0,0% | 0,0% | 0,187 | 12,3 | 7,7 | 0,0% | 47,2 / 50,2 / 53,2 |
| n4_cacador_mais_fraco_contra_aleatorio | 2000 | 0 | 23,8 | 9,7 | 0,1% | 0,0% | 0,0% | 0,615 | 15,8 | 7,5 | 17,5% | 41,0 / 44,8 / 48,3 |
| n4_cacador_mais_fraco_contra_construtor | 2000 | 0 | 26,0 | 7,5 | 2,4% | 0,0% | 0,0% | 0,040 | 12,8 | 8,5 | 75,0% | 44,2 / 46,6 / 49,0 |
| n4_cacador_mais_fraco_contra_heuristico | 2000 | 0 | 24,5 | 9,6 | 1,8% | 0,0% | 0,0% | 0,082 | 13,5 | 8,5 | 36,1% | 41,1 / 44,5 / 47,7 |
| n4_cacador_mais_fraco_contra_cacador_lider | 2000 | 0 | 31,5 | 12,4 | 1,1% | 0,0% | 0,0% | 0,173 | 11,8 | 7,7 | 0,0% | 47,2 / 50,1 / 53,2 |
| n4_cacador_mais_fraco_contra_cacador_aleatorio | 2000 | 0 | 31,5 | 13,0 | 1,6% | 0,0% | 0,0% | 0,253 | 13,0 | 7,8 | 0,0% | 47,1 / 50,2 / 53,3 |
| n4_cacador_aleatorio_contra_aleatorio | 2000 | 0 | 23,8 | 9,7 | 0,1% | 0,0% | 0,0% | 0,632 | 15,7 | 7,2 | 17,5% | 41,1 / 44,8 / 48,2 |
| n4_cacador_aleatorio_contra_construtor | 2000 | 0 | 26,0 | 7,5 | 2,6% | 0,0% | 0,0% | 0,059 | 12,6 | 8,5 | 75,0% | 44,3 / 46,6 / 48,9 |
| n4_cacador_aleatorio_contra_heuristico | 2000 | 0 | 24,4 | 9,6 | 1,6% | 0,0% | 0,0% | 0,068 | 13,2 | 8,5 | 36,1% | 41,0 / 44,4 / 47,5 |
| n4_cacador_aleatorio_contra_cacador_lider | 2000 | 0 | 31,5 | 12,2 | 0,9% | 0,0% | 0,0% | 0,148 | 11,5 | 7,6 | 0,0% | 47,1 / 50,1 / 53,2 |
| n4_cacador_aleatorio_contra_cacador_mais_fraco | 2000 | 0 | 31,5 | 12,8 | 1,6% | 0,0% | 0,0% | 0,295 | 13,8 | 7,9 | 0,0% | 47,1 / 50,2 / 53,1 |
| n4_todos_heuristicos | 10000 | 0 | 21,9 | 8,5 | 1,8% | 0,0% | 0,0% | 0,165 | 12,9 | 8,6 | 51,4% | 38,7 / 42,3 / 45,6 |
| n5_aleatorio_contra_construtor | 2000 | 0 | 30,8 | 10,1 | 1,8% | 20,8% | 0,0% | 0,154 | 14,3 | 8,8 | 84,7% | 50,7 / 53,7 / 56,7 |
| n5_aleatorio_contra_heuristico | 2000 | 0 | 28,1 | 11,7 | 2,0% | 6,9% | 0,0% | 0,206 | 14,5 | 8,7 | 44,5% | 46,6 / 50,2 / 53,8 |
| n5_aleatorio_contra_cacador_lider | 2000 | 0 | 36,9 | 13,4 | 1,1% | 0,2% | 0,0% | 0,153 | 11,4 | 7,4 | 4,8% | 53,2 / 56,8 / 60,3 |
| n5_aleatorio_contra_cacador_mais_fraco | 2000 | 0 | 37,0 | 17,2 | 2,6% | 0,3% | 0,0% | 0,316 | 16,1 | 9,1 | 4,8% | 54,8 / 58,5 / 62,3 |
| n5_aleatorio_contra_cacador_aleatorio | 2000 | 0 | 36,9 | 15,8 | 1,2% | 0,3% | 0,0% | 0,281 | 14,2 | 8,1 | 4,8% | 53,8 / 57,5 / 61,0 |
| n5_construtor_contra_aleatorio | 2000 | 0 | 29,0 | 11,2 | 0,1% | 2,9% | 0,0% | 0,156 | 17,1 | 7,0 | 39,0% | 47,9 / 51,9 / 55,8 |
| n5_construtor_contra_heuristico | 2000 | 0 | 28,7 | 10,2 | 1,7% | 8,8% | 0,0% | 0,163 | 13,3 | 8,6 | 60,2% | 46,9 / 50,5 / 53,5 |
| n5_construtor_contra_cacador_lider | 2000 | 0 | 37,5 | 13,3 | 1,0% | 0,2% | 0,0% | -0,007 | 12,1 | 7,9 | 20,0% | 54,3 / 57,6 / 60,8 |
| n5_construtor_contra_cacador_mais_fraco | 2000 | 0 | 37,5 | 13,4 | 2,8% | 0,2% | 0,0% | 0,152 | 14,1 | 8,0 | 20,0% | 54,9 / 58,2 / 61,4 |
| n5_construtor_contra_cacador_aleatorio | 2000 | 0 | 37,5 | 14,1 | 2,2% | 0,2% | 0,0% | 0,154 | 13,3 | 7,9 | 20,0% | 54,8 / 57,9 / 61,1 |
| n5_heuristico_contra_aleatorio | 2000 | 0 | 28,0 | 10,9 | 0,1% | 1,8% | 0,0% | 0,273 | 16,0 | 6,9 | 28,7% | 46,7 / 51,0 / 54,8 |
| n5_heuristico_contra_construtor | 2000 | 0 | 30,6 | 8,6 | 2,9% | 14,1% | 0,0% | 0,185 | 12,9 | 8,6 | 90,0% | 50,1 / 52,8 / 55,4 |
| n5_heuristico_contra_cacador_lider | 2000 | 0 | 37,3 | 13,8 | 1,1% | 0,4% | 0,0% | 0,024 | 12,3 | 7,9 | 9,7% | 53,7 / 57,2 / 60,4 |
| n5_heuristico_contra_cacador_mais_fraco | 2000 | 0 | 37,3 | 14,4 | 2,4% | 0,4% | 0,0% | 0,173 | 14,5 | 8,1 | 9,7% | 54,2 / 57,6 / 60,9 |
| n5_heuristico_contra_cacador_aleatorio | 2000 | 0 | 37,3 | 14,9 | 1,8% | 0,3% | 0,0% | 0,128 | 13,6 | 7,9 | 9,7% | 53,7 / 57,5 / 60,8 |
| n5_cacador_lider_contra_aleatorio | 2000 | 0 | 30,0 | 11,8 | 0,1% | 0,9% | 0,0% | 0,666 | 15,9 | 6,7 | 19,0% | 48,5 / 52,5 / 56,4 |
| n5_cacador_lider_contra_construtor | 2000 | 0 | 32,0 | 8,8 | 2,5% | 3,0% | 0,0% | 0,082 | 12,7 | 8,5 | 80,0% | 51,6 / 54,2 / 56,6 |
| n5_cacador_lider_contra_heuristico | 2000 | 0 | 30,4 | 11,5 | 1,8% | 3,8% | 0,0% | 0,060 | 13,3 | 8,5 | 39,1% | 47,8 / 51,5 / 54,8 |
| n5_cacador_lider_contra_cacador_mais_fraco | 2000 | 0 | 39,5 | 15,9 | 1,8% | 0,2% | 0,0% | 0,231 | 14,0 | 8,0 | 0,0% | 55,8 / 59,3 / 62,8 |
| n5_cacador_lider_contra_cacador_aleatorio | 2000 | 0 | 39,5 | 16,0 | 1,6% | 0,2% | 0,0% | 0,187 | 12,7 | 7,7 | 0,0% | 55,7 / 59,1 / 62,3 |
| n5_cacador_mais_fraco_contra_aleatorio | 2000 | 0 | 30,0 | 11,7 | 0,1% | 0,7% | 0,0% | 0,625 | 15,8 | 7,1 | 19,0% | 48,2 / 52,5 / 56,2 |
| n5_cacador_mais_fraco_contra_construtor | 2000 | 0 | 32,0 | 9,0 | 2,3% | 3,0% | 0,0% | 0,049 | 13,3 | 8,5 | 80,0% | 51,6 / 54,2 / 56,7 |
| n5_cacador_mais_fraco_contra_heuristico | 2000 | 0 | 30,4 | 11,7 | 2,1% | 3,5% | 0,0% | 0,100 | 14,0 | 8,6 | 39,1% | 47,9 / 51,5 / 54,8 |
| n5_cacador_mais_fraco_contra_cacador_lider | 2000 | 0 | 39,5 | 15,2 | 1,1% | 0,2% | 0,0% | 0,122 | 11,7 | 7,7 | 0,0% | 55,6 / 59,2 / 62,4 |
| n5_cacador_mais_fraco_contra_cacador_aleatorio | 2000 | 0 | 39,5 | 16,3 | 1,9% | 0,2% | 0,0% | 0,252 | 13,4 | 7,8 | 0,0% | 55,5 / 59,1 / 62,6 |
| n5_cacador_aleatorio_contra_aleatorio | 2000 | 0 | 30,0 | 11,7 | 0,1% | 0,7% | 0,0% | 0,640 | 15,9 | 6,9 | 19,0% | 48,4 / 52,4 / 56,3 |
| n5_cacador_aleatorio_contra_construtor | 2000 | 0 | 32,0 | 9,0 | 3,5% | 3,0% | 0,0% | 0,069 | 13,0 | 8,5 | 80,0% | 51,7 / 54,2 / 56,7 |
| n5_cacador_aleatorio_contra_heuristico | 2000 | 0 | 30,4 | 11,7 | 2,0% | 3,6% | 0,0% | 0,098 | 13,8 | 8,5 | 39,1% | 48,0 / 51,5 / 54,8 |
| n5_cacador_aleatorio_contra_cacador_lider | 2000 | 0 | 39,5 | 14,9 | 0,8% | 0,2% | 0,0% | 0,086 | 11,4 | 7,6 | 0,0% | 55,7 / 59,2 / 62,6 |
| n5_cacador_aleatorio_contra_cacador_mais_fraco | 2000 | 0 | 39,5 | 15,8 | 4,0% | 0,2% | 0,0% | 0,288 | 14,4 | 8,0 | 0,0% | 55,9 / 59,2 / 62,8 |
| n5_todos_heuristicos | 10000 | 0 | 28,1 | 10,7 | 2,5% | 7,7% | 0,0% | 0,157 | 13,4 | 8,7 | 50,8% | 45,8 / 49,7 / 53,1 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| n4_aleatorio_contra_construtor (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_aleatorio_contra_heuristico (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_aleatorio_contra_cacador_lider (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:60ad08b41b4c` |
| n4_aleatorio_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n4_aleatorio_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:60ad08b41b4c` |
| n4_construtor_contra_aleatorio (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_construtor_contra_heuristico (rotações somadas) | v2.2.1 | 4 | construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_construtor_contra_cacador_lider (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_construtor_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_construtor_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_heuristico_contra_aleatorio (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_heuristico_contra_construtor (rotações somadas) | v2.2.1 | 4 | construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_heuristico_contra_cacador_lider (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_heuristico_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_heuristico_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_cacador_lider_contra_aleatorio (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:60ad08b41b4c` |
| n4_cacador_lider_contra_construtor (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_cacador_lider_contra_heuristico (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_cacador_lider_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n4_cacador_lider_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:60ad08b41b4c` |
| n4_cacador_mais_fraco_contra_aleatorio (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n4_cacador_mais_fraco_contra_construtor (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_cacador_mais_fraco_contra_heuristico (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_cacador_mais_fraco_contra_cacador_lider (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n4_cacador_mais_fraco_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n4_cacador_aleatorio_contra_aleatorio (rotações somadas) | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:60ad08b41b4c` |
| n4_cacador_aleatorio_contra_construtor (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_cacador_aleatorio_contra_heuristico (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_cacador_aleatorio_contra_cacador_lider (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:60ad08b41b4c` |
| n4_cacador_aleatorio_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 4 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n4_todos_heuristicos | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_aleatorio_contra_construtor (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_aleatorio_contra_heuristico (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_aleatorio_contra_cacador_lider (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:60ad08b41b4c` |
| n5_aleatorio_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n5_aleatorio_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:60ad08b41b4c` |
| n5_construtor_contra_aleatorio (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_construtor_contra_heuristico (rotações somadas) | v2.2.1 | 5 | construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_construtor_contra_cacador_lider (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_construtor_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_construtor_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_heuristico_contra_aleatorio (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_heuristico_contra_construtor (rotações somadas) | v2.2.1 | 5 | construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_heuristico_contra_cacador_lider (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_heuristico_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_heuristico_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_cacador_lider_contra_aleatorio (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:60ad08b41b4c` |
| n5_cacador_lider_contra_construtor (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_cacador_lider_contra_heuristico (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_cacador_lider_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n5_cacador_lider_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:60ad08b41b4c` |
| n5_cacador_mais_fraco_contra_aleatorio (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n5_cacador_mais_fraco_contra_construtor (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_cacador_mais_fraco_contra_heuristico (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_cacador_mais_fraco_contra_cacador_lider (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n5_cacador_mais_fraco_contra_cacador_aleatorio (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n5_cacador_aleatorio_contra_aleatorio (rotações somadas) | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'} | `sha256:60ad08b41b4c` |
| n5_cacador_aleatorio_contra_construtor (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_cacador_aleatorio_contra_heuristico (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_cacador_aleatorio_contra_cacador_lider (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'} | `sha256:60ad08b41b4c` |
| n5_cacador_aleatorio_contra_cacador_mais_fraco (rotações somadas) | v2.2.1 | 5 | cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'aleatorio'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'} | `sha256:60ad08b41b4c` |
| n5_todos_heuristicos | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |

## Como refazer

No commit `ccd5649`: `cf experimento experimentos/fase4_melhor_estilo.yaml --oficial --processos 4`. O resultado não depende do número de processos.

# Relatório do experimento `fase4_exp5b_blefe_equilibrio`

Blefes bem-sucedidos (REQ-05) em mesas de Heurísticos sorteadas da mistura de perfis de blefe do equilíbrio do Experimento 5, com 4 e com 5 jogadores.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase4_exp5b_blefe_equilibrio.yaml` |
| Commit | `e17bbf2` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261117 |
| Partidas | 20000 |
| Falhas | 0 |
| Registros completos gravados | 20 |
| Início | 2026-11-11T00:42:53+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-05: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| n4_mistura_do_equilibrio | blefes bem-sucedidos / blefes tentados, na mesa sorteada da mistura | 0,395 | 0,386 a 0,403 | 0,300 a 0,500 | 10000 | passa |
| n5_mistura_do_equilibrio | blefes bem-sucedidos / blefes tentados, na mesa sorteada da mistura | 0,385 | 0,377 a 0,393 | 0,300 a 0,500 | 10000 | passa |

Nota: n4_mistura_do_equilibrio: pesos da mistura (blefa_nunca_contesta_nunca 325, blefa_nunca_contesta_limiar 501, blefa_sempre_contesta_nunca 133, blefa_sempre_contesta_limiar 41); 21532 blefes tentados.
Nota: n5_mistura_do_equilibrio: pesos da mistura (blefa_nunca_contesta_nunca 313, blefa_nunca_contesta_limiar 541, blefa_sempre_contesta_nunca 133, blefa_sempre_contesta_limiar 13); 23535 blefes tentados.

### REQ-09: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 20000 | inconclusivo |

Nota: o critério pede pelo menos 50000 partidas.

## Taxa de vitória por bot (MET-07)

Sem veredito. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| n4_mistura_do_equilibrio | blefa_nunca_contesta_nunca | 4 | 12957 | 0,256 | 0,248 a 0,263 | 0,250 |
| n4_mistura_do_equilibrio | blefa_nunca_contesta_limiar | 4 | 19999 | 0,251 | 0,246 a 0,257 | 0,250 |
| n4_mistura_do_equilibrio | blefa_sempre_contesta_limiar | 4 | 1679 | 0,237 | 0,218 a 0,259 | 0,250 |
| n4_mistura_do_equilibrio | blefa_sempre_contesta_nunca | 4 | 5365 | 0,234 | 0,223 a 0,246 | 0,250 |
| n5_mistura_do_equilibrio | blefa_nunca_contesta_nunca | 5 | 15618 | 0,209 | 0,203 a 0,215 | 0,200 |
| n5_mistura_do_equilibrio | blefa_nunca_contesta_limiar | 5 | 27122 | 0,200 | 0,195 a 0,205 | 0,200 |
| n5_mistura_do_equilibrio | blefa_sempre_contesta_limiar | 5 | 648 | 0,187 | 0,158 a 0,215 | 0,200 |
| n5_mistura_do_equilibrio | blefa_sempre_contesta_nunca | 5 | 6612 | 0,181 | 0,172 a 0,190 | 0,200 |

## Partidas desequilibradas (MET-01)

Sem veredito. Desequilibrada: o vencedor tem pelo menos o fator vezes a média dos demais. O fator principal é o fixado em `configs/requisitos.yaml` antes da execução; os outros são análise de sensibilidade. Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903). Na v2 é só descrição: o placar em fichas não está na mesma escala dos pontos da v1, e a comparação entre as versões é feita pelo REQ-02 (autor, 2026-11-10).

| Grupo | Família | Jogadores | Partidas | Fator | Desequilibradas | IC 95% |
|---|---|---|---|---|---|---|
| n4_mistura_do_equilibrio | v2 | 4 | 10000 | **1,50** | 0,677 | 0,667 a 0,686 |
| n4_mistura_do_equilibrio | v2 | 4 | 10000 | 1,25 | 0,922 | 0,917 a 0,927 |
| n4_mistura_do_equilibrio | v2 | 4 | 10000 | 2,00 | 0,213 | 0,205 a 0,221 |
| n5_mistura_do_equilibrio | v2 | 5 | 10000 | **1,50** | 0,685 | 0,676 a 0,694 |
| n5_mistura_do_equilibrio | v2 | 5 | 10000 | 1,25 | 0,953 | 0,949 a 0,957 |
| n5_mistura_do_equilibrio | v2 | 5 | 10000 | 2,00 | 0,200 | 0,192 a 0,208 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Sistema cheio no 1º Planejamento | Blefes por partida (bem-sucedidos) | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n4_mistura_do_equilibrio | 10000 | 0 | 22,0 | 3,3 | 2,3% | 0,0% | 0,0% | 0,187 | 12,1 | 8,5 | 51,1% | 2,15 (39,5%) | 35,0 / 38,7 / 42,6 |
| n5_mistura_do_equilibrio | 10000 | 0 | 28,2 | 3,9 | 2,9% | 7,8% | 0,0% | 0,181 | 12,5 | 8,5 | 51,1% | 2,35 (38,5%) | 40,7 / 44,6 / 48,8 |

## Equilíbrio dentro da partida (descrição)

Números sem critério de aceite; os vereditos, quando pedidos, estão na seção de requisitos. Razão de testes: máximo sobre a média de testes recebidos na partida (REQ-06a). Contra o menor: fração dos testes contra quem tinha o menor placar (REQ-06b). Zeradas: partidas com alguém em 0 ficha antes do último ciclo (REQ-07). Parado: percentil 90 do tempo parado por jogador e ciclo, pelos tempos provisórios do MOD-05 (REQ-10). Peso do dano: dano de incidente sobre as fichas movimentadas (REQ-13). Dispersão: placar do primeiro menos o do último no fim (REQ-14).

| Cenário | Razão de testes | Contra o menor | Zeradas | Parado p90 (min) | Peso do dano | Dispersão |
|---|---|---|---|---|---|---|
| n4_mistura_do_equilibrio | 1,37 | 0,423 | 4,3% | 5,8 | 0,172 | 7,1 |
| n5_mistura_do_equilibrio | 1,42 | 0,343 | 5,0% | 9,2 | 0,174 | 8,0 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| n4_mistura_do_equilibrio | v2.2.1 | 4 | blefa_nunca_contesta_nunca (peso 325): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 501): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 41): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_mistura_do_equilibrio | v2.2.1 | 5 | blefa_nunca_contesta_nunca (peso 313): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; blefa_nunca_contesta_limiar (peso 541): heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; blefa_sempre_contesta_nunca (peso 133): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; blefa_sempre_contesta_limiar (peso 13): heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |

## Como refazer

No commit `e17bbf2`: `cf experimento experimentos/fase4_exp5b_blefe_equilibrio.yaml --oficial --processos 4`. O resultado não depende do número de processos.

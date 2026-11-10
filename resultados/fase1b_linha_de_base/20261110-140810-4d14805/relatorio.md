# Relatório do experimento `fase1b_linha_de_base`

Linha de base com bots aleatórios (explicação correta em 50% das defesas, Auditor que sempre julga certo). Mede a equidade de assento (REQ-01), a duração estimada (REQ-08) e a robustez do simulador (REQ-09).

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase1b_linha_de_base.yaml` |
| Commit | `4d14805` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261110 |
| Partidas | 90000 |
| Falhas | 0 |
| Registros completos gravados | 90 |
| Início | 2026-11-10T14:08:10+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-01: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| v2_2_1_com_4_jogadores | taxa de vitória da posição 0 | 0,248 | 0,244 a 0,252 | 0,230 a 0,270 | 40000 | passa |
| v2_2_1_com_4_jogadores | taxa de vitória da posição 1 | 0,249 | 0,245 a 0,253 | 0,230 a 0,270 | 40000 | passa |
| v2_2_1_com_4_jogadores | taxa de vitória da posição 2 | 0,250 | 0,246 a 0,254 | 0,230 a 0,270 | 40000 | passa |
| v2_2_1_com_4_jogadores | taxa de vitória da posição 3 | 0,253 | 0,249 a 0,257 | 0,230 a 0,270 | 40000 | passa |
| v2_2_1_com_5_jogadores | taxa de vitória da posição 0 | 0,198 | 0,194 a 0,202 | 0,180 a 0,220 | 40000 | passa |
| v2_2_1_com_5_jogadores | taxa de vitória da posição 1 | 0,198 | 0,195 a 0,202 | 0,180 a 0,220 | 40000 | passa |
| v2_2_1_com_5_jogadores | taxa de vitória da posição 2 | 0,198 | 0,194 a 0,203 | 0,180 a 0,220 | 40000 | passa |
| v2_2_1_com_5_jogadores | taxa de vitória da posição 3 | 0,203 | 0,199 a 0,207 | 0,180 a 0,220 | 40000 | passa |
| v2_2_1_com_5_jogadores | taxa de vitória da posição 4 | 0,202 | 0,198 a 0,206 | 0,180 a 0,220 | 40000 | passa |

### REQ-08: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| v2_2_1_com_4_jogadores | mediana da duração estimada (min) | 41,6 | 41,5 a 41,6 | 40,0 a 50,0 | 40000 | passa |
| v2_2_1_com_5_jogadores | mediana da duração estimada (min) | 49,2 | 49,2 a 49,2 | 40,0 a 50,0 | 40000 | passa |

Nota: depende dos tempos provisórios de configs/duracao.yaml (MOD-05).

### REQ-09: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 90000 | passa |

Nota: o critério pede pelo menos 50000 partidas.

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Fichas do vencedor | Fichas médias | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|
| v2_2_1_com_4_jogadores | 40000 | 0 | 21,1 | 4,2 | 2,1% | 0,0% | 0,0% | 9,3 | 5,8 | 37,8 / 41,6 / 45,0 |
| v2_2_1_com_5_jogadores | 40000 | 0 | 27,6 | 5,6 | 2,3% | 0,2% | 0,0% | 9,9 | 5,9 | 45,2 / 49,2 / 52,9 |
| v2_2_1_com_modulo_5_jogadores | 5000 | 0 | 27,6 | 5,5 | 2,6% | 0,0% | 0,0% | 9,4 | 5,5 | 45,3 / 49,2 / 52,8 |
| v2_2_impressa_com_6_jogadores | 5000 | 0 | 32,4 | 6,5 | 2,2% | 100,0% | 0,0% | 8,3 | 4,0 | 51,1 / 55,3 / 59,5 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| v2_2_1_com_4_jogadores | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.5, 'precisao_auditor': 1.0} | `sha256:60ad08b41b4c` |
| v2_2_1_com_5_jogadores | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.5, 'precisao_auditor': 1.0} | `sha256:60ad08b41b4c` |
| v2_2_1_com_modulo_5_jogadores | v2.2.1 com {'modulo_seguranca_operacional': True} | 5 | aleatorio {'explicacao_correta': 0.5, 'precisao_auditor': 1.0} | `sha256:cf9e3da27587` |
| v2_2_impressa_com_6_jogadores | v2.2 | 6 | aleatorio {'explicacao_correta': 0.5, 'precisao_auditor': 1.0} | `sha256:d16ad3fcd4ea` |

## Como refazer

No commit `4d14805`: `cf experimento experimentos/fase1b_linha_de_base.yaml --oficial --processos 7`. O resultado não depende do número de processos.

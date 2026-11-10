# Relatório do experimento `fase2_fumaca_estilos`

Mesas mistas com um bot de cada estilo (Aleatório, Construtor, Caçador e Heurístico; com 5 jogadores, dois Caçadores com políticas de alvo diferentes), todos experientes, com blefe moderado e contestação pelo limiar. Rodízio de assentos. Primeira taxa de vitória por estilo, sem veredito.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase2_fumaca_estilos.yaml` |
| Commit | `058bd0e` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261111 |
| Partidas | 20000 |
| Falhas | 0 |
| Registros completos gravados | 40 |
| Início | 2026-11-10T14:32:05+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-09: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 20000 | inconclusivo |

Nota: o critério pede pelo menos 50000 partidas.

## Taxa de vitória por bot (MET-07)

Sem veredito: a métrica aguarda a confirmação do autor. Cada assento conta 1 na vitória, 1/k numa vitória dividida por k e 0 na derrota. Quem não leva vantagem nenhuma fica perto da referência 1/N. As rotações do rodízio estão somadas.

| Grupo | Bot | Jogadores | Assentos jogados | Taxa de vitória | IC 95% | Referência 1/N |
|---|---|---|---|---|---|---|
| estilos_com_4_jogadores | construtor | 4 | 10000 | 0,457 | 0,448 a 0,468 | 0,250 |
| estilos_com_4_jogadores | heuristico | 4 | 10000 | 0,368 | 0,359 a 0,378 | 0,250 |
| estilos_com_4_jogadores | cacador (lider) | 4 | 10000 | 0,172 | 0,165 a 0,180 | 0,250 |
| estilos_com_4_jogadores | aleatorio | 4 | 10000 | 0,002 | 0,001 a 0,003 | 0,250 |
| estilos_com_5_jogadores | construtor | 5 | 10000 | 0,353 | 0,344 a 0,362 | 0,200 |
| estilos_com_5_jogadores | heuristico | 5 | 10000 | 0,322 | 0,313 a 0,331 | 0,200 |
| estilos_com_5_jogadores | cacador (lider) | 5 | 10000 | 0,176 | 0,168 a 0,183 | 0,200 |
| estilos_com_5_jogadores | cacador (mais_fraco) | 5 | 10000 | 0,147 | 0,140 a 0,154 | 0,200 |
| estilos_com_5_jogadores | aleatorio | 5 | 10000 | 0,002 | 0,001 a 0,003 | 0,200 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Fichas do vencedor | Fichas médias | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|
| estilos_com_4_jogadores_r0 | 2500 | 0 | 25,0 | 9,5 | 1,2% | 0,0% | 0,0% | 14,1 | 8,5 | 42,5 / 45,8 / 48,8 |
| estilos_com_4_jogadores_r1 | 2500 | 0 | 25,2 | 9,6 | 1,4% | 0,0% | 0,0% | 14,0 | 8,5 | 42,7 / 45,9 / 49,0 |
| estilos_com_4_jogadores_r2 | 2500 | 0 | 24,8 | 9,4 | 1,5% | 0,0% | 0,0% | 14,0 | 8,5 | 42,3 / 45,6 / 48,6 |
| estilos_com_4_jogadores_r3 | 2500 | 0 | 24,6 | 9,4 | 1,1% | 0,0% | 0,0% | 14,1 | 8,6 | 42,2 / 45,4 / 48,3 |
| estilos_com_5_jogadores_r0 | 2000 | 0 | 33,4 | 13,6 | 1,7% | 3,8% | 0,0% | 14,7 | 8,6 | 51,7 / 55,2 / 58,6 |
| estilos_com_5_jogadores_r1 | 2000 | 0 | 33,4 | 13,5 | 2,0% | 3,0% | 0,0% | 14,6 | 8,8 | 51,5 / 55,2 / 58,8 |
| estilos_com_5_jogadores_r2 | 2000 | 0 | 33,1 | 13,3 | 2,1% | 0,7% | 0,0% | 14,5 | 8,6 | 51,4 / 55,0 / 58,4 |
| estilos_com_5_jogadores_r3 | 2000 | 0 | 32,6 | 13,2 | 1,4% | 0,4% | 0,0% | 14,6 | 8,6 | 51,0 / 54,3 / 57,6 |
| estilos_com_5_jogadores_r4 | 2000 | 0 | 33,0 | 13,4 | 1,7% | 1,9% | 0,0% | 14,7 | 8,7 | 51,3 / 54,8 / 57,9 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| estilos_com_4_jogadores_r0 | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| estilos_com_4_jogadores_r1 | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| estilos_com_4_jogadores_r2 | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| estilos_com_4_jogadores_r3 | v2.2.1 | 4 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| estilos_com_5_jogadores_r0 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| estilos_com_5_jogadores_r1 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| estilos_com_5_jogadores_r2 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| estilos_com_5_jogadores_r3 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| estilos_com_5_jogadores_r4 | v2.2.1 | 5 | aleatorio {'explicacao_correta': 0.85, 'precisao_auditor': 0.95}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'lider'}; cacador {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar', 'alvo': 'mais_fraco'}; construtor {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |

## Como refazer

No commit `058bd0e`: `cf experimento experimentos/fase2_fumaca_estilos.yaml --oficial --processos 7`. O resultado não depende do número de processos.

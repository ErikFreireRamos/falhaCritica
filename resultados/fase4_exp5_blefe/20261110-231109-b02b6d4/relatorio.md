# Relatório do experimento `fase4_exp5_blefe`

Equilíbrio do blefe na v2.2.1, com mesas de 4 e de 5. Matriz 9 x 9 entre os perfis puros de blefe (um Heurístico foco contra N-1 Heurísticos de outro perfil, com rodízio de assentos), análise de perfil dominante e dinâmica do replicador; mesas de perfis iguais para os blefes bem-sucedidos no equilíbrio.

| Item | Valor |
|---|---|
| Arquivo | `experimentos/fase4_exp5_blefe.yaml` |
| Commit | `b02b6d4` (árvore limpa) |
| Execução oficial | sim |
| Semente mestre | 20261115 |
| Partidas | 180000 |
| Falhas | 0 |
| Registros completos gravados | 684 |
| Início | 2026-11-10T23:11:09+00:00 |

## Requisitos

Veredito: **passa** se o intervalo de confiança de 95% inteiro está dentro da zona de aceite; **falha** se está inteiro fora; **inconclusivo** se cruza a borda. As zonas foram fixadas em `configs/requisitos.yaml` antes da execução.

### REQ-04: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| blefe_4_jogadores | estilos dominantes (melhor resposta contra todas as mesas) | 0 | — | 0,000 a 0,000 | 72000 | passa |
| blefe_5_jogadores | estilos dominantes (melhor resposta contra todas as mesas) | 0 | — | 0,000 a 0,000 | 72000 | passa |

Nota: blefe_4_jogadores (diferença mínima 0): blefa_nunca_contesta_nunca: não dominante; blefa_nunca_contesta_sempre: não dominante; blefa_nunca_contesta_limiar: não dominante; blefa_metade_contesta_nunca: não dominante; blefa_metade_contesta_sempre: não dominante; blefa_metade_contesta_limiar: não dominante; blefa_sempre_contesta_nunca: não dominante; blefa_sempre_contesta_sempre: não dominante; blefa_sempre_contesta_limiar: não dominante.
Nota: blefe_5_jogadores (diferença mínima 0): blefa_nunca_contesta_nunca: não dominante; blefa_nunca_contesta_sempre: não dominante; blefa_nunca_contesta_limiar: não dominante; blefa_metade_contesta_nunca: não dominante; blefa_metade_contesta_sempre: não dominante; blefa_metade_contesta_limiar: não dominante; blefa_sempre_contesta_nunca: não dominante; blefa_sempre_contesta_sempre: não dominante; blefa_sempre_contesta_limiar: não dominante.

### REQ-05: inconclusivo

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| blefe_4_jogadores | blefes bem-sucedidos no equilíbrio | — | — | 0,300 a 0,500 | 72000 | inconclusivo |
| blefe_5_jogadores | blefes bem-sucedidos no equilíbrio | — | — | 0,300 a 0,500 | 72000 | inconclusivo |

Nota: o equilíbrio é blefa_nunca_contesta_limiar, e nessa mesa ninguém blefa.
Nota: o equilíbrio é blefa_nunca_contesta_nunca, e nessa mesa ninguém blefa.

### REQ-09: passa

| Cenário | Medida | Valor | IC 95% | Zona de aceite | Partidas | Veredito |
|---|---|---|---|---|---|---|
| todos | partidas com exceção ou violação de invariante | 0 | — | 0,000 a 0,000 | 180000 | passa |

Nota: o critério pede pelo menos 50000 partidas.

## Matrizes de ganhos entre estilos ou perfis (MET-07 e REQ-04)

Taxa de vitória de 1 bot do estilo ou perfil da linha (o foco) numa mesa em que os outros N-1 são do da coluna, com rodízio de assentos. Na diagonal o foco joga contra bots iguais a ele e vence exatamente 1/N. Em negrito, as melhores respostas a cada mesa: as linhas que nenhuma outra supera com clareza (intervalo de 95% da diferença inteiro acima da diferença mínima do REQ-04).

### blefe_4_jogadores (4 jogadores, referência 1/N = 0,250)

| Foco \ Mesa | blefa_nunca_contesta_nunca | blefa_nunca_contesta_sempre | blefa_nunca_contesta_limiar | blefa_metade_contesta_nunca | blefa_metade_contesta_sempre | blefa_metade_contesta_limiar | blefa_sempre_contesta_nunca | blefa_sempre_contesta_sempre | blefa_sempre_contesta_limiar |
|---|---|---|---|---|---|---|---|---|---|
| blefa_nunca_contesta_nunca | 0,250 (1/N) | **0,450 (0,420 a 0,480)** | **0,332 (0,303 a 0,359)** | 0,203 (0,177 a 0,229) | 0,285 (0,257 a 0,315) | 0,193 (0,170 a 0,217) | 0,111 (0,093 a 0,131) | 0,172 (0,150 a 0,197) | 0,108 (0,091 a 0,128) |
| blefa_nunca_contesta_sempre | 0,115 (0,096 a 0,135) | 0,250 (1/N) | 0,149 (0,127 a 0,170) | 0,226 (0,199 a 0,251) | 0,317 (0,287 a 0,345) | 0,237 (0,211 a 0,263) | 0,396 (0,366 a 0,426) | 0,413 (0,382 a 0,443) | 0,336 (0,305 a 0,365) |
| blefa_nunca_contesta_limiar | 0,177 (0,154 a 0,200) | 0,348 (0,320 a 0,377) | 0,250 (1/N) | 0,300 (0,273 a 0,330) | **0,415 (0,385 a 0,445)** | **0,324 (0,292 a 0,351)** | 0,493 (0,465 a 0,525) | **0,502 (0,474 a 0,535)** | **0,435 (0,404 a 0,467)** |
| blefa_metade_contesta_nunca | 0,330 (0,303 a 0,363) | 0,339 (0,308 a 0,367) | 0,230 (0,203 a 0,255) | 0,250 (1/N) | 0,213 (0,188 a 0,237) | 0,127 (0,107 a 0,146) | 0,179 (0,155 a 0,201) | 0,112 (0,093 a 0,131) | 0,056 (0,042 a 0,070) |
| blefa_metade_contesta_sempre | 0,147 (0,126 a 0,170) | 0,197 (0,173 a 0,221) | 0,111 (0,092 a 0,132) | 0,291 (0,263 a 0,318) | 0,250 (1/N) | 0,163 (0,140 a 0,186) | 0,479 (0,448 a 0,507) | 0,324 (0,295 a 0,355) | 0,258 (0,232 a 0,285) |
| blefa_metade_contesta_limiar | 0,222 (0,195 a 0,247) | 0,267 (0,240 a 0,295) | 0,174 (0,150 a 0,199) | 0,372 (0,344 a 0,404) | 0,325 (0,295 a 0,354) | 0,250 (1/N) | 0,581 (0,551 a 0,612) | 0,412 (0,382 a 0,442) | 0,333 (0,303 a 0,362) |
| blefa_sempre_contesta_nunca | **0,463 (0,433 a 0,493)** | 0,254 (0,226 a 0,281) | 0,161 (0,139 a 0,183) | 0,343 (0,314 a 0,372) | 0,150 (0,130 a 0,172) | 0,078 (0,061 a 0,094) | 0,250 (1/N) | 0,086 (0,069 a 0,103) | 0,052 (0,039 a 0,066) |
| blefa_sempre_contesta_sempre | 0,233 (0,206 a 0,260) | 0,139 (0,116 a 0,160) | 0,074 (0,059 a 0,092) | 0,403 (0,374 a 0,433) | 0,169 (0,145 a 0,191) | 0,114 (0,094 a 0,135) | 0,587 (0,556 a 0,618) | 0,250 (1/N) | 0,192 (0,167 a 0,216) |
| blefa_sempre_contesta_limiar | 0,326 (0,295 a 0,354) | 0,203 (0,178 a 0,228) | 0,122 (0,103 a 0,143) | **0,502 (0,471 a 0,534)** | 0,221 (0,198 a 0,248) | 0,159 (0,138 a 0,180) | **0,669 (0,641 a 0,699)** | 0,314 (0,285 a 0,342) | 0,250 (1/N) |

| Estilo | Situação (REQ-04) | Por quê |
|---|---|---|
| blefa_nunca_contesta_nunca | não dominante | blefa_metade_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_nunca_contesta_sempre | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_nunca_contesta_limiar | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_metade_contesta_nunca | não dominante | blefa_sempre_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_metade_contesta_sempre | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_metade_contesta_limiar | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_sempre_contesta_nunca | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_sempre |
| blefa_sempre_contesta_sempre | não dominante | blefa_metade_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_sempre_contesta_limiar | não dominante | blefa_sempre_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |

Dinâmica do replicador (sem veredito; aproximação linear, a partir da população uniforme): blefa_nunca_contesta_limiar 1,000 (parou de mudar).

Mesas de perfis iguais (REQ-05: blefes bem-sucedidos divididos por blefes tentados).

| Perfil | Partidas | Blefes por partida | Bem-sucedidos | IC 95% |
|---|---|---|---|---|
| blefa_nunca_contesta_nunca | 2000 | 0,00 | — | — |
| blefa_nunca_contesta_sempre | 2000 | 0,00 | — | — |
| blefa_nunca_contesta_limiar | 2000 | 0,00 | — | — |
| blefa_metade_contesta_nunca | 2000 | 5,81 | 0,812 | 0,805 a 0,819 |
| blefa_metade_contesta_sempre | 2000 | 5,69 | 0,000 | 0,000 a 0,000 |
| blefa_metade_contesta_limiar | 2000 | 5,69 | 0,016 | 0,014 a 0,019 |
| blefa_sempre_contesta_nunca | 2000 | 12,45 | 0,816 | 0,811 a 0,820 |
| blefa_sempre_contesta_sempre | 2000 | 11,39 | 0,000 | 0,000 a 0,000 |
| blefa_sempre_contesta_limiar | 2000 | 11,29 | 0,016 | 0,014 a 0,018 |

### blefe_5_jogadores (5 jogadores, referência 1/N = 0,200)

| Foco \ Mesa | blefa_nunca_contesta_nunca | blefa_nunca_contesta_sempre | blefa_nunca_contesta_limiar | blefa_metade_contesta_nunca | blefa_metade_contesta_sempre | blefa_metade_contesta_limiar | blefa_sempre_contesta_nunca | blefa_sempre_contesta_sempre | blefa_sempre_contesta_limiar |
|---|---|---|---|---|---|---|---|---|---|
| blefa_nunca_contesta_nunca | 0,200 (1/N) | **0,370 (0,340 a 0,401)** | **0,263 (0,236 a 0,290)** | 0,139 (0,117 a 0,160) | 0,204 (0,179 a 0,230) | 0,132 (0,114 a 0,154) | 0,083 (0,067 a 0,101) | 0,107 (0,087 a 0,126) | 0,044 (0,032 a 0,058) |
| blefa_nunca_contesta_sempre | 0,090 (0,074 a 0,107) | 0,200 (1/N) | 0,137 (0,116 a 0,159) | 0,214 (0,191 a 0,238) | 0,253 (0,225 a 0,280) | 0,194 (0,170 a 0,219) | 0,378 (0,347 a 0,408) | 0,342 (0,313 a 0,370) | 0,287 (0,260 a 0,316) |
| blefa_nunca_contesta_limiar | 0,131 (0,110 a 0,150) | 0,284 (0,258 a 0,313) | 0,200 (1/N) | 0,265 (0,238 a 0,293) | **0,337 (0,308 a 0,367)** | **0,260 (0,232 a 0,285)** | 0,470 (0,435 a 0,499) | **0,437 (0,407 a 0,466)** | **0,360 (0,331 a 0,391)** |
| blefa_metade_contesta_nunca | 0,266 (0,240 a 0,292) | 0,266 (0,238 a 0,292) | 0,174 (0,149 a 0,196) | 0,200 (1/N) | 0,135 (0,114 a 0,155) | 0,088 (0,070 a 0,105) | 0,128 (0,108 a 0,149) | 0,070 (0,053 a 0,086) | 0,031 (0,021 a 0,041) |
| blefa_metade_contesta_sempre | 0,124 (0,104 a 0,144) | 0,151 (0,130 a 0,174) | 0,084 (0,067 a 0,101) | 0,271 (0,243 a 0,297) | 0,200 (1/N) | 0,151 (0,130 a 0,174) | 0,477 (0,446 a 0,511) | 0,261 (0,235 a 0,289) | 0,222 (0,197 a 0,248) |
| blefa_metade_contesta_limiar | 0,174 (0,151 a 0,198) | 0,208 (0,182 a 0,235) | 0,129 (0,108 a 0,150) | 0,339 (0,310 a 0,367) | 0,257 (0,229 a 0,284) | 0,200 (1/N) | 0,545 (0,514 a 0,577) | 0,326 (0,298 a 0,354) | 0,267 (0,240 a 0,294) |
| blefa_sempre_contesta_nunca | **0,407 (0,378 a 0,436)** | 0,196 (0,172 a 0,220) | 0,115 (0,095 a 0,135) | 0,307 (0,279 a 0,335) | 0,092 (0,074 a 0,110) | 0,059 (0,045 a 0,072) | 0,200 (1/N) | 0,044 (0,032 a 0,057) | 0,015 (0,008 a 0,022) |
| blefa_sempre_contesta_sempre | 0,177 (0,153 a 0,202) | 0,103 (0,084 a 0,122) | 0,060 (0,046 a 0,076) | 0,353 (0,324 a 0,384) | 0,148 (0,126 a 0,169) | 0,108 (0,089 a 0,128) | 0,569 (0,538 a 0,599) | 0,200 (1/N) | 0,158 (0,134 a 0,179) |
| blefa_sempre_contesta_limiar | 0,271 (0,243 a 0,297) | 0,144 (0,123 a 0,166) | 0,081 (0,064 a 0,098) | **0,448 (0,417 a 0,477)** | 0,196 (0,173 a 0,220) | 0,143 (0,122 a 0,167) | **0,642 (0,612 a 0,672)** | 0,252 (0,226 a 0,280) | 0,200 (1/N) |

| Estilo | Situação (REQ-04) | Por quê |
|---|---|---|
| blefa_nunca_contesta_nunca | não dominante | blefa_metade_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_nunca_contesta_sempre | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_nunca_contesta_limiar | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_metade_contesta_nunca | não dominante | blefa_sempre_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_metade_contesta_sempre | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_metade_contesta_limiar | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_sempre_contesta_nunca | não dominante | blefa_nunca_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_sempre |
| blefa_sempre_contesta_sempre | não dominante | blefa_metade_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |
| blefa_sempre_contesta_limiar | não dominante | blefa_sempre_contesta_nunca se sai melhor contra a mesa de blefa_nunca_contesta_nunca |

Dinâmica do replicador (sem veredito; aproximação linear, a partir da população uniforme): blefa_nunca_contesta_nunca 1,000 (parou de mudar).

Mesas de perfis iguais (REQ-05: blefes bem-sucedidos divididos por blefes tentados).

| Perfil | Partidas | Blefes por partida | Bem-sucedidos | IC 95% |
|---|---|---|---|---|
| blefa_nunca_contesta_nunca | 2000 | 0,00 | — | — |
| blefa_nunca_contesta_sempre | 2000 | 0,00 | — | — |
| blefa_nunca_contesta_limiar | 2000 | 0,00 | — | — |
| blefa_metade_contesta_nunca | 2000 | 7,66 | 0,816 | 0,810 a 0,823 |
| blefa_metade_contesta_sempre | 2000 | 7,60 | 0,000 | 0,000 a 0,000 |
| blefa_metade_contesta_limiar | 2000 | 7,50 | 0,027 | 0,025 a 0,030 |
| blefa_sempre_contesta_nunca | 2000 | 16,50 | 0,815 | 0,811 a 0,820 |
| blefa_sempre_contesta_sempre | 2000 | 15,19 | 0,000 | 0,000 a 0,000 |
| blefa_sempre_contesta_limiar | 2000 | 15,15 | 0,027 | 0,025 a 0,029 |

## Descrição das partidas

Números sem critério de aceite. Dependem de como os bots jogam. Na v1 o placar é em pontos, não em fichas, e não há modelo de duração. Vantagem do líder: P(vencer | líder isolado no ponto de corte) - 1/N.

| Cenário | Partidas | Falhas | Testes por partida | Contestações por partida | Vitórias divididas | Partidas com reembaralhamento | Partidas em que faltou carta | Vantagem do líder | Placar do vencedor | Placar médio | Sistema cheio no 1º Planejamento | Blefes por partida (bem-sucedidos) | Duração p10 / mediana / p90 (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n4_todos_blefa_nunca_contesta_nunca | 2000 | 0 | 21,9 | 0,0 | 2,5% | 0,0% | 0,0% | 0,192 | 11,6 | 8,5 | 51,2% | 0,00 (—) | 33,7 / 36,7 / 39,7 |
| n4_blefa_nunca_contesta_nunca_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 21,9 | 6,6 | 1,8% | 0,0% | 0,0% | 0,175 | 12,9 | 8,7 | 52,2% | 0,00 (—) | 34,6 / 38,2 / 41,5 |
| n4_blefa_nunca_contesta_nunca_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 21,8 | 3,3 | 2,0% | 0,0% | 0,0% | 0,184 | 12,1 | 8,6 | 52,2% | 0,00 (—) | 34,2 / 37,4 / 40,5 |
| n4_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_nunca | 1000 | 0 | 22,3 | 0,0 | 3,6% | 0,0% | 0,0% | 0,207 | 11,3 | 8,4 | 52,2% | 4,46 (81,4%) | 37,0 / 40,0 / 42,7 |
| n4_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_sempre | 1000 | 0 | 22,1 | 8,8 | 0,9% | 0,0% | 0,0% | 0,180 | 12,9 | 8,7 | 52,2% | 4,32 (26,7%) | 38,0 / 41,7 / 44,8 |
| n4_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_limiar | 1000 | 0 | 22,1 | 5,5 | 2,1% | 0,0% | 0,0% | 0,189 | 12,4 | 8,6 | 52,2% | 4,32 (27,8%) | 37,4 / 40,8 / 43,8 |
| n4_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 22,6 | 0,0 | 5,0% | 0,0% | 0,0% | 0,278 | 10,9 | 8,1 | 52,2% | 9,57 (82,3%) | 39,7 / 43,0 / 45,3 |
| n4_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 22,2 | 11,3 | 1,8% | 0,0% | 0,0% | 0,159 | 13,2 | 8,7 | 52,2% | 8,98 (27,4%) | 41,7 / 45,3 / 48,4 |
| n4_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 22,1 | 8,0 | 1,2% | 0,0% | 0,0% | 0,163 | 12,9 | 8,6 | 52,2% | 8,89 (28,2%) | 40,8 / 44,4 / 47,4 |
| n4_blefa_nunca_contesta_sempre_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 21,9 | 2,2 | 2,8% | 0,0% | 0,0% | 0,182 | 12,2 | 8,7 | 52,2% | 0,00 (—) | 34,0 / 37,4 / 40,5 |
| n4_todos_blefa_nunca_contesta_sempre | 2000 | 0 | 21,9 | 8,5 | 2,5% | 0,0% | 0,0% | 0,180 | 12,8 | 8,6 | 51,2% | 0,00 (—) | 34,9 / 38,3 / 41,9 |
| n4_blefa_nunca_contesta_sempre_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 21,8 | 5,2 | 3,1% | 0,0% | 0,0% | 0,142 | 12,4 | 8,7 | 52,2% | 0,00 (—) | 34,3 / 37,8 / 41,0 |
| n4_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_nunca | 1000 | 0 | 22,2 | 3,3 | 1,7% | 0,0% | 0,0% | 0,203 | 12,0 | 8,5 | 52,2% | 4,38 (54,5%) | 37,1 / 40,4 / 43,4 |
| n4_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_sempre | 1000 | 0 | 22,2 | 12,1 | 1,5% | 0,0% | 0,0% | 0,183 | 13,5 | 8,8 | 52,2% | 4,24 (0,0%) | 38,7 / 42,3 / 45,7 |
| n4_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_limiar | 1000 | 0 | 22,1 | 8,6 | 1,4% | 0,0% | 0,0% | 0,165 | 12,9 | 8,8 | 52,2% | 4,24 (0,8%) | 37,9 / 41,6 / 44,6 |
| n4_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 22,5 | 4,6 | 1,6% | 0,0% | 0,0% | 0,207 | 12,2 | 8,3 | 52,2% | 9,24 (54,7%) | 40,7 / 44,2 / 46,6 |
| n4_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 21,9 | 15,5 | 2,1% | 0,0% | 0,0% | 0,153 | 14,0 | 8,9 | 52,2% | 8,51 (0,0%) | 42,4 / 46,0 / 49,3 |
| n4_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 21,9 | 12,0 | 2,0% | 0,0% | 0,0% | 0,144 | 13,5 | 8,8 | 52,2% | 8,51 (1,2%) | 41,7 / 45,2 / 48,2 |
| n4_blefa_nunca_contesta_limiar_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 21,9 | 1,2 | 1,9% | 0,0% | 0,0% | 0,191 | 11,9 | 8,6 | 52,2% | 0,00 (—) | 33,9 / 37,2 / 40,2 |
| n4_blefa_nunca_contesta_limiar_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 21,8 | 7,5 | 3,0% | 0,0% | 0,0% | 0,124 | 12,8 | 8,7 | 52,2% | 0,00 (—) | 34,8 / 38,1 / 41,7 |
| n4_todos_blefa_nunca_contesta_limiar | 2000 | 0 | 21,7 | 3,9 | 2,3% | 0,0% | 0,0% | 0,180 | 12,2 | 8,5 | 51,2% | 0,00 (—) | 34,2 / 37,2 / 40,3 |
| n4_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_nunca | 1000 | 0 | 22,2 | 2,4 | 1,3% | 0,0% | 0,0% | 0,211 | 11,8 | 8,5 | 52,2% | 4,38 (55,1%) | 37,1 / 40,2 / 43,1 |
| n4_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_sempre | 1000 | 0 | 22,1 | 10,9 | 2,4% | 0,0% | 0,0% | 0,176 | 13,5 | 8,9 | 52,2% | 4,19 (0,5%) | 38,4 / 42,1 / 45,3 |
| n4_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_limiar | 1000 | 0 | 22,0 | 7,4 | 2,3% | 0,0% | 0,0% | 0,165 | 12,8 | 8,8 | 52,2% | 4,21 (1,4%) | 37,7 / 41,3 / 44,2 |
| n4_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 22,5 | 3,7 | 1,5% | 0,0% | 0,0% | 0,238 | 12,2 | 8,3 | 52,2% | 9,26 (55,3%) | 40,5 / 43,9 / 46,3 |
| n4_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 21,9 | 14,3 | 1,9% | 0,0% | 0,0% | 0,159 | 14,2 | 9,0 | 52,2% | 8,48 (0,6%) | 42,1 / 45,7 / 48,9 |
| n4_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 21,9 | 10,8 | 2,0% | 0,0% | 0,0% | 0,162 | 13,5 | 8,8 | 52,2% | 8,46 (1,7%) | 41,3 / 44,8 / 47,8 |
| n4_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 22,1 | 0,0 | 2,6% | 0,0% | 0,0% | 0,213 | 11,6 | 8,5 | 52,2% | 1,53 (81,1%) | 34,7 / 38,0 / 41,0 |
| n4_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 21,9 | 7,7 | 1,4% | 0,0% | 0,0% | 0,169 | 12,9 | 8,7 | 52,2% | 1,45 (0,0%) | 35,8 / 39,4 / 42,9 |
| n4_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 21,9 | 4,4 | 1,9% | 0,0% | 0,0% | 0,187 | 12,2 | 8,7 | 52,2% | 1,42 (1,4%) | 35,1 / 38,7 / 41,8 |
| n4_todos_blefa_metade_contesta_nunca | 2000 | 0 | 22,3 | 0,0 | 4,0% | 0,0% | 0,0% | 0,216 | 11,1 | 8,1 | 51,2% | 5,81 (81,2%) | 37,3 / 40,7 / 43,3 |
| n4_blefa_metade_contesta_nunca_contra_blefa_metade_contesta_sempre | 1000 | 0 | 22,2 | 10,1 | 1,6% | 0,0% | 0,0% | 0,155 | 13,2 | 8,7 | 52,2% | 5,80 (20,7%) | 39,3 / 43,0 / 46,2 |
| n4_blefa_metade_contesta_nunca_contra_blefa_metade_contesta_limiar | 1000 | 0 | 22,1 | 6,6 | 2,0% | 0,0% | 0,0% | 0,164 | 12,6 | 8,6 | 52,2% | 5,78 (22,2%) | 38,6 / 42,2 / 45,3 |
| n4_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 22,6 | 0,0 | 4,6% | 0,0% | 0,0% | 0,261 | 10,7 | 8,0 | 52,2% | 10,90 (82,0%) | 40,6 / 44,0 / 46,3 |
| n4_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 22,1 | 12,4 | 2,0% | 0,0% | 0,0% | 0,148 | 13,5 | 8,7 | 52,2% | 10,37 (24,0%) | 42,8 / 46,5 / 49,5 |
| n4_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 22,1 | 9,1 | 1,4% | 0,0% | 0,0% | 0,127 | 13,2 | 8,6 | 52,2% | 10,32 (24,8%) | 41,8 / 45,7 / 48,6 |
| n4_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 22,0 | 2,2 | 2,8% | 0,0% | 0,0% | 0,206 | 12,1 | 8,6 | 52,2% | 1,56 (80,6%) | 34,9 / 38,2 / 41,3 |
| n4_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 21,9 | 9,7 | 2,4% | 0,0% | 0,0% | 0,170 | 13,2 | 8,8 | 52,2% | 1,41 (0,0%) | 36,1 / 39,8 / 43,3 |
| n4_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 21,8 | 6,3 | 2,6% | 0,0% | 0,0% | 0,164 | 12,8 | 8,8 | 52,2% | 1,41 (1,7%) | 35,3 / 39,0 / 42,2 |
| n4_blefa_metade_contesta_sempre_contra_blefa_metade_contesta_nunca | 1000 | 0 | 22,3 | 3,4 | 2,8% | 0,0% | 0,0% | 0,230 | 11,9 | 8,4 | 52,2% | 5,83 (61,3%) | 38,3 / 41,4 / 44,2 |
| n4_todos_blefa_metade_contesta_sempre | 2000 | 0 | 21,9 | 13,2 | 1,8% | 0,0% | 0,0% | 0,165 | 13,6 | 8,7 | 51,2% | 5,69 (0,0%) | 39,8 / 43,4 / 47,0 |
| n4_blefa_metade_contesta_sempre_contra_blefa_metade_contesta_limiar | 1000 | 0 | 22,1 | 9,8 | 1,8% | 0,0% | 0,0% | 0,133 | 13,1 | 8,8 | 52,2% | 5,69 (1,0%) | 39,0 / 42,9 / 46,2 |
| n4_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 22,4 | 4,6 | 1,6% | 0,0% | 0,0% | 0,251 | 12,3 | 8,3 | 52,2% | 10,66 (58,3%) | 41,5 / 44,8 / 47,3 |
| n4_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 22,0 | 16,8 | 1,3% | 0,0% | 0,0% | 0,128 | 14,0 | 8,9 | 52,2% | 10,15 (0,0%) | 43,6 / 47,4 / 50,8 |
| n4_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 21,8 | 13,3 | 1,4% | 0,0% | 0,0% | 0,122 | 13,4 | 8,8 | 52,2% | 10,04 (1,3%) | 42,7 / 46,3 / 49,6 |
| n4_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 22,0 | 1,2 | 2,6% | 0,0% | 0,0% | 0,225 | 11,8 | 8,5 | 52,2% | 1,57 (80,9%) | 34,8 / 38,0 / 41,1 |
| n4_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 21,9 | 8,6 | 1,9% | 0,0% | 0,0% | 0,169 | 12,9 | 8,8 | 52,2% | 1,42 (0,0%) | 35,8 / 39,5 / 42,9 |
| n4_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 21,8 | 5,1 | 2,8% | 0,0% | 0,0% | 0,174 | 12,4 | 8,7 | 52,2% | 1,41 (1,6%) | 35,2 / 38,8 / 41,8 |
| n4_blefa_metade_contesta_limiar_contra_blefa_metade_contesta_nunca | 1000 | 0 | 22,2 | 2,4 | 2,7% | 0,0% | 0,0% | 0,223 | 11,8 | 8,4 | 52,2% | 5,84 (61,7%) | 38,0 / 41,2 / 44,0 |
| n4_blefa_metade_contesta_limiar_contra_blefa_metade_contesta_sempre | 1000 | 0 | 22,2 | 12,1 | 2,5% | 0,0% | 0,0% | 0,152 | 13,5 | 8,9 | 52,2% | 5,72 (0,3%) | 39,5 / 43,5 / 46,8 |
| n4_todos_blefa_metade_contesta_limiar | 2000 | 0 | 22,0 | 8,5 | 2,2% | 0,0% | 0,0% | 0,154 | 12,8 | 8,6 | 51,2% | 5,69 (1,6%) | 38,8 / 42,4 / 45,8 |
| n4_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 22,4 | 3,7 | 1,7% | 0,0% | 0,0% | 0,273 | 12,4 | 8,3 | 52,2% | 10,66 (58,8%) | 41,4 / 44,6 / 47,2 |
| n4_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 21,9 | 15,6 | 1,9% | 0,0% | 0,0% | 0,121 | 14,0 | 8,9 | 52,2% | 10,11 (0,4%) | 43,1 / 47,1 / 50,5 |
| n4_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 21,8 | 12,0 | 1,6% | 0,0% | 0,0% | 0,119 | 13,3 | 8,8 | 52,2% | 9,99 (1,8%) | 42,3 / 46,1 / 49,3 |
| n4_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 22,1 | 0,0 | 2,2% | 0,0% | 0,0% | 0,223 | 11,6 | 8,4 | 52,2% | 3,30 (81,9%) | 35,7 / 39,0 / 41,7 |
| n4_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 22,0 | 8,9 | 1,5% | 0,0% | 0,0% | 0,156 | 13,0 | 8,7 | 52,2% | 2,82 (0,0%) | 37,0 / 40,8 / 43,9 |
| n4_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 22,0 | 5,5 | 2,2% | 0,0% | 0,0% | 0,175 | 12,5 | 8,7 | 52,2% | 2,80 (1,3%) | 36,5 / 39,9 / 42,9 |
| n4_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_nunca | 1000 | 0 | 22,3 | 0,0 | 3,7% | 0,0% | 0,0% | 0,231 | 11,1 | 8,2 | 52,2% | 7,61 (81,5%) | 38,7 / 41,7 / 44,3 |
| n4_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_sempre | 1000 | 0 | 22,1 | 11,1 | 1,6% | 0,0% | 0,0% | 0,153 | 13,4 | 8,7 | 52,2% | 7,23 (17,2%) | 40,5 / 44,2 / 47,4 |
| n4_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_limiar | 1000 | 0 | 22,1 | 7,8 | 1,6% | 0,0% | 0,0% | 0,156 | 13,0 | 8,7 | 52,2% | 7,21 (18,7%) | 39,8 / 43,4 / 46,2 |
| n4_todos_blefa_sempre_contesta_nunca | 2000 | 0 | 22,5 | 0,0 | 6,9% | 0,0% | 0,0% | 0,252 | 10,4 | 7,8 | 51,2% | 12,45 (81,6%) | 42,0 / 45,0 / 47,0 |
| n4_blefa_sempre_contesta_nunca_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 22,1 | 13,6 | 1,6% | 0,0% | 0,0% | 0,179 | 13,9 | 8,8 | 52,2% | 11,73 (20,5%) | 44,0 / 47,8 / 50,8 |
| n4_blefa_sempre_contesta_nunca_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 22,1 | 10,3 | 1,2% | 0,0% | 0,0% | 0,149 | 13,6 | 8,7 | 52,2% | 11,66 (21,9%) | 43,2 / 47,0 / 49,8 |
| n4_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 22,1 | 2,2 | 1,7% | 0,0% | 0,0% | 0,199 | 11,8 | 8,5 | 52,2% | 3,36 (81,5%) | 36,1 / 39,4 / 42,3 |
| n4_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 22,0 | 11,0 | 2,2% | 0,0% | 0,0% | 0,152 | 13,5 | 8,8 | 52,2% | 2,83 (0,0%) | 37,3 / 41,2 / 44,3 |
| n4_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 22,0 | 7,4 | 2,3% | 0,0% | 0,0% | 0,164 | 13,2 | 8,8 | 52,2% | 2,85 (1,2%) | 36,8 / 40,3 / 43,3 |
| n4_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_nunca | 1000 | 0 | 22,3 | 3,3 | 3,4% | 0,0% | 0,0% | 0,222 | 11,9 | 8,3 | 52,2% | 7,54 (65,6%) | 39,0 / 42,5 / 45,2 |
| n4_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_sempre | 1000 | 0 | 22,1 | 14,4 | 1,8% | 0,0% | 0,0% | 0,146 | 13,7 | 8,9 | 52,2% | 7,21 (0,0%) | 41,2 / 44,8 / 48,3 |
| n4_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_limiar | 1000 | 0 | 22,0 | 10,9 | 1,7% | 0,0% | 0,0% | 0,138 | 13,4 | 8,8 | 52,2% | 7,15 (1,3%) | 40,3 / 44,1 / 47,3 |
| n4_blefa_sempre_contesta_sempre_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 22,5 | 4,6 | 2,6% | 0,0% | 0,0% | 0,246 | 12,4 | 8,2 | 52,2% | 12,35 (61,9%) | 42,5 / 46,0 / 48,5 |
| n4_todos_blefa_sempre_contesta_sempre | 2000 | 0 | 21,8 | 17,8 | 1,7% | 0,0% | 0,0% | 0,148 | 14,1 | 8,8 | 51,2% | 11,39 (0,0%) | 44,8 / 48,5 / 51,5 |
| n4_blefa_sempre_contesta_sempre_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 21,8 | 14,2 | 1,3% | 0,0% | 0,0% | 0,129 | 13,6 | 8,9 | 52,2% | 11,31 (1,4%) | 43,8 / 47,5 / 50,8 |
| n4_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 22,1 | 1,2 | 2,0% | 0,0% | 0,0% | 0,203 | 11,6 | 8,4 | 52,2% | 3,35 (81,6%) | 35,8 / 39,2 / 42,2 |
| n4_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 22,0 | 9,8 | 1,7% | 0,0% | 0,0% | 0,139 | 13,2 | 8,8 | 52,2% | 2,83 (0,0%) | 37,0 / 40,9 / 43,9 |
| n4_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 22,0 | 6,3 | 2,6% | 0,0% | 0,0% | 0,158 | 12,8 | 8,8 | 52,2% | 2,83 (1,2%) | 36,5 / 40,1 / 43,0 |
| n4_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_nunca | 1000 | 0 | 22,3 | 2,4 | 3,2% | 0,0% | 0,0% | 0,203 | 11,9 | 8,3 | 52,2% | 7,56 (65,9%) | 38,8 / 42,2 / 45,1 |
| n4_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_sempre | 1000 | 0 | 22,1 | 13,3 | 1,6% | 0,0% | 0,0% | 0,132 | 13,5 | 8,8 | 52,2% | 7,20 (0,3%) | 40,8 / 44,7 / 48,0 |
| n4_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_limiar | 1000 | 0 | 22,0 | 9,8 | 1,5% | 0,0% | 0,0% | 0,106 | 13,0 | 8,8 | 52,2% | 7,17 (1,6%) | 40,2 / 43,8 / 46,8 |
| n4_blefa_sempre_contesta_limiar_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 22,5 | 3,7 | 2,2% | 0,0% | 0,0% | 0,251 | 12,6 | 8,2 | 52,2% | 12,37 (62,5%) | 42,2 / 45,8 / 48,2 |
| n4_blefa_sempre_contesta_limiar_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 21,8 | 16,7 | 1,4% | 0,0% | 0,0% | 0,163 | 14,0 | 8,9 | 52,2% | 11,42 (0,5%) | 44,5 / 48,2 / 51,5 |
| n4_todos_blefa_sempre_contesta_limiar | 2000 | 0 | 21,8 | 13,0 | 1,8% | 0,0% | 0,0% | 0,139 | 13,3 | 8,7 | 51,2% | 11,29 (1,6%) | 43,5 / 47,2 / 50,2 |
| n5_todos_blefa_nunca_contesta_nunca | 2000 | 0 | 28,2 | 0,0 | 3,5% | 7,6% | 0,0% | 0,184 | 12,1 | 8,6 | 51,1% | 0,00 (—) | 39,4 / 42,4 / 45,8 |
| n5_blefa_nunca_contesta_nunca_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 28,2 | 8,6 | 2,4% | 6,5% | 0,0% | 0,166 | 13,4 | 8,7 | 48,9% | 0,00 (—) | 40,3 / 44,1 / 47,6 |
| n5_blefa_nunca_contesta_nunca_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 28,1 | 4,1 | 2,7% | 6,5% | 0,0% | 0,186 | 12,8 | 8,6 | 48,9% | 0,00 (—) | 39,8 / 42,9 / 46,2 |
| n5_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_nunca | 1000 | 0 | 28,6 | 0,0 | 4,5% | 6,1% | 0,0% | 0,175 | 11,7 | 8,3 | 48,9% | 6,21 (81,6%) | 43,1 / 46,4 / 49,4 |
| n5_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_sempre | 1000 | 0 | 28,3 | 12,1 | 2,1% | 5,3% | 0,0% | 0,137 | 13,7 | 8,8 | 48,9% | 6,06 (19,9%) | 44,8 / 48,9 / 52,5 |
| n5_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_limiar | 1000 | 0 | 28,3 | 7,5 | 2,8% | 5,3% | 0,0% | 0,145 | 13,1 | 8,7 | 48,9% | 6,00 (21,4%) | 44,1 / 47,8 / 51,2 |
| n5_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 28,9 | 0,0 | 6,6% | 6,8% | 0,0% | 0,209 | 11,1 | 8,0 | 48,9% | 13,41 (80,8%) | 47,4 / 51,1 / 53,4 |
| n5_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 28,4 | 16,1 | 2,5% | 6,4% | 0,0% | 0,134 | 13,9 | 8,7 | 48,9% | 12,50 (20,0%) | 50,5 / 54,4 / 57,6 |
| n5_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 28,4 | 11,3 | 2,6% | 6,1% | 0,0% | 0,179 | 13,5 | 8,6 | 48,9% | 12,46 (22,2%) | 49,6 / 53,2 / 56,0 |
| n5_blefa_nunca_contesta_sempre_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 28,2 | 2,3 | 3,3% | 6,6% | 0,0% | 0,150 | 12,7 | 8,7 | 48,9% | 0,00 (—) | 39,3 / 42,9 / 46,2 |
| n5_todos_blefa_nunca_contesta_sempre | 2000 | 0 | 28,2 | 10,6 | 1,8% | 7,3% | 0,0% | 0,147 | 13,4 | 8,7 | 51,1% | 0,00 (—) | 40,9 / 44,5 / 48,1 |
| n5_blefa_nunca_contesta_sempre_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 28,1 | 6,0 | 2,8% | 6,4% | 0,0% | 0,185 | 13,0 | 8,6 | 48,9% | 0,00 (—) | 40,3 / 43,2 / 46,9 |
| n5_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_nunca | 1000 | 0 | 28,4 | 3,3 | 2,8% | 6,2% | 0,0% | 0,185 | 12,4 | 8,5 | 48,9% | 6,10 (61,1%) | 43,8 / 46,8 / 50,2 |
| n5_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_sempre | 1000 | 0 | 28,2 | 15,2 | 2,1% | 5,7% | 0,0% | 0,132 | 14,2 | 8,9 | 48,9% | 6,07 (0,0%) | 45,2 / 49,6 / 53,5 |
| n5_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_limiar | 1000 | 0 | 28,1 | 10,5 | 2,6% | 5,7% | 0,0% | 0,123 | 13,5 | 8,8 | 48,9% | 5,94 (2,2%) | 44,5 / 48,3 / 51,9 |
| n5_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 28,7 | 4,7 | 3,1% | 6,2% | 0,0% | 0,199 | 12,4 | 8,3 | 48,9% | 13,10 (60,8%) | 48,8 / 52,0 / 54,6 |
| n5_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 28,3 | 20,5 | 1,8% | 5,3% | 0,0% | 0,128 | 14,8 | 9,0 | 48,9% | 12,15 (0,0%) | 51,5 / 55,3 / 58,3 |
| n5_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 28,2 | 15,5 | 1,6% | 4,9% | 0,0% | 0,125 | 14,1 | 8,9 | 48,9% | 12,13 (2,0%) | 50,4 / 53,9 / 57,1 |
| n5_blefa_nunca_contesta_limiar_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 28,2 | 1,2 | 3,7% | 6,0% | 0,0% | 0,170 | 12,5 | 8,6 | 48,9% | 0,00 (—) | 39,2 / 42,7 / 45,8 |
| n5_blefa_nunca_contesta_limiar_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 28,2 | 9,5 | 1,9% | 6,9% | 0,0% | 0,195 | 13,4 | 8,7 | 48,9% | 0,00 (—) | 40,6 / 44,1 / 48,0 |
| n5_todos_blefa_nunca_contesta_limiar | 2000 | 0 | 28,1 | 4,8 | 3,1% | 7,4% | 0,0% | 0,161 | 12,6 | 8,6 | 51,1% | 0,00 (—) | 40,0 / 43,1 / 46,2 |
| n5_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_nunca | 1000 | 0 | 28,5 | 2,4 | 3,0% | 6,0% | 0,0% | 0,161 | 12,2 | 8,4 | 48,9% | 6,05 (61,6%) | 43,6 / 46,6 / 50,0 |
| n5_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_sempre | 1000 | 0 | 28,2 | 14,1 | 2,7% | 5,7% | 0,0% | 0,159 | 14,2 | 8,9 | 48,9% | 6,02 (0,5%) | 44,9 / 49,3 / 53,1 |
| n5_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_limiar | 1000 | 0 | 28,2 | 9,3 | 2,5% | 5,6% | 0,0% | 0,157 | 13,4 | 8,8 | 48,9% | 5,92 (3,0%) | 44,4 / 48,1 / 51,7 |
| n5_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 28,7 | 3,8 | 3,5% | 6,4% | 0,0% | 0,226 | 12,4 | 8,3 | 48,9% | 13,10 (61,0%) | 48,5 / 51,8 / 54,1 |
| n5_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 28,3 | 19,2 | 2,5% | 5,5% | 0,0% | 0,128 | 14,8 | 9,0 | 48,9% | 12,15 (0,6%) | 51,2 / 55,0 / 58,0 |
| n5_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 28,2 | 14,2 | 1,9% | 4,8% | 0,0% | 0,150 | 14,0 | 8,9 | 48,9% | 12,14 (2,8%) | 50,2 / 53,7 / 56,5 |
| n5_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 28,4 | 0,0 | 4,4% | 5,6% | 0,0% | 0,167 | 12,1 | 8,5 | 48,9% | 1,59 (82,6%) | 40,1 / 43,4 / 46,4 |
| n5_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 28,3 | 9,8 | 2,2% | 5,9% | 0,0% | 0,156 | 13,5 | 8,7 | 48,9% | 1,47 (0,0%) | 41,8 / 45,4 / 48,9 |
| n5_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 28,2 | 5,2 | 2,4% | 6,1% | 0,0% | 0,164 | 12,9 | 8,7 | 48,9% | 1,44 (2,6%) | 41,0 / 44,3 / 47,4 |
| n5_todos_blefa_metade_contesta_nunca | 2000 | 0 | 28,6 | 0,0 | 4,1% | 7,3% | 0,0% | 0,231 | 11,5 | 8,2 | 51,1% | 7,66 (81,6%) | 44,1 / 47,4 / 50,1 |
| n5_blefa_metade_contesta_nunca_contra_blefa_metade_contesta_sempre | 1000 | 0 | 28,2 | 13,2 | 2,7% | 5,3% | 0,0% | 0,174 | 13,9 | 8,8 | 48,9% | 7,68 (16,4%) | 45,9 / 50,1 / 53,8 |
| n5_blefa_metade_contesta_nunca_contra_blefa_metade_contesta_limiar | 1000 | 0 | 28,3 | 8,7 | 2,6% | 5,3% | 0,0% | 0,170 | 13,4 | 8,7 | 48,9% | 7,50 (17,9%) | 45,3 / 49,0 / 52,4 |
| n5_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 28,8 | 0,0 | 7,6% | 6,8% | 0,0% | 0,222 | 10,9 | 7,9 | 48,9% | 14,65 (80,9%) | 48,8 / 51,8 / 54,1 |
| n5_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 28,4 | 17,1 | 2,2% | 6,3% | 0,0% | 0,177 | 14,2 | 8,8 | 48,9% | 14,02 (18,2%) | 51,9 / 55,7 / 58,8 |
| n5_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 28,3 | 12,4 | 2,3% | 5,6% | 0,0% | 0,189 | 13,8 | 8,7 | 48,9% | 13,86 (20,2%) | 50,7 / 54,4 / 57,3 |
| n5_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 28,4 | 2,3 | 2,5% | 6,5% | 0,0% | 0,167 | 12,5 | 8,6 | 48,9% | 1,62 (82,8%) | 40,3 / 43,9 / 47,2 |
| n5_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 28,2 | 11,8 | 1,8% | 6,5% | 0,0% | 0,182 | 13,7 | 8,8 | 48,9% | 1,49 (0,0%) | 42,0 / 45,7 / 49,3 |
| n5_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 28,1 | 7,1 | 3,2% | 6,3% | 0,0% | 0,188 | 13,2 | 8,7 | 48,9% | 1,45 (3,2%) | 41,2 / 44,6 / 48,1 |
| n5_blefa_metade_contesta_sempre_contra_blefa_metade_contesta_nunca | 1000 | 0 | 28,6 | 3,3 | 3,2% | 5,6% | 0,0% | 0,208 | 12,3 | 8,4 | 48,9% | 7,65 (65,9%) | 44,6 / 47,9 / 51,1 |
| n5_todos_blefa_metade_contesta_sempre | 2000 | 0 | 28,2 | 16,8 | 1,7% | 7,4% | 0,0% | 0,152 | 14,2 | 8,8 | 51,1% | 7,60 (0,0%) | 47,2 / 51,2 / 55,0 |
| n5_blefa_metade_contesta_sempre_contra_blefa_metade_contesta_limiar | 1000 | 0 | 28,1 | 11,7 | 2,8% | 5,4% | 0,0% | 0,184 | 13,8 | 8,8 | 48,9% | 7,51 (2,3%) | 45,7 / 49,7 / 53,1 |
| n5_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 28,7 | 4,7 | 3,7% | 5,5% | 0,0% | 0,206 | 12,5 | 8,2 | 48,9% | 14,49 (62,4%) | 49,7 / 52,8 / 55,3 |
| n5_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 28,2 | 21,6 | 1,3% | 5,7% | 0,0% | 0,143 | 14,8 | 9,0 | 48,9% | 13,60 (0,0%) | 52,9 / 56,6 / 59,6 |
| n5_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 28,2 | 16,5 | 2,3% | 5,4% | 0,0% | 0,145 | 14,1 | 8,9 | 48,9% | 13,54 (2,2%) | 51,7 / 55,2 / 58,3 |
| n5_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 28,3 | 1,2 | 2,9% | 6,4% | 0,0% | 0,167 | 12,3 | 8,6 | 48,9% | 1,61 (83,0%) | 40,2 / 43,6 / 46,7 |
| n5_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 28,2 | 10,7 | 2,5% | 6,1% | 0,0% | 0,163 | 13,5 | 8,7 | 48,9% | 1,49 (0,0%) | 41,8 / 45,4 / 49,1 |
| n5_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 28,1 | 5,9 | 3,0% | 6,2% | 0,0% | 0,181 | 12,9 | 8,7 | 48,9% | 1,44 (3,2%) | 41,1 / 44,3 / 47,6 |
| n5_blefa_metade_contesta_limiar_contra_blefa_metade_contesta_nunca | 1000 | 0 | 28,6 | 2,3 | 2,7% | 5,8% | 0,0% | 0,207 | 12,2 | 8,4 | 48,9% | 7,63 (66,4%) | 44,3 / 47,7 / 50,8 |
| n5_blefa_metade_contesta_limiar_contra_blefa_metade_contesta_sempre | 1000 | 0 | 28,1 | 15,3 | 3,7% | 5,5% | 0,0% | 0,145 | 14,2 | 8,9 | 48,9% | 7,65 (0,5%) | 46,4 / 50,5 / 53,9 |
| n5_todos_blefa_metade_contesta_limiar | 2000 | 0 | 28,2 | 10,6 | 2,2% | 6,9% | 0,0% | 0,173 | 13,4 | 8,7 | 51,1% | 7,50 (2,7%) | 45,9 / 49,6 / 53,0 |
| n5_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 28,7 | 3,8 | 3,0% | 6,0% | 0,0% | 0,228 | 12,6 | 8,2 | 48,9% | 14,39 (62,9%) | 49,3 / 52,5 / 55,1 |
| n5_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 28,2 | 20,4 | 1,5% | 6,3% | 0,0% | 0,154 | 14,8 | 9,0 | 48,9% | 13,61 (0,5%) | 52,7 / 56,2 / 59,2 |
| n5_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 28,1 | 15,2 | 1,2% | 5,4% | 0,0% | 0,162 | 14,0 | 8,9 | 48,9% | 13,48 (3,0%) | 51,5 / 54,8 / 57,8 |
| n5_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 28,5 | 0,0 | 3,8% | 5,8% | 0,0% | 0,163 | 12,0 | 8,5 | 48,9% | 3,60 (81,9%) | 41,4 / 44,8 / 47,8 |
| n5_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 28,3 | 11,0 | 2,5% | 4,6% | 0,0% | 0,170 | 13,6 | 8,7 | 48,9% | 2,98 (0,0%) | 43,2 / 46,7 / 50,4 |
| n5_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 28,2 | 6,4 | 3,0% | 5,4% | 0,0% | 0,157 | 13,1 | 8,7 | 48,9% | 2,94 (2,3%) | 42,4 / 45,6 / 48,7 |
| n5_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_nunca | 1000 | 0 | 28,7 | 0,0 | 4,2% | 5,9% | 0,0% | 0,194 | 11,4 | 8,2 | 48,9% | 9,58 (81,8%) | 45,1 / 48,4 / 51,1 |
| n5_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_sempre | 1000 | 0 | 28,4 | 14,6 | 1,7% | 6,1% | 0,0% | 0,144 | 14,2 | 8,8 | 48,9% | 9,17 (13,5%) | 48,0 / 51,7 / 55,2 |
| n5_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_limiar | 1000 | 0 | 28,4 | 9,9 | 2,1% | 6,4% | 0,0% | 0,179 | 13,7 | 8,7 | 48,9% | 8,99 (15,8%) | 46,9 / 50,5 / 53,9 |
| n5_todos_blefa_sempre_contesta_nunca | 2000 | 0 | 28,9 | 0,0 | 7,6% | 9,2% | 0,0% | 0,204 | 10,7 | 7,8 | 51,1% | 16,50 (81,5%) | 49,8 / 52,8 / 54,8 |
| n5_blefa_sempre_contesta_nunca_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 28,5 | 18,5 | 2,2% | 6,4% | 0,0% | 0,182 | 14,5 | 8,8 | 48,9% | 15,47 (16,3%) | 53,5 / 57,2 / 59,8 |
| n5_blefa_sempre_contesta_nunca_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 28,3 | 13,6 | 1,7% | 5,9% | 0,0% | 0,192 | 14,2 | 8,7 | 48,9% | 15,30 (18,4%) | 52,2 / 55,8 / 58,2 |
| n5_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 28,4 | 2,2 | 3,5% | 6,4% | 0,0% | 0,167 | 12,2 | 8,5 | 48,9% | 3,63 (81,2%) | 41,9 / 45,1 / 48,2 |
| n5_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 28,2 | 13,0 | 1,8% | 4,5% | 0,0% | 0,182 | 14,0 | 8,8 | 48,9% | 3,04 (0,0%) | 43,5 / 47,1 / 50,6 |
| n5_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 28,1 | 8,3 | 2,8% | 5,6% | 0,0% | 0,179 | 13,5 | 8,8 | 48,9% | 2,99 (3,2%) | 42,8 / 45,8 / 49,2 |
| n5_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_nunca | 1000 | 0 | 28,6 | 3,4 | 2,1% | 4,9% | 0,0% | 0,207 | 12,2 | 8,3 | 48,9% | 9,55 (68,5%) | 45,7 / 49,2 / 52,1 |
| n5_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_sempre | 1000 | 0 | 28,4 | 17,9 | 1,4% | 5,7% | 0,0% | 0,168 | 14,5 | 8,9 | 48,9% | 9,17 (0,0%) | 48,4 / 52,6 / 56,1 |
| n5_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_limiar | 1000 | 0 | 28,3 | 13,0 | 2,7% | 5,8% | 0,0% | 0,150 | 14,1 | 8,9 | 48,9% | 9,00 (2,3%) | 47,3 / 51,3 / 54,8 |
| n5_blefa_sempre_contesta_sempre_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 28,8 | 4,7 | 3,0% | 6,2% | 0,0% | 0,249 | 12,7 | 8,1 | 48,9% | 16,21 (64,8%) | 51,0 / 54,0 / 56,2 |
| n5_todos_blefa_sempre_contesta_sempre | 2000 | 0 | 28,2 | 23,0 | 1,3% | 6,6% | 0,0% | 0,146 | 14,7 | 8,9 | 51,1% | 15,19 (0,0%) | 54,0 / 58,0 / 61,0 |
| n5_blefa_sempre_contesta_sempre_contra_blefa_sempre_contesta_limiar | 1000 | 0 | 28,1 | 17,7 | 1,9% | 5,8% | 0,0% | 0,163 | 14,3 | 8,9 | 48,9% | 14,98 (2,4%) | 52,8 / 56,8 / 59,5 |
| n5_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_nunca | 1000 | 0 | 28,4 | 1,2 | 2,8% | 6,9% | 0,0% | 0,174 | 12,0 | 8,5 | 48,9% | 3,66 (81,2%) | 41,7 / 44,9 / 47,9 |
| n5_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_sempre | 1000 | 0 | 28,2 | 11,9 | 1,7% | 4,4% | 0,0% | 0,191 | 13,8 | 8,8 | 48,9% | 3,02 (0,0%) | 43,3 / 46,8 / 50,4 |
| n5_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_limiar | 1000 | 0 | 28,1 | 7,0 | 3,4% | 5,7% | 0,0% | 0,168 | 13,2 | 8,7 | 48,9% | 2,98 (3,0%) | 42,5 / 45,5 / 48,8 |
| n5_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_nunca | 1000 | 0 | 28,6 | 2,4 | 2,6% | 4,8% | 0,0% | 0,215 | 12,2 | 8,3 | 48,9% | 9,56 (68,8%) | 45,5 / 48,9 / 51,8 |
| n5_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_sempre | 1000 | 0 | 28,3 | 16,7 | 1,5% | 5,6% | 0,0% | 0,163 | 14,3 | 8,9 | 48,9% | 9,14 (0,5%) | 48,3 / 52,2 / 55,7 |
| n5_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_limiar | 1000 | 0 | 28,3 | 11,7 | 2,9% | 5,8% | 0,0% | 0,142 | 13,8 | 8,8 | 48,9% | 8,99 (3,1%) | 47,2 / 51,0 / 54,3 |
| n5_blefa_sempre_contesta_limiar_contra_blefa_sempre_contesta_nunca | 1000 | 0 | 28,8 | 3,7 | 3,2% | 6,6% | 0,0% | 0,270 | 12,9 | 8,1 | 48,9% | 16,15 (65,1%) | 50,8 / 53,8 / 55,8 |
| n5_blefa_sempre_contesta_limiar_contra_blefa_sempre_contesta_sempre | 1000 | 0 | 28,2 | 21,7 | 2,3% | 5,9% | 0,0% | 0,174 | 14,7 | 9,0 | 48,9% | 15,09 (0,6%) | 53,8 / 57,5 / 60,5 |
| n5_todos_blefa_sempre_contesta_limiar | 2000 | 0 | 28,2 | 16,6 | 1,8% | 7,3% | 0,0% | 0,129 | 13,9 | 8,7 | 51,1% | 15,15 (2,7%) | 52,8 / 56,5 / 59,0 |

## Cenários

| Cenário | Regras | Jogadores | Bots | Hash da configuração |
|---|---|---|---|---|
| n4_todos_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_nunca_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_nunca_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_sempre_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_todos_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_sempre_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_limiar_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_limiar_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_todos_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_todos_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_nunca_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_nunca_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_sempre_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_todos_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_sempre_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_limiar_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_limiar_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_todos_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_todos_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_nunca_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_nunca_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_sempre_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_todos_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_sempre_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_limiar_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n4_blefa_sempre_contesta_limiar_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n4_todos_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 4 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_nunca_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_nunca_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_nunca_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_nunca_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_sempre_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_sempre_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_sempre_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_sempre_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_limiar_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_limiar_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_limiar_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_nunca_contesta_limiar_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_nunca_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_nunca_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_nunca_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_nunca_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_sempre_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_sempre_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_sempre_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_sempre_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_limiar_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_limiar_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_limiar_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_metade_contesta_limiar_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_nunca_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_nunca_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_nunca_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_nunca_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_sempre_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_sempre_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_sempre_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_sempre_contra_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_limiar_contra_blefa_nunca_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'nunca', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'nunca'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'sempre'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_limiar_contra_blefa_metade_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'metade', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_limiar_contra_blefa_sempre_contesta_nunca (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'nunca'} | `sha256:60ad08b41b4c` |
| n5_blefa_sempre_contesta_limiar_contra_blefa_sempre_contesta_sempre (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'}; heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'sempre'} | `sha256:60ad08b41b4c` |
| n5_todos_blefa_sempre_contesta_limiar (rotações somadas) | v2.2.1 | 5 | heuristico {'conhecimento': 'experiente', 'blefe': 'sempre', 'contestacao': 'limiar'} | `sha256:60ad08b41b4c` |

## Como refazer

No commit `b02b6d4`: `cf experimento experimentos/fase4_exp5_blefe.yaml --oficial --processos 4`. O resultado não depende do número de processos.

# Resumo dos resultados do simulador

Situação em 14/11/2026, depois do commit `7953e75`. As regras vigentes são as da **v2.2.1**.

Cada número vem do `docs/DIARIO_DE_BORDO.md` e dos relatórios em `resultados/<experimento>/<execução>/relatorio.md`, que registram o commit, a semente e o hash das regras. As **sugestões de mudança de regra** (seção 5) são propostas para o autor decidir. Nenhuma delas foi aplicada.

---

## 1. Respostas curtas

| Pergunta | Resposta |
|---|---|
| Qual é o melhor estilo? | **O Heurístico**, que mistura construir e atacar conforme o valor de cada jogada. O Construtor fica logo atrás. Os Caçadores puros perdem para os dois. |
| O jogo está balanceado? | **Em grande parte, sim.** De 13 requisitos confirmados, 9 passam com folga, 3 passam só em parte e 1 falha: o tempo parado. |
| A v2 resolveu a bola de neve da v1? | **Sim.** A vantagem de quem lidera depois do ciclo 1 cai de cerca de 0,40 na v1 para cerca de 0,09 na v2.2.1. |
| O blefe funciona como o PDF pede? | **Sim.** Nenhum perfil de blefe domina. No equilíbrio, cerca de 39% dos blefes dão certo, dentro da faixa de 30% a 50%. |
| Testes sem limite dão um jogo mais profundo? | **Sim.** É a regra com mais decisões, mais defesas, menos vantagem do líder e mais retorno para quem joga bem. |
| Todas as fases terminaram? | **Sim**, da Fase 0 à 5 (seção 8). O que falta são decisões do autor e o playtest. |

---

## 2. O que foi feito

| Fase | Entrega |
|---|---|
| 0 | Especificação da v2.2 e da v1 em itens numerados, ambiguidades (AMB-01 a AMB-32), requisitos com zona de aceite, convenções e diário |
| 1 | Motor puro e determinístico da v2, registro de auditoria (`cf-audit/1`), `replay`, `narrar`, `folha`, bot Aleatório, testes por regra e de propriedades, CI |
| 1b | Executor paralelo com Parquet e manifest, primeiras métricas com intervalo de confiança |
| 2 | Bots com estilo (Construtor, Caçador com 3 políticas de alvo, Heurístico) e perfis de conhecimento, blefe e contestação |
| 3 | Motor da v1; Experimento 1 (validação da v1) e Experimento 2 (v1 contra v2.2.1) |
| 4 | Melhor estilo; Experimentos 3 (ablação), 4 e 4b (sensibilidade e combinações), 5 e 5b (blefe), 6 (variantes do playtest) e 7 (profundidade) |
| 5 | Testes metamórficos, fuzzing, teste de mutação e suíte noturna |

**Volume:** 12 execuções oficiais, **891.000 partidas, nenhuma falha.** Todas rodaram com a árvore do git limpa e podem ser refeitas pela semente.

---

## 3. Principais achados

### 3.1 v1 contra v2.2.1 (Experimentos 1 e 2)

- **A v1 do simulador reproduz a bola de neve do artigo.** Quem lidera depois de todos fazerem o primeiro teste vence entre 49% e 78% das partidas, conforme a população de bots.
- **A v2.2.1 quase não tem bola de neve.** Vantagem do líder (REQ-02): 0,392 na v1 contra 0,087 na v2.2.1 com 4 jogadores, e 0,419 contra 0,091 com 5.
- **Pelo critério fixado antes, a v1 do simulador é ainda mais desequilibrada que as 6 partidas do artigo.** Mais de 95% das partidas são desequilibradas com o fator 1,5, contra 4 de 6 no artigo. Com o fator 2,0, as populações mais parecidas com alunos ficam dentro do intervalo do artigo.
- **A política de alvo se inverte entre as versões.** Na v1, escolher o alvo ao acaso é a melhor resposta, porque atacar o líder lhe entrega a carta de ataque quando ele se defende. Na v2.2.1, atacar o líder é o melhor, e atacar o mais fraco é o pior.
- **A v1 deixa os estilos mais próximos. A v2.2.1 tirou a bola de neve, mas afastou construir de caçar.** Com 4 jogadores, o Construtor sobe de 0,323 para 0,455, e o Caçador cai de 0,260 para 0,173. A referência é 0,250.

### 3.2 Melhor estilo (Fase 4)

Matriz de 6 estilos, com 4 e 5 jogadores e 140.000 partidas.

- **O Heurístico é a melhor resposta** contra todas as mesas, menos a de Aleatórios, onde o Construtor rende um pouco mais. A dinâmica do replicador termina em 100% de Heurísticos.
- **Construir vence caçar.** Nenhum Caçador é melhor resposta a mesa alguma, salvo a de Aleatórios. Contra Construtores, um Caçador vence de 0,13 a 0,17 com 4 jogadores, para uma referência de 0,25.
- **Os dois estilos aparecem dentro do jogo de quem joga bem (REQ-11).** O Heurístico enche o sistema no 1º Planejamento em cerca de 51% das partidas. Nas outras, guarda cartas para testar. O "estilo" vira uma decisão de cada partida, não um tipo de jogador.
- **Habilidade importa (REQ-03).** O Heurístico vence 0,94 contra Aleatórios com 4 jogadores. O piso era 0,375.

### 3.3 Blefe (Experimentos 5 e 5b)

- **Os perfis de blefe formam um ciclo:** blefar sempre ganha de quem nunca contesta; contestar pelo limiar ganha de quem blefa; não contestar ganha numa mesa de honestos.
- **O equilíbrio é misto.** Cerca de 1 em cada 6 jogadores blefa sempre, e o perfil mais comum é "nunca blefa, contesta pelo limiar".
- **REQ-05 passa:** 0,395 dos blefes dão certo com 4 jogadores e 0,385 com 5, no meio da faixa de 0,30 a 0,50.
- **A duração depende muito de quanto a mesa contesta.** No equilíbrio há cerca de 3 contestações por partida, contra 9,5 com o blefe moderado, e a partida encurta de 7 a 10 minutos (de 45,7 para 38,7 min com 4 jogadores e de 55,1 para 44,6 com 5).

### 3.4 Requisitos de balanceamento da v2.2.1

Valores das mesas de Heurísticos sorteadas do equilíbrio do blefe (Experimentos 3, 4, 6 e 7).

| Requisito | Resultado | Valor medido | Zona |
|---|---|---|---|
| REQ-01 Equidade de assento | **em parte** | Com Aleatórios, todas as posições dentro (de 0,248 a 0,253 com 4 jogadores). Com Heurísticos, o 1º vence 0,276 e o último 0,224, na borda | 1/N ± 0,02 |
| REQ-02 Anti bola de neve | **passa** | v1 cerca de 0,40, v2.2.1 cerca de 0,09 | v2 menor que a v1 por ≥ 0,05 |
| REQ-03 Habilidade importa | **passa** | 0,94 e 0,93 | acima de 1,5/N |
| REQ-04 Sem estratégia dominante | **passa** | nenhum estilo nem perfil de blefe domina | — |
| REQ-05 Blefes bem-sucedidos | **passa** | 0,395 e 0,385 | 0,30 a 0,50 |
| REQ-06 Distribuição de ataques | **passa** | razão de 1,35 a 1,43; fração contra o menor de 0,34 a 0,43, perto do limite com experientes (alguns cenários inconclusivos) | até 1,5; até 1/(N−1) + 0,10 |
| REQ-07 Fichas não zeram cedo | **passa** | de 0,03 a 0,08 | até 0,10 |
| REQ-08 Duração | **em parte** | 5 jogadores: 44 min (passa). 4 jogadores: 38 min (**curta demais**) | mediana de 40 a 50 min |
| REQ-09 Robustez | **passa** | 0 falhas em 891.000 partidas | 0 em ≥ 50.000 |
| REQ-10 Tempo parado | **falha** | percentil 90 de 5,8 min (4 jogadores) e 9,0 min (5) | abaixo de 5 min |
| REQ-11 Os dois estilos aparecem | **passa** | de 0,50 a 0,58 | 0,10 a 0,90 |
| REQ-12 1º incidente não decide | **passa** | de 0,03 a 0,08 | até 0,10 |
| REQ-13 Incidentes pesam | **em parte** | iniciantes de 0,21 a 0,22 (passa); experientes 0,17 (**falha**) | 0,20 a 0,60 |

O REQ-08 e o REQ-10 dependem dos tempos do modelo de duração (MOD-05), que ainda são provisórios. Com todos os tempos 25% maiores, a mesa de 4 passa a durar 48 min. Com todos 25% menores, o tempo parado com 4 jogadores passa (4,3 min). O que não depende dos tempos: **a mesa de 5 dura cerca de 15% mais que a de 4 e fica cerca de 55% mais tempo parada.**

### 3.5 Variantes do playtest (Experimento 6)

**Nenhuma variante melhora tudo, e a regra atual é a melhor das 10 configurações no conjunto.**

| Variante | Efeito |
|---|---|
| VAR-01 (punição de 0 ou 2 fichas) | quase nada muda |
| VAR-02 (custo extra da explicação) | iniciantes zeram cedo: REQ-07 de 0,19 a 0,21 (falha) |
| VAR-03 (Auditor externo) | piora o tempo parado: 7,3 min com 4 jogadores |
| VAR-04 (vizinho designado) | encurta a partida e o tempo parado, mas concentra os testes e deixa a partida curta demais |
| VAR-05 (limite de 2 testes) | encurta a partida, mas os testes se concentram no menor placar com 5 jogadores |
| VAR-06 (palpite da plateia) | nada muda no que o bot mede; o efeito no engajamento só se mede com pessoas |
| VAR-07 (2 compras) | torna o REQ-11 impossível (ninguém chega a 5 cartas no ciclo 1); partida de 30 a 34 min |
| VAR-09 (módulo de Segurança Operacional) | quase nada muda |

### 3.6 Ablação: as mudanças da 2.2 se justificam (Experimento 3)

| Mudança desfeita | O que acontece |
|---|---|
| COR-01 (máximo de 5 jogadores) | com 6 jogadores: 51 min e 12 min parado por ciclo; falta carta em 0,1% das partidas |
| COR-02 (Alertas saem no Planejamento) | muda pouco; nenhum veredito vira |
| Bug duplicado proibido | com a regra da 2.1, os ataques se concentram (REQ-06a falha com 5 experientes) |
| Testes sem limite | com 1 teste por ciclo (2.1), o tempo parado passa, mas a partida cai para 28 a 32 min e os ataques se concentram no menor placar |

**Cada mudança da v2.2, quando desfeita, piora algum requisito ou não melhora nenhum.**

### 3.7 Fichas iniciais e dano de incidente (Experimentos 4 e 4b)

- **5 fichas é o mínimo que passa no REQ-07.** Com 3 fichas, de 34% a 52% das partidas têm alguém zerado antes do ciclo 3; com 4, de 13% a 23%; com 5, de 4% a 8%; com 6, de 1% a 2%. O PDF acertou o mínimo, e 6 dariam folga.
- **O REQ-07 e o REQ-13 puxam para lados opostos, e o conflito é entre públicos.** Quem sabe o conteúdo se cobre e sofre pouco dano; quem não sabe sofre muito. Um dano que pesa para o experiente zera o iniciante.
- **Nenhuma combinação de fichas (5, 6) e dano sem cobertura (2, 3) satisfaz os dois públicos.** Com 6 fichas e dano 3, os experientes passam, mas os iniciantes zeram cedo (de 0,15 a 0,17).

### 3.8 Profundidade (Experimento 7)

Quatro regras comparadas: a atual (sem limite), 1 teste por ciclo, 2 testes por ciclo e custo de 1 ficha do 2º teste em diante (VAR-12).

| Regra | Duração (4 / 5 jog.) | Defesas por jogador | Decisões por jogador | Vantagem do líder | Recuperação | Habilidade em degraus, T=4 (4 / 5 jog.) |
|---|---|---|---|---|---|---|
| **Sem limite (atual)** | 38 / 44 min | **5,5** | **33** | **0,15 a 0,19** | **0,56 a 0,63** | **1,88 / 2,10** |
| 2 testes por ciclo | 33 / 38 min | 4,0 | 28 | 0,18 a 0,21 | 0,54 a 0,60 | 1,68 / 1,92 |
| Custo do teste | 34 / 39 min | 4,1 | 30 | 0,18 a 0,22 | 0,54 a 0,61 | 1,86 / 2,10 |
| 1 teste por ciclo | 28 / 32 min | 2,2 | 22 | 0,22 a 0,27 | 0,52 a 0,58 | 1,60 / 1,78 |

- **A intuição do autor se confirma: testes sem limite dão o jogo mais profundo.** 1 teste por ciclo é a regra mais rasa em todas as medidas.
- **Os meios-termos ficam no meio, e nenhum resolve tudo.** 2 testes por ciclo e o custo do teste encurtam a partida em cerca de 5 min e passam no tempo parado com 4 jogadores, mas não com 5. O custo do teste preserva a habilidade, mas zera mais jogadores (REQ-07 falha com iniciantes).
- **A fração de escolhas apertadas não separa as regras** (de 0,79 a 0,85 em todas). Com o limiar de 0,5 ficha, quase toda decisão do Heurístico conta como apertada.

### 3.9 Outros achados

- **Efeito de vizinho:** o Heurístico vence de 1,6 a 4,3 pontos percentuais a mais quando joga logo depois de um Aleatório do que logo depois de um Construtor. O Backlog é comprado em sequência, e quem joga antes muda o que sobra. É uma propriedade do jogo e é medido toda noite.
- **Vantagem da ordem com bots que jogam bem:** com 4 Heurísticos, as posições vencem 0,276, 0,256, 0,244 e 0,224, uma queda contínua do 1º ao último. Uma explicação provável, mas não medida: o 1º escolhe primeiro no Backlog do ciclo 1, e, com 3 ciclos e 4 ou 5 jogadores, o marcador de primeiro jogador não passa por todos.
- **Contestar pelo limiar pega quase todo blefe** (só de 1,6% a 2,7% passam), porque os bots contam as cartas já vistas. Pessoas contam pior. A taxa real deve ficar entre esse número e os 81% de quem nunca contesta.

---

## 4. Confiança no simulador

| Verificação | Resultado |
|---|---|
| Determinismo | mesma configuração e mesma semente geram o mesmo registro byte a byte, no Windows e no Linux. Uma execução refeita deu a tabela de partidas com o mesmo SHA-256 |
| Auditoria | toda partida pode gerar um registro JSONL que o `replay` refaz e confere evento a evento; cada evento cita a regra que o justificou |
| Testes | 502 passam (1 pulado); todo item de regra da especificação tem teste (176 de 176 na matriz de rastreabilidade) |
| Metamórficos | trocar nomes de categorias, girar o dado do Critical Failure e inverter a ordem da mesa não mudam o que não deveriam mudar |
| Fuzzing | nenhum erro sem controle no motor, nas configurações nem no replay. Achou uma brecha na auditoria (a linha final não era conferida inteira), que foi corrigida |
| Teste de mutação | 4.883 mutantes do motor da v1 e da v2: 4.508 mortos, 342 sobreviventes, 13 por tempo esgotado, 20 sem teste. **Escore 0,930.** As lacunas do jogo base, dos ganchos de medida e das invariantes foram fechadas com testes novos, e os mutantes-alvo foram conferidos à mão |

**Lacunas que ficaram, por decisão do autor:** detalhes das variantes VAR-02 a VAR-06, a observação da v1 e a leitura de ação da v1 vinda do registro. Nenhuma delas afeta os resultados da v2.2.1 base.

---

## 5. Sugestões de mudança de regra (decisão do autor)

**Nada aqui foi aplicado.** Cada item traz o que os dados mostram, as opções e uma sugestão. A sugestão segue o princípio do autor de manter a simplicidade e de não mexer na regra antes do playtest quando o problema depende dos tempos provisórios.

| # | Ponto | O que os dados mostram | Opções | Sugestão |
|---|---|---|---|---|
| S1 | **Limite de testes** | Sem limite é a regra mais profunda. 1 ou 2 testes por ciclo e o custo do teste encurtam a partida, mas tiram profundidade e não resolvem o tempo parado com 5 jogadores | manter sem limite; adotar 2 testes por ciclo; adotar o custo do teste | **Manter sem limite.** Os meios-termos ficam guardados como variantes (VAR-11 e VAR-12) para comparar no playtest, se for o caso |
| S2 | **Tempo parado (REQ-10)** | Falha em tudo o que não limita os testes: 5,8 min com 4 jogadores e 9 min com 5. A diferença entre 4 e 5 é estrutural. Os tempos ainda são estimados | não mudar antes de cronometrar; recomendar 4 jogadores como a mesa ideal; avaliar o palpite da plateia (VAR-06) com pessoas; criar um limite de tempo para a explicação (não medido) | **Cronometrar no playtest antes de mudar a regra.** Se o tempo parado se confirmar, recomendar mesas de 4 e avaliar o palpite com pessoas, que é a variante desenhada para isso e que os bots não conseguem medir |
| S3 | **Peso dos incidentes para experientes (REQ-13)** | 0,17 com experientes, para uma zona de 0,20 a 0,60. Aumentar o dano faz os iniciantes zerarem cedo. Nenhuma combinação de fichas e dano serve aos dois públicos | rever a zona do REQ-13 para experientes; dano 3 com 6 fichas; manter | **Rever a zona, não o dano.** Quem domina o conteúdo sofrer menos com os incidentes é coerente com o objetivo do jogo, porque o conhecimento protege. O playtest com alunos diz qual público importa mais |
| S4 | **Fichas iniciais** | 5 é o mínimo que passa no REQ-07; 6 dá folga (de 1% a 2% de partidas com alguém zerado) e não muda mais nada | manter 5; passar para 6 | **Manter 5.** Passar para 6 só se o playtest mostrar alunos zerando cedo |
| S5 | **Duração com 4 jogadores (REQ-08)** | 38 min, abaixo da faixa de 40 a 50. O autor considera bom encurtar desde que não se perca profundidade, e a regra atual é a mais profunda | rever a zona (por exemplo, só o teto de 50 min); manter a zona e esperar os tempos reais | **Rever a zona do REQ-08** e decidir junto a parte "acima de 60 minutos". Não mudar a regra |
| S6 | **Vantagem da ordem (REQ-01)** | Com bots que jogam bem, o 1º vence cerca de 2,5 pontos acima de 1/N e o último cerca de 2,5 abaixo, na borda da zona | manter; medir uma compensação (por exemplo, 1 ficha a mais para os últimos da ordem do ciclo 1) | **Manter e observar no playtest.** O efeito é pequeno. Se o autor quiser tratar, a compensação precisa ser medida antes de virar regra |
| S7 | **Variantes do playtest** | VAR-07 torna o REQ-11 impossível; VAR-02 zera iniciantes; VAR-03 piora o tempo parado; VAR-01, VAR-06 e VAR-09 quase não mudam o que se mede | levar todas ao playtest; descartar as que falham | **Descartar VAR-07, VAR-02 e VAR-03.** Levar ao playtest só as que medem o que o bot não alcança, como o palpite (VAR-06) |
| S8 | **Construir contra caçar** | Caçar puro nunca é a melhor resposta, mas o melhor jogador mistura as duas coisas, e o REQ-11 passa | manter; criar uma variante que premie o teste certeiro (não medida) | **Manter.** O desenho já faz o bom jogador atacar quando vale a pena. Só criar a variante se o autor quiser que o Caçador puro seja viável |

### Detalhe da S2: máximo de 4 jogadores

- **Hoje o mínimo também é 4** (R-1.2: 4 a 5 jogadores). Com o máximo em 4, o jogo passa a ser só para exatamente 4 jogadores. Numa turma, isso pede mesas de 4 (uma turma de 30 deixa 2 alunos de fora ou exige uma mesa diferente).
- **O que sai com a mesa de 5:** o pior tempo parado (9 min por ciclo, contra 5,8 com 4). Com 4 jogadores, o REQ-10 ainda falha com os tempos provisórios, mas passa se os tempos reais forem 25% menores.
- **Nada precisa ser rodado de novo para 4 jogadores:** uma partida de 4 é igual nas duas versões. Só o rótulo e o hash das regras mudam.
- **Mesa de 3 nunca foi simulada.** Se o autor quiser 3 a 4, é preciso medir antes. Hipótese não medida: com 3, o atacante, o defensor e o Auditor são todos os jogadores, e ninguém fica parado na disputa.

### Detalhe da S3: o peso dos incidentes para experientes (REQ-13)

**O que o REQ-13 mede:** a fração de todas as fichas movimentadas na partida (ganhos e perdas de todas as fontes) que vem do dano dos 3 incidentes. A intenção vem do PDF (p. 34), na linha do parâmetro "Dano de incidente": "incidentes pesam, mas não decidem a partida sozinhos". A zona numérica, de 0,20 a 0,60, foi proposta na Fase 0 e confirmada pelo autor.

**Para onde vão as fichas.** Amostra descritiva de 400 partidas por cenário, com a configuração da base do Experimento 6 e os registros completos. Não é execução oficial. A razão bate com a oficial (0,169 e 0,216, contra 0,171 e 0,215).

| Fichas por jogador por partida, 4 jogadores | Iniciante | Experiente |
|---|---|---|
| Dano de incidente (perda) | 3,3 | 2,7 |
| Diagnóstico certo (ganho) | 1,2 | 2,4 |
| Homologação (ganho / perda) | 4,4 / 0,5 | 3,9 / 0,8 |
| Critical Failure (perda) | 2,7 | 2,8 |
| Pontuação final (ganho) | 3,2 | 3,5 |
| **Total movimentado** | **15,2** | **16,1** |
| **REQ-13 (dano ÷ total)** | **0,22** | **0,17** |

- **O experiente perde menos no incidente.** Ele sai sem dano nenhum em 58% dos incidentes, contra 49% do iniciante. Fica sem cobertura em 32% contra 39%, porque lê melhor o Radar e se prepara. Tem Alerta na categoria em 11% contra 18%, porque defende melhor na Homologação.
- **E ganha mais no próprio incidente.** Ele acerta o diagnóstico em 79% das vezes, contra 39% do iniciante, e isso aumenta o total movimentado.
- **Os dois efeitos se somam.** Trocar só o dano do iniciante pelo do experiente leva a razão de 0,22 para 0,19. Trocar só as outras fontes leva a 0,20. Cerca de dois terços da queda vêm do dano menor, e um terço das fichas a mais do diagnóstico.
- **No Critical Failure, o conhecimento não protege:** a categoria é sorteada no dado e não há diagnóstico. Os dois públicos perdem cerca de 2,8 fichas.

**A mesma partida, lida de outras formas** (amostra descritiva; 4 e 5 jogadores):

| Medida | Iniciante | Experiente |
|---|---|---|
| Atual: só o dano dos 3 incidentes | 0,22 / 0,21 | 0,17 / 0,18 |
| Dano dos incidentes e do Critical Failure | 0,40 / 0,39 | 0,34 / 0,35 |
| Incidente inteiro: dano e ganho do diagnóstico | 0,29 / 0,29 | 0,32 / 0,32 |

Lido como incidente inteiro, o incidente **não pesa menos para o experiente. Pesa um pouco mais**, só que como ganho, e não como perda. É a mensagem do jogo: quem sabe o conteúdo transforma o incidente em oportunidade.

**Ficar fora do REQ-13 o dano do Critical Failure foi escolha do assistente**, registrada no diário (Experimento 6) como detalhe e não perguntada. Ela muda o veredito, por isso precisa da confirmação do autor.

**Opções:**

| Opção | O que muda | Veredito com experientes |
|---|---|---|
| A. Manter a medida e a zona; explicar a falha com experientes como achado | nada | falha (0,17), com explicação |
| B. Contar o Critical Failure como incidente | definição da medida | passa (0,34) |
| C. Medir o incidente inteiro (dano e diagnóstico) | definição da medida | passa (0,32) |
| D. Piso menor para experientes (por exemplo, 0,15) | zona | passa |
| E. Mais dano, ou dano 3 com 6 fichas | regra | passa, mas os iniciantes zeram cedo (REQ-07 falha) |

**Sugestão: A, com C como descrição ao lado, sem veredito.** A regra não muda, o critério fixado antes da medição não muda, e o texto do TCC ganha a explicação de por que o requisito falha com experientes e por que isso é o comportamento desejado. B, C e D mudam o critério depois de ver o resultado. Se o autor escolher uma delas, o texto precisa declarar isso.

**Se o autor quiser uma v2.2.2 ou v2.3 antes do playtest**, a mudança mais defensável pelos dados é nenhuma na mecânica. Ficariam só a revisão das zonas do REQ-08 e do REQ-13 e, talvez, a recomendação de 4 jogadores. Pela convenção do projeto, qualquer mudança de regra cria um arquivo novo em `regras/`, uma entrada em `docs/HISTORICO_REGRAS.md` e um YAML novo.

---

## 6. Limites que o texto do TCC precisa declarar

1. **Bots não são alunos.** O simulador mede o balanceamento da mecânica, não a aprendizagem nem a diversão.
2. **Os perfis "iniciante" e "experiente"** mostram se a mecânica degrada com pouco conhecimento. Eles não testam a hipótese pedagógica, que cabe aos dados com pessoas.
3. **Os tempos do MOD-05 são provisórios.** Os vereditos de duração (REQ-08) e de tempo parado (REQ-10) só valem de verdade com os tempos cronometrados.
4. **"Nenhum estilo dominante" vale entre os 6 estilos escritos à mão.** O REQ-04 de estilos passou só por causa da mesa de Aleatórios; sem ela, o veredito seria inconclusivo.
5. **Os bots contam cartas.** O REQ-05 vale para quem conta; com pessoas, mais blefes devem passar.
6. **A validação da v1 se apoia em 6 partidas do artigo.** O simulador reproduz o mecanismo da bola de neve, mas não a taxa de desequilíbrio do artigo pelo critério principal.
7. **A v1 foi só observada**, nunca ajustada, como linha de base.
8. **As medidas de profundidade (MET-08 a MET-10) são só descrição**, sem zona de aceite. A das escolhas apertadas, com o limiar atual, não separa as regras.

---

## 7. Pendências

**Decisões do autor**

- Rever as zonas do REQ-08 (incluindo a parte "acima de 60 minutos") e do REQ-13 para experientes (S3 e S5).
- Decidir se haverá uma v2.2.2 ou v2.3 antes do playtest (seção 5).
- Limiar da escolha apertada (MET-08): baixar o limiar, trocar a medida ou deixá-la de lado.
- REQ-14 (Hotfix) e MET-02 a MET-06, ainda aguardando decisão.
- Revisar a redação dos trechos marcados em `regras/v2.2.1.md` e `regras/v1.md`.

**Para o playtest**

- Cronometrar as ações (compra, colocação, teste, explicação, contestação, Produção) para substituir os tempos do MOD-05 e julgar o REQ-08 e o REQ-10.
- Registrar o tempo parado de cada jogador e preencher a Folha de registro. O `cf folha` exporta o mesmo formato a partir de partidas simuladas, para comparar.
- Observar a taxa de blefes que passam, a vantagem da ordem e quantos jogadores zeram, que são os pontos em que pessoas devem diferir dos bots.

**Opcionais (fora do escopo atual)**

- Busca de exploits: uma busca automática nos parâmetros do Heurístico atrás de um perfil que vença todos, para fortalecer o REQ-04.
- Uma execução completa do teste de mutação, para medir o escore com os testes novos.

---

## 8. As fases terminaram?

**Sim. As Fases 0, 1, 1b, 2, 3, 4 e 5 foram entregues**, cada uma com commit, entrada no diário e, quando havia experimento, manifest e relatório no git. O simulador cumpriu o objetivo do autor: comparou estilos de jogo, apontou o melhor (o Heurístico) e mostrou que a v2.2.1 está balanceada em quase tudo o que um bot consegue medir. Os pontos abertos dependem de tempos reais e de pessoas.

O próximo passo é o **playtest** com a v2.2.1, que é o ciclo seguinte do Design Science Research: as regras foram para o simulador, e agora vão para as pessoas. Os dados do playtest podem voltar ao simulador, com os tempos cronometrados no MOD-05 e as Folhas de registro, para refazer as medidas com números reais.

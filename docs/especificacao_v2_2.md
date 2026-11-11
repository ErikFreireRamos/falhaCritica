# Especificação das regras — Critical Failure v2.2 (revisão atual: v2.2.1)

**Versão especificada:** v2.2.1, que é a v2.2 com as correções COR-01 e COR-02. O texto corrido das regras está em `regras/v2.2.1.md`; o da v2.2 impressa, em `regras/v2.2.md`. Os números de página deste documento são os do PDF da v2.2.

**Fonte:** `docs/Critical_Failure_-_Regras_Completas_2.2.pdf` (35 páginas, atualização de 17 de outubro de 2026). É a fonte da verdade para a v2.2, com uma exceção: as correções do autor listadas na seção "Correções do autor" (`COR-<nn>`) são posteriores ao PDF e valem sobre ele até que o PDF seja atualizado. Em qualquer outro ponto em que este documento e o PDF divergirem, vale o PDF e este documento deve ser corrigido.

Este documento reescreve as regras como itens atômicos e numerados. Cada evento do registro de auditoria e cada teste automático aponta para um destes identificadores.

## Como ler

### Identificadores

| Forma | Uso | Exemplo |
|---|---|---|
| `R-<seção>.<item>` | seção do PDF sem subseções numeradas | `R-6.1` |
| `R-<seção>.<subseção>.<item>` | subseção numerada do PDF | `R-7.2.2` |
| `R-<seção>.0.<item>` | texto próprio de uma seção que também tem subseções numeradas (2, 7, 8 e 9) | `R-8.0.4` |
| letra no fim | divisão atômica de um mesmo passo do PDF | `R-7.2.2a` |
| `R-B.<nn>`, `R-C.<nn>` | carta de Teste e carta de Incidente | `R-C.13` |
| `R-B.0.<n>`, `R-C.0.<n>` | regras gerais dos Apêndices B e C | `R-C.0.2` |
| `R-REG.<n>` | seção "Registro da partida" | `R-REG.2` |
| `VAR-<nn>` | variante de playtest | `VAR-04` |
| `MOD-<nn>` | hipótese do simulador que não é regra | `MOD-01` |
| `COR-<nn>` | correção do autor posterior ao PDF | `COR-01` |

O `<item>` é o número do passo quando o PDF numera os passos (seções 3, 5, 6, 7.2 e 8). Parágrafos sem número recebem os números seguintes, na ordem em que aparecem.

`AMB-<nn>` remete a `docs/AMBIGUIDADES.md`. `REQ-<nn>` e `MET-<nn>` remetem a `configs/requisitos.yaml`.

### Tipos

| Tipo | Significado | Precisa de teste por regra? |
|---|---|---|
| `regra` | mecânica que o motor aplica | sim |
| `definicao` | termo usado por outras regras | sim, quando é calculável |
| `componente` | quantidade ou peça física, validada pela configuração | sim, pela configuração |
| `mesa` | só existe na mesa física (fala, tempo, manuseio); no simulador vira modelo ou fica de fora | não |
| `nota` | justificativa, exemplo ou propriedade derivada; os exemplos viram casos de teste | não |
| `revogada` | regra impressa no PDF que o autor retirou; fica atrás de uma chave de configuração, desligada por padrão, para medir o efeito da mudança | sim, com a chave ligada |

### Parâmetros

A coluna Parâmetros propõe o nome que cada número terá em `configs/regras_v2_2.yaml` (Fase 1). Nenhum desses números pode aparecer no código.

### Direção

Sentido horário é o mesmo que "para a esquerda". No simulador os assentos são numerados em sentido horário: o jogador à esquerda do assento `i` é o assento `i + 1` (módulo N), e o da direita é o `i - 1`.

## Correções do autor

Decisões do autor posteriores ao PDF de 17 de outubro de 2026. Valem sobre o PDF até que ele seja atualizado; a atualização do PDF é pendência do autor. Cada correção está também em `docs/HISTORICO_REGRAS.md`.

O comportamento impresso no PDF continua disponível pela chave de configuração indicada, desligado por padrão, para o simulador medir o efeito de cada mudança.

| ID | Data | Regras afetadas | No PDF 2.2 | Correção | Origem | Configuração |
|---|---|---|---|---|---|---|
| COR-01 | 2026-11-09 | R-1.2 | 4 a 6 jogadores | 4 a 5 jogadores | AMB-06: com 6 jogadores o baralho pode acabar | `jogadores.maximo` |
| COR-02 | 2026-11-09 | R-6.9 (nova); R-6.2b (revogada); R-6.8, R-7.4.4 e R-8.1.5 (notas ajustadas) | O Alerta fica até o jogador colocar uma carta da categoria ou até um incidente da categoria | Todos os cubos de Alerta saem no início de cada Planejamento; colocar carta não remove mais Alerta | Resposta do autor a AMB-12 | `alertas.limpeza_no_planejamento` |

Consequências da COR-02, confirmadas pelo autor:

- Nos ciclos 1 e 2, um Alerta só pesa na Produção do mesmo ciclo, e só se for da categoria-chave do incidente. Fora dela, não custa nada ao defensor.
- Os Alertas recebidos na Homologação do ciclo 3 não têm Planejamento seguinte e ficam até o fim: custam 1 ficha no Critical Failure se a categoria for sorteada (R-9.1.6) e 1 ficha na pontuação final (R-9.2.4). O mesmo cubo pode custar 2.

## 1. Visão geral

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-1.1 | regra | Vence quem terminar a partida com mais Fichas de Reputação. | 1 | — | Desempate em R-9.2.7 e R-9.2.8 |
| R-1.2 | regra | A partida tem de 4 a 5 jogadores. | 1 | `jogadores.minimo=4`; `jogadores.maximo=5` | COR-01: o PDF diz 4 a 6; VAR-08; AMB-06 |
| R-1.3 | regra | A partida tem 3 ciclos, seguidos do Critical Failure e da revelação final. | 1 | `ciclos=3` | Detalhe em R-4.1 e R-4.2 |
| R-1.4 | definicao | As 7 categorias do jogo base são Desempenho, Compatibilidade, Interação, Confiabilidade, Segurança da Informação, Manutenibilidade e Flexibilidade. | 1 | `categorias.base=7` | 8ª categoria em R-11.1 |
| R-1.5 | nota | A duração estimada é de 40 a 50 minutos, a validar no playtest. | 1 | — | REQ-08 |

## 2. Componentes

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-2.0.1 | componente | O baralho de Testes do jogo base tem 63 cartas: 9 por categoria e 29 testes diferentes. | 2 | `baralho.cartas_base=63`; `baralho.testes_base=29`; `baralho.cartas_por_categoria=9` | Catálogo no Apêndice B |
| R-2.0.2 | componente | O baralho de Incidentes do jogo base tem 14 cartas, 2 por categoria-chave. | 2 | `incidentes.base=14`; `incidentes.por_categoria=2` | Catálogo no Apêndice C |
| R-2.0.3 | componente | Há 1 carta Critical Failure, que é o evento final. | 2 | — | R-9.1.1 |
| R-2.0.4 | mesa | Há 1 Documento do Auditor, com a descrição de cada teste e com o que ele não deve ser confundido. | 2 | — | MOD-02 |
| R-2.0.5 | mesa | Cada jogador tem um Cartão de Referência com os nomes dos testes por categoria e o resumo do ciclo. | 2 | — | MOD-06 |
| R-2.0.6 | componente | Cada jogador tem um Leque de Diagnóstico com uma carta por categoria (7 no jogo base). | 2 | — | R-8.0.2a |
| R-2.0.7 | componente | O banco tem 60 fichas de valor 1 e 15 fichas de valor 5. | 2 | `banco.fichas_valor_1=60`; `banco.fichas_valor_5=15` | AMB-17 |
| R-2.0.8 | componente | Há 30 cubos de Alerta. | 2 | `banco.cubos_alerta=30` | AMB-17 |
| R-2.0.9 | componente | O playmat de cada jogador tem as zonas Sistema (máximo de 5 cartas) e Mão, e uma trilha de categorias. | 2 | `sistema.teto=5` | R-6.2 |
| R-2.0.10 | componente | Há 1 dado de 8 faces, que sorteia a categoria do Critical Failure. | 2 | `dado.faces=8` | R-9.1.1 |
| R-2.0.11 | componente | Há um Marcador de Auditor e um marcador de primeiro jogador. | 2 | — | R-4.9 |
| R-2.0.12 | mesa | Há 1 Folha de registro por partida de avaliação, preenchida por um observador. | 2 | — | R-REG.1 a R-REG.3 |
| R-2.0.13 | regra | A Carta de Teste traz apenas a categoria e o nome do teste. A descrição fica só no Documento do Auditor. | 2 | — | |
| R-2.0.14 | regra | A trilha tem um espaço por categoria, mais um para o módulo. Um cubo num espaço significa Alerta naquela categoria. | 3 | — | Invariante derivado, com R-7.4.2: no máximo 1 Alerta por categoria por jogador |
| R-2.0.15 | regra | Faces do dado: 1 Desempenho; 2 Compatibilidade; 3 Interação; 4 Confiabilidade; 5 Segurança da Informação; 6 Manutenibilidade; 7 Flexibilidade; 8 Segurança Operacional. | 3 | — | |
| R-2.0.16 | regra | Sem o módulo, se sair 8, rola-se o dado de novo. | 3 | — | R-11.5 |

### 2.1 As duas faces do incidente

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-2.1.1 | regra | A frente do incidente mostra nome, número e relato completo, e fica visível desde que a carta entra no Radar. Não mostra categorias candidatas, categoria-chave, secundária nem testes-chave. | 3 | — | Informação pública |
| R-2.1.2 | regra | O verso (gabarito) traz a categoria-chave, a categoria secundária opcional, 1 ou 2 testes-chave, a explicação, a severidade e a lista de dano. Só é revelado depois que todos mostram o diagnóstico. | 3 | — | Informação oculta até R-8.0.3 |
| R-2.1.3 | definicao | A categoria-chave é a única resposta que conta como diagnóstico correto. Ela determina a ficha de diagnóstico, a Lição aprendida, a categoria usada para cobertura e dano e os Alertas removidos na limpeza. | 3 | — | |
| R-2.1.4 | regra | A categoria secundária não concede fichas, não conta como acerto no desempate, não permite pegar a Lição aprendida e não oferece cobertura. Os Alertas dela não são cobrados nem removidos pelo incidente. | 3 | — | |
| R-2.1.5 | regra | Não existe pontuação parcial por categorias próximas. | 3 | — | |
| R-2.1.6 | regra | O gabarito impresso define a categoria-chave. O Auditor não acrescenta respostas pontuáveis durante a resolução. | 3 | — | |
| R-2.1.7 | nota | Não há pista adicional no verso: toda a informação necessária para interpretar o incidente está no relato da frente. | 3 | — | MOD-03 |

## 3. Preparação

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-3.1 | regra | Cada jogador recebe um playmat, um Cartão de Referência, um Leque de Diagnóstico e 5 Fichas de Reputação. | 4 | `fichas.iniciais=5` | REQ-07 |
| R-3.2 | regra | Linha do Tempo: embaralham-se os Incidentes com o gabarito oculto e separam-se 3 cartas sem consultá-las. | 4 | `linha_do_tempo.incidentes=3` | Evento aleatório do jogo |
| R-3.2a | regra | A carta Critical Failure fica por baixo das 3, formando uma pilha de 4. | 4 | — | |
| R-3.2b | regra | Os demais incidentes voltam à caixa e não participam da partida. | 4 | — | |
| R-3.3 | regra | Radar: a 1ª carta da Linha do Tempo vai para a vaga Agora e a 2ª para a vaga Próximo, as duas com a frente para cima. | 4 | — | R-4.11 |
| R-3.4 | regra | Sistemas: embaralham-se as Cartas de Teste e cada jogador recebe 2, viradas para baixo, direto na zona Sistema. | 4 | `sistema.cartas_iniciais=2` | Evento aleatório do jogo; REQ-12 |
| R-3.4a | regra | Cada jogador pode olhar as cartas do próprio sistema a qualquer momento. | 4 | — | Informação privada do dono |
| R-3.4b | regra | Se as 2 cartas iniciais de um jogador forem do mesmo teste, troca-se uma delas pela carta do topo do baralho. | 4 | — | AMB-07 |
| R-3.4c | regra | Todos começam com a mão vazia. | 4 | — | |
| R-3.5 | regra | Backlog: 5 Cartas de Teste são viradas para cima no centro da mesa. | 4 | `backlog.tamanho=5` | Informação pública |
| R-3.6 | regra | Escolhe-se o primeiro jogador. | 4 | — | AMB-08 |
| R-3.6a | regra | O jogador à direita do primeiro jogador recebe o Marcador de Auditor e o Documento do Auditor. | 4 | — | R-4.9a |
| R-3.7 | regra | Nenhum jogador pode consultar o verso de um incidente antecipadamente. Não existe a ação de descartar uma carta para espiar. | 4 | — | Teste de não vazamento da observação |
| R-3.8 | nota | A preparação usa 2 Cartas de Teste por jogador nos sistemas e 5 no Backlog: 13 com 4 jogadores e 15 com 5. O PDF dá o exemplo de 6 jogadores (17 das 63), que deixou de valer com a COR-01. | 4 | — | Oráculo de teste; AMB-06 |

## 4. Estrutura da partida

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-4.1 | regra | Cada ciclo tem três fases, sempre nesta ordem: Planejamento, Homologação e Produção. | 5 | — | |
| R-4.2 | regra | Depois do terceiro ciclo vêm o Critical Failure, a revelação dos sistemas e a pontuação final. | 5 | — | |
| R-4.3 | regra | No Planejamento e na Homologação os jogadores agem um de cada vez, a partir do primeiro jogador e em sentido horário. | 5 | — | |
| R-4.4 | regra | A Produção é resolvida por todos ao mesmo tempo. | 5 | — | |
| R-4.5 | regra | O Planejamento termina quando todos fizeram a sua vez. | 5 | — | |
| R-4.6 | regra | A Homologação termina quando todos passaram. | 5 | — | AMB-03 |
| R-4.7 | regra | O ciclo termina depois da Produção. | 5 | — | |
| R-4.8 | regra | Alvo livre: na Homologação cada jogador escolhe quem testar, respeitando a regra do bug duplicado. | 5 | — | R-7.4.2; VAR-04; REQ-06 |
| R-4.9 | regra | Fim do ciclo: o marcador de primeiro jogador e o Marcador de Auditor passam para a esquerda. | 5 | — | |
| R-4.9a | definicao | O Auditor é sempre o último da ordem de jogo do ciclo e muda a cada ciclo. | 5 | — | Decorre de R-3.6a e R-4.9 |
| R-4.10 | regra | Em seguida, a carta da vaga Próximo passa para a vaga Agora, e a próxima carta da Linha do Tempo entra na vaga Próximo. | 5 | — | |
| R-4.11 | definicao | O Radar tem duas vagas: a carta da vaga Agora é o incidente deste ciclo e a da vaga Próximo é o do ciclo seguinte. | 5 | `radar.vagas=2` | |
| R-4.12 | regra | As duas cartas do Radar mostram o nome e o relato completo, e todos podem lê-las desde o Planejamento. | 5 | — | Informação pública; MOD-04 |
| R-4.13 | regra | Ocupação do Radar: ciclo 1, Incidente 1 e Incidente 2; ciclo 2, Incidente 2 e Incidente 3; ciclo 3, Incidente 3 e Critical Failure. | 5 | — | |
| R-4.14 | regra | O verso do incidente fica escondido até que todos revelem as suas escolhas na Produção. | 5 | — | R-8.0.3 |
| R-4.15 | mesa | Consultar o Cartão de Referência é permitido. Consultar os gabaritos do Apêndice C antes da resolução não é. | 5 | — | |

## 5. Fichas de Reputação

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-5.1 | definicao | Ganhar é pegar fichas do banco. Perder é devolver fichas ao banco. Pagar a um jogador é entregar fichas a ele. | 6 | — | |
| R-5.2 | regra | Mínimo 0: quem precisa pagar mais do que tem paga o que tiver. | 6 | `fichas.minimo=0` | AMB-01; AMB-13 |
| R-5.2a | regra | Se o pagamento é para outro jogador, a diferença sai do banco, e quem recebe nunca perde por isso. | 6 | — | |
| R-5.3 | regra | Cada item de pontuação ou dano vale 1 ou 2 fichas, e o total é a soma dos itens aplicáveis. | 6 | — | |
| R-5.4 | regra | As fichas de cada jogador ficam sempre à vista. | 6 | — | Informação pública |

## 6. Fase 1 — Planejamento

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-6.1 | regra | Comprar 3 cartas é obrigatório. | 6 | `planejamento.compras=3` | VAR-07; AMB-06 |
| R-6.1a | regra | As cartas são compradas uma de cada vez, do Backlog ou do topo do baralho. | 6 | — | |
| R-6.1b | regra | Depois de cada compra no Backlog, a vaga é reposta com a carta do topo do baralho. | 6 | — | AMB-06 |
| R-6.1c | regra | Toda carta comprada do Backlog é informação pública. | 6 | — | AMB-10 |
| R-6.2 | regra | Colocar cartas no sistema é opcional: o jogador coloca quantas quiser, viradas para baixo, até o teto de 5. | 6 | `sistema.teto=5` | AMB-09; REQ-11 |
| R-6.2a | regra | Colocar é permanente: não há troca nem retirada. | 6 | — | |
| R-6.2b | revogada | Se a carta colocada é de uma categoria em que o jogador tem Alerta, o cubo é removido. | 6 | — | Revogada pela COR-02; AMB-10 |
| R-6.3 | regra | O Planejamento é o único momento em que o sistema muda. | 6 | — | |
| R-6.4 | regra | Cada jogador faz o turno inteiro antes de passar a vez. | 6 | — | AMB-09 |
| R-6.5 | regra | Não há limite de cartas na mão. | 6 | — | |
| R-6.6 | regra | Baralho vazio: embaralha-se o descarte para formar um novo baralho. | 6 | — | Evento aleatório do jogo; AMB-06 |
| R-6.7 | mesa | Um turno de Planejamento leva cerca de 30 segundos. | 6 | — | MOD-05 |
| R-6.8 | nota | Com o sistema cheio, um Alerta novo não pode ser corrigido: fica até um incidente da categoria ou até o fim. | 6 | — | Propriedade derivada de R-6.2a e R-6.2b. Só vale com a COR-02 desligada |
| R-6.9 | regra | No início de cada Planejamento, todos os cubos de Alerta de todos os jogadores são removidos. | 6 | `alertas.limpeza_no_planejamento=sim` | Regra nova da COR-02. Não está no PDF; a página indicada é a da seção 6 |

## 7. Fase 2 — Homologação

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-7.0.1 | regra | Na sua vez, o jogador testa qualquer outro jogador ou passa. | 7 | — | AMB-03 |
| R-7.0.2 | regra | A vez segue em sentido horário e dá quantas voltas forem precisas. | 7 | — | |
| R-7.0.3 | regra | Quem passa sai da Homologação deste ciclo. | 7 | — | AMB-04 |
| R-7.0.4 | regra | A fase termina quando todos passaram. | 7 | — | Igual a R-4.6 |
| R-7.0.5 | regra | Quem decide se blefa é sempre o defensor. | 7 | — | |

### 7.1 O Auditor

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-7.1.1 | regra | O Auditor joga normalmente. | 7 | — | VAR-03 |
| R-7.1.2 | mesa | O Auditor é o único que consulta o Documento do Auditor. | 7 | — | MOD-02 |
| R-7.1.3 | regra | O Auditor julga apenas a explicação do defensor, nunca se ele tem a carta. | 7 | — | O Auditor não recebe informação oculta do defensor |
| R-7.1.4 | regra | Se o Auditor for atacante ou defensor numa disputa, a função passa, só nela, ao jogador não envolvido mais próximo à sua esquerda. | 7 | — | AMB-05 |
| R-7.1.5 | regra | A decisão do Auditor é final. | 7 | — | |
| R-7.1.6 | regra | A função de Auditor não exclui o jogador do diagnóstico na Produção: ele escolhe a sua categoria antes de consultar o verso, como os demais. | 7 | — | R-8.0.2 |

### 7.2 Passo a passo da disputa

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-7.2.1 | regra | Executar o teste: o atacante joga uma Carta de Teste da mão, virada para cima, e anuncia o teste e a categoria. Essa categoria é a X da disputa. | 7 | — | Informação pública |
| R-7.2.1a | regra | A carta de ataque vai para o descarte no fim da disputa. | 7 | — | |
| R-7.2.2 | regra | Responder: o defensor escolhe admitir ("Falhou") ou defender-se. | 7 | — | |
| R-7.2.2a | regra | Para defender-se, o defensor nomeia um teste da categoria X que diz ter no sistema e explica, com as próprias palavras, o que ele verifica. | 7 | — | MOD-01 |
| R-7.2.2b | regra | A defesa pode ser verdade ou blefe. | 7 | — | AMB-15 |
| R-7.2.2c | regra | Nomear um teste de outra categoria conta como "Falhou". | 7 | — | AMB-16 |
| R-7.2.2d | mesa | A explicação tem até 30 segundos. | 7 | `disputa.tempo_defesa_s=30` | MOD-05; também na p. 8 |
| R-7.2.3 | regra | Conferir: o Auditor compara a explicação com o Documento e diz "confere" ou "não confere". | 7 | — | MOD-02 |
| R-7.2.3a | mesa | Não é preciso usar as mesmas palavras. A explicação não confere quando descreve outro teste, principalmente um da mesma categoria. | 7 | — | MOD-01; MOD-02 |
| R-7.2.3b | regra | Se a explicação não conferir, conta como "Falhou". | 7 | — | VAR-02 |
| R-7.2.4 | regra | Aceitar ou contestar: se conferiu, o atacante aceita, e nada é revelado, ou contesta. | 7 | — | MOD-07 |
| R-7.2.4a | regra | Na contestação, o defensor precisa revelar do próprio sistema uma carta exatamente do teste que nomeou. | 7 | — | AMB-15 |
| R-7.2.4b | regra | A carta revelada volta virada para baixo, mas passa a ser conhecida por todos. | 7 | — | Informação pública permanente |
| R-7.2.5 | mesa | Qualquer que seja o resultado, o Auditor lê em voz alta a descrição correta do teste nomeado. | 7 | — | MOD-05 |

### 7.3 Resultados da disputa

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-7.3.1 | regra | Falhou (admitiu, nomeou teste de outra categoria ou a explicação não conferiu): o atacante ganha 1 ficha do banco e o defensor recebe Alerta X. | 8 | `disputa.falhou.atacante_ganha=1` | VAR-02 |
| R-7.3.2 | regra | Defesa aceita: nada acontece para o atacante nem para o defensor. | 8 | — | VAR-06 (palpite da plateia antes desta decisão); AMB-30; AMB-31 |
| R-7.3.3 | regra | Contestou, e o defensor tinha a carta: o atacante paga 1 ficha ao defensor. | 8 | `disputa.contestacao_verdade.atacante_paga=1` | |
| R-7.3.4 | regra | Contestou, e era blefe: o defensor paga 1 ficha ao atacante, o atacante ganha mais 1 do banco e o defensor recebe Alerta X. | 8 | `disputa.contestacao_blefe.defensor_paga=1`; `disputa.contestacao_blefe.atacante_ganha_do_banco=1` | VAR-01 |
| R-7.3.5 | nota | Tentar explicar nunca é pior do que admitir: uma explicação que não confere custa o mesmo que "Falhou". Pelo ganho esperado do atacante, contestar só compensa quando a chance de blefe é de pelo menos 1 em 3. | 8 | — | Oráculo de teste; REQ-04; REQ-05 |

### 7.4 Regras adicionais

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-7.4.1 | regra | Cada teste gasta 1 carta da mão. Não há outro limite ao número de testes. | 8 | — | VAR-05; VAR-11 |
| R-7.4.2 | regra | Bug duplicado: não é permitido testar um jogador numa categoria em que ele já tem Alerta. | 8 | — | MET-03; VAR-10 |
| R-7.4.2a | regra | A categoria volta a poder ser testada quando o cubo sai. | 8 | — | |
| R-7.4.3 | regra | Quem passa guarda as cartas que tem na mão. | 8 | — | Complementa R-7.0.3 |
| R-7.4.4 | nota | O Alerta chega antes da Produção do mesmo ciclo e sai no início do próximo Planejamento. | 8 | — | Texto ajustado pela COR-02; o PDF diz que o Alerta só pode ser corrigido no próximo Planejamento. Decorre de R-4.1 e R-6.9; REQ-14 |

### 7.5 Por que essa regra é didática

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-7.5.1 | nota | Como as cartas não trazem descrição, toda defesa exige explicar o teste com as próprias palavras; o blefe só sobrevive se a explicação estiver correta. | 8 | — | MOD-01 |

## 8. Fase 3 — Produção

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-8.0.1 | mesa | Ler o relato: sem virar a carta da vaga Agora, o Auditor lê em voz alta o relato completo da frente. | 9 | — | MOD-05 |
| R-8.0.2 | regra | Diagnosticar: cada jogador, inclusive o Auditor, escolhe em segredo uma única categoria do Leque. | 9 | — | MOD-03; MET-05 |
| R-8.0.2a | regra | Estão disponíveis as 7 categorias do jogo base; com o módulo, são 8. | 9 | — | |
| R-8.0.2b | regra | Todos revelam as escolhas juntos e, depois disso, não podem alterá-las. | 9 | — | Decisão simultânea: nenhum bot vê a escolha dos outros antes de escolher |
| R-8.0.3 | regra | Revelar o gabarito: só depois de todas as escolhas estarem à vista, vira-se a carta e leem-se a categoria-chave, a secundária, os testes-chave, a severidade e o "Por quê". | 9 | — | |
| R-8.0.4 | regra | Pontuar o diagnóstico: quem escolheu a categoria-chave ganha 1 ficha do banco. | 9 | `diagnostico.acerto=1` | AMB-01 |
| R-8.0.4a | regra | Quem escolheu a secundária ou qualquer outra categoria recebe 0. Não há pontuação parcial nem penalidade por errar. | 9 | — | |
| R-8.0.5 | regra | Aplicar o dano: cada jogador soma os itens da lista do verso e devolve o total ao banco. Todos os itens se referem à categoria-chave X. | 9 | — | R-8.1.1 a R-8.1.3; AMB-01 |
| R-8.0.5a | regra | Para comprovar cobertura, o jogador revela as cartas de categoria X do sistema. Quem não revela é tratado como sem cobertura. | 9 | — | AMB-11 |
| R-8.0.5b | regra | Cartas da categoria secundária não oferecem cobertura contra o incidente. | 9 | — | |
| R-8.0.6 | regra | Lição aprendida: na ordem de jogo, quem acertou a categoria-chave pode pegar 1 carta de categoria X do Backlog para a mão. | 9 | `licao_aprendida.cartas=1` | AMB-02 |
| R-8.0.6a | regra | O Backlog é reposto depois de cada retirada. | 9 | — | AMB-06 |
| R-8.0.6b | regra | Escolher a categoria secundária não dá direito à retirada. | 9 | — | |
| R-8.0.7 | regra | Limpeza: removem-se todos os cubos da categoria-chave X. | 9 | — | Com a COR-02, só muda o resultado no ciclo 3: nos ciclos 1 e 2 todos os cubos saem no Planejamento seguinte (R-6.9) |
| R-8.0.7a | regra | Cubos de outras categorias, inclusive da secundária, permanecem. | 9 | — | |
| R-8.0.7b | regra | As Cartas de Teste reveladas voltam viradas para baixo. | 9 | — | AMB-10 |
| R-8.0.7c | regra | O incidente sai do jogo. | 9 | — | |
| R-8.0.8 | definicao | Regra de acerto: "acertar o diagnóstico" significa escolher a categoria-chave impressa no verso. A definição vale para a Lição aprendida, o registro da partida e o desempate final. | 9 | — | |

### 8.1 Dano e exemplos

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-8.1.1 | regra | Nenhuma carta da categoria X no sistema: 2 fichas. | 10 | `dano.incidente.sem_cobertura=2` | REQ-13 |
| R-8.1.2 | regra | Alerta ativo na categoria X: 1 ficha. | 10 | `dano.incidente.alerta=1` | |
| R-8.1.3 | regra | Incidente severo e nenhum dos testes-chave no sistema: 1 ficha. | 10 | `dano.incidente.severo_sem_teste_chave=1` | R-C.0.2 |
| R-8.1.4 | regra | Um blefe aceito protege apenas na Homologação: na Produção só vale a carta de verdade no sistema. | 10 | — | |
| R-8.1.5 | nota | Exemplo de dano: incidente normal; Ana não tem carta da categoria-chave, tem Alerta nela e acertou o diagnóstico. Ganha 1 e devolve 3 (2 + 1), saldo de -2. | 10 | — | Caso de teste. A segunda parte do exemplo do PDF (construir uma carta da categoria para tirar o Alerta e ficar com +1) só vale com a COR-02 desligada |
| R-8.1.6 | nota | Exemplo de secundária: em Campanha viral, Ana escolhe Flexibilidade e ganha 1; Bruno escolhe Desempenho e não ganha. Só cartas de Flexibilidade contam como cobertura. O Alerta de Desempenho de Bruno não gera dano nem é removido. Por ser severo, o incidente cobra mais 1 de quem não tem Escalabilidade. | 10 | — | Caso de teste |

## 9. Fim de jogo

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-9.0.1 | regra | Depois da Produção do terceiro ciclo, a partida termina com o Critical Failure, que atinge todos, e com a revelação dos sistemas. | 10 | — | |

### 9.1 Critical Failure

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-9.1.1 | regra | Revela-se a carta e rola-se o d8 para sortear a categoria X. | 10 | — | Evento aleatório do jogo; R-2.0.15; R-2.0.16 |
| R-9.1.2 | regra | No Critical Failure não há diagnóstico nem categoria secundária. | 10 | — | |
| R-9.1.3 | regra | Dano que se aplica sempre: 1 ficha. | 10 | `dano.critical_failure.sempre=1` | |
| R-9.1.4 | regra | Não há 2 testes diferentes da categoria X no sistema: 1 ficha. | 10 | `dano.critical_failure.sem_cobertura_profunda=1` | |
| R-9.1.5 | regra | Não há nenhuma carta da categoria X no sistema: 2 fichas. | 10 | `dano.critical_failure.sem_cobertura=2` | |
| R-9.1.6 | regra | Alerta ativo na categoria X: 1 ficha. | 10 | `dano.critical_failure.alerta=1` | AMB-12: o cubo não sai depois. Com a COR-02, só chegam aqui Alertas recebidos no ciclo 3 |
| R-9.1.7 | regra | Cada jogador soma os itens e devolve o total ao banco. | 10 | — | R-5.2 |
| R-9.1.8 | nota | Na prática, o dano é de 1 com cobertura profunda, 2 com cobertura simples e 4 sem cobertura, mais 1 se houver Alerta. | 10 | — | Oráculo de teste |

### 9.2 Revelação e pontuação final

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-9.2.1 | regra | Todos viram o sistema inteiro para cima e acertam as fichas com o banco. | 11 | — | AMB-13 |
| R-9.2.2 | regra | Amplitude: +1 ficha por categoria distinta no sistema. | 11 | `final.categoria_distinta=1` | |
| R-9.2.3 | regra | +1 ficha por categoria com cobertura profunda. | 11 | `final.cobertura_profunda=1` | |
| R-9.2.3a | definicao | Cobertura profunda é ter 2 testes diferentes da mesma categoria no sistema. | 11 | `cobertura_profunda.testes_distintos=2` | Também usada em R-9.1.4 |
| R-9.2.4 | regra | -1 ficha por cubo de Alerta ainda ativo. | 11 | `final.alerta_ativo=1` | AMB-12; AMB-13. Com a COR-02, só chegam aqui Alertas recebidos no ciclo 3 |
| R-9.2.5 | regra | Cartas repetidas do mesmo teste não somam nada além da amplitude. | 11 | — | |
| R-9.2.6 | nota | O sistema vale no máximo 5 fichas, por exemplo com 5 categorias distintas ou com 3 categorias, 2 delas em cobertura profunda. | 11 | — | Propriedade para teste |
| R-9.2.7 | regra | Desempate: vence quem tem menos Alertas ativos. | 11 | — | |
| R-9.2.8 | regra | Persistindo o empate, vence quem acertou mais diagnósticos pela categoria-chave. Escolhas da secundária não contam. | 11 | — | AMB-14 |

## 10. Referência rápida

A seção 10 do PDF (p. 11) repete as regras em forma de resumo e tabela. Os valores abaixo precisam coincidir com os das seções anteriores; o `scripts/verificar_especificacao.py` confere isso.

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-10.1 | nota | Início: cada jogador com 5 fichas. | 11 | `fichas.iniciais=5` | R-3.1 |
| R-10.2 | nota | Planejamento: comprar 3; sistema com no máximo 5 cartas, sem troca. | 11 | `planejamento.compras=3`; `sistema.teto=5` | R-6.1; R-6.2 |
| R-10.3 | nota | Defensor falhou: atacante +1 e defensor recebe Alerta. | 11 | `disputa.falhou.atacante_ganha=1` | R-7.3.1 |
| R-10.4 | nota | Contestou e era verdade: atacante paga 1 ao defensor. | 11 | `disputa.contestacao_verdade.atacante_paga=1` | R-7.3.3 |
| R-10.5 | nota | Contestou e era blefe: defensor paga 1 ao atacante; atacante +1; defensor recebe Alerta. | 11 | `disputa.contestacao_blefe.defensor_paga=1`; `disputa.contestacao_blefe.atacante_ganha_do_banco=1` | R-7.3.4 |
| R-10.6 | nota | Diagnóstico: categoria-chave +1; secundária ou outra categoria 0. | 11 | `diagnostico.acerto=1` | R-8.0.4 |
| R-10.7 | nota | Produção: sem cobertura -2; Alerta -1; severo sem teste-chave -1. | 11 | `dano.incidente.sem_cobertura=2`; `dano.incidente.alerta=1`; `dano.incidente.severo_sem_teste_chave=1` | R-8.1.1 a R-8.1.3 |
| R-10.8 | nota | Critical Failure: sempre -1; sem 2 testes -1; sem cobertura -2; Alerta -1. | 11 | `dano.critical_failure.sempre=1`; `dano.critical_failure.sem_cobertura_profunda=1`; `dano.critical_failure.sem_cobertura=2`; `dano.critical_failure.alerta=1` | R-9.1.3 a R-9.1.6 |
| R-10.9 | nota | Final: categoria distinta +1; cobertura profunda +1; Alerta ativo -1. | 11 | `final.categoria_distinta=1`; `final.cobertura_profunda=1`; `final.alerta_ativo=1` | R-9.2.2 a R-9.2.4 |

## 11. Módulo opcional: Segurança Operacional

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-11.1 | regra | O módulo acrescenta a 8ª categoria, Segurança Operacional. | 12 | `categorias.modulo=1` | VAR-09 |
| R-11.2 | regra | Juntam-se ao baralho de Testes as 9 cartas de Segurança Operacional: Falha segura ×3, Alerta de perigo ×2, Restrição operacional ×2 e Análise de perigos ×2. | 12 | `baralho.cartas_modulo=9`; `baralho.testes_modulo=4` | R-B.30 a R-B.33 |
| R-11.3 | regra | Juntam-se aos Incidentes as cartas 15 e 16. | 12 | `incidentes.modulo=2` | R-C.15; R-C.16 |
| R-11.4 | regra | Cada jogador recebe a 8ª carta de diagnóstico. | 12 | — | R-8.0.2a |
| R-11.5 | regra | O resultado 8 do dado passa a valer no Critical Failure. | 12 | — | R-2.0.16 |
| R-11.6 | regra | O resto não muda: o teto continua em 5 cartas, e nos incidentes do módulo somente a categoria-chave pontua e determina dano e cobertura. | 12 | — | |
| R-11.7 | componente | Com o módulo, o jogo tem 72 Cartas de Teste, 33 testes e 16 incidentes. | 12 | `baralho.cartas_com_modulo=72`; `baralho.testes_com_modulo=33`; `incidentes.com_modulo=16` | Invariante de conservação de cartas |

## Apêndice A — Categorias e ISO/IEC 25010:2023

A página 13 do PDF relaciona cada categoria do jogo a uma característica da norma. Não há mecânica nesse apêndice.

## Apêndice B — Cartas de Teste (Documento do Auditor)

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-B.0.1 | componente | O jogo base tem 63 cartas e 29 testes, com 9 cartas por categoria. As 9 cartas de Segurança Operacional pertencem ao módulo. | 14 | `baralho.cartas_base=63`; `baralho.testes_base=29`; `baralho.cartas_por_categoria=9` | Conferido pelo script |
| R-B.0.2 | mesa | As descrições e os contrastes ("não confundir com") apoiam a conferência das defesas pelo Auditor. | 14 | — | MOD-01; MOD-02; MOD-03 |

A coluna "Não confundir com" lista os testes citados no contraste do Documento do Auditor. Ela é a base do modelo de confusão dos bots (MOD-03). Os nomes impressos nas cartas "Resistência (soak)" e "Penetração (pentest)" aparecem aqui na forma curta.

| ID | Categoria | Teste | Cópias | Conjunto | Não confundir com | Pág. | Descrição |
|---|---|---|---|---|---|---|---|
| R-B.01 | Desempenho | Carga | 3 | base | Estresse; Pico | 14 | Simula o uso normal e o pico esperado de usuários para verificar se o sistema mantém os tempos de resposta previstos. |
| R-B.02 | Desempenho | Estresse | 2 | base | Carga | 14 | Leva o sistema além do limite de projeto para descobrir onde e como ele quebra e se volta ao normal depois. |
| R-B.03 | Desempenho | Pico | 2 | base | Estresse; Escalabilidade | 14 | Aplica um aumento brusco e curto de usuários para ver se o sistema absorve a onda e se estabiliza quando ela passa. |
| R-B.04 | Desempenho | Resistência | 2 | base | Carga; Disponibilidade | 14 | Mantém uma carga normal por horas ou dias para revelar degradação lenta, como vazamento de memória. |
| R-B.05 | Compatibilidade | Coexistência | 3 | base | Adaptabilidade | 15 | Verifica se o sistema funciona no mesmo ambiente que outros produtos, dividindo recursos sem prejudicá-los nem ser prejudicado. |
| R-B.06 | Compatibilidade | Interoperabilidade | 2 | base | Contrato de API | 15 | Verifica, de ponta a ponta, se sistemas diferentes trocam informações e usam corretamente o que recebem. |
| R-B.07 | Compatibilidade | Contrato de API | 2 | base | Interoperabilidade; Retrocompatibilidade | 15 | Verifica se a API continua respeitando o formato combinado com quem a consome (campos, tipos, códigos de resposta), sem precisar subir os dois sistemas. |
| R-B.08 | Compatibilidade | Retrocompatibilidade | 2 | base | Adaptabilidade; Regressão | 15 | Verifica se a nova versão continua funcionando com clientes, arquivos e dados de versões anteriores. |
| R-B.09 | Interação | Acessibilidade | 3 | base | Teste com usuários | 16 | Verifica se pessoas com deficiência visual, auditiva, motora ou cognitiva conseguem usar o sistema, por exemplo com leitor de tela ou só com o teclado (WCAG). |
| R-B.10 | Interação | Proteção contra erro do usuário | 2 | base | Tolerância a falhas; Restrição operacional | 16 | Verifica se o sistema impede ou reduz as consequências de erros do usuário, com confirmação, desfazer e validação de campos. |
| R-B.11 | Interação | Teste A/B | 2 | base | Teste com usuários | 16 | Compara duas versões de uma tela ou funcionalidade com usuários reais e mede qual alcança melhor o objetivo. |
| R-B.12 | Interação | Teste com usuários | 2 | base | Teste A/B; Acessibilidade | 16 | Observa usuários representativos fazendo tarefas enquanto dizem o que pensam, para descobrir onde se confundem e quanto demoram para aprender. |
| R-B.13 | Confiabilidade | Recuperação | 3 | base | Tolerância a falhas | 17 | Provoca uma falha grave e verifica se o sistema volta a funcionar, em quanto tempo e se preserva os dados. |
| R-B.14 | Confiabilidade | Tolerância a falhas | 2 | base | Recuperação; Engenharia do Caos; Falha segura | 17 | Derruba uma parte do sistema e verifica se ele continua funcionando, mesmo de forma reduzida. |
| R-B.15 | Confiabilidade | Disponibilidade | 2 | base | Resistência | 17 | Mede se o sistema fica acessível durante todo o período de operação previsto, por exemplo 99,9% do mês. |
| R-B.16 | Confiabilidade | Engenharia do Caos | 2 | base | Tolerância a falhas | 17 | Injeta falhas de propósito e ao acaso em ambiente real ou quase real, como derrubar servidores ou atrasar a rede, para achar fraquezas antes que elas apareçam sozinhas. |
| R-B.17 | Segurança da Informação | Autenticação | 2 | base | Confidencialidade | 18 | Verifica se o sistema confirma a identidade de quem acessa (senha, 2FA, biometria) antes de liberar o acesso. |
| R-B.18 | Segurança da Informação | Confidencialidade | 2 | base | Autenticação; Integridade | 18 | Verifica se cada informação sensível só é acessada por quem tem autorização, com controle de acesso e criptografia. |
| R-B.19 | Segurança da Informação | Integridade | 2 | base | Confidencialidade | 18 | Verifica se os dados não podem ser alterados ou corrompidos sem autorização. |
| R-B.20 | Segurança da Informação | Não repúdio | 1 | base | Autenticação | 18 | Verifica se o sistema guarda provas de quem fez cada ação, para que ninguém possa negá-la depois. |
| R-B.21 | Segurança da Informação | Penetração | 2 | base | Análise de perigos | 18 | Simula um ataque real, como um invasor faria, para encontrar e explorar vulnerabilidades. |
| R-B.22 | Manutenibilidade | Regressão | 3 | base | Análise de impacto | 19 | Executa de novo testes que já passavam para garantir que uma mudança não quebrou o que funcionava. |
| R-B.23 | Manutenibilidade | Análise estática | 2 | base | Revisão de código | 19 | Examina o código sem executá-lo, com ferramentas, para medir complexidade, duplicação e más práticas. |
| R-B.24 | Manutenibilidade | Revisão de código | 2 | base | Análise estática | 19 | Outra pessoa da equipe lê o código antes da integração, procurando defeitos e trechos difíceis de entender ou de mudar. |
| R-B.25 | Manutenibilidade | Análise de impacto | 2 | base | Regressão | 19 | Antes de uma mudança, identifica quais partes do sistema dependem do trecho alterado e serão afetadas. |
| R-B.26 | Flexibilidade | Escalabilidade | 3 | base | Carga; Pico | 20 | Verifica se o sistema cresce ou encolhe, por exemplo adicionando servidores, para acompanhar a demanda sem ser reescrito. |
| R-B.27 | Flexibilidade | Adaptabilidade | 2 | base | Coexistência; Retrocompatibilidade | 20 | Verifica se o sistema funciona em ambientes diferentes (sistemas operacionais, navegadores, telas) sem grandes mudanças. |
| R-B.28 | Flexibilidade | Instalabilidade | 2 | base | Adaptabilidade | 20 | Verifica se o sistema se instala, atualiza e desinstala sem erros nos ambientes previstos. |
| R-B.29 | Flexibilidade | Substituibilidade | 2 | base | Interoperabilidade | 20 | Verifica se um componente pode ser trocado por outro equivalente, como o banco de dados ou o provedor de pagamento, sem afetar o funcionamento. |
| R-B.30 | Segurança Operacional | Falha segura | 3 | módulo | Tolerância a falhas; Recuperação | 21 | Provoca uma falha e verifica se o sistema vai para um estado que não causa dano, como o elevador que trava os freios. |
| R-B.31 | Segurança Operacional | Alerta de perigo | 2 | módulo | Proteção contra erro do usuário | 21 | Verifica se o sistema avisa as pessoas a tempo e com clareza quando surge uma situação perigosa. |
| R-B.32 | Segurança Operacional | Restrição operacional | 2 | módulo | Proteção contra erro do usuário | 21 | Verifica se o sistema respeita os limites seguros de operação e se recusa a operar fora deles. |
| R-B.33 | Segurança Operacional | Análise de perigos | 2 | módulo | Penetração | 21 | Identifica, antes da operação, quais falhas do software podem causar dano a pessoas ou ao ambiente e qual a gravidade de cada uma. |

## Apêndice C — Cartas de Incidente

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-C.0.1 | componente | O jogo base tem 14 incidentes, 2 por categoria-chave, dos quais 3 são severos. Os incidentes 15 e 16 pertencem ao módulo. | 22 | `incidentes.base=14`; `incidentes.por_categoria=2`; `incidentes.severos_base=3` | MET-04 |
| R-C.0.2 | regra | Incidente severo: ter qualquer um dos testes-chave no sistema evita o item extra de dano. Uma carta da categoria secundária não substitui o teste-chave. | 22 | — | R-8.1.3 |
| R-C.0.3 | regra | Dano impresso no verso: 2 sem carta da categoria-chave; 1 por Alerta ativo na categoria-chave; 1 se severo e sem nenhum teste-chave. | 22 | `dano.incidente.sem_cobertura=2`; `dano.incidente.alerta=1`; `dano.incidente.severo_sem_teste_chave=1` | Igual a R-8.1.1 a R-8.1.3 |
| R-C.0.4 | nota | Dos testes-chave, o primeiro é o indicado diretamente para o defeito e o segundo, quando existe, é um teste próximo aceito no gabarito. Isso não cria uma segunda categoria pontuável. | 22 | — | |
| R-C.0.5 | nota | Pares de confusão que o baralho cobre: Carga × Estresse × Pico × Resistência; Pico × Escalabilidade; Recuperação × Tolerância a falhas × Falha segura; Interoperabilidade × Contrato de API; Adaptabilidade × Coexistência × Retrocompatibilidade; Autenticação × Confidencialidade × Integridade; Regressão × Análise de impacto; Análise estática × Revisão de código. | 22 | — | MOD-03 |

| ID | Nome | Categoria-chave | Secundária | Testes-chave | Severo | Conjunto | Pág. |
|---|---|---|---|---|---|---|---|
| R-C.01 | Abertura da venda de ingressos | Desempenho | Confiabilidade | Pico; Estresse | não | base | 23 |
| R-C.02 | Feriado prolongado sem reinicialização | Desempenho | — | Resistência; Carga | não | base | 23 |
| R-C.03 | Integração com o Sistema Internacional | Compatibilidade | — | Interoperabilidade; Contrato de API | não | base | 24 |
| R-C.04 | Nova política de segurança da TI | Compatibilidade | — | Coexistência | não | base | 24 |
| R-C.05 | Lançamento para o público idoso | Interação | — | Acessibilidade; Teste com usuários | não | base | 25 |
| R-C.06 | Fechamento da folha de pagamento | Interação | — | Proteção contra erro do usuário; Teste com usuários | não | base | 25 |
| R-C.07 | Queda de energia no data center | Confiabilidade | — | Recuperação; Engenharia do Caos | sim | base | 26 |
| R-C.08 | Manutenção no provedor de nuvem | Confiabilidade | — | Tolerância a falhas; Engenharia do Caos | não | base | 26 |
| R-C.09 | Cliente contesta uma compra | Segurança da Informação | — | Não repúdio; Autenticação | sim | base | 27 |
| R-C.10 | Novo portal do aluno | Segurança da Informação | — | Confidencialidade; Penetração | não | base | 27 |
| R-C.11 | Deploy de sexta à tarde | Manutenibilidade | — | Regressão; Análise de impacto | não | base | 28 |
| R-C.12 | Novo desenvolvedor na equipe | Manutenibilidade | — | Análise estática; Revisão de código | não | base | 28 |
| R-C.13 | Campanha viral | Flexibilidade | Desempenho | Escalabilidade | sim | base | 29 |
| R-C.14 | Atualização automática dos computadores | Flexibilidade | Interação | Adaptabilidade | não | base | 29 |
| R-C.15 | Hospital universitário | Segurança Operacional | Confiabilidade | Falha segura; Análise de perigos | sim | módulo | 30 |
| R-C.16 | Frota de drones de entrega | Segurança Operacional | — | Restrição operacional; Análise de perigos | não | módulo | 30 |

### Relatos (frente das cartas)

Os relatos são a única informação que os jogadores têm para diagnosticar (R-2.1.1). O narrador (`cf narrar`) os reproduz.

| Incidente | Relato |
|---|---|
| 01 | Na abertura da venda, o site ficou 15 minutos sem responder. 50 mil pessoas entraram no mesmo segundo. Às 10h20 tudo voltou ao normal sozinho, com os mesmos servidores. |
| 02 | Na terça depois do feriado, o sistema estava muito mais lento do que na sexta. O número de usuários foi o mesmo nos dois dias, e a memória do servidor subiu sem parar desde o último reinício. |
| 03 | Os dados saem corretos do app, mas o sistema parceiro grava as datas invertidas: 03/04 vira 4 de março. |
| 04 | O sistema de ponto passou a travar ao abrir nos computadores da empresa. O problema começou quando o novo antivírus foi instalado nas mesmas máquinas. Sem ele, o sistema funciona normalmente. |
| 05 | Muitos usuários do novo app desistem antes de concluir o cadastro. A letra não aumenta quando o usuário amplia a fonte do celular, e os botões são pequenos demais para dedos menos precisos. |
| 06 | No fechamento da folha, 3 mil registros sumiram de uma vez. Um analista clicou em "Excluir todos", ao lado de "Exportar todos", e o sistema apagou tudo na hora. |
| 07 | Depois de uma queda de energia, pedidos de clientes desapareceram. Quando a energia voltou, o sistema reiniciou normalmente, mas os pedidos das últimas 2 horas não estavam mais no banco. |
| 08 | Durante uma manutenção programada do provedor, o sistema inteiro saiu do ar. Só um dos três servidores de banco de dados foi desligado; os outros dois continuavam funcionando. |
| 09 | Um cliente diz que não fez uma compra de R$ 2 mil registrada na conta dele. A compra foi feita pelo app, com a conta dele, mas a empresa não tem nenhum registro que prove quem confirmou a operação. |
| 10 | Alunos reclamam que suas notas estão sendo vistas por outras pessoas. Um aluno fez login normalmente e, trocando o número de matrícula no endereço da página, abriu as notas dos colegas. |
| 11 | Na segunda-feira, clientes reclamaram que o cupom de desconto não funciona mais. Na sexta, a equipe publicou uma correção no cálculo do frete. O cupom funcionava havia meses, e ninguém mexeu nele. |
| 12 | Uma mudança simples numa regra de desconto levou três semanas para ficar pronta. A mesma lógica estava copiada em 14 arquivos, dentro de funções com mais de 500 linhas. |
| 13 | Os usuários dobraram em uma semana, e o sistema ficou lento. A equipe adicionou servidores, mas cada servidor novo melhora cada vez menos o tempo de resposta. |
| 14 | O painel de vendas abre com botões desalinhados, e o gráfico não carrega. O problema começou depois que o navegador dos usuários foi atualizado. Na versão anterior, tudo funcionava. |
| 15 | Durante a madrugada, um paciente recebeu medicamento demais. O software da bomba de infusão travou, e a bomba continuou injetando na última velocidade programada, sem parar. |
| 16 | Um drone de entrega caiu num estacionamento. Havia rajadas de vento acima do limite do fabricante, e mesmo assim o drone decolou normalmente. |

## Registro da partida (Folha de registro)

A seção "Registro da partida" (p. 35) define o que o observador anota. O comando `cf folha` exporta exatamente estes campos, para que dados simulados e reais tenham o mesmo esquema.

| ID | Tipo | Regra | Pág. | Parâmetros | Notas |
|---|---|---|---|---|---|
| R-REG.1 | regra | Por incidente, anota-se o diagnóstico de cada jogador, inclusive o do Auditor, separando categoria-chave, secundária e outra categoria. Só a categoria-chave conta como acerto. | 35 | — | MET-05 |
| R-REG.2 | regra | Por defesa, anotam-se a categoria atacada, o teste nomeado, se era blefe, a decisão do Auditor e se houve contestação. | 35 | — | AMB-15 |
| R-REG.3 | regra | No fim, anotam-se as fichas de cada jogador. | 35 | — | |

## Variantes de playtest

Variantes que a configuração deve permitir ligar e desligar (seção 3.2 do prompt). O valor marcado como "atual" é a regra da v2.2. A mecânica de VAR-02, VAR-03, VAR-04 e VAR-06 foi decidida pelo autor em 2026-11-10 (coluna Mecânica). No YAML, VAR-02 a VAR-06 ficam no bloco opcional `variantes`; sem o bloco, vale a regra da versão.

| ID | Variante | Valores | Fonte | Mecânica |
|---|---|---|---|---|
| VAR-01 | Punição do blefe descoberto | sem punição; 1 ficha (atual); 2 fichas | prompt 3.2; R-7.3.4 | `disputa.contestacao_blefe.defensor_paga`: 0, 1 ou 2; o Alerta e o ganho do banco continuam |
| VAR-02 | Custo da explicação que não confere | igual a "Falhou" (atual); custo extra | prompt 3.2; R-7.2.3b | além do "Falhou", o defensor perde 1 ficha para o banco (`variantes.custo_extra_da_explicacao`) |
| VAR-03 | Auditor | jogador rotativo (atual); externo, que não joga | prompt 3.2; R-7.1.1 | o motor julga a explicação e acerta 95 de cada 100 (MOD-02, perfil experiente); todos jogam e diagnosticam |
| VAR-04 | Alvo na Homologação | livre (atual); vizinho designado da v2.0 (esquerda, direita, esquerda) | prompt 3.2; PDF p. 33 | só o alvo muda: sem limite de testes e com o bug duplicado; sem teste legal contra o vizinho, o jogador passa |
| VAR-05 | Limite de testes recebidos por ciclo | sem limite (atual); 2 | prompt 3.2; PDF p. 34 | quem já recebeu 2 testes no ciclo não pode ser alvo |
| VAR-06 | Voto da mesa | desligado (atual); palpite da plateia sobre a posse da carta; voto sobre a explicação, antes do Auditor | prompt 3.2; PDF p. 35; AMB-30; AMB-31 | só o palpite do PDF: depois da conferência, quem não é atacante, defensor nem Auditor vota em segredo; os votos são revelados antes da decisão do atacante; havendo contestação, quem acertou ganha 1 ficha do banco. O bot vota "blefe" quando a chance estimada passa de 1/2. O voto sobre a explicação ficou fora |
| VAR-07 | Compras por Planejamento | 3 (atual); 2 | prompt 3.2; PDF p. 34 | `planejamento.compras` |
| VAR-08 | Número de jogadores | 4; 5 (6 só com a COR-01 desligada, para medir o problema do baralho) | prompt 3.2; R-1.2; COR-01 | número de jogadores do cenário |
| VAR-09 | Módulo de Segurança Operacional | desligado (jogo base); ligado | PDF seção 11 | `modulo_seguranca_operacional` |
| VAR-10 | Bug duplicado (ablação, regra da 2.1) | proibido (atual); permitido | PDF p. 33 (histórico); R-7.4.2 | pode testar categoria em que o alvo já tem Alerta; o atacante ganha a ficha, sem cubo novo (`ablacoes.bug_duplicado_permitido`) |
| VAR-11 | Testes por ciclo (ablação, regra da 2.1) | sem limite (atual); 1 | PDF p. 33 (histórico); R-7.4.1 | cada jogador faz no máximo 1 teste por ciclo; depois disso passa (`ablacoes.testes_por_ciclo`) |

Texto do palpite da plateia no PDF (p. 35, "plano B, fora das regras"): antes de o atacante decidir se contesta, quem está fora da disputa vota se a defesa é verdade ou blefe; se houver contestação, quem acertou ganha 1 ficha.

## Hipóteses de modelo

Não são regras do jogo. São o que o simulador precisa supor para substituir pessoas por bots. Ficam separadas para que nenhuma hipótese passe por regra. Os parâmetros de cada uma serão perguntados ao autor na fase em que entram.

| ID | Hipótese | Substitui | Fase |
|---|---|---|---|
| MOD-01 | A explicação do defensor está correta ou não conforme um sorteio do perfil de conhecimento do defensor. | A fala do jogador (R-7.2.2a) | 1 (mínimo) e 2 |
| MOD-02 | O Auditor diz "confere" ou "não confere" conforme a sua precisão ao julgar, podendo errar nos dois sentidos. | O julgamento do Auditor (R-7.2.3) | 1 (mínimo) e 2 |
| MOD-03 | O diagnóstico segue um modelo de confusão de poucos parâmetros: chance de acerto, chance de cair na secundária ao errar, e o resto do erro distribuído pelas categorias vizinhas do "Não confundir com". | A leitura do relato (R-8.0.2) | 1 (mínimo) e 2 |
| MOD-04 | O que um bot deduz do Radar usa o mesmo modelo de MOD-03. A leitura de cada incidente é sorteada uma vez e vale para o planejamento, o ataque e o diagnóstico (autor, 2026-11-10). | A interpretação do Radar (R-4.12) | 2 |
| MOD-05 | A duração da partida é a soma de tempos configuráveis por ação (turno de Planejamento, disputa, defesa, Produção). | O relógio da mesa (R-6.7, R-7.2.2d) | 1b |
| MOD-06 | Todo bot sabe quais testes pertencem a cada categoria. | O Cartão de Referência (R-2.0.5) | 1 |
| MOD-07 | O atacante contesta nunca, sempre, ou quando a chance estimada de blefe é pelo menos o limiar de R-7.3.5, calculado com os números das regras em uso (autor, 2026-11-10). | O julgamento do atacante (R-7.2.4) | 2 |
| MOD-08 | Todo bot conhece a composição do baralho (Apêndice B: cópias de cada teste) e quantos incidentes são severos (3 de 14). Não conhece o verso de nenhum incidente. | O texto das regras, que todos podem ler antes de jogar | 2 |
| MOD-09 | Um bot estima a chance de um adversário não ter um teste ou uma categoria contando as cartas que ainda não viu: as cartas escondidas do sistema dele são tratadas como sorteadas, sem reposição, entre essas. Se o viu pegar a carta do Backlog, supõe que ela está no sistema. | A dedução do jogador atento | 2 |

## Requisitos derivados da tabela "Parâmetros a validar no playtest"

As páginas 34 e 35 do PDF definem o que o simulador deve medir. A definição exata de cada métrica e a zona de aceite ficam em `configs/requisitos.yaml`.

| Parâmetro do PDF (p. 34 e 35) | O que validar | Onde |
|---|---|---|
| Fichas iniciais | Ninguém chega a 0 com frequência antes do ciclo 3 | REQ-07 |
| Sistema inicial | O primeiro incidente não decide a partida | REQ-12 |
| Compra por Planejamento | Partida entre 40 e 50 minutos; se passar, voltar para 2 | REQ-08; VAR-07 |
| Colocação livre, teto 5, sem troca | Os dois estilos aparecem na mesa | REQ-11 |
| Contestação | Nenhuma estratégia pura domina; blefes bem-sucedidos entre 30% e 50% | REQ-04; REQ-05 |
| Dano de incidente | Incidentes pesam, mas não decidem a partida sozinhos | REQ-13 |
| Severos | Em média 0,64 severo por partida | MET-04 |
| Diagnóstico sem alternativas na frente | Acertos na categoria-chave e confusões | MET-05 (comparável com dados reais) |
| Participação do Auditor | Manuseio físico e igualdade de oportunidades | fora do simulador |
| Alvo livre, sem limite de testes | Ninguém recebe muito mais testes que os outros, sobretudo o de menor placar | REQ-06; VAR-05 |
| Bug duplicado | Quantas categorias diferentes são testadas por partida | MET-03 |
| Sem Hotfix | Alertas antes de um incidente da mesma categoria não dispersam demais o placar | REQ-14 |
| Tempo parado | Menos de 5 minutos parado por ciclo | REQ-10; VAR-06 |
| Vocabulário | Cada defesa leva até 1 minuto; Auditores julgam da mesma forma | MOD-05; fora do simulador |
| Duração | Entre 40 e 50 minutos com 4 a 6 jogadores (4 e 5 depois da COR-01) | REQ-08 |
| Categoria secundária | Se a relação complementar ajuda a aprender | fora do simulador |
| Leitura e repetição | Diagnóstico por evidência ou por memorização | fora do simulador |

## O que não é regra vigente

As páginas 31 a 33 do PDF trazem o histórico das versões 2.0, 2.1 e 2.2. O histórico da 2.1 descreve regras que a 2.2 substituiu e não deve ser usado como regra. Ele só é fonte para as variantes VAR-04 e VAR-05.

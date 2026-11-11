# Ambiguidades e omissões das regras

Pontos em que as fontes são ambíguas ou omissas. Nenhum é resolvido em silêncio: cada entrada traz a regra, o trecho, as interpretações possíveis, a sugestão do assistente e a decisão do autor.

**Quem decide é o autor.** A sugestão só vira padrão depois da resposta dele, registrada aqui com data e também em `docs/DIARIO_DE_BORDO.md`. Enquanto o estado for "aguardando decisão", a parte do motor que depende do ponto não é implementada.

Sempre que for barato, a escolha fica configurável, com a chave indicada em "Configuração". Quando uma regra é aplicada segundo uma destas decisões, o evento do registro de auditoria cita o identificador `AMB-<nn>`.

Duas respostas do autor foram além da interpretação e mudaram regra. Elas estão em AMB-06 e AMB-12 e viraram as correções COR-01 e COR-02 (seção "Correções do autor" de `docs/especificacao_v2_2.md` e `docs/HISTORICO_REGRAS.md`).

## Resumo

| ID | Ponto | Versão | Impacto | Estado |
|---|---|---|---|---|
| AMB-01 | Mínimo 0 e ordem entre diagnóstico e dano | v2.2 | médio | decidido: diagnóstico antes |
| AMB-02 | Lição aprendida sem carta da categoria no Backlog | v2.2 | baixo | decidido: não acontece |
| AMB-03 | Quem não pode testar passa automaticamente | v2.2 | nenhum | decidido: passa |
| AMB-04 | Quem já passou pode ser testado | v2.2 | alto | decidido: continua alvo |
| AMB-05 | Auditor envolvido na disputa | v2.2 | baixo | decidido: substituto à esquerda |
| AMB-06 | Baralho e descarte vazios ao mesmo tempo | v2.2 | médio | decidido: máximo de 5 jogadores (COR-01) e pular a compra |
| AMB-07 | Carta repetida na preparação | v2.2 | baixo | decidido: fundo do baralho |
| AMB-08 | Escolha do primeiro jogador | v2.2 | nenhum | decidido: assento 0 |
| AMB-09 | Ordem dentro do turno de Planejamento | v2.2 | nenhum | decidido: compra e depois coloca |
| AMB-10 | Lista fechada do que é informação pública | v2.2 | médio | decidido: lista proposta |
| AMB-11 | Como se comprova cobertura na Produção | v2.2 | médio | decidido: revelação mínima |
| AMB-12 | Alerta no Critical Failure e duração dos Alertas | v2.2 | alto | decidido: regra nova dos Alertas (COR-02); no fim de jogo o cubo fica |
| AMB-13 | Pontuação final e mínimo 0 | v2.2 | baixo | decidido: saldo único |
| AMB-14 | Empate depois dos dois critérios | v2.2 | baixo | decidido: vitória dividida |
| AMB-15 | O que conta como blefe | v2.2 | médio | decidido: teste nomeado fora do sistema |
| AMB-16 | Nomear teste de outra categoria | v2.2 | baixo | decidido: não modelado na Fase 1 |
| AMB-17 | Limites físicos de fichas e cubos | v2.2 | baixo | decidido: ilimitados, com medição |
| AMB-20 | v1: blefe aceito | v1 | alto | decidido: vale a declaração |
| AMB-21 | v1: baralho da Tabela 3 | v1 | baixo | decidido: Tabela 3 |
| AMB-22 | v1: carta tirada ao acaso | v1 | baixo | decidido: ao acaso |
| AMB-23 | v1: destino da carta de ataque quando a falha é encontrada | v1 | alto | decidido: descarte |
| AMB-24 | v1: uma carta em mais de uma combinação de pontos | v1 | alto | decidido: uma combinação por carta |
| AMB-25 | v1: alvo com sistema vazio | v1 | médio | decidido: pode ser alvo |
| AMB-26 | v1: o que identifica um teste | v1 | baixo | decidido: atributo e nome |
| AMB-27 | v1: número de jogadores e o que é uma partida | v1 | médio | decidido: partida é uma rodada |
| AMB-28 | v1: Critical Failure na mão inicial | v1 | baixo | decidido: fica entre as cartas de teste |
| AMB-29 | v1: empate | v1 | baixo | decidido: vitória dividida |
| AMB-30 | Palpite da plateia (VAR-06): o Auditor da disputa vota? | v2.2 (variante) | baixo | decidido: não vota |
| AMB-31 | Palpite da plateia (VAR-06): de onde vem a ficha de quem acertou | v2.2 (variante) | baixo | decidido: do banco |
| AMB-32 | Custo do teste (VAR-12): quem não tem ficha para pagar pode fazer o teste pago? | v2.2 (proposta) | baixo | decidido: não pode |

Os números 18 e 19 ficam reservados para novos pontos da v2.2.

**Princípio registrado pelo autor em 2026-11-09:** "Sobre a pontuação no geral busque manter simplicidade." Vale para qualquer ponto futuro de pontuação.

## v2.2

### AMB-01 — Mínimo 0 e ordem entre diagnóstico e dano

- **Regras:** R-5.2, R-8.0.4, R-8.0.5
- **Trecho:** "Mínimo 0. Quem precisa pagar mais do que tem paga o que tiver." (p. 6). Na Produção, o passo 4 pontua o diagnóstico e o passo 5 aplica o dano (p. 9).
- **Interpretações:**
  - (a) Ordem impressa: primeiro o +1 do diagnóstico, depois o dano. Jogador com 1 ficha que acerta e leva dano 3: sobe para 2 e cai para 0.
  - (b) Dano antes do diagnóstico: cai de 1 para 0 e depois sobe para 1.
  - Aplicar o saldo de uma vez dá o mesmo resultado de (a).
- **Sugestão:** (a). É a ordem dos passos do PDF e a do exemplo da p. 10 ("pega 1 ficha e devolve 3").
- **Configuração:** `producao.ordem: diagnostico_primeiro | dano_primeiro`
- **Impacto:** médio. Só muda o resultado de quem tem menos fichas que o dano. Em (b), quem acerta o diagnóstico nunca termina a Produção em 0.
- **Estado:** decidido pelo autor em 2026-11-09: (a), diagnóstico antes do dano

### AMB-02 — Lição aprendida sem carta da categoria no Backlog

- **Regras:** R-8.0.6, R-8.0.6a
- **Trecho:** "quem acertou a categoria-chave pode pegar 1 carta de categoria X do Backlog para a mão. Reponha o Backlog após cada retirada." (p. 9)
- **Interpretações:**
  - (a) Sem carta de X no Backlog, a retirada não acontece.
  - (b) O jogador pega a carta do topo do baralho.
  - (c) Procura-se uma carta de X no baralho.
- **Sugestão:** (a). Dois detalhes decorrem do texto: "pode" torna a retirada opcional, então é decisão do bot; e, como o Backlog é reposto depois de cada retirada, uma carta de X recém-virada serve ao próximo jogador da ordem.
- **Configuração:** `licao_aprendida.sem_carta: nada`
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-09: (a), a retirada não acontece; pegar a carta é opcional

### AMB-03 — Quem não pode testar passa automaticamente

- **Regras:** R-4.6, R-7.0.1, R-7.0.3
- **Trecho:** "Na sua vez, você testa qualquer jogador ou passa." (p. 7)
- **Interpretações:**
  - (a) Quem não tem jogada legal passa automaticamente e sai da fase. Isso vale para mão vazia e para o caso em que toda combinação de carta e alvo é proibida pelo bug duplicado.
  - (b) O jogador continua na roda sem agir, e a fase termina quando ninguém mais pode ou quer testar.
- **Sugestão:** (a), com o evento marcado como passagem automática. As duas dão o mesmo placar, porque durante a Homologação a mão não cresce e os Alertas não saem: quem ficou sem jogada não volta a ter.
- **Configuração:** não precisa
- **Impacto:** nenhum no placar; muda o registro e a duração estimada
- **Estado:** decidido pelo autor em 2026-11-09: (a), passa automaticamente

### AMB-04 — Quem já passou pode ser testado

- **Regras:** R-7.0.3, R-7.0.1
- **Trecho:** "Quem passa sai da Homologação deste ciclo" (p. 7)
- **Interpretações:**
  - (a) Sai só como atacante: continua podendo ser testado e se defende normalmente.
  - (b) Sai por completo: não pode mais ser alvo neste ciclo.
- **Sugestão:** (a). Em (b), passar cedo daria imunidade, e o primeiro jogador teria a vantagem de se proteger antes de todos.
- **Configuração:** `homologacao.quem_passou_pode_ser_alvo: true | false`
- **Impacto:** alto
- **Estado:** decidido pelo autor em 2026-11-09: (a), continua podendo ser testado

### AMB-05 — Auditor envolvido na disputa

- **Regras:** R-7.1.4
- **Trecho:** "Se o Auditor for atacante ou defensor numa disputa, a função passa, só nela, ao jogador não envolvido mais próximo à sua esquerda." (p. 7)
- **Interpretações:**
  - (a) O substituto é procurado a partir da esquerda do Auditor titular, em sentido horário, pulando o atacante e o defensor.
- **Sugestão:** (a), que é a leitura literal. O evento da disputa registra o Auditor titular do ciclo e o Auditor da disputa.
- **Configuração:** não precisa
- **Impacto:** baixo
- **Estado:** decidido pelo autor (prompt, seção 6): a função passa ao não envolvido mais próximo à esquerda e isso aparece no registro

### AMB-06 — Baralho e descarte vazios ao mesmo tempo

- **Regras:** R-1.2, R-6.1, R-6.1b, R-6.6, R-8.0.6a, R-3.8
- **Trecho:** "Baralho vazio. Embaralhe o descarte para formar um novo baralho." (p. 6)
- **Problema:** com 6 jogadores a preparação usa 17 cartas e sobram 46; os 3 Planejamentos compram 6 × 3 × 3 = 54. Só as cartas de ataque voltam ao descarte. Se houver menos de 8 testes antes do fim do terceiro Planejamento, falta carta. Com 5 jogadores sobram 48 e compram-se 45, mas cada Lição aprendida tira mais uma do baralho, então o caso ainda pode acontecer, raramente. Com 4 jogadores sobram 50 e a demanda máxima é 48: nunca falta. O texto não diz o que fazer.
- **Interpretações:**
  - (a) A compra ou a reposição que não tem carta não acontece, e o evento é registrado.
  - (b) A partida é encerrada como inválida e contada à parte.
  - (c) Regra nova, como limite de mão ou descarte obrigatório. Isso já é mudança de regra, não interpretação.
- **Sugestão:** (a), medindo a frequência do caso.
- **Configuração:** `jogadores.maximo: 5` (COR-01); `baralho.esgotado: pular_compra | invalidar`
- **Impacto:** médio
- **Estado:** decidido pelo autor em 2026-11-09, em duas partes. Primeira: o jogo passa a ter no máximo 5 jogadores, como correção da própria v2.2 (COR-01); o PDF será atualizado pelo autor. Segunda: para o caso raro que resta com 5 jogadores, vale (a), pular a compra e registrar. A regra impressa (até 6 jogadores) continua disponível por configuração para medir o problema.

### AMB-07 — Carta repetida na preparação

- **Regras:** R-3.4b
- **Trecho:** "Se as 2 forem do mesmo teste, troque uma pela carta do topo do baralho." (p. 4)
- **Interpretações:** para o destino da carta trocada:
  - (a) Fundo do baralho.
  - (b) Reembaralhada no baralho.
  - (c) Descarte.
  - E, se a carta nova repetir de novo: (i) troca-se outra vez até diferir, ou (ii) troca-se uma vez só.
- **Sugestão:** (a) com (i).
- **Configuração:** `preparacao.carta_repetida: fundo | reembaralha | descarte`
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-09: (a) com (i), fundo do baralho, repetindo a troca enquanto as 2 cartas forem do mesmo teste

### AMB-08 — Escolha do primeiro jogador

- **Regras:** R-3.6
- **Trecho:** "Escolha o primeiro jogador." (p. 4)
- **Interpretações:**
  - (a) O assento 0 sempre começa. Os experimentos distribuem os bots pelos assentos em rodízio.
  - (b) O primeiro jogador é sorteado pelo fluxo de aleatoriedade do jogo.
- **Sugestão:** (a). Assim "assento" significa posição na ordem inicial, que é o que o requisito de equidade de assento (REQ-01) mede.
- **Configuração:** `preparacao.primeiro_jogador: assento_0 | sorteio`
- **Impacto:** nenhum sobre as regras; define como REQ-01 é medido
- **Estado:** decidido pelo autor em 2026-11-09: (a), o assento 0 sempre começa

### AMB-09 — Ordem dentro do turno de Planejamento

- **Regras:** R-6.1, R-6.2, R-6.4
- **Trecho:** os passos "1. Comprar 3 cartas" e "2. Colocar cartas no sistema" (p. 6)
- **Interpretações:**
  - (a) O jogador compra as 3 cartas e só depois coloca.
  - (b) O jogador pode intercalar compras e colocações.
- **Sugestão:** (a), a ordem dos passos do PDF. O resultado é o mesmo: colocar uma carta não dá informação nova a quem coloca.
- **Configuração:** não precisa
- **Impacto:** nenhum
- **Estado:** decidido pelo autor em 2026-11-09: (a), compra as 3 e depois coloca

### AMB-10 — Lista fechada do que é informação pública

- **Regras:** R-3.4a, R-5.4, R-6.1c, R-6.2b, R-7.2.1, R-7.2.4b, R-8.0.7b
- **Trecho:** o PDF diz o que é público em pontos isolados ("Toda carta comprada do Backlog é informação pública", "As fichas de cada jogador ficam sempre à vista", "agora todos sabem o que ela é"). O simulador precisa de uma lista fechada para montar a `Observacao` de cada bot.
- **Interpretações:**
  - (a) Lista proposta. **Público:** fichas e Alertas de todos; Backlog; frente dos incidentes do Radar; quantidade de cartas na mão e no sistema de cada jogador; cada carta comprada do Backlog e quem a comprou; o fato de alguém ter comprado do topo, sem a carta; quantas cartas alguém colocou no sistema; a categoria de uma carta colocada quando ela remove um Alerta, porque o cubo sai à vista; cartas de ataque e o descarte; teste nomeado, veredito do Auditor e decisão de aceitar ou contestar; cartas reveladas em contestações e na Produção, que ficam conhecidas até o fim; diagnósticos revelados; gabarito depois de virado; cartas retiradas na Lição aprendida. **Privado do dono:** a própria mão e o próprio sistema. **Oculto de todos:** a ordem do baralho, o verso dos incidentes e os incidentes ainda na Linha do Tempo.
  - (b) A mesma lista, sem tratar como pública a categoria da carta que remove um Alerta.
- **Sugestão:** (a). Na mesa, o cubo sai à vista de todos.
- **Configuração:** não precisa; a lista vira o contrato de `observacao.py` e o teste de não vazamento
- **Impacto:** médio. Define o que os bots podem usar para escolher alvo e para estimar blefe.
- **Estado:** decidido pelo autor em 2026-11-09: (a), a lista proposta inteira. Com a COR-02, colocar carta não remove mais Alerta, então o item da categoria revelada pelo cubo só se aplica quando a regra impressa é religada por configuração.

### AMB-11 — Como se comprova cobertura na Produção

- **Regras:** R-8.0.5a
- **Trecho:** "Para comprovar cobertura, revele as cartas de categoria X do sistema; quem não revela é tratado como sem cobertura." (p. 9)
- **Interpretações:**
  - (a) Revelação mínima: o jogador revela 1 carta de X. Num incidente severo, revela um teste-chave se tiver, o que comprova as duas coisas.
  - (b) O jogador revela todas as cartas de X que tem.
  - (c) É decisão do bot, que pode esconder a carta e pagar o dano.
- **Sugestão:** (a). É o que um jogador faz para não pagar sem mostrar mais do que precisa.
- **Configuração:** `producao.revelacao: minima | todas | livre`
- **Impacto:** médio. Carta revelada vira informação pública para os ataques seguintes.
- **Estado:** decidido pelo autor em 2026-11-09: (a), revelação mínima

### AMB-12 — Alerta no Critical Failure e duração dos Alertas

- **Regras:** R-6.9, R-6.2b, R-9.1.6, R-9.2.4, R-8.0.7
- **Trecho:** a seção 9.1 lista o item "Alerta ativo na categoria X: 1" (p. 10) e não fala em limpeza; a 9.2 cobra "-1 por cubo de Alerta ainda ativo" (p. 11).
- **Interpretações:** para a pergunta original, se o cubo sai depois do Critical Failure:
  - (a) Literal: o Alerta não sai. Custa 1 no Critical Failure e mais 1 na pontuação final.
  - (b) O Critical Failure limpa os Alertas da categoria sorteada, como a limpeza da Produção.
- **Sugestão:** (a), por ser o que o texto diz.
- **Configuração:** `alertas.limpeza_no_planejamento: sim | nao` (COR-02); `critical_failure.limpa_alertas: false | true`
- **Impacto:** alto, por causa da regra nova
- **Estado:** decidido pelo autor em 2026-11-09, em duas partes. Primeira, uma regra nova (COR-02): todos os cubos de Alerta saem no início de cada Planejamento, e a regra de remover o Alerta colocando uma carta da categoria (R-6.2b) é revogada. O autor confirmou as consequências: nos ciclos 1 e 2 o Alerta só pesa na Produção do mesmo ciclo e, fora da categoria-chave, não custa nada ao defensor. Segunda, para o fim de jogo vale (a): os Alertas recebidos no ciclo 3 ficam até o fim, custam 1 no Critical Failure se a categoria for sorteada e 1 na pontuação final. A regra impressa continua disponível por configuração para medir o efeito da mudança.

### AMB-13 — Pontuação final e mínimo 0

- **Regras:** R-9.2.1, R-9.2.2, R-9.2.3, R-9.2.4, R-5.2
- **Trecho:** "Todos viram o sistema inteiro para cima e acertam as fichas com o banco" (p. 11)
- **Interpretações:**
  - (a) Saldo único: somam-se ganhos e perdas e aplica-se o piso 0 ao resultado.
  - (b) Perdas antes dos ganhos. Jogador com 0 fichas, 3 de amplitude e 1 Alerta termina com 2 em (a) e com 3 em (b).
- **Sugestão:** (a), que corresponde a "acertar as fichas" de uma vez.
- **Configuração:** `final.ordem: saldo | perdas_primeiro`
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-09: (a), saldo único, seguindo o princípio de manter a pontuação simples

### AMB-14 — Empate depois dos dois critérios

- **Regras:** R-9.2.7, R-9.2.8
- **Trecho:** "vence quem tem menos Alertas ativos; persistindo, quem acertou mais diagnósticos pela categoria-chave" (p. 11)
- **Interpretações:**
  - (a) Vitória dividida: com k empatados, cada um conta 1/k nas taxas de vitória.
  - (b) Um terceiro critério, a definir.
  - (c) Sorteio.
- **Sugestão:** (a).
- **Configuração:** `final.empate: dividido | sorteio`
- **Impacto:** baixo nas regras; define como as taxas de vitória são calculadas
- **Estado:** decidido pelo autor em 2026-11-09: (a), vitória dividida

### AMB-15 — O que conta como blefe

- **Regras:** R-7.2.2b, R-7.2.4a, R-REG.2
- **Trecho:** "o defensor precisa revelar do próprio sistema uma carta exatamente do teste que nomeou" (p. 7)
- **Caso:** o defensor tem Carga no sistema e nomeia Estresse.
- **Interpretações:**
  - (a) É blefe. Se contestado, ele não consegue revelar Estresse e perde (R-7.3.4). A Folha marca "era blefe" sempre que o teste nomeado não está no sistema.
  - (b) Só é blefe quando o defensor não tem nenhuma carta da categoria.
- **Sugestão:** (a), a leitura literal.
- **Configuração:** não precisa
- **Impacto:** médio. Define a métrica de blefe (REQ-05) e abre uma jogada: quem tem a categoria mas não sabe explicar o teste que tem pode nomear outro que sabe.
- **Estado:** decidido pelo autor em 2026-11-09: (a), é blefe sempre que o teste nomeado não está no sistema

### AMB-16 — Nomear teste de outra categoria

- **Regras:** R-7.2.2c
- **Trecho:** "Nomear um teste de outra categoria conta como 'Falhou'." (p. 7)
- **Interpretações:**
  - (a) Os bots nunca cometem esse erro: a ação não é oferecida.
  - (b) O erro tem uma probabilidade no perfil de conhecimento.
- **Sugestão:** (a) na Fase 1, com reavaliação na Fase 2, quando o perfil iniciante for definido.
- **Configuração:** `conhecimento.erro_de_categoria: 0` (em (b))
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-09: (a) na Fase 1. O ponto volta a ser perguntado na Fase 2, com o perfil iniciante.

### AMB-17 — Limites físicos de fichas e cubos

- **Regras:** R-2.0.7, R-2.0.8
- **Trecho:** "60 de valor 1 e 15 de valor 5"; "Cubos de Alerta (vermelhos): 30" (p. 2)
- **Problema:** o banco tem 135 fichas e 30 cubos. Com 5 jogadores e 7 categorias cabem até 35 Alertas ao mesmo tempo, e 40 com o módulo.
- **Interpretações:**
  - (a) No simulador os componentes são ilimitados, e o pico de fichas e de cubos em uso é medido (MET-06).
  - (b) Os limites valem, e o motor precisa de uma regra para a falta.
- **Sugestão:** (a). A medida diz se a quantidade de peças do jogo físico é suficiente.
- **Configuração:** não precisa
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-09: (a), componentes ilimitados no simulador, com medição do pico de uso

## v1

### AMB-20 — v1: blefe aceito

- **Regras:** V1-4.3.8, V1-4.3.10a
- **Trecho:** "the standard rule from Performing a Test applies (Successful Defense or Flaw Discovered, depending on the truthfulness of the defender's claim about the card they actually have for that attribute). The play proceeds based on the attacker's trust in the defender's word." (p. 6). A regra é circular: manda aplicar pela verdade, mas a carta não é revelada.
- **Interpretações:**
  - (a) Pela verdade: o motor conhece o estado e aplica defesa ou falha conforme a carta que o defensor realmente tem.
  - (b) Vale a declaração: aceito, conta como defesa bem-sucedida, sem verificação.
- **Consequência de (a):** blefar nunca compensa. Aceito, a falha é aplicada do mesmo jeito (perde 1 carta, igual a admitir); contestado, o defensor perde 2. Um bot racional não blefa e, por isso, ninguém contesta. Isso contradiz o diagnóstico da v1 no briefing (slide 4: "Blefe aceito nunca é verificado, então declarar cobertura sempre compensa"). Em (b), declarar que tem é sempre vantajoso, que é o que o slide descreve.
- **Sugestão:** manter (a) como padrão, por ser a decisão registrada no prompt, e rodar o Experimento 1 nas duas.
- **Configuração:** `v1.blefe_aceito: declaracao | verdade`
- **Impacto:** alto
- **Estado:** decidido pelo autor em 2026-11-09: (b), vale a declaração, como acontecia na mesa. Substitui a decisão anterior do prompt (seção 6), que era resolver pela verdade. Na defesa aceita, o defensor fica com a carta de ataque (V1-4.3.7), mesmo quando blefou.

### AMB-21 — v1: baralho da Tabela 3

- **Regras:** V1-T3.1 a V1-T3.18
- **Trecho:** Tabela 3 (p. 5), com Compatibilidade em 6 cartas e nomes de teste trocados.
- **Interpretações:**
  - (a) Usar as quantidades por atributo da Tabela 3, como impressas.
  - (b) Corrigir o baralho para 9 cartas por atributo.
- **Sugestão:** (a).
- **Configuração:** `v1.baralho: tabela_3`
- **Impacto:** baixo
- **Estado:** decidido pelo autor (prompt, seção 6): usar a Tabela 3, que é o baralho que foi jogado

### AMB-22 — v1: carta tirada ao acaso

- **Regras:** V1-4.2.3, V1-4.3.6, V1-4.3.11, V1-4.3.12
- **Trecho:** "their choice from the face-down system cards"; "of their choice, without seeing it" (p. 6)
- **Interpretações:**
  - (a) Como as cartas estão viradas para baixo, a escolha é um sorteio do fluxo de aleatoriedade do jogo.
  - (b) O bot escolhe, usando o que sabe de cartas já reveladas.
- **Sugestão:** (a), aplicada a toda retirada de carta de um sistema alheio.
- **Configuração:** não precisa
- **Impacto:** baixo
- **Estado:** decidido pelo autor (prompt, seção 6): a carta é escolhida ao acaso

### AMB-23 — v1: destino da carta de ataque quando a falha é encontrada

- **Regras:** V1-4.3.6, V1-4.3.12, V1-4.2.3
- **Trecho:** o artigo só diz para onde vai a carta de ataque na defesa bem-sucedida: "The defender then adds the test card used by the attacker to their own system." (p. 6)
- **Interpretações:**
  - (a) Vai para o descarte e sai do jogo.
  - (b) Vai para o sistema do atacante.
  - (c) Fica com o defensor.
- **Sugestão:** (a), valendo também para a carta Critical Failure usada.
- **Configuração:** `v1.carta_de_ataque_apos_falha: descarte | atacante | defensor`
- **Impacto:** alto. Muda o número de cartas em jogo e o tamanho dos sistemas.
- **Estado:** decidido pelo autor em 2026-11-09: (a), descarte

### AMB-24 — v1: uma carta em mais de uma combinação de pontos

- **Regras:** V1-4.3.16, V1-4.3.17, V1-4.3.18
- **Trecho:** "It is possible to score for multiple pairs of the same color (quality attributes), as long as each pair consists of cards of different types (tests)." (p. 6)
- **Caso:** sistema com Load e Stress (Desempenho), Recovery (Confiabilidade) e Authentication (Segurança): 4 cartas.
- **Interpretações:**
  - (a) Cada carta entra em no máximo uma combinação, e vale a melhor partição. No caso: 4 + 2 = 6.
  - (b) Cada carta entra em no máximo um par e no máximo um trio. No caso: 4 + 2 + 2 = 8.
  - (c) Toda combinação válida conta, com cartas reaproveitadas. No caso: 4 + 2 + 4 = 10.
- **Sugestão:** (a), a mais conservadora. O autor sabe como a mesa pontuou.
- **Configuração:** `v1.pontuacao.combinacoes: particao | par_e_trio | todas`
- **Impacto:** alto. Em (c) a pontuação cresce mais que o tamanho do sistema, o que amplia a bola de neve.
- **Estado:** decidido pelo autor em 2026-11-09: (a), uma combinação por carta, valendo a melhor partição

### AMB-25 — v1: alvo com sistema vazio

- **Regras:** V1-4.3.5, V1-4.3.6, V1-4.3.11, V1-4.3.12
- **Trecho:** o artigo não trata de sistemas sem cartas.
- **Interpretações:**
  - (a) Pode ser alvo. A falha é encontrada, mas não há carta para tirar; a carta de ataque é gasta.
  - (b) Não pode ser alvo.
- **Sugestão:** (a). O mesmo vale quando falta carta nos outros casos: na contestação com blefe, tira-se o que houver; na contestação com verdade, se o atacante não tem cartas no sistema, o defensor não pega nada.
- **Configuração:** `v1.alvo_com_sistema_vazio: true | false`
- **Impacto:** médio. Pesa na política de atacar o mais fraco.
- **Estado:** decidido pelo autor em 2026-11-09: (a), pode ser alvo e nada é tirado

### AMB-26 — v1: o que identifica um teste

- **Regras:** V1-4.2.1, V1-4.3.16, V1-4.3.17, V1-T3.16, V1-T3.17
- **Trecho:** a pontuação exige "different types (different non-functional tests)" (p. 6), e a Tabela 3 repete os nomes "Stress" e "Scalability" em Usabilidade.
- **Interpretações:**
  - (a) O teste é o par atributo e nome. "Stress" de Usabilidade e "Stress" de Desempenho são testes diferentes, e os nomes trocados não mudam a mecânica.
  - (b) O teste é só o nome. As duas cartas "Stress" não poderiam formar um trio juntas.
- **Sugestão:** (a), coerente com a nota do prompt de que os nomes trocados não afetam a mecânica.
- **Configuração:** não precisa
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-09: (a), atributo e nome

### AMB-27 — v1: número de jogadores e o que é uma partida

- **Regras:** V1-T2.2, V1-4.4.1, V1-4.4.2
- **Trecho:** "3 to 8 players" (p. 4); "groups of approximately six students"; "two consecutive rounds, resulting in a total of six complete playthroughs" (p. 6)
- **Interpretações:**
  - (a) Uma partida é uma rodada, com o baralho reembaralhado a cada rodada. O Experimento 1 usa 6 jogadores, como os grupos do artigo; a comparação com a v2 usa os mesmos tamanhos de mesa nas duas versões.
  - (b) Uma partida são 2 rodadas, com soma de pontos.
- **Sugestão:** (a). O artigo conta 6 partidas para 3 grupos com 2 rodadas cada.
- **Configuração:** `v1.jogadores` no arquivo de cada experimento
- **Impacto:** médio
- **Estado:** decidido pelo autor em 2026-11-09: (a). Com a COR-01, a comparação entre v1 e v2.2 usa mesas de 4 e 5 jogadores.

### AMB-28 — v1: Critical Failure na mão inicial

- **Regras:** V1-4.2.2, V1-4.3.3
- **Trecho:** "this card cannot be used to build a player's system" (p. 5)
- **Interpretações:**
  - (a) Uma Critical Failure recebida fica obrigatoriamente entre as 3 cartas de teste. Como só existem 3 no baralho, sempre é possível montar o sistema. A escolha das outras cartas é decisão do bot.
  - (b) O jogador devolve a carta e compra outra.
- **Sugestão:** (a).
- **Configuração:** não precisa
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-09: (a), fica entre as cartas de teste

### AMB-29 — v1: empate

- **Regras:** V1-4.3.19
- **Trecho:** "The player with the highest total score wins the round." (p. 6). O artigo não tem critério de desempate.
- **Interpretações:**
  - (a) Vitória dividida, como em AMB-14.
  - (b) Sorteio.
- **Sugestão:** (a).
- **Configuração:** `v1.empate: dividido | sorteio`
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-09: (a), vitória dividida

### AMB-30 — Palpite da plateia: o Auditor vota?

- **Regras:** VAR-06 (PDF 2.2, p. 35, "plano B, fora das regras")
- **Trecho:** "Antes de o atacante decidir se contesta, quem está fora da disputa vota com o polegar" (p. 35).
- **Interpretações:**
  - (a) O Auditor faz parte da disputa: votam só os jogadores que não são atacante, defensor nem Auditor.
  - (b) "Fora da disputa" é quem não é atacante nem defensor: o Auditor vota junto.
- **Sugestão:** (a).
- **Configuração:** fixo no motor; só existe com `variantes.palpite_da_plateia` ligado.
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-10: (a), o Auditor não vota

### AMB-31 — Palpite da plateia: de onde vem a ficha

- **Regras:** VAR-06 (PDF 2.2, p. 35)
- **Trecho:** "Se houver contestação, quem acertou ganha 1 ficha" (p. 35).
- **Interpretações:**
  - (a) Do banco, como os outros ganhos do jogo.
  - (b) De quem errou o palpite.
- **Sugestão:** (a).
- **Configuração:** `variantes.premio_do_palpite` (quantas fichas o banco paga)
- **Impacto:** baixo
- **Estado:** decidido pelo autor em 2026-11-10: (a), do banco

### AMB-32 — Custo do teste: e quem não tem ficha?

- **Regras:** VAR-12 (proposta do Experimento 7, autor em 2026-11-11)
- **Trecho:** "a partir do 2º teste do ciclo, cada teste custa 1 ficha", na definição do autor, que não diz o que acontece com quem está com 0 ficha.
- **Interpretações:**
  - (a) Teste pago só é permitido a quem pode pagar: com 0 ficha, só o teste de graça do ciclo é possível.
  - (b) O teste acontece e paga o que puder (nada, com 0 ficha): quem está zerado testa sem limite e sem custo.
- **Sugestão:** (a).
- **Configuração:** fixo no motor; só existe com `propostas.custo_do_teste` maior que 0.
- **Impacto:** baixo. Só pesa para quem chega a 0 ficha no meio da partida (REQ-07: cerca de 5% das partidas).
- **Estado:** decidido pelo autor em 2026-11-11: (a), não pode testar

## Divergências entre as fontes

Não são ambiguidades de regra, mas ficam registradas para que ninguém use o número errado.

| Fonte | Diz | Vale |
|---|---|---|
| PDF 2.2, p. 1 | 4 a 6 jogadores | 4 a 5, pela COR-01, até o PDF ser atualizado |
| PDF 2.2, p. 6 e 8 | O Alerta sai quando o jogador coloca uma carta da categoria | Todos os Alertas saem no início de cada Planejamento, pela COR-02, até o PDF ser atualizado |
| Prompt, seção 6 | v1: blefe aceito resolvido pela verdade | Vale a declaração (AMB-20, decisão de 2026-11-09) |
| Briefing, slide 12 | "54 cartas sempre" como invariante | 63 cartas, ou 72 com o módulo (R-2.0.1, R-11.7); 54 é o baralho da v1 |
| Briefing, slides 6 a 9 | Regras da versão 2.0 (vizinho designado, compra de 2, Hotfix) | Não usar; vale o PDF 2.2 |
| Prompt, seção 2.1 | Exemplo de evento com `"regra": "R-7.2.2"` | Compatível com a numeração adotada: R-7.2.2 é o passo "Responder" |
| PDF 2.2, p. 8 e p. 34 | Defesa "até 30 segundos" e "cada defesa leva até 1 minuto" | Não se contradizem: 30 s é a explicação; 1 min inclui conferência e leitura (MOD-05) |

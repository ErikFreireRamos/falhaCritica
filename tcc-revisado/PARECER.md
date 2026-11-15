# Parecer de revisão do TCC

Revisão de `tcc/main.pdf` (28 páginas, versão de 15/11/2026), feita em 15/11/2026.

- **Original:** `tcc/`, não alterado.
- **Cópia revisada:** esta pasta (`tcc-revisado/`), com `main.pdf` de 32 páginas.

## O que foi e o que não foi conferido

**Conferido.** O PDF foi lido inteiro. Os números e os vereditos foram comparados com
`docs/RESUMO_DOS_RESULTADOS.md`, `docs/DIARIO_DE_BORDO.md`, `configs/requisitos.yaml`, `regras/v2.2.2.md` e os
`relatorio.md` de `resultados/`. As somas das tabelas foram refeitas (971 mil partidas, 13 execuções, 63 cartas e
29 testes, linhas das Tabelas 10 e 12).

**Não conferido.**
- As referências bibliográficas não foram checadas em fontes externas.
- As normas de TCC do curso (formato, capa, uso de IA) não foram consultadas.
- As relações da Tabela 11 dependem da intenção do autor.

## 1. Veredito

**O trabalho é válido como TCC no conteúdo, mas ainda não está pronto para depósito.**

- **Por que é válido:** tem problema definido, método declarado (DSR), artefatos (regras e simulador), avaliação
  e limitações. O rigor da parte de simulação está acima do usual em TCC.
- **O que falta:** tratar os problemas da seção 3 deste parecer, resolver os 5 marcadores `[Pendente]` e
  confirmar o formato com a coordenação.
- **Sobre o formato:** o texto está no modelo de artigo da SBC. O TCC do CI localizado no repositório da UFPB
  (GiroJampa) é monografia; os de formato artigo são do CCAE. Vale confirmar com a orientadora e a coordenação
  que o artigo é aceito no CI.

## 2. Pontos fortes

- **Critério antes da medição.** Cada requisito tem medida e zona de aceite confirmadas antes do experimento, com
  veredito por intervalo de confiança.
- **Reprodutibilidade.** Determinismo por semente, registro de auditoria e manifesto com o commit.
- **O simulador também foi testado.** Testes por regra, propriedades, metamórficos, fuzzing e mutação.
- **Limitações declaradas.** O texto já admite a mudança do REQ-13, a dependência do REQ-04 e o tamanho do
  playtest.
- **Texto claro.** Frases diretas, termos definidos antes de usados, tabelas legíveis.

## 3. Problemas encontrados

Cada item diz onde está, qual é o problema, a evidência e o que foi feito na cópia.

### 3.1 Críticos (afetam as conclusões)

**C1. Vereditos da Tabela 8 fora da regra do próprio texto.**
- A Seção 3.2 define três vereditos: passa, falha, inconclusivo. A Tabela 8 usa "em parte", que não é definido.
- Pelos relatórios: REQ-01 é **inconclusivo** com Heurísticos (`fase4_melhor_estilo`); REQ-06(b) é
  **inconclusivo** com 5 experientes (0,347 para um limite de 0,350, `fase4_exp6_variantes`); REQ-08 **falha**
  com 4 e passa com 5.
- "10 de 13 passam" aparece no resumo e na conclusão sem ressalva, mas três dos dez têm ressalva (REQ-04,
  REQ-06 e REQ-13).
- *Na cópia:* regra de agregação na Seção 3.2; Tabela 8 com os vereditos dos relatórios; resumo, abstract e
  conclusão com as ressalvas.

**C2. "O melhor estilo mistura construir e atacar" é afirmado sem ressalva.**
- No confronto direto, Heurístico e Construtor empatam dentro do intervalo (0,264 e 0,239, referência 0,250).
- Nas mesas mistas do Experimento 2, **o Construtor vence mais**: 0,455 contra 0,370 (4 jogadores) e 0,349
  contra 0,331 (5). O texto não cita esse dado.
- O REQ-04 "passa", mas o replicador termina em 100% de Heurísticos, e o veredito depende só da mesa de
  Aleatórios. Isso estava nas limitações, e não no resumo nem na conclusão.
- *Na cópia:* parágrafo dos estilos reescrito; ressalva do REQ-04 junto do resultado; resumo e conclusão
  ajustados.

**C3. A resposta à QP1 troca de medida sem avisar, e o 0,09 não vale para todas as mesas.**
- A validação da v1 usa "partidas desequilibradas"; a comparação entre versões usa "vantagem do líder". O valor
  da v2 na primeira medida não aparecia. Ele existe no relatório do Experimento 2: 0,93 e 0,94 (fator 1,5) e
  0,55 e 0,53 (fator 2), contra 0,99 e 1,00, e 0,92 e 0,94 na v1.
- Há motivo registrado para a troca (as escalas de placar são diferentes; decisão de 10/11 em
  `configs/requisitos.yaml`), mas o texto não o dizia.
- O 0,09 é de mesas mistas. Em mesas de Heurísticos, a Tabela 9 mostra 0,15 a 0,19, sem explicação.
- *Na cópia:* dois parágrafos novos na Seção 5.1 e a ressalva "em mesas mistas" no resumo e na conclusão.

**C4. As perguntas de pesquisa não cobrem o corpo do trabalho.**
- A QP1 fala só do desequilíbrio da v1. Os 13 requisitos, os estilos, as variantes, a ablação e a profundidade
  ficam sem pergunta.
- A QP3 já traz a resposta na redação ("para tornar o jogo mais imersivo e educativo") e junta duas perguntas.
- *Na cópia:* QP1 e QP3 reescritas, com uma nota explicando a mudança. **Decisão do autor.**

**C5. "Os sete marcaram que se divertiram" contra 6/7 na Tabela 10.**
- São duas perguntas: na múltipla escolha, 7 marcaram "Me diverti jogando"; na afirmação Likert, 6 concordaram.
- *Na cópia:* o texto diz de qual pergunta vem cada número (Seções 5.3 e 6).

### 3.2 Importantes

**I1. Escore de mutação.** "De 4.883 mutantes, 4.508 foram mortos, um escore de 0,930": 4.508 / 4.883 dá 0,923.
O 0,930 é 4.508 / (4.508 + 342). *Na cópia:* a conta completa, com os 342 sobreviventes, 13 por tempo e 20 sem
teste.

**I2. Validação da v1.** Pelo critério principal, a v1 simulada não reproduz a taxa do artigo (mais de 95%
contra 4 de 6, intervalo de 0,30 a 0,90). O texto não dizia isso com clareza. "Mostra por que" é uma afirmação
causal forte. *Na cópia:* frase explícita; "sugere por que".

**I3. Origem das zonas de aceite.** O texto não dizia de onde vêm as faixas. *Na cópia:* parágrafo novo na
Seção 3.2, a partir do campo `fonte` de `configs/requisitos.yaml`, com nota para o autor conferir.

**I4. Matriz de ganhos e replicador.** A matriz só tem mesas homogêneas, e o replicador usa uma aproximação
linear, a partir da população uniforme. *Na cópia:* dito no método e nas ameaças; trabalho futuro novo.

**I5. Ciclo de DSR.** A Figura 1 mostra regras verificadas indo para pessoas. Na prática, o playtest veio antes
do simulador, com a versão 2.2, e houve uma única iteração. *Na cópia:* parágrafo novo na Seção 3.

**I6. Profundidade e tempo parado.** O texto dizia que os limites intermediários "não resolvem o tempo parado",
mas a Tabela 9 não tinha essa coluna. Além disso, manter os testes sem limite mantém o REQ-10 falhando, e isso é
uma escolha. *Na cópia:* coluna de tempo parado na Tabela 9 e a escolha dita de forma explícita.

**I7. Tabela 1.** "Balanceamento verificado: Não" para jogos cooperativos e individuais, em que equilíbrio entre
jogadores não se aplica. *Na cópia:* "Não se aplica" e texto ajustado.

**I8. Os quatro problemas da v1 não eram retomados.** *Na cópia:* subseção 5.5 nova, com a Tabela 13. A coluna
"Situação" é leitura do revisor.

**I9. Ameaças à validade.** O texto cita Wohlin, mas não usava os quatro tipos. Faltavam: perfis de conhecimento
não calibrados, pontos de corte diferentes entre v1 e v2, autor em vários papéis, autosseleção, comparações
múltiplas e fidelidade do simulador às regras. *Na cópia:* seção reorganizada, com as ameaças novas em azul.

**I10. Generalizações do playtest.** "O blefe pareceu impune para os jogadores" vem de 2 respostas abertas.
Faltava o viés de autosseleção e o enquadramento ético. *Na cópia:* frase ajustada, viés declarado e nota sobre
a Resolução CNS 510/2016, a confirmar com a orientadora.

**I11. O blefe não aparece na Tabela 11.** A Seção 4.1 diz que o blefe é o centro do jogo, mas a tabela da QP3
não o relaciona a nenhum conceito. *Na cópia:* só uma nota. **Decisão do autor.**

### 3.3 Menores

| # | Onde | Problema | Na cópia |
|---|---|---|---|
| M1 | Tabela 2, Seção 4.4 | "a validar no playtest": o playtest já ocorreu | "num próximo playtest" |
| M2 | Seção 4.3 | Dado de 8 faces com 7 categorias; desempate e vitória dividida não explicados | Explicados |
| M3 | Seção 4.2 | "Cada categoria é um tipo de teste" | "reúne tipos de teste" |
| M4 | Seção 5.2, Tabela 6 | "Cada mudança da 2.2"; resultado da COR-02 ausente | Corrigido e completado |
| M5 | Vários | Registro coloquial: "virou", "dispara", "pega", "dão certo", "conversam", "estragadas" | Trocados |
| M6 | Tabela 6 | Numeração fora de ordem, sem explicação | Explicada na legenda |
| M7 | Seção 4.4 | Requisitos e experimentos como parágrafos da seção do simulador | Subseção 4.5 |
| M8 | Seção 1 | "quase uma hora" contra 40 a 50 min das regras | Ajustado |
| M9 | Seção 5.1 | REQ-03 discrimina pouco: o Construtor vence 0,973 dos Aleatórios | Dito no texto |
| M10 | Seção 4.4 | Perfis de conhecimento sem dizer que são suposições | Dito no texto |

### 3.4 Não alterados na cópia (ficam para o autor)

- **Figuras do jogo.** Não há imagem de carta, da mesa nem do Radar. Para um TCC sobre um jogo de cartas, uma
  figura com uma Carta de Teste, um incidente (frente e verso) e a mesa montada ajuda muito a banca.
- **Apêndices.** O questionário completo e o texto das regras não estão anexados.
- **Citações a conferir.** Ahamed (2010) é um texto do arXiv para uma afirmação básica; um livro-texto serve
  melhor. Vanhanen et al. (2018) trata de projetos de fim de curso; conferir se sustenta a frase sobre aulas
  expositivas.
- **"and" nas citações** ("Gomes and Lelli"), já listado nas pendências do `tcc/README.md`.
- **"GPT 6".** Confirmar o nome exato da ferramenta e nomear o assistente de IA usado.

## 4. Pendências formais (já marcadas em vermelho no PDF)

1. Capa, ficha catalográfica e folha de aprovação do modelo do CI; mês e ano da defesa.
2. Número de participantes do playtest, turma e datas das sessões.
3. Conferência da Tabela 11.
4. Link público do repositório.
5. Revisão do título e agradecimentos, se o modelo pedir.

## 5. Como ler a cópia revisada

- **Azul:** texto novo ou alterado. Aceitar ou rejeitar trecho a trecho.
- **Verde, entre colchetes `[Revisão: ...]`:** nota do revisor, que não faz parte do texto.
- **Vermelho:** as pendências que já existiam.
- Para ver o texto final, sem cores nem notas, troque `\revisaocoloridatrue` por `\revisaocoloridafalse` em
  `main.tex` e compile de novo.
- Todo número novo tem um comentário `% fonte:` no `.tex`, com o relatório de origem.

| Arquivo | O que mudou |
|---|---|
| `main.tex` | Macros de marcação; resumo e abstract com as ressalvas |
| `secoes/01-introducao.tex` | QP1 e QP3; duração da partida; ressalva do REQ-13 nas contribuições |
| `secoes/02-trabalhos-relacionados.tex` | Tabela 1 e a frase da lacuna |
| `secoes/03-metodologia.tex` | Ordem real do ciclo; origem das zonas; veredito agregado; matriz e replicador; autosseleção; nota de ética |
| `secoes/04-implementacao.tex` | Dado e desempate; perfis de conhecimento; escore de mutação; subseção 4.5; Tabela 6 |
| `secoes/05-resultados.tex` | Seção 5.1 (validação, líder, medida da v2, estilos); Tabelas 8 e 9; playtest; subseção 5.5; ameaças |
| `secoes/06-conclusoes.tex` | Respostas à QP1 e à QP2 com as ressalvas; trabalho futuro novo |
| `secoes/07-artefatos.tex` | Nota sobre a declaração de uso de IA |

## 6. Decisões que ficam com o autor

1. Aceitar ou não a nova redação da QP1 e da QP3.
2. Como apresentar o REQ-04: "passa, com ressalva" ou separar estilos e perfis de blefe.
3. Manter "10 de 13" com as ressalvas ou contar de outra forma.
4. Conferir e completar a justificativa das zonas de aceite.
5. Dizer o que o blefe representa na Tabela 11, ou que é só mecânica de jogo.
6. Conferir a coluna "Situação" da Tabela 13.
7. Enquadramento ético do questionário.

## 7. Lista de conferência antes da defesa

- [ ] Formato (artigo ou monografia) confirmado com a coordenação.
- [ ] Os 5 marcadores `[Pendente]` resolvidos.
- [ ] Decisões da seção 6 tomadas e registradas no diário.
- [ ] Figuras do jogo e apêndices incluídos.
- [ ] Referências conferidas uma a uma.
- [ ] Resumo, Tabela 8 e conclusão dizendo o mesmo sobre os requisitos.
- [ ] Texto compilado sem cores e relido do início ao fim.

## Correção em relação ao plano desta revisão

O plano dizia que o fator 2 da validação da v1 era uma análise feita depois do resultado. **Não é:** a análise
de sensibilidade com os fatores de 1,25 a 2 foi fixada junto com o critério, antes do Experimento 1
(`configs/requisitos.yaml`, MET-01). O problema real é só o do item I2.

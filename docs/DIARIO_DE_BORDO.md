# Diário de bordo

Registro do processo de desenvolvimento do simulador do Critical Failure. Uma entrada por fase ou sessão de trabalho, com o que foi feito, as decisões do autor e as opções que ele tinha, os detalhes que o assistente escolheu sem perguntar, as pendências e o commit.

As decisões sobre regras ambíguas têm o texto completo em `docs/AMBIGUIDADES.md`. As mudanças de regra estão em `docs/HISTORICO_REGRAS.md`.

---

## 2026-11-09 — Fase 0: especificação

### O que foi feito

1. **Leitura das fontes:** PDF das regras 2.2 (35 páginas), artigo do SBQS 2025 (seções 4.1 a 4.4, Tabelas 2 a 4), briefing (slides 5 e 10 a 13) e `docs/prompt_claude_code_simulador.md`.
2. **Plano:** avaliado o plano inicial do autor, propostas 11 mudanças e aprovado depois de duas revisões pedidas por ele.
3. **Repositório:** `git init` no ramo `main`, identidade do autor configurada só neste repositório, `.gitignore` e `.gitattributes` (fim de linha LF).
4. **Documentos criados:**
   - `docs/especificacao_v2_2.md`: 181 itens numerados (128 regras, 7 definições, 12 componentes, 11 de mesa, 22 notas e 1 regra revogada), catálogo das 33 cartas de Teste e dos 16 incidentes, 9 variantes de playtest, 7 hipóteses de modelo e 2 correções do autor.
   - `docs/especificacao_v1.md`: 38 itens (25 regras) e o baralho da Tabela 3.
   - `docs/AMBIGUIDADES.md`: 27 pontos, todos decididos pelo autor nesta sessão.
   - `configs/requisitos.yaml`: 14 requisitos e 6 métricas, com definição e zona sugeridas, aguardando confirmação.
   - `docs/HISTORICO_REGRAS.md`, este diário e `CLAUDE.md`.
   - `scripts/verificar_especificacao.py`.
5. **Rodada de decisões:** 27 ambiguidades apresentadas ao autor em blocos de perguntas. Duas respostas mudaram regra (COR-01 e COR-02).

### Mudanças aprovadas em relação ao prompt inicial

O autor perguntou se algo no plano dele merecia alteração. Estas 11 mudanças foram propostas e aprovadas junto com o plano:

| # | Mudança | Motivo |
|---|---|---|
| 1 | Executor mínimo de experimentos logo depois do motor (Fase 1b) | O primeiro número só apareceria na Fase 4, e os bots não podem ser desenvolvidos sem executor |
| 2 | CI básica na Fase 1, não na 5 | Protege o que vem depois e prova cedo o registro idêntico entre plataformas |
| 3 | Requisitos com zona de aceite fixada antes de rodar | Com 1 milhão de partidas qualquer diferença é significativa; e evita escolher a margem que reproduz o artigo |
| 4 | Separar requisito de regra de requisito de comportamento, com análise de equilíbrio para o blefe | Com probabilidades fixas, a taxa de blefe mede os parâmetros dos bots, não o jogo |
| 5 | Validação da v1 como plausibilidade, com evidência no mecanismo | 4 de 6 partidas dá um intervalo de 95% de 30% a 90% |
| 6 | Código por família de regras (`regras/v2/`), YAML por versão | O jogo vai continuar mudando; cada iteração vira um YAML, sem copiar código |
| 7 | Variantes do playtest uma por vez | 60 configurações em vez de 1.728 |
| 8 | Modelo de conhecimento com poucos parâmetros | Matrizes de confusão inventadas não se defendem; as completas entram com dados reais |
| 9 | Três salvaguardas: árvore do git suja registrada e bloqueada em experimento oficial; sem ponto flutuante no motor; teste que procura números literais nas regras | Rastreabilidade e determinismo entre plataformas |
| 10 | Assento humano no terminal, na Fase 2 | Jogar contra os bots é a forma mais barata de conferir o motor |
| 11 | Parada nova depois da Fase 3 | É quando saem os primeiros resultados da QP1 |

Sugestão não incluída, a decidir depois da Fase 4: busca evolutiva de exploits nos parâmetros do bot Heurístico.

Limites que o texto do TCC precisa declarar: bots não são alunos; os perfis iniciante e experiente mostram se a mecânica degrada com pouco conhecimento, e não testam a hipótese de revisão contra primeira aprendizagem; a validação da v1 se apoia em 6 partidas.

### Decisões do autor

**Sobre o processo**

| Assunto | Opções | Escolha |
|---|---|---|
| O que "auditar tudo" cobre | diário e histórico de regras; só o registro das partidas; diário e ADRs formais | Diário e histórico de regras |
| Identidade dos commits | pessoal, só neste repositório; manter a global da máquina | Pessoal, só neste repositório |
| Autonomia do assistente | — | Primeiro: "fique livre para tomar decisões e opiniões MAS SEMPRE INFORME A MIM". Depois, ao ver o plano: "sobre as regras e decisões tomadas sozinho, não faça isso, mas pergunte a mim o que fazer". Vale a segunda |
| Quando confirmar as zonas de aceite | antes de cada medição; todas agora; revisar o arquivo | Antes de cada medição |
| Princípio para pontuação | — | "Sobre a pontuação no geral busque manter simplicidade" |

**Sobre as regras da v2.2**

| Ponto | Escolha | Observação |
|---|---|---|
| AMB-01 | Diagnóstico antes do dano | |
| AMB-02 | Sem carta no Backlog, a Lição aprendida não acontece | Pegar é opcional |
| AMB-03 | Quem não pode testar passa automaticamente | |
| AMB-04 | Quem já passou continua podendo ser testado | |
| AMB-06 | Máximo de 5 jogadores; no caso raro que resta, pular a compra | Resposta livre: "limite o jogo ate 5 jogadores". Depois escolheu "Corrigir a própria v2.2" em vez de abrir uma v2.3. Virou a COR-01 |
| AMB-07 | Carta repetida vai para o fundo do baralho | Não marcada no primeiro bloco; perguntada de novo |
| AMB-08 | O assento 0 sempre começa | |
| AMB-09 | Compra as 3 cartas e depois coloca | |
| AMB-10 | Lista proposta de informação pública | |
| AMB-11 | Revelação mínima para comprovar cobertura | |
| AMB-12 | Regra nova: todos os Alertas saem no início de cada Planejamento | Resposta livre: "alertas sao zerados na rodada seguinte(proximo planejamento". Confirmou depois de ver as consequências: R-6.2b sai; os Alertas do ciclo 3 ficam até o fim e podem custar 2. Virou a COR-02 |
| AMB-13 | Saldo único na pontuação final | Pelo princípio de simplicidade |
| AMB-14 | Vitória dividida no empate | |
| AMB-15 | É blefe sempre que o teste nomeado não está no sistema | |
| AMB-16 | Bots não erram a categoria na Fase 1 | Reavaliar na Fase 2 |
| AMB-17 | Fichas e cubos ilimitados, com medição do pico | |

**Sobre as regras da v1**

| Ponto | Escolha | Observação |
|---|---|---|
| AMB-20 | Blefe aceito: vale a declaração | Mudou a decisão do prompt, que era resolver pela verdade, depois de ver que pela verdade blefar nunca compensa |
| AMB-23 | Carta de ataque vai para o descarte quando a falha é encontrada | |
| AMB-24 | Uma combinação de pontos por carta | |
| AMB-25 | Sistema vazio pode ser alvo; nada é tirado | |
| AMB-26 | Teste identificado por atributo e nome | |
| AMB-27 | Partida é uma rodada; Experimento 1 com 6 jogadores | A comparação com a v2.2 usa mesas de 4 e 5 |
| AMB-28 | Critical Failure fica entre as cartas de teste | |
| AMB-29 | Vitória dividida no empate | |

AMB-05, AMB-21 e AMB-22 já estavam decididas no prompt (seção 6).

**Sobre como registrar as correções:** as duas mudanças entram como correções da própria v2.2, valem sobre o PDF até o autor atualizá-lo, e o comportamento impresso continua disponível por configuração para o simulador medir o efeito de cada uma.

### Detalhes escolhidos pelo assistente, sem perguntar

Não mudam regra nem resultado. Ficam aqui para o autor poder discordar.

- **Identificadores:** letra no fim para dividir um passo do PDF em itens atômicos (`R-7.2.2a`); `R-<seção>.0.<n>` para o texto próprio das seções 2, 7, 8 e 9; prefixos novos `VAR` (variantes), `MET` (métricas sem critério de aceite), `COR` (correções do autor) e `R-REG` (Folha de registro).
- **Tipos de item:** `regra`, `definicao`, `componente`, `mesa`, `nota`, `revogada` e, na v1, `evidencia`.
- **Nomes dos 62 parâmetros** propostos para o YAML (por exemplo `dano.incidente.sem_cobertura`). São só nomes; os valores vêm do PDF.
- **Requisitos além dos 9 do prompt:** REQ-10 a REQ-14 e MET-03 a MET-06 foram derivados da tabela "Parâmetros a validar no playtest" (p. 34 e 35). Todas as definições e zonas são sugestão e aguardam confirmação.
- **Git:** `core.autocrlf=false` neste repositório, para o `.gitattributes` mandar no fim de linha.
- **Saída do verificador em UTF-8**, para funcionar quando redirecionada no Windows.

### Achados da Fase 0

- **O baralho não fecha com 6 jogadores.** A preparação e os 3 Planejamentos pedem 71 cartas e o baralho tem 63; só os testes devolvem cartas ao descarte. O defeito foi encontrado na leitura das regras, antes de qualquer simulação, e levou à COR-01. Com 5 jogadores o caso ainda pode ocorrer por causa da Lição aprendida, mas raramente; com 4, nunca.
- **A regra de blefe aceito da v1 é circular** no artigo: manda aplicar pela verdade sem revelar a carta. Resolvida pela verdade, blefar nunca compensa, o que contradiz o que se observou na mesa.
- **As contagens do PDF 2.2 fecham:** 63 cartas e 29 testes, 72 e 33 com o módulo, 14 e 16 incidentes, 3 severos no jogo base.

### Verificação

- `py -3.12 scripts/verificar_especificacao.py`: 0 erros e 0 avisos. Confere identificadores, páginas, valores de parâmetro repetidos, somas dos baralhos, incidentes, campos das ambiguidades e dos requisitos, e referências cruzadas.
- **Teste do verificador:** numa cópia com 7 defeitos plantados (número de cópias, teste-chave e severidade de um incidente, valor de parâmetro, página, referência inexistente, campo ausente e baralho da v1), ele acusou todos.
- **Conferência contra os PDFs:** 23 frases de regras amostradas foram procuradas na página citada. 22 foram achadas. A outra ("4 a 6" jogadores, p. 1) aparece como "4a6" na extração de texto da tabela, e foi conferida à mão.

### Pendências

**Do autor**

- Atualizar o PDF das regras com a COR-01 e a COR-02. Os trechos que a COR-02 torna obsoletos estão listados em `docs/HISTORICO_REGRAS.md`.
- Criar o repositório no GitHub e passar a URL, para a CI da Fase 1. Não há `gh` nesta máquina.
- Se existirem, as anotações de placar das 6 partidas da v1 ajudam o Experimento 1.

**A perguntar na Fase 1**

- Parâmetros mínimos de MOD-01, MOD-02 e MOD-03 para o bot Aleatório jogar partidas completas.
- Formato do CSV de `cf folha` (um arquivo com coluna de tipo, ou três arquivos).
- Como o cabeçalho do registro identifica a versão das regras ("v2.2" mais a lista de correções ativas).

**Mais adiante**

- Zonas de REQ-01, REQ-08 e REQ-09 antes da Fase 1b; as demais, antes da primeira medição de cada uma.
- AMB-16 e o detalhamento de VAR-02, VAR-03, VAR-04 e VAR-06 na Fase 2.

### Commit

Commit único da Fase 0 no ramo `main` (ver `git log`).

---

## 2026-11-09 — Regras em Markdown (pasta `regras/`)

### Pedido do autor

Depois de revisar a Fase 0, o autor respondeu: "Não se coloque como co-author, por enquanto faça o pdf das regras como .md, pois pode ser que esteja sujeita a alterações, crie uma pasta regras contendo arquivos com as versões das regras, não tenho anotação de placar, fase 1 liberada".

### O que foi feito

1. **Coautoria:** a linha `Co-Authored-By` foi retirada do commit da Fase 0 com `git commit --amend` (não havia repositório remoto). Os commits seguintes não levam atribuição ao assistente.
2. **`regras/v2.2.md`:** transcrição do PDF 2.2 em Markdown. Só a formatação mudou.
3. **`regras/v2.2.1.md`:** a v2.2 com as correções COR-01 e COR-02 e com 14 esclarecimentos, cada trecho alterado com a sua marca. Gerado por 28 substituições exatas sobre a transcrição.
4. **`regras/v1.md`:** regras da v1 em português, a partir do artigo, com as decisões AMB-20 a AMB-29 marcadas.
5. **`regras/README.md`:** tabela de versões e como criar uma versão nova.

### Decisões do autor

| Assunto | Opções | Escolha |
|---|---|---|
| Nome dos arquivos de versão e rótulo no registro das partidas | v2.2 e v2.2.1; revisões datadas; um arquivo editado no lugar | v2.2 e v2.2.1 |
| Arquivo da v1 na pasta | sim, em português; não | Sim, em português |
| Esclarecimentos AMB no texto das regras | sim, marcados; só as 2 correções | Sim, marcados |
| Anotações de placar das 6 partidas da v1 | — | Não existem |

### Detalhes escolhidos pelo assistente, sem perguntar

- **Redação dos trechos marcados** em `regras/v2.2.1.md` e de todo o `regras/v1.md`. É proposta e aguarda a revisão do autor.
- **Três decisões ficaram fora do texto das regras** por só valerem para o simulador: AMB-08, AMB-16 e AMB-17.
- **Duas linhas novas na tabela de parâmetros a validar** da v2.2.1, uma para cada correção.
- **O exemplo de dano da seção 8.1** foi reescrito: a segunda frase do PDF dependia da regra revogada. O novo texto diz que, com uma carta da categoria no sistema, Ana devolveria só 1 e terminaria com 0.

### Verificação

- **Transcrição contra o PDF:** de 928 trechos de `regras/v2.2.md`, 888 foram achados literalmente no texto extraído do PDF. Os outros 40 são 32 rótulos de formatação ("Frente - relato", "Verso - gabarito"), o símbolo de severidade da seção 8.1 (anotado no arquivo), 1 linha de fontes em que a extração perde um hífen e 6 células de tabela que a extração embaralha. Todos foram conferidos à mão.
- **v2.2.1:** as 28 substituições exigem que o trecho original apareça exatamente uma vez na v2.2; todas passaram. As 14 marcas AMB e as marcas COR-01 e COR-02 estão no texto.
- `py -3.12 scripts/verificar_especificacao.py` passa, agora lendo também a pasta `regras/`.

### Pendências

- **Do autor:** revisar a redação dos trechos marcados em `regras/v2.2.1.md` e o `regras/v1.md`. A atualização do PDF deixa de ser pendência enquanto as regras estiverem em ajuste.
- O repositório no GitHub continua pendente para a CI.

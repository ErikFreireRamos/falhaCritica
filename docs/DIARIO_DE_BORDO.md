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

---

## 2026-11-09 — Fase 1: motor da v2, registro de auditoria e testes

### O que foi feito

1. **Ambiente:** projeto `uv` com `pyproject.toml` e `uv.lock`, Python 3.12, `ruff`, `mypy` no modo estrito, `pytest` e `hypothesis`.
2. **Configuração:** `configs/regras_v2_2_1.yaml` (versão atual) e `configs/regras_v2_2.yaml` (como impressa), com todos os números das regras e a regra de cada um. `configs/catalogo_v2.yaml` é gerado da especificação por `scripts/gerar_catalogo.py`.
3. **Núcleo** (`src/critical_failure/nucleo/`): erros controlados, JSON canônico e hash, aleatoriedade por contador, catálogo de cartas e incidentes.
4. **Motor da família v2** (`regras/v2/`): estado imutável, ações, `preparar`, `acoes_legais`, `aplicar` e invariantes. Implementa a v2.2.1 e, por configuração, a v2.2 impressa e o módulo de Segurança Operacional.
5. **Observação** (`observacao.py`): o que cada assento vê, pela lista de AMB-10.
6. **Bot Aleatório** (`bots/`) e o laço da partida (`partida.py`).
7. **Auditoria** (`auditoria/`): registro JSONL `cf-audit/1`, replay em dois modos, narração e Folha em três CSVs.
8. **Linha de comando** `cf`: `jogar`, `replay`, `narrar` e `folha`.
9. **Testes:** 231, entre testes por regra, de propriedades, de convenções e de registros de referência.
10. **Rastreabilidade:** `scripts/matriz_rastreabilidade.py` gera `docs/MATRIZ_RASTREABILIDADE.md`.
11. **CI:** `.github/workflows/ci.yml`, para Linux e Windows. Passa a rodar quando houver repositório remoto.
12. **Exemplos:** duas partidas narradas em `docs/exemplos/`, geradas dos registros de `tests/dourados/`.

### Decisões do autor

| Assunto | Opções | Escolha |
|---|---|---|
| Valores provisórios do bot Aleatório (MOD-01 e MOD-02) | 50% e Auditor perfeito; 50% e Auditor com 90%; outros | Explicação correta em 50% das defesas; Auditor sempre julga certo |
| Formato da Folha de registro | três arquivos CSV; um CSV só | Três arquivos CSV |

### Detalhes escolhidos pelo assistente, sem perguntar

- **Dependências de desenvolvimento fora da lista do prompt:** `hatchling` (empacotamento) e `types-pyyaml` (tipos para o `mypy`). `pandas`, `pyarrow` e `mutmut` ainda não foram instalados; entram nas fases que os usam.
- **Limite de 120 colunas** no `ruff`.
- **Cartas citadas pelo nome do teste nas ações** (`testar:Carga:2`). Cópias do mesmo teste são equivalentes; o motor escolhe a carta física.
- **Distribuição na preparação:** as 2 cartas de cada jogador saem seguidas do topo, a partir do assento 0.
- **Reposição do Backlog** na mesma vaga da carta que saiu.
- **Carta revelada** (contestação ou Produção): entre as que servem, o motor prefere uma que a mesa já conhece.
- **Interpretações que dá para trocar no YAML:** ordem entre diagnóstico e dano (AMB-01), quem passou pode ser alvo (AMB-04), Critical Failure limpa Alertas (AMB-12) e ordem da pontuação final (AMB-13), além das duas correções. As outras só aceitam o valor decidido.
- **`estado_hash` do último evento de cada passo** é o do estado em repouso, já com a vez passada ao próximo jogador.
- **Defesa com teste de outra categoria** (R-7.2.2c): o motor aceita e aplica "Falhou", mas não oferece a opção aos bots (AMB-16).
- **Narração:** nomes Ana, Bruno, Carla, Davi, Elisa e Fábio por assento; o que estava oculto aparece entre colchetes, com opção para esconder.
- **Pastas novas:** `tests/dourados/` e `docs/exemplos/`.
- **Duração estimada** fica nula no registro até a Fase 1b, quando entra o modelo de tempos (MOD-05).
- **Fuzzing básico** do motor já nesta fase, como teste de propriedade. O fuzzing completo continua na Fase 5.
- **`cf jogar`** só usa bots aleatórios por enquanto; a escolha de bots entra na Fase 2.

### Defeitos achados e corrigidos durante a fase

- **Decisão que não ia para o registro:** encerrar o turno de Planejamento não gerava evento, então a ação do bot não teria onde ser gravada. Criado o evento `fim_do_turno` (R-6.4), e o motor passou a recusar qualquer ação que não gere evento.
- **Hash do estado errado no fim de cada passo:** depois do último evento o motor ainda passava a vez, e o hash gravado não era o do estado final. Corrigido.
- **Citação de regra inexistente:** um comentário do código citava as regras da seção 2 com um identificador genérico, que não existe na especificação. O teste de convenções acusou. O mesmo erro apareceu depois numa frase deste diário, e o verificador da especificação também acusou.
- **Dois erros de expectativa em testes** (não do motor): um teste pedia 4 cópias de Carga, e o baralho tem 3; outro esquecia que a compra no Backlog repõe a vaga com a carta do topo.

### Verificação

- `uv run pytest`: 231 testes passam e 1 é pulado (o caso de 6 jogadores não tem narração de exemplo).
- `uv run ruff check .` e `uv run mypy` (modo estrito, 24 arquivos): sem apontamentos.
- **Matriz de rastreabilidade:** 148 de 148 itens que exigem teste têm pelo menos um.
- **Registros de referência:** 3 partidas (4, 5 e 6 jogadores) refeitas byte a byte e pelo replay nos dois modos. A comparação entre Windows e Linux só acontece quando a CI rodar.
- **Replay contra adulteração:** 8 tipos de alteração no registro, nos dois modos; todos acusados.
- **Não vazamento:** teste de não interferência com 120 partidas aleatórias. Trocar o que está oculto para um assento não muda a observação dele.
- **Defeitos plantados:** 17 alterações no motor, uma de cada vez; os testes por regra, sem os registros de referência, acusaram as 17. É uma amostra feita à mão, não o teste de mutação da Fase 5.
- **Fumaça:** 200 partidas na v2.2.1 e 300 na v2.2 impressa, com os invariantes conferidos a cada evento.

### Observações (não são medição de requisito)

- **Velocidade no modo rápido, num núcleo:** 74 partidas por segundo com 4 jogadores e 54 com 5. Um milhão de partidas levaria de 4 a 5 horas num núcleo. Perfilar e paralelizar é trabalho da Fase 1b.
- **Baralho com 6 jogadores:** na v2.2 impressa, as 200 partidas de bots aleatórios com 6 jogadores precisaram embaralhar o descarte. Com 4 e 5, nenhuma. Em nenhuma faltou carta, porque bots aleatórios testam muito (32 testes por partida com 6). É coerente com a conta que levou à COR-01, mas bots aleatórios não são jogadores.

### Pendências

- **Do autor:** rever as duas narrações de `docs/exemplos/` e dizer se o motor joga como as regras dizem; criar o repositório no GitHub para a CI rodar.
- **Antes da Fase 1b:** confirmar as zonas de REQ-01, REQ-08 e REQ-09 e os tempos por ação do modelo de duração (MOD-05).

---

## 2026-11-10 — Revisão da Fase 1 e sincronização com o GitHub

### Respostas do autor à revisão da Fase 1

| Assunto | Resposta |
|---|---|
| As duas narrações de `docs/exemplos/` | "O jogo está jogando corretamente" |
| Os 13 detalhes escolhidos pelo assistente na Fase 1 | Aceitos |
| Repositório remoto | Criado: https://github.com/ErikFreireRamos/falhaCritica |
| Redação dos trechos marcados em `regras/v2.2.1.md` e do `regras/v1.md` | Sem resposta ainda; continua pendente |

O autor também lembrou o objetivo das simulações: ter bots com estilos de jogo diferentes, avaliar qual é o melhor estilo e se o jogo está balanceado. Ficou registrado como a métrica MET-07 em `configs/requisitos.yaml` (sugestão do assistente, aguardando confirmação). As duas perguntas se respondem juntas: se um estilo vence todos os outros, ele é o melhor e o jogo não está balanceado.

### Erro do assistente: histórico reescrito depois de publicado

O autor não conseguia sincronizar pelo VS Code, que pedia rebase.

- **Causa:** em 9 de novembro, para tirar a linha de coautoria, o assistente reescreveu o commit da Fase 0 com `git commit --amend` e registrou neste diário que "não havia repositório remoto". Não tinha conferido. O commit original (`69764b1`) já estava no GitHub. O histórico local (`b78a07a` e os dois commits seguintes) e o remoto divergiram.
- **O que estava em jogo:** os dois commits da Fase 0 tinham o mesmo conteúdo; só a mensagem diferia. Nenhum arquivo foi perdido.
- **Decisão do autor:** entre sobrescrever o GitHub, manter o commit antigo ou não mexer, escolheu sobrescrever.
- **Correção:** `git push --force-with-lease=main:69764b1 origin main`. O GitHub ficou igual ao histórico local, sem linha de coautoria em nenhum commit.
- **Para não repetir:** antes de qualquer reescrita de histórico, conferir `git remote -v` e `git status -sb`. Commit já enviado só se corrige com commit novo, a menos que o autor autorize sobrescrever.

### Integração contínua

Com o envio, o workflow `.github/workflows/ci.yml` rodou pela primeira vez, no commit `560522d`.

| Plataforma | Resultado |
|---|---|
| `ubuntu-latest` | sucesso, 11 passos de 11 |
| `windows-latest` | sucesso, 11 passos de 11 |

Isso fecha a pendência da Fase 1: os registros de referência, gerados no Windows, foram refeitos byte a byte no Linux. O determinismo entre plataformas deixou de ser promessa e passou a ser conferido a cada envio.

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

---

## 2026-11-10 — Fase 1b: executor de experimentos e primeiros requisitos medidos

### Decisões do autor

| Assunto | Opções | Escolha |
|---|---|---|
| Envio ao GitHub | enviar a cada fase; o autor sincroniza | "Faça sempre, mas não se coloque como co-author": envio normal (sem forçar) a cada commit, sem linha de coautoria |
| Zona de REQ-01 (equidade de assento) | 1, 2 ou 3 pontos percentuais | 2 pontos: cada posição entre 1/N − 0,02 e 1/N + 0,02 |
| Tempos do modelo de duração (MOD-05) | sugestão do assistente; o autor informa | Sugestão: teste admitido 20 s, teste com defesa 60 s, contestação +15 s, passar 5 s, Produção 3 min, fim de jogo 3 min; preparação 3 min e turno de 30 s vêm do PDF |
| Robustez (REQ-09) | 100 mil agora e 1 milhão depois; 1 milhão agora; otimizar antes | Resposta livre: "REQ-09 está muito criterioso, reduza o número de partidas para 50.000. Esse número já basta" |

O REQ-08 foi confirmado com a zona do próprio PDF (mediana entre 40 e 50 minutos). A outra parte que eu tinha sugerido, no máximo 5% das partidas acima de 60 minutos, não chegou a ser perguntada: ficou só como descrição (percentil 90), sem veredito, até o autor decidir.

### O que foi feito

1. **Modelo de duração** (`duracao.py`, `configs/duracao.yaml`): cada partida soma os tempos das suas ações. A duração estimada vai para o fim do registro de auditoria, em segundos, e o modelo usado vai para o cabeçalho.
2. **Executor** (`experimentos/`): `cf experimento` lê um YAML com cenários, roda em paralelo e grava `partidas.parquet`, os registros completos de uma amostra e de toda partida que falhar, `manifest.json` e `relatorio.md`. `cf relatorio` refaz o relatório a partir do manifest e da tabela.
3. **Métricas** (`metricas/`): intervalo de Wilson, bootstrap e o veredito passa, falha ou inconclusivo. Só recebem veredito os requisitos com `estado: confirmado` e um `criterio` estruturado em `configs/requisitos.yaml`.
4. **Fábrica de bots** (`bots/fabrica.py`): cria um bot pelo tipo e pelos parâmetros gravados num registro ou num experimento.
5. **Testes novos:** 53, sobre duração, estatística e executor. Entre eles: o resultado não depende do número de processos; partida que falha vira linha de erro e ganha registro; o relatório refeito do manifest é igual ao original.
6. **Registros de referência** gerados de novo, porque o formato mudou (cabeçalho com o modelo de duração; fim com a duração em segundos). Só a primeira e a última linha de cada um mudaram: os eventos são os mesmos, então o motor joga igual.

### Detalhes escolhidos pelo assistente, sem perguntar

- **`pyarrow`** como dependência, para o Parquet. Estava na lista do prompt.
- **REQ-01 usa bootstrap, não Wilson.** A vitória dividida (AMB-14) gera frações, e o intervalo de Wilson só vale para resultados 0 ou 1.
- **Invariantes conferidos a cada evento** em todas as partidas do experimento, para a robustez valer de verdade. Custa o dobro do tempo; dá para desligar no YAML.
- **`relatorio.md` também vai para o git**, além do `manifest.json`, para os resultados aparecerem no GitHub.
- **Ordem de trabalho para experimento oficial:** commit do código, `cf experimento --oficial` e depois commit do manifest, do relatório e do diário. Ficou registrada no `CLAUDE.md`.
- **Organização da execução:** pasta `resultados/<experimento>/<data>-<commit>/`; lotes de 250 partidas; processos padrão igual ao número de núcleos menos 1; 1.000 reamostras no bootstrap; registro completo de 1 partida a cada 1.000.
- **Cenários extras só para a robustez:** v2.2.1 com o módulo de Segurança Operacional e v2.2 impressa com 6 jogadores.

### Resultado do experimento `fase1b_linha_de_base`

Execução oficial no commit `4d14805`, árvore limpa: 90.000 partidas em 685 s com 7 processos, nenhuma falha. Relatório em `resultados/fase1b_linha_de_base/20261110-140810-4d14805/relatorio.md`.

| Requisito | Resultado |
|---|---|
| REQ-01, equidade de assento | **passa** com 4 e com 5 jogadores. Todas as posições entre 0,248 e 0,253 (4 jogadores) e entre 0,198 e 0,203 (5 jogadores), com intervalos de cerca de ±0,004 |
| REQ-08, duração | **passa** com 4 e com 5 jogadores. Medianas de 41,6 e 49,2 minutos |
| REQ-09, robustez | **passa**: 0 falhas em 90.000 partidas, acima das 50.000 pedidas |

### Observações (cuidado ao ler)

- **Os bots são aleatórios.** A equidade de assento com bots aleatórios mostra que a ordem de jogo, sozinha, não dá vantagem. Não diz nada sobre jogadores com estratégia; isso é a Fase 2.
- **A mediana com 5 jogadores, 49,2 min, está perto do teto de 50**, e 10% das partidas passam de 52,9 min. Os tempos são provisórios e bots aleatórios testam muito (27,6 testes por partida com 5 jogadores). Vale cronometrar no playtest antes de concluir algo.
- **Com 6 jogadores, na regra impressa**, a mediana foi de 55,3 min e todas as partidas precisaram embaralhar o descarte. Nenhuma ficou sem carta, porque bots aleatórios testam muito. É mais um dado a favor da COR-01.

### Pendências

- Do autor: rever a redação dos trechos marcados em `regras/v2.2.1.md` e o `regras/v1.md`.
- Decidir se o REQ-08 terá a parte "no máximo 5% das partidas acima de 60 minutos".

---

## 2026-11-10 — Fase 2: bots com estilo de jogo

### Decisões do autor

| Assunto | Opções | Escolha |
|---|---|---|
| Construtor | enche e testa com sobras; enche e nunca testa | Enche e testa com sobras: compra e coloca na ordem categoria lida no Agora, no Próximo, categorias novas; testa só com o que não serve ao sistema |
| Caçador | sistema mínimo; sistema vazio | Sistema mínimo: coloca só 1 carta da categoria lida no incidente Agora, se não tiver; testa com o resto, começando por essa categoria; alvo pela política (líder, mais fraco ou ao acaso) |
| Heurístico | valor esperado e softmax; regras fixas | Valor esperado e softmax com temperatura de 0,5 ficha, pesos inteiros |
| Leitura do Radar (MOD-04) | uma vez por incidente; a cada uso | Uma vez por incidente: a mesma leitura vale para o planejamento, o ataque e o diagnóstico |
| Perfis de blefe | 3 × 3 = 9; 3 perfis | 9: blefar nunca, metade das vezes ou sempre; contestar nunca, sempre ou pelo limiar de R-7.3.5 |
| Teste nomeado no blefe | o mais provável; ao acaso | O teste da categoria com mais cópias ainda não vistas |
| Perfis de conhecimento | sugestão; outros valores | Sugestão. Iniciante: explicação 50%, diagnóstico 40%, Auditor 75%. Experiente: 85%, 80%, 95%. Ao errar o diagnóstico, metade cai na secundária, se houver |
| Variantes do playtest | Fase 4; Fase 2 | Fase 4 |
| Assento humano | manter na Fase 2; adiar | Resposta livre: "não coloque humanos, pois queremos simular um número maior de partidas". Saiu do escopo |
| Fumaça da Fase 2 | mesas mistas com 20 mil partidas; só narrações; os dois | Mesas mistas, 20 mil partidas |

### O que foi feito

1. **Perfis** em `configs/perfis.yaml`. Num experimento, um bot pode citar o perfil pelo nome; o registro de auditoria grava sempre os valores resolvidos.
2. **Mesa pública e Leitor** (`bots/mesa.py`). O bot recebe, ao iniciar a partida, as regras e a composição do baralho (MOD-08). O gabarito dos incidentes fica dentro do Leitor, que só devolve a leitura sorteada (MOD-03, MOD-04). Um teste confere que o código dos bots não consulta o gabarito por outro caminho.
3. **Estimativas por contagem** (`bots/estimativas.py`, MOD-09): cartas não vistas, chance de um adversário não ter um teste ou uma categoria, teste mais provável de uma categoria.
4. **Os três estilos** (`bots/estrategicos.py`), sobre uma base comum que cuida do blefe, da contestação, do papel de Auditor, do diagnóstico e da Lição aprendida. Cada decisão grava o motivo; a do Heurístico grava os valores que pesou.
5. **Executor:** rodízio de assentos (cada mesa mista roda em todas as rotações, com as mesmas sementes) e taxa de vitória por bot no relatório (MET-07, sem veredito).
6. **Testes novos:** 43. Conferem cada estilo decisão por decisão em partidas inteiras, os perfis de blefe e de contestação, a leitura, as estimativas, o softmax e mesas aleatórias de bots com os invariantes ligados.
7. **Registro de referência com os quatro estilos** (`tests/dourados/v2_2_1_estilos_mistos.jsonl`) e a narração `docs/exemplos/narracao_v2_2_1_estilos_mistos.txt`. Os três registros antigos não mudaram.
8. **Especificação:** MOD-04 e MOD-07 detalhados; MOD-08 e MOD-09 novos.

### Detalhes escolhidos pelo assistente, sem perguntar

**Comuns a todos os estilos**
- Com carta da categoria atacada, o bot nomeia um teste que tem (de preferência um já revelado) e defende com a verdade.
- Na Lição aprendida, sempre pega a carta, preferindo um teste que ainda não tem.
- A leitura de cada incidente usa um contador próprio no fluxo do bot. Com isso, bots de estilos diferentes no mesmo assento leem o mesmo relato do mesmo jeito (números aleatórios comuns).
- Se o bot viu um adversário pegar do Backlog uma carta do teste em questão, supõe que ela está no sistema dele (MOD-09).
- No Leitor, quando o teste-chave não tem vizinho fora da categoria secundária (é o caso do incidente 13), o resto do erro vai por igual para as demais categorias.

**Construtor:** sem carta útil no Backlog, compra do topo. Entre as sobras, testa com carta e alvo ao acaso.

**Caçador:** compra no Backlog cartas da categoria lida no Agora, para cobrir e como munição; sem elas, compra do topo. Empates na política de alvo são sorteados.

**Heurístico.** Dentro da abordagem aprovada, o modelo de valor é meu:
- uma carta no sistema vale o dano evitado nos incidentes à frente (Agora com peso 1, Próximo com o desconto), o Critical Failure (categoria sorteada, peso igual ao desconto ao quadrado) e a pontuação final;
- a chance de uma categoria ser a chave é a do perfil para a categoria lida, e o resto é dividido igualmente entre as outras;
- a chance de o teste novo ser teste-chave é 1 dividido pelo número de testes da categoria;
- testar vale a chance estimada de o alvo não ter a categoria vezes o ganho do atacante, mais 1/(N − 1) do dano que o Alerta causa a ele;
- guardar uma carta para o próximo Planejamento vale o seu valor no sistema vezes o desconto;
- **desconto do futuro: 0,8.** Número escolhido por mim, em `configs/perfis.yaml`;
- a exponencial do softmax é calculada só com soma, produto e divisão, para dar o mesmo resultado em qualquer plataforma.

**Fumaça:** com 4 jogadores o Caçador ataca o líder; com 5, entram dois Caçadores, um que ataca o líder e outro que ataca o mais fraco. Todos contestam pelo limiar. O Aleatório entra com os valores do perfil experiente (explicação 85%, Auditor 95%).

### Verificação

- `uv run pytest`: 327 testes passam e 1 é pulado. `ruff` e `mypy` estrito sem apontamentos. Matriz: 148 de 148.
- Partida narrada com os quatro estilos lida por inteiro: os motivos gravados batem com o que cada estilo deve fazer.

### Resultado do experimento `fase2_fumaca_estilos`

Execução oficial no commit `058bd0e`, árvore limpa: 20.000 partidas em 236 s com 7 processos, nenhuma falha. Relatório em `resultados/fase2_fumaca_estilos/20261110-143205-058bd0e/relatorio.md`. Todos com conhecimento experiente, blefe moderado e contestação pelo limiar; rodízio de assentos.

**Taxa de vitória por bot (MET-07, sem veredito).** Referência de quem não leva vantagem: 0,250 com 4 jogadores e 0,200 com 5.

| Bot | 4 jogadores | 5 jogadores |
|---|---|---|
| Construtor | 0,457 (0,448 a 0,468) | 0,353 (0,344 a 0,362) |
| Heurístico | 0,368 (0,359 a 0,378) | 0,322 (0,313 a 0,331) |
| Caçador, ataca o líder | 0,172 (0,165 a 0,180) | 0,176 (0,168 a 0,183) |
| Caçador, ataca o mais fraco | — | 0,147 (0,140 a 0,154) |
| Aleatório | 0,002 (0,001 a 0,003) | 0,002 (0,001 a 0,003) |

REQ-09 saiu inconclusivo só porque a fumaça tem 20.000 partidas e o critério pede 50.000. Não houve nenhuma falha.

### Observações (é fumaça, não conclusão)

- **Os estilos jogam diferente**, que era o objetivo da fumaça. O sistema final médio do Construtor é cheio (5), o do Caçador fica perto de 3,5.
- **Primeiro sinal sobre o melhor estilo:** construir rende mais que caçar na v2.2.1. O Construtor vence quase o dobro da referência com 4 jogadores, e os dois Caçadores ficam abaixo dela. Se isso se confirmar na Fase 4, com mesas e perfis variados, é um achado de balanceamento: atacar pode estar valendo pouco, e a regra do PDF que pede "os dois estilos na mesa" (REQ-11) estaria em risco.
- **Caçar o mais fraco rende menos que caçar o líder** (0,147 contra 0,176, com 5 jogadores). É o contrário do que se viu na v1, segundo o artigo. É só a primeira medida; o Experimento 1 da Fase 3 olha isso na v1.
- **O Heurístico é o meu primeiro modelo de valor** e perde para o Construtor. Isso diz mais do modelo de valor do que do jogo.
- **Duração com bots que jogam de verdade:** com 5 jogadores, a mediana foi de cerca de 55 minutos, acima dos 50 do REQ-08, que tinha passado com bots aleatórios (49,2). Bots com estratégia testam mais: 33 testes por partida contra 27,6. Os tempos ainda são provisórios, mas é um alerta para a duração com 5 jogadores.
- **Baralho com 5 jogadores:** de 0,4% a 3,8% das partidas embaralharam o descarte; em nenhuma faltou carta.

---

## 2026-11-10 — Fase 3: v1 e Experimentos 1 e 2

### Decisões do autor

| Assunto | Opções | Escolha |
|---|---|---|
| A dúvida na v1 | a definição pesa; não pesa | **A definição não pesa:** o atacante decide só pelo perfil de contestação; a definição fica só registrada |
| Estilos na v1 | os quatro, traduzidos; só Aleatório e Caçador | Os quatro, traduzidos |
| Critério de partida desequilibrada (MET-01) | 1,5 × média dos outros; diferença para o 2º colocado | 1,5 × média dos outros, com 1,25 e 2,0 como sensibilidade. Fixado antes do Experimento 1 |
| Zona do REQ-02 | v2.2.1 menor por 0,05; só menor; só descrever | Resposta livre: "a v1 não deve ser balanceada, ela deve ser apenas analisada e observada; dito isto, menor por 0,05" |

**Princípio registrado:** a v1 é linha de base. Só é analisada e observada; nunca se propõe ajuste para ela.

### O que foi feito

1. **Regras da v1 em YAML** (`configs/regras_v1.yaml`): baralho da Tabela 3, números do artigo e as decisões AMB-20 a AMB-29.
2. **Motor da v1** (`regras/v1/`): estado, ações, motor, pontuação pela melhor divisão (AMB-24), observação e invariantes. Mesma interface do motor da v2.
3. **Núcleo comum:** `regras/familias.py` escolhe o motor pela família declarada no YAML. O laço da partida, o registro de auditoria, o replay, o executor e a linha de comando passaram a servir às duas famílias. Os registros de referência da v2 não mudaram com isso.
4. **Bots da v1** (`bots/v1.py`): os quatro estilos traduzidos, com os mesmos perfis de blefe e de conhecimento.
5. **Narração da v1** (`auditoria/narrar_v1.py`). A Folha de registro continua só para a v2.
6. **Métricas novas no executor e no relatório:** partidas desequilibradas (MET-01), matriz de política de alvo (MET-02) e a vantagem do líder com o veredito do REQ-02.
7. **Experimentos:** `experimentos/fase3_exp1_validacao_v1.yaml` (85 mil partidas) e `experimentos/fase3_exp2_v1_contra_v2.yaml` (40 mil).
8. **Testes novos:** 56, com pelo menos um por regra da v1. A matriz de rastreabilidade passou a cobrir as duas versões: 176 de 176 itens.
9. **Registro de referência da v1** com seis estilos e a narração `docs/exemplos/narracao_v1_estilos_mistos_6_jogadores.txt`.

### Detalhes escolhidos pelo assistente, sem perguntar

**Regras e motor da v1**
- **Tamanho do par (2 cartas) e do trio (3 cartas)** foram para o YAML e para a especificação (`v1.combinacoes`), para não haver número de regra no código.
- O parâmetro `v1.blefe_aceito` da especificação passou a se chamar `v1.interpretacoes.blefe_aceito`, como no YAML.
- **Fluxo da dúvida:** depois da declaração, o atacante escolhe aceitar ou duvidar; depois da definição, aceitar ou contestar. Aceitar sem duvidar e aceitar depois da definição dão o mesmo resultado.
- **Informação pública:** a carta de ataque que vai para o sistema do defensor fica conhecida pela mesa. Depois de uma carta tirada ao acaso de um sistema, a mesa deixa de saber quais cartas conhecidas continuam nele.
- **REQ-02 na v1:** o ponto de corte é quando todos fizeram o primeiro teste, e o placar ali é o número de cartas no sistema.

**Bots da v1**
- Construtor, Caçador e Heurístico montam o sistema de 3 cartas que mais pontua (empate sorteado).
- O defensor que tem a cor sempre declara que tem; sem a cor, blefa com a chance do perfil.
- Com o perfil "nunca contesta", o bot nem duvida; com os outros, sempre duvida, porque duvidar não custa nada.
- O Caçador escolhe o alvo pela política e a carta ao acaso. O Construtor escolhe carta e alvo ao acaso.
- **Heurístico da v1:** valor = chance de o alvo não ter a cor × (1 + 1/(N − 1)) − (chance de ter) × 1/(N − 1). A Critical Failure vale uma carta certa. O desconto do futuro não é usado na v1.
- O limiar de contestação da v1 sai dos números da v1, pela mesma conta de R-7.3.5: 1 / (1 + 2) = 1/3.

**Métricas e experimentos**
- **MET-01:** "os demais" são todos menos o primeiro colocado; partida com placar zerado não conta como desequilibrada.
- **REQ-02:** só entram partidas com um líder isolado no corte. A vantagem é a média da fração de vitória do líder menos 1/N, e o intervalo da diferença entre v1 e v2.2.1 vem de bootstrap com as duas amostras independentes.
- **Experimento 1:** mesas de 6. Matriz 3 × 3 com um Caçador foco contra cinco Caçadores com outra política, rodízio de assentos, 6.000 partidas por célula. Cinco populações de bots idênticos (5.000 partidas cada) e uma mesa mista (6.000).
- **Experimento 2:** mesas mistas de 4 e 5 jogadores nas duas versões, com a mesma formação da fumaça da Fase 2, rodízio de assentos e as mesmas sementes. 10.000 partidas por versão e por tamanho de mesa.
- Todos com conhecimento experiente, blefe moderado e contestação pelo limiar, como na Fase 2.

### Defeitos achados e corrigidos durante a fase

Os dois foram apontados pelos invariantes na primeira fumaça da v1:
- **Carta contada duas vezes:** numa defesa bem-sucedida, a carta de ataque já estava no sistema do defensor, mas a disputa ainda apontava para ela até fechar. A disputa agora marca que a carta foi entregue.
- **Fim antes do vencedor:** a fase passava a "fim" antes de o vencedor ser definido, e os eventos de pontuação no meio ficavam num estado incoerente.

### Verificação

- `uv run pytest`: 383 testes passam e 1 é pulado. `ruff` e `mypy` estrito sem apontamentos. Matriz: 176 de 176.
- Fumaça da v1: 600 partidas com os invariantes conferidos a cada evento; replay nos dois modos.
- Narração de uma partida da v1 lida por inteiro: declaração, dúvida, definição, contestação, cartas tiradas ao acaso e pontuação seguem o artigo e as decisões AMB-20 a AMB-29.

### Experimento 1 interrompido e correções (2026-11-10)

**O que aconteceu.** A primeira execução oficial do Experimento 1 (commit `756f209`) parou no meio, junto com um travamento do VS Code. O registro da execução mostra que uma partida do cenário `todos_cacadores_lider` (partida 2731) foi marcada como falha e que, em seguida, a gravação do arquivo dela deu um erro do Windows (`OSError 22`), que derrubou o experimento. O Experimento 2 não chegou a começar. Os 442 registros parciais, sem manifest, foram apagados.

**Diagnóstico.** A mesma partida, jogada sozinha, termina normalmente: não é defeito das regras. A causa mais provável, não medida (a medição foi interrompida), é falta de memória. A pontuação da v1 guardava em memória todas as combinações já calculadas, sem limite, em cada processo. Os Caçadores da v1 acumulam sistemas grandes, e a máquina tinha 0,8 GB livres de 7,8.

**Decisão do autor:** trocar o cálculo por conta direta, implementar as propostas e refazer os experimentos.

**Correções:**
1. **Pontuação da v1 por conta direta** (`regras/v1/pontuacao.py`), sem busca e sem guardar nada entre partidas. De um atributo dá para tirar `p` pares se, contando no máximo `p` cartas de cada teste, sobram pelo menos `2p`; para os trios só importa quantas cartas de cada atributo sobraram. O cálculo percorre quantos pares sair de cada atributo e, para cada escolha, o máximo de trios. Um teste compara a conta direta com a busca exaustiva antiga em 300 sistemas aleatórios, inclusive com valores de par e trio diferentes dos da v1; outro mostra que um sistema de 40 cartas é pontuado em menos de 1 segundo. O registro de referência da v1 não mudou.
2. **O executor não cai mais se a gravação de um registro falhar:** a partida ganha um aviso na tabela (`aviso`), e o manifest conta os registros não gravados. Um teste simula o erro de disco.
3. **Os experimentos da Fase 3 rodam com 4 processos**, em vez de 7, para sobrar memória para o resto da máquina.

**Detalhe escolhido pelo assistente, sem perguntar:** o executor exige a árvore do git limpa, e o manifest e o relatório do Experimento 1 ainda não estavam no git. Por isso eles foram commitados (`f447f4b`) antes de o Experimento 2 começar. O código dos dois experimentos é o mesmo (`ad1624f`).

### Resultado do Experimento 1 (`fase3_exp1_validacao_v1`)

Execução oficial no commit `ad1624f`, árvore limpa: 85.000 partidas em 1.214 s com 4 processos, nenhuma falha (REQ-09 passa). Relatório em `resultados/fase3_exp1_validacao_v1/20261110-205949-ad1624f/relatorio.md`. Mesas de 6; todos os bots com conhecimento experiente, blefe moderado e contestação pelo limiar.

**Partidas desequilibradas (MET-01, critério fixado antes da execução).** Referência do artigo: 4 de 6 partidas (0,667; IC 95% de 0,300 a 0,903).

| População (6 bots iguais, salvo a mista) | Fator 1,5 (principal) | Fator 2,0 (sensibilidade) |
|---|---|---|
| Aleatórios | 0,958 | 0,663 |
| Construtores | 0,998 | 0,964 |
| Caçadores que atacam o líder | 0,991 | 0,960 |
| Caçadores que atacam o mais fraco | 0,957 | 0,622 |
| Heurísticos | 0,999 | 0,960 |
| Estilos mistos | 0,998 | 0,945 |

Os intervalos têm cerca de ±0,01.

**Política de alvo (MET-02).** Taxa de vitória de 1 Caçador (o foco, na linha) numa mesa em que os outros 5 usam a política da coluna. Referência 1/6 = 0,167.

| Foco \ Outros | líder | mais fraco | ao acaso |
|---|---|---|---|
| líder | — | 0,233 (0,224 a 0,243) | 0,134 (0,126 a 0,143) |
| mais fraco | 0,179 (0,168 a 0,189) | — | 0,134 (0,126 a 0,142) |
| ao acaso | 0,184 (0,175 a 0,193) | 0,286 (0,275 a 0,297) | — |

**Vantagem do líder** (chance de vencer de quem lidera sozinho depois que todos fizeram o primeiro teste, menos 1/6): de 0,32 a 0,62 conforme a população. Quem lidera no corte vence entre 49% e 78% das partidas.

**Mesa mista (MET-07):** Heurístico 0,220; Construtor 0,214; Caçadores de 0,166 a 0,189; Aleatório 0,029. Referência 0,167.

### Resultado do Experimento 2 (`fase3_exp2_v1_contra_v2`)

Execução oficial no commit `f447f4b`, árvore limpa: 40.000 partidas em 257 s com 4 processos, nenhuma falha. Relatório em `resultados/fase3_exp2_v1_contra_v2/20261110-212034-f447f4b/relatorio.md`. Mesmas mesas mistas da fumaça da Fase 2, nas duas versões, com rodízio de assentos e as mesmas sementes.

**REQ-02 (vantagem do líder): passa** com 4 e com 5 jogadores.

| Jogadores | v1 | v2.2.1 | Diferença (IC 95%) | Zona |
|---|---|---|---|---|
| 4 | 0,392 | 0,087 | 0,305 (0,290 a 0,319) | pelo menos 0,05 |
| 5 | 0,419 | 0,091 | 0,328 (0,316 a 0,342) | pelo menos 0,05 |

**Taxa de vitória por estilo (MET-07, sem veredito).**

| Bot | v1, 4 jog. | v2.2.1, 4 jog. | v1, 5 jog. | v2.2.1, 5 jog. |
|---|---|---|---|---|
| Construtor | 0,323 | 0,455 | 0,259 | 0,349 |
| Heurístico | 0,354 | 0,370 | 0,262 | 0,331 |
| Caçador, ataca o líder | 0,260 | 0,173 | 0,200 | 0,173 |
| Caçador, ataca o mais fraco | — | — | 0,233 | 0,146 |
| Aleatório | 0,063 | 0,003 | 0,045 | 0,001 |
| Referência 1/N | 0,250 | 0,250 | 0,200 | 0,200 |

**Partidas desequilibradas (MET-01):** com o fator 1,5, v1 0,991 e 0,996; v2.2.1 0,928 e 0,943 (4 e 5 jogadores). Com o fator 2,0, v1 0,921 e 0,937; v2.2.1 0,553 e 0,532.

**Duração da v2.2.1 (descrição; o REQ-08 não estava neste experimento):** medianas de 45,5 a 45,9 min com 4 jogadores e de 54,5 a 55,2 min com 5.

O REQ-09 saiu inconclusivo só porque o experimento tem 40.000 partidas e o critério pede 50.000. Somados os dois experimentos, foram 125.000 partidas sem nenhuma falha.

### Observações (cuidado ao ler)

1. **A v1 do simulador tem a bola de neve do artigo, e a v2.2.1 quase não tem.** A vantagem do líder cai de cerca de 0,40 para cerca de 0,09. É a primeira evidência, com bots, de que o redesenho atacou o problema da v1.
2. **Pelo critério principal, a v1 do simulador é mais desequilibrada que as 6 partidas do artigo.** Todas as populações ficaram acima de 0,95, acima do limite superior do intervalo do artigo (0,903). Com o fator 2,0, as duas populações mais parecidas com o que o artigo relata (aleatórios e caçadores do mais fraco) ficam em 0,66 e 0,62, dentro do intervalo. O critério não foi mudado: foi fixado antes. Leituras possíveis: bots não jogam como alunos; o "significativamente" do artigo pode querer dizer uma diferença maior que 1,5 vez; 6 partidas são pouca evidência.
3. **O MET-01 com o fator 1,5 quase não separa as versões** (v2.2.1 acima de 0,93). O placar da v1 é em pontos e o da v2 em fichas; a razão entre o vencedor e a média dos demais não está na mesma escala nas duas. Com o fator 2,0 as versões se separam (0,92 a 0,94 contra 0,53 a 0,55). Ponto para o autor decidir antes de usar o MET-01 na v2.
4. **Na v1, atacar o mais fraco não é a melhor resposta para os bots.** A pergunta do Experimento 1 era se o simulador mostraria isso, e a resposta é não. Escolher o alvo ao acaso empata com a melhor resposta ou é a melhor contra as três populações, e é a única das três políticas em que ninguém ganha mudando sozinho. Explicação mecânica: na v1, a defesa bem-sucedida dá a carta de ataque ao defensor. Quem ataca o líder, que tem sistema grande e quase sempre tem o atributo, alimenta o líder (na população "todos atacam o líder", o vencedor faz 27 pontos e a média é 8). Quem ataca o mais fraco acerta mais, mas um sistema vazio não tem o que tomar (AMB-25).
5. **A v2.2.1 tirou a bola de neve, mas afastou construir de caçar.** Na v1 os estilos ficam próximos (com 4 jogadores, Heurístico 0,354, Construtor 0,323, Caçador 0,260). Na v2.2.1 o Construtor vence 0,455 e o Caçador fica abaixo da referência (0,173). Isso alimenta a pergunta da Fase 4 sobre o melhor estilo, o REQ-04 (nenhum perfil dominante) e o REQ-11 (os dois estilos na mesa).
6. **A duração com 5 jogadores e bots com estratégia** fica em 55 min, acima do teto de 50 do REQ-08, como na fumaça da Fase 2. Os tempos do modelo ainda são provisórios.

### Pendências (parada para revisão da Fase 3)

- Revisão dos resultados pelo autor.
- MET-01 na v2: manter o fator 1,5, passar a usar o 2,0 ou adotar outro critério que valha nas duas escalas.
- Decisões da Fase 4: ordem dos experimentos 3 a 6; zonas de REQ-03 a REQ-07 e de REQ-10 a REQ-14; mecânica de VAR-02, VAR-03, VAR-04 e VAR-06; se o REQ-08 terá a parte "acima de 60 minutos".
- Do autor: rever a redação dos trechos marcados em `regras/v2.2.1.md` e `regras/v1.md`.

---

## 2026-11-10 — Fase 4: o melhor estilo de jogo

### Decisões do autor

| Assunto | Opções | Escolha |
|---|---|---|
| Revisão da Fase 3 | — | "Aprovo suas sugestões, siga avançando nas fases" |
| MET-01 na v2 | manter o fator 1,5 nas duas versões; passar a 2,0; outro critério; 1,5 só na v1 | 1,5 só na v1. Na v2 o MET-01 é só descrição, e a comparação entre as versões é feita pelo REQ-02 |
| Ordem da Fase 4 | sugestão do assistente | Primeiro o melhor estilo (REQ-04 e REQ-11), depois o torneio de blefe (Experimento 5), as variantes do playtest (Experimento 6), a ablação (3) e a sensibilidade (4) |
| Zonas e variantes da Fase 4 | todas agora; na hora de cada experimento | Na hora do experimento que as usa |
| Estilos na matriz (MET-07) | 6; 4 | 6: Aleatório, Construtor, Heurístico e o Caçador com as três políticas de alvo (líder, mais fraco, ao acaso) |
| Estilo dominante (REQ-04) | melhor resposta; acima da referência | **Melhor resposta contra todas as mesas**, inclusive a de bots iguais a ele, com o intervalo da diferença inteiro acima de 0. Vale também para os perfis de blefe. Corrige a redação anterior ("acima de 1/N + 0,02 contra todas as mesas, inclusive a do próprio perfil"), que nunca acusaria dominância, porque na mesa do próprio perfil o foco vence exatamente 1/N |
| Zona do REQ-03 | só o piso; 1,5/N a 0,85; 1,5/N a 0,95 | **Só o piso: acima de 1,5/N.** O Aleatório quase nunca vence na v2.2.1, então um teto diria mais sobre ele do que sobre o jogo |
| Zona do REQ-11 | 0,10 a 0,90; 0,25 a 0,75 | 0,10 a 0,90 |

### O que foi feito

1. **Matriz de estilos** (`metricas/matrizes.py`). Um cenário pode declarar `matriz` e `celula` (estilo do foco, estilo dos outros). A análise calcula cada célula com o seu intervalo, as melhores respostas a cada mesa, a situação de cada estilo no REQ-04 (dominante, não dominante ou indefinido, com o motivo) e a dinâmica do replicador.
2. **REQ-03 e REQ-11 medidos.** O motor da v2 passou a informar quem terminou o Planejamento do ciclo 1 com o sistema no teto. A informação vai para uma coluna nova da tabela de partidas (`cheios_no_planejamento_1`), e o relatório a mostra para todos os cenários.
3. **Relatório:** seção da matriz de estilos. As rotações de uma célula de matriz aparecem somadas, numa linha só, na descrição e na lista de cenários. O MET-07 deixou de dizer que aguarda o autor, e o MET-01 ganhou a nota sobre a v2.
4. **Uma só função de análise** (`metricas/analise.py`) para o executor e para o `cf relatorio`. Assim o relatório refeito continua igual ao original.
5. **Experimento** `experimentos/fase4_melhor_estilo.yaml`: 140.000 partidas.
6. **Testes novos:** 8, contando os três casos do REQ-04. Cobrem a coluna de sistemas cheios, conferida evento a evento; o replicador em dois casos com resposta conhecida; o REQ-04 nos três vereditos, com matrizes montadas à mão; um experimento do melhor estilo em miniatura, com o relatório refeito; e a validação do arquivo do experimento.

### Verificação

- `uv run pytest`: 394 testes passam e 1 é pulado. `ruff` e `mypy` estrito sem apontamentos. Matriz de rastreabilidade e registros de referência sem mudança.

### Detalhes escolhidos pelo assistente, sem perguntar

- **A diagonal não roda:** com bots iguais e rodízio, o foco vence exatamente 1/N.
- **2.000 partidas por célula** (500 por rotação com 4 jogadores, 400 com 5). O intervalo de cada célula fica em cerca de ±0,02.
- **Diferença entre duas células:** cada célula tem as suas 1.000 reamostras de bootstrap, e o intervalo da diferença sai das diferenças entre as médias reamostradas, como amostras independentes. Não há correção para comparações múltiplas: com 6 estilos são 180 comparações por matriz.
- **Dinâmica do replicador:** tempo discreto (cada proporção é multiplicada pelo ganho do estilo e dividida pelo ganho médio), a partir da população uniforme, até 200.000 passos ou até a mudança ficar abaixo de 10⁻¹². É uma aproximação linear: numa população mista, o ganho de um estilo é a média dos seus ganhos contra cada população pura, pesada pelas proporções.
- **Mesas só de Heurísticos** com 10.000 partidas por tamanho de mesa. Nelas também é medido o REQ-01, que já estava confirmado: é a primeira medida da equidade de assento com bots que jogam com estratégia.
- **REQ-11:** a média é sobre as partidas, e o intervalo vem de bootstrap sobre as partidas, porque jogadores da mesma partida não são independentes. "Cheio" quer dizer sistema com o número de cartas do teto (`sistema.teto` do YAML).
- **Perfis:** os mesmos das Fases 2 e 3 (experiente, blefe moderado, contestação pelo limiar); o Aleatório com explicação 85% e Auditor 95%. Semente mestre 20261114; 4 processos.

### Resultado do experimento `fase4_melhor_estilo`

Execução oficial no commit `ccd5649`, árvore limpa: 140.000 partidas em 2.693 s com 4 processos, nenhuma falha (REQ-09 passa). Relatório em `resultados/fase4_melhor_estilo/20261110-221516-ccd5649/relatorio.md`.

**Primeira execução descartada.** A primeira execução, no commit `0834531` e com a mesma semente, gerou um relatório com dois defeitos de apresentação. A seção da matriz de alvos da v1 (MET-02) aparecia vazia, e o MET-01 listava as 60 células da matriz. O código do relatório foi corrigido (`ccd5649`, com teste) e o experimento rodou de novo. A tabela de partidas das duas execuções é idêntica byte a byte (mesmo SHA-256, `1744a69c…`), o que confirma o determinismo: só o relatório mudou. A pasta da primeira execução não foi guardada.

**Matriz de estilos, 4 jogadores (MET-07).** Taxa de vitória do foco (linha) contra a mesa (coluna); referência 0,250; intervalos de cerca de ±0,02. Em negrito, as melhores respostas a cada mesa.

| Foco \ Mesa | Aleatório | Construtor | Heurístico | Caçador líder | Caçador mais fraco | Caçador ao acaso |
|---|---|---|---|---|---|---|
| Aleatório | 0,250 | 0,001 | 0,002 | 0,055 | 0,004 | 0,004 |
| Construtor | **0,973** | **0,250** | **0,239** | **0,531** | 0,383 | **0,427** |
| Heurístico | 0,938 | **0,264** | **0,250** | **0,549** | **0,434** | **0,451** |
| Caçador líder | **0,965** | 0,168 | 0,113 | 0,250 | 0,387 | 0,294 |
| Caçador mais fraco | 0,925 | 0,134 | 0,083 | 0,202 | 0,250 | 0,203 |
| Caçador ao acaso | 0,943 | 0,146 | 0,087 | 0,234 | 0,325 | 0,250 |

**Matriz de estilos, 5 jogadores.** Referência 0,200.

| Foco \ Mesa | Aleatório | Construtor | Heurístico | Caçador líder | Caçador mais fraco | Caçador ao acaso |
|---|---|---|---|---|---|---|
| Aleatório | 0,200 | 0,000 | 0,002 | 0,066 | 0,005 | 0,002 |
| Construtor | **0,971** | 0,200 | 0,165 | **0,530** | 0,352 | 0,378 |
| Heurístico | 0,926 | **0,240** | **0,200** | **0,524** | **0,405** | **0,428** |
| Caçador líder | 0,948 | 0,145 | 0,085 | 0,200 | 0,357 | 0,253 |
| Caçador mais fraco | 0,901 | 0,098 | 0,048 | 0,176 | 0,200 | 0,164 |
| Caçador ao acaso | 0,925 | 0,116 | 0,072 | 0,185 | 0,268 | 0,200 |

**Requisitos**

| Requisito | Resultado |
|---|---|
| REQ-03, habilidade importa | **passa**: o Heurístico contra Aleatórios vence 0,938 (0,927 a 0,949) com 4 jogadores e 0,926 (0,913 a 0,937) com 5. Piso: 0,375 e 0,300 |
| REQ-04, nenhum estilo dominante | **passa** com 4 e com 5 jogadores: nenhum estilo é a melhor resposta contra todas as mesas |
| REQ-11, os dois estilos aparecem | **passa**: 51,4% (4 jogadores) e 50,8% (5) dos Heurísticos terminam o 1º Planejamento com o sistema cheio. Zona: 10% a 90% |
| REQ-01, equidade de assento (mesas de Heurísticos) | **inconclusivo**. Com 4 jogadores, o primeiro vence 0,276 (0,268 a 0,285) e o último 0,224 (0,216 a 0,233), para uma zona de 0,230 a 0,270. Com 5, o primeiro vence 0,222 (0,215 a 0,231) e o último 0,181 (0,174 a 0,189), para uma zona de 0,180 a 0,220 |

**Dinâmica do replicador:** termina em 100% Heurísticos, com 4 e com 5 jogadores.

### Observações (cuidado ao ler)

1. **O melhor estilo é o Heurístico.** Ele é melhor resposta, sozinho ou empatado, contra todas as mesas menos a de Aleatórios, onde o Construtor rende mais (0,973 contra 0,938). A dinâmica do replicador termina nele. O Construtor vem logo atrás e empata com o Heurístico em várias mesas.
2. **Construir vence caçar na v2.2.1.** Nenhum Caçador é melhor resposta a mesa nenhuma, a não ser a de Aleatórios. Numa mesa de Construtores, um Caçador vence de 0,13 a 0,17 com 4 jogadores, para uma referência de 0,25. Isso confirma o sinal das Fases 2 e 3. Mesmo assim, o REQ-11 passa: o próprio Heurístico enche o sistema em metade das vezes e, nas outras, guarda cartas para testar. Os dois estilos aparecem dentro das decisões de um jogador que joga bem, não como dois tipos de jogador.
3. **O REQ-04 passa só por causa da mesa de Aleatórios.** Sem essa coluna, o Heurístico ficaria "indefinido": nenhum estilo o supera com clareza, mas ele não supera o Construtor com clareza em todas as mesas, e o veredito seria inconclusivo. O critério foi fixado antes e não foi mudado. Vale lembrar também que "nenhum estilo dominante" vale só entre os 6 estilos escritos pelo assistente.
4. **Política de alvo na v2.2.1 (o MET-02 da v1, agora na v2):** entre os Caçadores, atacar o líder é a melhor resposta contra as três populações de Caçadores, e atacar o mais fraco é a pior. É o contrário da v1, onde o alvo ao acaso era o melhor e atacar o líder alimentava o líder. Na v2.2.1, atacar quem lidera compensa.
5. **Vantagem do primeiro jogador com bots que jogam bem.** Com Aleatórios, o REQ-01 passou (Fase 1b). Com Heurísticos, o primeiro da ordem vence cerca de 2,5 pontos percentuais acima de 1/N, e o último cerca de 2,5 abaixo, bem na borda da zona de 2 pontos. Não é medida de mudança de regra: fica como pendência para o autor.
6. **Duração (descrição; o REQ-08 não foi medido aqui):** nas mesas só de Heurísticos, as medianas foram de 42,3 min com 4 jogadores e de 49,7 com 5. Nas células com 5 jogadores, ficaram entre 50,5 e 54,2.

### Decisões do autor para o Experimento 5 (torneio de blefe)

| Assunto | Opções | Escolha |
|---|---|---|
| Estilo dos 9 perfis puros de blefe | Heurístico; Construtor; os dois | Heurístico |
| Tamanho | 1.000 por célula com 4 e 5 jogadores; 2.000 por célula; só 4 jogadores | 1.000 por célula, com 4 e com 5 jogadores, e 2.000 partidas por mesa de perfis iguais |
| REQ-05 | 0,30 a 0,50 no equilíbrio; só descrição; outra zona | 0,30 a 0,50, com veredito no equilíbrio da dinâmica do replicador do torneio. Se ela terminar num perfil só, vale a mesa desse perfil; se terminar numa mistura, roda depois uma mesa sorteada da mistura. As 9 populações aparecem como faixa, só como descrição |

### Pendências

- REQ-01 com bots que jogam bem: a vantagem do primeiro jogador está na borda da zona.

## 2026-11-10 — Fase 4, Experimento 5: equilíbrio do blefe

As decisões do autor estão na entrada anterior (estilo Heurístico; 1.000 partidas por célula, com 4 e 5 jogadores; REQ-05 entre 0,30 e 0,50, com veredito no equilíbrio).

### O que foi feito

1. **Blefes contados em toda partida.** O motor da v2 diz quando uma defesa é blefe (AMB-15) e quando uma disputa termina aceita. O laço da partida conta os blefes tentados e os bem-sucedidos, e a tabela de partidas ganhou as colunas `blefes` e `blefes_bem_sucedidos`. Na v1 a contagem é zero: o REQ-05 é da v2.
2. **Mesas de perfis iguais na matriz.** A diagonal de uma matriz pode ser rodada como mesa de bots iguais, sem rodízio. Ela não entra como célula (a taxa do foco seria exatamente 1/N) e serve para medir a população pura.
3. **REQ-05 no equilíbrio** (`metricas/matrizes.py`). Se a dinâmica do replicador termina num perfil só (pelo menos 99,9% da população), o veredito sai da mesa de perfis iguais desse perfil. Se termina numa mistura, a medida sai inconclusiva, com a mistura na nota, e fica para uma mesa sorteada da mistura. Se no equilíbrio ninguém blefa, também sai inconclusiva, com nota.
4. **Relatório:** tabela das mesas de perfis iguais (blefes por partida, fração bem-sucedida e intervalo) e coluna "Blefes por partida (bem-sucedidos)" na descrição. A seção das matrizes passou a se chamar "Matrizes de ganhos entre estilos ou perfis".
5. **Experimento** `experimentos/fase4_exp5_blefe.yaml`: 180.000 partidas.
6. **Testes novos:** 9. Conferem a contagem de blefes evento a evento; o intervalo da razão; o REQ-05 em quatro casos montados à mão (passa, falha, equilíbrio misto, ninguém blefa); a diagonal como mesa de bots iguais; um torneio em miniatura com o relatório refeito; e o arquivo do experimento.

### Verificação

- `uv run pytest`: 403 testes passam e 1 é pulado. `ruff` e `mypy` estrito sem apontamentos. Matriz 176 de 176; registros de referência sem mudança.

### Detalhes escolhidos pelo assistente, sem perguntar

- **Nomes dos perfis:** `blefa_<nunca|metade|sempre>_contesta_<nunca|sempre|limiar>`.
- **Intervalo do REQ-05:** razão das somas (blefes bem-sucedidos sobre blefes tentados), com bootstrap sobre as partidas, porque os blefes de uma mesma partida não são independentes.
- **"Termina num perfil só":** pelo menos 99,9% da população, com a dinâmica parada.
- **Semente mestre 20261115; 4 processos.**

## 2026-11-10 — Fase 4, Experimento 6: variantes do playtest

### Decisões do autor

| Assunto | Opções | Escolha |
|---|---|---|
| VAR-04, vizinho designado | só o alvo; alvo e 1 teste por ciclo | **Só o alvo**: todo teste do ciclo vai para o vizinho designado (esquerda, direita, esquerda); sem limite de testes e com o bug duplicado; sem teste legal contra o vizinho, o jogador passa |
| VAR-02, custo extra da explicação | +1 ficha ao banco; +1 ao atacante | **+1 ficha ao banco**, além do "Falhou" |
| VAR-03, Auditor externo | 95% (perfil experiente); 100% | **95%**. Todos jogam e diagnosticam; a função não passa de mão em mão |
| VAR-06, voto da mesa | só o palpite do PDF; as duas formas; fora do simulador | **Só o palpite do PDF**. O bot vota "blefe" quando a chance estimada passa de 1/2 |
| AMB-30, o Auditor vota no palpite? | não; sim | **Não vota** |
| AMB-31, de onde vem a ficha do palpite | do banco; de quem errou | **Do banco** |
| Desenho | Heurísticos com 2.000; com 5.000; com mesa mista | **Mesas só de Heurísticos, 2.000 partidas por cenário**: 10 configurações (a base e as variantes) × 2 perfis de conhecimento × 2 tamanhos de mesa = 40 cenários, 80.000 partidas |
| Zonas de REQ-06, REQ-07, REQ-12 e REQ-13 | confirmar; mudar | **Confirmadas** como na Fase 0. O REQ-14 fica só como descrição |
| REQ-10, tempo parado | p90 abaixo de 5 min; mediana; só descrição | **p90 abaixo de 5 min** |
| Blefe dos bots no Experimento 6 | mesa sorteada do equilíbrio do Experimento 5; blefe moderado e limiar | **Mesa sorteada do equilíbrio**: cada assento é sorteado da mistura de perfis de blefe do equilíbrio, com os pesos do Experimento 5b |

### O que foi feito

1. **Variantes no motor**, atrás do bloco opcional `variantes` do YAML (VAR-02 a VAR-06). Sem o bloco, vale a regra da versão, e o hash das versões já usadas não muda. Um experimento liga uma variante passando o bloco inteiro em `mudancas`. VAR-01, VAR-07 e VAR-09 já eram parâmetros do YAML.
   - VAR-02: evento `custo_da_explicacao`, depois da conferência que não confere.
   - VAR-03: o motor julga a explicação no mesmo passo da defesa, com um sorteio do fluxo do jogo (95 acertos em 100); a conferência sai sem ator, citando VAR-03.
   - VAR-04 e VAR-05: restringem os alvos legais.
   - VAR-06: decisão nova, `palpitar`, para cada votante. O voto é secreto até o último votar, e os votos são revelados antes da decisão do atacante. Havendo contestação, quem acertou ganha do banco.
2. **Estado:** a disputa ganhou o campo `palpites`, que fica fora do hash enquanto vazio (`OMITIR_SE_PADRAO` em `nucleo/canonico.py`). Os registros de referência não mudaram.
3. **Bots:** os estilos com estratégia votam no palpite; o Aleatório sorteia.
4. **Coletor de medidas** (`coleta.py`): em toda partida da v2, testes recebidos por jogador, testes contra o menor placar, se alguém ficou com 0 ficha antes do último ciclo, tempo parado por jogador e ciclo, quem começou cobrindo a categoria-chave do incidente 1 e fichas movimentadas (no total e pelo dano de incidente). São 7 colunas novas na tabela de partidas.
5. **Requisitos medidos:** REQ-06 (a e b), REQ-07, REQ-10, REQ-12 e REQ-13, cenário a cenário. O relatório ganhou a seção "Equilíbrio dentro da partida (descrição)", com a dispersão final do REQ-14.
6. **Especificação:** a seção de variantes ganhou a coluna "Mecânica"; AMB-30 e AMB-31 em `docs/AMBIGUIDADES.md`.
7. **Experimento** `experimentos/fase4_exp6_variantes.yaml`: 80.000 partidas.
8. **Mesa sorteada de uma mistura** (`pesos` no cenário): cada assento de cada partida é sorteado entre os perfis candidatos, com pesos inteiros e um fluxo de aleatoriedade próprio (`FLUXO_DA_MESA`). A tabela ganha a coluna `bots_da_mesa`; a taxa de vitória por perfil usa a mesa sorteada; o REQ-05 recebe veredito nesse tipo de cenário.
9. **Testes novos:** 27. Cada variante tem o seu teste, sobre partidas com os invariantes conferidos; o coletor é conferido contra os eventos; cada requisito novo tem um caso que passa e um que falha; o sorteio por pesos e a mesa sorteada têm testes próprios (o replay refaz a mesma mesa); há também uma miniatura do Experimento 6, com o relatório refeito.

### Detalhes escolhidos pelo assistente, sem perguntar

- **Teste de convenção:** na v2, o evento de uma variante cita a própria variante (`VAR-xx`), e o teste que exige uma regra em todo evento passou a aceitar esse formato.
- **Variantes juntas:** o palpite da plateia com o Auditor externo não foi definido (quem votaria?), e a configuração recusa os dois juntos.
- **REQ-06 (b):** empate no menor placar conta como teste contra o menor, e "os outros" são todos menos o atacante.
- **REQ-07:** "antes do ciclo 3" é qualquer evento dos ciclos anteriores ao último.
- **REQ-10:** o tempo de cada evento vem do modelo de duração. Na Produção ninguém fica parado (todos diagnosticam juntos). Numa disputa, ficam livres o atacante, o defensor e o Auditor (com o Auditor externo, só os dois primeiros). No Planejamento, só quem tem a vez. O palpite da plateia não tem tempo no modelo (0 s), porque o voto é com o polegar, enquanto o atacante decide. O intervalo vem de bootstrap sobre as partidas.
- **REQ-12:** "cobrir" é ter, no sistema inicial, uma carta da categoria-chave do incidente 1. O intervalo trata os assentos como independentes.
- **REQ-13:** o dano do Critical Failure não conta como dano de incidente; o total inclui todas as fontes, inclusive a pontuação final.
- **Mistura no Experimento 6:** os pesos do equilíbrio foram medidos com conhecimento experiente e na regra sem variante; o Experimento 6 usa os mesmos pesos com conhecimento iniciante e com as variantes. O REQ-12 pede bots idênticos, e na mesa sorteada só o perfil de blefe varia (o estilo é o mesmo). Semente mestre 20261116.

### Defeito achado no Experimento 5: a dinâmica do replicador parava num ponto que não era equilíbrio

A primeira análise do torneio de blefe (execução `b02b6d4`) dizia que a dinâmica terminava em "nunca blefa, contesta pelo limiar" (4 jogadores) e em "nunca blefa, nunca contesta" (5 jogadores). Com isso, o REQ-05 saía inconclusivo, com a nota "nessa mesa ninguém blefa". Estava errado: nas duas mesas, outro perfil se sai melhor que esse "equilíbrio" (por exemplo, contra uma mesa de "nunca blefa, nunca contesta", quem sempre blefa e nunca contesta vence 0,463, para uma referência de 0,25).

**Causa:** os perfis de blefe formam um ciclo, como pedra-papel-tesoura. Quem nunca blefa nem contesta perde para quem sempre blefa; quem sempre blefa perde para quem contesta pelo limiar; quem contesta perde para quem nunca contesta numa mesa de honestos. A versão da dinâmica em tempo discreto, com passo cheio, espirala para fora num jogo assim e chega perto de um vértice. Ali a mudança fica menor que a tolerância, e o critério de parada leu isso como equilíbrio.

**Correção** (`metricas/matrizes.py`): a dinâmica passou a usar tempo contínuo, com passo pequeno (0,05). No fim, só vale como equilíbrio se nenhum perfil se sair melhor que a média ali. Dois testes novos de pedra-papel-tesoura cobrem os dois casos: o equilíbrio misto que atrai a trajetória e o que a repele. Nas duas matrizes do torneio, a dinâmica corrigida converge para o único equilíbrio simétrico do jogo linearizado, conferido por fora com a enumeração de todos os suportes. A matriz de estilos não muda: lá o Heurístico é um equilíbrio estrito.

**Relatório refeito com registro:** o `cf relatorio` agora anota no manifest (`relatorio_refeito`) e no cabeçalho do relatório quando a análise é refeita com o código de outro commit. O hash novo do relatório também vai para o manifest. A execução e a tabela de partidas continuam as originais. O relatório do Experimento 5 foi refeito assim.

### Experimento 5b: REQ-05 no equilíbrio misto

Pela decisão do autor, com equilíbrio misto o REQ-05 vale numa mesa sorteada da mistura. O arquivo `experimentos/fase4_exp5b_blefe_equilibrio.yaml` foi gerado a partir da tabela do Experimento 5, pela análise corrigida: pesos em milésimos, arredondados pelos maiores restos. Com 4 jogadores, 325, 501, 133 e 41 (nunca blefa e nunca contesta; nunca blefa e contesta pelo limiar; sempre blefa e nunca contesta; sempre blefa e contesta pelo limiar). Com 5 jogadores, 313, 541, 133 e 13. São 10.000 partidas por tamanho de mesa; semente mestre 20261117.

### Resultado do Experimento 5 (`fase4_exp5_blefe`)

Execução oficial no commit `b02b6d4`, árvore limpa: 180.000 partidas em 4.760 s com 4 processos, nenhuma falha (REQ-09 passa). Relatório em `resultados/fase4_exp5_blefe/20261110-231109-b02b6d4/relatorio.md`. O relatório original, com a análise do replicador com defeito, está no commit `e387763`. A versão atual foi refeita com o código corrigido, e o refazimento está registrado no manifest e no cabeçalho do relatório.

| Requisito | Resultado |
|---|---|
| REQ-04, nenhum perfil dominante | **passa** com 4 e com 5 jogadores: nenhum perfil puro de blefe é a melhor resposta contra todas as mesas |
| REQ-05, blefes bem-sucedidos | **sem veredito aqui**: o equilíbrio é misto, então o veredito sai do Experimento 5b, com a mesa sorteada da mistura |

**O equilíbrio do blefe é misto** (dinâmica do replicador corrigida):

| Perfil | 4 jogadores | 5 jogadores |
|---|---|---|
| Nunca blefa, contesta pelo limiar | 50,1% | 54,1% |
| Nunca blefa, nunca contesta | 32,5% | 31,3% |
| Sempre blefa, nunca contesta | 13,3% | 13,3% |
| Sempre blefa, contesta pelo limiar | 4,1% | 1,3% |

**Blefes nas populações puras** (só descrição): quem nunca contesta deixa passar cerca de 81% dos blefes; quem sempre contesta, nenhum; e quem contesta pelo limiar deixa passar só 1,6% (4 jogadores) a 2,7% (5 jogadores).

### Observações (cuidado ao ler)

1. **O blefe está equilibrado no sentido de jogo:** nenhum perfil puro domina, e os perfis formam um ciclo. Blefar sempre ganha de quem nunca contesta; contestar pelo limiar ganha de quem blefa; não contestar ganha numa mesa de honestos. No equilíbrio, cerca de 1 em cada 6 jogadores blefa sempre. É o comportamento que a regra de contestação (R-7.3.5) pretendia criar.
2. **Contestar pelo limiar pega quase todo blefe** (só 1,6% a 2,7% passam). Os bots contam as cartas já vistas (MOD-09) e sabem quando um teste nomeado está esgotado. Jogadores humanos não contam tão bem: a taxa real de blefes que passam deve ficar entre esse número e os 81% de quem nunca contesta. O veredito do REQ-05 vale para bots que contam cartas.
3. **"Contestar pelo limiar" é o perfil mais comum no equilíbrio**, e o mesmo de todos os experimentos anteriores. Por isso aqueles resultados não estão longe do comportamento de equilíbrio. O blefe "metade das vezes" usado antes, porém, não aparece no equilíbrio: quem blefa, blefa sempre.

### Resultado do Experimento 5b (`fase4_exp5b_blefe_equilibrio`)

Execução oficial no commit `e17bbf2`, árvore limpa: 20.000 partidas em 318 s com 4 processos, nenhuma falha. Relatório em `resultados/fase4_exp5b_blefe_equilibrio/20261111-004253-e17bbf2/relatorio.md`.

| Requisito | Resultado |
|---|---|
| REQ-05, blefes bem-sucedidos no equilíbrio | **passa**: 0,395 (0,386 a 0,403) com 4 jogadores e 0,385 (0,377 a 0,393) com 5, em 21.532 e 23.535 blefes. Zona: 0,30 a 0,50 |

**Observações**

1. **Os números do PDF batem com o equilíbrio:** com a contestação de R-7.3.4 e R-7.3.5, a mistura estável de comportamentos faz cerca de 39% dos blefes darem certo, no meio da faixa de 30% a 50% que o PDF pede para o playtest.
2. **Na mesa de equilíbrio, os perfis vencem perto de 1/N**, como se espera de um equilíbrio. Quem sempre blefa fica um pouco abaixo (0,234 com 4 jogadores, intervalo de 0,223 a 0,246), porque a dinâmica usa uma aproximação linear.
3. **A duração depende muito de como a mesa contesta.** Na mesa de equilíbrio há 3,3 contestações por partida com 4 jogadores, contra cerca de 9,5 com o blefe moderado. As medianas caem para 38,7 min (4 jogadores) e 44,6 min (5), contra 45,7 e 55,1 nos Experimentos 2 e 3. É só descrição (o REQ-08 não foi medido aqui), mas a duração com 5 jogadores, que estourava os 50 min, fica dentro da faixa com o comportamento de equilíbrio.

### Resultado do Experimento 6 (`fase4_exp6_variantes`)

Execução oficial no commit `cf01dd6`, árvore limpa: 80.000 partidas em 1.350 s com 4 processos, nenhuma falha (REQ-09 passa). Relatório em `resultados/fase4_exp6_variantes/20261111-004839-cf01dd6/relatorio.md`. Mesas de Heurísticos sorteadas da mistura do equilíbrio do blefe.

Valor e veredito de cada requisito por cenário (✓ passa, ✗ falha, ? inconclusivo). REQ-06a: razão máximo/média de testes recebidos (até 1,5). REQ-06b: fração dos testes contra o menor placar (até 0,43 com 4 jogadores e 0,35 com 5). REQ-07: partidas com alguém em 0 ficha antes do ciclo 3 (até 0,10). REQ-08: mediana da duração em minutos (40 a 50). REQ-10: percentil 90 do tempo parado por jogador e ciclo, em minutos (até 5). REQ-11: sistema cheio ao fim do 1º Planejamento (0,10 a 0,90). REQ-12: vantagem de quem começa cobrindo a chave do incidente 1 (até ±0,10). REQ-13: dano de incidente sobre fichas movimentadas (0,20 a 0,60).

| Cenário | REQ-06a | REQ-06b | REQ-07 | REQ-08 | REQ-10 | REQ-11 | REQ-12 | REQ-13 |
|---|---|---|---|---|---|---|---|---|
| n4_iniciante_base | 1,36✓ | 0,42✓ | 0,07✓ | 38,4✗ | 5,8✗ | 0,58✓ | 0,07✓ | 0,22✓ |
| n4_iniciante_var01_2_fichas | 1,36✓ | 0,41✓ | 0,09? | 38,4✗ | 5,8✗ | 0,58✓ | 0,06✓ | 0,21✓ |
| n4_iniciante_var01_sem_punicao | 1,36✓ | 0,42✓ | 0,07✓ | 38,4✗ | 5,8✗ | 0,58✓ | 0,06✓ | 0,22✓ |
| n4_iniciante_var02_custo_extra | 1,36✓ | 0,40✓ | 0,19✗ | 38,4✗ | 5,8✗ | 0,58✓ | 0,06✓ | 0,20✗ |
| n4_iniciante_var03_auditor_externo | 1,35✓ | 0,42✓ | 0,06✓ | 38,5✗ | 7,3✗ | 0,58✓ | 0,07✓ | 0,22✓ |
| n4_iniciante_var04_vizinho | 1,49? | 0,43? | 0,08✓ | 34,6✗ | 5,0✓ | 0,58✓ | 0,06✓ | 0,22✓ |
| n4_iniciante_var05_limite_2 | 1,16✓ | 0,44? | 0,08✓ | 34,0✗ | 4,7✓ | 0,58✓ | 0,08✓ | 0,22✓ |
| n4_iniciante_var06_palpite | 1,36✓ | 0,42✓ | 0,07✓ | 38,4✗ | 5,8✗ | 0,58✓ | 0,06✓ | 0,21✓ |
| n4_iniciante_var07_2_compras | 1,54✗ | 0,44? | 0,10? | 30,3✗ | 4,1✓ | 0,00✗ | 0,09? | 0,24✓ |
| n4_iniciante_var09_modulo | 1,36✓ | 0,42✓ | 0,07✓ | 37,6✗ | 5,7✗ | 0,55✓ | 0,08? | 0,24✓ |
| n4_experiente_base | 1,38✓ | 0,42✓ | 0,03✓ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_var01_2_fichas | 1,38✓ | 0,42✓ | 0,06✓ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_var01_sem_punicao | 1,38✓ | 0,42✓ | 0,03✓ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,18✗ |
| n4_experiente_var02_custo_extra | 1,38✓ | 0,41✓ | 0,05✓ | 38,7✗ | 5,8✗ | 0,51✓ | 0,02✓ | 0,17✗ |
| n4_experiente_var03_auditor_externo | 1,37✓ | 0,42✓ | 0,04✓ | 38,7✗ | 7,4✗ | 0,51✓ | 0,05✓ | 0,17✗ |
| n4_experiente_var04_vizinho | 1,49? | 0,43? | 0,03✓ | 34,9✗ | 5,0? | 0,51✓ | 0,04✓ | 0,18✗ |
| n4_experiente_var05_limite_2 | 1,17✓ | 0,45✗ | 0,03✓ | 34,3✗ | 4,7✓ | 0,51✓ | 0,03✓ | 0,18✗ |
| n4_experiente_var06_palpite | 1,38✓ | 0,42✓ | 0,03✓ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_var07_2_compras | 1,56✗ | 0,44? | 0,04✓ | 30,4✗ | 4,0✓ | 0,00✗ | 0,07✓ | 0,18✗ |
| n4_experiente_var09_modulo | 1,37✓ | 0,43✓ | 0,05✓ | 37,7✗ | 5,6✗ | 0,49✓ | 0,05✓ | 0,19✗ |
| n5_iniciante_base | 1,40✓ | 0,34✓ | 0,07✓ | 44,2✓ | 9,0✗ | 0,57✓ | 0,06✓ | 0,22✓ |
| n5_iniciante_var01_2_fichas | 1,40✓ | 0,34✓ | 0,09? | 44,2✓ | 9,0✗ | 0,57✓ | 0,06✓ | 0,21✓ |
| n5_iniciante_var01_sem_punicao | 1,40✓ | 0,34✓ | 0,06✓ | 44,2✓ | 9,0✗ | 0,57✓ | 0,06✓ | 0,22✓ |
| n5_iniciante_var02_custo_extra | 1,40✓ | 0,33✓ | 0,21✗ | 44,2✓ | 9,0✗ | 0,57✓ | 0,06✓ | 0,20✗ |
| n5_iniciante_var03_auditor_externo | 1,40✓ | 0,34✓ | 0,08✓ | 44,4✓ | 10,2✗ | 0,57✓ | 0,05✓ | 0,22✓ |
| n5_iniciante_var04_vizinho | 1,55✗ | 0,35? | 0,09? | 39,0✗ | 7,7✗ | 0,57✓ | 0,07✓ | 0,23✓ |
| n5_iniciante_var05_limite_2 | 1,17✓ | 0,36✗ | 0,09✓ | 38,9✗ | 7,0✗ | 0,57✓ | 0,08✓ | 0,22✓ |
| n5_iniciante_var06_palpite | 1,40✓ | 0,34✓ | 0,06✓ | 44,2✓ | 9,0✗ | 0,57✓ | 0,06✓ | 0,21✓ |
| n5_iniciante_var07_2_compras | 1,61✗ | 0,36✗ | 0,12✗ | 34,2✗ | 6,3✗ | 0,00✗ | 0,08✓ | 0,24✓ |
| n5_iniciante_var09_modulo | 1,40✓ | 0,34✓ | 0,09? | 43,3✓ | 8,8✗ | 0,55✓ | 0,08✓ | 0,23✓ |
| n5_experiente_base | 1,42✓ | 0,35? | 0,06✓ | 44,6✓ | 9,2✗ | 0,50✓ | 0,04✓ | 0,17✗ |
| n5_experiente_var01_2_fichas | 1,42✓ | 0,34✓ | 0,08✓ | 44,6✓ | 9,2✗ | 0,50✓ | 0,03✓ | 0,17✗ |
| n5_experiente_var01_sem_punicao | 1,42✓ | 0,35? | 0,05✓ | 44,5✓ | 9,2✗ | 0,50✓ | 0,04✓ | 0,18✗ |
| n5_experiente_var02_custo_extra | 1,42✓ | 0,34✓ | 0,09? | 44,6✓ | 9,2✗ | 0,50✓ | 0,03✓ | 0,17✗ |
| n5_experiente_var03_auditor_externo | 1,42✓ | 0,34✓ | 0,06✓ | 44,6✓ | 10,2✗ | 0,50✓ | 0,03✓ | 0,17✗ |
| n5_experiente_var04_vizinho | 1,55✗ | 0,35? | 0,05✓ | 39,5✗ | 7,9✗ | 0,50✓ | 0,05✓ | 0,18✗ |
| n5_experiente_var05_limite_2 | 1,20✓ | 0,36✗ | 0,05✓ | 39,3✗ | 7,2✗ | 0,50✓ | 0,04✓ | 0,18✗ |
| n5_experiente_var06_palpite | 1,42✓ | 0,34✓ | 0,05✓ | 44,6✓ | 9,2✗ | 0,50✓ | 0,04✓ | 0,17✗ |
| n5_experiente_var07_2_compras | 1,64✗ | 0,36✗ | 0,04✓ | 34,2✗ | 6,2✗ | 0,00✗ | 0,06✓ | 0,19✗ |
| n5_experiente_var09_modulo | 1,43✓ | 0,35✓ | 0,05✓ | 43,5✓ | 8,8✗ | 0,48✓ | 0,06✓ | 0,19✗ |

### Observações (cuidado ao ler)

1. **A v2.2.1, com o comportamento de equilíbrio, passa em REQ-06, REQ-07, REQ-11 e REQ-12** com 4 e com 5 jogadores, para iniciantes e experientes.
2. **Tempo parado (REQ-10) é o problema maior:** o percentil 90 fica em 5,8 min por ciclo com 4 jogadores e em 9 min com 5. Com 5 jogadores, nenhuma variante o traz para menos de 5 min. Os tempos do MOD-05 são provisórios, mas a diferença entre 4 e 5 jogadores vem da estrutura: mais disputas em que cada um não está.
3. **A duração (REQ-08) falha com 4 jogadores por ser curta demais** (38,4 a 38,7 min). Com 5 jogadores passa (44 min). O comportamento de equilíbrio contesta pouco (2 a 4 contestações por partida, contra cerca de 9,5 com o blefe moderado), e a partida encurta.
4. **O peso dos incidentes (REQ-13) depende do conhecimento:** passa com iniciantes (0,21 a 0,24) e falha com experientes (0,17 a 0,19). Quem sabe o conteúdo diagnostica e se cobre melhor, e o incidente pesa menos.
5. **O que cada variante faz:**
   - VAR-01 (punição de 0 ou 2 fichas) e VAR-06 (palpite) quase não mudam nada que o simulador mede. O palpite existe para engajar quem está parado, e isso um bot não mede; pela definição do REQ-10, quem vota continua contando como parado.
   - VAR-02 (custo extra da explicação) derruba o REQ-07 para iniciantes (19% a 21% das partidas com alguém em 0 ficha), porque iniciantes erram muitas explicações.
   - VAR-03 (Auditor externo) piora o tempo parado (7,3 min com 4 jogadores), porque ninguém da mesa fica ocupado como Auditor.
   - VAR-04 (vizinho designado) e VAR-05 (limite de 2 testes) encurtam a partida e o tempo parado, mas deixam a duração abaixo de 40 min. O VAR-04 concentra os testes (REQ-06a até 1,55); o VAR-05 os espalha, mas aumenta a fração contra o menor placar (REQ-06b falha com 5 jogadores).
   - VAR-07 (2 compras) torna o REQ-11 impossível: com 2 cartas iniciais e 2 compras, ninguém chega a 5 cartas no ciclo 1. A partida também fica curta demais (30 a 34 min).
   - VAR-09 (módulo) quase não muda os números.
6. **Resumo para o texto:** nenhuma variante melhora tudo. A regra atual é a melhor das 10 configurações no conjunto. O ponto fraco que sobra é o tempo parado com 5 jogadores, e a variante desenhada para ele (o palpite) não pode ser avaliada por bots.

---

## 2026-11-11 — Fase 4, Experimentos 3 (ablação) e 4 (sensibilidade)

### Decisões do autor

| Assunto | Opções | Escolha |
|---|---|---|
| Ablação: o que desfazer | correções COR-01 e COR-02; bug duplicado; 1 teste por ciclo; diagnóstico da 2.1 | **As correções, o bug duplicado e 1 teste por ciclo.** Hotfix, troca com sistema cheio, limite de mão, Monitorar e teste-chave único pedem mais código e ficam para depois, se for o caso |
| Sensibilidade: o que variar | fichas iniciais; dano de incidente; tempos do modelo de duração; pagamentos da contestação | **Fichas iniciais (3 a 7), dano de incidente (sem cobertura de 1 a 3; Alerta de 0 a 2) e tempos do MOD-05 (−25% e +25%).** Os pagamentos da contestação ficaram de fora: cada valor pediria um torneio de blefe novo |
| REQ-10 com o palpite da plateia | manter a definição; votar conta como ocupado | **Manter a definição:** quem vota continua parado no simulador; o efeito do palpite no engajamento fica para o playtest |

### O que foi feito

1. **Ablações no motor**, atrás do bloco opcional `ablacoes` (sem ele, vale a regra da versão, e o hash não muda): VAR-10, bug duplicado permitido, e VAR-11, testes por ciclo. Com o bug duplicado permitido, o teste numa categoria que já tem Alerta não põe um cubo novo, porque um jogador nunca tem dois Alertas da mesma categoria.
2. **Modelo de duração por cenário** (`duracao` no cenário), registrado no manifest com o hash. Dois modelos novos, `configs/duracao_menos_25.yaml` e `configs/duracao_mais_25.yaml`, com todos os tempos multiplicados por 0,75 e 1,25.
3. **Especificação:** VAR-10 e VAR-11 na tabela de variantes, citadas em R-7.4.1 e R-7.4.2.
4. **Experimentos** `fase4_exp3_ablacao` (18 cenários, 36.000 partidas) e `fase4_exp4_sensibilidade` (44 cenários, 88.000 partidas).
5. **Testes novos:** 4. Cobrem o bug duplicado, o limite de testes, os tempos por cenário (o jogo não muda, só a medida) e os arquivos dos experimentos.

### Verificação

- `uv run pytest`: 434 testes passam e 1 é pulado. `ruff` e `mypy` estrito sem apontamentos. Matriz 176 de 176; registros de referência sem mudança.

### Detalhes escolhidos pelo assistente, sem perguntar

- **Desenho dos dois experimentos:** igual ao do Experimento 6. Mesas de Heurísticos sorteadas da mistura do equilíbrio do blefe, conhecimento iniciante e experiente, mesas de 4 e de 5, 2.000 partidas por cenário e os mesmos requisitos.
- **COR-02 desfeita:** `alertas.limpeza_no_planejamento: false` sobre a v2.2.1. **COR-01 desfeita:** `jogadores.maximo: 6`, com mesas de 6. Não há torneio de blefe com 6 jogadores, então essas mesas usam a mistura de 5.
- **Tempos:** arredondados para o segundo mais próximo, com meio segundo para cima (por exemplo, 37,5 s vira 38 s).
- **Sementes mestre:** 20261118 (ablação) e 20261119 (sensibilidade); 4 processos.

### Resultado do Experimento 3 (`fase4_exp3_ablacao`)

Execução oficial no commit `f925943`, árvore limpa: 36.000 partidas em 592 s com 4 processos, nenhuma falha. O REQ-09 saiu inconclusivo só porque o experimento tem menos de 50.000 partidas. Relatório em `resultados/fase4_exp3_ablacao/20261111-080955-f925943/relatorio.md`. Mesma legenda da tabela do Experimento 6.

| Cenário | REQ-06a | REQ-06b | REQ-07 | REQ-08 | REQ-10 | REQ-11 | REQ-12 | REQ-13 |
|---|---|---|---|---|---|---|---|---|
| n4_iniciante_base | 1,36✓ | 0,42✓ | 0,06✓ | 38,3✗ | 5,8✗ | 0,57✓ | 0,07✓ | 0,21✓ |
| n4_iniciante_sem_cor02 | 1,33✓ | 0,42✓ | 0,07✓ | 37,9✗ | 5,8✗ | 0,57✓ | 0,08? | 0,25✓ |
| n4_iniciante_var10_bug_duplicado | 1,44✓ | 0,42✓ | 0,06✓ | 38,2✗ | 5,8✗ | 0,57✓ | 0,08? | 0,20✓ |
| n4_iniciante_var11_1_teste | 1,67✗ | 0,47✗ | 0,08✓ | 28,2✗ | 3,3✓ | 0,57✓ | 0,08? | 0,23✓ |
| n4_experiente_base | 1,38✓ | 0,42✓ | 0,05✓ | 38,8✗ | 5,8✗ | 0,51✓ | 0,06✓ | 0,17✗ |
| n4_experiente_sem_cor02 | 1,35✓ | 0,42✓ | 0,05✓ | 38,8✗ | 5,9✗ | 0,51✓ | 0,05✓ | 0,19✗ |
| n4_experiente_var10_bug_duplicado | 1,43✓ | 0,43✓ | 0,04✓ | 38,3✗ | 5,8✗ | 0,51✓ | 0,05✓ | 0,16✗ |
| n4_experiente_var11_1_teste | 1,65✗ | 0,47✗ | 0,04✓ | 28,5✗ | 3,3✓ | 0,51✓ | 0,06✓ | 0,18✗ |
| n5_iniciante_base | 1,40✓ | 0,34✓ | 0,07✓ | 44,5✓ | 9,2✗ | 0,57✓ | 0,05✓ | 0,21✓ |
| n5_iniciante_sem_cor02 | 1,36✓ | 0,34✓ | 0,08✓ | 44,2✓ | 9,0✗ | 0,57✓ | 0,05✓ | 0,25✓ |
| n5_iniciante_var10_bug_duplicado | 1,50? | 0,34✓ | 0,06✓ | 43,7✓ | 9,0✗ | 0,57✓ | 0,08✓ | 0,20✓ |
| n5_iniciante_var11_1_teste | 1,76✗ | 0,40✗ | 0,10? | 31,6✗ | 4,9✓ | 0,57✓ | 0,08✓ | 0,23✓ |
| n5_experiente_base | 1,43✓ | 0,34✓ | 0,05✓ | 44,7✓ | 9,2✗ | 0,51✓ | 0,04✓ | 0,17✗ |
| n5_experiente_sem_cor02 | 1,41✓ | 0,35? | 0,05✓ | 45,1✓ | 9,4✗ | 0,51✓ | 0,06✓ | 0,19✗ |
| n5_experiente_var10_bug_duplicado | 1,52✗ | 0,35? | 0,04✓ | 43,7✓ | 8,9✗ | 0,51✓ | 0,05✓ | 0,16✗ |
| n5_experiente_var11_1_teste | 1,77✗ | 0,39✗ | 0,04✓ | 31,8✗ | 4,9✓ | 0,51✓ | 0,07✓ | 0,18✗ |
| n6_iniciante_sem_cor01 | 1,44✓ | 0,29✓ | 0,08✓ | 50,8✗ | 12,2✗ | 0,57✓ | 0,06✓ | 0,21✓ |
| n6_experiente_sem_cor01 | 1,46✓ | 0,29✓ | 0,06✓ | 51,0✗ | 12,3✗ | 0,51✓ | 0,05✓ | 0,17✗ |

### Observações (cuidado ao ler)

1. **COR-01 (máximo de 5 jogadores) se confirma.** Com 6 jogadores, a mediana da duração passa de 50 min (50,8 a 51,0) e o tempo parado chega a 12 min por ciclo. Todas as partidas reembaralham o descarte, e em 0,1% delas faltou carta para comprar.
2. **COR-02 (Alertas saem no Planejamento) muda pouco os requisitos.** Sem ela, o Alerta fica mais tempo, o dano de incidente pesa um pouco mais (REQ-13 de 0,21 para 0,25 com iniciantes) e o placar médio cai de 7,3 para 5,7 fichas. Nenhum veredito muda de lado por causa dela.
3. **O bug duplicado da 2.2 espalha os ataques, como o PDF diz.** Com a regra da 2.1 (permitido), a razão máximo/média de testes recebidos sobe (de 1,36 a 1,43 para 1,43 a 1,52) e o REQ-06a falha com 5 jogadores experientes.
4. **"Sem limite de testes" (2.2) contra "1 teste por ciclo" (2.1):** o limite da 2.1 resolve o tempo parado (REQ-10 passa: 3,3 e 4,9 min), mas encurta a partida para 28 a 32 min e concentra os testes no menor placar (REQ-06 falha). Na 2.2, testar mais tem custo em tempo, e o teste por ciclo não é a saída: a partida fica curta demais.
5. **Resumo:** cada mudança da v2.2 desfeita piora algum requisito, ou não melhora nenhum. O ponto fraco que sobra, o tempo parado, vem justamente do teste sem limite, que dá valor às cartas guardadas.

### Resultado do Experimento 4 (`fase4_exp4_sensibilidade`)

Execução oficial no commit `73762b5`, árvore limpa: 88.000 partidas em 1.421 s com 4 processos, nenhuma falha (REQ-09 passa). Relatório em `resultados/fase4_exp4_sensibilidade/20261111-082054-73762b5/relatorio.md`. Mesma legenda da tabela do Experimento 6.

| Cenário | REQ-06a | REQ-06b | REQ-07 | REQ-08 | REQ-10 | REQ-11 | REQ-12 | REQ-13 |
|---|---|---|---|---|---|---|---|---|
| n4_iniciante_base | 1,35✓ | 0,42✓ | 0,06✓ | 38,4✗ | 5,8✗ | 0,59✓ | 0,08✓ | 0,22✓ |
| n4_iniciante_dano_alerta_0 | 1,35✓ | 0,42✓ | 0,03✓ | 38,4✗ | 5,8✗ | 0,60✓ | 0,08? | 0,19✗ |
| n4_iniciante_dano_alerta_2 | 1,36✓ | 0,42✓ | 0,13✗ | 38,4✗ | 5,8✗ | 0,57✓ | 0,08✓ | 0,24✓ |
| n4_iniciante_dano_sem_cobertura_1 | 1,37✓ | 0,44✗ | 0,01✓ | 38,2✗ | 5,8✗ | 0,52✓ | 0,04✓ | 0,16✗ |
| n4_iniciante_dano_sem_cobertura_3 | 1,36✓ | 0,41✓ | 0,27✗ | 38,6✗ | 5,8✗ | 0,62✓ | 0,10? | 0,27✓ |
| n4_iniciante_fichas_3 | 1,35✓ | 0,42✓ | 0,46✗ | 38,4✗ | 5,8✗ | 0,59✓ | 0,08✓ | 0,22✓ |
| n4_iniciante_fichas_4 | 1,35✓ | 0,42✓ | 0,17✗ | 38,4✗ | 5,8✗ | 0,59✓ | 0,08✓ | 0,22✓ |
| n4_iniciante_fichas_6 | 1,35✓ | 0,42✓ | 0,02✓ | 38,4✗ | 5,8✗ | 0,59✓ | 0,08✓ | 0,22✓ |
| n4_iniciante_fichas_7 | 1,35✓ | 0,42✓ | 0,00✓ | 38,4✗ | 5,8✗ | 0,59✓ | 0,08? | 0,21✓ |
| n4_iniciante_tempos_mais_25 | 1,35✓ | 0,42✓ | 0,06✓ | 48,1✓ | 7,2✗ | 0,59✓ | 0,08✓ | 0,22✓ |
| n4_iniciante_tempos_menos_25 | 1,35✓ | 0,42✓ | 0,06✓ | 28,9✗ | 4,3✓ | 0,59✓ | 0,08? | 0,22✓ |
| n4_experiente_base | 1,38✓ | 0,42✓ | 0,04✓ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_dano_alerta_0 | 1,38✓ | 0,42✓ | 0,02✓ | 38,7✗ | 5,8✗ | 0,53✓ | 0,03✓ | 0,15✗ |
| n4_experiente_dano_alerta_2 | 1,38✓ | 0,42✓ | 0,10? | 38,7✗ | 5,8✗ | 0,49✓ | 0,03✓ | 0,19✗ |
| n4_experiente_dano_sem_cobertura_1 | 1,36✓ | 0,44? | 0,01✓ | 38,6✗ | 5,8✗ | 0,50✓ | 0,04✓ | 0,12✗ |
| n4_experiente_dano_sem_cobertura_3 | 1,37✓ | 0,42✓ | 0,19✗ | 38,8✗ | 5,8✗ | 0,52✓ | 0,06✓ | 0,22✓ |
| n4_experiente_fichas_3 | 1,38✓ | 0,42✓ | 0,34✗ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_fichas_4 | 1,38✓ | 0,42✓ | 0,13✗ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_fichas_6 | 1,38✓ | 0,42✓ | 0,01✓ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_fichas_7 | 1,38✓ | 0,42✓ | 0,00✓ | 38,7✗ | 5,8✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_tempos_mais_25 | 1,38✓ | 0,42✓ | 0,04✓ | 48,4✓ | 7,2✗ | 0,51✓ | 0,03✓ | 0,17✗ |
| n4_experiente_tempos_menos_25 | 1,38✓ | 0,42✓ | 0,04✓ | 29,1✗ | 4,3✓ | 0,51✓ | 0,03✓ | 0,17✗ |
| n5_iniciante_base | 1,41✓ | 0,34✓ | 0,08✓ | 44,2✓ | 9,0✗ | 0,58✓ | 0,07✓ | 0,21✓ |
| n5_iniciante_dano_alerta_0 | 1,40✓ | 0,34✓ | 0,04✓ | 44,3✓ | 9,2✗ | 0,60✓ | 0,07✓ | 0,18✗ |
| n5_iniciante_dano_alerta_2 | 1,40✓ | 0,33✓ | 0,17✗ | 44,3✓ | 9,0✗ | 0,57✓ | 0,07✓ | 0,24✓ |
| n5_iniciante_dano_sem_cobertura_1 | 1,40✓ | 0,36✗ | 0,01✓ | 44,1✓ | 8,9✗ | 0,52✓ | 0,04✓ | 0,16✗ |
| n5_iniciante_dano_sem_cobertura_3 | 1,41✓ | 0,33✓ | 0,32✗ | 44,5✓ | 9,2✗ | 0,62✓ | 0,09? | 0,26✓ |
| n5_iniciante_fichas_3 | 1,41✓ | 0,34✓ | 0,52✗ | 44,2✓ | 9,0✗ | 0,58✓ | 0,07✓ | 0,21✓ |
| n5_iniciante_fichas_4 | 1,41✓ | 0,34✓ | 0,23✗ | 44,2✓ | 9,0✗ | 0,58✓ | 0,07✓ | 0,21✓ |
| n5_iniciante_fichas_6 | 1,41✓ | 0,34✓ | 0,02✓ | 44,2✓ | 9,0✗ | 0,58✓ | 0,07✓ | 0,21✓ |
| n5_iniciante_fichas_7 | 1,41✓ | 0,34✓ | 0,01✓ | 44,2✓ | 9,0✗ | 0,58✓ | 0,07✓ | 0,21✓ |
| n5_iniciante_tempos_mais_25 | 1,41✓ | 0,34✓ | 0,08✓ | 55,4✗ | 11,3✗ | 0,58✓ | 0,07✓ | 0,21✓ |
| n5_iniciante_tempos_menos_25 | 1,41✓ | 0,34✓ | 0,08✓ | 33,4✗ | 6,8✗ | 0,58✓ | 0,07✓ | 0,21✓ |
| n5_experiente_base | 1,43✓ | 0,35✓ | 0,05✓ | 44,5✓ | 9,2✗ | 0,52✓ | 0,07✓ | 0,17✗ |
| n5_experiente_dano_alerta_0 | 1,43✓ | 0,34✓ | 0,03✓ | 44,5✓ | 9,2✗ | 0,53✓ | 0,07✓ | 0,15✗ |
| n5_experiente_dano_alerta_2 | 1,43✓ | 0,34✓ | 0,13✗ | 44,5✓ | 9,1✗ | 0,51✓ | 0,07✓ | 0,20✗ |
| n5_experiente_dano_sem_cobertura_1 | 1,43✓ | 0,36✗ | 0,01✓ | 44,4✓ | 9,0✗ | 0,50✓ | 0,04✓ | 0,12✗ |
| n5_experiente_dano_sem_cobertura_3 | 1,42✓ | 0,33✓ | 0,24✗ | 44,6✓ | 9,2✗ | 0,53✓ | 0,07✓ | 0,22✓ |
| n5_experiente_fichas_3 | 1,43✓ | 0,35? | 0,40✗ | 44,5✓ | 9,2✗ | 0,52✓ | 0,07✓ | 0,17✗ |
| n5_experiente_fichas_4 | 1,43✓ | 0,35✓ | 0,15✗ | 44,5✓ | 9,2✗ | 0,52✓ | 0,07✓ | 0,17✗ |
| n5_experiente_fichas_6 | 1,43✓ | 0,35✓ | 0,02✓ | 44,5✓ | 9,2✗ | 0,52✓ | 0,07✓ | 0,17✗ |
| n5_experiente_fichas_7 | 1,43✓ | 0,35✓ | 0,00✓ | 44,5✓ | 9,2✗ | 0,52✓ | 0,07✓ | 0,17✗ |
| n5_experiente_tempos_mais_25 | 1,43✓ | 0,35✓ | 0,05✓ | 55,7✗ | 11,5✗ | 0,52✓ | 0,07✓ | 0,17✗ |
| n5_experiente_tempos_menos_25 | 1,43✓ | 0,35? | 0,05✓ | 33,5✗ | 6,9✗ | 0,52✓ | 0,07✓ | 0,17✗ |

### Observações (cuidado ao ler)

1. **Fichas iniciais: 5 é o mínimo que passa no REQ-07.** Com 3 fichas, 34% a 52% das partidas têm alguém em 0 ficha antes do ciclo 3; com 4, de 13% a 23% (falha); com 5, de 4% a 8% (passa); com 6, de 1% a 2%; com 7, quase nenhuma. As outras medidas não mudam: os bots não decidem pelo número de fichas, então o valor só muda o piso. O PDF acertou o mínimo; 6 daria folga.
2. **O REQ-07 e o REQ-13 puxam para lados opostos.** Com experientes, o peso dos incidentes só passa de 0,20 com o dano sem cobertura em 3 (0,22), e aí o REQ-07 falha (19% a 32% das partidas com alguém zerado). Mais dano por Alerta (2) também ajuda o REQ-13 e derruba o REQ-07 com iniciantes. Dano menor (sem cobertura 1 ou Alerta 0) faz o REQ-13 falhar também com iniciantes. Uma combinação, por exemplo dano 3 com 6 fichas iniciais, pode satisfazer os dois. Isso é uma interação, que não foi medida aqui.
3. **Duração e tempo parado dependem dos tempos provisórios.** Com todos os tempos +25%, a mesa de 4 passa a durar 48 min (REQ-08 passa) e a de 5 estoura (55 min). Com −25%, as duas ficam curtas demais (29 e 33 min), e o tempo parado passa com 4 jogadores (4,3 min). O REQ-08 e o REQ-10 só podem ser julgados de verdade com os tempos cronometrados no playtest. O que não depende dos tempos é a relação entre 4 e 5 jogadores: a de 5 dura cerca de 15% mais e fica cerca de 55% mais tempo parada.

## Fase 4 — resumo

**Melhor estilo (MET-07, REQ-03, REQ-04, REQ-11):** o Heurístico é o melhor estilo e o equilíbrio da dinâmica do replicador; o Construtor vem logo atrás. Construir vence caçar na v2.2.1, e nenhum Caçador é melhor resposta a mesa nenhuma, a não ser a de Aleatórios. Mesmo assim, os dois estilos aparecem dentro das decisões do Heurístico (REQ-11 passa). Entre os Caçadores, atacar o líder é o melhor, o contrário da v1.

**Blefe (REQ-04, REQ-05):** nenhum perfil puro domina. O equilíbrio é misto, com cerca de 1 em cada 6 jogadores blefando sempre, e nele cerca de 39% dos blefes dão certo, no meio da faixa do PDF.

**O jogo está balanceado?** Com o comportamento de equilíbrio, a v2.2.1 passa na equidade de assento com bots aleatórios (REQ-01), na anti bola de neve (REQ-02), na habilidade (REQ-03), em nenhuma estratégia dominante (REQ-04), no blefe (REQ-05), na distribuição de ataques (REQ-06), nas fichas (REQ-07), na robustez (REQ-09), nos dois estilos (REQ-11) e no primeiro incidente (REQ-12). Os pontos fracos:
- o tempo parado (REQ-10), sobretudo com 5 jogadores;
- o peso dos incidentes para experientes (REQ-13);
- a duração com 4 jogadores, curta demais pelos tempos provisórios (REQ-08);
- a vantagem do primeiro jogador com bots que jogam bem, na borda da zona (REQ-01).

**Variantes, ablação e sensibilidade:** nenhuma variante do playtest melhora tudo, e as mudanças da v2.2 se justificam todas. Os números mais sensíveis são as fichas iniciais (5 é o mínimo) e o dano de incidente (em tensão com as fichas). Os tempos do MOD-05 decidem os vereditos de duração e de tempo parado.

### Pendências

- Do autor: decidir se haverá uma v2.3, por exemplo com a combinação de dano e fichas da observação 2, antes da Fase 5 ou depois do playtest.
- Do autor: a parte "acima de 60 minutos" do REQ-08; a redação dos trechos marcados em `regras/`.
- Para o playtest: cronometrar as ações (MOD-05) e registrar o tempo parado.

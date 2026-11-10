# Prompt para o Claude Code — Simulador do Critical Failure

Cole o texto abaixo como primeira mensagem no Claude Code, numa pasta de projeto vazia que já contenha a pasta `docs/` com os arquivos indicados.

---

Você vai construir o simulador de partidas do jogo de cartas **Critical Failure**, parte do meu TCC em Ciência da Computação (UFPB). O simulador é a etapa 2 de um ciclo de Design Science Research: regras v2 → simulador → testes com humanos, com os resultados voltando para ajustar as regras.

O simulador trata o jogo como um **sistema sob teste**. Os bots são os usuários virtuais, como num teste de carga. Milhares de partidas entre bots verificam requisitos de balanceamento com critério de aceite. Tudo o que o simulador produz vai para o texto do TCC. Por isso, **cada número precisa ser reproduzível e rastreável** até as regras, a configuração, a semente e a versão do código que o geraram.

## 1. Fontes, em ordem de autoridade

Estão em `docs/`:

1. `Critical_Failure_-_Regras_Completas_2.2.pdf`: **especificação da versão atual (v2.2)**. É a fonte da verdade para a v2. Inclui as tabelas de cartas (Apêndice B), os incidentes com gabarito (Apêndice C) e a seção "Parâmetros a validar no playtest", que define o que o simulador deve medir.
2. `Critical_Failure_Artigo.pdf`: artigo original (SBQS 2025). A **v1** está na seção 4.3 (regras) e na Tabela 3 (baralho). A seção 4.4 relata o problema que o simulador deve reproduzir: 4 de 6 partidas desequilibradas, com jogadores atacando o mais fraco.
3. `Briefing_Apresentacao_TCC.md`: use **somente** os slides 5 e 10 a 13 (plano, simulador, requisitos de balanceamento, técnicas de teste, registro em sala). Os slides 6 a 9 descrevem uma versão antiga das regras (2.0). Quando divergirem, o PDF 2.2 prevalece.

Não invente regras. Quando as fontes forem ambíguas ou omissas, siga a seção 6.

## 2. Requisito central: registro de auditoria

Toda partida pode gerar um registro de auditoria completo. Ele tem três funções:

- **Reprodução:** a partida pode ser refeita exatamente a partir do registro.
- **Rastreabilidade:** cada evento aponta para a regra que o justificou.
- **Explicação:** cada decisão de bot registra as opções disponíveis, a escolhida e o motivo.

### 2.1 Formato

Um arquivo JSONL por partida, com três tipos de registro.

**Cabeçalho (1ª linha):** versão do esquema (`cf-audit/1`), versão do motor, commit do git, versão das regras (`v1` ou `v2.2`), configuração completa já resolvida e o seu hash SHA-256, semente mestre, bots de cada assento com os seus parâmetros, e data e hora.

**Evento (uma linha por evento):**

```json
{"seq": 42, "ciclo": 1, "fase": "homologacao", "tipo": "defesa", "ator": 2,
 "regra": "R-7.2.2",
 "publico": {"atacante": 0, "categoria": "Desempenho", "teste_nomeado": "Estresse"},
 "oculto": {"tem_carta": false, "blefe": true},
 "decisao": {"opcoes": ["admitir", "defender:Carga", "defender:Estresse"],
             "escolha": "defender:Estresse",
             "motivo": "perfil blefe p=0.40; sorteio=0.12"},
 "estado_hash": "sha256:..."}
```

- `regra` é o identificador da regra na especificação gerada na Fase 0 (seção 5).
- A separação entre `publico` e `oculto` é obrigatória. Com ela é possível reconstruir, a partir do registro, exatamente o que cada jogador podia ver. Informação privada de um jogador (a própria mão, o próprio sistema) vai em `oculto` com o campo `visivel_para`.
- `estado_hash` é o hash do estado completo depois do evento. É ele que permite verificar a reprodução.
- Eventos aleatórios (embaralhar, comprar, rolar o dado) registram o resultado.

**Fim (última linha):** placar final com o detalhamento por fonte (Homologação, diagnóstico, dano, Critical Failure e pontuação final), vencedor, critério de desempate usado, resultado da checagem de invariantes e duração estimada (seção 3.5).

### 2.2 Ferramentas sobre o registro

- `cf replay <log>`: refaz a partida a partir do cabeçalho e confere o `estado_hash` de cada evento. Qualquer divergência é erro.
- `cf narrar <log>`: gera uma narração legível em português ("Ciclo 1, Homologação: Ana testa Bruno com Teste de Carga (Desempenho). Bruno defende com Estresse; o Auditor Carla diz 'confere'..."). Uso: conferir com a orientadora se o motor joga como as regras dizem.
- `cf folha <log>`: exporta um CSV com **os mesmos campos da Folha de registro usada em sala** (seção "Registro da partida" do PDF 2.2): diagnóstico de cada jogador por incidente (categoria-chave, secundária ou outra), cada defesa (categoria atacada, teste nomeado, se era blefe, decisão do Auditor, se houve contestação) e as fichas finais. Dados simulados e reais precisam ter o mesmo esquema para serem comparados.

### 2.3 Volume

Um milhão de partidas com registro completo não cabe em disco. Por isso:

- O resumo de cada partida (placar, vencedor, métricas) é sempre salvo, em Parquet.
- O registro completo é salvo para uma amostra configurável (por exemplo, 1 em 1000) e **sempre** para qualquer partida com exceção ou violação de invariante.
- Cada execução de experimento gera um `manifest.json` com o arquivo do experimento, os hashes das configurações, o número de partidas, a semente mestre, o commit e o comando exato. Todo gráfico e toda tabela do TCC devem poder ser refeitos a partir de um manifest.

## 3. O que construir

### 3.1 Motor de regras

- Python 3.12. Dependências leves: `numpy`, `pyyaml`, `pydantic` (validação de configuração), `pandas`/`pyarrow`, `pytest`, `hypothesis`, `mutmut`, `ruff` e `mypy`.
- **Determinístico:** a mesma configuração e a mesma semente geram um registro idêntico, byte a byte (exceto a data e hora do cabeçalho). Use `numpy.random.SeedSequence` para derivar as sementes de cada partida, de modo que o resultado não dependa do paralelismo.
- **Fluxos de aleatoriedade separados:** um para o jogo (baralhos, dado) e um para cada bot. Assim, trocar um bot não muda a ordem das cartas, e comparações entre variantes usam números aleatórios comuns (mesmas sementes, menos variância).
- **Motor puro:** `aplicar(estado, ação) → (novo_estado, eventos)`. O motor valida se a ação é legal. Bots nunca acessam nem alteram o estado.
- **Nenhum número de regra no código.** Todo valor (fichas iniciais, dano, teto do sistema, compras por Planejamento, recompensas da contestação etc.) vem do YAML, com o identificador da regra ao lado.
- Implementar **v2.2** primeiro, com o módulo opcional de Segurança Operacional, e depois a **v1**, como versões de regras separadas sobre um núcleo comum.
- Vocabulário do domínio em português, igual ao das regras (ficha, alerta, homologação, backlog, categoria-chave), para facilitar a rastreabilidade.

### 3.2 Variantes configuráveis

Além dos parâmetros da tabela "Parâmetros a validar no playtest" do PDF 2.2, o YAML deve permitir ligar e desligar estas variantes, todas já usadas ou propostas no playtest:

| Variante | Valores |
|---|---|
| Punição do blefe descoberto | sem punição / atual (1 ficha) / 2 fichas |
| Custo da explicação que não confere | igual a "Falhou" (atual) / custo extra |
| Auditor | jogador rotativo (atual) / externo, que não joga |
| Alvo na Homologação | livre (atual) / vizinho designado (v2.0) |
| Limite de testes recebidos por ciclo | sem limite (atual) / 2 |
| Voto da mesa | desligado / sobre a posse da carta (palpite da plateia) / sobre a explicação, antes do Auditor |
| Compras por Planejamento | 3 (atual) / 2 |
| Número de jogadores | 4, 5 e 6 |

### 3.3 Observação de cada bot

Cada bot recebe um objeto `Observacao` montado só com o que um jogador real veria: a própria mão e o próprio sistema; o Backlog; as frentes do Radar; as fichas e os Alertas de todos; cartas reveladas em contestações e na Produção; compras públicas no Backlog; e o histórico público de disputas. Um teste automático deve garantir que nenhuma informação de `oculto` chegue a um bot que não deveria vê-la.

### 3.4 Bots

Um bot é a combinação de três perfis independentes:

**Estratégia**
- *Aleatório:* escolhe uniformemente entre as ações legais.
- *Construtor:* enche o sistema cedo, priorizando as categorias que deduz do Radar, e testa pouco.
- *Caçador:* mantém o sistema pequeno e usa as cartas para testar. A política de alvo é um parâmetro: líder, mais fraco ou aleatório. É ela que verifica se o ataque ao mais fraco da v1 volta com o alvo livre.
- *Heurístico:* estima o valor de cada ação a partir da informação pública (dano esperado pelo Radar, chance de o alvo não ter a categoria, Alertas) e escolhe por softmax com temperatura, para não ser determinístico.

**Blefe:** probabilidade de blefar quando não tem a carta, e política de contestação (probabilidade fixa ou limiar sobre a chance estimada de blefe).

**Conhecimento (o aluno simulado):**
- Probabilidade de a explicação conferir, por teste ou por categoria.
- Matriz de confusão para o diagnóstico de cada incidente, que também determina o que o bot deduz do Radar.
- Precisão do Auditor ao julgar uma explicação.
- Perfis prontos "iniciante" e "experiente". Eles permitem testar a hipótese do playtest de que o jogo funciona melhor como revisão do que como primeira aprendizagem. Os valores são provisórios e serão calibrados depois com as Folhas de registro das partidas reais.

### 3.5 Modelo de duração

Estimar a duração de cada partida a partir de tempos por ação configuráveis (turno de Planejamento, disputa, defesa, Produção). Isso permite verificar o requisito de 40 a 50 minutos e o tempo parado por ciclo.

### 3.6 Métricas e requisitos

Os requisitos de balanceamento ficam em `configs/requisitos.yaml`, com critério de aceite e limites marcados como provisórios. Cada execução gera um relatório com o valor medido, o **intervalo de confiança** (Wilson para proporções, bootstrap para o resto) e o veredito (passa, falha ou inconclusivo):

| Requisito | Critério (a calibrar) |
|---|---|
| Equidade de assento | Vitória por posição perto de 1/N |
| Anti bola de neve | Líder após o ciclo 1 vence menos que na v1 |
| Habilidade importa | Heurístico vence bem acima de 1/N, sem ganhar sempre |
| Sem estratégia dominante | Nenhum perfil puro de blefe vence todos os outros |
| Blefe | Blefes bem-sucedidos entre 30% e 50% |
| Distribuição de ataques | Ninguém recebe muito mais testes que a média, sobretudo o último colocado |
| Fichas | Ninguém chega a 0 com frequência antes do ciclo 3 |
| Duração | Entre 40 e 50 minutos com 4 a 6 jogadores |
| Robustez | 1 milhão de partidas sem exceção nem violação de invariante |

Registre também as métricas da v1 que o artigo cita: a proporção de partidas desequilibradas (defina o critério de margem e coloque-o em configuração) e a taxa de vitória por política de alvo.

### 3.7 Experimentos

Cada experimento é um YAML em `experimentos/` e roda com `cf experimento <arquivo>`:

1. **Validação da v1:** o simulador reproduz o desequilíbrio relatado e mostra que atacar o mais fraco é a melhor política?
2. **v1 × v2.2** com os mesmos bots e as mesmas sementes.
3. **Ablação:** desligar uma mudança da v2.2 por vez.
4. **Sensibilidade:** varrer os parâmetros provisórios.
5. **Equilíbrio do blefe:** torneio entre perfis de blefe.
6. **Variantes do playtest:** as da seção 3.2, cruzadas com conhecimento iniciante e experiente.

## 4. Testes do próprio simulador

O TCC aplica teste não funcional ao jogo que ensina teste não funcional, e o simulador também é testado:

- **Unitários por regra:** cada identificador de regra da especificação tem pelo menos um teste, marcado com `@pytest.mark.regra("R-7.3")`. Um script gera a **matriz de rastreabilidade** regra → código → teste e aponta as regras sem teste.
- **Baseados em propriedades** (`hypothesis`), sobre partidas aleatórias: o total de cartas se conserva (63, ou 72 com o módulo); o sistema nunca passa de 5 cartas; as fichas nunca ficam negativas; no máximo 1 Alerta por categoria; só a categoria-chave pontua no diagnóstico; nenhum bot recebe informação oculta; replay e reexecução com a mesma semente geram registros idênticos.
- **Metamórficos:** permutar os nomes das categorias não muda as métricas, dentro de uma tolerância estatística; trocar a ordem dos assentos com bots idênticos não muda a taxa de vitória por bot.
- **Fuzzing:** sequências de ações aleatórias e configurações malformadas não podem quebrar o motor, só gerar erros controlados.
- **Mutação** (`mutmut`) sobre o motor, para medir a qualidade da suíte.
- **Integração contínua** (GitHub Actions): unitários e propriedades a cada push; a suíte de balanceamento, com N reduzido, toda noite.

## 5. Como trabalhar

Trabalhe em fases, com um commit por fase. **Pare ao fim das Fases 0 e 1 para eu revisar.**

**Fase 0: especificação.** Leia as fontes e produza:
- `docs/especificacao_v2_2.md` e `docs/especificacao_v1.md`: as regras reescritas como itens numerados e atômicos (`R-6.1`, `R-7.2.3`...), seguindo a numeração das seções do PDF, cada um com a referência de página.
- `docs/AMBIGUIDADES.md` (seção 6).
- `CLAUDE.md` com as convenções deste projeto: auditoria obrigatória, nenhum número de regra no código, determinismo e testes por regra.

**Fase 1:** núcleo do motor, v2.2, registro de auditoria, `replay`, `narrar`, `folha` e testes unitários e de propriedades. Mostre-me a narração de 2 partidas completas.

**Fase 2:** bots e perfis.

**Fase 3:** v1.

**Fase 4:** executor de experimentos, métricas, intervalos de confiança e relatórios (Markdown e gráficos).

**Fase 5:** testes metamórficos, fuzzing, mutação e CI.

## 6. Ambiguidades

Quando as regras forem ambíguas ou omissas, **não decida em silêncio**. Registre em `docs/AMBIGUIDADES.md`: a regra, o trecho, as interpretações possíveis, a escolhida como padrão e o motivo. Torne a escolha configurável sempre que for barato. Se a escolha puder mudar os resultados de balanceamento, pare e me pergunte.

Pontos que eu já sei que precisam de decisão:

- **Fichas mínimas em 0 e ordem na Produção:** o +1 do diagnóstico vem antes do dano. Com o mínimo 0, a ordem muda o resultado de quem tem poucas fichas.
- **Lição aprendida sem carta da categoria no Backlog:** a retirada simplesmente não acontece?
- **Fim da Homologação:** quem fica sem cartas na mão passa automaticamente?
- **Auditor envolvido na disputa:** a função passa ao jogador não envolvido mais próximo à esquerda, e isso precisa aparecer no registro.
- **v1, blefe aceito:** a regra do artigo é circular ("aplica-se o resultado conforme a veracidade da declaração", mas a carta não é revelada). No simulador, resolva pela verdade, já que o motor conhece o estado, e documente essa escolha.
- **v1, baralho:** use as quantidades por cor da Tabela 3 do artigo (Compatibilidade com 6 cartas), porque é o baralho que foi jogado. Os nomes de teste trocados na tabela não afetam a mecânica da v1, que só olha a cor.
- **v1, carta de falha encontrada:** a carta tirada do sistema do defensor é escolhida ao acaso.

## 7. Estrutura sugerida

```
src/critical_failure/
  nucleo/          # tipos, estado, cartas, RNG, hash de estado
  regras/v1/  regras/v2_2/
  auditoria/       # escrita, replay, narração, exportação da folha
  bots/            # estratégias, perfis de blefe e de conhecimento
  observacao.py
  metricas/  experimentos/  relatorios/
  cli.py           # cf jogar | replay | narrar | folha | experimento | relatorio
configs/           # regras_v1.yaml, regras_v2_2.yaml, requisitos.yaml, perfis/
experimentos/
tests/
docs/
resultados/        # fora do git, exceto os manifests
```

Comece pela Fase 0.

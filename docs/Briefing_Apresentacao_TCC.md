# Briefing para o Claude Design — Apresentação do TCC (Critical Failure 2.0)

Sep 23, 2026 · @Erik Freire Ramos

Este documento reúne tudo o que o Claude Design precisa para montar a apresentação para a orientadora: o prompt, o roteiro de 15 slides e a lista de arquivos de apoio. Exporte-o em PDF ou Markdown e envie junto com os outros arquivos ao criar o projeto.

## 1. Prompt para colar no Claude Design

Copie o texto abaixo como primeira mensagem do projeto, depois de anexar os arquivos da seção 5.

> Crie uma apresentação de 15 slides, em português, para uma reunião de orientação de TCC em Ciência da Computação (Centro de Informática, UFPB). A orientadora é a profa. Yuska Paola Costa Aguiar, coautora do artigo original do jogo Critical Failure, então ela já conhece bem a versão 1: os slides sobre a v1 devem ser curtos e focados nos problemas.
>
> Objetivo da reunião: apresentar a proposta de TCC e obter validação da orientadora para o escopo, as regras da v2, o simulador e o plano de avaliação.
>
> Siga o roteiro slide a slide do documento "Briefing para o Claude Design". Use o documento "Critical Failure 2.0 — Regras Completas" e o artigo em PDF como fonte de detalhes.
>
> Regras de conteúdo: pouco texto por slide (no máximo 5 tópicos curtos), um diagrama ou tabela quando o roteiro pedir, nenhum dado inventado. Os números das regras da v2 são provisórios e devem aparecer marcados assim.
>
> Estilo visual: acadêmico e limpo, fundo claro. Use de forma consistente uma cor para cada um dos 6 atributos de qualidade (Desempenho, Compatibilidade, Confiabilidade, Segurança, Portabilidade, Usabilidade), sempre acompanhada de um ícone, nunca só a cor. Duração alvo: 15 a 20 minutos de fala.

## 2. Roteiro, parte 1 — Ponto de partida e plano

### Slide 1 — Capa

- **Título provisório:** Critical Failure 2.0: redesign orientado por simulação e avaliação de um jogo de cartas para o ensino de teste não-funcional
- Nome do aluno, orientadora (profa. Yuska Paola Costa Aguiar), Centro de Informática — UFPB, data da reunião

### Slide 2 — O artigo de partida

**Mensagem:** a v1 funcionou bem como atividade, mas deixou problemas de design documentados.

- Critical Failure: jogo de cartas competitivo sobre atributos de qualidade e testes não-funcionais (SBQS 2025)
- Aplicado na disciplina de Teste de Software; 17 alunos jogaram e responderam ao questionário
- 14 de 17 disseram que se divertiram; 9 que revisaram conteúdo; 5 que aprenderam algo novo
- O blefe foi o elemento mais elogiado
- Problemas observados: 4 de 6 partidas desequilibradas; confusão entre mão e sistema e na pontuação

### Slide 3 — Regras da v1 (resumo)

**Visual sugerido:** fluxo curto de um turno.

- 54 cartas: 6 atributos de qualidade com 2 ou 3 testes cada, mais 3 cartas Critical Failure
- Cada jogador recebe 6 cartas: 3 viradas para baixo formam o sistema, 3 ficam na mão para testar
- Teste: se o defensor não tem a cor, o atacante pega uma carta do sistema dele; se tem, o defensor fica com a carta de ataque
- Blefe: o defensor declara ter a cor e, se contestado, lê a descrição de um teste; a resolução depende de aceitar ou revelar
- Pontuação: 1 por carta, +2 por par da mesma cor, +2 por trio de cores diferentes

### Slide 4 — O que a v1 deixou em aberto

**Mensagem:** os problemas vêm da estrutura das regras, não da inexperiência dos jogadores.

- Atacar o mais fraco é a jogada ótima: atacar o líder entrega cartas a ele
- Cada teste move 2 cartas de lugar, o que alimenta o efeito bola de neve
- Blefe aceito nunca é verificado, então declarar cobertura sempre compensa
- Não há trade-off nem contexto: mais cartas é sempre melhor
- Erros no baralho: Usabilidade com testes de Desempenho, "ScalabilityAvailability", Compatibilidade com só 6 cartas

### Slide 5 — Plano do TCC em 3 etapas iterativas

**Visual sugerido:** ciclo com três etapas e setas de retorno (Design Science Research).

1. **Regras v2:** redesign com base nos problemas da v1
2. **Simulador (motor de testes):** milhares de partidas entre bots para testar e calibrar o balanceamento
3. **Testes com humanos:** playtests pequenos e aplicação em turma

Os resultados de cada etapa voltam para ajustar as regras.

**Perguntas de pesquisa:**

- QP1: as novas regras reduzem o desequilíbrio observado na v1?
- QP2: como os alunos avaliam a experiência com a v2?
- QP3: jogar a v2 aumenta o acerto em questões sobre testes não-funcionais?

## 3. Roteiro, parte 2 — Regras da v2

### Slide 6 — A ideia central da v2

**Mensagem:** na v1, só os colegas testam o seu sistema; na v2, a produção também testa.

**Visual sugerido:** fluxo de um ciclo: Planejamento → Homologação → Produção, repetido 3 vezes, seguido do Critical Failure e da revelação final.

- **Planejamento:** comprar 2 cartas de um Backlog aberto (5 cartas visíveis) e construir até 1; sistema com no máximo 5 cartas
- **Homologação:** testar o vizinho designado (esquerda, direita, esquerda); sem escolha de alvo
- **Produção:** um incidente do mundo real atinge todos os jogadores
- Cada carta da mão serve para construir ou para testar: o dilema real entre desenvolver e testar

### Slide 7 — Homologação: blefe com Auditor

**Mensagem:** o blefe continua, mas agora exige conhecimento.

- As cartas mostram só atributo e nome do teste, sem descrição
- O defensor admite a falha ou se defende **explicando o teste com as próprias palavras**, tendo ou não a carta
- O **Auditor** (último jogador do ciclo, rotativo) confere a explicação no documento de referência e depois lê a descrição correta para a mesa
- O atacante aceita ou contesta: contestou e era verdade, atacante −1 e defensor compra 1 carta; era blefe, atacante +2 e defensor −1 com Alerta
- Base pedagógica: efeito de geração (Slamecka e Graf), já citado no artigo original

### Slide 8 — Produção, incidentes e pontuação

**Visual sugerido:** uma carta de incidente com o verso (contexto) e a frente (relato).

- **Radar de Riscos:** os próximos 2 contextos ficam visíveis (ex.: "Black Friday"), o que permite preparar-se por análise de risco
- **Diagnóstico simultâneo:** todos escolhem em segredo o atributo do incidente; acertar dá +1 ponto e reduz o dano
- Sem cobertura do atributo, o jogador perde pontos; quem tinha Alerta e não corrigiu perde mais
- **Critical Failure** vira o evento final: um dado sorteia o atributo, e nem a melhor cobertura evita todo o dano
- **Pontuação final:** pontos acumulados + 1 por atributo distinto no sistema + 1 por cobertura profunda − 1 por Alerta ativo

### Slide 9 — v1 × v2

**Visual sugerido:** tabela de três colunas.

| Problema na v1 | Mudança na v2 | Efeito esperado |
| --- | --- | --- |
| Atacar o mais fraco é ótimo | Vizinho designado | Fim do ataque ao jogador em desvantagem |
| Swing de 2 cartas por teste | Nenhuma carta troca de mão | Menos efeito bola de neve |
| Blefe nunca verificado | Contestação com revelação e Auditor | Blefar e detectar exigem conhecimento |
| Mais cartas é sempre melhor | Teto de 5 cartas e pontos por amplitude | Trade-off entre amplitude e profundidade |
| Teste sem contexto | Incidentes com Radar de Riscos | Teste baseado em risco |
| Pouco conteúdo por turno | Diagnóstico de incidentes por todos | Toda a mesa aprende a cada ciclo |

Nota no slide: os valores numéricos da v2 são provisórios e serão calibrados com o simulador.

## 4. Roteiro, parte 3 — Simulador, avaliação e TCC

### Slide 10 — O simulador e os bots

**Mensagem:** o jogo é tratado como um sistema sob teste, e os bots são os usuários virtuais, como num teste de carga.

**Visual sugerido:** diagrama de blocos: Regras (configuração YAML) → Motor de regras → Bots → Milhares de partidas → Métricas.

- Motor de regras em Python, determinístico (semente fixa), com v1 e v2 implementadas
- Bots: Aleatório, Construtor, Caçador, Heurístico e perfis de blefe (chance de blefar e de contestar)
- O conhecimento do aluno entra como probabilidade (acerto na explicação, matriz de confusão no diagnóstico), depois calibrada com dados da turma
- Cada bot só vê o que um jogador real veria

### Slide 11 — Balanceamento como requisito não-funcional

**Mensagem:** balanceamento vira um conjunto de requisitos com critério de aceite, verificados automaticamente.

| Requisito | Critério de aceite (a calibrar) |
| --- | --- |
| Equidade de assento | Vitória por posição perto de 1/N |
| Anti bola de neve | Líder após o ciclo 1 vence menos que na v1 |
| Habilidade importa | Bot Heurístico vence bem acima de 1/N, sem tornar o jogo determinístico |
| Sem estratégia dominante | Nenhuma estratégia pura de blefe vence todas as outras |
| Robustez | 1 milhão de partidas sem erro |

Experimentos: validar a v1, comparar v1 × v2, ablação de cada mudança, sensibilidade dos parâmetros, equilíbrio do blefe.

### Slide 12 — Técnicas de teste de software aplicadas

**Mensagem:** o simulador testa o jogo e também é testado; o TCC aplica teste não-funcional ao jogo que ensina teste não-funcional.

- **Testes unitários:** cada regra isolada
- **Testes baseados em propriedades:** invariantes em partidas aleatórias (54 cartas sempre, sistema com no máximo 5)
- **Teste metamórfico:** resolve o problema do oráculo (ex.: trocar nomes de atributos não muda as métricas)
- **Fuzzing e teste de mutação:** robustez do motor e qualidade da própria suíte de testes
- **Regressão em integração contínua:** cada mudança de regra roda a suíte de balanceamento

### Slide 13 — Testes com humanos

- Playtests pequenos para cronometrar a partida e corrigir ambiguidades
- Aplicação em turma: pré-teste → partida → pós-teste → questionário MEEGA+
- Registro por partida: placar, diagnósticos (curva de acerto e matriz de confusão) e cada defesa (teste nomeado, blefe, decisão do Auditor)
- Os dados reais calibram os bots e validam o simulador

### Slide 14 — Estrutura do TCC

**Mensagem:** formato artigo no modelo SBC, com capa e folha de aprovação do CI, como nos TCCs recentes do curso.

1. Introdução
2. Fundamentação teórica (teste não-funcional e ISO/IEC 25010, jogos educacionais, balanceamento e simulação, MEEGA+)
3. Trabalhos relacionados
4. Metodologia (Design Science Research)
5. Critical Failure 2.0
6. Resultados e discussão
7. Ameaças à validade
8. Conclusão e trabalhos futuros

### Slide 15 — Decisões e próximos passos

**Pontos para decidir com a orientadora:**

- Acesso a uma turma de Teste de Software (ou similar) no período do TCC
- Necessidade de aprovação no comitê de ética
- Conversa com os coautores da v1 sobre o trabalho derivado
- Nomenclatura da ISO/IEC 25010: versão 2011 ou 2023

**Próximos passos:** motor de regras da v2 com testes → bots e primeiros experimentos → playtests → aplicação em turma.

## 5. Arquivos para anexar

O Claude Design não lê esta conversa; ele só conhece o que você anexar ao projeto. Anexe estes três arquivos antes de colar o prompt.

| Arquivo | Como obter | Para quê |
| --- | --- | --- |
| Este briefing | Exportar em PDF ou Markdown | Roteiro e instruções da apresentação |
| Critical Failure 2.0 — Regras Completas | Exportar em PDF | Detalhes das regras da v2 |
| Artigo Critical Failure (SBQS 2025) | O PDF que já está no projeto do TCC | Dados e regras da v1 |

Na primeira versão gerada, confira principalmente três pontos: se os números da v1 batem com o artigo, se os valores da v2 aparecem marcados como provisórios e se a cor de cada atributo é a mesma em todos os slides.

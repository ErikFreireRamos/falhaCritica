# Critical Failure — simulador de partidas (TCC)

Simulador do jogo de cartas Critical Failure, parte do TCC de Erik Freire Ramos (Ciência da Computação, UFPB; orientadora: profa. Yuska Paola Costa Aguiar). O jogo é tratado como sistema sob teste: bots jogam milhares de partidas para verificar requisitos de balanceamento. Tudo o que o simulador produz vai para o texto do TCC.

## Quem decide é o autor

Não decida sozinho. Pare, apresente as opções com uma sugestão e deixe o autor escolher.

- **Sempre pergunte antes:** regra ou ambiguidade de regra, valor de parâmetro, zona de aceite de requisito, modelo e parâmetros dos bots, critério de métrica, escopo, ordem das fases, estrutura do projeto, dependência nova.
- **Siga sem perguntar:** só o que já foi aprovado e detalhes internos que não mudam comportamento (nomes de funções, organização de arquivos dentro da estrutura aprovada).
- Na dúvida se algo é decisão ou detalhe, pergunte.
- Toda decisão do autor entra em `docs/DIARIO_DE_BORDO.md` com data, opções e escolha.
- Detalhes internos escolhidos sem perguntar também são informados no diário.
- Princípio do autor para qualquer ponto de pontuação: manter a simplicidade.
- As zonas de aceite de `configs/requisitos.yaml` são confirmadas com o autor antes da primeira medição de cada requisito.

## Fontes, em ordem de autoridade

1. `docs/Critical_Failure_-_Regras_Completas_2.2.pdf`: fonte da verdade da v2.2, exceto pelas correções do autor (`COR-nn`), que são posteriores ao PDF e valem sobre ele até o PDF ser atualizado. Tudo reescrito em `docs/especificacao_v2_2.md`; as correções estão na seção "Correções do autor" e em `docs/HISTORICO_REGRAS.md`.
2. `docs/Critical_Failure_Artigo.pdf`: v1 (seções 4.2 a 4.4, Tabelas 2 a 4). Reescrita em `docs/especificacao_v1.md`.
3. `docs/Briefing_Apresentacao_TCC.md`: **só** os slides 5 e 10 a 13. Os slides 6 a 9 são da versão 2.0 e não valem.
4. `docs/prompt_claude_code_simulador.md`: especificação do simulador. As mudanças aprovadas em relação a ele estão no diário (entrada de 2026-11-09).

Não invente regras. Ponto ambíguo ou omisso vai para `docs/AMBIGUIDADES.md` e é perguntado ao autor.

## Convenções

- **Auditoria obrigatória.** Toda partida pode gerar um registro JSONL (`cf-audit/1`) com cabeçalho, eventos e fim. Cada evento separa `publico` de `oculto`, cita a `regra` que o justificou e traz o `estado_hash`. O registro permite refazer a partida.
- **Nenhum número de regra no código.** Todo valor vem do YAML em `configs/`, com o identificador da regra ao lado. Um teste varre o código das regras atrás de números literais.
- **Determinismo.** Mesma configuração e mesma semente geram registro idêntico byte a byte (exceto a data e hora do cabeçalho), em qualquer plataforma. Para isso: aleatoriedade derivada de `SeedSequence(semente, spawn_key=(partida, fluxo, contador))`; fluxo 0 para o jogo e um por bot; nenhum ponto flutuante no estado do motor; sorteios de bot com pesos inteiros; JSON canônico (chaves ordenadas, UTF-8, LF).
- **Motor puro.** `aplicar(estado, acao) -> (novo_estado, eventos)`. O motor valida a ação. Bots só recebem a `Observacao` e nunca tocam no estado.
- **Teste por regra.** Cada identificador de tipo `regra`, `definicao` ou `componente` tem pelo menos um teste marcado com `@pytest.mark.regra("R-x.y")`.
- **Vocabulário em português**, igual ao das regras: ficha, Alerta, Homologação, Backlog, categoria-chave, sistema, mão.
- **Identificadores:** `R-…` (v2.2), `V1-…` (v1), `AMB-nn`, `COR-nn`, `REQ-nn`, `MET-nn`, `VAR-nn`, `MOD-nn`. A convenção está no início de `docs/especificacao_v2_2.md`.
- **Regra impressa continua acessível.** Toda correção do autor fica atrás de uma chave de configuração, para o simulador medir o efeito da mudança. O padrão é sempre a versão corrigida.
- **Código por família de regras, YAML por versão:** `regras/v2/` com `configs/regras_v2_2.yaml`. Uma nova iteração das regras é um YAML novo e uma entrada em `docs/HISTORICO_REGRAS.md`, sem copiar código.
- **Registro do processo.** Atualize `docs/DIARIO_DE_BORDO.md` em toda sessão de trabalho e `docs/HISTORICO_REGRAS.md` em toda mudança de regra ou parâmetro.
- **Experimento oficial só com a árvore do git limpa.** O cabeçalho e o manifest registram o commit e se havia alteração não commitada.
- **Git:** um commit por fase, mensagens em português. A identidade do autor está configurada só neste repositório.

## Fases

| Fase | Entrega | Parada para revisão |
|---|---|---|
| 0 | Especificações, ambiguidades, requisitos, convenções, diário | sim |
| 1 | Núcleo, v2 (2.2 com módulo), auditoria, `replay`, `narrar`, `folha`, bot Aleatório, testes por regra e de propriedades, CI básica | sim |
| 1b | Executor mínimo, manifest, Parquet, primeiras métricas com intervalo de confiança | resumo |
| 2 | Bots e perfis, variantes estruturais, assento humano | resumo |
| 3 | v1 e Experimentos 1 e 2 | sim |
| 4 | Experimentos 3 a 6, equilíbrio do blefe, relatórios | resumo |
| 5 | Metamórficos, fuzzing, mutação, suíte noturna | resumo |

O estado atual está na última entrada do diário.

## Comandos

```
py -3.12 scripts/verificar_especificacao.py   # confere as especificações (Fase 0)
```

## Ambiente

- Windows, Python 3.12 (`py -3.12`), `uv` instalado. Sem `gh`.
- A pasta fica dentro do OneDrive: o diretório de resultados deve ser configurável.
- `mutmut` não roda no Windows nativo (precisa de `fork`): na Fase 5, usar o Linux da CI ou Docker.

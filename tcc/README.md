# TCC — versão inicial

Versão inicial do TCC, escrita em 14/11/2026. Usa o modelo de artigo da SBC e segue a mesma estrutura de seções
do artigo do SBQS 2025 (`docs/Critical_Failure_Artigo.pdf`), como pediu a orientadora.

## Como compilar

**Nesta máquina.** O MiKTeX foi instalado em 14/11/2026, para o usuário, com instalação automática de pacotes.

```
cd tcc
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

Se o terminal não encontrar o `pdflatex`, os programas estão em `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64`.

**No Overleaf.** Suba a pasta `tcc/` inteira, que já traz o `sbc-template.sty` e o `sbc.bst` oficiais, e compile
com pdfLaTeX.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `main.tex` | Preâmbulo, título, resumo, abstract e a ordem das seções |
| `capa.tex` | Capa provisória: substituir pela capa, ficha catalográfica e folha de aprovação do CI |
| `secoes/01-introducao.tex` a `06-conclusoes.tex` | As 6 seções do artigo |
| `secoes/07-artefatos.tex` | Disponibilidade dos artefatos e uso de IA |
| `figuras/` | Figuras em TikZ e pgfplots: ciclo de DSR, arquitetura do simulador, vantagem do líder |
| `referencias.bib` | As referências do artigo e as novas; os DOIs vão no campo `note`, porque o `sbc.bst` não imprime `doi` |
| `sbc-template.sty`, `sbc.bst` | Modelo oficial da SBC, baixado de `https://www.sbc.org.br/wp-content/uploads/2024/07/modelosparapublicaodeartigos.zip` |

Nota técnica: o `babel` e o `hyperref` precisam ser carregados **antes** do `sbc-template`. Na ordem inversa, o
LaTeX de 2026 para em `\begin{document}` com "Undefined control sequence".

## Pendências do autor (marcadas em vermelho no PDF com `\pendente`)

- Capa, ficha catalográfica e folha de aprovação do modelo do CI; mês e ano da defesa.
- Número de participantes do playtest, a turma e as datas das sessões (seção 3.4).
- Link público do repositório (Disponibilidade dos artefatos).
- Revisão do título, que é uma sugestão.
- Agradecimentos, se o modelo do curso pedir.
- O `sbc.bst` escreve "and" entre autores nas citações (por exemplo, "Gomes and Lelli 2021"). Decidir se fica assim
  ou se o estilo é adaptado para "e".

## De onde vem cada número

| Onde no texto | Fonte |
|---|---|
| Vantagem do líder, v1 × v2 (Fig. 3) | `resultados/fase3_exp2_v1_contra_v2/20261110-212034-f447f4b/relatorio.md` |
| Validação da v1 | `resultados/fase3_exp1_validacao_v1/20261110-205949-ad1624f/relatorio.md` |
| Matriz de estilos (Tab. 7), REQ-03, REQ-04, REQ-11, REQ-01 | `resultados/fase4_melhor_estilo/20261110-221516-ccd5649/relatorio.md` |
| Blefe e REQ-05 | `resultados/fase4_exp5_blefe/20261110-231109-b02b6d4/` e `fase4_exp5b_blefe_equilibrio/20261111-004253-e17bbf2/` |
| Requisitos (Tab. 8), variantes, REQ-13 | `resultados/fase4_exp6_variantes/20261114-145900-0564baa/relatorio.md` |
| Ablação | `resultados/fase4_exp3_ablacao/20261111-080955-f925943/relatorio.md` |
| Sensibilidade e combinações | `resultados/fase4_exp4_sensibilidade/20261111-082054-73762b5/` e `fase4_exp4b_combinacoes/20261111-134424-b263c34/` |
| Profundidade (Tab. 9) | `resultados/fase4_exp7_profundidade/20261111-183119-3a2f2e0/relatorio.md` |
| Total de partidas, teste de mutação | `docs/RESUMO_DOS_RESULTADOS.md` e `docs/DIARIO_DE_BORDO.md` |
| Playtest (Tab. 10 e texto da 5.3) | `uv run python scripts/resumir_playtest.py`, que lê o CSV local, fora do git |

## Decisões do autor para esta versão (14/11/2026)

- LaTeX no modelo SBC, em português, com Abstract em inglês.
- Mesmas seções do artigo, com os resultados na seção 5.
- Perguntas de pesquisa: QP1 e QP2. A QP3 (pré e pós-teste) foi retirada.
- Playtest com a v2.2 e o módulo; só o que o questionário perguntou; o CSV fica fora do git.
- Uso de IA declarado de forma breve; as imagens das cartas foram feitas com o GPT 6.

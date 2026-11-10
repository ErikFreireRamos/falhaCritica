# Regras do Critical Failure

Um arquivo por versão das regras. Enquanto o jogo estiver em ajuste, a fonte das regras é o Markdown desta pasta, e não um PDF (decisão do autor em 9 de novembro de 2026).

| Arquivo | Versão | Data | Origem | Situação |
|---|---|---|---|---|
| [v1.md](v1.md) | v1 | 2025 | Artigo do SBQS 2025, seções 4.2 e 4.3, com as decisões AMB-20 a AMB-29 | Linha de base da comparação |
| [v2.2.md](v2.2.md) | v2.2 | 2026-10-17 | Transcrição do PDF `docs/Critical_Failure_-_Regras_Completas_2.2.pdf` | Referência impressa; não editar |
| [v2.2.1.md](v2.2.1.md) | v2.2.1 | 2026-11-09 | v2.2 com as correções COR-01 e COR-02 e os esclarecimentos AMB-01 a AMB-15 | **Versão atual** |

## Como ler as marcas

- **[COR-nn]**: correção de regra decidida pelo autor. O antes e o depois estão em `docs/HISTORICO_REGRAS.md`.
- **[AMB-nn]**: esclarecimento de um ponto que o texto deixava em aberto. As interpretações consideradas e a decisão estão em `docs/AMBIGUIDADES.md`.

A redação dos trechos marcados foi proposta pelo assistente e aguarda a revisão do autor.

## Como criar uma versão nova

1. Copiar a versão atual para um arquivo com o próximo número (`v2.2.2.md`, por exemplo). Uma versão já usada em experimento não é mais editada.
2. Fazer as mudanças no arquivo novo, marcando cada trecho, e resumir tudo numa seção de histórico.
3. Registrar cada mudança em `docs/HISTORICO_REGRAS.md`, com a evidência que a motivou (o manifest do experimento ou a Folha de registro).
4. Criar o arquivo de configuração correspondente em `configs/` e atualizar `docs/especificacao_v2_2.md`.

O rótulo da versão vai no cabeçalho do registro de auditoria de cada partida, junto com o hash da configuração. É ele que diz com quais regras a partida foi jogada.

## Relação com os outros documentos

- `docs/especificacao_v2_2.md` e `docs/especificacao_v1.md` reescrevem as regras como itens numerados (`R-7.2.2`, `V1-4.3.6`). O motor, os testes e o registro de auditoria citam esses identificadores.
- `configs/` guarda os números de cada versão em YAML. Nenhum número de regra fica no código.

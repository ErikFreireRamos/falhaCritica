# Matriz de rastreabilidade — v2.2.1 e v1

Gerada por `scripts/matriz_rastreabilidade.py`. Não edite à mão.

Para cada item de `docs/especificacao_v2_2.md` e `docs/especificacao_v1.md`: onde o código o cita e quais testes o cobrem. Itens dos tipos `regra`, `definicao`, `componente` e `revogada` precisam de pelo menos um teste marcado com `@pytest.mark.regra`. Itens `mesa` e `nota` não são mecânica do motor.

**Cobertura:** 176 de 176 itens que exigem teste têm pelo menos um.

| ID | Tipo | Código | Testes | Situação |
|---|---|---|---|---|
| R-1.1 | regra | `regras/v2/motor.py:1116`, `regras/v2/motor.py:1135` | `test_vence_quem_tem_mais_fichas` | coberta |
| R-1.2 | regra | `regras/v2/motor.py:205` | `test_numero_de_jogadores_fora_do_intervalo`, `test_partidas_da_v2_2_2_sao_as_da_v2_2_1` e mais 1 | coberta |
| R-1.3 | regra | — | `test_depois_do_terceiro_ciclo_vem_o_critical_failure_e_a_pontuacao` | coberta |
| R-1.4 | definicao | — | `test_componentes_do_catalogo` | coberta |
| R-1.5 | nota | — | — | não exige teste |
| R-2.0.1 | componente | `regras/config.py:353` | `test_componentes_declarados_precisam_bater_com_o_catalogo`, `test_componentes_do_catalogo` e mais 1 | coberta |
| R-2.0.2 | componente | `regras/config.py:353` | `test_componentes_do_catalogo` | coberta |
| R-2.0.3 | componente | — | `test_depois_do_terceiro_ciclo_vem_o_critical_failure_e_a_pontuacao` | coberta |
| R-2.0.4 | mesa | — | — | não exige teste |
| R-2.0.5 | mesa | — | — | não exige teste |
| R-2.0.6 | componente | — | `test_todos_diagnosticam_uma_categoria_inclusive_o_auditor` | coberta |
| R-2.0.7 | componente | — | `test_todo_parametro_da_especificacao_esta_no_yaml_com_o_mesmo_valor` | coberta |
| R-2.0.8 | componente | — | `test_todo_parametro_da_especificacao_esta_no_yaml_com_o_mesmo_valor` | coberta |
| R-2.0.9 | componente | — | `test_invariantes_valem_a_cada_evento`, `test_teto_do_sistema` e mais 1 | coberta |
| R-2.0.10 | componente | — | `test_faces_do_dado`, `test_todo_parametro_da_especificacao_esta_no_yaml_com_o_mesmo_valor` | coberta |
| R-2.0.11 | componente | — | `test_estado_depois_da_preparacao` | coberta |
| R-2.0.12 | mesa | — | — | não exige teste |
| R-2.0.13 | regra | — | `test_carta_tem_so_categoria_e_nome` | coberta |
| R-2.0.14 | regra | — | `test_bug_duplicado`, `test_invariantes_valem_a_cada_evento` e mais 1 | coberta |
| R-2.0.15 | regra | — | `test_faces_do_dado` | coberta |
| R-2.0.16 | regra | `regras/v2/motor.py:1042` | `test_o_dado_sorteia_a_categoria_e_o_oito_e_rolado_de_novo` | coberta |
| R-2.1.1 | regra | `observacao.py:42` | `test_o_gabarito_so_aparece_depois_de_todos_revelarem` | coberta |
| R-2.1.2 | regra | — | `test_o_gabarito_so_aparece_depois_de_todos_revelarem` | coberta |
| R-2.1.3 | definicao | — | `test_so_a_categoria_chave_pontua` | coberta |
| R-2.1.4 | regra | — | `test_exemplo_da_categoria_secundaria_do_pdf`, `test_so_o_diagnostico_pela_categoria_chave_da_ficha` | coberta |
| R-2.1.5 | regra | — | `test_so_a_categoria_chave_pontua`, `test_so_o_diagnostico_pela_categoria_chave_da_ficha` | coberta |
| R-2.1.6 | regra | — | `test_na_producao_o_auditor_nao_tem_decisao_propria` | coberta |
| R-2.1.7 | nota | — | — | não exige teste |
| R-3.1 | regra | `regras/v2/motor.py:245` | `test_estado_depois_da_preparacao` | coberta |
| R-3.2 | regra | `regras/v2/motor.py:250` | `test_linha_do_tempo_e_radar` | coberta |
| R-3.2a | regra | — | `test_depois_do_terceiro_ciclo_vem_o_critical_failure_e_a_pontuacao` | coberta |
| R-3.2b | regra | — | `test_depois_do_terceiro_ciclo_vem_o_critical_failure_e_a_pontuacao`, `test_linha_do_tempo_e_radar` | coberta |
| R-3.3 | regra | `regras/v2/motor.py:251` | `test_linha_do_tempo_e_radar` | coberta |
| R-3.4 | regra | `regras/v2/motor.py:255`, `regras/v2/motor.py:265` | `test_estado_depois_da_preparacao` | coberta |
| R-3.4a | regra | — | `test_cada_um_ve_a_propria_mao_e_o_proprio_sistema_e_so_eles` | coberta |
| R-3.4b | regra | `regras/v2/motor.py:294`, `regras/v2/motor.py:313` | `test_carta_repetida_e_trocada_e_vai_para_o_fundo` | coberta |
| R-3.4c | regra | — | `test_estado_depois_da_preparacao` | coberta |
| R-3.5 | regra | `regras/v2/motor.py:275` | `test_estado_depois_da_preparacao`, `test_fichas_alertas_contagens_backlog_e_descarte_sao_publicos` | coberta |
| R-3.6 | regra | — | `test_estado_depois_da_preparacao` | coberta |
| R-3.6a | regra | `regras/v2/motor.py:276` | `test_estado_depois_da_preparacao` | coberta |
| R-3.7 | regra | — | `test_o_gabarito_so_aparece_depois_de_todos_revelarem` | coberta |
| R-3.8 | nota | — | — | não exige teste |
| R-4.1 | regra | `regras/v2/motor.py:444`, `regras/v2/motor.py:573`, `regras/v2/motor.py:859` | `test_as_fases_vem_sempre_na_mesma_ordem` | coberta |
| R-4.2 | regra | — | `test_depois_do_terceiro_ciclo_vem_o_critical_failure_e_a_pontuacao` | coberta |
| R-4.3 | regra | `regras/v2/motor.py:155` | `test_a_vez_segue_em_sentido_horario_e_da_voltas`, `test_cada_um_faz_o_turno_inteiro_em_sentido_horario` | coberta |
| R-4.4 | regra | — | `test_escolhas_ficam_ocultas_ate_todos_escolherem` | coberta |
| R-4.5 | regra | `regras/v2/motor.py:486` | `test_cada_um_faz_o_turno_inteiro_em_sentido_horario` | coberta |
| R-4.6 | regra | `regras/v2/motor.py:587` | `test_a_fase_termina_quando_todos_passaram` | coberta |
| R-4.7 | regra | — | `test_fim_do_ciclo_passa_os_marcadores_e_avanca_o_radar` | coberta |
| R-4.8 | regra | — | `test_na_sua_vez_o_jogador_testa_qualquer_outro_ou_passa` | coberta |
| R-4.9 | regra | `regras/v2/motor.py:1023` | `test_fim_do_ciclo_passa_os_marcadores_e_avanca_o_radar` | coberta |
| R-4.9a | definicao | `regras/v2/invariantes.py:61` | `test_disputas_respeitam_o_bug_duplicado_e_o_auditor_nunca_esta_envolvido`, `test_fim_do_ciclo_passa_os_marcadores_e_avanca_o_radar` | coberta |
| R-4.10 | regra | — | `test_fim_do_ciclo_passa_os_marcadores_e_avanca_o_radar` | coberta |
| R-4.11 | definicao | — | `test_linha_do_tempo_e_radar`, `test_todo_parametro_da_especificacao_esta_no_yaml_com_o_mesmo_valor` | coberta |
| R-4.12 | regra | — | `test_o_gabarito_so_aparece_depois_de_todos_revelarem` | coberta |
| R-4.13 | regra | `regras/v2/estado.py:108` | `test_fim_do_ciclo_passa_os_marcadores_e_avanca_o_radar` | coberta |
| R-4.14 | regra | — | `test_o_gabarito_so_aparece_depois_de_todos_revelarem` | coberta |
| R-4.15 | mesa | — | — | não exige teste |
| R-5.1 | definicao | — | `test_ganhar_vem_do_banco_e_pagar_passa_de_um_jogador_a_outro` | coberta |
| R-5.2 | regra | `regras/v2/motor.py:183` | `test_invariantes_valem_a_cada_evento`, `test_minimo_zero_e_o_banco_completa_o_pagamento` e mais 2 | coberta |
| R-5.2a | regra | `regras/v2/motor.py:190` | `test_minimo_zero_e_o_banco_completa_o_pagamento` | coberta |
| R-5.3 | regra | — | `test_itens_de_dano_do_incidente` | coberta |
| R-5.4 | regra | — | `test_fichas_alertas_contagens_backlog_e_descarte_sao_publicos` | coberta |
| R-6.1 | regra | `regras/v2/motor.py:462` | `test_baralho_e_descarte_vazios_a_compra_nao_acontece`, `test_tres_compras_obrigatorias_do_backlog_ou_do_topo` | coberta |
| R-6.1a | regra | `regras/v2/motor.py:537` | `test_tres_compras_obrigatorias_do_backlog_ou_do_topo` | coberta |
| R-6.1b | regra | `regras/v2/motor.py:528` | `test_baralho_e_descarte_vazios_a_compra_nao_acontece`, `test_compra_do_backlog_e_publica_e_a_vaga_e_reposta` | coberta |
| R-6.1c | regra | `regras/v2/motor.py:527` | `test_carta_pega_do_backlog_fica_conhecida_ate_ser_usada`, `test_compra_do_backlog_e_publica_e_a_vaga_e_reposta` e mais 1 | coberta |
| R-6.2 | regra | `regras/v2/motor.py:553` | `test_colocar_e_opcional_e_permanente`, `test_teto_do_sistema` | coberta |
| R-6.2a | regra | — | `test_colocar_e_opcional_e_permanente`, `test_o_sistema_so_muda_no_planejamento_e_so_cresce` | coberta |
| R-6.2b | revogada | `regras/v2/motor.py:563` | `test_regra_impressa_o_alerta_persiste_e_a_carta_o_corrige` | coberta |
| R-6.3 | regra | — | `test_fora_do_planejamento_nao_ha_acao_que_mude_o_sistema`, `test_o_sistema_so_muda_no_planejamento_e_so_cresce` | coberta |
| R-6.4 | regra | `regras/v2/motor.py:481` | `test_cada_um_faz_o_turno_inteiro_em_sentido_horario` | coberta |
| R-6.5 | regra | — | `test_nao_ha_limite_de_cartas_na_mao` | coberta |
| R-6.6 | regra | `regras/v2/motor.py:493`, `regras/v2/motor.py:502` | `test_baralho_vazio_reembaralha_o_descarte` | coberta |
| R-6.7 | mesa | — | — | não exige teste |
| R-6.8 | nota | — | — | não exige teste |
| R-6.9 | regra | `regras/v2/motor.py:449` | `test_alertas_saem_no_inicio_de_cada_planejamento`, `test_no_planejamento_ninguem_tem_alerta` e mais 2 | coberta |
| R-7.0.1 | regra | — | `test_na_sua_vez_o_jogador_testa_qualquer_outro_ou_passa`, `test_quem_nao_tem_jogada_possivel_passa_automaticamente` | coberta |
| R-7.0.2 | regra | — | `test_a_vez_segue_em_sentido_horario_e_da_voltas` | coberta |
| R-7.0.3 | regra | `regras/v2/motor.py:585`, `regras/v2/motor.py:632` | `test_quem_ja_passou_continua_podendo_ser_testado`, `test_quem_passa_sai_da_fase_e_guarda_as_cartas` | coberta |
| R-7.0.4 | regra | — | `test_a_fase_termina_quando_todos_passaram` | coberta |
| R-7.0.5 | regra | — | `test_o_defensor_nomeia_um_teste_da_categoria_com_ou_sem_a_carta` | coberta |
| R-7.1.1 | regra | — | `test_o_auditor_joga_normalmente` | coberta |
| R-7.1.2 | mesa | `observacao.py:72` | — | não exige teste |
| R-7.1.3 | regra | — | `test_o_auditor_julga_a_explicacao_sem_saber_se_o_defensor_tem_a_carta` | coberta |
| R-7.1.4 | regra | `regras/config.py:34`, `regras/v2/motor.py:409` | `test_auditor_envolvido_passa_a_funcao_a_esquerda`, `test_disputas_respeitam_o_bug_duplicado_e_o_auditor_nunca_esta_envolvido` | coberta |
| R-7.1.5 | regra | — | `test_a_decisao_do_auditor_e_final` | coberta |
| R-7.1.6 | regra | — | `test_todos_diagnosticam_uma_categoria_inclusive_o_auditor` | coberta |
| R-7.2.1 | regra | `regras/v2/motor.py:606` | `test_executar_o_teste_gasta_uma_carta_e_define_a_categoria` | coberta |
| R-7.2.1a | regra | `regras/v2/motor.py:849` | `test_a_carta_de_ataque_vai_para_o_descarte_no_fim_da_disputa` | coberta |
| R-7.2.2 | regra | `regras/v2/motor.py:636` | `test_admitir_e_falhou` | coberta |
| R-7.2.2a | regra | `regras/v2/motor.py:662` | `test_o_defensor_nomeia_um_teste_da_categoria_com_ou_sem_a_carta` | coberta |
| R-7.2.2b | regra | — | `test_o_defensor_nomeia_um_teste_da_categoria_com_ou_sem_a_carta` | coberta |
| R-7.2.2c | regra | `regras/v2/motor.py:427`, `regras/v2/motor.py:650` | `test_nomear_teste_de_outra_categoria_conta_como_falhou` | coberta |
| R-7.2.2d | mesa | — | — | não exige teste |
| R-7.2.3 | regra | `regras/v2/motor.py:697` | `test_a_decisao_do_auditor_e_final` | coberta |
| R-7.2.3a | mesa | — | — | não exige teste |
| R-7.2.3b | regra | — | `test_a_decisao_do_auditor_e_final` | coberta |
| R-7.2.4 | regra | — | `test_defesa_aceita_nada_acontece_e_nada_e_revelado` | coberta |
| R-7.2.4a | regra | — | `test_contestou_e_era_blefe`, `test_contestou_e_o_defensor_tinha_a_carta` | coberta |
| R-7.2.4b | regra | — | `test_carta_revelada_na_contestacao_fica_conhecida`, `test_contestou_e_o_defensor_tinha_a_carta` | coberta |
| R-7.2.5 | mesa | — | — | não exige teste |
| R-7.3.1 | regra | `regras/v2/estado.py:34`, `regras/v2/motor.py:813`, `regras/v2/motor.py:821` | `test_admitir_e_falhou` | coberta |
| R-7.3.2 | regra | `regras/v2/motor.py:758` | `test_defesa_aceita_nada_acontece_e_nada_e_revelado` | coberta |
| R-7.3.3 | regra | `regras/v2/motor.py:775` | `test_contestou_e_o_defensor_tinha_a_carta` | coberta |
| R-7.3.4 | regra | `regras/v2/estado.py:34`, `regras/v2/motor.py:793` | `test_contestou_e_era_blefe` | coberta |
| R-7.3.5 | nota | `bots/estrategicos.py:7`, `bots/estrategicos.py:170`, `bots/estrategicos.py:233` e mais 1 | — | não exige teste |
| R-7.4.1 | regra | — | `test_executar_o_teste_gasta_uma_carta_e_define_a_categoria` | coberta |
| R-7.4.2 | regra | `regras/v2/motor.py:376` | `test_bug_duplicado`, `test_disputas_respeitam_o_bug_duplicado_e_o_auditor_nunca_esta_envolvido` | coberta |
| R-7.4.2a | regra | — | `test_bug_duplicado` | coberta |
| R-7.4.3 | regra | — | `test_quem_passa_sai_da_fase_e_guarda_as_cartas` | coberta |
| R-7.4.4 | nota | — | — | não exige teste |
| R-7.5.1 | nota | — | — | não exige teste |
| R-8.0.1 | mesa | `regras/v2/motor.py:863` | — | não exige teste |
| R-8.0.2 | regra | `regras/v2/motor.py:878` | `test_todos_diagnosticam_uma_categoria_inclusive_o_auditor` | coberta |
| R-8.0.2a | regra | — | `test_todos_diagnosticam_uma_categoria_inclusive_o_auditor` | coberta |
| R-8.0.2b | regra | `observacao.py:97`, `regras/v2/motor.py:889` | `test_escolhas_ficam_ocultas_ate_todos_escolherem` | coberta |
| R-8.0.3 | regra | `observacao.py:51`, `regras/v2/motor.py:893` | `test_o_gabarito_so_aparece_depois_de_todos_revelarem` | coberta |
| R-8.0.4 | regra | `regras/v2/motor.py:921` | `test_exemplo_de_dano_do_pdf`, `test_so_a_categoria_chave_pontua` | coberta |
| R-8.0.4a | regra | `regras/v2/motor.py:924` | `test_so_a_categoria_chave_pontua`, `test_so_o_diagnostico_pela_categoria_chave_da_ficha` | coberta |
| R-8.0.5 | regra | `regras/v2/motor.py:950` | `test_exemplo_de_dano_do_pdf`, `test_itens_de_dano_do_incidente` | coberta |
| R-8.0.5a | regra | `regras/v2/motor.py:944` | `test_comprovar_cobertura_prefere_a_carta_que_a_mesa_ja_conhece`, `test_comprovar_cobertura_revela_o_minimo` | coberta |
| R-8.0.5b | regra | — | `test_exemplo_da_categoria_secundaria_do_pdf` | coberta |
| R-8.0.6 | regra | `regras/v2/motor.py:964`, `regras/v2/motor.py:974`, `regras/v2/motor.py:980` | `test_licao_aprendida`, `test_licao_aprendida_sem_carta_da_categoria_nao_acontece` | coberta |
| R-8.0.6a | regra | `regras/v2/motor.py:975` | `test_licao_aprendida` | coberta |
| R-8.0.6b | regra | — | `test_licao_aprendida` | coberta |
| R-8.0.7 | regra | `regras/v2/motor.py:1000` | `test_limpeza_remove_so_os_alertas_da_categoria_chave` | coberta |
| R-8.0.7a | regra | — | `test_exemplo_da_categoria_secundaria_do_pdf`, `test_limpeza_remove_so_os_alertas_da_categoria_chave` | coberta |
| R-8.0.7b | regra | — | `test_comprovar_cobertura_revela_o_minimo` | coberta |
| R-8.0.7c | regra | — | `test_limpeza_remove_so_os_alertas_da_categoria_chave` | coberta |
| R-8.0.8 | definicao | `regras/v2/estado.py:54` | `test_so_a_categoria_chave_pontua` | coberta |
| R-8.1.1 | regra | `regras/v2/motor.py:934` | `test_itens_de_dano_do_incidente` | coberta |
| R-8.1.2 | regra | `regras/config.py:317`, `regras/v2/motor.py:936` | `test_itens_de_dano_do_incidente` | coberta |
| R-8.1.3 | regra | `regras/v2/motor.py:938` | `test_itens_de_dano_do_incidente` | coberta |
| R-8.1.4 | regra | — | `test_blefe_aceito_nao_protege_na_producao` | coberta |
| R-8.1.5 | nota | — | — | não exige teste |
| R-8.1.6 | nota | — | — | não exige teste |
| R-9.0.1 | regra | `regras/v2/motor.py:1007` | `test_depois_do_terceiro_ciclo_vem_o_critical_failure_e_a_pontuacao` | coberta |
| R-9.1.1 | regra | `regras/v2/motor.py:1047` | `test_o_dado_sorteia_a_categoria_e_o_oito_e_rolado_de_novo` | coberta |
| R-9.1.2 | regra | — | `test_no_critical_failure_nao_ha_diagnostico` | coberta |
| R-9.1.3 | regra | `regras/v2/motor.py:1051` | `test_itens_de_dano_do_critical_failure` | coberta |
| R-9.1.4 | regra | `regras/v2/motor.py:1053` | `test_itens_de_dano_do_critical_failure` | coberta |
| R-9.1.5 | regra | `regras/v2/motor.py:1055` | `test_itens_de_dano_do_critical_failure` | coberta |
| R-9.1.6 | regra | `regras/v2/motor.py:1057`, `regras/v2/motor.py:1074` | `test_itens_de_dano_do_critical_failure`, `test_o_alerta_nao_sai_depois_do_critical_failure` | coberta |
| R-9.1.7 | regra | `regras/v2/motor.py:1063` | `test_itens_de_dano_do_critical_failure` | coberta |
| R-9.1.8 | nota | — | — | não exige teste |
| R-9.2.1 | regra | `regras/v2/motor.py:1099` | `test_pontuacao_final`, `test_pontuacao_final_com_poucas_fichas_usa_o_saldo` | coberta |
| R-9.2.2 | regra | `regras/v2/motor.py:1087` | `test_pontuacao_final` | coberta |
| R-9.2.3 | regra | — | `test_pontuacao_final` | coberta |
| R-9.2.3a | definicao | — | `test_itens_de_dano_do_critical_failure` | coberta |
| R-9.2.4 | regra | `regras/v2/motor.py:1090` | `test_o_alerta_nao_sai_depois_do_critical_failure`, `test_pontuacao_final` | coberta |
| R-9.2.5 | regra | — | `test_pontuacao_final` | coberta |
| R-9.2.6 | nota | — | — | não exige teste |
| R-9.2.7 | regra | `regras/v2/motor.py:1116` | `test_desempate_por_menos_alertas_ativos` | coberta |
| R-9.2.8 | regra | `regras/v2/motor.py:1116` | `test_desempate_por_mais_diagnosticos_certos` | coberta |
| R-10.1 | nota | — | — | não exige teste |
| R-10.2 | nota | — | — | não exige teste |
| R-10.3 | nota | — | — | não exige teste |
| R-10.4 | nota | — | — | não exige teste |
| R-10.5 | nota | — | — | não exige teste |
| R-10.6 | nota | — | — | não exige teste |
| R-10.7 | nota | — | — | não exige teste |
| R-10.8 | nota | — | — | não exige teste |
| R-10.9 | nota | — | — | não exige teste |
| R-11.1 | regra | — | `test_componentes_do_catalogo` | coberta |
| R-11.2 | regra | — | `test_com_o_modulo_as_72_cartas_se_conservam`, `test_componentes_do_catalogo` | coberta |
| R-11.3 | regra | — | `test_com_o_modulo_as_72_cartas_se_conservam`, `test_componentes_do_catalogo` | coberta |
| R-11.4 | regra | — | `test_com_o_modulo_ha_oito_categorias_no_leque` | coberta |
| R-11.5 | regra | — | `test_com_o_modulo_a_face_oito_vale` | coberta |
| R-11.6 | regra | — | `test_com_o_modulo_ha_oito_categorias_no_leque` | coberta |
| R-11.7 | componente | `regras/config.py:353` | `test_com_o_modulo_as_72_cartas_se_conservam`, `test_componentes_declarados_precisam_bater_com_o_catalogo` e mais 1 | coberta |
| R-B.0.1 | componente | — | `test_componentes_do_catalogo` | coberta |
| R-B.0.2 | mesa | — | — | não exige teste |
| R-C.0.1 | componente | — | `test_componentes_do_catalogo` | coberta |
| R-C.0.2 | regra | — | `test_itens_de_dano_do_incidente` | coberta |
| R-C.0.3 | regra | — | `test_itens_de_dano_do_incidente` | coberta |
| R-C.0.4 | nota | — | — | não exige teste |
| R-C.0.5 | nota | — | — | não exige teste |
| R-REG.1 | regra | `auditoria/folha.py:1` | `test_folha_traz_o_diagnostico_de_cada_jogador_por_incidente` | coberta |
| R-REG.2 | regra | — | `test_folha_traz_cada_defesa` | coberta |
| R-REG.3 | regra | `auditoria/folha.py:1` | `test_folha_traz_as_fichas_finais_e_e_exportada_em_csv` | coberta |
| V1-T2.1 | componente | — | `test_baralho_da_tabela_3` | coberta |
| V1-T2.2 | regra | `regras/v1/motor.py:130` | `test_numero_de_jogadores` | coberta |
| V1-T2.3 | nota | — | — | não exige teste |
| V1-4.1.1 | definicao | — | `test_baralho_da_tabela_3` | coberta |
| V1-4.2.1 | definicao | — | `test_baralho_da_tabela_3` | coberta |
| V1-4.2.2 | regra | `regras/v1/invariantes.py:25` | `test_critical_failure_fica_obrigatoriamente_na_mao`, `test_montagem_do_sistema` | coberta |
| V1-4.2.3 | regra | `regras/v1/motor.py:273`, `regras/v1/motor.py:274` | `test_critical_failure_e_falha_automatica` | coberta |
| V1-4.3.1 | regra | `regras/v1/motor.py:151`, `regras/v1/motor.py:159` | `test_cada_jogador_compra_seis_cartas_e_ha_ordem_de_jogo` | coberta |
| V1-4.3.2 | regra | `regras/v1/motor.py:166` | `test_cada_jogador_compra_seis_cartas_e_ha_ordem_de_jogo` | coberta |
| V1-4.3.3 | regra | `regras/v1/motor.py:217`, `regras/v1/motor.py:230` | `test_critical_failure_fica_obrigatoriamente_na_mao`, `test_montagem_do_sistema` | coberta |
| V1-4.3.4 | regra | `regras/v1/motor.py:242`, `regras/v1/motor.py:245`, `regras/v1/motor.py:418` | `test_cada_um_testa_na_sua_vez_ate_usar_as_tres_cartas` | coberta |
| V1-4.3.4a | regra | — | `test_cada_um_testa_na_sua_vez_ate_usar_as_tres_cartas` | coberta |
| V1-4.3.5 | regra | `regras/v1/motor.py:267` | `test_testa_qualquer_adversario_com_qualquer_carta_da_mao` | coberta |
| V1-4.3.6 | regra | `regras/v1/motor.py:294`, `regras/v1/motor.py:353` | `test_declarar_que_nao_tem_e_falha_encontrada` | coberta |
| V1-4.3.7 | regra | `regras/v1/motor.py:357`, `regras/v1/motor.py:366` | `test_declaracao_aceita_e_defesa_bem_sucedida`, `test_so_a_declaracao_de_quem_tem_a_cor_leva_explicacao` | coberta |
| V1-4.3.8 | regra | `regras/v1/motor.py:287` | `test_declaracao_aceita_e_defesa_bem_sucedida` | coberta |
| V1-4.3.9 | regra | `regras/v1/motor.py:311`, `regras/v1/motor.py:315` | `test_duvida_pede_a_definicao_e_o_atacante_decide` | coberta |
| V1-4.3.10 | regra | — | `test_duvida_pede_a_definicao_e_o_atacante_decide` | coberta |
| V1-4.3.10a | regra | `regras/v1/motor.py:301`, `regras/v1/motor.py:305` | `test_blefe_aceito_pela_verdade_se_a_configuracao_pedir`, `test_declaracao_aceita_e_defesa_bem_sucedida` e mais 1 | coberta |
| V1-4.3.10b | regra | `regras/v1/motor.py:334`, `regras/v1/motor.py:343` | `test_contestacao_revela_a_carta_que_a_mesa_ja_conhece`, `test_contestou_e_era_verdade` | coberta |
| V1-4.3.11 | regra | `regras/v1/motor.py:339`, `regras/v1/motor.py:340` | `test_contestou_e_era_verdade` | coberta |
| V1-4.3.12 | regra | `regras/v1/motor.py:245`, `regras/v1/motor.py:344` | `test_contestou_e_era_blefe` | coberta |
| V1-4.3.13 | regra | `regras/v1/motor.py:424`, `regras/v1/motor.py:428` | `test_cada_um_testa_na_sua_vez_ate_usar_as_tres_cartas` | coberta |
| V1-4.3.14 | regra | `regras/v1/motor.py:436` | `test_revelacao_pontuacao_e_vencedor` | coberta |
| V1-4.3.15 | regra | `regras/v1/pontuacao.py:1` | `test_pontuacao_pela_melhor_divisao` | coberta |
| V1-4.3.16 | regra | — | `test_pontuacao_pela_melhor_divisao` | coberta |
| V1-4.3.17 | regra | — | `test_pontuacao_pela_melhor_divisao` | coberta |
| V1-4.3.18 | regra | `regras/v1/pontuacao.py:1` | `test_pontuacao_pela_melhor_divisao` | coberta |
| V1-4.3.19 | regra | `regras/v1/motor.py:424`, `regras/v1/motor.py:454` | `test_revelacao_pontuacao_e_vencedor` | coberta |
| V1-T4.1 | nota | — | — | não exige teste |
| V1-T4.2 | nota | — | — | não exige teste |
| V1-T4.3 | nota | — | — | não exige teste |
| V1-4.4.1 | evidencia | — | — | não exige teste |
| V1-4.4.2 | evidencia | — | — | não exige teste |
| V1-4.4.3 | evidencia | — | — | não exige teste |
| V1-4.4.4 | evidencia | — | — | não exige teste |
| V1-4.4.5 | evidencia | — | — | não exige teste |
| V1-4.4.6 | evidencia | — | — | não exige teste |

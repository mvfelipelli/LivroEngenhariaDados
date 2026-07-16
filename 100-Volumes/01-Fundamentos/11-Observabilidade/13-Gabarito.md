---
title: Gabarito dos Exercícios de Observabilidade
aliases: [Gabarito do Módulo de Observabilidade]
tags: [observabilidade, gabarito, modulo-11]
created: 2026-07-16
updated: 2026-07-16
description: "Respostas comentadas dos exercícios de observabilidade."
---

# Gabarito

1. Telemetria emite evidência; monitoramento compara condições conhecidas; observabilidade permite explicar estados e investigar o desconhecido.
2. Logs detalham eventos, métricas resumem séries e traces ligam operações causais.
3. SLI mede comportamento, SLO define meta e orçamento expressa falha tolerada.
4. Upstream busca causas e fontes; downstream identifica produtos e consumidores afetados.
5. Contagem, completude, volume esperado, reconciliação e contrato do dataset.
6. Cardinalidade quase ilimitada, custo alto e consultas degradadas.
7. Correlacionar pela linhagem, agrupar pelo incidente upstream e deduplicar notificações.
8. Duplicar efeitos, publicar dados incorretos e declarar recuperação sem validar consumidores.
9. `trace_id`, `run_id`, tarefa, dataset, partição, versão, ambiente e owner.
10. Freshness, reconciliação e disponibilidade de consulta dentro de janelas definidas.
11. Executivo mostra SLO e risco; operacional mostra fila, erro e capacidade; diagnóstico permite decompor por contexto.
12. Confirmar atraso, fonte, partição, dependências, retry seguro, comunicação, backfill e validação.
13. O grafo deve ligar fontes, transformações, produto e consumidores com direção e contexto temporal.
14. Redigir segredos e identificadores na origem, restringir acesso e definir retenção por criticidade e auditoria.
15. Teste de regressão, guardrail de implantação, automação de rollback e verificação de eficácia com owner e prazo.
16. O caminho cai de 420 para 300 segundos, equivalente ao SLO; a condição `>` não deve abrir incidente.

> [!tip]
> Uma resposta forte relaciona sinal a pergunta, impacto e ação operacional.

Continue em [[14-Laboratorio]].

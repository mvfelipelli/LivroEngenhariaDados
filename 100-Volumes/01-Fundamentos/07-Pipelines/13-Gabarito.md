---
title: Gabarito dos Exercícios de Pipelines
aliases: [Gabarito do Módulo de Pipelines]
tags: [pipelines, gabarito, modulo-07]
created: 2026-07-16
updated: 2026-07-16
description: "Respostas comentadas dos exercícios de pipelines."
---

# Gabarito

1. Tarefa é unidade operacional; job é trabalho parametrizado; run é uma instância; pipeline coordena o fluxo completo.
2. O programa pode terminar sem erro e ainda processar partição incompleta, schema incorreto ou valores inválidos.
3. Dependência de dados transfere uma saída; dependência de controle apenas impõe ordem ou condição.
4. Event time pertence ao fato; processing time pertence à observação pelo sistema.
5. O relógio não prova prontidão. Um evento de chegada confirmada, manifesto ou sensor de completude é limite melhor.
6. O efeito pode ter ocorrido antes do timeout. Sem chave idempotente, a repetição pode criar outra cobrança.
7. A aciclicidade; não existe ordenação topológica completa.
8. `partições publicadas até 08h / partições esperadas`, medido na janela acordada.
9. `extrair_pedidos → validar_pedidos`; `extrair_clientes → validar_clientes`; ambas convergem em `enriquecer_vendas → publicar → reconciliar`.
10. Retry com backoff para rede; timeout conforme volume histórico; schema inválido falha cedo; registros inválidos vão para quarentena com causa.
11. Executar por partição, com código versionado, pool separado, prioridade menor, limite de concorrência e reconciliação antes do commit.
12. `MERGE` por `pedido_id`, ou substituição atômica da partição após deduplicação determinística.
13. Escrever em staging, validar e trocar atomicamente um ponteiro, view ou partição; manter a versão anterior para rollback.
14. Logs com run/tarefa/partição; métricas de fila, duração e freshness; metadados de versão, schema e linhagem.
15. Descartar após limite reduz custo, mas perde correções; atualizar janelas mantém precisão com estado; encaminhar para reconciliação batch separa baixa latência de correção final.
16. A implementação deve atualizar o grafo, manter aciclicidade e demonstrar que a nova tarefa só depende das entradas necessárias.

> [!tip]
> Respostas diferentes podem estar corretas se explicitarem requisitos, fronteiras e trade-offs.

Continue com a prática em [[14-Laboratorio]].

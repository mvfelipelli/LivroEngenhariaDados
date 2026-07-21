---
title: Estudo de Caso — Pedidos em Tempo Quase Real
description: "Agregação por event time e publicação idempotente."
tags: [apache-spark, structured-streaming, dataretail]
aliases: [Caso DataRetail Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — Pedidos em Tempo Quase Real

A DataRetail consome pedidos Kafka e publica receita por loja em janelas de cinco minutos. A análise histórica mostra que 99,7% chegam em até 12 minutos; o watermark é definido em 20 minutos, com reconciliação diária para a cauda tardia.

```mermaid
flowchart LR
    K["Kafka pedidos"] --> V["Validação"]
    V --> D["Deduplicação por evento"]
    D --> W["Janela + watermark"]
    W --> F["foreachBatch"]
    F --> T["Tabela com upsert"]
    V --> Q["Quarentena"]
```

O checkpoint é exclusivo por ambiente. `batch_id` e identificador da query compõem a chave de commit. Métricas acompanham atraso, backlog, estado, descartes tardios e duração do trigger.

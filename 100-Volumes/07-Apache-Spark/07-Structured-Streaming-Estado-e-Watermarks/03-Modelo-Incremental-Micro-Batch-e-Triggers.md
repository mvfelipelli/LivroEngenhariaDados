---
title: Modelo Incremental, Micro-batch e Triggers
description: "Agendamento, latência e ritmo de processamento."
tags: [apache-spark, micro-batch, triggers]
aliases: [Triggers Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Modelo Incremental, Micro-batch e Triggers

Cada micro-batch identifica um intervalo disponível, executa o plano e registra progresso. Trigger padrão inicia o próximo lote assim que o anterior termina; processing time estabelece intervalo mínimo; available-now processa o backlog disponível e encerra.

```python
query = (resultado.writeStream
    .trigger(processingTime="30 seconds")
    .outputMode("append")
    .start())
```

Trigger menor que a duração do lote não cria capacidade; apenas evidencia atraso crescente. Monitore `inputRowsPerSecond`, `processedRowsPerSecond`, duração por fase e backlog da fonte. Para cargas incrementais finitas, available-now simplifica orquestração e mantém semântica streaming.

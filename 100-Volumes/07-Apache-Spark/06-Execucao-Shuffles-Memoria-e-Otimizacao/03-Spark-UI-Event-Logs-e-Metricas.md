---
title: Spark UI, Event Logs e Métricas
description: "Observação de jobs, stages, tasks, SQL e executors."
tags: [apache-spark, spark-ui, metricas]
aliases: [Spark UI]
created: 2026-07-20
updated: 2026-07-20
---

# Spark UI, Event Logs e Métricas

A aba Jobs mostra ações e DAGs; Stages detalha tasks, shuffle, spill e duração; SQL liga consultas a planos; Executors revela memória, GC e falhas; Storage acompanha persistência.

Event logs preservam eventos para o History Server após a aplicação. Habilite caminho durável e retenção compatível com investigação.

Métricas essenciais incluem percentis de duração, input/output, shuffle read/write, fetch wait, spill, peak execution memory, GC e registros. Compare mediana com máximo: uma cauda longa sugere skew, host degradado ou variabilidade externa.

> [!tip]
> Comece pelo stage que domina o caminho crítico, não pelo maior número absoluto fora dele.

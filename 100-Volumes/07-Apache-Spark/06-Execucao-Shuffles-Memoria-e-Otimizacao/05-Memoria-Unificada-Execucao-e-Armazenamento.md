---
title: Memória Unificada, Execução e Armazenamento
description: "Uso de heap, overhead, cache e estruturas de execução."
tags: [apache-spark, memoria, gc]
aliases: [Memória Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Memória Unificada, Execução e Armazenamento

A região unificada atende execução — joins, agregações e sorts — e armazenamento de blocos persistidos. Execução pode desalojar cache; cache não deve impedir memória mínima de execução.

Heap JVM não representa toda a memória do container. Overhead cobre estruturas nativas, buffers, Python workers e outros processos. Exceder limite físico pode matar o executor sem `OutOfMemoryError` claro no heap.

Mais memória por executor reduz paralelismo por host e amplia impacto de falha. Muitos núcleos por executor aumentam concorrência por heap e GC. Dimensione com métricas de peak memory, spill, GC, tamanho de partição e limite do cluster.

Serialização compacta e APIs estruturadas reduzem objetos e pressão de GC.

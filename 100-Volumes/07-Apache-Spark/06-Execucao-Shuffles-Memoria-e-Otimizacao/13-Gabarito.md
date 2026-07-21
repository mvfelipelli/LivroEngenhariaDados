---
title: Gabarito — Otimização Spark
description: "Respostas dos exercícios de desempenho."
tags: [apache-spark, performance, gabarito]
aliases: [Gabarito Otimização Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. Jobs/DAG; Stages/tasks; SQL/planos; Executors/memória, GC e falhas.
2. Chaves precisam ser redistribuídas para a mesma partição de agregação.
3. Métricas registram bytes derramados antes/depois de serialização e escrita física.
4. Investigar skew, bytes, spill, retries, GC e host da task extrema.
5. Coalesce se apenas reduzir mantendo equilíbrio; repartition se redistribuição for necessária.
6. Reuso múltiplo, custo alto de recomputação e tamanho compatível com armazenamento.
7. Mesma entrada/cluster, aquecimento, repetições, plano confirmado, duração e memória.
8. Pré-agregar, separar chave quente ou usar sal e segunda agregação.

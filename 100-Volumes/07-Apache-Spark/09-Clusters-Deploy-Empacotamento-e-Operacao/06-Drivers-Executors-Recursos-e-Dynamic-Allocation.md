---
title: Drivers, Executors, Recursos e Dynamic Allocation
description: "Dimensionamento e elasticidade de recursos."
tags: [apache-spark, recursos, dynamic-allocation]
aliases: [Recursos Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Drivers, Executors, Recursos e Dynamic Allocation

Driver precisa armazenar planos, metadados e resultados pequenos. Executors combinam cores, heap e overhead. Número de slots aproxima executors × cores, mas I/O, tasks e limites externos determinam utilização.

Dynamic allocation adiciona executors sob backlog e remove executors ociosos. Requer mecanismo de preservação de shuffle compatível, limites mínimo/máximo e tempo de ociosidade ajustado. Cargas curtas podem terminar antes da expansão; streaming stateful exige cuidado ao remover executors.

Executors enormes ampliam GC e impacto de falha; executors minúsculos aumentam overhead. Use métricas de CPU, memória, spill, GC, task duration e espera por recurso para dimensionar.

---
title: Resumo — Fundamentos Spark
description: "Síntese dos conceitos do módulo."
tags: [apache-spark, resumo]
aliases: [Resumo Fundamentos Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Resumo

- Spark troca simplicidade local por paralelismo, escala e recuperação.
- Driver planeja; executors processam; cluster manager aloca recursos.
- Ações criam jobs, shuffles separam stages e partições originam tasks.
- Lazy evaluation permite analisar o DAG antes da execução.
- Linhagem permite recomputar partições perdidas.
- `SparkSession` é a entrada das APIs estruturadas.
- Configuração operacional deve ficar fora da lógica de negócio.

O próximo módulo desenvolverá RDDs, partições, transformações e ações.

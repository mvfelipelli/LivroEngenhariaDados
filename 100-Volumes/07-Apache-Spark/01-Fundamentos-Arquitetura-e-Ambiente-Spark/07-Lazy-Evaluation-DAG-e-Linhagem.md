---
title: Lazy Evaluation, DAG e Linhagem
description: "Planos, dependências e recomputação tolerante a falhas."
tags: [apache-spark, lazy-evaluation, dag, linhagem]
aliases: [Lazy Evaluation Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Lazy Evaluation, DAG e Linhagem

Transformações descrevem novos dados, mas não os materializam. Uma ação como `count`, `write` ou `collect` solicita resultado. O Spark organiza dependências em um grafo acíclico direcionado.

```python
pedidos = spark.range(1_000_000)
pares = pedidos.where("id % 2 = 0")  # plano
total = pares.count()                 # execução
```

A linhagem registra como reconstruir uma partição perdida. Ações repetidas podem recomputar toda a linhagem se não houver persistência.

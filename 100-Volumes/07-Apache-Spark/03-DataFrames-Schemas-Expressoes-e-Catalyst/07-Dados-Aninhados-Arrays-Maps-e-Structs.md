---
title: Dados Aninhados, Arrays, Maps e Structs
description: "Manipulação declarativa de estruturas semiestruturadas."
tags: [apache-spark, arrays, structs]
aliases: [Dados Aninhados Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Dados Aninhados, Arrays, Maps e Structs

`StructType` agrupa campos; `ArrayType` preserva sequência; `MapType` representa chaves homogêneas. Acesso por `pedido.cliente.id`, `element_at` e funções de ordem superior evita converter estruturas em objetos Python.

```python
normalizado = eventos.select(
    F.col("pedido.id").alias("pedido_id"),
    F.explode_outer("pedido.itens").alias("item"),
).select("pedido_id", "item.sku", "item.quantidade")
```

`explode` multiplica linhas e pode amplificar volume. Calcule cardinalidade esperada e filtre antes de explodir. `explode_outer` preserva linha com coleção nula ou vazia conforme a semântica desejada.

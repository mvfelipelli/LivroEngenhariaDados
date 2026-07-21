---
title: Select, Filter, withColumn e Expressões
description: "Transformações declarativas e composição de colunas."
tags: [apache-spark, dataframe, expressoes]
aliases: [Transformações DataFrame]
created: 2026-07-20
updated: 2026-07-20
---

# Select, Filter, withColumn e Expressões

`select` projeta expressões; `where` filtra; `withColumn` adiciona ou substitui; `drop` remove; `withColumnRenamed` altera nome. Operações retornam novo DataFrame.

```python
validos = (
    pedidos
    .where(F.col("status").isin("pago", "enviado"))
    .select(
        "pedido_id",
        F.upper(F.trim("uf")).alias("uf"),
        F.coalesce("desconto_centavos", F.lit(0)).alias("desconto_centavos"),
    )
)
```

Encadear centenas de `withColumn` em loop cria planos profundos. Gere a lista de expressões e use um único `select`. Colunas qualificadas evitam ambiguidade após joins.

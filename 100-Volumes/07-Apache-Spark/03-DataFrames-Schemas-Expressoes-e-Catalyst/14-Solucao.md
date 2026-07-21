---
title: Solução — Normalização Declarativa de Pedidos
description: "Implementação de referência com funções nativas."
tags: [apache-spark, dataframe, solucao]
aliases: [Solução Laboratório DataFrame]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Normalização Declarativa de Pedidos

```python
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.master("local[2]").appName("normalizacao").getOrCreate()
try:
    pedidos = (spark.range(10_000, numPartitions=4)
        .withColumn("pedido_id", F.concat(F.lit("P-"), F.col("id")))
        .withColumn("loja_id", F.col("id") % 10)
        .withColumn("valor_centavos", (F.col("id") % 5_000) + 1)
        .withColumn("status", F.when(F.col("id") % 2 == 0, "pago").otherwise("pendente")))
    publicados = (pedidos.where((F.col("valor_centavos") > 0) & (F.col("status") == "pago"))
        .select("pedido_id", "loja_id",
            (F.col("valor_centavos") / F.lit(100)).cast("decimal(18,2)").alias("valor_reais")))
    publicados.explain(mode="formatted")
    assert publicados.count() == 5_000
    assert publicados.select("loja_id").distinct().count() == 5
    print("VALIDACAO_OK pedidos=5000 lojas=5")
finally:
    spark.stop()
```

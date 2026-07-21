---
title: Solução — Mart Comercial com Spark SQL
description: "Implementação de referência do laboratório SQL."
tags: [apache-spark, spark-sql, solucao]
aliases: [Solução Laboratório Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Mart Comercial com Spark SQL

```python
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.master("local[2]").appName("mart-comercial").getOrCreate()
try:
    pedidos = (spark.range(20_000).withColumn("loja_id", F.col("id") % 10)
        .withColumn("cliente_id", F.col("id") % 1000)
        .withColumn("valor_centavos", (F.col("id") % 5000) + 100)
        .withColumn("status", F.when(F.col("id") % 2 == 0, "pago").otherwise("pendente")))
    lojas = spark.range(10).select(F.col("id").alias("loja_id"),
        F.concat(F.lit("Loja "), F.col("id")).alias("loja"))
    pagos = pedidos.where("status = 'pago'")
    base = pagos.join(F.broadcast(lojas), "loja_id", "left")
    orfaos = base.where("loja IS NULL").count()
    receita = base.groupBy("loja_id").agg(F.sum("valor_centavos").alias("receita"))
    w = Window.partitionBy("cliente_id").orderBy("id")
    sequencia = base.withColumn("ordem", F.row_number().over(w))
    assert pagos.count() == 10_000 and receita.count() == 5 and orfaos == 0
    sequencia.explain(mode="formatted")
    print("VALIDACAO_OK pagos=10000 lojas=5 orfaos=0")
finally:
    spark.stop()
```

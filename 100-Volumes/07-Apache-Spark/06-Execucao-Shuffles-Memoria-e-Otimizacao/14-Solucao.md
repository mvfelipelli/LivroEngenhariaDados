---
title: Solução — Diagnóstico de Skew e Partições
description: "Implementação de referência com sal em dois níveis."
tags: [apache-spark, skew, solucao]
aliases: [Solução Laboratório Otimização]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Diagnóstico de Skew e Partições

```python
from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder.master("local[2]").appName("skew-lab")
    .config("spark.sql.adaptive.enabled", "true").getOrCreate())
try:
    base = (spark.range(1_000_000, numPartitions=8)
        .withColumn("chave", F.when(F.col("id") < 800_000, F.lit(0))
            .otherwise(((F.col("id") - 800_000) % 100) + 1)))
    direto = base.groupBy("chave").agg(F.count("*").alias("n"))
    salgado = (base.withColumn("sal", F.when(F.col("chave") == 0, F.col("id") % 8).otherwise(F.lit(0)))
        .groupBy("chave", "sal").agg(F.count("*").alias("parcial"))
        .groupBy("chave").agg(F.sum("parcial").alias("n")))
    assert direto.exceptAll(salgado).isEmpty() and salgado.exceptAll(direto).isEmpty()
    total = salgado.agg(F.sum("n").alias("total")).first()["total"]
    assert total == 1_000_000 and salgado.count() == 101
    salgado.explain(mode="formatted")
    print("VALIDACAO_OK total=1000000 chaves=101")
finally:
    spark.stop()
```

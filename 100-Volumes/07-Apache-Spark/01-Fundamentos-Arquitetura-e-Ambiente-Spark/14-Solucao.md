---
title: Solução — Primeira Aplicação PySpark Observável
description: "Implementação de referência do laboratório."
tags: [pyspark, solucao, arquitetura]
aliases: [Solução Fundamentos Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Primeira Aplicação PySpark Observável

```python
from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder.master("local[2]")
    .appName("dataretail-primeiro-job")
    .config("spark.sql.session.timeZone", "UTC").getOrCreate())

try:
    pedidos = (spark.range(100_000, numPartitions=4)
        .withColumn("loja_id", F.col("id") % 10)
        .withColumn("valor_centavos", (F.col("id") % 5_000) + 100)
        .where(F.col("id") % 2 == 0))
    agregado = pedidos.groupBy("loja_id").agg(
        F.count("*").alias("pedidos"),
        F.sum("valor_centavos").alias("receita_centavos"))
    agregado.explain(mode="formatted")
    total = agregado.agg(F.sum("pedidos").alias("total")).first()["total"]
    assert total == 50_000
    lojas = agregado.count()
    assert lojas == 5
    print(f"VALIDACAO_OK total={total} lojas={lojas}")
finally:
    spark.stop()
```

Como IDs pares produzem apenas restos pares em `id % 10`, há cinco lojas. A escrita em arquivo fica como extensão porque, no Windows, ela também exige as ferramentas Hadoop nativas configuradas.

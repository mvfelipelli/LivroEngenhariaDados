---
title: Solução — Janelas e Watermarks com a Fonte Rate
description: "Implementação de referência para streaming local."
tags: [apache-spark, structured-streaming, solucao]
aliases: [Solução Laboratório Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Janelas e Watermarks com a Fonte Rate

```python
from time import sleep
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.master("local[2]").appName("rate-watermark").getOrCreate()
query = None
try:
    eventos = (spark.readStream.format("rate").option("rowsPerSecond", 100).load()
        .withColumn("loja_id", F.col("value") % 5))
    agregado = (eventos.withWatermark("timestamp", "10 seconds")
        .groupBy(F.window("timestamp", "5 seconds"), "loja_id").count())
    query = (agregado.writeStream.format("memory").queryName("receita_rate")
        .outputMode("complete").trigger(processingTime="2 seconds").start())
    for _ in range(15):
        sleep(1)
        if query.lastProgress and spark.table("receita_rate").select("loja_id").distinct().count() == 5:
            break
    lojas = spark.table("receita_rate").select("loja_id").distinct().count()
    assert lojas == 5 and query.lastProgress is not None
    print(f"VALIDACAO_OK lojas={lojas} batch={query.lastProgress['batchId']}")
finally:
    if query is not None:
        query.stop()
    spark.stop()
```

O memory sink é exclusivo para testes. Ele ainda utiliza checkpoint temporário; por isso, o Hadoop local precisa estar funcional no Windows. Produção deve configurar checkpoint explicitamente em armazenamento confiável e um sink durável.

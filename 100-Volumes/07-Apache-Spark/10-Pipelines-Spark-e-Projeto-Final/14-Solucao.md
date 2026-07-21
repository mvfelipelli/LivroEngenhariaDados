---
title: Solução — Pipeline Spark Integrado da DataRetail
description: "Implementação de referência do projeto final em memória."
tags: [apache-spark, projeto-final, solucao]
aliases: [Solução Projeto Final Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Pipeline Spark Integrado da DataRetail

```python
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.window import Window

def construir_mart(entrada, lojas):
    motivo = (F.when(F.col("pedido_id").isNull(), "id_nulo")
        .when(F.col("valor_centavos") < 0, "valor_negativo"))
    classificados = entrada.withColumn("motivo", motivo)
    validos = classificados.where(F.col("motivo").isNull())
    w = Window.partitionBy("pedido_id").orderBy(F.col("versao").desc(), F.col("id").desc())
    canonicos = validos.withColumn("rn", F.row_number().over(w)).where("rn = 1").drop("rn")
    base = canonicos.join(F.broadcast(lojas), "loja_id", "left")
    mart = (base.where(F.col("status") == "pago").groupBy("loja_id", "loja")
        .agg(F.count("*").alias("pedidos"), F.sum("valor_centavos").alias("receita_centavos")))
    return classificados, base, mart

spark = SparkSession.builder.master("local[2]").appName("projeto-final-spark").getOrCreate()
try:
    entrada = (spark.range(100_000, numPartitions=8)
        .withColumn("pedido_id", F.when(F.col("id") % 997 == 0, F.lit(None))
            .otherwise(F.concat(F.lit("P-"), (F.col("id") % 90_000))))
        .withColumn("versao", F.when(F.col("id") >= 90_000, F.lit(2)).otherwise(F.lit(1)))
        .withColumn("loja_id", F.col("id") % 10)
        .withColumn("valor_centavos", F.when(F.col("id") % 991 == 0, -1)
            .otherwise((F.col("id") % 5000) + 100))
        .withColumn("status", F.when(F.col("id") % 2 == 0, "pago").otherwise("pendente")))
    lojas = spark.range(10).select(F.col("id").alias("loja_id"),
        F.concat(F.lit("Loja "), F.col("id")).alias("loja"))
    classificados, base, mart = construir_mart(entrada, lojas)
    _, _, mart2 = construir_mart(entrada, lojas)
    assert classificados.count() == 100_000
    assert base.where(F.col("loja").isNull()).isEmpty()
    assert mart.count() == 5
    assert mart.exceptAll(mart2).isEmpty() and mart2.exceptAll(mart).isEmpty()
    mart.explain(mode="formatted")
    print("VALIDACAO_OK entrada=100000 lojas=5 orfaos=0")
finally:
    spark.stop()
```

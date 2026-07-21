---
title: Solução — Contrato e Testes de Pedidos
description: "Implementação de referência para qualidade testável."
tags: [apache-spark, testes, solucao]
aliases: [Solução Laboratório Confiabilidade]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Contrato e Testes de Pedidos

```python
from pyspark.sql import DataFrame, SparkSession, functions as F

def classificar_pedidos(df: DataFrame) -> DataFrame:
    motivo = (F.when(F.col("pedido_id").isNull(), "pedido_id_nulo")
        .when(F.col("valor_centavos") < 0, "valor_negativo"))
    return df.withColumn("motivo_quarentena", motivo)

spark = SparkSession.builder.master("local[2]").appName("contrato-pedidos").getOrCreate()
try:
    entrada = (spark.range(10_000, numPartitions=4)
        .withColumn("pedido_id", F.when(F.col("id") % 100 == 0, F.lit(None))
            .otherwise(F.concat(F.lit("P-"), F.col("id"))))
        .withColumn("valor_centavos", F.when(F.col("id") % 77 == 0, F.lit(-1))
            .otherwise((F.col("id") % 5000) + 1)))
    classificados = classificar_pedidos(entrada)
    validos = classificados.where(F.col("motivo_quarentena").isNull())
    quarentena = classificados.where(F.col("motivo_quarentena").isNotNull())
    total = entrada.count()
    assert validos.count() + quarentena.count() == total
    assert validos.where(F.col("pedido_id").isNull() | (F.col("valor_centavos") < 0)).isEmpty()
    assert classificados.exceptAll(classificar_pedidos(entrada)).isEmpty()
    print(f"VALIDACAO_OK entrada={total} reconciliado={validos.count() + quarentena.count()}")
finally:
    spark.stop()
```

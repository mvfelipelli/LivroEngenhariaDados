---
title: Solução — Publicação Particionada em Parquet
description: "Implementação de referência para I/O particionado."
tags: [apache-spark, parquet, solucao]
aliases: [Solução Laboratório I/O]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Publicação Particionada em Parquet

```python
from pathlib import Path
from shutil import rmtree
from pyspark.sql import SparkSession, functions as F

saida = Path("saida/pedidos")
spark = SparkSession.builder.master("local[2]").appName("io-parquet").getOrCreate()
try:
    df = (spark.range(20_000, numPartitions=4)
        .withColumn("data_negocio", F.when(F.col("id") % 2 == 0, "2026-07-19").otherwise("2026-07-20"))
        .withColumn("loja_id", F.col("id") % 10)
        .withColumn("valor_centavos", (F.col("id") % 100) + 1))
    if saida.exists():
        rmtree(saida)
    (df.repartition("data_negocio").write.mode("overwrite")
        .option("compression", "snappy").partitionBy("data_negocio").parquet(str(saida)))
    leitura = spark.read.parquet(str(saida)).where(F.col("data_negocio") == "2026-07-20")
    leitura.explain(mode="formatted")
    assert leitura.count() == 10_000
    assert len(list(saida.glob("data_negocio=*"))) == 2
    print("VALIDACAO_OK registros=10000 particoes=2")
finally:
    spark.stop()
```

Em armazenamento de objetos, substitua operações locais por uma estratégia de publicação compatível com as garantias do serviço.

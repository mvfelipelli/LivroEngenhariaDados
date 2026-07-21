---
title: Solução — Aplicação Empacotável e Configurável
description: "Implementação de referência para submissão Spark."
tags: [apache-spark, spark-submit, solucao]
aliases: [Solução Laboratório Operação]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Aplicação Empacotável e Configurável

`dataretail_spark/job.py`:

```python
from pyspark.sql import DataFrame, functions as F

def transformar(df: DataFrame, data_negocio: str) -> DataFrame:
    return (df.withColumn("data_negocio", F.lit(data_negocio))
        .withColumn("loja_id", F.col("id") % 10))
```

`app.py`:

```python
import argparse
from pyspark.sql import SparkSession
from dataretail_spark.job import transformar

p = argparse.ArgumentParser()
p.add_argument("--data-negocio", required=True)
p.add_argument("--linhas", type=int, required=True)
args = p.parse_args()
if args.linhas < 0:
    p.error("--linhas deve ser não negativo")

spark = SparkSession.builder.appName("dataretail-operacao").config(
    "spark.sql.session.timeZone", "UTC").getOrCreate()
try:
    saida = transformar(spark.range(args.linhas), args.data_negocio)
    assert saida.count() == args.linhas
    print(f"VALIDACAO_OK data={args.data_negocio} linhas={args.linhas}")
finally:
    spark.stop()
```

O master e os recursos permanecem no comando de submissão.

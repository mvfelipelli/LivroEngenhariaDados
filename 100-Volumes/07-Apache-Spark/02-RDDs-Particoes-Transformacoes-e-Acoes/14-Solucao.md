---
title: Solução — Agregação Particionada com RDDs
description: "Implementação de referência do laboratório de RDDs."
tags: [apache-spark, rdd, solucao]
aliases: [Solução Laboratório RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Agregação Particionada com RDDs

```python
from operator import add
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[2]").appName("dataretail-rdd").getOrCreate()
try:
    pedidos = spark.sparkContext.parallelize(range(10_000), 4)
    pares = pedidos.map(lambda i: (i % 10, (i % 100) + 1))
    totais = pares.reduceByKey(add, numPartitions=4)
    resultado = totais.collectAsMap()
    assert len(resultado) == 10
    assert sum(resultado.values()) == 505_000
    print(totais.toDebugString().decode("utf-8"))
    print("VALIDACAO_OK lojas=10 total=505000")
finally:
    spark.stop()
```

`collectAsMap` é seguro apenas porque o resultado contém dez chaves. Em produção, cardinalidade desconhecida deve permanecer distribuída.

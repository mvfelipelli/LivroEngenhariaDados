---
title: SparkSession, Configuração e Modos de Execução
description: "Ponto de entrada e execução local ou em cluster."
tags: [apache-spark, sparksession, configuracao]
aliases: [SparkSession]
created: 2026-07-20
updated: 2026-07-20
---

# SparkSession, Configuração e Modos de Execução

`SparkSession` é a entrada das APIs estruturadas. O master deve ser fornecido externamente em produção para não acoplar a aplicação ao ambiente.

```python
from pyspark.sql import SparkSession

spark = (SparkSession.builder
    .appName("dataretail-pedidos")
    .config("spark.sql.session.timeZone", "UTC")
    .getOrCreate())
```

`local[*]` usa threads locais. Em client mode, o driver permanece junto à submissão; em cluster mode, executa no cluster. Memória e executors pertencem preferencialmente ao `spark-submit` e à plataforma.

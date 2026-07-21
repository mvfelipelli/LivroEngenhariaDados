---
title: DataFrames, Rows, Colunas e Tipos
description: "Elementos da API estruturada e resolução de colunas."
tags: [apache-spark, dataframe, colunas]
aliases: [Colunas Spark]
created: 2026-07-20
updated: 2026-07-20
---

# DataFrames, Rows, Colunas e Tipos

DataFrame é uma coleção distribuída de `Row` descrita por `StructType`. Uma `Column` não contém valores locais: representa uma expressão que será resolvida no plano.

```python
from pyspark.sql import functions as F

resultado = pedidos.select(
    F.col("pedido_id"),
    (F.col("valor_centavos") / 100).alias("valor_reais"),
)
```

Tipos Spark não são idênticos aos tipos Python. `LongType`, `DecimalType`, `TimestampType` e `ArrayType` possuem semântica distribuída e de serialização. Para dinheiro, inteiros em centavos ou `DecimalType` evitam erros binários de `DoubleType`.

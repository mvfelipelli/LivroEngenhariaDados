---
title: Funções de Janela e Ordenação
description: "Rankings, acumulados, defasagens e frames."
tags: [apache-spark, window-functions, ordenacao]
aliases: [Janelas Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Funções de Janela e Ordenação

Janelas calculam valores relacionados sem reduzir linhas. A especificação contém particionamento lógico, ordenação e frame.

```python
from pyspark.sql.window import Window

w = Window.partitionBy("cliente_id").orderBy(F.col("instante").desc(), F.col("pedido_id").desc())
ultimo = pedidos.withColumn("rn", F.row_number().over(w)).where("rn = 1")
```

Inclua desempate estável; ordenar apenas por timestamp repetido torna `row_number` não determinístico. `rowsBetween` conta posições; `rangeBetween` usa faixa de valores. Janelas provocam reparticionamento e ordenação, exigindo atenção a skew e partições grandes.

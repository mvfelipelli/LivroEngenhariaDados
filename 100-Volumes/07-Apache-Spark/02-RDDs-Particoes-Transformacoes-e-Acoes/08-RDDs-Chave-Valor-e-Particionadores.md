---
title: RDDs Chave–Valor e Particionadores
description: "Agregações por chave, joins e preservação do particionamento."
tags: [apache-spark, pair-rdd, particionador]
aliases: [Pair RDD]
created: 2026-07-20
updated: 2026-07-20
---

# RDDs Chave–Valor e Particionadores

RDDs de pares habilitam `reduceByKey`, `aggregateByKey`, `join` e `partitionBy`. O particionador define qual partição recebe cada chave e pode ser preservado entre operações compatíveis.

```python
totais = (
    pedidos.map(lambda p: (p["loja_id"], p["valor_centavos"]))
    .reduceByKey(lambda a, b: a + b)
)
```

`reduceByKey` combina valores localmente antes do shuffle; `groupByKey` envia todos os valores e exige materializá-los por chave. Para somas, contagens e mínimos, a agregação prévia é preferível.

Chaves muito frequentes geram skew mesmo com bom hash. Salting, pré-agregação ou tratamento separado das chaves quentes podem distribuir o trabalho.

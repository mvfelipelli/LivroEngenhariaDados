---
title: JDBC, Bancos e Fontes Externas
description: "Leitura paralela sem sobrecarregar sistemas operacionais."
tags: [apache-spark, jdbc, bancos-de-dados]
aliases: [JDBC no Spark]
created: 2026-07-20
updated: 2026-07-20
---

# JDBC, Bancos e Fontes Externas

JDBC pode dividir leitura por uma coluna usando `partitionColumn`, `lowerBound`, `upperBound` e `numPartitions`. Os limites definem faixas, não um filtro de validade. A coluna deve distribuir bem e ser comparável.

```python
df = (spark.read.format("jdbc")
    .option("url", url).option("dbtable", "public.pedidos")
    .option("partitionColumn", "pedido_sk")
    .option("lowerBound", 1).option("upperBound", 10_000_000)
    .option("numPartitions", 8).load())
```

Mais partições significam mais conexões e carga no banco. Alinhe com limites do sistema fonte, use fetch size e empurre projeções/filtros seguros. Credenciais pertencem a secret manager, nunca ao código.

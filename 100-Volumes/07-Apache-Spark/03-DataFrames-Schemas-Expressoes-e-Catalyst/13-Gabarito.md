---
title: Gabarito — DataFrames e Catalyst
description: "Respostas dos exercícios do módulo."
tags: [apache-spark, dataframe, gabarito]
aliases: [Gabarito DataFrame Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. `StringType`, `TimestampType` e `DecimalType`, com nulabilidade definida pelo contrato.
2. `upper(trim(coalesce(col("uf"), lit("ND"))))`.
3. Row é registro; Column é expressão; DataFrame é relação distribuída tipada.
4. `upper(col("campo"))`.
5. `explode_outer("itens")`.
6. Parsed, analyzed, optimized e physical.
7. Contar entrada não nula, saída nula e amostra de valores rejeitados.
8. Adicionar campo nullable com padrão sem reinterpretar registros antigos; versionar produtores e consumidores.

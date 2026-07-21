---
title: Nulos, Duplicidade e Semântica ANSI
description: "Lógica ternária, comparações e falhas de conversão."
tags: [apache-spark, null, ansi-sql]
aliases: [Nulos no Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Nulos, Duplicidade e Semântica ANSI

SQL usa lógica de três valores: comparações com `NULL` resultam em desconhecido. Use `isNull`, `isNotNull` ou comparação null-safe `<=>` quando dois nulos devem corresponder.

`dropDuplicates` escolhe uma linha sem declarar qual sobreviverá. Para deduplicação determinística, ordene por versão, instante de ingestão e identificador de desempate em uma janela.

Com `spark.sql.ansi.enabled=true`, overflow e casts inválidos tendem a falhar em vez de gerar resultados silenciosos. A escolha deve ser consistente entre desenvolvimento e produção e acompanhada por quarentena de entradas inválidas.

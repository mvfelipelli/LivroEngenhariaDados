---
title: Introdução aos RDDs
description: "Modelo mental da abstração distribuída original do Spark."
tags: [apache-spark, rdd, introducao]
aliases: [Introdução RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Introdução

Um Resilient Distributed Dataset é uma coleção imutável dividida em partições. Cada transformação produz outro RDD; o Spark conserva dependências suficientes para recomputar partições perdidas.

```mermaid
flowchart LR
    R0["RDD de entrada"] --> M["map"]
    M --> F["filter"]
    F --> G["reduceByKey"]
    G --> A["collect/take/write"]
```

RDDs permitem lógica arbitrária, mas não informam ao otimizador o significado das colunas. Para dados estruturados, [[03-DataFrames-Schemas-Expressoes-e-Catalyst/README|DataFrames]] oferecem planos mais ricos e normalmente melhores resultados.

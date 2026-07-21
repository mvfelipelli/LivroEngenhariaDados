---
title: Estudo de Caso — Conciliação por Loja com RDDs
description: "Análise de partições e agregação na DataRetail S.A."
tags: [apache-spark, rdd, dataretail]
aliases: [Caso DataRetail RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — Conciliação por Loja

A DataRetail precisa conciliar registros legados sem schema uniforme. Cada linha é validada por um parser específico e convertida em `(loja_id, valor_centavos)`. A flexibilidade justifica RDD na borda; após normalização, os dados migram para DataFrame.

`reduceByKey` soma valores antes do shuffle. Registros inválidos são enviados a uma saída de quarentena, sem acumulá-los no driver. Métricas por partição revelam duas lojas com volume desproporcional.

```mermaid
flowchart LR
    L["Linhas legadas"] --> P["Parser por partição"]
    P --> V["Pares válidos"]
    P --> Q["Quarentena"]
    V --> R["reduceByKey"]
    R --> D["DataFrame normalizado"]
```

A solução limita a API RDD à etapa que realmente precisa de objetos arbitrários.

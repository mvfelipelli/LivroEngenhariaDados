---
title: Estudo de Caso — Receita e Recorrência da DataRetail
description: "Joins, agregações e janelas em um mart comercial."
tags: [apache-spark, spark-sql, dataretail]
aliases: [Caso DataRetail Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — Receita e Recorrência

A DataRetail consolida pedidos pagos, dimensão de lojas e histórico de clientes. A dimensão é validada como única por `loja_id` e transmitida por broadcast. A receita diária é agregada em centavos.

Uma janela por cliente, ordenada por instante e pedido, calcula pedido anterior e dias desde a última compra. Outra janela seleciona o cadastro vigente de cada loja.

```mermaid
flowchart LR
    P["Pedidos pagos"] --> J["Join com lojas"]
    L["Dimensão lojas"] --> J
    J --> A["Receita diária"]
    J --> W["Janela por cliente"]
    A --> M["Mart comercial"]
    W --> M
```

Reconciliações garantem que o join não multiplique pedidos e que a soma publicada coincida com a origem válida.

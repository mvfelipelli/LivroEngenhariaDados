---
title: Estudo de Caso — Normalização de Eventos da DataRetail
description: "Schema explícito e transformação de pedidos aninhados."
tags: [apache-spark, dataframe, dataretail]
aliases: [Caso DataRetail DataFrame]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — Normalização de Eventos

Eventos de checkout chegam com pedido, cliente e itens aninhados. A DataRetail define schema explícito, preserva o evento bruto para auditoria e cria duas relações: pedidos e itens.

```mermaid
flowchart LR
    J["JSON aninhado"] --> S["Schema explícito"]
    S --> V["Validação"]
    V --> P["Pedidos"]
    V --> E["explode_outer de itens"]
    E --> I["Itens"]
    V --> Q["Quarentena"]
```

Expressões nativas normalizam UF, datas e valores. Registros sem `pedido_id` vão à quarentena. Métricas contabilizam entrada, válidos, inválidos e itens produzidos, garantindo reconciliação.

---
title: Estudo de Caso — Evolução de Pedidos na DataRetail
description: "Renomeação sem indisponibilidade e backfill controlado."
tags: [dataretail, sql, migration, estudo-de-caso]
aliases: [Caso DataRetail Evolução de Schema]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

A DataRetail S.A. precisa substituir `valor` por `valor_centavos`, eliminando ambiguidade de moeda sem interromper APIs e pipelines antigos.

O time adiciona a coluna opcional, publica escritor duplo e executa backfill por `pedido_id`. Uma reconciliação verifica `valor_centavos = ROUND(valor * 100)`.

```mermaid
sequenceDiagram
    participant DB
    participant V1 as Aplicação antiga
    participant V2 as Aplicação nova
    DB->>DB: adiciona valor_centavos
    V2->>DB: grava ambas
    DB->>DB: backfill em lotes
    V2->>DB: lê nova coluna
    V1->>DB: ainda lê valor
    DB->>DB: remove legado após adoção
```

O `NOT NULL` só é aplicado após contagem de nulos igual a zero. Dashboards e CDC são migrados antes da contração. O rollback de aplicação permanece possível durante toda a expansão.

Métricas acompanham lotes, divergências, locks e lag. A remoção ocorre semanas depois, com evidência de ausência de leitores antigos.

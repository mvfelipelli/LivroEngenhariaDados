---
title: Estudo de Caso — Agregação de Pedidos da DataRetail
description: "Escolha de tipos e coleções para consolidação comercial."
tags: [python, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Coleções]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

A DataRetail precisa consolidar pedidos de vários canais. Cada evento possui `pedido_id`, `loja`, `status` e `valor_centavos`. Reenvios podem duplicar um pedido.

A equipe adotou:

- `dict` indexado por `pedido_id` para deduplicação;
- inteiro em centavos para valores monetários;
- `set` para medir lojas distintas;
- outro `dict` para totais por loja;
- lista ordenada com desempate explícito para publicação.

```mermaid
flowchart LR
    E["Eventos"] --> D["Deduplicar por pedido"]
    D --> F["Filtrar aprovados"]
    F --> A["Agregar por loja"]
    A --> R["Ranking determinístico"]
```

Eventos inválidos são rejeitados antes da agregação. A política escolhe a maior versão do pedido, em vez de depender da ordem de chegada. Assim, uma reexecução com a mesma entrada produz exatamente o mesmo resultado.

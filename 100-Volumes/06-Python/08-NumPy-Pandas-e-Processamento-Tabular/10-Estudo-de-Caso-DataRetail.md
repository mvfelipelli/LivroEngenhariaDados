---
title: Estudo de Caso — Mart de Vendas da DataRetail
description: "Deduplicação, join, agregação e reconciliação tabular."
tags: [python, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Pandas]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

A DataRetail recebe versões de pedidos e itens. O mart deve usar a maior versão aprovada, enriquecer produtos e totalizar por loja.

Controles adotados:

- dtypes string e inteiros nullable;
- timestamp UTC;
- ordenação e deduplicação por ID/versão;
- filtro de aprovados antes do join;
- `many_to_one` entre itens e produtos;
- rejeição de produto desconhecido;
- groupby com grão loja;
- reconciliação entre itens aprovados e mart.

```mermaid
flowchart LR
    P["Versões de pedidos"] --> D["Deduplicar"]
    D --> F["Aprovados"]
    I["Itens"] --> J["Join por pedido"]
    F --> J
    J --> G["Agregação por loja"]
    G --> R["Reconciliação"]
```

O join é auditado com indicador para que linhas órfãs não desapareçam silenciosamente.

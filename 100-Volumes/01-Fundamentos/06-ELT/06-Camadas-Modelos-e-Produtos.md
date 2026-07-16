---
title: Camadas, Modelos e Produtos
aliases: [ELT Layers and Models]
tags: [engenharia-de-dados, fundamentos, elt, camadas, marts]
type: chapter
order: 06
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Organização de raw, staging, intermediários e produtos de dados."
---

# 06 — Camadas, Modelos e Produtos

## Responsabilidades

| Camada | Responsabilidade |
| --- | --- |
| Raw | evidência próxima da fonte |
| Staging | tipos, nomes, deduplicação e limpeza local |
| Intermediate | regras reutilizáveis e integrações |
| Mart | fatos, dimensões e produtos orientados ao consumo |

Camadas são contratos, não obrigação de copiar fisicamente todos os dados. Uma view pode representar staging; uma tabela incremental pode materializar um mart.

## Princípios

- uma fonte entra uma vez e é reutilizada;
- staging não contém regra de métrica corporativa;
- intermediários evitam duplicar joins;
- marts declaram grão e consumidor;
- exposição ocorre somente por interfaces governadas.

## Grafo

```mermaid
flowchart LR
    A[raw_orders] --> B[stg_orders]
    C[raw_items] --> D[stg_items]
    B --> E[int_confirmed_orders]
    D --> E
    E --> F[fct_sales]
```

## Próximo Capítulo

➡️ [[07-Incrementalidade-e-Materializacoes|07 — Incrementalidade e Materializações]]

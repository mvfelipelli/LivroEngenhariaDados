---
title: Estudo de Caso — ELT da DataRetail
aliases: [DataRetail ELT Case Study]
tags: [engenharia-de-dados, fundamentos, elt, estudo-de-caso, dataretail]
type: case-study
order: 10
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Arquitetura ELT governada para vendas da DataRetail S.A."
---

# 10 — Estudo de Caso DataRetail

## Cenário

Pedidos de três canais chegam à plataforma analítica. Finanças e operações precisam de produtos distintos, mas com definições conformadas.

## Arquitetura

```mermaid
flowchart LR
    A[CDC e arquivos] --> B[raw_orders]
    B --> C[stg_orders]
    C --> D[int_order_items]
    D --> E[fct_sales]
    D --> F[fct_operations]
    E --> G[Financeiro]
    F --> H[Operações]
```

## Contratos

Raw preserva payload e metadados. Staging padroniza UTC, decimal e chaves. `fct_sales` possui grão de item confirmado; cancelamentos continuam em operações.

## Incremental

Modelos reprocessam 24 horas e fazem merge por `(source, order_id, line_number)`. Snapshot versiona categoria de produto. Full refresh mensal compara equivalência.

## Testes

Unicidade, não nulos, referências, status aceitos, líquido não negativo, reconciliação por dia e atualidade até 7h.

## Incidente

Um analista consultou raw e somou versões duplicadas. O acesso foi restringido, o mart passou a ser interface oficial e a documentação destacou grão e política de versão.

## Aceite

- produtos compartilham dimensões conformadas;
- raw não é exposto ao BI;
- modelos são reconstruíveis;
- incremental equivale ao full refresh;
- custo e linhagem são atribuíveis.

## Próximo Capítulo

➡️ [[11-Resumo|11 — Resumo]]

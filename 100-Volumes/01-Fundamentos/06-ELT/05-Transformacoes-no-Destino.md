---
title: Transformações no Destino
aliases: [In-Warehouse Transformations]
tags: [engenharia-de-dados, fundamentos, elt, sql, transformacao]
type: chapter
order: 05
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "SQL modular, dependências e regras para transformações ELT."
---

# 05 — Transformações no Destino

SQL dentro da plataforma torna a lógica próxima aos dados, mas precisa ser tratada como software: modular, versionada, testável e revisada.

## Modelo modular

Um modelo deve ter propósito e grão claros. Evite uma única query que mistura limpeza, integração e regra de negócio.

```sql
SELECT
    source_system,
    order_id,
    line_number,
    CAST(quantity AS INTEGER) AS quantity,
    CAST(unit_price AS NUMERIC) AS unit_price
FROM raw_order_items
WHERE is_deleted = 0;
```

## Dependências

Referencie modelos estáveis, não tabelas físicas acidentais. O grafo deve impedir ciclos e ordenar staging antes de marts.

## Determinismo

Declare ordem em funções de janela, timezone, precisão e precedência de deduplicação. `ROW_NUMBER()` sem desempate estável produz resultados variáveis.

## Contratos

Cada modelo publica colunas, tipos, grão, chaves, atualidade e política de mudança. SQL válido não garante semântica correta.

## Próximo Capítulo

➡️ [[06-Camadas-Modelos-e-Produtos|06 — Camadas, Modelos e Produtos]]

---
title: SELECT, Projeção, Aliases e Ordem Lógica
description: "Construção e interpretação de consultas fundamentais."
tags: [sql, select, projecao, aliases]
aliases: [Fundamentos do SELECT]
created: 2026-07-17
updated: 2026-07-17
---

# SELECT, Projeção, Aliases e Ordem Lógica

`SELECT` constrói colunas resultantes; `FROM` define fontes. Embora `SELECT` apareça primeiro na sintaxe, a fonte é conceitualmente formada antes da projeção.

```sql
SELECT
    p.pedido_id,
    p.valor,
    p.valor * 0.05 AS cashback
FROM pedidos AS p;
```

Aliases nomeiam relações ou expressões e melhoram legibilidade. Evite `SELECT *` em contratos e pipelines: mudanças de schema alteram forma, ordem e volume do resultado.

```mermaid
flowchart LR
    F["FROM"] --> W["WHERE"]
    W --> G["GROUP BY"]
    G --> H["HAVING"]
    H --> S["SELECT"]
    S --> D["DISTINCT"]
    D --> O["ORDER BY"]
```

Essa ordem lógica explica por que muitos dialetos não aceitam um alias de `SELECT` em `WHERE`: o alias ainda não existe nessa etapa.

Constantes também podem ser consultadas:

```sql
SELECT 2 + 3 AS resultado;
```

Um resultado sem `ORDER BY` não possui ordem garantida, mesmo que pareça estável em testes pequenos.

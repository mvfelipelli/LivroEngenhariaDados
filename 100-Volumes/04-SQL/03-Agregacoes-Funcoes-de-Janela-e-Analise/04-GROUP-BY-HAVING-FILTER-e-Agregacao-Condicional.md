---
title: GROUP BY, HAVING, FILTER e Agregação Condicional
description: "Formação de grupos e critérios em diferentes etapas lógicas."
tags: [sql, group-by, having, filter]
aliases: [GROUP BY e HAVING]
created: 2026-07-17
updated: 2026-07-17
---

# GROUP BY, HAVING, FILTER e Agregação Condicional

`GROUP BY` define uma linha resultante por combinação de chaves. `WHERE` filtra antes da agregação; `HAVING`, depois.

```sql
SELECT cliente_id, SUM(valor) AS total
FROM pedidos
WHERE status = 'pago'
GROUP BY cliente_id
HAVING SUM(valor) >= 500;
```

Agregação condicional calcula várias métricas na mesma população:

```sql
SELECT
    cliente_id,
    SUM(CASE WHEN status = 'pago' THEN valor ELSE 0 END) AS pago,
    SUM(CASE WHEN status = 'cancelado' THEN 1 ELSE 0 END) AS cancelados
FROM pedidos
GROUP BY cliente_id;
```

Quando suportado, `FILTER` separa condição da expressão:

```sql
COUNT(*) FILTER (WHERE status = 'cancelado')
```

```mermaid
flowchart LR
    W["WHERE: linhas"] --> G["GROUP BY"]
    G --> A["Agregações"]
    A --> H["HAVING: grupos"]
```

Colunas selecionadas que não são agregadas precisam integrar o agrupamento ou depender funcionalmente dele segundo regras do dialeto. Evite confiar em extensões permissivas.

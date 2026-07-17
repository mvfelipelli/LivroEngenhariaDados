---
title: Funções de Janela, Partições, Ordem e Peers
description: "Cálculos sobre conjuntos relacionados preservando linhas."
tags: [sql, window-functions, partition-by, peers]
aliases: [Fundamentos de Window Functions]
created: 2026-07-17
updated: 2026-07-17
---

# Funções de Janela, Partições, Ordem e Peers

Uma função de janela é identificada por `OVER`. `PARTITION BY` separa conjuntos independentes; `ORDER BY` define sequência dentro deles.

```sql
SELECT
    pedido_id,
    cliente_id,
    valor,
    SUM(valor) OVER (PARTITION BY cliente_id) AS total_cliente
FROM pedidos;
```

As linhas permanecem. Sem `PARTITION BY`, todas formam uma partição. Sem ordenação, funções dependentes de sequência não têm resultado determinístico.

```mermaid
flowchart LR
    R["Resultado após WHERE/GROUP BY"] --> P["PARTITION BY"]
    P --> O["ORDER BY"]
    O --> F["Frame"]
    F --> C["Cálculo por linha"]
```

Peers são linhas empatadas nas expressões de ordenação da janela. Rankings e frames `RANGE` tratam peers de modo específico.

Funções de janela são logicamente avaliadas depois de `WHERE`, `GROUP BY` e `HAVING`, por isso geralmente só aparecem em `SELECT` e `ORDER BY`. Para filtrar um ranking, use subconsulta ou CTE.

> [!note]
> O `ORDER BY` dentro de `OVER` governa o cálculo; o `ORDER BY` externo governa a apresentação final.

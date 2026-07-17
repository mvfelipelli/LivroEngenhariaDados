---
title: Ranking — ROW_NUMBER, RANK e NTILE
description: "Ordenação analítica, empates e segmentação."
tags: [sql, row-number, rank, dense-rank, ntile]
aliases: [Ranking SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Ranking: ROW_NUMBER, RANK e NTILE

`ROW_NUMBER` atribui sequência única; `RANK` preserva empates e deixa lacunas; `DENSE_RANK` preserva empates sem lacunas. `NTILE(n)` distribui linhas ordenadas em grupos aproximadamente equilibrados.

```sql
WITH classificados AS (
    SELECT
        cliente_id,
        pedido_id,
        valor,
        ROW_NUMBER() OVER (
            PARTITION BY cliente_id
            ORDER BY valor DESC, pedido_id
        ) AS posicao
    FROM pedidos
)
SELECT * FROM classificados WHERE posicao <= 3;
```

```mermaid
flowchart LR
    O["Ordenação por valor"] --> P["Peers empatados"]
    P --> N["ROW_NUMBER: únicos"]
    P --> R["RANK: lacunas"]
    P --> D["DENSE_RANK: sem lacunas"]
```

Inclua uma chave estável para desempatar `ROW_NUMBER`. Sem ela, o conjunto top N pode variar.

`NTILE(4)` cria quartis por quantidade de linhas, não percentis estatísticos exatos. Distribuições com muitos empates exigem interpretação cuidadosa.

Escolha a função pela regra de negócio: “três linhas” pede `ROW_NUMBER`; “três melhores posições incluindo empates” pede `RANK` ou `DENSE_RANK`.

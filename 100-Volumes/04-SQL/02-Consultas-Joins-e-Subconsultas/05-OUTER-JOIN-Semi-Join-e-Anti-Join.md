---
title: OUTER JOIN, Semi-join e Anti-join
description: "Preservação de ausência e testes de existência."
tags: [sql, outer-join, semi-join, anti-join]
aliases: [Outer e Anti Join]
created: 2026-07-17
updated: 2026-07-17
---

# OUTER JOIN, Semi-join e Anti-join

`LEFT JOIN` preserva todas as linhas da esquerda e completa colunas da direita com `NULL` quando não existe correspondência.

```sql
SELECT c.cliente_id, p.pedido_id
FROM clientes AS c
LEFT JOIN pedidos AS p
    ON p.cliente_id = c.cliente_id
   AND p.status = 'pago';
```

Mover `p.status = 'pago'` para `WHERE` eliminaria clientes sem pedido pago. Predicados em `ON` definem correspondência; em `WHERE`, filtram o resultado formado.

Semi-join pergunta se existe ao menos uma correspondência, sem duplicar a linha externa:

```sql
SELECT c.cliente_id, c.nome
FROM clientes AS c
WHERE EXISTS (
    SELECT 1 FROM pedidos AS p WHERE p.cliente_id = c.cliente_id
);
```

Trocar por `NOT EXISTS` implementa anti-join e encontra ausência.

```mermaid
flowchart LR
    C["Clientes"] --> E["EXISTS pedido?"]
    E --> S["Sim: compradores"]
    E --> N["Não: sem pedidos"]
```

Prefira `NOT EXISTS` a `NOT IN` quando a subconsulta puder produzir `NULL`, pois a lógica de três valores pode tornar o predicado desconhecido.

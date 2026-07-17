---
title: Solução — Composição Relacional sem Fanout
description: "Implementação SQLite validada do laboratório."
tags: [sql, sqlite, joins, solucao]
aliases: [Solução Laboratório Joins]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Composição Relacional sem Fanout

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript(
    """
    CREATE TABLE pedidos (pedido_id INTEGER PRIMARY KEY, cliente_id INTEGER NOT NULL);
    CREATE TABLE itens (item_id INTEGER PRIMARY KEY, pedido_id INTEGER, valor NUMERIC);
    CREATE TABLE pagamentos (pagamento_id INTEGER PRIMARY KEY, pedido_id INTEGER, valor NUMERIC);
    CREATE TABLE categorias (categoria_id INTEGER PRIMARY KEY, pai_id INTEGER, nome TEXT);

    INSERT INTO pedidos VALUES (1, 10), (2, 10), (3, 20);
    INSERT INTO itens VALUES (1, 1, 100), (2, 1, 50), (3, 2, 40), (4, 3, 200);
    INSERT INTO pagamentos VALUES (1, 1, 120), (2, 1, 30), (3, 3, 190);
    INSERT INTO categorias VALUES (1, NULL, 'Loja'), (2, 1, 'Eletronicos'), (3, 2, 'Audio');
    """
)

report = db.execute(
    """
    WITH item_totals AS (
        SELECT pedido_id, SUM(valor) AS total_itens
        FROM itens GROUP BY pedido_id
    ), payment_totals AS (
        SELECT pedido_id, SUM(valor) AS total_pago
        FROM pagamentos GROUP BY pedido_id
    )
    SELECT p.pedido_id, i.total_itens, COALESCE(pg.total_pago, 0)
    FROM pedidos AS p
    JOIN item_totals AS i ON i.pedido_id = p.pedido_id
    LEFT JOIN payment_totals AS pg ON pg.pedido_id = p.pedido_id
    ORDER BY p.pedido_id
    """
).fetchall()

unpaid = db.execute(
    """
    SELECT COUNT(*) FROM pedidos AS p
    WHERE NOT EXISTS (
        SELECT 1 FROM pagamentos AS pg WHERE pg.pedido_id = p.pedido_id
    )
    """
).fetchone()[0]

tree = db.execute(
    """
    WITH RECURSIVE arvore(categoria_id, nome, profundidade) AS (
        SELECT categoria_id, nome, 1 FROM categorias WHERE pai_id IS NULL
        UNION ALL
        SELECT c.categoria_id, c.nome, a.profundidade + 1
        FROM categorias AS c
        JOIN arvore AS a ON c.pai_id = a.categoria_id
    )
    SELECT categoria_id, nome, profundidade FROM arvore ORDER BY profundidade
    """
).fetchall()

assert len(report) == len({row[0] for row in report}) == 3
assert sum(float(row[1]) for row in report) == 390.0
assert sum(float(row[2]) for row in report) == 340.0
assert unpaid == 1
assert [row[2] for row in tree] == [1, 2, 3]

print(f"pedidos={len(report)}")
print("grao=unico")
print(f"total_itens={sum(float(row[1]) for row in report):.2f}")
print(f"total_pago={sum(float(row[2]) for row in report):.2f}")
print(f"sem_pagamento={unpaid}")
print(f"hierarquia={len(tree)}")
print("composicao=ok")
db.close()
```

As CTEs reduzem cada relação filha a uma linha por pedido antes da composição. O anti-join e a recursão são validados separadamente.

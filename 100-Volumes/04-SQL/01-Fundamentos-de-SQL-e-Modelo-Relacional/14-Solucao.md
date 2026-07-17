---
title: Solução — Consultas Fundamentais da DataRetail
description: "Implementação SQLite validada do laboratório."
tags: [sql, sqlite, laboratorio, solucao]
aliases: [Solução Laboratório Fundamentos SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Consultas Fundamentais da DataRetail

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
connection.executescript(
    """
    CREATE TABLE clientes (
        cliente_id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cidade TEXT,
        ativo INTEGER NOT NULL CHECK (ativo IN (0, 1))
    );

    CREATE TABLE pedidos (
        pedido_id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL REFERENCES clientes(cliente_id),
        valor NUMERIC NOT NULL CHECK (valor >= 0)
    );

    INSERT INTO clientes VALUES
        (1, 'Ana', 'Recife', 1),
        (2, 'Bruno', 'Sao Paulo', 1),
        (3, 'Carla', NULL, 0);

    INSERT INTO pedidos VALUES
        (101, 1, 150.00),
        (102, 1, 200.00),
        (103, 2, 90.00);
    """
)

report = connection.execute(
    """
    SELECT
        c.cliente_id,
        c.nome,
        COUNT(p.pedido_id) AS quantidade,
        COALESCE(SUM(p.valor), 0) AS total
    FROM clientes AS c
    LEFT JOIN pedidos AS p ON p.cliente_id = c.cliente_id
    GROUP BY c.cliente_id, c.nome
    ORDER BY total DESC, c.cliente_id
    """
).fetchall()

clients = connection.execute("SELECT COUNT(*) FROM clientes").fetchone()[0]
orders = connection.execute("SELECT COUNT(*) FROM pedidos").fetchone()[0]
without_orders = sum(1 for row in report if row[2] == 0)
leader = report[0]

assert clients == 3 and orders == 3
assert without_orders == 1
assert leader[1] == "Ana" and float(leader[3]) == 350.0
assert report[-1][1] == "Carla" and report[-1][3] == 0

try:
    connection.execute("INSERT INTO pedidos VALUES (104, 1, -1)")
    raise AssertionError("constraint_nao_aplicada")
except sqlite3.IntegrityError:
    pass

print(f"clientes={clients}")
print(f"pedidos={orders}")
print(f"sem_pedidos={without_orders}")
print(f"lider={leader[1]}:{float(leader[3]):.2f}")
print("integridade=ok")
print("consulta=ok")
connection.close()
```

O banco existe somente durante a conexão. As assertions validam cardinalidade, `LEFT JOIN`, agregação, ordenação e constraint.

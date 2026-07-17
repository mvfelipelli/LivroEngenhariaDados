---
title: Solução — Do Domínio ao Esquema Validado
description: "Implementação validada do modelo fundamental no SQLite."
tags: [modelagem-de-dados, sqlite, solucao]
aliases: [Solução Laboratório Fundamentos de Modelagem]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Do Domínio ao Esquema Validado

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript(
    """
    CREATE TABLE cliente (
        cliente_id INTEGER PRIMARY KEY,
        documento TEXT NOT NULL UNIQUE
    );
    CREATE TABLE pedido (
        pedido_id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL REFERENCES cliente(cliente_id),
        criado_em TEXT NOT NULL
    );
    CREATE TABLE item_pedido (
        pedido_id INTEGER NOT NULL REFERENCES pedido(pedido_id),
        numero_item INTEGER NOT NULL,
        produto_codigo TEXT NOT NULL,
        quantidade INTEGER NOT NULL CHECK (quantidade > 0),
        preco_centavos INTEGER NOT NULL CHECK (preco_centavos >= 0),
        PRIMARY KEY (pedido_id, numero_item)
    );
    INSERT INTO cliente VALUES (1, 'DOC-001');
    INSERT INTO pedido VALUES (100, 1, '2026-07-17T12:00:00Z');
    INSERT INTO item_pedido VALUES
        (100, 1, 'A', 2, 1000),
        (100, 2, 'B', 1, 1500);
    """
)

def deve_rejeitar(sql, parametros):
    try:
        db.execute(sql, parametros)
        raise AssertionError("invariante_nao_aplicada")
    except sqlite3.IntegrityError:
        return "rejeitada"

quantidade = deve_rejeitar(
    "INSERT INTO item_pedido VALUES (?, ?, ?, ?, ?)",
    (100, 3, "C", 0, 100),
)
duplicado = deve_rejeitar(
    "INSERT INTO item_pedido VALUES (?, ?, ?, ?, ?)",
    (100, 1, "C", 1, 100),
)
referencia = deve_rejeitar(
    "INSERT INTO pedido VALUES (?, ?, ?)",
    (101, 999, "2026-07-17T13:00:00Z"),
)

clientes = db.execute("SELECT COUNT(*) FROM cliente").fetchone()[0]
pedidos = db.execute("SELECT COUNT(*) FROM pedido").fetchone()[0]
itens, total = db.execute(
    "SELECT COUNT(*), SUM(quantidade * preco_centavos) FROM item_pedido"
).fetchone()
assert (clientes, pedidos, itens, total) == (1, 1, 2, 3500)

print(f"clientes={clientes}")
print(f"pedidos={pedidos}")
print(f"itens={itens}")
print(f"total_centavos={total}")
print(f"quantidade_invalida={quantidade}")
print(f"item_duplicado={duplicado}")
print(f"referencia_invalida={referencia}")
print("modelo=ok")
db.close()
```

O esquema físico materializa identidade, relacionamento e invariantes definidos no domínio. Os testes negativos comprovam que estados inválidos não são persistidos.

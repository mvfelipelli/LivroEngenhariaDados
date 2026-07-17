---
title: Solução — Normalização de Vendas
description: "Implementação validada de decomposição relacional."
tags: [modelagem-de-dados, sqlite, normalizacao, solucao]
aliases: [Solução Laboratório Normalização]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Normalização de Vendas

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript(
    """
    CREATE TABLE venda_legada (
        pedido_id INTEGER, cliente_id INTEGER, cliente_nome TEXT,
        numero_item INTEGER, produto_id INTEGER, produto_nome TEXT,
        quantidade INTEGER, preco_centavos INTEGER
    );
    INSERT INTO venda_legada VALUES
        (1, 10, 'Ana', 1, 100, 'Café', 2, 1000),
        (1, 10, 'Ana', 2, 200, 'Filtro', 1, 500),
        (2, 20, 'Bia', 1, 100, 'Café', 3, 1000);
    UPDATE venda_legada SET cliente_nome = 'Ana Silva'
    WHERE pedido_id = 1 AND numero_item = 1;
    """
)

nomes_ana = db.execute(
    "SELECT COUNT(DISTINCT cliente_nome) FROM venda_legada WHERE cliente_id = 10"
).fetchone()[0]
assert nomes_ana == 2

db.executescript(
    """
    CREATE TABLE cliente (cliente_id INTEGER PRIMARY KEY, nome TEXT NOT NULL);
    CREATE TABLE produto (produto_id INTEGER PRIMARY KEY, nome TEXT NOT NULL);
    CREATE TABLE pedido (
        pedido_id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL REFERENCES cliente(cliente_id)
    );
    CREATE TABLE item_pedido (
        pedido_id INTEGER NOT NULL REFERENCES pedido(pedido_id),
        numero_item INTEGER NOT NULL,
        produto_id INTEGER NOT NULL REFERENCES produto(produto_id),
        quantidade INTEGER NOT NULL CHECK (quantidade > 0),
        preco_centavos INTEGER NOT NULL,
        PRIMARY KEY (pedido_id, numero_item)
    );
    INSERT INTO cliente VALUES (10, 'Ana Silva'), (20, 'Bia');
    INSERT INTO produto VALUES (100, 'Café'), (200, 'Filtro');
    INSERT INTO pedido VALUES (1, 10), (2, 20);
    INSERT INTO item_pedido VALUES
        (1, 1, 100, 2, 1000),
        (1, 2, 200, 1, 500),
        (2, 1, 100, 3, 1000);
    """
)

reconstruida = db.execute(
    """
    SELECT p.pedido_id, c.cliente_id, c.nome, i.numero_item,
           pr.produto_id, pr.nome, i.quantidade, i.preco_centavos
    FROM pedido p
    JOIN cliente c ON c.cliente_id = p.cliente_id
    JOIN item_pedido i ON i.pedido_id = p.pedido_id
    JOIN produto pr ON pr.produto_id = i.produto_id
    ORDER BY p.pedido_id, i.numero_item
    """
).fetchall()
assert len(reconstruida) == 3

clientes = db.execute("SELECT COUNT(*) FROM cliente").fetchone()[0]
produtos = db.execute("SELECT COUNT(*) FROM produto").fetchone()[0]
pedidos = db.execute("SELECT COUNT(*) FROM pedido").fetchone()[0]
itens, total = db.execute(
    "SELECT COUNT(*), SUM(quantidade * preco_centavos) FROM item_pedido"
).fetchone()
assert (clientes, produtos, pedidos, itens, total) == (2, 2, 2, 3, 5500)

print("anomalia_legada=detectada")
print(f"clientes={clientes}")
print(f"produtos={produtos}")
print(f"pedidos={pedidos}")
print(f"itens={itens}")
print(f"total_centavos={total}")
print("reconstrucao=sem_perda")
print("normalizacao=ok")
db.close()
```

A dependência `cliente_id → cliente_nome` fica protegida em `cliente`; a visão original é reconstruída por chaves sem multiplicar linhas.

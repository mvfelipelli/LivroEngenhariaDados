---
title: Solução — Modelo Conceitual de Marketplace
description: "Implementação validada do laboratório ER no SQLite."
tags: [modelagem-de-dados, sqlite, solucao, er]
aliases: [Solução Laboratório Modelo ER]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Modelo Conceitual de Marketplace

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript(
    """
    CREATE TABLE vendedor (vendedor_id INTEGER PRIMARY KEY, nome TEXT NOT NULL);
    CREATE TABLE produto (produto_id INTEGER PRIMARY KEY, nome TEXT NOT NULL);
    CREATE TABLE oferta (
        oferta_id INTEGER PRIMARY KEY,
        vendedor_id INTEGER NOT NULL REFERENCES vendedor(vendedor_id),
        produto_id INTEGER NOT NULL REFERENCES produto(produto_id),
        codigo_vendedor TEXT NOT NULL,
        preco_centavos INTEGER NOT NULL CHECK (preco_centavos >= 0),
        UNIQUE (vendedor_id, codigo_vendedor)
    );
    CREATE TABLE pedido (pedido_id INTEGER PRIMARY KEY);
    CREATE TABLE item_pedido (
        pedido_id INTEGER NOT NULL REFERENCES pedido(pedido_id),
        numero_item INTEGER NOT NULL,
        oferta_id INTEGER NOT NULL REFERENCES oferta(oferta_id),
        quantidade INTEGER NOT NULL CHECK (quantidade > 0),
        preco_praticado_centavos INTEGER NOT NULL,
        PRIMARY KEY (pedido_id, numero_item)
    );
    INSERT INTO vendedor VALUES (1, 'Loja A'), (2, 'Loja B');
    INSERT INTO produto VALUES (10, 'Cafeteira');
    INSERT INTO oferta VALUES
        (100, 1, 10, 'CAF-1', 2500),
        (200, 2, 10, 'CF-9', 2600);
    INSERT INTO pedido VALUES (1000);
    INSERT INTO item_pedido VALUES
        (1000, 1, 100, 1, 2500),
        (1000, 2, 200, 1, 2600);
    """
)

def rejeitar(sql, parametros):
    try:
        db.execute(sql, parametros)
        raise AssertionError("regra_nao_aplicada")
    except sqlite3.IntegrityError:
        return "rejeitada"

duplicada = rejeitar(
    "INSERT INTO oferta VALUES (?, ?, ?, ?, ?)",
    (300, 1, 10, "CAF-1", 2400),
)
referencia = rejeitar(
    "INSERT INTO item_pedido VALUES (?, ?, ?, ?, ?)",
    (1000, 3, 999, 1, 100),
)

vendedores = db.execute("SELECT COUNT(*) FROM vendedor").fetchone()[0]
produtos = db.execute("SELECT COUNT(*) FROM produto").fetchone()[0]
ofertas = db.execute("SELECT COUNT(*) FROM oferta").fetchone()[0]
itens, total = db.execute(
    "SELECT COUNT(*), SUM(quantidade * preco_praticado_centavos) FROM item_pedido"
).fetchone()
assert (vendedores, produtos, ofertas, itens, total) == (2, 1, 2, 2, 5100)

print(f"vendedores={vendedores}")
print(f"produtos={produtos}")
print(f"ofertas={ofertas}")
print(f"itens={itens}")
print(f"total_centavos={total}")
print(f"oferta_duplicada={duplicada}")
print(f"referencia_invalida={referencia}")
print("modelo_er=ok")
db.close()
```

`OFERTA` preserva atributos da associação vendedor-produto. `ITEM_PEDIDO` depende do pedido e referencia a oferta realmente comprada.

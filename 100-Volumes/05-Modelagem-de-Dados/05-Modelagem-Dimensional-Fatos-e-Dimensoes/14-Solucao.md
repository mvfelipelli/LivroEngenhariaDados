---
title: Solução — Star Schema de Vendas
description: "Implementação validada de esquema estrela no SQLite."
tags: [modelagem-de-dados, sqlite, dimensional, solucao]
aliases: [Solução Laboratório Star Schema]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Star Schema de Vendas

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript(
    """
    CREATE TABLE dim_data (
        data_sk INTEGER PRIMARY KEY, data_iso TEXT UNIQUE, mes TEXT
    );
    CREATE TABLE dim_produto (
        produto_sk INTEGER PRIMARY KEY, produto_id INTEGER UNIQUE,
        nome TEXT, categoria TEXT
    );
    CREATE TABLE dim_loja (
        loja_sk INTEGER PRIMARY KEY, loja_id INTEGER UNIQUE, nome TEXT
    );
    CREATE TABLE fato_item_venda (
        pedido_id INTEGER NOT NULL,
        numero_item INTEGER NOT NULL,
        data_sk INTEGER NOT NULL REFERENCES dim_data(data_sk),
        produto_sk INTEGER NOT NULL REFERENCES dim_produto(produto_sk),
        loja_sk INTEGER NOT NULL REFERENCES dim_loja(loja_sk),
        quantidade INTEGER NOT NULL CHECK (quantidade > 0),
        receita_centavos INTEGER NOT NULL,
        PRIMARY KEY (pedido_id, numero_item)
    );
    INSERT INTO dim_data VALUES
        (20260701, '2026-07-01', '2026-07'),
        (20260702, '2026-07-02', '2026-07');
    INSERT INTO dim_produto VALUES
        (1, 100, 'Café', 'Mercearia'),
        (2, 200, 'Caneca', 'Casa');
    INSERT INTO dim_loja VALUES (1, 10, 'Centro'), (2, 20, 'Norte');
    INSERT INTO fato_item_venda VALUES
        (1000, 1, 20260701, 1, 1, 2, 2000),
        (1000, 2, 20260701, 2, 1, 1, 1500),
        (1001, 1, 20260701, 1, 2, 3, 3000),
        (1002, 1, 20260702, 1, 1, 1, 1000);
    """
)

try:
    db.execute(
        "INSERT INTO fato_item_venda VALUES (?, ?, ?, ?, ?, ?, ?)",
        (1000, 1, 20260701, 1, 1, 1, 1000),
    )
    raise AssertionError("grao_nao_protegido")
except sqlite3.IntegrityError:
    duplicado = "rejeitado"

agregado = db.execute(
    """
    SELECT p.categoria, l.nome, SUM(f.receita_centavos)
    FROM fato_item_venda f
    JOIN dim_produto p USING (produto_sk)
    JOIN dim_loja l USING (loja_sk)
    GROUP BY p.categoria, l.nome
    """
).fetchall()
total_agregado = sum(linha[2] for linha in agregado)

datas = db.execute("SELECT COUNT(*) FROM dim_data").fetchone()[0]
produtos = db.execute("SELECT COUNT(*) FROM dim_produto").fetchone()[0]
lojas = db.execute("SELECT COUNT(*) FROM dim_loja").fetchone()[0]
itens, quantidade, receita = db.execute(
    "SELECT COUNT(*), SUM(quantidade), SUM(receita_centavos) FROM fato_item_venda"
).fetchone()
assert (datas, produtos, lojas, itens, quantidade, receita) == (2, 2, 2, 4, 7, 7500)
assert total_agregado == receita

print(f"datas={datas}")
print(f"produtos={produtos}")
print(f"lojas={lojas}")
print(f"itens_fato={itens}")
print(f"quantidade={quantidade}")
print(f"receita_centavos={receita}")
print(f"grao_duplicado={duplicado}")
print("estrela=ok")
db.close()
```

A chave `(pedido_id, numero_item)` protege o grão; dimensões fornecem contexto sem alterar a soma da medida.

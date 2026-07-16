---
title: Solução — Modelo Operacional e Analítico
aliases: [Solução do Laboratório de Modelagem]
tags: [engenharia-de-dados, fundamentos, modelagem-de-dados, solucao, sqlite, python]
type: solution
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável do laboratório de modelagem operacional e analítica."
---

# 14 — Solução

## Implementação

Crie `database_modeling_lab.py`:

```python
from pathlib import Path
import sqlite3

DB_PATH = Path("dataretail_modeling.db")

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL
);

CREATE TABLE sales_order (
    order_id INTEGER PRIMARY KEY,
    source_system TEXT NOT NULL,
    source_order_id TEXT NOT NULL,
    customer_id INTEGER NOT NULL REFERENCES customer(customer_id),
    placed_at TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('confirmed', 'cancelled')),
    UNIQUE (source_system, source_order_id)
);

CREATE TABLE order_item (
    order_id INTEGER NOT NULL REFERENCES sales_order(order_id),
    line_number INTEGER NOT NULL CHECK (line_number > 0),
    product_id INTEGER NOT NULL REFERENCES product(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC NOT NULL CHECK (unit_price >= 0),
    discount NUMERIC NOT NULL CHECK (discount >= 0),
    PRIMARY KEY (order_id, line_number)
);

CREATE TABLE dim_product (
    product_key INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    valid_from TEXT NOT NULL,
    valid_to TEXT,
    is_current INTEGER NOT NULL CHECK (is_current IN (0, 1)),
    UNIQUE (product_id, valid_from)
);

CREATE TABLE fact_sales_item (
    order_id INTEGER NOT NULL,
    line_number INTEGER NOT NULL,
    product_key INTEGER NOT NULL REFERENCES dim_product(product_key),
    quantity INTEGER NOT NULL,
    net_amount NUMERIC NOT NULL,
    PRIMARY KEY (order_id, line_number)
);
"""

def seed(connection: sqlite3.Connection) -> None:
    connection.executemany(
        "INSERT INTO customer VALUES (?, ?, ?)",
        [(1, "Ana", "ana@example.com"), (2, "Bruno", "bruno@example.com")],
    )
    connection.executemany(
        "INSERT INTO product VALUES (?, ?, ?)",
        [(101, "TEC-01", "Teclado"), (102, "MON-01", "Monitor")],
    )
    connection.executemany(
        "INSERT INTO sales_order VALUES (?, ?, ?, ?, ?, ?)",
        [
            (1001, "web", "W-1", 1, "2026-06-15", "confirmed"),
            (1002, "store", "S-1", 2, "2026-07-10", "cancelled"),
        ],
    )
    connection.executemany(
        "INSERT INTO order_item VALUES (?, ?, ?, ?, ?, ?)",
        [(1001, 1, 101, 2, 150, 20), (1001, 2, 102, 1, 100, 0), (1002, 1, 101, 1, 150, 0)],
    )
    connection.executemany(
        "INSERT INTO dim_product VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            (10001, 101, "Teclado", "Periféricos", "2026-01-01", "2026-07-01", 0),
            (10002, 101, "Teclado", "Acessórios", "2026-07-01", None, 1),
            (10003, 102, "Monitor", "Monitores", "2026-01-01", None, 1),
        ],
    )
    connection.commit()

def load_fact(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        INSERT INTO fact_sales_item
        SELECT i.order_id,
               i.line_number,
               d.product_key,
               i.quantity,
               i.quantity * i.unit_price - i.discount
        FROM order_item AS i
        JOIN sales_order AS o ON o.order_id = i.order_id
        JOIN dim_product AS d
          ON d.product_id = i.product_id
         AND o.placed_at >= d.valid_from
         AND (d.valid_to IS NULL OR o.placed_at < d.valid_to)
        WHERE o.status = 'confirmed'
        """
    )
    connection.commit()

def constraint_tests(connection: sqlite3.Connection) -> tuple[bool, bool]:
    try:
        connection.execute(
            "INSERT INTO sales_order VALUES (1003, 'web', 'W-1', 1, '2026-07-16', 'confirmed')"
        )
    except sqlite3.IntegrityError:
        duplicate_blocked = True
    else:
        duplicate_blocked = False

    try:
        connection.execute("INSERT INTO order_item VALUES (9999, 1, 101, 1, 150, 0)")
    except sqlite3.IntegrityError:
        orphan_blocked = True
    else:
        orphan_blocked = False
    connection.rollback()
    return duplicate_blocked, orphan_blocked

def main() -> None:
    DB_PATH.unlink(missing_ok=True)
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(SCHEMA)
        seed(connection)
        load_fact(connection)
        duplicate_blocked, orphan_blocked = constraint_tests(connection)

        fact = connection.execute(
            "SELECT COUNT(*), SUM(quantity), SUM(net_amount) FROM fact_sales_item"
        ).fetchone()
        operational = connection.execute(
            """
            SELECT SUM(i.quantity), SUM(i.quantity * i.unit_price - i.discount)
            FROM order_item i JOIN sales_order o USING (order_id)
            WHERE o.status = 'confirmed'
            """
        ).fetchone()
        category = connection.execute(
            """
            SELECT d.category FROM fact_sales_item f
            JOIN dim_product d USING (product_key)
            WHERE f.order_id = 1001 AND f.line_number = 1
            """
        ).fetchone()[0]
        integrity = connection.execute("PRAGMA foreign_key_check").fetchall()

        assert not integrity
        assert duplicate_blocked and orphan_blocked
        assert fact == (2, 3, 380)
        assert operational == fact[1:]
        assert category == "Periféricos"

        print("integridade=ok")
        print("duplicidade_bloqueada=sim")
        print("orfao_bloqueado=sim")
        print(f"fato_linhas={fact[0]}")
        print(f"quantidade={fact[1]}")
        print(f"valor_liquido={fact[2]:.2f}")
        print(f"categoria_historica={category}")
        print("reconciliacao=ok")

if __name__ == "__main__":
    main()
```

## Análise

O modelo operacional preserva chaves e integridade. A fato seleciona somente itens confirmados e resolve a versão de produto válida na data do pedido. A categoria atual muda para `Acessórios`, mas a venda de junho continua ligada a `Periféricos`.

A reconciliação compara quantidade e valor líquido no mesmo conjunto elegível e grão compatível. Os testes negativos demonstram que duplicidade de origem e referência órfã são bloqueadas.

## Respostas

1. Cancelamento não atende à definição de venda confirmada.
2. Operacional: linha do pedido; analítico: linha confirmada enriquecida com chaves dimensionais.
3. A chave operacional identifica produto; a chave dimensional identifica uma versão histórica.
4. O intervalo de vigência seleciona a versão existente no instante da venda.
5. Limites agregados, estoque e entregas parciais exigem proteção sob concorrência.

## Próximo Capítulo

➡️ [[15-Referencias|15 — Referências]]

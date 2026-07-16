---
title: Solução — Raw, Staging e Mart com SQL
aliases: [Solução do Laboratório ELT]
tags: [engenharia-de-dados, fundamentos, elt, solucao, sql, sqlite]
type: solution
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável do laboratório ELT."
---

# 14 — Solução

```python
from pathlib import Path
import sqlite3

DB = Path("elt_lab.db")
RAW = [
    ("web", "p1", 1, "confirmed", 100, 10, "b1"),
    ("web", "p1", 2, "confirmed", 150, 20, "b2"),
    ("app", "p2", 1, "cancelled", 80, 0, "b2"),
    ("store", "p3", 1, "confirmed", 100, 0, "b2"),
]

def rebuild(connection: sqlite3.Connection) -> None:
    connection.executescript("""
        DROP TABLE IF EXISTS stg_orders;
        CREATE TABLE stg_orders AS
        SELECT source, order_id, version, status, gross, discount
        FROM (
            SELECT *, ROW_NUMBER() OVER (
                PARTITION BY source, order_id ORDER BY version DESC, ingested_at DESC
            ) AS rn
            FROM raw_orders
        ) WHERE rn = 1;
        CREATE UNIQUE INDEX ux_stg_orders ON stg_orders(source, order_id);

        DROP TABLE IF EXISTS mart_sales;
        CREATE TABLE mart_sales AS
        SELECT source, order_id, gross - discount AS net_amount
        FROM stg_orders WHERE status = 'confirmed';
        CREATE UNIQUE INDEX ux_mart_sales ON mart_sales(source, order_id);
    """)
    connection.commit()

def main() -> None:
    DB.unlink(missing_ok=True)
    with sqlite3.connect(DB) as connection:
        connection.execute("""
            CREATE TABLE raw_orders (
                source TEXT, order_id TEXT, version INTEGER, status TEXT,
                gross NUMERIC, discount NUMERIC, batch_id TEXT,
                ingested_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(source, order_id, version)
            )
        """)
        connection.executemany(
            "INSERT INTO raw_orders(source,order_id,version,status,gross,discount,batch_id) VALUES(?,?,?,?,?,?,?)",
            RAW,
        )
        rebuild(connection)
        first = connection.execute("SELECT * FROM mart_sales ORDER BY 1,2").fetchall()
        rebuild(connection)
        second = connection.execute("SELECT * FROM mart_sales ORDER BY 1,2").fetchall()
        raw = connection.execute("SELECT COUNT(*) FROM raw_orders").fetchone()[0]
        staging = connection.execute("SELECT COUNT(*) FROM stg_orders").fetchone()[0]
        mart = connection.execute("SELECT COUNT(*) FROM mart_sales").fetchone()[0]
        revenue = connection.execute("SELECT SUM(net_amount) FROM mart_sales").fetchone()[0]
        duplicates = connection.execute("SELECT COUNT(*)-COUNT(DISTINCT source||'|'||order_id) FROM mart_sales").fetchone()[0]
        invalid = connection.execute("SELECT COUNT(*) FROM stg_orders WHERE status NOT IN ('confirmed','cancelled')").fetchone()[0]
        assert (raw, staging, mart, revenue) == (4, 3, 2, 230)
        assert duplicates == invalid == 0 and first == second
        print(f"raw={raw}\nstaging={staging}\nmart={mart}")
        print(f"receita_liquida={revenue:.2f}\ntestes=ok\nrebuild=ok")
        print("linhagem=raw_orders>stg_orders>mart_sales")

if __name__ == "__main__":
    main()
```

## Análise

Raw mantém duas versões de `p1`. Staging escolhe a versão 2; mart exclui cancelados. O rebuild recria derivados sem alterar raw e produz resultado idêntico.

## Próximo Capítulo

➡️ [[15-Referencias|15 — Referências]]

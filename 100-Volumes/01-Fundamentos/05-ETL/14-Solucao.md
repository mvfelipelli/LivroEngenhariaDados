---
title: Solução — ETL Incremental de Pedidos
aliases: [Solução do Laboratório ETL]
tags: [engenharia-de-dados, fundamentos, etl, solucao, python, sqlite]
type: solution
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável do ETL incremental da DataRetail."
---

# 14 — Solução

```python
from pathlib import Path
import csv
import sqlite3

DB = Path("etl_lab.db")
CSV = Path("orders.csv")
ROWS = [
    ["e1", "web", "p1", "1", "2026-07-16T10:00:00Z", "confirmed", "100.00"],
    ["e2", "web", "p1", "2", "2026-07-16T10:01:00Z", "confirmed", "150.00"],
    ["e3", "app", "p2", "1", "2026-07-16T10:02:00Z", "confirmed", "-2.00"],
    ["e4", "store", "p3", "1", "2026-07-16T10:03:00Z", "cancelled", "80.00"],
]

def prepare() -> sqlite3.Connection:
    DB.unlink(missing_ok=True)
    with CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["event_id", "source", "order_id", "version", "updated_at", "status", "total"])
        writer.writerows(ROWS)
    connection = sqlite3.connect(DB)
    connection.executescript("""
        CREATE TABLE orders (
            source TEXT NOT NULL, order_id TEXT NOT NULL, version INTEGER NOT NULL,
            updated_at TEXT NOT NULL, status TEXT NOT NULL, total NUMERIC NOT NULL,
            PRIMARY KEY (source, order_id)
        );
        CREATE TABLE quarantine (event_id TEXT PRIMARY KEY, reason TEXT NOT NULL);
        CREATE TABLE pipeline_state (name TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE audit (run_id TEXT PRIMARY KEY, extracted INTEGER, valid INTEGER, rejected INTEGER);
    """)
    return connection

def run(connection: sqlite3.Connection, run_id: str) -> tuple[int, int, int]:
    with CSV.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    latest: dict[tuple[str, str], dict[str, str]] = {}
    rejected = 0
    for row in rows:
        try:
            total = float(row["total"])
            version = int(row["version"])
            if not row["source"] or not row["order_id"] or total < 0:
                raise ValueError("campos ou total inválidos")
            if row["status"] not in {"confirmed", "cancelled"}:
                raise ValueError("status inválido")
        except ValueError as error:
            connection.execute("INSERT OR REPLACE INTO quarantine VALUES (?, ?)", (row["event_id"], str(error)))
            rejected += 1
            continue
        key = (row["source"], row["order_id"])
        if key not in latest or version > int(latest[key]["version"]):
            latest[key] = row
    for row in latest.values():
        connection.execute("""
            INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(source, order_id) DO UPDATE SET
              version=excluded.version, updated_at=excluded.updated_at,
              status=excluded.status, total=excluded.total
            WHERE excluded.version > orders.version
        """, (row["source"], row["order_id"], int(row["version"]), row["updated_at"], row["status"], float(row["total"])))
    watermark = max((row["updated_at"], row["event_id"]) for row in rows)
    connection.execute("INSERT OR REPLACE INTO pipeline_state VALUES ('orders', ?)", ("|".join(watermark),))
    connection.execute("INSERT OR REPLACE INTO audit VALUES (?, ?, ?, ?)", (run_id, len(rows), len(latest), rejected))
    connection.commit()
    return len(rows), len(latest), rejected

def main() -> None:
    with prepare() as connection:
        first = run(connection, "run-1")
        before = connection.execute("SELECT * FROM orders ORDER BY source, order_id").fetchall()
        second = run(connection, "run-2")
        after = connection.execute("SELECT * FROM orders ORDER BY source, order_id").fetchall()
        count = connection.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
        total = connection.execute("SELECT SUM(total) FROM orders WHERE status='confirmed'").fetchone()[0]
        watermark = connection.execute("SELECT value FROM pipeline_state WHERE name='orders'").fetchone()[0]
        assert first == second == (4, 2, 1)
        assert before == after and count == 2 and total == 150
        print("extraidos=4\nvalidos=2\nrejeitados=1")
        print(f"pedidos={count}\ntotal_confirmado={total:.2f}")
        print(f"watermark={watermark}\nidempotencia=ok\nreconciliacao=ok")

if __name__ == "__main__":
    main()
```

## Análise

`p1` permanece uma única vez com versão 2; `p2` vai para quarentena; `p3` é mantido cancelado. O upsert só aceita versão maior, e o cursor é persistido após o commit.

## Próximo Capítulo

➡️ [[15-Referencias|15 — Referências]]

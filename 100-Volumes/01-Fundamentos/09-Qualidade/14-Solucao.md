---
title: Solução — Quality Gate de Pedidos
aliases: [Solução do Laboratório de Qualidade]
tags: [qualidade, solucao, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável do quality gate de pedidos."
---

# Solução — Quality Gate de Pedidos

```python
from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path


ORDERS = [
    {"event_id": "e-1", "order_id": "p-100", "customer_id": "c-1", "value": 100.0},
    {"event_id": "e-2", "order_id": None, "customer_id": "c-1", "value": 50.0},
    {"event_id": "e-3", "order_id": "p-102", "customer_id": "c-1", "value": -1.0},
    {"event_id": "e-4", "order_id": "p-103", "customer_id": "c-99", "value": 70.0},
    {"event_id": "e-1", "order_id": "p-104", "customer_id": "c-2", "value": 80.0},
    {"event_id": "e-5", "order_id": "p-105", "customer_id": "c-2", "value": 120.0},
]

CUSTOMERS = {"c-1", "c-2"}
DIMENSIONS = ("completude", "validade", "integridade", "unicidade")


def evaluate(orders: list[dict]) -> tuple[list[dict], list[dict], dict[str, float]]:
    seen_events = set()
    approved = []
    quarantined = []
    failures = {dimension: 0 for dimension in DIMENSIONS}

    for position, order in enumerate(orders, start=1):
        reason = None
        if not order["order_id"]:
            reason = "completude"
        elif order["value"] < 0:
            reason = "validade"
        elif order["customer_id"] not in CUSTOMERS:
            reason = "integridade"
        elif order["event_id"] in seen_events:
            reason = "unicidade"

        seen_events.add(order["event_id"])
        if reason:
            failures[reason] += 1
            quarantined.append({"position": position, "event_id": order["event_id"], "reason": reason})
        else:
            approved.append(order)

    total = len(orders)
    metrics = {
        dimension: 100.0 * (total - failures[dimension]) / total
        for dimension in DIMENSIONS
    }
    return approved, quarantined, metrics


def prepare(connection: sqlite3.Connection) -> None:
    connection.executescript("""
        CREATE TABLE IF NOT EXISTS quality_run (
            run_id TEXT PRIMARY KEY,
            score REAL NOT NULL,
            decision TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS quality_metric (
            run_id TEXT NOT NULL,
            dimension TEXT NOT NULL,
            value REAL NOT NULL,
            PRIMARY KEY (run_id, dimension)
        );
        CREATE TABLE IF NOT EXISTS quarantine (
            run_id TEXT NOT NULL,
            position INTEGER NOT NULL,
            event_id TEXT NOT NULL,
            reason TEXT NOT NULL,
            PRIMARY KEY (run_id, position)
        );
    """)
    connection.commit()


def persist(
    connection: sqlite3.Connection,
    run_id: str,
    score: float,
    decision: str,
    metrics: dict[str, float],
    quarantined: list[dict],
) -> None:
    with connection:
        connection.execute(
            "INSERT OR REPLACE INTO quality_run VALUES (?, ?, ?)",
            (run_id, score, decision),
        )
        for dimension, value in metrics.items():
            connection.execute(
                "INSERT OR REPLACE INTO quality_metric VALUES (?, ?, ?)",
                (run_id, dimension, value),
            )
        for item in quarantined:
            connection.execute(
                "INSERT OR REPLACE INTO quarantine VALUES (?, ?, ?, ?)",
                (run_id, item["position"], item["event_id"], item["reason"]),
            )


def main() -> None:
    approved, quarantined, metrics = evaluate(ORDERS)
    score = sum(metrics.values()) / len(metrics)
    decision = "aprovado" if score >= 80.0 else "reprovado"

    database = Path(tempfile.gettempdir()) / "dataretail_quality.sqlite3"
    database.unlink(missing_ok=True)
    connection = sqlite3.connect(database)
    try:
        prepare(connection)
        persist(connection, "run-009", score, decision, metrics, quarantined)
        persist(connection, "run-009", score, decision, metrics, quarantined)
        violations = connection.execute("SELECT COUNT(*) FROM quarantine").fetchone()[0]

        assert len(approved) == 2
        assert len(quarantined) == violations == 4
        assert decision == "aprovado"
        print(f"registros={len(ORDERS)}")
        print(f"aprovados={len(approved)}")
        print(f"quarentena={len(quarantined)}")
        for dimension in DIMENSIONS:
            print(f"{dimension}={metrics[dimension]:.2f}")
        print(f"score={score:.2f}")
        print(f"quality_gate={decision}")
        print(f"violacoes_persistidas={violations}")
        print("segunda_execucao=sem_duplicacao")
        print("qualidade=ok")
    finally:
        connection.close()
    database.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
```

## Leitura da solução

As regras são avaliadas em ordem para atribuir uma causa primária a cada registro. As taxas mantêm denominador comum, o score é a média simples e o gate compara o resultado com o threshold. Chaves compostas e operações `INSERT OR REPLACE` tornam a persistência repetível.

> [!warning]
> Uma média pode esconder dimensão crítica. Em produção, combine score com invariantes que sempre bloqueiam, independentemente da média.

Finalize em [[15-Referencias]].

---
title: Solução — Prontidão de Produtos de Dados
aliases: [Solução do Laboratório de Conceitos Modernos]
tags: [conceitos-modernos, solucao, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável para avaliação de produtos de dados."
---

# Solução — Prontidão de Produtos de Dados

```python
from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path


CRITERIA = ("owner", "consumers", "schema", "slo", "quality", "access", "lineage", "cost")

PRODUCTS = [
    {"name": "pedidos_confiaveis", **{criterion: True for criterion in CRITERIA}},
    {
        "name": "clientes_360",
        "owner": True, "consumers": True, "schema": True, "slo": True,
        "quality": True, "access": True, "lineage": False, "cost": True,
    },
    {
        "name": "sandbox_marketing",
        "owner": False, "consumers": True, "schema": True, "slo": True,
        "quality": False, "access": False, "lineage": True, "cost": True,
    },
]


def evaluate(products: list[dict]) -> dict[str, list[str]]:
    return {
        product["name"]: [criterion for criterion in CRITERIA if not product[criterion]]
        for product in products
    }


def prepare(connection: sqlite3.Connection) -> None:
    connection.executescript("""
        CREATE TABLE IF NOT EXISTS readiness_run (
            run_id TEXT PRIMARY KEY,
            ready_products INTEGER NOT NULL,
            readiness REAL NOT NULL
        );
        CREATE TABLE IF NOT EXISTS readiness_violation (
            run_id TEXT NOT NULL,
            product TEXT NOT NULL,
            criterion TEXT NOT NULL,
            PRIMARY KEY (run_id, product, criterion)
        );
    """)
    connection.commit()


def persist(connection, run_id, ready, readiness, violations) -> None:
    with connection:
        connection.execute(
            "INSERT OR REPLACE INTO readiness_run VALUES (?, ?, ?)",
            (run_id, ready, readiness),
        )
        for product, criterion in violations:
            connection.execute(
                "INSERT OR REPLACE INTO readiness_violation VALUES (?, ?, ?)",
                (run_id, product, criterion),
            )


def main() -> None:
    findings = evaluate(PRODUCTS)
    ready = sum(not violations for violations in findings.values())
    violations = [
        (product, criterion)
        for product, criteria in findings.items()
        for criterion in criteria
    ]
    readiness = 100.0 * ready / len(PRODUCTS)

    database = Path(tempfile.gettempdir()) / "dataretail_products.sqlite3"
    database.unlink(missing_ok=True)
    connection = sqlite3.connect(database)
    try:
        prepare(connection)
        persist(connection, "run-012", ready, readiness, violations)
        persist(connection, "run-012", ready, readiness, violations)
        persisted = connection.execute("SELECT COUNT(*) FROM readiness_violation").fetchone()[0]

        assert ready == 1
        assert len(violations) == persisted == 4
        print(f"produtos={len(PRODUCTS)}")
        print(f"checks={len(PRODUCTS) * len(CRITERIA)}")
        print(f"prontos={ready}")
        print(f"bloqueados={len(PRODUCTS) - ready}")
        print(f"violacoes={len(violations)}")
        print(f"readiness={readiness:.2f}")
        print(f"violacoes_persistidas={persisted}")
        print("segunda_execucao=sem_duplicacao")
        print("produtos_de_dados=ok")
    finally:
        connection.close()
    database.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
```

## Leitura da solução

Os oito critérios funcionam como guardrails mínimos. O resultado separa produtos prontos, bloqueios e causas. A persistência usa chaves compostas para que repetir a mesma avaliação não duplique evidências.

> [!warning]
> Booleanos são adequados ao exemplo, mas produção exige evidência, versão, owner da regra e validade temporal.

Finalize em [[15-Referencias]].

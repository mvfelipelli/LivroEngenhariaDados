---
title: Solução — Executor de DAG Idempotente
aliases: [Solução do Laboratório de Pipelines]
tags: [pipelines, solucao, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável do laboratório de pipelines."
---

# Solução — Executor de DAG Idempotente

```python
from __future__ import annotations

import sqlite3
import tempfile
from collections import deque
from pathlib import Path

TASKS = {
    "extract": [],
    "validate": ["extract"],
    "transform": ["validate"],
    "load": ["transform"],
    "reconcile": ["load"],
}

def topological_order(tasks: dict[str, list[str]]) -> list[str]:
    indegree = {task: len(dependencies) for task, dependencies in tasks.items()}
    followers = {task: [] for task in tasks}
    for task, dependencies in tasks.items():
        for dependency in dependencies:
            if dependency not in tasks:
                raise ValueError(f"Dependência inexistente: {dependency}")
            followers[dependency].append(task)

    ready = deque(task for task, degree in indegree.items() if degree == 0)
    order = []
    while ready:
        task = ready.popleft()
        order.append(task)
        for follower in followers[task]:
            indegree[follower] -= 1
            if indegree[follower] == 0:
                ready.append(follower)

    if len(order) != len(tasks):
        raise ValueError("O DAG contém um ciclo")
    return order

def prepare_database(connection: sqlite3.Connection) -> None:
    connection.executescript("""
        CREATE TABLE IF NOT EXISTS pedidos (
            pedido_id TEXT PRIMARY KEY,
            versao INTEGER NOT NULL,
            status TEXT NOT NULL,
            valor REAL NOT NULL
        );
        CREATE TABLE IF NOT EXISTS quarentena (
            run_id TEXT NOT NULL,
            pedido_id TEXT,
            motivo TEXT NOT NULL,
            UNIQUE (run_id, pedido_id, motivo)
        );
        CREATE TABLE IF NOT EXISTS auditoria (
            run_id TEXT NOT NULL,
            tarefa TEXT NOT NULL,
            status TEXT NOT NULL,
            PRIMARY KEY (run_id, tarefa)
        );
    """)

def extract(context: dict) -> None:
    context["raw"] = [
        {"pedido_id": "p-100", "versao": 1, "status": "confirmado", "valor": 90.0},
        {"pedido_id": "p-100", "versao": 2, "status": "confirmado", "valor": 150.0},
        {"pedido_id": "p-200", "versao": 1, "status": "cancelado", "valor": 40.0},
        {"pedido_id": None, "versao": 1, "status": "confirmado", "valor": -5.0},
    ]

def validate(context: dict) -> None:
    valid = []
    rejected = []
    for row in context["raw"]:
        if not row["pedido_id"] or row["valor"] < 0:
            rejected.append(row)
        else:
            valid.append(row)
    context["validated"] = valid
    context["rejected"] = rejected
    connection = context["connection"]
    for row in rejected:
        connection.execute(
            "INSERT OR IGNORE INTO quarentena VALUES (?, ?, ?)",
            (context["run_id"], row["pedido_id"], "chave ausente ou valor negativo"),
        )
    connection.commit()

def transform(context: dict) -> None:
    latest = {}
    for row in context["validated"]:
        current = latest.get(row["pedido_id"])
        if current is None or row["versao"] > current["versao"]:
            latest[row["pedido_id"]] = row
    context["final"] = list(latest.values())

def load(context: dict) -> None:
    connection = context["connection"]
    with connection:
        for row in context["final"]:
            connection.execute("""
                INSERT INTO pedidos VALUES (?, ?, ?, ?)
                ON CONFLICT(pedido_id) DO UPDATE SET
                    versao = excluded.versao,
                    status = excluded.status,
                    valor = excluded.valor
                WHERE excluded.versao >= pedidos.versao
            """, (row["pedido_id"], row["versao"], row["status"], row["valor"]))

def reconcile(context: dict) -> None:
    connection = context["connection"]
    count, total = connection.execute("""
        SELECT COUNT(*), COALESCE(SUM(CASE WHEN status = 'confirmado' THEN valor ELSE 0 END), 0)
        FROM pedidos
    """).fetchone()
    if count != 2 or round(total, 2) != 150.00:
        raise RuntimeError("Reconciliação reprovada")
    context["count"] = count
    context["total"] = total

FUNCTIONS = {
    "extract": extract,
    "validate": validate,
    "transform": transform,
    "load": load,
    "reconcile": reconcile,
}

def execute(connection: sqlite3.Connection, run_id: str) -> tuple[list[str], dict]:
    order = topological_order(TASKS)
    context = {"connection": connection, "run_id": run_id}
    for task in order:
        connection.execute(
            "INSERT OR REPLACE INTO auditoria VALUES (?, ?, ?)",
            (run_id, task, "executando"),
        )
        connection.commit()
        FUNCTIONS[task](context)
        connection.execute(
            "UPDATE auditoria SET status = ? WHERE run_id = ? AND tarefa = ?",
            ("concluido", run_id, task),
        )
        connection.commit()
    return order, context

def main() -> None:
    database = Path(tempfile.gettempdir()) / "dataretail_pipeline.sqlite3"
    database.unlink(missing_ok=True)
    connection = sqlite3.connect(database)
    try:
        prepare_database(connection)
        order, first = execute(connection, "run-001")
        _, second = execute(connection, "run-002")
        audited = connection.execute("SELECT COUNT(*) FROM auditoria").fetchone()[0]
        rejected = len(first["rejected"])

        assert first["count"] == second["count"] == 2
        assert audited == 10
        print(f"ordem={'>'.join(order)}")
        print(f"extraidos={len(first['raw'])}")
        print(f"validos={len(first['final'])}")
        print(f"rejeitados={rejected}")
        print(f"pedidos={second['count']}")
        print(f"total_confirmado={second['total']:.2f}")
        print(f"tarefas_auditadas={audited}")
        print("segunda_execucao=sem_duplicacao")
        print("pipeline=ok")
    finally:
        connection.close()
    database.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
```

## Por que a solução é confiável

- a ordenação topológica verifica dependências e ciclos;
- cada execução possui `run_id` e estado por tarefa;
- registros inválidos preservam motivo na quarentena;
- a transformação escolhe uma versão determinística;
- o upsert torna a carga repetível;
- a transação impede publicação parcial da carga;
- a reconciliação valida o estado final;
- duas runs demonstram ausência de duplicação.

> [!warning]
> Este executor é didático. Produção exige concorrência segura, leases, heartbeats, retries, isolamento de workers, segredos e persistência de estado mais robusta.

Finalize o módulo com [[15-Referencias]].

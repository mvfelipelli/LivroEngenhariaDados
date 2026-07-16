---
title: Solução — Correlação de Telemetria e SLO
aliases: [Solução do Laboratório de Observabilidade]
tags: [observabilidade, solucao, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável para trace, SLO e persistência de incidente."
---

# Solução — Correlação de Telemetria e SLO

```python
from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path


SPANS = [
    {"trace_id": "trace-011", "name": "extract", "duration_seconds": 60},
    {"trace_id": "trace-011", "name": "validate", "duration_seconds": 30},
    {"trace_id": "trace-011", "name": "transform", "duration_seconds": 240},
    {"trace_id": "trace-011", "name": "publish", "duration_seconds": 90},
]

SLOS = {"freshness_minutes": 5.0, "completeness_percent": 99.0}


def correlate(spans: list[dict]) -> tuple[str, int]:
    trace_ids = {span["trace_id"] for span in spans}
    if len(trace_ids) != 1:
        raise ValueError("Os spans não pertencem ao mesmo trace")
    path = ">".join(span["name"] for span in spans)
    duration = sum(span["duration_seconds"] for span in spans)
    return path, duration


def evaluate(freshness: float, completeness: float) -> list[str]:
    alerts = []
    if freshness > SLOS["freshness_minutes"]:
        alerts.append("freshness")
    if completeness < SLOS["completeness_percent"]:
        alerts.append("completeness")
    return alerts


def prepare(connection: sqlite3.Connection) -> None:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS incident (
            incident_id TEXT PRIMARY KEY,
            trace_id TEXT NOT NULL,
            symptom TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    connection.commit()


def persist(connection: sqlite3.Connection, alerts: list[str]) -> None:
    with connection:
        for symptom in alerts:
            connection.execute("""
                INSERT INTO incident VALUES (?, ?, ?, ?)
                ON CONFLICT(incident_id) DO UPDATE SET
                    trace_id = excluded.trace_id,
                    symptom = excluded.symptom,
                    status = excluded.status
            """, ("INC-011", "trace-011", symptom, "aberto"))


def main() -> None:
    path, critical_seconds = correlate(SPANS)
    freshness = 8.0
    completeness = 99.5
    alerts = evaluate(freshness, completeness)

    database = Path(tempfile.gettempdir()) / "dataretail_observability.sqlite3"
    database.unlink(missing_ok=True)
    connection = sqlite3.connect(database)
    try:
        prepare(connection)
        persist(connection, alerts)
        persist(connection, alerts)
        incidents = connection.execute("SELECT COUNT(*) FROM incident").fetchone()[0]

        assert critical_seconds == 420
        assert alerts == ["freshness"]
        assert incidents == 1
        print(f"spans={len(SPANS)}")
        print(f"caminho={path}")
        print(f"caminho_critico_segundos={critical_seconds}")
        print(f"freshness_minutos={freshness:.2f}")
        print(f"completude={completeness:.2f}")
        print(f"alertas={len(alerts)}")
        print("incidente=INC-011")
        print(f"incidentes_persistidos={incidents}")
        print("segunda_execucao=sem_duplicacao")
        print("observabilidade=ok")
    finally:
        connection.close()
    database.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
```

## Leitura da solução

A correlação exige um único `trace_id`, preserva a ordem dos spans e calcula a duração. Freshness e completude são avaliadas separadamente. O incidente usa identificador estável e upsert para evitar duplicação.

> [!warning]
> Em sistemas paralelos, caminho crítico não é a soma de todos os spans; é o maior caminho causal. O exemplo é sequencial para manter o foco na correlação.

Finalize em [[15-Referencias]].

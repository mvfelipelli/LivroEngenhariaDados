---
title: Solução — Política Executável de Governança
aliases: [Solução do Laboratório de Governança]
tags: [governanca, solucao, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Solução executável para avaliação e evidência de governança."
---

# Solução — Política Executável de Governança

```python
from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path


ASSETS = [
    {
        "asset": "pedidos",
        "owner": "dominio_pedidos",
        "classification": "confidencial",
        "retention_days": 2555,
        "access_policy": True,
    },
    {
        "asset": "clientes",
        "owner": "dominio_clientes",
        "classification": "restrito",
        "retention_days": 365,
        "access_policy": True,
    },
    {
        "asset": "clickstream",
        "owner": None,
        "classification": "interno",
        "retention_days": 400,
        "access_policy": True,
    },
    {
        "asset": "sandbox_export",
        "owner": None,
        "classification": "restrito",
        "retention_days": 30,
        "access_policy": False,
    },
]


def evaluate(asset: dict) -> list[str]:
    violations = []
    if not asset["owner"]:
        violations.append("owner_obrigatorio")
    if asset["classification"] in {"confidencial", "restrito"} and not asset["access_policy"]:
        violations.append("politica_acesso_obrigatoria")
    minimum_retention = {"confidencial": 2555, "restrito": 365}.get(asset["classification"], 0)
    if asset["retention_days"] < minimum_retention:
        violations.append("retencao_insuficiente")
    return violations


def prepare(connection: sqlite3.Connection) -> None:
    connection.executescript("""
        CREATE TABLE IF NOT EXISTS governance_run (
            run_id TEXT PRIMARY KEY,
            decision TEXT NOT NULL,
            compliant_assets INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS governance_violation (
            run_id TEXT NOT NULL,
            asset TEXT NOT NULL,
            rule TEXT NOT NULL,
            PRIMARY KEY (run_id, asset, rule)
        );
    """)
    connection.commit()


def persist(
    connection: sqlite3.Connection,
    run_id: str,
    decision: str,
    compliant: int,
    violations: list[tuple[str, str]],
) -> None:
    with connection:
        connection.execute(
            "INSERT OR REPLACE INTO governance_run VALUES (?, ?, ?)",
            (run_id, decision, compliant),
        )
        for asset, rule in violations:
            connection.execute(
                "INSERT OR REPLACE INTO governance_violation VALUES (?, ?, ?)",
                (run_id, asset, rule),
            )


def main() -> None:
    findings = {asset["asset"]: evaluate(asset) for asset in ASSETS}
    compliant = sum(not violations for violations in findings.values())
    violations = [
        (asset, rule)
        for asset, rules in findings.items()
        for rule in rules
    ]
    owner_coverage = 100.0 * sum(bool(asset["owner"]) for asset in ASSETS) / len(ASSETS)
    decision = "aprovado" if compliant == len(ASSETS) else "reprovado"

    database = Path(tempfile.gettempdir()) / "dataretail_governance.sqlite3"
    database.unlink(missing_ok=True)
    connection = sqlite3.connect(database)
    try:
        prepare(connection)
        persist(connection, "run-010", decision, compliant, violations)
        persist(connection, "run-010", decision, compliant, violations)
        persisted = connection.execute("SELECT COUNT(*) FROM governance_violation").fetchone()[0]

        assert compliant == 2
        assert len(violations) == persisted == 4
        print(f"ativos={len(ASSETS)}")
        print(f"conformes={compliant}")
        print(f"nao_conformes={len(ASSETS) - compliant}")
        print(f"violacoes={len(violations)}")
        print(f"cobertura_owner={owner_coverage:.2f}")
        print(f"decisao={decision}")
        print(f"violacoes_persistidas={persisted}")
        print("segunda_execucao=sem_duplicacao")
        print("governanca=ok")
    finally:
        connection.close()
    database.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
```

## Leitura da solução

As regras variam pela classificação: todo ativo exige owner, enquanto ativos mais sensíveis recebem requisitos adicionais. A avaliação separa decisão de persistência; chaves compostas preservam idempotência das evidências.

> [!warning]
> A solução é didática. Uma política real precisa de versionamento, exceções, validade temporal, identidade do avaliador e evidência íntegra da configuração avaliada.

Finalize em [[15-Referencias]].

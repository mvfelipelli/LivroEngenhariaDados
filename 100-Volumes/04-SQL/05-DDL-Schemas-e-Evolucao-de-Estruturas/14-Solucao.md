---
title: Solução — Migração Expand-Contract em SQLite
description: "Implementação validada do laboratório de evolução."
tags: [sql, sqlite, migration, solucao]
aliases: [Solução Laboratório Evolução de Schema]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Migração Expand-Contract em SQLite

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE schema_version (version INTEGER PRIMARY KEY)")
db.executescript(
    """
    CREATE TABLE pedidos (
        pedido_id INTEGER PRIMARY KEY,
        valor NUMERIC NOT NULL CHECK (valor >= 0)
    );
    INSERT INTO pedidos VALUES (1, 100.00), (2, 249.90), (3, 10.00);
    INSERT INTO schema_version VALUES (1);
    """
)

with db:
    db.execute("ALTER TABLE pedidos ADD COLUMN valor_centavos INTEGER")
    db.execute("UPDATE pedidos SET valor_centavos = ROUND(valor * 100) WHERE valor_centavos IS NULL")
    divergencias = db.execute(
        "SELECT COUNT(*) FROM pedidos WHERE valor_centavos != ROUND(valor * 100)"
    ).fetchone()[0]
    assert divergencias == 0
    db.execute("UPDATE schema_version SET version = 2")

with db:
    db.executescript(
        """
        CREATE TABLE pedidos_novo (
            pedido_id INTEGER PRIMARY KEY,
            valor_centavos INTEGER NOT NULL CHECK (valor_centavos >= 0)
        );
        INSERT INTO pedidos_novo SELECT pedido_id, valor_centavos FROM pedidos;
        DROP TABLE pedidos;
        ALTER TABLE pedidos_novo RENAME TO pedidos;
        UPDATE schema_version SET version = 3;
        """
    )

version = db.execute("SELECT version FROM schema_version").fetchone()[0]
rows = db.execute("SELECT COUNT(*) FROM pedidos").fetchone()[0]
columns = [row[1] for row in db.execute("PRAGMA table_info(pedidos)")]
total = db.execute("SELECT SUM(valor_centavos) FROM pedidos").fetchone()[0]

try:
    db.execute("INSERT INTO pedidos VALUES (4, -1)")
    raise AssertionError("constraint_nao_aplicada")
except sqlite3.IntegrityError:
    pass

assert version == 3 and rows == 3
assert columns == ["pedido_id", "valor_centavos"]
assert total == 35990

print(f"versao={version}")
print(f"linhas={rows}")
print("backfill=ok")
print("constraints=ok")
print("coluna_legada=removida")
print(f"total_centavos={total}")
print("migracao=ok")
db.close()
```

A reconstrução ocorre em transação e o contrato final é inspecionado pelo catálogo do SQLite.

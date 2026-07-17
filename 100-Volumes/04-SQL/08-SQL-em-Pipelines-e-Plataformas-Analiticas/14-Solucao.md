---
title: Solução — Carga Incremental Idempotente
description: "Implementação validada de pipeline incremental no SQLite."
tags: [sql, sqlite, pipeline, solucao]
aliases: [Solução Laboratório de Pipeline SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Carga Incremental Idempotente

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript(
    """
    CREATE TABLE origem_pedidos (
        sequencia INTEGER PRIMARY KEY,
        pedido_id INTEGER NOT NULL,
        versao INTEGER NOT NULL,
        valor_centavos INTEGER NOT NULL
    );
    CREATE TABLE staging_pedidos AS SELECT * FROM origem_pedidos WHERE 0;
    CREATE TABLE fato_pedidos (
        pedido_id INTEGER PRIMARY KEY,
        versao INTEGER NOT NULL,
        valor_centavos INTEGER NOT NULL
    );
    CREATE TABLE controle (
        pipeline TEXT PRIMARY KEY,
        watermark INTEGER NOT NULL
    );
    INSERT INTO controle VALUES ('pedidos', 0);
    INSERT INTO origem_pedidos VALUES
        (1, 101, 1, 1000),
        (2, 102, 1, 2000),
        (3, 103, 1, 500);
    """
)

def executar():
    with db:
        watermark = db.execute(
            "SELECT watermark FROM controle WHERE pipeline = 'pedidos'"
        ).fetchone()[0]
        limite = db.execute(
            "SELECT COALESCE(MAX(sequencia), ?) FROM origem_pedidos",
            (watermark,),
        ).fetchone()[0]

        db.execute("DELETE FROM staging_pedidos")
        db.execute(
            """
            INSERT INTO staging_pedidos
            SELECT sequencia, pedido_id, versao, valor_centavos
            FROM origem_pedidos
            WHERE sequencia > MAX(0, ? - 3)
              AND sequencia <= ?
            """,
            (watermark, limite),
        )

        db.execute(
            """
            INSERT INTO fato_pedidos (pedido_id, versao, valor_centavos)
            SELECT pedido_id, versao, valor_centavos
            FROM staging_pedidos
            ORDER BY sequencia
            ON CONFLICT (pedido_id) DO UPDATE SET
                versao = excluded.versao,
                valor_centavos = excluded.valor_centavos
            WHERE excluded.versao > fato_pedidos.versao
            """
        )
        db.execute(
            "UPDATE controle SET watermark = ? WHERE pipeline = 'pedidos'",
            (limite,),
        )

executar()
db.executemany(
    "INSERT INTO origem_pedidos VALUES (?, ?, ?, ?)",
    [
        (4, 101, 2, 1250),
        (5, 104, 1, 500),
        (6, 102, 0, 9999),
    ],
)
executar()

snapshot_antes = db.execute(
    "SELECT pedido_id, versao, valor_centavos FROM fato_pedidos ORDER BY pedido_id"
).fetchall()
executar()
snapshot_depois = db.execute(
    "SELECT pedido_id, versao, valor_centavos FROM fato_pedidos ORDER BY pedido_id"
).fetchall()

assert snapshot_antes == snapshot_depois
assert snapshot_depois == [
    (101, 2, 1250),
    (102, 1, 2000),
    (103, 1, 500),
    (104, 1, 500),
]
watermark = db.execute("SELECT watermark FROM controle").fetchone()[0]
total = sum(linha[2] for linha in snapshot_depois)
assert watermark == 6 and total == 4250

print(f"pedidos={len(snapshot_depois)}")
print(f"total_centavos={total}")
print("correcao=aplicada")
print("versao_antiga=ignorada")
print("reexecucao=idempotente")
print(f"watermark={watermark}")
print("pipeline=ok")
db.close()
```

O pipeline relê uma pequena sobreposição, mas a chave única e a comparação de versão fazem o destino convergir. Dados e watermark avançam na mesma transação.

---
title: Solução — SCD Tipo 2 e Lookup Temporal
description: "Implementação validada de SCD2 no SQLite."
tags: [modelagem-de-dados, sqlite, scd2, solucao]
aliases: [Solução Laboratório SCD2]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — SCD Tipo 2 e Lookup Temporal

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript(
    """
    CREATE TABLE dim_cliente (
        cliente_sk INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL,
        segmento TEXT NOT NULL,
        valido_desde TEXT NOT NULL,
        valido_ate TEXT,
        atual INTEGER NOT NULL CHECK (atual IN (0, 1)),
        UNIQUE (cliente_id, valido_desde),
        CHECK (valido_ate IS NULL OR valido_desde < valido_ate)
    );
    CREATE UNIQUE INDEX uq_cliente_atual
    ON dim_cliente (cliente_id) WHERE atual = 1;
    CREATE TABLE staging_venda (
        venda_id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL,
        ocorrido_em TEXT NOT NULL,
        valor_centavos INTEGER NOT NULL
    );
    CREATE TABLE fato_venda (
        venda_id INTEGER PRIMARY KEY,
        cliente_sk INTEGER NOT NULL REFERENCES dim_cliente(cliente_sk),
        ocorrido_em TEXT NOT NULL,
        valor_centavos INTEGER NOT NULL
    );
    INSERT INTO dim_cliente VALUES
        (1, 10, 'Bronze', '2026-07-01', '2026-07-10', 0),
        (2, 10, 'Ouro', '2026-07-10', NULL, 1);
    INSERT INTO staging_venda VALUES
        (100, 10, '2026-07-05', 1000),
        (200, 10, '2026-07-12', 2000);
    INSERT INTO fato_venda
    SELECT s.venda_id, d.cliente_sk, s.ocorrido_em, s.valor_centavos
    FROM staging_venda s
    JOIN dim_cliente d
      ON d.cliente_id = s.cliente_id
     AND d.valido_desde <= s.ocorrido_em
     AND (d.valido_ate > s.ocorrido_em OR d.valido_ate IS NULL);
    """
)

overlaps = db.execute(
    """
    SELECT COUNT(*) FROM dim_cliente a JOIN dim_cliente b
      ON a.cliente_id = b.cliente_id AND a.cliente_sk < b.cliente_sk
     AND a.valido_desde < COALESCE(b.valido_ate, '9999-12-31')
     AND b.valido_desde < COALESCE(a.valido_ate, '9999-12-31')
    """
).fetchone()[0]
agregado = dict(db.execute(
    """
    SELECT d.segmento, SUM(f.valor_centavos)
    FROM fato_venda f JOIN dim_cliente d USING (cliente_sk)
    GROUP BY d.segmento
    """
).fetchall())

versoes = db.execute("SELECT COUNT(*) FROM dim_cliente").fetchone()[0]
atuais = db.execute("SELECT COUNT(*) FROM dim_cliente WHERE atual = 1").fetchone()[0]
fatos = db.execute("SELECT COUNT(*) FROM fato_venda").fetchone()[0]
assert (versoes, atuais, fatos, overlaps) == (2, 1, 2, 0)
assert agregado == {"Bronze": 1000, "Ouro": 2000}

print(f"versoes={versoes}")
print(f"versoes_atuais={atuais}")
print(f"fatos={fatos}")
print(f"bronze_centavos={agregado['Bronze']}")
print(f"ouro_centavos={agregado['Ouro']}")
print(f"overlaps={overlaps}")
print("lookup_temporal=ok")
print("scd2=ok")
db.close()
```

O intervalo semiaberto faz a venda de 10 de julho pertencer à nova versão. A chave parcial garante apenas uma linha atual por cliente.

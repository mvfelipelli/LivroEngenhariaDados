---
title: Solução — Consulta Temporal e Expansão de JSON
description: "Implementação validada com intervalos e JSON no SQLite."
tags: [sql, sqlite, temporal, json, solucao]
aliases: [Solução Laboratório SQL Temporal e JSON]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Consulta Temporal e Expansão de JSON

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript(
    """
    CREATE TABLE historico_precos (
        sku TEXT NOT NULL,
        preco_centavos INTEGER NOT NULL,
        valido_desde TEXT NOT NULL,
        valido_ate TEXT,
        CHECK (valido_ate IS NULL OR valido_desde < valido_ate),
        PRIMARY KEY (sku, valido_desde)
    );
    CREATE TABLE eventos_pedido (
        pedido_id INTEGER PRIMARY KEY,
        ocorrido_em TEXT NOT NULL,
        payload TEXT NOT NULL CHECK (json_valid(payload))
    );

    INSERT INTO historico_precos VALUES
        ('A', 1000, '2026-07-01T00:00:00Z', '2026-07-10T00:00:00Z'),
        ('A', 1500, '2026-07-10T00:00:00Z', NULL),
        ('B', 500,  '2026-07-01T00:00:00Z', NULL);

    INSERT INTO eventos_pedido VALUES
        (1, '2026-07-05T12:00:00Z',
         '{"schema_version":1,"itens":[{"sku":"A","quantidade":2},{"sku":"B","quantidade":1}]}'),
        (2, '2026-07-12T12:00:00Z',
         '{"schema_version":1,"itens":[{"sku":"A","quantidade":1}]}');
    """
)

linhas = db.execute(
    """
    WITH itens AS (
        SELECT e.pedido_id,
               e.ocorrido_em,
               json_extract(j.value, '$.sku') AS sku,
               json_extract(j.value, '$.quantidade') AS quantidade
        FROM eventos_pedido AS e
        JOIN json_each(e.payload, '$.itens') AS j
    )
    SELECT i.pedido_id,
           i.sku,
           i.quantidade,
           p.preco_centavos,
           i.quantidade * p.preco_centavos AS subtotal_centavos
    FROM itens AS i
    JOIN historico_precos AS p
      ON p.sku = i.sku
     AND p.valido_desde <= i.ocorrido_em
     AND (p.valido_ate > i.ocorrido_em OR p.valido_ate IS NULL)
    ORDER BY i.pedido_id, i.sku
    """
).fetchall()

assert linhas == [
    (1, "A", 2, 1000, 2000),
    (1, "B", 1, 500, 500),
    (2, "A", 1, 1500, 1500),
]

pedidos = len({linha[0] for linha in linhas})
quantidade = sum(linha[2] for linha in linhas)
receita = sum(linha[4] for linha in linhas)
assert pedidos == 2 and quantidade == 4 and receita == 4000

json_validos = db.execute(
    "SELECT COUNT(*) FROM eventos_pedido WHERE json_valid(payload)"
).fetchone()[0]
assert json_validos == 2

print(f"pedidos={pedidos}")
print(f"itens_expandidos={len(linhas)}")
print(f"quantidade={quantidade}")
print(f"receita_centavos={receita}")
print("precos_temporais=corretos")
print("json=valido")
print("resultado=ok")
db.close()
```

Cada item encontra a versão cujo intervalo contém `ocorrido_em`. O array muda o grão para item do pedido antes da agregação.

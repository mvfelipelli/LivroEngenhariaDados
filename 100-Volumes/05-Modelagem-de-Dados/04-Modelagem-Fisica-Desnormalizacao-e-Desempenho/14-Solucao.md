---
title: Solução — Índice e Projeção Desnormalizada
description: "Implementação validada de acesso e reconciliação física."
tags: [modelagem-de-dados, sqlite, desempenho, solucao]
aliases: [Solução Laboratório Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Índice e Projeção Desnormalizada

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute(
    """
    CREATE TABLE pedido (
        pedido_id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL,
        criado_em INTEGER NOT NULL,
        valor_centavos INTEGER NOT NULL CHECK (valor_centavos >= 0)
    )
    """
)
db.executemany(
    "INSERT INTO pedido VALUES (?, ?, ?, ?)",
    ((i, (i % 100) + 1, i, (i * 13) % 5000) for i in range(1, 10001)),
)

consulta = """
SELECT pedido_id, criado_em, valor_centavos
FROM pedido WHERE cliente_id = 42
ORDER BY criado_em DESC LIMIT 5
"""

def plano():
    return " | ".join(linha[3] for linha in db.execute(
        "EXPLAIN QUERY PLAN " + consulta
    ))

antes = plano()
assert "SCAN pedido" in antes and "USE TEMP B-TREE" in antes

db.execute(
    "CREATE INDEX idx_pedido_cliente_data ON pedido (cliente_id, criado_em DESC)"
)
depois = plano()
assert "SEARCH pedido" in depois and "USE TEMP B-TREE" not in depois

db.executescript(
    """
    CREATE TABLE resumo_cliente (
        cliente_id INTEGER PRIMARY KEY,
        pedidos INTEGER NOT NULL,
        total_centavos INTEGER NOT NULL
    );
    INSERT INTO resumo_cliente
    SELECT cliente_id, COUNT(*), SUM(valor_centavos)
    FROM pedido GROUP BY cliente_id;
    """
)

divergencias = db.execute(
    """
    SELECT COUNT(*) FROM resumo_cliente r
    JOIN (
        SELECT cliente_id, COUNT(*) pedidos, SUM(valor_centavos) total
        FROM pedido GROUP BY cliente_id
    ) f USING (cliente_id)
    WHERE r.pedidos <> f.pedidos OR r.total_centavos <> f.total
    """
).fetchone()[0]
resumos = db.execute("SELECT COUNT(*) FROM resumo_cliente").fetchone()[0]
assert divergencias == 0 and resumos == 100

print("linhas=10000")
print("plano_antes=scan")
print("plano_depois=search")
print("ordenacao=indice")
print(f"resumos={resumos}")
print("reconciliacao=ok")
print("modelo_fisico=ok")
db.close()
```

O índice alinha filtro e ordem. O resumo acelera agregações, mas continua sendo uma projeção reconstruível e reconciliada da tabela canônica.

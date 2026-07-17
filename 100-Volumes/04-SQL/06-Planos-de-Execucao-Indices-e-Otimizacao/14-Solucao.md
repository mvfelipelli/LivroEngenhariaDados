---
title: Solução — Plano e Índice no SQLite
description: "Implementação validada da comparação de planos."
tags: [sql, sqlite, explain, solucao]
aliases: [Solução Laboratório de Plano SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Plano e Índice no SQLite

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute(
    """
    CREATE TABLE pedidos (
        pedido_id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL,
        criado_em INTEGER NOT NULL,
        valor INTEGER NOT NULL CHECK (valor >= 0)
    )
    """
)

db.executemany(
    "INSERT INTO pedidos VALUES (?, ?, ?, ?)",
    ((i, (i % 100) + 1, i, (i * 17) % 10000) for i in range(1, 10001)),
)

consulta = """
SELECT pedido_id, criado_em, valor
FROM pedidos
WHERE cliente_id = ?
ORDER BY criado_em DESC
LIMIT 5
"""

def explicar():
    return " | ".join(
        linha[3]
        for linha in db.execute("EXPLAIN QUERY PLAN " + consulta, (42,))
    )

plano_antes = explicar()
resultado_antes = db.execute(consulta, (42,)).fetchall()

assert "SCAN pedidos" in plano_antes
assert "USE TEMP B-TREE FOR ORDER BY" in plano_antes

db.execute(
    """
    CREATE INDEX idx_pedidos_cliente_criado_valor
    ON pedidos (cliente_id, criado_em DESC, valor)
    """
)

plano_depois = explicar()
resultado_depois = db.execute(consulta, (42,)).fetchall()

assert "SEARCH pedidos" in plano_depois
assert "USE TEMP B-TREE" not in plano_depois
assert resultado_antes == resultado_depois
assert len(resultado_depois) == 5

print("linhas=10000")
print("plano_antes=scan")
print("ordenacao_antes=temporaria")
print("plano_depois=search")
print("ordenacao_depois=indice")
print("resultado=equivalente")
print("otimizacao=ok")
db.close()
```

O teste usa dados determinísticos e asserções sobre plano e resultado. A coluna `criado_em` representa uma ordem temporal crescente para manter o experimento compacto.

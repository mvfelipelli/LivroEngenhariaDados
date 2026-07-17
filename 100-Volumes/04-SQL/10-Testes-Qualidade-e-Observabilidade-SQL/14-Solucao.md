---
title: Solução — Gate de Qualidade SQL
description: "Implementação validada de controles de qualidade no SQLite."
tags: [sql, sqlite, qualidade, solucao]
aliases: [Solução Laboratório Qualidade SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Gate de Qualidade SQL

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript(
    """
    CREATE TABLE clientes (cliente_id INTEGER PRIMARY KEY);
    CREATE TABLE staging_pedidos (
        pedido_id INTEGER NOT NULL,
        cliente_id INTEGER NOT NULL,
        valor_centavos INTEGER NOT NULL
    );
    CREATE TABLE fato_pedidos (
        pedido_id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL REFERENCES clientes(cliente_id),
        valor_centavos INTEGER NOT NULL CHECK (valor_centavos >= 0)
    );
    INSERT INTO clientes VALUES (10), (20);
    INSERT INTO staging_pedidos VALUES
        (1, 10, 1000), (1, 10, 1000), (2, 99, 2000), (3, 20, 3000);
    """
)

def violacoes():
    duplicidades = db.execute(
        """
        SELECT COUNT(*) FROM (
            SELECT pedido_id FROM staging_pedidos
            GROUP BY pedido_id HAVING COUNT(*) > 1
        )
        """
    ).fetchone()[0]
    referencias = db.execute(
        """
        SELECT COUNT(*)
        FROM staging_pedidos s
        LEFT JOIN clientes c ON c.cliente_id = s.cliente_id
        WHERE c.cliente_id IS NULL
        """
    ).fetchone()[0]
    return duplicidades, referencias

duplicidades, referencias = violacoes()
assert (duplicidades, referencias) == (1, 1)

db.executescript(
    """
    DELETE FROM staging_pedidos;
    INSERT INTO staging_pedidos VALUES
        (1, 10, 1000), (2, 20, 2000), (3, 20, 3000);
    """
)
assert violacoes() == (0, 0)

def publicar():
    with db:
        db.execute(
            """
            INSERT INTO fato_pedidos
            SELECT pedido_id, cliente_id, valor_centavos FROM staging_pedidos
            WHERE 1
            ON CONFLICT (pedido_id) DO UPDATE SET
                cliente_id = excluded.cliente_id,
                valor_centavos = excluded.valor_centavos
            """
        )

publicar()
antes = db.execute("SELECT * FROM fato_pedidos ORDER BY pedido_id").fetchall()
publicar()
depois = db.execute("SELECT * FROM fato_pedidos ORDER BY pedido_id").fetchall()
assert antes == depois

pedidos, receita = db.execute(
    "SELECT COUNT(*), SUM(valor_centavos) FROM fato_pedidos"
).fetchone()
origem = db.execute("SELECT SUM(valor_centavos) FROM staging_pedidos").fetchone()[0]
assert pedidos == 3 and receita == origem == 6000

print("gate_inicial=bloqueado")
print(f"duplicidades_detectadas={duplicidades}")
print(f"referencias_invalidas={referencias}")
print("gate_final=aprovado")
print(f"pedidos={pedidos}")
print(f"receita_centavos={receita}")
print("reexecucao=idempotente")
print("qualidade=ok")
db.close()
```

O gate mede violações antes da escrita. Após correção, a reconciliação financeira e a reexecução comprovam o contrato publicado.

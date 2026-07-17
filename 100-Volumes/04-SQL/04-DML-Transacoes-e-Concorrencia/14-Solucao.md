---
title: Solução — Transferência Atômica e Evento Idempotente
description: "Implementação SQLite validada do laboratório."
tags: [sql, sqlite, transacoes, solucao]
aliases: [Solução Laboratório Transações SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Transferência Atômica e Evento Idempotente

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript(
    """
    CREATE TABLE contas (
        conta_id INTEGER PRIMARY KEY,
        saldo NUMERIC NOT NULL CHECK (saldo >= 0)
    );
    CREATE TABLE eventos (
        evento_id TEXT PRIMARY KEY,
        tipo TEXT NOT NULL
    );
    CREATE TABLE outbox (
        evento_id TEXT PRIMARY KEY REFERENCES eventos(evento_id),
        payload TEXT NOT NULL
    );
    INSERT INTO contas VALUES (1, 1000), (2, 500);
    """
)


def transferir(origem, destino, valor):
    with db:
        db.execute("UPDATE contas SET saldo = saldo - ? WHERE conta_id = ?", (valor, origem))
        db.execute("UPDATE contas SET saldo = saldo + ? WHERE conta_id = ?", (valor, destino))


def processar_evento(evento_id):
    with db:
        cursor = db.execute(
            "INSERT OR IGNORE INTO eventos VALUES (?, 'pagamento')", (evento_id,)
        )
        if cursor.rowcount == 1:
            db.execute("INSERT INTO outbox VALUES (?, ?)", (evento_id, '{"status":"pago"}'))


transferir(1, 2, 200)
saldos_apos = [row[0] for row in db.execute("SELECT saldo FROM contas ORDER BY conta_id")]
assert saldos_apos == [800, 700]

try:
    transferir(1, 2, 1000)
except sqlite3.IntegrityError:
    pass
assert [row[0] for row in db.execute("SELECT saldo FROM contas ORDER BY conta_id")] == saldos_apos

processar_evento("evt-001")
processar_evento("evt-001")
events = db.execute("SELECT COUNT(*) FROM eventos").fetchone()[0]
outbox = db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0]
total = sum(float(value) for value in saldos_apos)

assert total == 1500.0 and events == 1 and outbox == 1
print(f"saldo_total={total:.2f}")
print("transferencia=ok")
print("rollback=ok")
print(f"eventos={events}")
print("idempotencia=ok")
print(f"outbox={outbox}")
print("transacao=ok")
db.close()
```

O context manager confirma em sucesso e desfaz em exceção. A chave do evento arbitra reprocessamento e protege a outbox.

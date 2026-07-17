---
title: Solução — Mini Data Vault Idempotente
description: "Implementação validada de um mini Data Vault no SQLite."
tags: [modelagem-de-dados, sqlite, data-vault, solucao]
aliases: [Solução Laboratório Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Mini Data Vault Idempotente

```python
import hashlib
import sqlite3

def hash_key(*valores):
    partes = ["<NULL>" if v is None else f"{len(str(v))}:{str(v).strip().upper()}" for v in valores]
    return hashlib.sha256("|".join(partes).encode("utf-8")).hexdigest()

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript(
    """
    CREATE TABLE hub_cliente (
        cliente_hk TEXT PRIMARY KEY, cliente_bk TEXT UNIQUE,
        load_ts TEXT, record_source TEXT
    );
    CREATE TABLE hub_pedido (
        pedido_hk TEXT PRIMARY KEY, pedido_bk TEXT UNIQUE,
        load_ts TEXT, record_source TEXT
    );
    CREATE TABLE link_pedido_cliente (
        link_hk TEXT PRIMARY KEY, pedido_hk TEXT REFERENCES hub_pedido,
        cliente_hk TEXT REFERENCES hub_cliente, load_ts TEXT, record_source TEXT
    );
    CREATE TABLE sat_cliente (
        cliente_hk TEXT REFERENCES hub_cliente, load_ts TEXT,
        hashdiff TEXT, nome TEXT, record_source TEXT,
        PRIMARY KEY (cliente_hk, load_ts)
    );
    CREATE TABLE sat_pedido (
        pedido_hk TEXT REFERENCES hub_pedido, load_ts TEXT,
        hashdiff TEXT, status TEXT, record_source TEXT,
        PRIMARY KEY (pedido_hk, load_ts)
    );
    """
)

lote = [
    ("C-10", "Ana", "P-100", "pago"),
    ("C-20", "Bia", "P-200", "aberto"),
]
load_ts = "2026-07-17T12:00:00Z"
source = "ECOMMERCE"

def carregar():
    with db:
        for cliente_bk, nome, pedido_bk, status in lote:
            cliente_hk = hash_key(cliente_bk)
            pedido_hk = hash_key(pedido_bk)
            link_hk = hash_key(pedido_bk, cliente_bk)
            db.execute("INSERT OR IGNORE INTO hub_cliente VALUES (?, ?, ?, ?)",
                       (cliente_hk, cliente_bk, load_ts, source))
            db.execute("INSERT OR IGNORE INTO hub_pedido VALUES (?, ?, ?, ?)",
                       (pedido_hk, pedido_bk, load_ts, source))
            db.execute("INSERT OR IGNORE INTO link_pedido_cliente VALUES (?, ?, ?, ?, ?)",
                       (link_hk, pedido_hk, cliente_hk, load_ts, source))
            db.execute("INSERT OR IGNORE INTO sat_cliente VALUES (?, ?, ?, ?, ?)",
                       (cliente_hk, load_ts, hash_key(nome), nome, source))
            db.execute("INSERT OR IGNORE INTO sat_pedido VALUES (?, ?, ?, ?, ?)",
                       (pedido_hk, load_ts, hash_key(status), status, source))

carregar()
antes = tuple(db.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in
              ("hub_cliente", "hub_pedido", "link_pedido_cliente", "sat_cliente", "sat_pedido"))
carregar()
depois = tuple(db.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in
               ("hub_cliente", "hub_pedido", "link_pedido_cliente", "sat_cliente", "sat_pedido"))
assert antes == depois == (2, 2, 2, 2, 2)
sources = db.execute("SELECT COUNT(DISTINCT record_source) FROM sat_cliente").fetchone()[0]
assert sources == 1

print(f"hub_cliente={depois[0]}")
print(f"hub_pedido={depois[1]}")
print(f"link_pedido_cliente={depois[2]}")
print(f"sat_cliente={depois[3]}")
print(f"sat_pedido={depois[4]}")
print("record_source=preservado")
print("reexecucao=idempotente")
print("data_vault=ok")
db.close()
```

As hash keys são reproduzíveis e as constraints tornam a repetição do lote inócua. Business keys e record source continuam disponíveis para auditoria.

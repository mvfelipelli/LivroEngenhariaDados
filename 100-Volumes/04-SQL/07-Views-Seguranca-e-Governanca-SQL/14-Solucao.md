---
title: Solução — View Mínima e Consulta Parametrizada
description: "Implementação validada do laboratório de segurança SQL."
tags: [sql, sqlite, seguranca, solucao]
aliases: [Solução Laboratório de Segurança SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — View Mínima e Consulta Parametrizada

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript(
    """
    CREATE TABLE pedidos (
        pedido_id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL,
        email TEXT NOT NULL,
        status TEXT NOT NULL,
        valor_centavos INTEGER NOT NULL
    );

    INSERT INTO pedidos VALUES
        (1, 10, 'ana@example.com', 'pago', 12990),
        (2, 20, 'bia@example.com', 'aberto', 5000),
        (3, 10, 'ana@example.com', 'pago', 2590);

    CREATE VIEW vw_pedidos_publicos AS
    SELECT pedido_id, cliente_id, valor_centavos
    FROM pedidos
    WHERE status = 'pago';
    """
)

def autorizar(acao, argumento_1, argumento_2, banco, origem):
    leitura_direta = (
        acao == sqlite3.SQLITE_READ
        and argumento_1 == "pedidos"
        and origem != "vw_pedidos_publicos"
    )
    return sqlite3.SQLITE_DENY if leitura_direta else sqlite3.SQLITE_OK

db.set_authorizer(autorizar)

linhas = db.execute(
    "SELECT pedido_id, cliente_id, valor_centavos FROM vw_pedidos_publicos"
).fetchall()
assert linhas == [(1, 10, 12990), (3, 10, 2590)]

try:
    db.execute("SELECT email FROM pedidos").fetchall()
    raise AssertionError("leitura_direta_nao_bloqueada")
except sqlite3.DatabaseError as erro:
    mensagem = str(erro).lower()
    assert "not authorized" in mensagem or "prohibited" in mensagem

entrada_hostil = "10 OR 1=1"
resultado_hostil = db.execute(
    """
    SELECT pedido_id
    FROM vw_pedidos_publicos
    WHERE cliente_id = ?
    """,
    (entrada_hostil,),
).fetchall()
assert resultado_hostil == []

colunas = [item[0] for item in db.execute(
    "SELECT * FROM vw_pedidos_publicos LIMIT 0"
).description]
assert "email" not in colunas and "status" not in colunas

print(f"linhas_view={len(linhas)}")
print("colunas_sensiveis=omitidas")
print("leitura_direta=negada")
print("consulta_parametrizada=segura")
print("resultado=ok")
db.close()
```

A função de autorização recebe a origem da leitura. Assim, a tabela participa da avaliação da view, mas uma consulta direta é negada. A entrada hostil é tratada como valor, não como fragmento SQL.

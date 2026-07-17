---
title: DB-API, Conexões, Cursores e Parâmetros
description: "Interface relacional, recursos e SQL seguro."
tags: [python, db-api, sql, parametros]
aliases: [DB-API Python]
created: 2026-07-17
updated: 2026-07-17
---

# DB-API, Conexões, Cursores e Parâmetros

PEP 249 padroniza conceitos de conexão, cursor, execução, fetch e exceções. Drivers diferem em placeholder, autocommit e extensões.

```python
import sqlite3

with sqlite3.connect("pedidos.db") as conexao:
    cursor = conexao.execute(
        "SELECT pedido_id, valor_centavos FROM pedido WHERE status = ?",
        ("aprovado",),
    )
    for pedido_id, valor in cursor:
        processar(pedido_id, valor)
```

Parâmetros são transmitidos separadamente do SQL e impedem que dados se tornem comandos. Eles não parametrizam nomes de tabela ou coluna; identificadores dinâmicos exigem allowlist e composição oferecida pelo driver.

Evite `fetchall()` para conjuntos grandes; itere ou busque em lotes. Feche cursores e conexões conforme o driver. DSNs e erros não devem aparecer completos nos logs.

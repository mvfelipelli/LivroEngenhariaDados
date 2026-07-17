---
title: Transações, Isolamento, Idempotência e Upsert
description: "Unidades atômicas e reexecução segura."
tags: [python, transacoes, idempotencia, upsert]
aliases: [Transações Python]
created: 2026-07-17
updated: 2026-07-17
---

# Transações, Isolamento, Idempotência e Upsert

Uma transação agrupa mudanças que devem confirmar ou reverter juntas. O contexto de conexão do sqlite3 confirma em sucesso e reverte em exceção.

```python
with conexao:
    conexao.execute(
        "INSERT INTO pedido(id, versao, valor) VALUES (?, ?, ?) "
        "ON CONFLICT(id) DO UPDATE SET versao=excluded.versao, valor=excluded.valor "
        "WHERE excluded.versao > pedido.versao",
        (pedido.id, pedido.versao, pedido.valor),
    )
```

Upsert só é idempotente quando a chave e a política de precedência refletem o domínio. Sob concorrência, confie em constraints e operações atômicas do banco, não em “consultar e depois inserir”.

Não mantenha transações abertas durante chamadas HTTP. Persista página e checkpoint na mesma transação para não avançar o cursor sem os dados correspondentes.

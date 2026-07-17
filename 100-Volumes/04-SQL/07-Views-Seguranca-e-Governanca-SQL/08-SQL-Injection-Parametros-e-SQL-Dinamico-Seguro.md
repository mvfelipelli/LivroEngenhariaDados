---
title: SQL Injection, Parâmetros e SQL Dinâmico Seguro
description: "Separação entre código SQL e dados não confiáveis."
tags: [sql, injection, parametros, seguranca]
aliases: [Prevenção de SQL Injection]
created: 2026-07-17
updated: 2026-07-17
---

# SQL Injection, Parâmetros e SQL Dinâmico Seguro

SQL injection ocorre quando entrada não confiável altera a estrutura da instrução. Escapar manualmente é frágil; consultas parametrizadas enviam comando e valores por canais semânticos distintos.

```python
# Correto com DB-API: o valor não vira sintaxe SQL
cursor.execute(
    "SELECT pedido_id FROM pedidos WHERE cliente_id = ?",
    (cliente_id,),
)
```

Placeholders representam **valores**, não identificadores, palavras-chave ou direção de ordenação. SQL dinâmico estrutural exige allowlist:

```python
colunas_permitidas = {"data": "criado_em", "valor": "valor"}
coluna = colunas_permitidas[ordenacao_solicitada]
sql = f"SELECT pedido_id, valor FROM pedidos ORDER BY {coluna} DESC"
```

Stored procedures e ORMs não eliminam o risco se concatenarem entrada. Menor privilégio reduz impacto, mas não corrige a vulnerabilidade. Logs devem registrar contexto da tentativa sem copiar senhas, tokens ou dados pessoais desnecessários.

> [!warning]
> Nunca forme listas, filtros ou nomes de tabela concatenando entrada bruta. Use parâmetros para valores e mapeamento fechado para estrutura.

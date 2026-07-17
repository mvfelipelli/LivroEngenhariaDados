---
title: Expressões, Funções, CASE e Conversões
description: "Derivação de valores com semântica explícita."
tags: [sql, expressoes, case, cast, funcoes]
aliases: [Expressões SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Expressões, Funções, CASE e Conversões

Expressões combinam colunas, literais, operadores e funções. Devem preservar tipos, unidades e significado do domínio.

```sql
SELECT
    pedido_id,
    valor,
    CASE
        WHEN valor >= 500 THEN 'alto'
        WHEN valor >= 100 THEN 'medio'
        ELSE 'baixo'
    END AS faixa,
    CAST(valor AS TEXT) AS valor_texto
FROM pedidos;
```

`CASE` produz um valor e pode ser usado em projeções, filtros e ordenação. `CAST` torna conversão explícita. `COALESCE(a, b)` retorna o primeiro argumento não nulo.

```sql
SELECT COALESCE(email, 'nao-informado') AS contato
FROM clientes;
```

Funções de texto, data e numéricas variam mais entre dialetos que a estrutura central do `SELECT`. Isole extensões e teste portabilidade.

> [!warning]
> Substituir `NULL` por zero ou texto vazio altera semântica. Faça isso apenas quando o domínio declarar equivalência.

Erros de arredondamento e divisão inteira também são dependentes de tipos. Para valores monetários, prefira representação decimal adequada ou unidades inteiras bem documentadas.

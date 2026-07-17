---
title: Pirâmide de Testes, Fixtures e Determinismo
description: "Camadas de teste e conjuntos mínimos de dados."
tags: [sql, testes, fixtures]
aliases: [Testes SQL Determinísticos]
created: 2026-07-17
updated: 2026-07-17
---

# Pirâmide de Testes, Fixtures e Determinismo

Testes pequenos localizam falhas rapidamente; testes integrados detectam incompatibilidades reais. Uma estratégia equilibrada usa várias camadas.

| Camada | Escopo | Exemplo |
|---|---|---|
| expressão | regra isolada | classificação de status |
| transformação | entrada e saída controladas | deduplicação |
| integração | SGBD e objetos reais | transação e tipos |
| ponta a ponta | pipeline completo | reconciliação publicada |

Fixtures devem cobrir vazio, `NULL`, duplicata, fronteira temporal, empate, valor extremo e versão atrasada. Datas e parâmetros precisam ser fixos; depender de `CURRENT_DATE` torna o resultado variável.

```sql
WITH fixture(id, valor) AS (VALUES (1, 10), (2, NULL))
SELECT id, COALESCE(valor, 0) AS valor_normalizado
FROM fixture;
```

> [!tip]
> Uma fixture pequena que expõe a regra comunica melhor que uma cópia opaca de produção.

---
title: EXPLAIN ANALYZE — Leitura de Planos e Diagnóstico
description: "Método seguro para comparar estimativas com execução real."
tags: [sql, explain, analyze, diagnostico]
aliases: [Leitura de EXPLAIN ANALYZE]
created: 2026-07-17
updated: 2026-07-17
---

# EXPLAIN ANALYZE — Leitura de Planos e Diagnóstico

`EXPLAIN` apresenta o plano estimado. No PostgreSQL, `EXPLAIN ANALYZE` executa a instrução e acrescenta tempos e cardinalidades reais. Para escrita, use uma transação descartável ou ambiente controlado.

```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE, FORMAT TEXT)
SELECT pedido_id, valor
FROM pedidos
WHERE cliente_id = 42
  AND criado_em >= TIMESTAMP '2026-07-01';
```

## Roteiro de leitura

1. confirme o resultado e o contexto da execução;
2. comece nos nós folha;
3. compare linhas estimadas e reais;
4. multiplique tempo por `loops` quando necessário;
5. observe linhas removidas por filtro;
6. procure leituras, temporários, sorts, batches e spills;
7. identifique o primeiro ponto onde a estimativa diverge;
8. meça novamente após uma única alteração.

O tempo do nó geralmente inclui seus descendentes. Por isso, somar tempos de todos os nós produz dupla contagem. Em sistemas ocupados, repetição, cache aquecido e métricas de espera são indispensáveis.

> [!warning]
> `ANALYZE` executa a consulta. Um `DELETE`, `UPDATE` ou função com efeito colateral realmente alterará estado se não houver proteção.

No SQLite, `EXPLAIN QUERY PLAN` é uma visão de diagnóstico de alto nível. `SCAN`, `SEARCH`, `USING INDEX`, `USING COVERING INDEX` e `USE TEMP B-TREE` ajudam a reconhecer o caminho, mas o formato não deve ser tratado como API estável.

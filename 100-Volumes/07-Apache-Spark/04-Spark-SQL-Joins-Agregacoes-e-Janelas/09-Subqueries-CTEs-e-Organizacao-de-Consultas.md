---
title: Subqueries, CTEs e Organização de Consultas
description: "Composição legível e verificável de SQL analítico."
tags: [apache-spark, cte, sql]
aliases: [CTEs Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Subqueries, CTEs e Organização de Consultas

CTEs nomeiam etapas lógicas e tornam granularidade explícita. Elas não garantem materialização; Catalyst pode expandi-las e reorganizar o plano.

```sql
WITH pagos AS (
  SELECT * FROM pedidos WHERE status = 'pago'
), por_loja AS (
  SELECT loja_id, SUM(valor_centavos) AS receita_centavos
  FROM pagos GROUP BY loja_id
)
SELECT * FROM por_loja WHERE receita_centavos > 0
```

Divida consultas por contratos testáveis, não por cada linha. Evite interpolar entrada externa no SQL; use APIs seguras e parâmetros da camada de aplicação. Inspecione o plano final, pois legibilidade textual não implica execução eficiente.

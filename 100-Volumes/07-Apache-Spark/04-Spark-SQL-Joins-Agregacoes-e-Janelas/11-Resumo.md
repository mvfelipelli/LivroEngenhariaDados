---
title: Resumo — Spark SQL
description: "Síntese de joins, agregações e janelas."
tags: [apache-spark, spark-sql, resumo]
aliases: [Resumo Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Resumo

- SQL e DataFrame API convergem para planos Catalyst.
- Cardinalidade e granularidade determinam correção de joins.
- Broadcast evita shuffle quando uma relação realmente cabe em memória.
- Agregações definem granularidade e podem combinar parcialmente.
- Janelas preservam linhas, mas exigem reparticionamento e ordenação.
- Deduplicação precisa de critério determinístico.
- Semântica ANSI torna erros de dados mais visíveis.
- CTE organiza lógica, mas não garante materialização.

O próximo módulo trata leitura, escrita, formatos e particionamento físico.

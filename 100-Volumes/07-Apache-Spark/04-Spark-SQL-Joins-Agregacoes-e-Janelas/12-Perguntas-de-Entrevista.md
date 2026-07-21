---
title: Perguntas de Entrevista — Spark SQL
description: "Questões comentadas sobre joins e análise distribuída."
tags: [apache-spark, spark-sql, entrevista]
aliases: [Entrevista Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Quando broadcast join é adequado?

Quando um lado é pequeno o bastante para ser replicado com segurança em todos os executors.

## Como um join multiplica linhas?

Para uma chave com `m` registros de um lado e `n` do outro, pode produzir `m × n` correspondências.

## `rank`, `dense_rank` e `row_number` diferem como?

`row_number` é sequência única; `rank` deixa lacunas após empates; `dense_rank` não deixa.

## CTE materializa o resultado?

Não necessariamente. É uma construção lógica sujeita à otimização.

## Como deduplicar deterministicamente?

Com janela ordenada por versão, timestamp e desempate estável, mantendo `row_number = 1`.

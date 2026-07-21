---
title: Laboratório — Janelas e Watermarks com a Fonte Rate
description: "Consulta streaming local, progresso e agregação por evento."
tags: [apache-spark, structured-streaming, laboratorio]
aliases: [Laboratório Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Janelas e Watermarks com a Fonte Rate

## Objetivo

Executar micro-batches, agregar por janela e inspecionar progresso e estado.

## Pré-requisitos

- PySpark configurado;
- ambiente local com duas threads;
- no Windows, `HADOOP_HOME` e `winutils.exe` configurados, pois toda query streaming mantém checkpoint, inclusive com memory sink.

## Ambiente

Use fonte `rate` com 100 linhas por segundo, watermark de dez segundos e sink em memória. O sink evita um destino externo, mas não elimina o checkpoint interno da query.

## Passos

1. Leia `timestamp` e `value` da fonte rate.
2. Derive `loja_id = value % 5`.
3. Aplique watermark e janela de cinco segundos.
4. Conte eventos por janela e loja.
5. Escreva em memory sink no modo complete.
6. Aguarde pelo menos três micro-batches.
7. Consulte o sink e `lastProgress`.
8. Pare a query em `finally`.

## Validação

Deve haver cinco lojas após dados suficientes e `numInputRows` positivo em algum progresso.

## Conclusão

O laboratório torna visíveis ritmo, janela, estado e ciclo de vida da query, inclusive a dependência do checkpoint local.

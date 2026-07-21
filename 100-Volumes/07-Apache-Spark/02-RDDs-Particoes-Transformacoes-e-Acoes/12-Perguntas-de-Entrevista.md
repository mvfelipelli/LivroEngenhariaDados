---
title: Perguntas de Entrevista — RDDs
description: "Questões comentadas sobre RDD, partições e ações."
tags: [apache-spark, rdd, entrevista]
aliases: [Entrevista RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## RDD é tolerante a qualquer falha?

Não. Linhagem recupera partições perdidas enquanto fontes e driver estiverem disponíveis. Ela não substitui saída durável nem alta disponibilidade da aplicação.

## Qual a diferença entre `repartition` e `coalesce`?

`repartition` redistribui amplamente e pode aumentar ou reduzir. `coalesce` normalmente reduz tentando evitar shuffle completo.

## Por que `reduceByKey` supera `groupByKey` em somas?

Porque agrega localmente antes de transferir dados, reduzindo rede e memória por chave.

## Quando persistir?

Quando o conjunto é reutilizado e recomputá-lo custa mais que mantê-lo no nível de armazenamento escolhido.

## Quando usar RDD em vez de DataFrame?

Quando a lógica exige objetos ou controle de baixo nível que não pode ser expresso adequadamente pelas APIs estruturadas.

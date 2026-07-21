---
title: Perguntas de Entrevista — DataFrames e Catalyst
description: "Questões comentadas sobre APIs estruturadas."
tags: [apache-spark, dataframe, entrevista]
aliases: [Entrevista DataFrame Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Por que schema explícito é preferível?

Evita varredura de inferência, documenta contrato e mantém tipos consistentes entre execuções.

## `Column` contém os dados?

Não. Ela representa uma expressão a ser resolvida e executada sobre partições.

## Por que evitar UDF Python?

Ela adiciona serialização JVM–Python e impede que Catalyst compreenda sua lógica.

## O que procurar em `explain()`?

Scans, filtros antecipados, colunas lidas, exchanges, estratégia de join e estimativas.

## Qual o risco de `explode`?

Multiplicação de cardinalidade, memória e shuffle. Meça e filtre antes da expansão.

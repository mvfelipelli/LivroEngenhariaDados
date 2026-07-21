---
title: Laboratório — Diagnóstico de Skew e Partições
description: "Comparação de distribuição desequilibrada e corrigida."
tags: [apache-spark, skew, laboratorio]
aliases: [Laboratório Otimização Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Diagnóstico de Skew e Partições

## Objetivo

Medir distribuição de uma chave quente e aplicar agregação em dois níveis com sal.

## Pré-requisitos

- PySpark configurado;
- Spark UI disponível durante a execução.

## Ambiente

Use `spark.range(1_000_000, numPartitions=8)` e AQE habilitado.

## Passos

1. Faça 80% dos registros pertencerem à chave zero.
2. Conte registros por chave e confirme o skew.
3. Observe shuffle e distribuição das tasks.
4. Adicione oito sais apenas à chave zero.
5. Agregue por chave e sal; depois, somente por chave.
6. Compare resultado, plano e duração após aquecimento.
7. Valide total de um milhão de registros.

## Validação

A saída deve conter `VALIDACAO_OK total=1000000 chaves=101` e ambas as versões devem coincidir.

## Conclusão

O laboratório demonstra que corrigir distribuição exige preservar semântica e medir custo adicional.

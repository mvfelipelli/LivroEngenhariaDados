---
title: Laboratório — Normalização Declarativa de Pedidos
description: "Schema, expressões, dados aninhados e inspeção do plano."
tags: [apache-spark, dataframe, laboratorio]
aliases: [Laboratório DataFrame Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Normalização Declarativa de Pedidos

## Objetivo

Normalizar pedidos sintéticos usando apenas funções nativas e inspecionar o plano.

## Pré-requisitos

- ambiente PySpark do Módulo 01;
- API DataFrame disponível.

## Ambiente

Use `spark.range(10_000, numPartitions=4)` para evitar dependência de arquivos externos.

## Passos

1. Derive `pedido_id`, `loja_id`, `valor_centavos` e `status`.
2. Marque como válidos apenas valores positivos e status `pago`.
3. Calcule `valor_reais` como decimal.
4. Selecione somente colunas publicadas.
5. Inspecione o plano formatado.
6. Valide 5 mil pedidos e cinco lojas.

## Validação

A execução deve imprimir `VALIDACAO_OK pedidos=5000 lojas=5` e não conter UDF Python.

## Conclusão

O laboratório demonstra uma transformação totalmente visível ao Catalyst.

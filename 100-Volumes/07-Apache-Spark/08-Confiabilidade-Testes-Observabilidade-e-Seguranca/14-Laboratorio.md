---
title: Laboratório — Contrato e Testes de Pedidos
description: "Transformação pura, qualidade e reconciliação em PySpark."
tags: [apache-spark, testes, laboratorio]
aliases: [Laboratório Confiabilidade Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Contrato e Testes de Pedidos

## Objetivo

Implementar transformação testável e validar contrato, qualidade e reconciliação.

## Pré-requisitos

- PySpark configurado;
- conceitos de DataFrame e Spark SQL.

## Ambiente

Use `spark.range(10_000, numPartitions=4)` e derive casos válidos e inválidos sem arquivos externos.

## Passos

1. Implemente `classificar_pedidos(df)` sem I/O.
2. Marque IDs divisíveis por 100 como sem identificador.
3. Marque IDs divisíveis por 77 com valor negativo.
4. Separe válidos e quarentena com motivo.
5. Valide schema publicado e ausência de valores inválidos.
6. Reconcilie entrada, válidos e quarentena.
7. Execute a função duas vezes e compare os resultados.

## Validação

A saída deve conter `VALIDACAO_OK entrada=10000 reconciliado=10000`.

## Conclusão

O laboratório transforma regras de qualidade em contratos executáveis.

---
title: Laboratório — Mart Comercial com Spark SQL
description: "Join, agregação e janela em dados sintéticos."
tags: [apache-spark, spark-sql, laboratorio]
aliases: [Laboratório Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Mart Comercial com Spark SQL

## Objetivo

Construir um mart com receita por loja e ordem das compras por cliente.

## Pré-requisitos

- PySpark configurado;
- conceitos dos Módulos 01–03.

## Ambiente

Gere pedidos com `spark.range(20_000)` e dimensão de dez lojas com `spark.range(10)`.

## Passos

1. Derive loja, cliente, valor e status.
2. Registre views temporárias.
3. Filtre pedidos pagos.
4. Faça left join com lojas e valide ausência de órfãos.
5. Agregue receita por loja.
6. Calcule `row_number` por cliente com desempate por ID.
7. Inspecione o plano e confirme broadcast da dimensão.

## Validação

A saída deve registrar `VALIDACAO_OK pagos=10000 lojas=5 orfaos=0`.

## Conclusão

O laboratório une correção relacional e verificação do plano físico.

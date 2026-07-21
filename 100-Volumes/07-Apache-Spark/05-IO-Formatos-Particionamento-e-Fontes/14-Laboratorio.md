---
title: Laboratório — Publicação Particionada em Parquet
description: "Escrita, releitura e verificação de pruning."
tags: [apache-spark, parquet, laboratorio]
aliases: [Laboratório I/O Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Publicação Particionada em Parquet

## Objetivo

Publicar pedidos em Parquet por data e validar conteúdo e plano de leitura.

## Pré-requisitos

- PySpark configurado;
- diretório temporário gravável;
- no Windows, `HADOOP_HOME` configurado para escrita local.

## Ambiente

Use `spark.range(20_000)` e duas datas sintéticas.

## Passos

1. Derive `data_negocio`, `loja_id` e `valor_centavos`.
2. Reparticione por data e escreva com Snappy.
3. Liste arquivos por partição e calcule seus tamanhos.
4. Leia apenas uma data e inspecione `PartitionFilters` no plano.
5. Valide 10 mil registros e soma esperada.
6. Repita a escrita com overwrite em diretório isolado.

## Validação

A saída deve conter `VALIDACAO_OK registros=10000 particoes=2` e o plano deve mostrar filtro de partição.

## Conclusão

O laboratório conecta layout físico, número de arquivos e leitura seletiva.

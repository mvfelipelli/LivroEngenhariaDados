---
title: Laboratório — Pipeline Spark Integrado da DataRetail
description: "Normalização, qualidade, deduplicação e mart em memória."
tags: [apache-spark, projeto-final, laboratorio]
aliases: [Laboratório Projeto Final Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Pipeline Spark Integrado da DataRetail

## Objetivo

Construir um pipeline batch em memória com contrato, quarentena, deduplicação, dimensão, mart e reconciliação.

## Pré-requisitos

- PySpark configurado;
- domínio dos módulos anteriores.

## Ambiente

Use `spark.range(100_000, numPartitions=8)` e funções nativas.

## Passos

1. Gere pedidos com ID, versão, loja, valor e status.
2. Injete IDs nulos, valores negativos e versões duplicadas.
3. Classifique válidos e quarentena.
4. Deduplicate por ID usando versão e desempate estável.
5. Enriqueca com dimensão de dez lojas por broadcast.
6. Agregue pedidos pagos e receita por loja.
7. Reconcilie entrada e qualidade; confirme ausência de órfãos.
8. Repita a transformação e compare o mart.
9. Inspecione o plano físico.

## Validação

A saída deve conter `VALIDACAO_OK entrada=100000 lojas=5 orfaos=0` e o mart repetido deve ser idêntico. Como o status pago é derivado de IDs pares, apenas as cinco lojas pares aparecem no mart.

## Conclusão

O laboratório prova o núcleo funcional sem depender de armazenamento externo; publicação e streaming seguem os contratos dos módulos anteriores.

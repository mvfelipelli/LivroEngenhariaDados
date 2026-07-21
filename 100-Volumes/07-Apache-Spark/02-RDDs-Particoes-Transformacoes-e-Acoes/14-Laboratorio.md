---
title: Laboratório — Agregação Particionada com RDDs
description: "Construção e inspeção de uma conciliação chave–valor."
tags: [apache-spark, rdd, laboratorio]
aliases: [Laboratório RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Agregação Particionada com RDDs

## Objetivo

Construir uma agregação por loja, inspecionar partições e comparar `groupByKey` com `reduceByKey`.

## Pré-requisitos

- ambiente do Módulo 01;
- workers Python funcionais;
- `pyspark==3.5.3`.

## Ambiente

Use `local[2]` e um conjunto sintético de 10 mil pedidos.

## Passos

1. Crie quatro partições com `parallelize(range(10_000), 4)`.
2. Mapeie cada ID para `(id % 10, (id % 100) + 1)`.
3. Agregue valores com `reduceByKey`.
4. Valide dez lojas e soma global `505000`.
5. Use `toDebugString()` para observar a dependência de shuffle.
6. Repita a soma com `groupByKey` apenas para comparar o plano.
7. Libere qualquer RDD persistido.

## Validação

```bash
python laboratorio_rdd.py
```

A saída deve conter `VALIDACAO_OK lojas=10 total=505000`.

## Conclusão

O experimento torna visíveis partições, shuffle e agregação local.

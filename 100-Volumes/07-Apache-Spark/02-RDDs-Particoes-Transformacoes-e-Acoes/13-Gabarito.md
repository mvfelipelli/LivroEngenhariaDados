---
title: Gabarito — RDDs e Partições
description: "Respostas dos exercícios sobre RDDs."
tags: [apache-spark, rdd, gabarito]
aliases: [Gabarito RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. Recuperável por linhagem, distribuído em processos e tratado como coleção.
2. `map` e `filter` são transformações narrow; `reduceByKey` é wide; `collect` é ação.
3. Aproximadamente 42 tasks no total, 12 mais 30.
4. `rdd.reduceByKey(lambda a, b: a + b)`.
5. O objeto pode ser serializado e replicado por tasks/executors, elevando rede e memória.
6. `cache` usa padrão; `persist` escolhe nível; checkpoint materializa e corta linhagem.
7. Salting, pré-agregação ou fluxo separado para a chave quente.
8. Parser produz registros canônicos; schema explícito valida a fronteira; DataFrame assume as transformações seguintes.

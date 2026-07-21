---
title: Criação de RDDs e Serialização
description: "Fontes, parallelize, textFile e custo de objetos."
tags: [apache-spark, rdd, serializacao]
aliases: [Criação de RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Criação de RDDs e Serialização

RDDs surgem de fontes externas, de coleções locais ou de conversão controlada. `parallelize` copia dados do driver e serve para testes, não para distribuir grandes entradas.

```python
sc = spark.sparkContext
pequeno = sc.parallelize([1, 2, 3, 4], numSlices=2)
linhas = sc.textFile("dados/pedidos/*.csv", minPartitions=8)
```

Funções e objetos usados pelas tasks precisam ser serializados. Capturar uma instância grande dentro de uma closure replica estado e aumenta tráfego. Prefira funções puras, argumentos pequenos e broadcast para referência somente leitura.

No PySpark, registros atravessam a fronteira JVM–Python. Operações estruturadas nativas evitam parte desse custo, reforçando a preferência por DataFrames.

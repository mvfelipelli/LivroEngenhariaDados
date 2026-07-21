---
title: Partições, Paralelismo e Localidade
description: "Distribuição do trabalho, quantidade de tasks e proximidade dos dados."
tags: [apache-spark, particoes, paralelismo]
aliases: [Particionamento de RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Partições, Paralelismo e Localidade

Uma task processa uma partição por stage. Poucas partições subutilizam núcleos; muitas partições pequenas elevam agendamento, abertura de arquivos e metadados.

```python
rdd = spark.sparkContext.parallelize(range(1000), 8)
assert rdd.getNumPartitions() == 8
```

`repartition(n)` redistribui os dados e pode aumentar ou reduzir partições; `coalesce(n)` normalmente reduz com menos movimento. A localidade expressa quão perto a task executa dos dados. Em armazenamento remoto, localidade de bloco perde importância, mas rede e região continuam decisivas.

O objetivo não é maximizar partições, e sim manter tasks suficientemente grandes, equilibradas e numerosas para ocupar os slots disponíveis.

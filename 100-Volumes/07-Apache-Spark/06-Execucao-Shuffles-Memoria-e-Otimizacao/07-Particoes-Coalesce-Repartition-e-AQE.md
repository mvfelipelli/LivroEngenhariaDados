---
title: Partições, Coalesce, Repartition e AQE
description: "Dimensionamento estático e adaptação em tempo de execução."
tags: [apache-spark, particoes, aqe]
aliases: [Adaptive Query Execution]
created: 2026-07-20
updated: 2026-07-20
---

# Partições, Coalesce, Repartition e AQE

Partições de entrada dependem de arquivos e splits; partições de shuffle dependem de `spark.sql.shuffle.partitions` e do AQE. `repartition` introduz exchange para equilibrar ou mudar chave; `coalesce` reduz evitando redistribuição ampla.

Adaptive Query Execution usa estatísticas de runtime para coalescer partições pós-shuffle, alterar estratégia de join e dividir partições skewed. Ele corrige incertezas, não substitui layout ou lógica adequados.

Uma meta inicial é várias tasks por núcleo disponível, com duração suficiente para amortizar agendamento e tamanho que não provoque spill excessivo. Ajuste com percentis reais, não por uma regra universal de megabytes.

Confirme `AdaptiveSparkPlan` e plano final na UI.

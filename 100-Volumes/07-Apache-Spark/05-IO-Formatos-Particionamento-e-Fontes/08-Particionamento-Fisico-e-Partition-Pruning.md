---
title: Particionamento Físico e Partition Pruning
description: "Layout de diretórios e eliminação de dados na leitura."
tags: [apache-spark, partition-pruning, layout]
aliases: [Particionamento Físico Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Particionamento Físico e Partition Pruning

`partitionBy` na escrita cria diretórios por valores, como `data=2026-07-20/`. Um filtro nessas colunas permite partition pruning. Isso não é o mesmo que `repartition`, que organiza partições de execução.

Boas colunas de partição aparecem em filtros frequentes, têm cardinalidade controlada e distribuem volume razoavelmente. Data costuma funcionar; `cliente_id` geralmente cria diretórios demais.

Dynamic partition pruning usa valores do outro lado de um join para eliminar partições em tempo de execução. Verifique no plano e nas métricas de arquivos lidos.

Partições vazias e muito pequenas indicam granularidade física excessiva ou skew.

---
title: Resumo — RDDs e Partições
description: "Síntese da API RDD e da distribuição física."
tags: [apache-spark, rdd, resumo]
aliases: [Resumo RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Resumo

- RDD é coleção imutável, particionada e reconstruível por linhagem.
- Uma task processa uma partição em cada stage.
- Dependências wide normalmente criam shuffle e nova fronteira de stage.
- Ações iniciam jobs e podem transferir resultados ao driver.
- `reduceByKey` é preferível a `groupByKey` para agregações combináveis.
- Persistência acelera reuso; checkpoint corta linhagem.
- DataFrames são preferíveis quando a estrutura pode ser declarada.

O próximo módulo introduz DataFrames, schemas, expressões e o otimizador Catalyst.

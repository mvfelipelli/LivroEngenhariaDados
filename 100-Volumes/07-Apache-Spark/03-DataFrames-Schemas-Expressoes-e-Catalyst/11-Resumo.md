---
title: Resumo — DataFrames e Catalyst
description: "Síntese das APIs estruturadas e do otimizador."
tags: [apache-spark, dataframe, resumo]
aliases: [Resumo DataFrame Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Resumo

- DataFrames combinam partições distribuídas com schema e expressões.
- Schema explícito é contrato e reduz inferência imprevisível.
- Colunas são expressões, não valores locais.
- Funções nativas preservam visibilidade ao Catalyst.
- Estruturas aninhadas podem ser tratadas sem UDF.
- Catalyst analisa, otimiza e gera alternativas físicas.
- Tungsten reduz objetos e melhora execução JVM.

O próximo módulo aplica essas bases a Spark SQL, joins, agregações e janelas.

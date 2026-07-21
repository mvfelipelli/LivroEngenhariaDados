---
title: Encoders, Codegen e Tungsten
description: "Representação interna, geração de código e eficiência de memória."
tags: [apache-spark, tungsten, codegen]
aliases: [Tungsten Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Encoders, Codegen e Tungsten

Tungsten reúne técnicas de execução: formato binário compacto, gerenciamento de memória, operadores cache-aware e geração de código. Whole-stage code generation combina operadores compatíveis em funções JVM, reduzindo virtual dispatch e objetos intermediários.

Na API Scala, Datasets usam encoders para converter objetos tipados à representação interna. PySpark trabalha principalmente com DataFrames e cruza processos quando exige lógica Python.

`explain()` pode mostrar operadores prefixados por asterisco em regiões de codegen. UDFs, alguns operadores e fronteiras de exchange podem quebrar a fusão.

> [!note]
> “Em memória” não significa “sem disco”: shuffle, spill, cache e tolerância a falhas utilizam armazenamento conforme necessário.

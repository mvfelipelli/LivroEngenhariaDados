---
title: Funções Nativas, UDFs e Fronteiras de Execução
description: "Visibilidade ao otimizador e custo da execução Python."
tags: [apache-spark, udf, funcoes]
aliases: [UDF Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Funções Nativas, UDFs e Fronteiras de Execução

Funções de `pyspark.sql.functions` geram expressões JVM compreendidas pelo Catalyst. UDF Python serializa dados para workers e oculta a lógica do otimizador. Pandas UDF usa Arrow em lotes, reduzindo custo por linha, mas mantém fronteira de linguagem.

Ordem preferencial:

1. expressão nativa;
2. SQL ou função de ordem superior;
3. pandas UDF quando vetorização é adequada;
4. UDF Python escalar como último recurso.

Toda UDF precisa declarar tipo de retorno, comportamento para nulos, determinismo e testes de casos extremos. Não faça chamadas de rede por registro dentro de UDF.

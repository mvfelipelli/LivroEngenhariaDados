---
title: Testes Unitários, Integração e Regressão
description: "Pirâmide de testes para aplicações distribuídas."
tags: [apache-spark, testes, regressao]
aliases: [Testes Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Testes Unitários, Integração e Regressão

Testes unitários validam transformações com datasets mínimos; integração verifica conectores e configuração; ponta a ponta cobre publicação e recuperação; regressão compara contratos e resultados de referência.

Compare DataFrames sem depender da ordem, exceto quando a ordem faz parte do contrato. Verifique schema, tipos, nulabilidade e multiplicidade, não apenas linhas.

Casos mínimos incluem nulos, duplicatas, limite numérico, timezone, coleção vazia, chave ausente e registro tardio. Testes baseados em propriedades validam invariantes como conservação de contagem ou soma.

Uma `SparkSession` compartilhada por suíte reduz custo, mas cada teste deve limpar views, cache e configuração modificada.

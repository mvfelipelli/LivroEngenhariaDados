---
title: Perguntas de Entrevista — Otimização Spark
description: "Questões comentadas sobre diagnóstico de desempenho."
tags: [apache-spark, performance, entrevista]
aliases: [Entrevista Otimização Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Como reconhecer skew?

Poucas tasks têm bytes, spill e duração muito acima da mediana, frequentemente associados a chaves concentradas.

## Spill é sempre ruim?

Não. Ele permite concluir sob pressão de memória; excesso recorrente indica partições ou estruturas inadequadas.

## Mais executors sempre aceleram?

Não. Fonte, serialização, skew, etapas seriais e limites de rede podem dominar.

## Quando usar cache?

Quando o mesmo resultado caro é reutilizado e cabe no nível escolhido sem prejudicar execução.

## O que AQE pode mudar?

Coalescer partições, tratar skew e alterar algumas estratégias de join durante a execução.

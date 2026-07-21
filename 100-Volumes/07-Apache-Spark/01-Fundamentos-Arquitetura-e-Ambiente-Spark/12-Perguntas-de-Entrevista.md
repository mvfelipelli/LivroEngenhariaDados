---
title: Perguntas de Entrevista — Fundamentos Spark
description: "Questões comentadas sobre arquitetura e execução."
tags: [apache-spark, entrevista]
aliases: [Entrevista Fundamentos Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Qual é a diferença entre driver e executor?

O driver constrói planos e agenda trabalho. Executors executam tasks e armazenam partições. Perder o driver normalmente encerra a aplicação; partições perdidas podem ser reconstruídas pela linhagem.

## O que dispara um job?

Uma ação que exige materialização, como `count` ou escrita. Transformações apenas ampliam o plano.

## Stage e task são sinônimos?

Não. Um stage agrupa transformações sem redistribuição ampla. Tasks aplicam esse trabalho às partições.

## Por que `collect()` é perigoso?

Porque transfere todos os registros ao driver e pode esgotar sua memória.

## Quando não usar Spark?

Para dados pequenos, transações unitárias ou serving de latência muito baixa.

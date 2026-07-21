---
title: Perguntas de Entrevista — Operação Spark
description: "Questões comentadas sobre cluster e deploy."
tags: [apache-spark, operacao, entrevista]
aliases: [Entrevista Operação Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Client e cluster mode diferem como?

No client, driver fica no processo submetente; no cluster, fica sob gestão do cluster.

## Por que um import funciona no driver e falha no executor?

A dependência pode existir apenas no host do driver e não ter sido distribuída ou instalada na imagem.

## Dynamic allocation sempre reduz custo?

Não. Ramp-up, churn, estado e limites incorretos podem aumentar latência ou recomputação.

## Rollback de código restaura dados?

Não automaticamente. Saídas e migrações exigem versionamento e estratégia de restauração.

## O que medir além de duração?

Freshness, correção, falhas, recursos, backlog e custo por unidade de dados.

---
title: Perguntas de Entrevista — Confiabilidade Spark
description: "Questões comentadas sobre testes e operação segura."
tags: [apache-spark, confiabilidade, entrevista]
aliases: [Entrevista Confiabilidade Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Como testar uma transformação Spark?

Separá-la de I/O, usar dataset mínimo, comparar schema e linhas sem ordem acidental e cobrir limites.

## Job concluído prova qualidade?

Não. É preciso validar invariantes, contagens, somas, atualidade e quarentena.

## O que torna backfill seguro?

Entrada e código versionados, intervalo explícito, escrita idempotente, reconciliação e publicação isolada.

## Onde não colocar segredos?

Código, Git, argumentos, logs, notebooks, variáveis exibidas e configurações públicas.

## Event log substitui logs da aplicação?

Não. Ele detalha execução Spark; regras de negócio e decisões precisam de telemetria própria correlacionada.

---
title: Perguntas de Entrevista — Projeto Spark
description: "Questões integradoras de arquitetura e operação."
tags: [apache-spark, projeto-final, entrevista]
aliases: [Entrevista Projeto Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Como combinar batch e streaming?

Compartilhar contratos e transformações, definir precedência/versionamento e usar batch para reconciliação histórica.

## Como provar idempotência?

Executar a mesma unidade repetidamente e comparar chaves, contagens, somas e estado publicado.

## O que torna quarentena auditável?

Payload permitido, motivo, origem, versão, run, retenção, acesso e reconciliação.

## Como estimar capacidade streaming?

Medir pico, taxa sustentável, backlog, duração de falha e margem para recuperar mais rápido que a chegada.

## Qual é o critério de produção?

Correção, replay, recuperação, SLO, custo, segurança e operação demonstrados por evidência.

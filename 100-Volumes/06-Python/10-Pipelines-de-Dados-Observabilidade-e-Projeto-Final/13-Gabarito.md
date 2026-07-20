---
title: Gabarito — Pipelines e Observabilidade Python
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, pipelines]
aliases: [Gabarito Projeto Final Python]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

## 1

Domínio valida eventos; aplicação coordena; port descreve source/sink; adapters implementam CSV e banco.

## 2

JSON e valor negativo são erros de dados previstos; banco indisponível é falha sistêmica.

## 3

Use tupla `(timestamp, id)` e condição lexicográfica, ou cursor opaco fornecido pela origem.

## 4

Chave `pedido_id`; maior versão vence; empate divergente deve ser rejeitado ou desempatar por regra explícita.

## 5

Uma falha intermediária perde dados porque a próxima execução começa depois deles.

## 6

Use checkpoint e destino de backfill separados, intervalo fechado e promoção após reconciliação.

## 7

Logs por run_id; métricas de volume, rejeição, duração e freshness; SLO temporal; alerta acionável com runbook.

## 8

Leia após checkpoint, valide, faça upsert e quarantine, atualize linha na mesma transação e repita para provar estabilidade.

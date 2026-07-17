---
title: Exercícios
description: "Exercícios progressivos de SQL incremental e analítico."
tags: [sql, exercicios, pipelines]
aliases: [Exercícios SQL em Pipelines]
created: 2026-07-17
updated: 2026-07-17
---

# Exercícios

## 1 — Contrato

Defina grão, chave e invariantes de uma tabela de pagamentos.

## 2 — Staging

Explique por que validar diretamente na tabela publicada é arriscado.

## 3 — Watermark

Mostre como `(atualizado_em, pedido_id)` evita perda em empates.

## 4 — Atraso

Projete uma janela incremental para dados com atraso de até seis horas.

## 5 — Deduplicação

Escreva uma CTE que mantenha o evento mais recente por `evento_id`.

## 6 — Upsert

Explique como impedir regressão de versão no destino.

## 7 — Dimensional

Compare fato transacional, snapshot periódico e SCD Tipo 2.

## 8 — Desafio operacional

Projete um backfill de um ano em warehouse cobrado por bytes, com validação e rollback.

---
title: Exercícios
description: "Exercícios progressivos de diagnóstico e projeto de índices."
tags: [sql, exercicios, otimizacao]
aliases: [Exercícios de Otimização SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Exercícios

## 1 — Conceitos

Explique cardinalidade, seletividade e custo e descreva como se relacionam.

## 2 — Operador

Uma consulta retorna 90% das linhas. Justifique por que o sequential scan pode superar um index scan.

## 3 — SARGabilidade

Reescreva `WHERE DATE(criado_em) = DATE '2026-07-17'` como intervalo.

## 4 — Índice composto

Projete um índice para filtrar por `loja_id`, ordenar por `criado_em DESC` e retornar `valor`.

## 5 — Estimativa

Um nó estimou 100 linhas e produziu 800.000. Indique três causas investigáveis.

## 6 — Join

Compare nested loop e hash join para cruzar duas tabelas de dez milhões de linhas por igualdade.

## 7 — Plano

Uma consulta lê 5 milhões de linhas, remove 4.999.990 no filtro e devolve 10. Qual é a hipótese inicial e como testá-la?

## 8 — Desafio operacional

Elabore um plano seguro para criar um índice grande em produção, validar o ganho e permitir rollback.

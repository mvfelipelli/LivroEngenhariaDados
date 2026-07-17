---
title: Exercícios — DML, Transações e Concorrência
description: "Atividades progressivas sobre mutações e isolamento."
tags: [sql, exercicios, transacoes]
aliases: [Exercícios Transações SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Exercícios

## Revisão

1. Diferencie atomicidade, consistência, isolamento e durabilidade.
2. Explique `COMMIT`, `ROLLBACK` e `SAVEPOINT`.

## Interpretação

3. Identifique a corrida em “SELECT antes de INSERT”.
4. Explique dirty read, nonrepeatable read e phantom.
5. Descreva um deadlock entre duas contas.

## Aplicação

6. Escreva um upsert que rejeite versões atrasadas.
7. Projete transferência atômica com saldo não negativo.
8. Defina retry para serialization failure.

## Desafio

9. Modele callback de pagamento idempotente com chave de evento.
10. Projete outbox e métricas operacionais para publicação confiável.

Compare com [[13-Gabarito|o gabarito]] antes do laboratório.

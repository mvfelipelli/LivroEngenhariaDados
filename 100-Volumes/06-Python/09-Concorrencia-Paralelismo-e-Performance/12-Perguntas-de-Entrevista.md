---
title: Perguntas de Entrevista — Concorrência Python
description: "Questões sobre threads, processos, asyncio e profiling."
tags: [python, entrevista, concorrencia]
aliases: [Entrevista Concorrência Python]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Concorrência e paralelismo diferem como?

Concorrência coordena tarefas sobrepostas; paralelismo executa trabalho simultaneamente.

## 2. GIL impede qualquer paralelismo?

Não. Processos e extensões nativas que liberam o GIL podem usar múltiplos núcleos; threads sobrepõem I/O.

## 3. Lock torna estrutura thread-safe automaticamente?

Somente se todas as operações que preservam a mesma invariante usarem corretamente a região crítica.

## 4. Quando usar processos?

Em cálculo CPU-bound suficientemente grande para superar startup, serialização e IPC.

## 5. O que bloqueia o event loop?

Código síncrono demorado ou I/O bloqueante executado diretamente em coroutine.

## 6. Por que TaskGroup?

Vincula criação, espera, falha e cancelamento das tasks a um escopo estruturado.

## 7. Semáforo e rate limiter são iguais?

Não. Semáforo limita simultaneidade; rate limiter limita eventos por intervalo.

## 8. Qual a primeira otimização?

Medir e eliminar trabalho desnecessário no gargalo dominante antes de paralelizar.

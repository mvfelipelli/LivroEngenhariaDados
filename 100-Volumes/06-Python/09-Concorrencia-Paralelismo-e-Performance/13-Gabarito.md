---
title: Gabarito — Concorrência e Performance Python
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, concorrencia]
aliases: [Gabarito Concorrência Python]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Download e query aguardam I/O; compressão costuma consumir CPU, embora também leia e escreva.

## 2

Leitura-modificação-escrita pode intercalar. Use Lock, fila com owner único ou redução por worker.

## 3

Startup, agendamento, pickle e IPC podem exceder o cálculo; agrupe tarefas maiores.

## 4

Crie uma task por item dentro de TaskGroup, aguarde o bloco e ordene por chave antes de publicar.

## 5

Libere recurso no finally e não capture permanentemente `asyncio.CancelledError`.

## 6

Defina maxsize pela memória e latência; `await queue.put` desacelera o produtor quando cheia.

## 7

Meça throughput, p50/p95, CPU, memória e erros com mesma carga, aquecimento e repetições.

## 8

Use Semaphore(2), timeout por tentativa, loop limitado de retry e dicionário indexado antes da ordenação.

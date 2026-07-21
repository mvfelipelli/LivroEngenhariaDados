---
title: Perguntas de Entrevista — Structured Streaming
description: "Questões comentadas sobre tempo, estado e garantias."
tags: [apache-spark, structured-streaming, entrevista]
aliases: [Entrevista Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Watermark descarta imediatamente todo evento atrasado?

Não. Ele fornece uma fronteira para limpeza de estado; comportamento depende da operação e modo de saída.

## Event time e processing time diferem como?

O primeiro pertence ao evento no domínio; o segundo indica quando a plataforma o processa.

## Por que stream-stream join precisa de intervalo?

Para determinar quando correspondências futuras deixam de ser possíveis e remover estado.

## Checkpoint pode ser compartilhado?

Não entre queries independentes. Cada query precisa de localização exclusiva.

## `foreachBatch` é exactly-once?

Por padrão, não no destino. A função deve usar `batch_id` e escrita idempotente ou transacional.

---
title: Resumo — Structured Streaming
description: "Síntese de processamento incremental e estado."
tags: [apache-spark, structured-streaming, resumo]
aliases: [Resumo Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Resumo

- Structured Streaming executa planos estruturados incrementalmente.
- Trigger define ritmo, não capacidade de processamento.
- Event time preserva semântica de negócio sob atraso.
- Watermark limita estado e define política para tardios.
- Operações stateful exigem monitoramento e compatibilidade de checkpoint.
- Stream-stream join precisa de restrição temporal.
- Output mode deve corresponder à evolução do resultado.
- Exactly-once precisa ser provado da fonte ao sink.

O próximo módulo trata confiabilidade, testes, observabilidade e segurança.

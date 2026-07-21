---
title: Fontes, Sinks e Modos de Saída
description: "Integrações e semântica de publicação incremental."
tags: [apache-spark, streaming-sinks, output-mode]
aliases: [Sinks Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Fontes, Sinks e Modos de Saída

Fontes fornecem offsets ou progresso equivalente. Kafka, arquivos e `rate` possuem semânticas diferentes. Sinks devem aceitar a forma como o resultado evolui.

`append` publica apenas linhas finalizadas; `update` publica linhas alteradas; `complete` reescreve toda a tabela de resultado e só é viável para estado limitado. Nem toda consulta suporta todo modo.

```python
eventos = (spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", servidores)
    .option("subscribe", topico)
    .load())
```

Console e memory sink servem para testes. Produção exige contrato de idempotência, particionamento, retenção e observabilidade do destino.

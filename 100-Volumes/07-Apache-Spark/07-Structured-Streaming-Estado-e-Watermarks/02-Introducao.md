---
title: Introdução ao Structured Streaming
description: "Modelo declarativo para dados ilimitados."
tags: [apache-spark, structured-streaming, introducao]
aliases: [Introdução Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Introdução

Uma consulta streaming descreve transformações sobre uma tabela de entrada que recebe novas linhas. O mecanismo acompanha quais dados foram consumidos e atualiza a tabela de resultado incrementalmente.

```mermaid
flowchart LR
    F["Fonte contínua"] --> B["Novo intervalo"]
    B --> Q["Plano incremental"]
    Q --> S["Estado"]
    Q --> O["Sink"]
    Q --> C["Checkpoint"]
```

Baixa latência não elimina batch: o modo padrão usa micro-batches pequenos. A confiabilidade depende da combinação entre fonte, checkpoint, transformação e sink, não de uma opção isolada.

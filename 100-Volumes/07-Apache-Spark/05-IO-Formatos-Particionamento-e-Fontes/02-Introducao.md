---
title: Introdução ao I/O no Spark
description: "O caminho entre armazenamento e processamento distribuído."
tags: [apache-spark, io, introducao]
aliases: [Introdução I/O Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Introdução

Leitura converte bytes e metadados em partições; escrita faz o caminho inverso. Desempenho depende de quantidade de arquivos, compressão, projeção, filtros, latência da fonte e capacidade de commit.

```mermaid
flowchart LR
    S["Fonte"] --> D["Data Source"]
    D --> P["Partições Spark"]
    P --> T["Transformações"]
    T --> W["Writer"]
    W --> O["Destino"]
```

Um formato eficiente não corrige layout ruim. Milhões de arquivos pequenos ou partições por chave de alta cardinalidade tornam metadados e listagem o gargalo antes que as tasks processem dados.

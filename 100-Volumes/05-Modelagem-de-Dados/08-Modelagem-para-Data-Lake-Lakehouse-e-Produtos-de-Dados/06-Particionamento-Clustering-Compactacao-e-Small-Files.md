---
title: Particionamento, Clustering, Compactação e Small Files
description: "Layout físico para pruning e operação sustentável."
tags: [particionamento, clustering, compactacao, small-files]
aliases: [Layout Lakehouse]
created: 2026-07-17
updated: 2026-07-17
---

# Particionamento, Clustering, Compactação e Small Files

Partições devem corresponder a filtros frequentes e produzir volume suficiente por parte. Particionar por identificador de alta cardinalidade cria diretórios e arquivos excessivos.

Clustering ordena ou agrupa dados dentro de partições. Tabelas modernas podem ocultar transformação da partição, reduzindo acoplamento da consulta ao layout físico.

Small files surgem de microbatches, alta cardinalidade e writers paralelos. Eles aumentam listagem, planejamento e metadados. Compactação reescreve arquivos em tamanhos-alvo e precisa de agenda, isolamento e custo controlado.

```mermaid
flowchart LR
    S1["Arquivo pequeno"] --> C["Compactação"]
    S2["Arquivo pequeno"] --> C
    S3["Arquivo pequeno"] --> C
    C --> G["Arquivo otimizado"]
```

> [!warning]
> Particionamento é decisão física evolutiva; não incorpore caminho de pasta como semântica permanente do consumidor.

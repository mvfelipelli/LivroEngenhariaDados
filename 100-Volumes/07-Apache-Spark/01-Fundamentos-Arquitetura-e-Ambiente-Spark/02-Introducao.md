---
title: Introdução aos Fundamentos Spark
description: "Modelo mental inicial para processamento distribuído."
tags: [apache-spark, introducao]
aliases: [Introdução Fundamentos Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Introdução

Uma máquina possui limites de CPU, memória, armazenamento e vazão. O Spark divide dados e computação entre processos, mas acrescenta coordenação, serialização, rede e recuperação. Distribuir é uma troca: capacidade e paralelismo em troca de complexidade.

```mermaid
flowchart LR
    F["Fonte"] --> D["Partições"]
    D --> E1["Executor 1"]
    D --> E2["Executor 2"]
    E1 --> R["Resultado"]
    E2 --> R
```

As operações formam um plano e o processamento começa quando uma ação exige resultado. Essa separação permite otimizar o trabalho completo.

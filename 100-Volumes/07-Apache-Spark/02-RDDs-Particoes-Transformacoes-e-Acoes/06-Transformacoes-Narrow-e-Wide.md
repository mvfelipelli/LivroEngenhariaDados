---
title: Transformações Narrow e Wide
description: "Dependências locais, shuffles e fronteiras entre stages."
tags: [apache-spark, transformacoes, shuffle]
aliases: [Narrow e Wide Dependencies]
created: 2026-07-20
updated: 2026-07-20
---

# Transformações Narrow e Wide

Em dependência narrow, cada partição filha depende de poucas partições ancestrais e as operações podem ser encadeadas na mesma task. `map`, `filter` e `mapPartitions` são exemplos usuais.

Em dependência wide, uma partição filha pode receber dados de muitas ancestrais. `groupByKey`, `reduceByKey`, `distinct` e ordenação normalmente provocam shuffle e nova fronteira de stage.

```mermaid
flowchart LR
    P1["p0"] --> M1["map p0"]
    P2["p1"] --> M2["map p1"]
    M1 --> S1["chave A"]
    M1 --> S2["chave B"]
    M2 --> S1
    M2 --> S2
```

Shuffle envolve serialização, disco e rede. Ele não é erro por si; torna-se problema quando desnecessário, desequilibrado ou dimensionado incorretamente.

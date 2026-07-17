---
title: Introdução
description: "Do modelo lógico ao comportamento real do armazenamento."
tags: [modelagem-de-dados, introducao, desempenho]
aliases: [Introdução à Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

O mesmo modelo lógico pode ser implementado em banco transacional, warehouse colunar ou lakehouse. Cada ambiente possui unidade de I/O, concorrência, distribuição e custos distintos.

```mermaid
flowchart TD
    Q["Padrões de consulta"] --> D["Decisões físicas"]
    E["Padrões de escrita"] --> D
    V["Volume e crescimento"] --> D
    S["SLO e custo"] --> D
    D --> B["Benchmark"]
    B --> R["Revisão"]
```

Uma otimização local pode prejudicar o sistema: índices aceleram leitura, mas ampliam escrita; partições ajudam pruning, mas podem criar muitos arquivos; desnormalização reduz joins, mas introduz consistência derivada.

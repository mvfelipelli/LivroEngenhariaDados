---
title: Aplicações, Jobs, Stages e Tasks
description: "Hierarquia operacional da execução Spark."
tags: [apache-spark, jobs, stages, tasks]
aliases: [Hierarquia de Execução Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Aplicações, Jobs, Stages e Tasks

Uma aplicação abrange driver e executors. Uma ação costuma criar um job. O job é dividido em stages nas fronteiras de redistribuição. Cada stage contém tasks, normalmente uma por partição.

```mermaid
flowchart LR
    A["Aplicação"] --> J["Job"]
    J --> S1["Stage 1"]
    J --> S2["Stage 2"]
    S1 --> T1["Task p0"]
    S1 --> T2["Task p1"]
```

Uma partição enorme produz task longa; partições minúsculas geram sobrecarga. Essa hierarquia conecta código às métricas da Spark UI.

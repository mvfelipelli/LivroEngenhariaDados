---
title: Logs, Métricas, Event Logs e Lineage
description: "Telemetria correlacionada para operação e investigação."
tags: [apache-spark, observabilidade, lineage]
aliases: [Observabilidade Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Logs, Métricas, Event Logs e Lineage

Logs estruturados devem incluir aplicação, execução, dataset, partição lógica, versão e erro. Não registre payload sensível. Métricas técnicas cobrem duração, retries, shuffle e estado; métricas de dados cobrem entrada, saída, quarentena, atraso e reconciliação.

Event logs alimentam History Server e explicam execução física. Lineage registra fontes, transformações e destinos em nível de dataset ou coluna, permitindo análise de impacto e auditoria.

```mermaid
flowchart LR
    A["application_id"] --> L["Logs"]
    A --> M["Métricas"]
    A --> E["Event log"]
    A --> D["Run de dados"]
```

Alertas devem representar impacto e ação possível; cardinalidade descontrolada de labels pode derrubar o sistema de métricas.

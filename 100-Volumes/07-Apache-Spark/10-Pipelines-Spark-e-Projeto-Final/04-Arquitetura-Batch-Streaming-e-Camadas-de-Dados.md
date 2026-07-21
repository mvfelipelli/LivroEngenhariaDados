---
title: Arquitetura Batch, Streaming e Camadas de Dados
description: "Fluxos convergentes e contratos de camadas."
tags: [apache-spark, arquitetura, batch-streaming]
aliases: [Arquitetura Projeto Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Arquitetura Batch, Streaming e Camadas de Dados

Streaming captura eventos e produz visão recente; batch reconcilia o histórico autoritativo. Ambos reutilizam funções canônicas de normalização e qualidade. A convergência ocorre em tabelas com chave, versão e regra de precedência explícitas.

Bronze preserva payload, metadados e sequência. Silver aplica schema, deduplicação e semântica. Gold materializa granularidades de consumo. Quarentena não é lixo: possui motivo, origem, versão e ciclo de correção.

```mermaid
flowchart TB
    K["Kafka"] --> ST["Structured Streaming"]
    O["Object Storage"] --> BA["Batch Spark"]
    ST --> BR["Bronze"]
    BA --> BR
    BR --> SI["Silver canônica"]
    SI --> GO["Gold"]
    SI --> RE["Reconciliação"]
```

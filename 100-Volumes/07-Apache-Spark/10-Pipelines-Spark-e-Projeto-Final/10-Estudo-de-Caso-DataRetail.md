---
title: Estudo de Caso — Plataforma Spark da DataRetail
description: "Projeto completo de pedidos, receita e operação."
tags: [apache-spark, projeto-final, dataretail]
aliases: [Caso Final DataRetail Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — Plataforma Spark da DataRetail

A DataRetail implementa o projeto em três incrementos. Primeiro, batch diário cria Bronze e Silver com reconciliação. Depois, Gold publica receita e recorrência. Por fim, streaming antecipa a visão intradiária, reconciliada pelo batch seguinte.

```mermaid
flowchart LR
    E["Eventos + arquivos"] --> B["Bronze auditável"]
    B --> S["Silver idempotente"]
    S --> G["Gold comercial"]
    B --> Q["Quarentena"]
    G --> BI["Consumo"]
    S --> OB["Observabilidade"]
    G --> OB
```

No teste final, um evento duplicado, uma chave skewed e uma falha de publicação são injetados. O pipeline deduplica, mantém SLA e preserva a versão anterior até o retry aprovado.

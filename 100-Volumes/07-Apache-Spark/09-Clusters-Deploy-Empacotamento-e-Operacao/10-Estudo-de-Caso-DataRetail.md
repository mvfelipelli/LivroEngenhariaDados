---
title: Estudo de Caso — Deploy Spark da DataRetail
description: "Promoção e operação de um pipeline comercial."
tags: [apache-spark, operacao, dataretail]
aliases: [Caso DataRetail Operação]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — Deploy Spark

A DataRetail empacota o pipeline em imagem identificada por digest. CI executa testes e scan; CD promove a mesma imagem ao cluster Kubernetes com service account e configurações do ambiente.

O deploy começa em shadow para um dia recente. Contagem, soma em centavos e distribuição por loja são comparadas à versão atual. Após aprovação, uma referência de tabela muda para a nova saída.

```mermaid
flowchart LR
    I["Imagem imutável"] --> SH["Shadow"]
    SH --> C["Comparação"]
    C -->|aprovada| P["Publicação"]
    C -->|divergente| R["Rollback"]
    P --> S["SLO + custo"]
```

Runbooks cobrem pod do driver, falta de executors, throttling da fonte e falha de publicação.

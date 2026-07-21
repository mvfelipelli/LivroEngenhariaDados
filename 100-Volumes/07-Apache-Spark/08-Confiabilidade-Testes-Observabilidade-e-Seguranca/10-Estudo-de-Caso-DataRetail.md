---
title: Estudo de Caso — Pipeline Confiável da DataRetail
description: "Contratos, telemetria e recuperação de pedidos."
tags: [apache-spark, confiabilidade, dataretail]
aliases: [Caso DataRetail Confiabilidade]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — Pipeline Confiável

A DataRetail publica pedidos curados sob contrato de unicidade, valores não negativos e atraso máximo. Transformações puras são testadas; integração valida catálogo e permissões; um dataset dourado protege regras monetárias.

```mermaid
flowchart LR
    C["Contrato"] --> V["Validação"]
    V --> P["Processamento"]
    P --> R["Reconciliação"]
    R --> O["Publicação"]
    P --> Q["Quarentena"]
    O --> M["Métricas + lineage"]
```

Cada run registra código, entrada, contagens e somas. A identidade Spark lê apenas a zona necessária e grava staging/destino. Um teste de desastre interrompe o commit, confirma ausência de publicação parcial e repete a execução com o mesmo resultado.

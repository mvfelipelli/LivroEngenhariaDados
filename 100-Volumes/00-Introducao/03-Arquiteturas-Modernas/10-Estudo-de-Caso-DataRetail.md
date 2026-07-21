---
title: Estudo de Caso — Arquitetura Evolutiva da DataRetail
description: "Escolhas graduais para integração e consumo."
tags: [arquitetura-de-dados, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Arquitetura]
created: 2026-07-21
updated: 2026-07-21
---

# Estudo de Caso — Arquitetura Evolutiva da DataRetail

A DataRetail inicia com batch diário, object storage e Warehouse de consumo. Eventos do e-commerce são preservados em log durável, mas só o caso de fraude exige processamento contínuo.

```mermaid
flowchart LR
    ERP["ERP/CRM"] --> B["Ingestão batch"]
    WEB["Eventos web"] --> LOG["Log durável"]
    LOG --> ST["Fraude streaming"]
    LOG --> B
    B --> LAKE["Camadas abertas"]
    LAKE --> WH["Warehouse/Marts"]
    ST --> ALERT["Alertas"]
```

Essa solução evita duplicar toda lógica em batch e streaming. Contratos unem caminhos; batch reconcilia histórico. ADRs registram por que baixa latência foi limitada ao caso que a justifica.

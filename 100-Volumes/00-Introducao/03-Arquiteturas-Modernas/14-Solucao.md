---
title: Solução — Decisão Arquitetural da DataRetail
description: "ADR de referência para batch e streaming seletivo."
tags: [arquitetura-de-dados, solucao, dataretail]
aliases: [Solução Arquitetura DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Solução — Decisão Arquitetural da DataRetail

## Decisão

Adotar log durável para eventos web, processamento streaming apenas para fraude e batch incremental para camadas canônicas e receita. O batch reconcilia o caminho rápido.

```mermaid
flowchart LR
    F["Fontes operacionais"] --> B["Batch incremental"]
    W["Eventos web"] --> L["Log durável"]
    L --> S["Detecção de fraude"]
    L --> B
    B --> BR["Bronze"]
    BR --> SI["Silver"]
    SI --> GO["Gold receita"]
```

## Consequências

- menor duplicação que Lambda completa;
- necessidade de operar log e streaming;
- receita com maior latência, porém auditável;
- replay disponível pelo log e Bronze;
- contratos compartilhados reduzem divergência.

Revisar quando a latência de novos casos justificar custo operacional adicional.

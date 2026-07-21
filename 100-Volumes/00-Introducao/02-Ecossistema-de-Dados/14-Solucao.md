---
title: Solução — Mapa do Ecossistema DataRetail
description: "Referência para o laboratório de ecossistema."
tags: [ecossistema-de-dados, solucao, dataretail]
aliases: [Solução Ecossistema DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Solução — Mapa do Ecossistema DataRetail

```mermaid
flowchart LR
    ERP["ERP — Vendas"] --> PED["Produto Pedidos"]
    WEB["E-commerce — Vendas"] --> PED
    PAY["Gateway — Financeiro"] --> PED
    CRM["CRM — Clientes"] --> CLI["Produto Clientes"]
    WMS["WMS — Logística"] --> ENT["Produto Entregas"]
    PED --> REC["Receita"]
    CLI --> REC
    PED --> SLA["SLA de Entrega"]
    ENT --> SLA
```

| Produto | Owner | Consumidor | Controle principal |
|---|---|---|---|
| Pedidos | Vendas | Financeiro/Operação | Unicidade e reconciliação |
| Clientes | CRM | Marketing/Atendimento | Privacidade e atualização |
| Entregas | Logística | Operação/Cliente | Freshness e completude |

SLIs: lead time de nova fonte, freshness por produto e tempo de recuperação após falha.

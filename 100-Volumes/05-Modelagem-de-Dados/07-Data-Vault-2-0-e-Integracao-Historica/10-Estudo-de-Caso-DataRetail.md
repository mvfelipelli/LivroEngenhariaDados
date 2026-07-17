---
title: Estudo de Caso — DataRetail S.A.
description: "Integração de clientes e pedidos omnichannel em Data Vault."
tags: [modelagem-de-dados, estudo-de-caso, dataretail, data-vault]
aliases: [Caso DataRetail Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

A DataRetail integra CRM, e-commerce e lojas. Clientes possuem identificadores por fonte; pedidos podem mudar de status e receber correções.

```mermaid
flowchart LR
    HC["HUB_CLIENTE"] --> SC["SAT_CLIENTE_CRM"]
    HC --> SE["SAT_CLIENTE_ECOM"]
    HP["HUB_PEDIDO"] --> SP["SAT_PEDIDO"]
    HC --> L["LINK_PEDIDO_CLIENTE"]
    HP --> L
```

## Decisões

- `(sistema, cliente_id_origem)` é business key inicial;
- regra corporativa de identidade fica no Business Vault;
- Hubs preservam primeira fonte e carga;
- Satellites são separados por fonte e ritmo;
- Link representa relação pedido-cliente;
- status é historizado em Satellite;
- mart de vendas deriva fato e dimensão cliente conformada.

PIT diário acelera visão corrente. Todas as linhas mantêm record source e load timestamp, permitindo reconstrução e investigação.

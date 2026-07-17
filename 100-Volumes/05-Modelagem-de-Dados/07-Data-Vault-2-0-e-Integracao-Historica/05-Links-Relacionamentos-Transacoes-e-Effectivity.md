---
title: Links, Relacionamentos, Transações e Effectivity
description: "Associações historizadas entre Hubs."
tags: [data-vault, links, effectivity]
aliases: [Links Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Links, Relacionamentos, Transações e Effectivity

Link registra associação entre duas ou mais business keys. Pode representar relação estável, transação ou evento.

```text
LINK_PEDIDO_CLIENTE(link_hk, pedido_hk, cliente_hk, load_ts, record_source)
```

A granularidade do Link é o conjunto de Hubs participantes. A ordem de componentes do hash deve ser fixa e baseada em papéis, não em ordem de chegada.

Effectivity Satellite representa validade de uma relação quando a fonte informa começo e fim. Driving key identifica qual lado determina exclusividade ou mudança, como um pedido pertencer a um cliente.

> [!warning]
> Alterar participantes de um Link muda seu grão; não adicione um Hub apenas porque surgiu novo atributo contextual.

---
title: Granularidade, Cardinalidade, Opcionalidade e Tempo
description: "Precisão estrutural para fatos e relações."
tags: [grao, cardinalidade, opcionalidade, tempo]
aliases: [Grão em Modelagem]
created: 2026-07-17
updated: 2026-07-17
---

# Granularidade, Cardinalidade, Opcionalidade e Tempo

Grão declara o que uma ocorrência representa: um pedido, uma linha de pedido ou um estado diário. Misturar grãos é fonte recorrente de duplicidade e métricas erradas.

Cardinalidade define quantas ocorrências podem participar: um cliente realiza zero ou muitos pedidos; cada pedido pertence a exatamente um cliente. Opcionalidade precisa refletir o ciclo de vida, não apenas o estado final ideal.

## Tempo

- atributos de estado representam o valor atual;
- eventos representam mudanças ocorridas;
- versões preservam histórico;
- intervalos representam validade;
- snapshots registram estado em momentos definidos.

```mermaid
flowchart LR
    P["Pedido: um por compra"] --> I["Item: um por produto no pedido"]
    I --> E["Evento: um por mudança do item"]
```

> [!warning]
> Adicionar uma coluna `data` não torna o modelo temporal. É necessário definir o que o instante representa e como correções são registradas.

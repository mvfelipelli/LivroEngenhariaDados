---
title: Batch, Streaming, Lambda e Kappa
description: "Modelos temporais e estilos de processamento."
tags: [batch, streaming, lambda-architecture]
aliases: [Arquiteturas Batch e Streaming]
created: 2026-07-21
updated: 2026-07-21
---

# Batch, Streaming, Lambda e Kappa

Batch processa conjuntos delimitados e favorece reexecução e eficiência. Streaming processa dados conforme chegam e requer estado, tempo de evento, atrasos e recuperação contínua.

Lambda mantém caminhos batch e speed e reconcilia resultados; oferece correção histórica e baixa latência ao custo de duas implementações. Kappa usa o log como fonte reprocessável e um caminho streaming, reduzindo duplicação, mas exige retenção e capacidade de replay.

```mermaid
flowchart TB
    E["Eventos"] --> L["Log durável"]
    L --> ST["Streaming"]
    L --> RP["Replay"]
    ST --> V["Visão"]
    RP --> V
```

Muitas plataformas combinam incremental batch e streaming sem aderir rigidamente a um rótulo.

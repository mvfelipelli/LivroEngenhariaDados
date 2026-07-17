---
title: Introdução
description: "Preservação de mudanças e estados analíticos."
tags: [modelagem-de-dados, introducao, historico]
aliases: [Introdução ao Histórico Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Se um cliente muda de segmento, vendas passadas devem aparecer no segmento antigo ou no atual? Ambas as respostas podem ser legítimas para perguntas diferentes. O modelo deve escolher e permitir uso correto.

```mermaid
sequenceDiagram
    participant D as Dimensão
    participant F as Fato
    D->>D: versão V1 válida
    F->>D: fato referencia V1
    D->>D: fechar V1 e criar V2
    F->>D: novo fato referencia V2
```

SCD preserva mudanças de atributos; snapshots preservam estados; bridges representam muitos membros e hierarquias. Esses padrões exigem regras contra sobreposição e duplicação de medidas.

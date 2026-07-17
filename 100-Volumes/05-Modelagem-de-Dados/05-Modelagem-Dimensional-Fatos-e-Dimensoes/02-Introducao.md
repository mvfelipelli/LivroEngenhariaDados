---
title: Introdução
description: "Modelos analíticos compreensíveis e consistentes."
tags: [modelagem-de-dados, introducao, dimensional]
aliases: [Introdução à Modelagem Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Sistemas operacionais registram transações; análise cruza processos, períodos e perspectivas. O modelo dimensional apresenta medidas no centro e contexto descritivo ao redor.

```mermaid
erDiagram
    DIM_DATA ||--o{ FATO_VENDA : contextualiza
    DIM_PRODUTO ||--o{ FATO_VENDA : contextualiza
    DIM_LOJA ||--o{ FATO_VENDA : contextualiza
```

Denormalização dimensional não elimina rigor. Identidade, histórico, grão, aditividade e conformidade precisam ser mais explícitos porque muitos consumidores agregam dados diretamente.

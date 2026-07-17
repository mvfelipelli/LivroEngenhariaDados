---
title: Chaves Substitutas, Dimensões Degeneradas, Junk e Role-Playing
description: "Padrões especiais de dimensões e identidade analítica."
tags: [surrogate-key, degenerate-dimension, junk-dimension]
aliases: [Padrões Dimensionais Especiais]
created: 2026-07-17
updated: 2026-07-17
---

# Chaves Substitutas, Dimensões Degeneradas, Junk e Role-Playing

Chave substituta dimensional identifica uma versão da dimensão e desacopla fatos da chave operacional. O fato preserva a chave válida no evento.

Dimensão degenerada é identificador sem tabela dimensional própria, como número do pedido na fato. Junk dimension agrupa flags e códigos pequenos para evitar dezenas de colunas dispersas.

Role-playing reutiliza a mesma dimensão em papéis diferentes:

```text
data_pedido_sk → DIM_DATA
data_pagamento_sk → DIM_DATA
data_entrega_sk → DIM_DATA
```

Dimensão mini pode separar atributos de mudança frequente; outriggers relacionam dimensões, mas podem complicar navegação e conformidade.

> [!warning]
> Não use chave operacional como chave dimensional se histórico de versões precisa ser preservado.

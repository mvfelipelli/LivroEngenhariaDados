---
title: Esquema Estrela, Snowflake e Constelações
description: "Organização física dos modelos dimensionais."
tags: [star-schema, snowflake, constelacao]
aliases: [Esquema Estrela e Snowflake]
created: 2026-07-17
updated: 2026-07-17
---

# Esquema Estrela, Snowflake e Constelações

Estrela conecta fato diretamente a dimensões desnormalizadas, favorecendo simplicidade. Snowflake normaliza hierarquias dimensionais, reduzindo redundância ao custo de mais joins. Constelação compartilha dimensões entre várias fatos.

```mermaid
erDiagram
    DIM_DATA ||--o{ FATO_VENDA : data
    DIM_PRODUTO ||--o{ FATO_VENDA : produto
    DIM_LOJA ||--o{ FATO_VENDA : loja
    DIM_DATA ||--o{ FATO_ESTOQUE : data
    DIM_PRODUTO ||--o{ FATO_ESTOQUE : produto
    DIM_LOJA ||--o{ FATO_ESTOQUE : loja
```

Escolha snowflake quando governança, cardinalidade ou manutenção da hierarquia justificarem. Não normalize automaticamente dimensões pequenas.

> [!important]
> Fatos de grãos diferentes não devem ser juntados diretamente; agregue cada uma ao grão comum antes de combinar.

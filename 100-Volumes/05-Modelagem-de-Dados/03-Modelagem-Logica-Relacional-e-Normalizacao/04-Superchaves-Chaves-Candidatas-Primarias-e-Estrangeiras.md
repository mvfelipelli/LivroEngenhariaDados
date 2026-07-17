---
title: Superchaves, Chaves Candidatas, Primárias e Estrangeiras
description: "Identidade e referências no modelo lógico."
tags: [chaves, integridade-referencial]
aliases: [Chaves Relacionais]
created: 2026-07-17
updated: 2026-07-17
---

# Superchaves, Chaves Candidatas, Primárias e Estrangeiras

Superchave identifica tupla, mesmo com atributos excedentes. Chave candidata é superchave mínima. Uma candidata é escolhida como primária; as demais continuam sendo chaves alternativas e merecem `UNIQUE`.

```sql
CREATE TABLE produto (
    produto_id BIGINT PRIMARY KEY,
    sku TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL
);
```

Chave estrangeira representa inclusão referencial: todo valor não nulo referencia chave existente. A ação em exclusão deve refletir domínio: `CASCADE`, `RESTRICT`, `SET NULL` e ausência de ação não são escolhas de conveniência.

Chaves compostas são adequadas quando a identidade depende do contexto, como `(pedido_id, numero_item)`. Uma chave substituta pode facilitar referências, mas não remove unicidade natural.

> [!warning]
> Chave primária não é sinônimo de coluna autoincremental; é a candidata escolhida para representar identidade relacional.

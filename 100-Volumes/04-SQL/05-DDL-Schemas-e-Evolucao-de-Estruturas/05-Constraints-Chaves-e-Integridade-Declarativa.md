---
title: Constraints, Chaves e Integridade Declarativa
description: "Invariantes verificáveis para qualquer escritor."
tags: [sql, constraints, primary-key, foreign-key]
aliases: [Integridade Declarativa SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Constraints, Chaves e Integridade Declarativa

`NOT NULL`, `CHECK`, `UNIQUE`, `PRIMARY KEY` e `FOREIGN KEY` protegem propriedades diferentes. Nomear constraints melhora erros e futuras alterações.

```sql
CREATE TABLE itens_pedido (
    pedido_id BIGINT NOT NULL,
    linha INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    CONSTRAINT pk_itens PRIMARY KEY (pedido_id, linha),
    CONSTRAINT ck_quantidade_positiva CHECK (quantidade > 0),
    CONSTRAINT fk_item_pedido FOREIGN KEY (pedido_id)
        REFERENCES pedidos (pedido_id)
);
```

`CHECK` que resulta desconhecido pode ser aceito; combine com `NOT NULL` quando ausência for proibida. Regras entre várias linhas geralmente não pertencem a `CHECK` simples.

```mermaid
flowchart LR
    E["Escrita"] --> N["NOT NULL / CHECK"]
    N --> U["UNIQUE / PK"]
    U --> F["FK"]
    F --> V["Estado válido"]
```

Ações `ON DELETE` e `ON UPDATE` devem refletir ciclo de vida. `CASCADE` é útil para dependência de composição, mas perigoso quando a exclusão deveria ser impedida.

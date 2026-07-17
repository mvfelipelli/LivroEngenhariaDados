---
title: Qualidade, Integridade, Constraints e Invariantes
description: "Regras que preservam estados válidos."
tags: [qualidade, integridade, constraints]
aliases: [Invariantes de Modelo]
created: 2026-07-17
updated: 2026-07-17
---

# Qualidade, Integridade, Constraints e Invariantes

Invariante é uma condição que deve permanecer verdadeira. O modelo deve indicar onde ela é aplicada: banco, serviço, pipeline ou processo humano.

```sql
CREATE TABLE item_pedido (
    pedido_id INTEGER NOT NULL REFERENCES pedido(pedido_id),
    numero_item INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    preco_centavos INTEGER NOT NULL CHECK (preco_centavos >= 0),
    PRIMARY KEY (pedido_id, numero_item)
);
```

Chaves, `NOT NULL`, `CHECK`, unicidade e referências tornam o contrato executável. Regras agregadas, temporais ou entre sistemas exigem controles complementares.

Qualidade deve ser definida em relação ao uso: completude, validade, consistência, unicidade, integridade e atualidade possuem impactos diferentes por produto.

> [!important]
> Uma regra documentada mas não verificada tende a se tornar apenas uma expectativa.

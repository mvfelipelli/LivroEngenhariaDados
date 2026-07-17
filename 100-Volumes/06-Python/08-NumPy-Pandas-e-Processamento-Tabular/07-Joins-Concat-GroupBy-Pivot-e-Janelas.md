---
title: Joins, Concat, GroupBy, Pivot e Janelas
description: "Composição tabular e controle de cardinalidade."
tags: [python, pandas, joins, groupby]
aliases: [Joins Pandas]
created: 2026-07-17
updated: 2026-07-17
---

# Joins, Concat, GroupBy, Pivot e Janelas

`merge` combina chaves e pode multiplicar linhas. Declare `validate="many_to_one"`, `one_to_one` ou outra cardinalidade esperada e use `indicator=True` para reconciliação.

```python
enriquecido = itens.merge(
    produtos,
    on="produto_id",
    how="left",
    validate="many_to_one",
    indicator=True,
)
```

Valores nulos nas chaves podem casar de forma diferente do SQL; filtre ou normalize conforme o contrato. `concat` empilha e alinha colunas; confirme schema antes.

`groupby(..., dropna=False, observed=True)` torna decisões sobre nulos e categorias explícitas. `agg` reduz, `transform` retorna ao tamanho original. Pivot exige combinações únicas; `pivot_table` agrega duplicatas. Rolling, expanding e shift dependem de ordenação correta dentro do grupo.

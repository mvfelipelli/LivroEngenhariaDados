---
title: Solução — Mart Tabular Reconciliado
description: "Implementação de referência do laboratório."
tags: [python, solucao, numpy, pandas]
aliases: [Solução Pandas]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Mart Tabular Reconciliado

```python
from __future__ import annotations

import numpy as np
import pandas as pd

def construir_mart(pedidos: pd.DataFrame, itens: pd.DataFrame) -> pd.DataFrame:
    atuais = (
        pedidos.sort_values(["pedido_id", "versao"], kind="stable")
        .drop_duplicates("pedido_id", keep="last")
    )
    aprovados = atuais.loc[atuais["status"].eq("aprovado"), ["pedido_id", "loja"]]
    base = itens.merge(
        aprovados,
        on="pedido_id",
        how="inner",
        validate="many_to_one",
        indicator=True,
    )
    if not base["_merge"].eq("both").all():
        raise ValueError("join incompleto")
    mart = (
        base.groupby("loja", as_index=False, observed=True)
        .agg(itens=("item_id", "nunique"), total_centavos=("valor_centavos", "sum"))
        .sort_values("loja", kind="stable")
        .reset_index(drop=True)
    )
    if int(mart["itens"].sum()) != len(base):
        raise ValueError("contagem não reconciliada")
    if int(mart["total_centavos"].sum()) != int(base["valor_centavos"].sum()):
        raise ValueError("total não reconciliado")
    return mart

if __name__ == "__main__":
    pedidos = pd.DataFrame(
        [
            ("P1", 1, "SP", "recebido"),
            ("P1", 2, "SP", "aprovado"),
            ("P2", 1, "RJ", "aprovado"),
            ("P3", 1, "SP", "aprovado"),
            ("P4", 1, "RJ", "cancelado"),
        ],
        columns=["pedido_id", "versao", "loja", "status"],
    ).astype({"pedido_id": "string", "versao": "Int64", "loja": "category", "status": "category"})
    itens = pd.DataFrame(
        [("I1", "P1", 1200), ("I2", "P2", 800), ("I3", "P3", 2500), ("I4", "P4", 900)],
        columns=["item_id", "pedido_id", "valor_centavos"],
    ).astype({"item_id": "string", "pedido_id": "string", "valor_centavos": "Int64"})

    mart = construir_mart(pedidos, itens)
    segunda = construir_mart(pedidos.sample(frac=1, random_state=7), itens)
    pd.testing.assert_frame_equal(mart, segunda)
    valores = mart["total_centavos"].to_numpy(dtype=np.int64)
    assert np.add.reduce(valores) == 4500
    assert mart.to_dict("records") == [
        {"loja": "RJ", "itens": 1, "total_centavos": 800},
        {"loja": "SP", "itens": 2, "total_centavos": 3700},
    ]
    print("lojas=2 itens=3 total_centavos=4500 join=many_to_one reconciliacao=ok determinismo=ok")
```

A segunda execução embaralha pedidos para demonstrar que versão, não ordem de entrada, governa a deduplicação.

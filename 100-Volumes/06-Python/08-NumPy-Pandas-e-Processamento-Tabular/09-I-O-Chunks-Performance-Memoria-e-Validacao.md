---
title: I/O, Chunks, Performance, Memória e Validação
description: "Execução tabular controlada e verificável."
tags: [python, pandas, performance, memoria]
aliases: [Performance Pandas]
created: 2026-07-17
updated: 2026-07-17
---

# I/O, Chunks, Performance, Memória e Validação

Declare `usecols`, `dtype`, `parse_dates` e encoding ao ler. Inferência pode variar entre chunks e arquivos.

```python
for chunk in pd.read_csv(
    "pedidos.csv",
    usecols=["loja", "valor_centavos"],
    dtype={"loja": "string", "valor_centavos": "Int64"},
    chunksize=100_000,
):
    consumir(chunk.groupby("loja")["valor_centavos"].sum())
```

Agregações por chunk precisam de redução associativa e combinação final; medianas e distinct counts exigem estratégia própria. Alguns joins não cabem em streaming simples.

Meça com `memory_usage(deep=True)`, tempo e volume. Evite `iterrows`; use operações vetorizadas ou `itertuples` quando loop for necessário. Valide schema, unicidade, domínios, nulos, cardinalidade de joins, grão e reconciliação monetária em cada gate.

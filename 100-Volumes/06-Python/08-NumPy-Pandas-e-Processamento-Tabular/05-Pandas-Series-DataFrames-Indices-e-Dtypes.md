---
title: Pandas — Series, DataFrames, Índices e Dtypes
description: "Estruturas rotuladas e tipos tabulares."
tags: [python, pandas, dataframe, dtypes]
aliases: [DataFrames Pandas]
created: 2026-07-17
updated: 2026-07-17
---

# Pandas: Series, DataFrames, Índices e Dtypes

Series é vetor rotulado; DataFrame é coleção de colunas alinhadas por índice. Operações entre Series alinham rótulos, não posição.

```python
import pandas as pd

pedidos = pd.DataFrame(
    {"pedido_id": ["P1", "P2"], "valor_centavos": [1200, 800]},
).astype({"pedido_id": "string", "valor_centavos": "Int64"})
```

Índice deve ter propósito: alinhamento e lookup. Para uma coluna comum de chave, mantê-la explícita pode evitar ambiguidades. Índice não garante unicidade sem verificação.

Dtypes nullable como `Int64`, `boolean` e `string` representam ausência sem promover inteiro para float. Categoricals comprimem baixa cardinalidade e definem ordem de categorias, mas categorias divergentes exigem harmonização.

---
title: NumPy — Arrays, Dtypes, Shapes e Memória
description: "Modelo n-dimensional e representação compacta."
tags: [python, numpy, arrays, dtypes]
aliases: [Arrays NumPy]
created: 2026-07-17
updated: 2026-07-17
---

# NumPy: Arrays, Dtypes, Shapes e Memória

`ndarray` combina buffer, dtype, shape, strides e ordem. Um dtype fixo permite operações contíguas e evita o overhead de objetos Python.

```python
import numpy as np

valores = np.array([[1200, 800], [2500, 0]], dtype=np.int64)
assert valores.shape == (2, 2)
assert valores.ndim == 2
assert valores.nbytes == 32
```

Inteiros possuem largura fixa e podem overflow; escolha dtype conforme domínio. Float segue IEEE 754 e inclui NaN e infinidades. `object` armazena referências Python e perde várias vantagens de memória e vetorização.

`reshape` muda a visão lógica quando possível; `ravel` tende a produzir view, enquanto `flatten` copia. Strides descrevem quantos bytes avançar em cada eixo.

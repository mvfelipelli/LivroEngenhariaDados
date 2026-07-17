---
title: Indexação, Views, Cópias, Broadcasting e Vetorização
description: "Transformações eficientes e efeitos de memória."
tags: [python, numpy, broadcasting, vetorizacao]
aliases: [Vetorização NumPy]
created: 2026-07-17
updated: 2026-07-17
---

# Indexação, Views, Cópias, Broadcasting e Vetorização

Slices básicos normalmente retornam views; indexação avançada com arrays ou máscaras retorna cópias.

```python
import numpy as np

base = np.array([1, 2, 3, 4])
view = base[1:3]
view[0] = 20
assert base.tolist() == [1, 20, 3, 4]
```

Broadcasting combina shapes compatíveis comparando eixos da direita: dimensões iguais ou uma delas igual a 1.

```python
matriz = np.array([[1, 2], [3, 4]])
resultado = matriz * np.array([10, 100])
```

Vetorização reduz loops Python, mas arrays temporários podem elevar memória. Operações in-place economizam alocação se ownership for exclusivo. Meça tempo, pico de memória e clareza; `np.vectorize` é conveniência, não vetorização nativa.

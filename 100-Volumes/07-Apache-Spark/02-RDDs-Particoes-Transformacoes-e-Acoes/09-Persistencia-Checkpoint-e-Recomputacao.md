---
title: Persistência, Checkpoint e Recomputation
description: "Reuso de resultados e corte de linhagem."
tags: [apache-spark, cache, checkpoint]
aliases: [Persistência de RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Persistência, Checkpoint e Recomputation

`cache()` usa o nível padrão; `persist()` permite escolher memória, disco e serialização. A persistência é lazy e só ocupa recursos após uma ação.

```python
from pyspark import StorageLevel

validos = entrada.filter(validar).persist(StorageLevel.MEMORY_AND_DISK)
try:
    total = validos.count()
    amostra = validos.take(10)
finally:
    validos.unpersist()
```

Persistir vale quando o custo de recomputar supera armazenamento e pressão sobre o cluster. Checkpoint materializa em sistema confiável e remove dependências anteriores; é útil para linhagens longas e algoritmos iterativos. `localCheckpoint` é mais rápido, porém não oferece a mesma resiliência.

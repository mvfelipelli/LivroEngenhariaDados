---
title: Estratégias de Join e Broadcast
description: "Escolha física, estatísticas e movimento de dados."
tags: [apache-spark, broadcast-join, shuffle]
aliases: [Estratégias de Join Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Estratégias de Join e Broadcast

Broadcast hash join replica a relação pequena e evita shuffle do lado grande. Sort-merge join redistribui e ordena ambos por chave; é robusto para relações grandes. Shuffle hash join constrói tabelas hash por partição quando as condições favorecem.

```python
from pyspark.sql.functions import broadcast

enriquecidos = fatos.join(broadcast(dim_lojas), "loja_id", "left")
```

O hint é orientação, não licença para ignorar tamanho. Broadcast excessivo pressiona memória de todos os executors. Estatísticas desatualizadas levam a decisões ruins; confira `explain()` e métricas reais. Adaptive Query Execution pode alterar estratégias durante o job.

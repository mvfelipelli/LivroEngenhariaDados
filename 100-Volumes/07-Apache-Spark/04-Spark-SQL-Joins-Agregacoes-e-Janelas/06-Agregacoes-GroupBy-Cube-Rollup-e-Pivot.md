---
title: Agregações, GroupBy, Cube, Rollup e Pivot
description: "Resumos distribuídos e múltiplos níveis de granularidade."
tags: [apache-spark, agregacoes, rollup]
aliases: [Agregações Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Agregações, GroupBy, Cube, Rollup e Pivot

`groupBy` define uma granularidade. `rollup` produz hierarquia de subtotais; `cube` produz combinações; `pivot` transforma valores em colunas e pode ampliar schema e memória.

```python
resumo = pedidos.groupBy("data", "loja_id").agg(
    F.countDistinct("pedido_id").alias("pedidos"),
    F.sum("valor_centavos").alias("receita_centavos"),
)
```

Agregações ocorrem parcialmente antes do shuffle quando possível. `countDistinct` e percentis exatos podem ser caros; versões aproximadas servem quando o contrato aceita erro delimitado. No pivot, forneça explicitamente valores conhecidos para evitar uma ação de descoberta.

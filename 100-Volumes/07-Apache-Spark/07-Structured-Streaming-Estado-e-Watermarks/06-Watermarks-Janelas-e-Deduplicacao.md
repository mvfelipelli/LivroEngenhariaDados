---
title: Watermarks, Janelas e Deduplicação
description: "Limites de estado e política para eventos tardios."
tags: [apache-spark, watermark, deduplicacao]
aliases: [Watermark Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Watermarks, Janelas e Deduplicação

`withWatermark("event_time", "15 minutes")` declara tolerância de atraso para operações stateful compatíveis. O mecanismo deriva watermark do maior event time observado menos o atraso e pode remover estado antigo.

```python
por_janela = (eventos.withWatermark("event_time", "15 minutes")
    .groupBy(F.window("event_time", "5 minutes"), "loja_id")
    .agg(F.sum("valor_centavos").alias("receita")))
```

Eventos anteriores à fronteira podem ser descartados da atualização stateful; defina reconciliação tardia ou backfill. Deduplicação por ID também precisa de watermark para limitar quanto tempo o ID permanece no estado. Quanto maior a tolerância, maior a correção tardia e o custo de estado.

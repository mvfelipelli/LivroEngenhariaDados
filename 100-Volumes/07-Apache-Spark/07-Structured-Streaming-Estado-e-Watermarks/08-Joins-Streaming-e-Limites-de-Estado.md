---
title: Joins Streaming e Limites de Estado
description: "Junções stream-static e stream-stream."
tags: [apache-spark, streaming-join, estado]
aliases: [Joins Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Joins Streaming e Limites de Estado

Stream-static usa uma relação estática para enriquecer cada lote e normalmente não precisa guardar ambos os lados. A atualização da dimensão depende de como ela é carregada e reiniciada.

Stream-stream precisa manter linhas de ambos os fluxos até saber que novas correspondências não chegarão. Watermarks e condição temporal limitam essa espera.

```python
condicao = [
    pedidos.cliente_id == pagamentos.cliente_id,
    pagamentos.event_time >= pedidos.event_time,
    pagamentos.event_time <= pedidos.event_time + F.expr("INTERVAL 30 MINUTES"),
]
correlacionados = pedidos.join(pagamentos, condicao, "inner")
```

Sem intervalo temporal, o estado pode crescer indefinidamente. Outer joins possuem requisitos adicionais para decidir quando emitir ausência de correspondência.

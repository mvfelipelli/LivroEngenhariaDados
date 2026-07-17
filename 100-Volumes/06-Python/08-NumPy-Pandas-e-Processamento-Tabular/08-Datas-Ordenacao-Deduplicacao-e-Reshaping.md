---
title: Datas, Ordenação, Deduplicação e Reshaping
description: "Tempo tabular, precedência e mudança de forma."
tags: [python, pandas, datas, deduplicacao]
aliases: [Datas Pandas]
created: 2026-07-17
updated: 2026-07-17
---

# Datas, Ordenação, Deduplicação e Reshaping

Normalize instantes com timezone para UTC. `.dt` expõe componentes, floor, period e conversões, mas calendário local exige timezone de negócio antes de extrair data.

Deduplicação é política de precedência, não simples remoção:

```python
atuais = (
    eventos.sort_values(["pedido_id", "versao", "ingestao_utc"])
    .drop_duplicates("pedido_id", keep="last")
)
```

Se versão e ingestão empatarem, inclua desempate determinístico ou rejeite ambiguidade. Ordenação é estável quando solicitado com algoritmo apropriado e deve preceder janelas e `merge_asof`.

`melt` transforma wide em long; pivot faz o inverso. Toda mudança de forma deve declarar identificadores, variáveis, medidas e grão resultante. Reconcile contagem e somas aditivas antes e depois.

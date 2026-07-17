---
title: Snapshots Periódicos e Acumulativos
description: "Representação de estados e marcos ao longo do tempo."
tags: [snapshot-periodico, snapshot-acumulativo]
aliases: [Snapshots Dimensionais]
created: 2026-07-17
updated: 2026-07-17
---

# Snapshots Periódicos e Acumulativos

Snapshot periódico registra estado em intervalos fixos, como saldo diário por conta. Seu grão inclui período e entidade. Ausência pode significar zero, não observado ou falha; defina a regra.

Snapshot acumulativo registra marcos de processo em uma linha, atualizada conforme avanço:

```text
pedido_id, criado_data_sk, pago_data_sk, enviado_data_sk,
entregue_data_sk, dias_ate_entrega
```

Ele favorece análise de duração de processos com início e fim previsíveis. Eventos continuam úteis quando etapas repetem, retrocedem ou não têm sequência fixa.

Saldo é semiaditivo no tempo; agregue por entidade no mesmo instante ou use média/mínimo/máximo conforme pergunta.

> [!note]
> Snapshot não é backup: é fato analítico com grão, medidas e política de preenchimento.

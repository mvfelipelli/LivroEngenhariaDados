---
title: Gabarito — Structured Streaming
description: "Respostas dos exercícios de streaming."
tags: [apache-spark, structured-streaming, gabarito]
aliases: [Gabarito Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. Imediato após conclusão; cadência mínima; backlog finito e encerramento.
2. Append quando janelas finalizadas puderem ser emitidas; update se atualizações intermediárias forem aceitas.
3. Ocorrência no domínio, entrada na plataforma e execução pelo Spark.
4. Atraso aceito deve equilibrar correção tardia, estado, custo e reconciliação.
5. `withWatermark` em event time e deduplicação por identificador compatível.
6. Watermarks nos fluxos e condição de igualdade mais intervalo temporal.
7. Reprocessamento do batch deve encontrar commit existente ou executar upsert idempotente.
8. Offsets no checkpoint, transformação determinística e commit transacional identificado por query/batch.

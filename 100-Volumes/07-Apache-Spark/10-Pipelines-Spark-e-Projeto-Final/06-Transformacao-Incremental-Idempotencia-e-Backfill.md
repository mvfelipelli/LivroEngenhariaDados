---
title: Transformação Incremental, Idempotência e Backfill
description: "Processamento por unidade lógica e reconstrução histórica."
tags: [apache-spark, incremental, idempotencia]
aliases: [Incrementalidade Projeto Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Transformação Incremental, Idempotência e Backfill

Batch processa `data_negocio` e versão de origem; streaming processa offsets sob checkpoint. A chave canônica combina `pedido_id` e versão, com desempate determinístico por instante de ingestão.

Publicação usa staging por `run_id`, reconciliação e commit de tabela. Repetir a mesma unidade substitui ou faz merge dos mesmos registros, sem acrescentar duplicatas.

Backfill recebe intervalo, versão de código e prioridade separada. Ele não compete irrestritamente com SLA corrente. Após cálculo, compara-se com a versão publicada e promove-se apenas o conjunto aprovado.

Correção tardia e deleção possuem eventos ou tabelas de controle, evitando mutações invisíveis.

---
title: Transações, Checkpoints, Reprocessamento e Backfill
description: "Consistência entre resultado e progresso."
tags: [python, transacoes, checkpoint, backfill]
aliases: [Checkpoint de Pipelines Python]
created: 2026-07-20
updated: 2026-07-20
---

# Transações, Checkpoints, Reprocessamento e Backfill

Dados e checkpoint devem confirmar na mesma transação sempre que compartilham um sistema. Assim, uma falha produz ambos ou nenhum.

Quando fonte e sink não compartilham transação distribuída, use protocolo recuperável: gravação idempotente, marcador de lote, confirmação e reconciliação. Exactly-once de ponta a ponta é propriedade do sistema, não de uma chamada isolada.

Reprocessamento repete uma unidade conhecida. Backfill cobre intervalo histórico e precisa de namespace, limites de capacidade e política de publicação. Não mova o watermark corrente com um backfill independente.

Registre motivo, intervalo, versão do código, executor e resultado. Faça dry-run quando possível e reconcilie antes de promover a saída.

Compensação corrige efeito confirmado quando rollback não é possível; ela é uma nova operação auditável, não apagamento de histórico.

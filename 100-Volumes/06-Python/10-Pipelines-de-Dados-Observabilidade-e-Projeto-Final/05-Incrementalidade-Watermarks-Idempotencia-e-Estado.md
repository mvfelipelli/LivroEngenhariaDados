---
title: Incrementalidade, Watermarks, Idempotência e Estado
description: "Progresso retomável e reexecução segura."
tags: [python, incrementalidade, watermark, idempotencia]
aliases: [Estado de Pipelines Python]
created: 2026-07-20
updated: 2026-07-20
---

# Incrementalidade, Watermarks, Idempotência e Estado

Incrementalidade seleciona somente dados novos ou alterados. Watermark precisa de ordenação total, normalmente `(updated_at, id)`, para não perder empates.

Overlap relê uma janela anterior e depende de sink idempotente para capturar atrasos. CDC fornece sequência própria, mas retenção e reset precisam de política.

Idempotência significa que repetir uma unidade produz o mesmo estado observável. Estratégias incluem chave natural com versão, partição overwrite, merge e ledger de eventos.

Estado deve ser pequeno, versionado e auditável: cursor, watermark, run_id e versão do contrato. Não derive avanço apenas da leitura; ele representa dados efetivamente confirmados.

Uma mudança de regra pode exigir reset ou migração do checkpoint, nunca edição manual sem registro.

---
title: Checkpoint, Falhas, Garantias e foreachBatch
description: "Recuperação e efeitos externos em pipelines streaming."
tags: [apache-spark, checkpoint, foreachbatch]
aliases: [Checkpoint Structured Streaming]
created: 2026-07-20
updated: 2026-07-20
---

# Checkpoint, Falhas, Garantias e foreachBatch

Checkpoint armazena offsets, commits e estado. Deve ficar em armazenamento confiável, exclusivo por query e estável entre reinícios compatíveis. Apagá-lo reinicia o progresso e pode duplicar ou perder efeitos conforme a fonte.

Exactly-once interno não garante exatamente uma vez no sistema externo. `foreachBatch` recebe `batch_id`; use-o como chave de idempotência e faça transação ou upsert no destino.

```python
def publicar(df, batch_id):
    gravar_idempotente(df, chave_execucao=str(batch_id))

query = resultado.writeStream.foreachBatch(publicar).option(
    "checkpointLocation", checkpoint
).start()
```

Teste kill/restart, replay, indisponibilidade do sink e mudança de versão. Garantias são propriedades fim a fim.

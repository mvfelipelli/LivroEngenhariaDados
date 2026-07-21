---
title: Escrita, Modos, Commit e Idempotência
description: "Publicação segura e semântica dos modos de escrita."
tags: [apache-spark, escrita, idempotencia]
aliases: [Escrita Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Escrita, Modos, Commit e Idempotência

`append`, `overwrite`, `errorIfExists` e `ignore` controlam comportamento, mas não garantem transação. Tasks escrevem arquivos temporários e o commit protocol publica resultados; sem atomicidade do armazenamento, falhas podem deixar artefatos.

Idempotência exige que repetir a mesma unidade lógica produza o mesmo estado. Estratégias incluem sobrescrever partição determinística, publicar em caminho versionado e trocar ponteiro, ou usar formato de tabela transacional.

```python
(resultado.write.mode("overwrite")
    .partitionBy("data_negocio")
    .parquet(destino))
```

Nunca sobrescreva escopo maior que o lote. Valide contagem, soma, schema e manifesto antes de disponibilizar a saída.

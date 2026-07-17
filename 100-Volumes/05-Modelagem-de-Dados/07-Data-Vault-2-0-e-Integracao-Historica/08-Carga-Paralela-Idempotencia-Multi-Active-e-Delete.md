---
title: Carga Paralela, Idempotência, Multi-Active e Delete
description: "Padrões operacionais de ingestão no Vault."
tags: [data-vault, carga, idempotencia, multi-active]
aliases: [Carga Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Carga Paralela, Idempotência, Multi-Active e Delete

Hash keys permitem carregar Hubs independentes e Links sem lookup sequencial de chaves. A ordem lógica continua: staging confiável, Hubs, Links e Satellites.

Carga idempotente insere Hub/Link somente se hash key não existe e Satellite somente se combinação de parent, mudança e instante ainda não foi registrada. Deduplicação do lote precede a comparação.

Multi-active Satellite representa vários valores simultaneamente válidos, como telefones. Inclui chave de discriminação no grão. Record Tracking Satellite registra presença por lote; status/effectivity modelam exclusões lógicas.

Deletes físicos da fonte não devem apagar o Raw Vault. Registre ausência ou evento de exclusão conforme capacidade de captura.

> [!tip]
> Reexecute o mesmo lote em testes e compare contagem de cada objeto para provar idempotência.

---
title: SCD Tipo 2, Chaves, Intervalos e Lookup Temporal
description: "Implementação segura de versões dimensionais."
tags: [scd2, intervalos, lookup-temporal]
aliases: [SCD Tipo 2]
created: 2026-07-17
updated: 2026-07-17
---

# SCD Tipo 2, Chaves, Intervalos e Lookup Temporal

Cada versão recebe chave substituta distinta, enquanto a chave natural conecta versões do mesmo membro.

```text
cliente_sk, cliente_id, segmento, valido_desde, valido_ate, atual
```

Ao mudar: localizar versão atual, comparar atributos rastreados, fechar `valido_ate` e inserir nova linha. As duas operações devem ser atômicas e idempotentes.

Lookup do fato:

```sql
ON d.cliente_id = f.cliente_id
AND d.valido_desde <= f.ocorrido_em
AND (d.valido_ate > f.ocorrido_em OR d.valido_ate IS NULL)
```

Invariantes: um membro atual por chave natural, intervalos válidos, nenhuma sobreposição e um match por fato. Hash de atributos pode acelerar detecção, mas precisa de serialização canônica.

> [!warning]
> Atualizar chave dimensional de fatos antigos para a versão atual destrói a análise “como era”.

---
title: Consulta, Expansão e Agregação de JSON e Arrays
description: "Extração tipada e controle de cardinalidade em estruturas aninhadas."
tags: [sql, json, arrays, unnest]
aliases: [Consulta de JSON e Arrays]
created: 2026-07-17
updated: 2026-07-17
---

# Consulta, Expansão e Agregação de JSON e Arrays

Extrair um escalar preservando tipo é diferente de obter sua representação textual. Compare números como números, não por ordem lexicográfica.

```sql
SELECT evento_id,
       json_extract(payload, '$.canal') AS canal
FROM eventos
WHERE json_extract(payload, '$.schema_version') = 2;
```

Funções tabulares expandem arrays. Cada elemento multiplica a linha pai:

```sql
SELECT e.evento_id,
       json_extract(i.value, '$.sku') AS sku,
       json_extract(i.value, '$.quantidade') AS quantidade
FROM eventos AS e
JOIN json_each(e.payload, '$.itens') AS i;
```

Expandir simultaneamente `itens` e `cupons` produz produto cartesiano dentro do evento. Agregue cada coleção antes de combiná-las ou mantenha grãos separados.

## Reconstrução

Agregadores JSON podem formar arrays e objetos, mas ordem e duplicidade de chaves precisam de regra explícita. Ordene antes de agregar quando o array tiver semântica ordenada.

> [!tip]
> Registre o grão após cada expansão: “uma linha por evento” torna-se “uma linha por item do evento”.

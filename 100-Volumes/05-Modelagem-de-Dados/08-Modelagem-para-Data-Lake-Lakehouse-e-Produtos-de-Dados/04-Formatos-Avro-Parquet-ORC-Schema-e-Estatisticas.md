---
title: Formatos Avro, Parquet, ORC, Schema e Estatísticas
description: "Representação física para transporte e analytics."
tags: [avro, parquet, orc, formatos]
aliases: [Formatos Analíticos]
created: 2026-07-17
updated: 2026-07-17
---

# Formatos Avro, Parquet, ORC, Schema e Estatísticas

Avro é orientado a registros e comum em transporte/streaming. Parquet e ORC são colunares, adequados a scans analíticos com compressão e projeção.

| Propriedade | Avro | Parquet/ORC |
|---|---|---|
| layout | linhas | colunas |
| uso típico | eventos e intercâmbio | analytics e storage |
| projeção de poucas colunas | limitada | eficiente |
| estatísticas por blocos | menor foco | fundamentais |

Schema embutido preserva tipos, mas significado, grão e chaves ficam no contrato. Row groups/stripes, min/max, dicionários e ordenação influenciam pruning e compressão.

JSON e CSV são úteis na borda, porém têm tipos frágeis, maior volume e ambiguidades de encoding, delimitador e `NULL`.

> [!tip]
> Escolha formato pelo padrão de acesso e ecossistema, não apenas pela taxa de compressão.

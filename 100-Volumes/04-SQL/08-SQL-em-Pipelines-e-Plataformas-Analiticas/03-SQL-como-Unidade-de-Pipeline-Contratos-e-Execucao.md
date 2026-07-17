---
title: SQL como Unidade de Pipeline, Contratos e Execução
description: "Transformações SQL versionadas com entradas, saídas e efeitos explícitos."
tags: [sql, pipelines, contratos]
aliases: [Unidade SQL de Pipeline]
created: 2026-07-17
updated: 2026-07-17
---

# SQL como Unidade de Pipeline, Contratos e Execução

Cada transformação deve declarar entradas, saída, grão, chave, modo de escrita, janela processada e invariantes. Um arquivo SQL sem contexto operacional não é uma unidade implantável.

## Contrato mínimo

| Campo | Exemplo |
|---|---|
| entrada | `raw.pedidos` |
| saída | `analytics.fato_pedidos` |
| grão | um pedido |
| chave | `pedido_id` |
| estratégia | merge incremental |
| janela | watermark menos 24 horas |
| qualidade | chave única, valor não negativo |
| owner | equipe de Pedidos |

Use nomes qualificados e liste colunas. Sessão, timezone, locale e parâmetros precisam ser controlados para que a mesma entrada produza o mesmo resultado.

```sql
INSERT INTO analytics.fato_pedidos (pedido_id, data_id, cliente_id, valor_centavos)
SELECT pedido_id,
       CAST(criado_em AS DATE),
       cliente_id,
       valor_centavos
FROM staging.pedidos_validos;
```

Uma transformação deve falhar de modo explícito diante de schema incompatível. Preencher silenciosamente uma coluna crítica com `NULL` preserva execução, mas viola significado.

> [!tip]
> Versione SQL, parâmetros e contrato juntos; registre a versão que produziu cada execução.

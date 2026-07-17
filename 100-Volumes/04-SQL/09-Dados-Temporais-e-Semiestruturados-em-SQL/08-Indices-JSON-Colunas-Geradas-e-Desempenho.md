---
title: Índices JSON, Colunas Geradas e Desempenho
description: "Caminhos de acesso para atributos semiestruturados."
tags: [sql, json, indices, desempenho]
aliases: [Indexação de JSON]
created: 2026-07-17
updated: 2026-07-17
---

# Índices JSON, Colunas Geradas e Desempenho

Indexação deve seguir consultas reais. Alguns SGBDs oferecem índices invertidos sobre documentos; outros favorecem índices de expressão ou colunas geradas.

```sql
-- PostgreSQL: contenção em JSONB
CREATE INDEX idx_eventos_payload_gin
ON eventos USING gin (payload);

-- SQLite: caminho frequente materializado virtualmente
ALTER TABLE eventos ADD COLUMN canal TEXT
GENERATED ALWAYS AS (json_extract(payload, '$.canal')) VIRTUAL;
CREATE INDEX idx_eventos_canal ON eventos (canal);
```

O predicado precisa corresponder à expressão indexada e ao tipo. `"10"` e `10` não são equivalentes. Índices amplos sobre documentos consomem armazenamento e manutenção; índices de caminho são menores, porém menos flexíveis.

Arrays extensos podem aumentar muitas entradas por documento. Para elementos que participam de joins, constraints ou análises frequentes, normalizar em tabela filha pode ser superior.

> [!note]
> Compare plano, cardinalidade, bytes e custo de escrita como em [[08-EXPLAIN-ANALYZE-Leitura-de-Planos-e-Diagnostico|EXPLAIN ANALYZE]].

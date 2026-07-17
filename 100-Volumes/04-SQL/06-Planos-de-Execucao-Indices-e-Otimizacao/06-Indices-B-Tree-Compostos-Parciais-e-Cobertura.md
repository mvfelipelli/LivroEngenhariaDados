---
title: Índices B-tree, Compostos, Parciais e de Cobertura
description: "Projeto de índices orientado a padrões reais de acesso."
tags: [sql, indices, btree, cobertura]
aliases: [Projeto de Índices SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Índices B-tree, Compostos, Parciais e de Cobertura

Um índice mantém uma estrutura auxiliar ordenada ou especializada para localizar dados. B-tree atende igualdade, intervalos e ordenação; outros tipos servem a documentos, geometrias, vetores ou padrões específicos do SGBD.

## Índices compostos

A ordem das colunas representa o padrão de busca. Para igualdade em `cliente_id` e intervalo ou ordem em `criado_em`:

```sql
CREATE INDEX idx_pedidos_cliente_data
    ON pedidos (cliente_id, criado_em DESC);
```

Esse índice favorece consultas iniciadas por `cliente_id`. Ele não equivale a `(criado_em, cliente_id)`. Colunas de igualdade normalmente antecedem a coluna de intervalo/ordenação do caminho crítico.

## Parcial e cobertura

```sql
-- PostgreSQL: indexar apenas trabalho pendente
CREATE INDEX idx_eventos_pendentes
    ON eventos (criado_em)
    WHERE processado_em IS NULL;

-- Colunas incluídas podem evitar acesso à tabela
CREATE INDEX idx_pedidos_cliente_data_cover
    ON pedidos (cliente_id, criado_em DESC)
    INCLUDE (valor, status);
```

Um índice de cobertura contém tudo que a consulta precisa, embora visibilidade transacional ainda possa exigir acesso adicional conforme o SGBD. Índices parciais economizam espaço quando o predicado da consulta implica o predicado do índice.

## Custo total

Cada índice consome armazenamento, cache e manutenção em `INSERT`, `UPDATE` e `DELETE`. Índices redundantes ampliam write amplification e duração de operações administrativas.

> [!warning]
> Não crie um índice por consulta. Consolide padrões compatíveis, meça a seletividade e revise índices sem uso antes de removê-los com segurança.

---
title: Cargas Incrementais e CDC
aliases: [Incremental Loads, Change Data Capture]
tags: [engenharia-de-dados, fundamentos, etl, incremental, cdc]
type: chapter
order: 07
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Watermarks, CDC, exclusões, atrasos e ordenação de mudanças."
---

# 07 — Cargas Incrementais e CDC

## Incrementalidade

Processar apenas mudanças reduz custo, mas introduz estado. O pipeline precisa saber até onde confirmou e como tratar eventos atrasados.

## Watermark seguro

Use cursor composto, avance somente após publicação e sobreponha uma janela quando atualizações puderem chegar atrasadas. Deduplicação torna a sobreposição segura.

```mermaid
sequenceDiagram
    participant S as Fonte
    participant P as Pipeline
    participant D as Destino
    P->>S: Ler após cursor confirmado
    S-->>P: Mudanças ordenadas
    P->>D: Upsert idempotente
    D-->>P: Commit
    P->>P: Avançar cursor
```

## CDC

CDC por log captura inserts, updates e deletes com posição ordenável. Requer snapshot inicial, continuidade entre snapshot e log, retenção do log e tratamento de alterações de schema.

## Exclusões

Watermark em linhas atuais não detecta delete físico. Alternativas: tombstones, coluna de exclusão, tabela de auditoria, CDC ou reconciliação periódica.

## Eventos fora de ordem

Compare versão ou instante da origem; não use apenas horário de chegada. Defina política para empates e correções retroativas.

## Próximo Capítulo

➡️ [[08-Confiabilidade-Idempotencia-e-Reprocessamento|08 — Confiabilidade, Idempotência e Reprocessamento]]

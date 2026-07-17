---
title: Estudo de Caso — Sincronização de Catálogo da DataRetail
description: "API paginada, validação e upsert transacional."
tags: [python, estudo-de-caso, dataretail]
aliases: [Caso DataRetail APIs]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

A DataRetail sincroniza catálogo de marketplace por cursor. A versão anterior salvava o cursor antes dos produtos e perdia uma página quando o processo falhava.

O protocolo corrigido:

- GET com timeout e token em header;
- validação de status, JSON e contrato;
- upsert por `produto_id` e maior versão;
- produtos e próximo cursor na mesma transação;
- retry somente para falhas transitórias;
- detecção de cursor repetido;
- métricas de páginas, itens, rejeições e atraso.

```mermaid
sequenceDiagram
    participant C as Cliente
    participant A as API
    participant B as Banco
    C->>A: GET página(cursor)
    A-->>C: itens + próximo cursor
    C->>B: BEGIN + upserts + checkpoint
    B-->>C: COMMIT
```

Reexecuções atualizam as mesmas chaves e não duplicam produtos. O watermark só avança depois do commit.

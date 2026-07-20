---
title: Estudo de Caso — Pipeline Python da DataRetail
description: "Decisões do projeto integrador e resposta a falhas."
tags: [python, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Projeto Final Python]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — DataRetail S.A.

A DataRetail recebe um CSV append-only. Cada linha tem `pedido_id`, `versao`, `status` e `valor_centavos`. O pipeline anterior truncava a tabela e recarregava tudo.

O novo desenho usa:

- linha do arquivo como checkpoint;
- upsert condicionado à maior versão;
- transação por lote incluindo checkpoint;
- quarentena com linha e motivo;
- logs JSON por execução;
- reconciliação de leitura, aceitação e rejeição;
- reexecução sem mudanças adicionais.

```mermaid
sequenceDiagram
    participant F as CSV
    participant P as Pipeline
    participant B as SQLite
    P->>F: Ler após checkpoint
    F-->>P: Linhas novas
    P->>B: BEGIN + upserts + quarentena + checkpoint
    B-->>P: COMMIT
    P-->>P: Emitir métricas reconciliadas
```

Se o processo falha antes do commit, o checkpoint não avança. Se falha depois, a próxima execução começa após as linhas confirmadas.

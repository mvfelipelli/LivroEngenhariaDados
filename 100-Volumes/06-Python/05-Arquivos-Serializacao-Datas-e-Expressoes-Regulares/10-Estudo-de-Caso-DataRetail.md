---
title: Estudo de Caso — Normalização de Eventos da DataRetail
description: "JSONL, tempo UTC, validação e publicação atômica."
tags: [python, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Serialização]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

A DataRetail recebe eventos JSONL com ID, instante ISO 8601 e valor em centavos. Alguns produtores enviavam timestamp sem offset e IDs fora do padrão.

A nova fronteira executa:

- leitura UTF-8 linha a linha;
- parsing JSON isolado por registro;
- validação de chaves e tipos;
- ID por regex ancorada;
- rejeição de datetime naive;
- conversão para UTC com `Z`;
- ordenação determinística;
- escrita CSV temporária e substituição atômica.

```mermaid
flowchart LR
    J["JSONL"] --> P["Parse + validar"]
    P --> U["UTC"]
    P --> Q["Quarentena"]
    U --> O["Ordenar"]
    O --> T["CSV temporário"]
    T --> A["CSV publicado"]
```

O consumidor nunca observa um arquivo parcialmente escrito. Rejeições preservam número da linha e motivo sem expor dados sensíveis.

---
title: Introdução
description: "Semântica explícita para tempo e estruturas flexíveis."
tags: [sql, introducao, semiestruturado]
aliases: [Introdução a SQL Temporal e JSON]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

“Quando ocorreu?” pode significar instante do evento, registro na origem, ingestão ou conhecimento pelo banco. “Qual era o estado?” exige validade. Do mesmo modo, um campo JSON pode conter número, texto, ausente ou `null`, estados que não são equivalentes.

```mermaid
flowchart TD
    F["Fato do domínio"] --> E["Tempo do evento"]
    F --> V["Validade no negócio"]
    F --> S["Tempo do sistema"]
    F --> P["Payload semiestruturado"]
    E --> Q["Consulta correta"]
    V --> Q
    S --> Q
    P --> Q
```

O modelo relacional continua responsável por chaves, restrições e relações. JSON é valioso para atributos esparsos, envelopes e evolução controlada, mas campos essenciais e frequentemente consultados merecem contrato explícito.

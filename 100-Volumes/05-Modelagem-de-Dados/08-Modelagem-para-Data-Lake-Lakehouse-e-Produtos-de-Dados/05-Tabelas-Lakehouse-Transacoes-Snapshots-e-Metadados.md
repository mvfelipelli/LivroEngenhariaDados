---
title: Tabelas Lakehouse, Transações, Snapshots e Metadados
description: "Camada de tabela sobre arquivos e object storage."
tags: [lakehouse, snapshots, metadados]
aliases: [Tabelas Lakehouse]
created: 2026-07-17
updated: 2026-07-17
---

# Tabelas Lakehouse, Transações, Snapshots e Metadados

Formatos de tabela como Apache Iceberg, Delta Lake e Apache Hudi mantêm metadados que apontam para conjuntos consistentes de arquivos. Eles oferecem snapshots, evolução e operações transacionais conforme suas garantias.

```mermaid
flowchart LR
    C["Catálogo"] --> M["Snapshot/metadata"]
    M --> A["Arquivo A"]
    M --> B["Arquivo B"]
    N["Novo commit"] --> M2["Novo snapshot"]
    M2 --> B
    M2 --> D["Arquivo D"]
```

Time travel consulta snapshot anterior; não substitui retenção, backup ou histórico semântico. Expiração de snapshots e remoção de arquivos órfãos precisam respeitar leitores concorrentes.

Catálogo resolve nomes, namespaces e versão atual. Concorrência usa controle otimista ou mecanismo equivalente; writers devem tratar conflito e retry idempotente.

> [!note]
> ACID da tabela não garante transação atômica entre tabelas nem qualidade do conteúdo.

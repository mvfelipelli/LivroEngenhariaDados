---
title: Linguagens, Bancos, Modelagem e Processamento
description: "Competências centrais para construir produtos de dados."
tags: [python, sql, modelagem-de-dados]
aliases: [Núcleo Técnico do Roadmap]
created: 2026-07-21
updated: 2026-07-21
---

# Linguagens, Bancos, Modelagem e Processamento

Modelagem define significado, histórico e granularidade. Python automatiza integração, validação e operação. Spark distribui transformações. PostgreSQL aprofunda persistência, transações e administração relacional.

```mermaid
flowchart LR
    M["Modelagem"] --> SQL["SQL"]
    SQL --> DB["PostgreSQL"]
    PY["Python"] --> SP["Spark"]
    M --> SP
    DB --> P["Produtos de dados"]
    SP --> P
```

O estudante deve saber escolher processamento local, banco ou motor distribuído. “Dados grandes” precisa de volume, SLA, custo e paralelizabilidade. Evidência central: construir pipeline idempotente com contrato, testes, reconciliação e explicação do plano.

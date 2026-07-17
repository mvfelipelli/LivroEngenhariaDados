---
title: Estudo de Caso — Gate Python da DataRetail
description: "Qualidade automatizada, pacote e diagnóstico operacional."
tags: [python, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Qualidade]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

Um pipeline da DataRetail era copiado para servidores e testado manualmente. A equipe passou a produzir um wheel e estabeleceu um gate:

- formatação, lint e tipos;
- unitários de transformação;
- integração com SQLite e filesystem temporário;
- contratos de schema;
- build de sdist e wheel;
- instalação do wheel em ambiente limpo;
- smoke test da CLI;
- logs JSON com `run_id`, `lote_id`, contagens e duração.

```mermaid
flowchart LR
    P["Pull request"] --> Q["Qualidade"]
    Q --> T["Testes"]
    T --> B["Build"]
    B --> S["Smoke do wheel"]
    S --> R["Release imutável"]
```

Tokens e registros pessoais foram excluídos por allowlist de campos. A release passou a ser rastreável até o commit e reproduzível a partir do lock aprovado.

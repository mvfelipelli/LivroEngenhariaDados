---
title: Introdução
description: "Integração resiliente e rastreável de fontes."
tags: [modelagem-de-dados, introducao, data-vault]
aliases: [Introdução ao Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Integração empresarial recebe chaves divergentes, atributos em ritmos diferentes e regras que mudam. Um modelo monolítico acopla ingestão, historização e interpretação. Data Vault separa essas responsabilidades.

```mermaid
flowchart LR
    F["Fontes"] --> S["Staging"]
    S --> R["Raw Vault"]
    R --> B["Business Vault"]
    B --> M["Information Marts"]
```

O Raw Vault preserva dados orientados à fonte com mínima transformação técnica. O Business Vault aplica regras derivadas. Marts oferecem modelos dimensionais, semânticos ou produtos específicos.

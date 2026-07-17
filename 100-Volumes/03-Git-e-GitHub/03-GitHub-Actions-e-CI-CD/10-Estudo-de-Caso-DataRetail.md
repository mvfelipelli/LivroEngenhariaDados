---
title: Estudo de Caso — CI/CD da DataRetail
description: "Pipeline protegido para worker e migrations."
tags: [github-actions, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Actions]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

A DataRetail S.A. reconstruiu artefatos em cada ambiente e guardava chave cloud como secret de repositório. Releases diferentes recebiam o mesmo nome e rollback não era testado.

## Novo pipeline

- PR executa lint, unitários, contratos, integração e scans;
- merge em `main` gera um artefato por digest, SBOM e atestação;
- staging recebe esse digest e executa smoke e reconciliação;
- produção usa environment, aprovação, OIDC e concurrency;
- deploy registra commit, digest, migration e métricas;
- rollback usa artefato anterior e schema compatível.

```mermaid
flowchart LR
    P["PR"] --> C["CI"]
    C --> B["Build único"]
    B --> S["Staging"]
    S --> G["Gate"]
    G --> D["Produção"]
    D --> O["Observação"]
```

Workflows externos são fixados por SHA; tokens têm escopo por job; código de fork não recebe segredo. O laboratório em [[14-Laboratorio]] valida a política estrutural desse DAG.

---
title: Git, Repositórios e Ciclo de Trabalho
description: "Versionamento do código, documentação e decisões."
tags: [git, repositorio, versionamento]
aliases: [Git no Ambiente]
created: 2026-07-21
updated: 2026-07-21
---

# Git, Repositórios e Ciclo de Trabalho

Git registra snapshots e permite comparar, revisar e recuperar mudanças. O repositório inclui código, documentação, contratos e configurações não sensíveis; exclui segredos, caches, ambientes, grandes dados gerados e artefatos recuperáveis.

Ciclo básico:

```mermaid
flowchart LR
    W["Working tree"] --> S["Stage"]
    S --> C["Commit"]
    C --> R["Remote"]
    R --> V["Revisão/CI"]
```

Antes de commit, confira `status`, diff e validações. Mensagens descrevem intenção. Branches isolam mudanças quando o fluxo exige revisão.

Git não substitui backup de tudo: histórico não enviado pode ser perdido, e arquivos ignorados precisam de outra estratégia.

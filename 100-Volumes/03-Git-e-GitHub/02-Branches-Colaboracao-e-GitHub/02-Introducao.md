---
title: Introdução à Colaboração com Git e GitHub
description: "Mudanças como fluxo técnico e social verificável."
tags: [git, github, introducao]
aliases: [Introdução GitHub]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Um branch permite divergência temporária; uma pull request torna essa divergência discutível, testável e governável. A qualidade depende tanto do tamanho e contexto da mudança quanto das configurações da plataforma.

```mermaid
sequenceDiagram
    participant A as Autor
    participant G as GitHub
    participant R as Revisores
    participant C as CI
    A->>G: push e pull request
    G->>R: solicita revisão
    G->>C: executa checks
    R-->>G: aprovação ou mudanças
    C-->>G: status
    G->>G: aplica regras e merge
```

GitHub não substitui Git: pull request relaciona branches e eventos, mas commits continuam sendo objetos Git. Da mesma forma, uma aprovação não prova correção; ela registra uma decisão sob evidências disponíveis.

> [!warning]
> Bypass administrativo sem processo transforma proteção em recomendação. Exceções devem ser mínimas, auditadas e revisadas.

Comece em [[03-Modelos-de-Colaboracao-Permissoes-e-Forks]].

---
title: Introdução ao GitHub Actions e CI/CD
description: "Automação acionada por eventos e promoção confiável."
tags: [github-actions, ci-cd, introducao]
aliases: [Introdução GitHub Actions]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Integração contínua reduz o intervalo entre mudança e feedback. Entrega contínua mantém artefato implantável; implantação contínua promove automaticamente conforme política. São capacidades diferentes.

```mermaid
flowchart TD
    E["Evento"] --> W["Workflow"]
    W --> J["Jobs em DAG"]
    J --> A["Artefato"]
    A --> P["Promoção"]
    P --> O["Observação e rollback"]
```

Workflow é código privilegiado: pode ler fonte, gerar artefatos e acessar ambientes. Revisão, pinning, permissões mínimas e isolamento são requisitos de segurança.

> [!warning]
> Automação rápida de um processo inseguro amplia o impacto. Desenhe confiança e recuperação antes de aumentar frequência.

Comece em [[03-Workflows-Eventos-Filtros-Contextos-e-Expressoes]].

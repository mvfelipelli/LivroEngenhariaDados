---
title: Resumo — GitHub Actions e CI/CD
description: "Síntese dos fundamentos de automação segura."
tags: [github-actions, ci-cd, resumo]
aliases: [Resumo GitHub Actions]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

Workflow confiável transforma evento em DAG, evidência, artefato imutável e promoção protegida.

```mermaid
mindmap
  root((CI CD))
    Execução
      eventos e jobs
      runners e matrix
      cache e artifacts
    Segurança
      permissions
      OIDC e environments
      SHA completo
    Entrega
      build único
      concurrency
      rollback
    Governança
      reuso
      métricas
      supply chain
```

Regras: permissões mínimas; código externo não confiável; cache regenerável; artefato por digest; OIDC; ambientes protegidos; migrations compatíveis; workflows reutilizáveis versionados; observabilidade e rollback.

Revise em [[12-Perguntas-de-Entrevista]] e [[13-Exercicios]].

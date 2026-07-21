---
title: CI/CD, Deploy Progressivo e Rollback
description: "Entrega segura de aplicações e contratos de dados."
tags: [apache-spark, ci-cd, rollback]
aliases: [CI/CD Spark]
created: 2026-07-20
updated: 2026-07-20
---

# CI/CD, Deploy Progressivo e Rollback

CI valida lint, testes, segurança, pacote e smoke test. CD promove o mesmo artefato, aplicando configuração por ambiente. Migrações de schema e checkpoint exigem plano próprio.

Deploy shadow executa sem publicar; canary processa partição ou intervalo limitado; blue-green mantém versões lado a lado e troca referência após reconciliação.

Rollback de código não desfaz dados já publicados. Antes do deploy, defina compatibilidade de leitura/escrita, versão de tabelas, checkpoint e estratégia de restauração.

```mermaid
flowchart LR
    B["Build"] --> T["Testes"]
    T --> S["Shadow/Canary"]
    S --> R["Reconciliação"]
    R --> P["Promoção"]
    R --> X["Rollback"]
```

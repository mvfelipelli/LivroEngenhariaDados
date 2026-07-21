---
title: Volumes, Trilhas e Dependências
description: "Progressão oficial e relações entre áreas da formação."
tags: [academia, volumes, roadmap]
aliases: [Trilha da Academia]
created: 2026-07-21
updated: 2026-07-21
---

# Volumes, Trilhas e Dependências

A ordem oficial parte de fundamentos, passa por sistemas e linguagens, avança para motores e plataformas e termina em arquitetura integrada. Linux, Git, SQL, modelagem e Python sustentam os volumes de Spark, bancos, Lakehouse e orquestração.

Nem toda dependência é rígida. Um profissional pode consultar um módulo avançado, mas deve retornar aos fundamentos quando um conceito pressuposto não estiver claro.

```mermaid
flowchart LR
    F["Fundamentos"] --> B["Linux, Git, SQL"]
    B --> P["Modelagem e Python"]
    P --> S["Spark e PostgreSQL"]
    S --> PL["Lakehouse e Plataforma"]
    PL --> A["Arquiteturas e Projeto"]
```

O [[ROADMAP|ROADMAP]] registra estado real; diretório existente não significa conteúdo concluído.

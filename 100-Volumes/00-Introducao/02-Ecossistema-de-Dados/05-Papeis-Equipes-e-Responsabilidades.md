---
title: Papéis, Equipes e Responsabilidades
description: "Colaboração entre engenharia, analytics, ciência, plataforma e negócio."
tags: [equipes-de-dados, papeis, ownership]
aliases: [Papéis no Ecossistema de Dados]
created: 2026-07-21
updated: 2026-07-21
---

# Papéis, Equipes e Responsabilidades

Engenharia de Dados constrói fluxos e produtos; Analytics Engineering modela dados de consumo; BI desenvolve análise e visualização; Ciência de Dados experimenta e modela; ML Engineering operacionaliza modelos; plataforma oferece capacidades compartilhadas; governança estabelece políticas e apoio.

Responsabilidades variam por empresa. Uma matriz RACI pode esclarecer quem executa, aprova, consulta e é informado, mas não substitui colaboração.

```mermaid
flowchart LR
    N["Domínio de negócio"] <--> DE["Engenharia de Dados"]
    DE <--> AE["Analytics Engineering"]
    AE <--> BI["BI/Analytics"]
    DE <--> DS["Ciência/ML"]
    PF["Plataforma"] --> DE
    GV["Governança"] --> N
    GV --> DE
```

Todo produto precisa de owner semântico e técnico claramente identificados.

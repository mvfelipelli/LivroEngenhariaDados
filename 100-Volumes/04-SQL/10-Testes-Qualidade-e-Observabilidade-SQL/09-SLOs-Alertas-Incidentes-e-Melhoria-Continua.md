---
title: SLOs, Alertas, Incidentes e Melhoria Contínua
description: "Compromissos mensuráveis e resposta operacional."
tags: [sql, slo, alertas, incidentes]
aliases: [SLO de Dados]
created: 2026-07-17
updated: 2026-07-17
---

# SLOs, Alertas, Incidentes e Melhoria Contínua

Um SLI mede comportamento; um SLO define alvo; um SLA formaliza consequência externa. Para dados, exemplos incluem freshness, completude, sucesso de execução e tempo de recuperação.

```text
SLI: percentual de dias com mart_receita publicado até 06:00
SLO: 99,5% em janela móvel de 90 dias
```

Alertas devem ser acionáveis, possuir owner, severidade, contexto, runbook e condição de recuperação. Páginas são adequadas a impacto imediato; tickets atendem degradações que toleram horário comercial.

```mermaid
flowchart LR
    S["SLI fora do objetivo"] --> A["Alerta"]
    A --> T["Triagem"]
    T --> M["Mitigação"]
    M --> R["Recuperação"]
    R --> P["Postmortem"]
    P --> C["Controle preventivo"]
```

Postmortem sem culpa descreve impacto, linha do tempo, causa, fatores contribuintes, detecção e ações com responsáveis e prazos.

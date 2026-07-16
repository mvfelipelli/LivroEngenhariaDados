---
title: Requisitos, SLOs, Topologia e Modelo Operacional
description: "Conversão de objetivos em arquitetura e responsabilidades."
tags: [linux, operacao, slo, topologia]
aliases: [Modelo Operacional de Dados, SLO Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Requisitos, SLOs, Topologia e Modelo Operacional

Requisitos operacionais devem ser mensuráveis: disponibilidade, atraso máximo, janela de processamento, RPO, RTO, retenção, throughput e segurança. “Sempre disponível” não orienta decisões.

## Topologia

Mapeie processos, hosts, volumes, redes, identidades, portas, fluxos, dependências e failure domains. Uma réplica no mesmo disco ou rack não cobre a falha compartilhada.

```mermaid
flowchart LR
    F["Fonte"] --> G["Gateway"]
    G --> W["Workers"]
    W --> B["Banco"]
    W --> L["Data Lake"]
    O["Observabilidade"] -. monitora .-> G
    O -. monitora .-> W
    O -. monitora .-> B
```

## SLO e orçamento de erro

SLI mede comportamento; SLO define alvo; SLA estabelece compromisso externo. O orçamento de erro equilibra confiabilidade e mudança, mas requer janela e população bem definidas.

O modelo operacional deve incluir owner, on-call, escalonamento, janela de manutenção, catálogo, runbook, mudança, acesso, backup e revisão de capacidade.

> [!tip]
> Registre dependência degradável, obrigatória ou assíncrona. Essa classificação orienta timeout, retry e fallback.

Próximo: [[04-Implantacao-Configuracao-e-Gestao-de-Servicos]].

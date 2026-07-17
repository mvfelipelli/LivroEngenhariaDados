---
title: Zonas Bronze, Silver, Gold e Responsabilidades
description: "Camadas com contratos e critérios de promoção."
tags: [bronze, silver, gold, medallion]
aliases: [Arquitetura Medalhão]
created: 2026-07-17
updated: 2026-07-17
---

# Zonas Bronze, Silver, Gold e Responsabilidades

Bronze preserva recepção e proveniência; Silver padroniza, deduplica e aplica contratos técnicos; Gold publica modelos orientados ao consumo.

| Zona | Grão e objetivo | Controles |
|---|---|---|
| Bronze | evento/registro recebido | imutabilidade, fonte, ingestão |
| Silver | entidade/evento canônico | tipos, chave, deduplicação |
| Gold | fato, dimensão ou agregado | semântica, SLO, reconciliação |

As zonas não são níveis automáticos de qualidade. Cada promoção exige critérios explícitos e falhas vão para quarentena com motivo e caminho de correção.

Bronze deve permitir replay; Silver deve oferecer identidade e interoperabilidade; Gold deve evitar múltiplas definições conflitantes da mesma métrica.

> [!warning]
> Copiar o mesmo arquivo entre pastas sem mudança de contrato não cria arquitetura em camadas.

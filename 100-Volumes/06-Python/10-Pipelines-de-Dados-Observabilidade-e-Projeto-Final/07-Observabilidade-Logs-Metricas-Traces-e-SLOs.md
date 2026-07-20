---
title: Observabilidade, Logs, Métricas, Traces e SLOs
description: "Evidência operacional e objetivos de serviço."
tags: [python, observabilidade, logs, metricas, slos]
aliases: [Observabilidade de Pipelines Python]
created: 2026-07-20
updated: 2026-07-20
---

# Observabilidade, Logs, Métricas, Traces e SLOs

Logs explicam eventos discretos; métricas agregam comportamento; traces conectam etapas e dependências. Todos compartilham `run_id`, pipeline, versão e ambiente.

Métricas essenciais incluem lidos, aceitos, rejeitados, escritos, duplicados, duração, atraso do watermark, retries e freshness. Contagens devem reconciliar: `lidos = aceitos + rejeitados`.

SLO traduz expectativa do consumidor, por exemplo: 99% das execuções concluídas até 07:00 e dados com atraso inferior a 30 minutos. SLI mede; error budget orienta prioridade.

Alertas precisam indicar impacto e ação. Runbook contém diagnóstico, dashboards, rollback, reprocessamento e escalonamento. Evite alta cardinalidade em labels e dados pessoais em logs.

Instrumentação deve permanecer válida em falhas, emitindo um único evento terminal por run.

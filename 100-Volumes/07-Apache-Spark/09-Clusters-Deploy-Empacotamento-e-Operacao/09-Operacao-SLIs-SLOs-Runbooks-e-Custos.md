---
title: Operação, SLIs, SLOs, Runbooks e Custos
description: "Gestão cotidiana, resposta e eficiência econômica."
tags: [apache-spark, slo, runbook]
aliases: [SLOs Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Operação, SLIs, SLOs, Runbooks e Custos

SLIs úteis incluem sucesso, duração, freshness, completude e atraso de streaming. SLO define objetivo e janela; alerta deve consumir orçamento de erro ou indicar risco real.

Runbook começa pelo sintoma, oferece consultas e decisões, registra ações seguras, escalonamento e validação final. Exemplos: executor perdido, backlog crescente, schema incompatível, skew e falha de commit.

Custo combina tempo de CPU/memória, armazenamento, rede e ociosidade. Métricas como custo por TB processado ou por lote válido permitem comparar otimizações. Spot/preemptible reduz preço, mas exige tolerância a interrupção e checkpoint adequado.

Postmortem sem culpabilização transforma incidente em mudanças verificáveis.

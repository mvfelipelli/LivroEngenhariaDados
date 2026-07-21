---
title: Resumo — Otimização Spark
description: "Síntese de execução, memória e desempenho."
tags: [apache-spark, performance, resumo]
aliases: [Resumo Otimização Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Resumo

- UI e event logs ligam sintomas a jobs, stages e tasks.
- Shuffle movimenta dados; spill move estruturas para disco.
- Heap, overhead, cache e workers disputam memória física.
- Skew aparece na cauda das métricas, não na média.
- Repartition corrige distribuição com shuffle; coalesce reduz.
- AQE adapta o plano usando estatísticas reais.
- Cache só vale para reuso comprovado.
- Benchmark controlado transforma tuning em engenharia.

O próximo módulo aplica o modelo estruturado a fluxos contínuos.

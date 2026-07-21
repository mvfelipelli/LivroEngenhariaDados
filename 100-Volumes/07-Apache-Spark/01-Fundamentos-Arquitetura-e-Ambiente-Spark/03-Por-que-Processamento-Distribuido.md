---
title: Por que Processamento Distribuído
description: "Escala, paralelismo, custos e critérios de adoção."
tags: [processamento-distribuido, escala, apache-spark]
aliases: [Por que Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Por que Processamento Distribuído

Distribuição é adequada quando dados ou prazo excedem a capacidade econômica de uma máquina. O ganho depende de o trabalho ser particionável e de a computação superar o custo de coordenação.

Pela Lei de Amdahl, se apenas a fração `p` é paralelizável em `n` unidades: `speedup <= 1 / ((1-p) + p/n)`. Mais executors não eliminam fonte lenta, skew, etapas seriais ou rede.

Para poucos gigabytes e transformação simples, SQL ou processamento local pode ser melhor. Para terabytes particionáveis e SLA reduzido, Spark tende a oferecer vantagem.

> [!warning]
> Distribuir um algoritmo ineficiente multiplica desperdício. Meça volume, vazão, SLA e custo.

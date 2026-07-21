---
title: Gabarito — Fundamentos Spark
description: "Respostas dos exercícios do módulo."
tags: [apache-spark, gabarito]
aliases: [Gabarito Fundamentos Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. Driver planeja; executor processa; cluster manager aloca recursos.
2. Transformações são lazy e compõem o plano até uma ação.
3. Em geral, 40 tasks, uma por partição.
4. Todo o conjunto iria ao driver, com risco de falta de memória.
5. `local[1]` reduz concorrência; `local[*]` usa todos os núcleos disponíveis.
6. Leitura alimenta filtro; agrupamento introduz provável shuffle; escrita é a ação.
7. Volume, duração, SLA, crescimento, paralelizabilidade, custo e operação.
8. Persistir custa memória/disco; materializar acrescenta I/O, mas cria fronteira durável.

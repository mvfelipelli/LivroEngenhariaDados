---
title: Resumo — Operação Spark
description: "Síntese de deploy, cluster e operação."
tags: [apache-spark, operacao, resumo]
aliases: [Resumo Operação Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Resumo

- `spark-submit` separa aplicação de plataforma.
- Client e cluster mode diferem pela localização do driver.
- Código, JARs e bibliotecas nativas precisam chegar aos executors.
- Cluster manager integra Spark ao modelo operacional existente.
- Recursos são dimensionados por métricas, não por máximo disponível.
- Dynamic allocation exige limites e shuffle compatível.
- CI/CD promove artefato imutável e valida dados.
- Rollback inclui efeitos publicados, schemas e checkpoints.
- SLOs e custo orientam operação contínua.

O próximo módulo integra o volume em um projeto final.

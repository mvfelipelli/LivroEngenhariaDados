---
title: Exercícios — Fundamentos Spark
description: "Atividades progressivas sobre arquitetura e ambiente."
tags: [apache-spark, exercicios]
aliases: [Exercícios Fundamentos Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Exercícios

1. Classifique driver, executor e cluster manager por responsabilidade.
2. Explique por que três transformações podem não executar imediatamente.
3. Um stage possui 40 partições. Quantas tasks são esperadas?
4. Identifique o risco de `spark.read.parquet(caminho).collect()` para 500 GB.
5. Compare `local[1]` e `local[*]` em teste automatizado.
6. Desenhe o DAG conceitual de leitura, filtro, agrupamento e escrita.
7. Proponha critérios mensuráveis para migrar um ETL local para Spark.
8. Desafio: uma ação é repetida três vezes sobre linhagem cara. Liste duas alternativas e custos.

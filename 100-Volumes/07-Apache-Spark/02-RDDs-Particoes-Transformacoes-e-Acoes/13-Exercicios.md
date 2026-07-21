---
title: Exercícios — RDDs e Partições
description: "Atividades progressivas sobre a API de baixo nível."
tags: [apache-spark, rdd, exercicios]
aliases: [Exercícios RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Exercícios

1. Explique as três palavras de “Resilient Distributed Dataset”.
2. Classifique `map`, `filter`, `reduceByKey` e `collect`.
3. Calcule o número provável de tasks para dois stages com 12 e 30 partições.
4. Reescreva uma soma baseada em `groupByKey` usando `reduceByKey`.
5. Explique por que uma closure que captura um modelo de 2 GB é problemática.
6. Compare `cache`, `persist` e checkpoint.
7. Proponha tratamento para uma chave que concentra 60% dos registros.
8. Desafio: desenhe uma transição segura de parser RDD para DataFrame tipado.

---
title: RDD, Imutabilidade, Distribuição e Linhagem
description: "Propriedades essenciais e tolerância a falhas dos RDDs."
tags: [apache-spark, rdd, linhagem]
aliases: [Propriedades de RDD]
created: 2026-07-20
updated: 2026-07-20
---

# RDD, Imutabilidade, Distribuição e Linhagem

Imutabilidade significa que `map` ou `filter` não altera a coleção de origem: cria uma descrição para outra coleção. Distribuição significa que suas partições podem residir e ser processadas em executors diferentes.

A linhagem é o grafo de dependências necessário para reconstrução. Se uma partição de saída for perdida, o scheduler identifica suas ancestrais e reexecuta apenas o trecho necessário quando possível.

> [!note]
> Resiliência não equivale a durabilidade. Sem escrita externa, os dados desaparecem quando a aplicação termina.

Linhas longas de dependência elevam o custo de recomputação. Persistência reutiliza resultados; checkpoint corta a linhagem após materialização confiável.

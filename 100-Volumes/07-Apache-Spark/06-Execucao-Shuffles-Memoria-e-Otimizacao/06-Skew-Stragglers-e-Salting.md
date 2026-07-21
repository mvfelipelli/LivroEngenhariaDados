---
title: Skew, Stragglers e Salting
description: "Desequilíbrio de dados e tasks que prolongam stages."
tags: [apache-spark, skew, salting]
aliases: [Data Skew Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Skew, Stragglers e Salting

Skew ocorre quando algumas chaves ou partições concentram volume. Na UI, poucas tasks apresentam input, shuffle, spill ou duração muito acima da mediana. Stragglers também podem resultar de host lento, GC ou retry; confirme a distribuição de bytes.

Tratamentos incluem:

- filtrar ou agregar antes do shuffle;
- transmitir o lado pequeno do join;
- separar chaves quentes;
- adicionar sal à chave quente e reagrupar depois;
- habilitar tratamento de skew do AQE.

Salting replica ou divide trabalho e acrescenta complexidade. Escolha número de sais pelo volume da chave, paralelismo e custo de recombinação. Não aplique globalmente sem evidência.

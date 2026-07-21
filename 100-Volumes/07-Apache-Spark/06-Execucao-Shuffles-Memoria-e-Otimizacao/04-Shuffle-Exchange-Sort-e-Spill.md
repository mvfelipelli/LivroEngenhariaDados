---
title: Shuffle, Exchange, Sort e Spill
description: "Redistribuição de dados e pressão sobre rede e disco."
tags: [apache-spark, shuffle, spill]
aliases: [Shuffle Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Shuffle, Exchange, Sort e Spill

`Exchange` no plano marca redistribuição por hash, range ou round-robin. Map tasks escrevem blocos; reduce tasks buscam blocos pela rede. Ordenação pode ser necessária para sort-merge join, janelas e `orderBy`.

Spill ocorre quando estruturas de execução não cabem na memória disponível e passam a disco. Um pouco de spill pode ser saudável; volumes grandes junto de GC e tasks longas indicam partições excessivas, agregação ampla ou memória insuficiente.

Reduza dados antes do shuffle com filtros e projeções, use agregação combinável e evite repartições consecutivas. Eliminar todo shuffle não é objetivo: agrupamento global exige movimento; o objetivo é movimento necessário e equilibrado.

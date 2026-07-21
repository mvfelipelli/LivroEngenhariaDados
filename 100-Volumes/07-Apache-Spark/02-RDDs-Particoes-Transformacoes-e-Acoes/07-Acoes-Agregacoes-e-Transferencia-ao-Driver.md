---
title: Ações, Agregações e Transferência ao Driver
description: "Materialização, resultados distribuídos e limites do driver."
tags: [apache-spark, acoes, driver]
aliases: [Ações de RDD]
created: 2026-07-20
updated: 2026-07-20
---

# Ações, Agregações e Transferência ao Driver

Ações materializam o plano. `count`, `reduce`, `take`, `saveAsTextFile` e `collect` iniciam jobs. A escolha define onde o resultado termina.

`take(20)` limita a transferência; `collect()` não. `reduce` exige operação associativa e comutativa para resultado independente da ordem distribuída. `fold` acrescenta elemento neutro; `aggregate` permite tipos distintos entre acumulador local e resultado.

> [!warning]
> Não use `count()` apenas para verificar se um RDD está vazio quando `isEmpty()` ou `take(1)` basta. A ação adequada reduz trabalho.

Resultados grandes devem permanecer distribuídos e ser gravados por partição, não retornar ao driver.

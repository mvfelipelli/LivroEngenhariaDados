---
title: Semântica de Join e Cardinalidade
description: "Tipos de junção, granularidade e multiplicação de linhas."
tags: [apache-spark, join, cardinalidade]
aliases: [Joins Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Semântica de Join e Cardinalidade

Inner preserva correspondências; left mantém todas as linhas da esquerda; full preserva ambos; left semi retorna linhas da esquerda que possuem correspondência; left anti retorna as que não possuem. Cross join produz produto cartesiano.

Se uma chave ocorre `m` vezes à esquerda e `n` à direita, o inner join pode produzir `m × n` linhas para essa chave. Portanto, “juntar por cliente” sem controlar granularidade duplica fatos.

```python
pedidos.join(clientes, on="cliente_id", how="left")
```

Valide unicidade da dimensão, contagem antes/depois, chaves órfãs e nulos. Deduplicar sem critério apenas oculta o problema.

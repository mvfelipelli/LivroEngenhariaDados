---
title: Gabarito — Spark SQL
description: "Respostas dos exercícios sobre SQL distribuído."
tags: [apache-spark, spark-sql, gabarito]
aliases: [Gabarito Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. Inner retorna correspondências; semi retorna linhas da esquerda com correspondência; anti, sem correspondência.
2. Doze linhas para a chave.
3. Quando tamanho serializado cabe com margem na memória de cada executor e evita shuffle relevante.
4. `rollup("data", "loja_id").agg(sum("valor_centavos"))`.
5. `lag("instante").over(Window.partitionBy("cliente_id").orderBy(...))`.
6. Janela por chave, ordem decrescente por versão/instante/ID e `row_number = 1`.
7. Igualdade comum não faz nulo corresponder a nulo; use semântica null-safe quando apropriado.
8. Unicidade das dimensões, órfãos, contagem de fatos, soma monetária e distribuição de multiplicidade por chave.

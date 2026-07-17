---
title: Gabarito — Consultas, Joins e Subconsultas
description: "Respostas orientadoras dos exercícios."
tags: [sql, gabarito, joins]
aliases: [Gabarito Joins SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

1. Grão define a linha; cardinalidade mede quantidade; multiplicidade descreve correspondências.
2. Interno mantém pares; esquerdo preserva a esquerda; cruzado produz todas as combinações.
3. Cada item combina com cada pagamento do mesmo pedido, formando N×M linhas.
4. Linhas sem correspondência recebem `NULL` e são eliminadas pelo filtro, anulando preservação.
5. `NOT EXISTS` testa ausência por correlação; `NOT IN` pode ficar desconhecido se houver `NULL`.
6. `WHERE NOT EXISTS (SELECT 1 FROM pedidos p WHERE p.cliente_id = c.cliente_id)`.
7. Ambas são válidas; pré-agregação costuma explicitar melhor o grão e servir vários atributos.
8. `UNION ALL` preserva; `UNION` elimina, desde que colunas sejam compatíveis.
9. Crie CTEs agregadas por `pedido_id` e faça joins 1:1 com pedidos.
10. Use âncora, `UNION ALL`, referência recursiva e coluna `profundidade` com limite.

Respostas alternativas são corretas quando preservam semântica e demonstram os invariantes.

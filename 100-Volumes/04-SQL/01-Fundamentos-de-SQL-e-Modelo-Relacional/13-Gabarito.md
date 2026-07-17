---
title: Gabarito — Fundamentos de SQL
description: "Respostas orientadoras dos exercícios."
tags: [sql, gabarito, relacional]
aliases: [Gabarito Fundamentos SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

1. Schema define estrutura; relação é conjunto de tuplas; tupla associa atributos a valores; atributo nomeia propriedade; domínio limita valores.
2. Definição, consulta, manipulação, controle de acesso e controle transacional.
3. Relações não possuem ordem e o plano físico pode variar.
4. Use `email IS NULL`, pois comparação com `NULL` resulta em desconhecido.
5. `COUNT(*)` conta a linha preservada; `COUNT(pedido_id)` retorna zero quando não há pedido correspondente.
6. `CREATE TABLE produtos (produto_id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco NUMERIC NOT NULL CHECK (preco >= 0));`.
7. Use `WHERE ativo = 1 AND cidade IN (...) ORDER BY nome, cliente_id`.
8. `CASE` com limites explícitos, ordenados do maior para o menor.
9. `LEFT JOIN`, agrupamento por chave e nome, `COUNT(p.pedido_id)` e `COALESCE(SUM(p.valor), 0)`.
10. Tipos e coerções, funções de data/texto, quoting, concatenação e paginação são exemplos válidos.

O gabarito orienta a semântica; nomes e valores podem variar sem alterar o princípio.

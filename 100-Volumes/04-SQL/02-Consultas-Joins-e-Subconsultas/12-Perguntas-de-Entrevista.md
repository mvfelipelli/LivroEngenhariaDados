---
title: Perguntas de Entrevista — Joins e Subconsultas
description: "Questões práticas com respostas fundamentadas."
tags: [sql, entrevista, joins, subconsultas]
aliases: [Entrevista Joins SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. O que é grão de uma consulta?

É o fato representado por cada linha, como uma linha por pedido ou por item.

## 2. INNER e LEFT JOIN diferem como?

O interno mantém apenas correspondências; o esquerdo preserva todas as linhas da esquerda.

## 3. Como um filtro transforma LEFT em INNER na prática?

Ao exigir em `WHERE` uma coluna da direita, linhas completadas com `NULL` são descartadas.

## 4. O que é fanout?

Multiplicação de linhas causada por cardinalidade 1:N ou N:N, frequentemente inflando agregações.

## 5. Quando usar EXISTS em vez de JOIN?

Quando a pergunta é apenas existência e a linha externa não deve ser duplicada.

## 6. Por que NOT EXISTS costuma ser mais seguro que NOT IN?

Porque `NULL` no conjunto de `NOT IN` pode produzir resultado desconhecido.

## 7. O que é subconsulta correlacionada?

Uma subconsulta que referencia colunas da consulta externa.

## 8. CTE sempre melhora desempenho?

Não. Ela melhora estrutura; materialização ou inlining dependem do mecanismo e do plano.

## 9. UNION e UNION ALL diferem como?

`UNION` elimina duplicatas; `UNION ALL` preserva e normalmente evita esse custo.

## 10. Como evitar totais inflados com duas relações filhas?

Pré-agregar cada filha ao grão do pai antes dos joins.

## 11. Como funciona uma CTE recursiva?

Um termo âncora inicia resultados e um termo recursivo produz novas linhas até não haver saída.

## 12. Como testar um join?

Validar contagem, unicidade, nulos, linhas sem correspondência e totais de controle.

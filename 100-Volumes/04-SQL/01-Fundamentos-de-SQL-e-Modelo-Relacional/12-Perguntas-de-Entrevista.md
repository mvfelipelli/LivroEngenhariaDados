---
title: Perguntas de Entrevista — Fundamentos de SQL
description: "Questões práticas com respostas fundamentadas."
tags: [sql, entrevista, fundamentos]
aliases: [Entrevista Fundamentos SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Por que SQL é declarativo?

Porque descreve o resultado desejado, não o algoritmo físico para obtê-lo. O SGBD escolhe o plano.

## 2. Tabela e relação são sinônimos perfeitos?

Não. Relação formal é conjunto sem ordem ou duplicatas; tabelas e resultados SQL seguem semântica de multiconjunto em muitos contextos.

## 3. Qual a diferença entre chave primária e estrangeira?

A primária identifica uma linha; a estrangeira referencia uma chave de outra relação e preserva integridade referencial.

## 4. Por que evitar `SELECT *`?

Ele cria contrato instável, transfere colunas desnecessárias e pode quebrar consumidores após evolução do schema.

## 5. `NULL = NULL` é verdadeiro?

Não; a comparação resulta em desconhecido. Testes de ausência usam `IS NULL`.

## 6. Sem `ORDER BY`, qual é a ordem?

Nenhuma ordem é garantida. O plano pode mudar entre execuções.

## 7. `DISTINCT` corrige duplicidade de join?

Ele apenas elimina duplicatas do resultado. A causa pode ser cardinalidade ou predicado incorreto e deve ser compreendida.

## 8. `COUNT(*)` e `COUNT(coluna)` diferem?

O primeiro conta linhas; o segundo conta valores não nulos da coluna.

## 9. `LEFT JOIN` pode comportar-se como `INNER JOIN`?

Sim, se `WHERE` exigir um valor não nulo da relação direita e eliminar as linhas sem correspondência.

## 10. O que é ordem lógica da consulta?

É a sequência conceitual que forma fontes, filtra, agrupa, projeta e ordena, distinta da sintaxe e do plano físico.

## 11. Constraints substituem validação da aplicação?

Não; complementam-na e garantem invariantes contra qualquer escritor.

## 12. Como lidar com dialetos?

Manter núcleo portável, documentar extensões, isolar diferenças e testar no mecanismo de destino.

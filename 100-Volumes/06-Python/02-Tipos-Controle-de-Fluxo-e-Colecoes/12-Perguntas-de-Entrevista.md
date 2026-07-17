---
title: Perguntas de Entrevista — Tipos e Coleções Python
description: "Questões sobre valores, fluxo e estruturas."
tags: [python, entrevista, colecoes]
aliases: [Entrevista Tipos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Qual a diferença entre `is` e `==`?

`is` compara identidade; `==` delega ao protocolo de igualdade dos objetos.

## 2. Por que argumento default mutável é perigoso?

O objeto é criado uma vez na definição e pode acumular estado entre chamadas. Use `None` e crie a coleção dentro da função.

## 3. Por que `0.1 + 0.2 != 0.3`?

Porque esses decimais não possuem representação binária finita em `float`.

## 4. Quando usar tuple em vez de list?

Quando a estrutura é fixa, não deve ser alterada e sua semântica é posicional ou precisa ser hashable.

## 5. Qual o custo médio de busca em dict?

O(1), sustentado por tabela hash, embora o pior caso e custos de redimensionamento existam.

## 6. Dict preserva ordem?

Sim, ordem de inserção faz parte da linguagem nas versões modernas; isso não equivale a ordenar por chave.

## 7. `sorted()` e `.sort()` diferem como?

`sorted()` aceita qualquer iterável e cria lista; `.sort()` altera uma lista e retorna `None`.

## 8. Quando evitar comprehension?

Quando contém lógica ramificada, efeitos, tratamento de erros ou fica difícil nomear e testar etapas.

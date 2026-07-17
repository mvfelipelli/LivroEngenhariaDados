---
title: Perguntas de Entrevista — NumPy e Pandas
description: "Questões sobre arrays, DataFrames e performance."
tags: [python, entrevista, pandas]
aliases: [Entrevista Processamento Tabular]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. O que strides representam?

Quantidade de bytes avançada no buffer para mover um elemento em cada eixo.

## 2. Slice NumPy copia?

Indexação básica geralmente cria view; indexação avançada normalmente cria cópia.

## 3. O que é broadcasting?

Regra que combina shapes comparando eixos da direita, quando iguais ou um deles é 1.

## 4. Series somam por posição?

Não necessariamente; operações alinham pelo índice antes de calcular.

## 5. Por que usar `Int64` em Pandas?

Para inteiros nullable sem promover a coluna para float por causa de ausência.

## 6. Como impedir fanout inesperado?

Declare `validate` no merge, verifique unicidade da chave e reconcilie linhas e medidas.

## 7. `agg` e `transform` diferem como?

Agg reduz grupos; transform devolve resultado alinhado ao tamanho original.

## 8. Chunking resolve qualquer volume?

Não. Funciona para operações combináveis; joins e estatísticas não associativas podem exigir outra estratégia.

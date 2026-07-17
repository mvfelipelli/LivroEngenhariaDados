---
title: Perguntas de Entrevista
description: "Perguntas sobre normalização e modelo relacional."
tags: [modelagem-de-dados, entrevista, normalizacao]
aliases: [Entrevista Normalização]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Chave candidata e primária diferem como?

Candidata é qualquer identificador mínimo; primária é uma candidata escolhida como referência principal.

## 2. O que é dependência funcional?

Regra em que igualdade no determinante implica igualdade no atributo determinado.

## 3. O que é dependência parcial?

Atributo não primo depende de parte própria de chave candidata composta.

## 4. O que a 3FN evita?

Determinantes não chave inadequados, incluindo dependências transitivas de atributos não primos.

## 5. BCNF e 3FN diferem como?

BCNF exige todo determinante como superchave; 3FN permite exceção quando o atributo determinado é primo.

## 6. O que é decomposição sem perda?

Projeções podem ser reunidas para reconstruir exatamente as tuplas válidas originais.

## 7. O que é preservação de dependências?

Capacidade de verificar dependências nas relações decompostas sem junção.

## 8. Quando aplicar 4FN?

Quando uma relação mistura fatos multivalorados independentes sobre a mesma chave.

## 9. Normalização elimina JOINs?

Não. Ela frequentemente introduz relações que são compostas por joins semanticamente corretos.

## 10. Quando desnormalizar?

Após medir um problema e definir fonte canônica, sincronização, validação e custo de escrita.

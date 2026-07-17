---
title: Gabarito — Bancos e APIs Python
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, integracao]
aliases: [Gabarito Bancos APIs Python]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

`conexao.execute("SELECT ... WHERE id = ?", (identificador,))`.

## 2

Execute ambos dentro do mesmo contexto transacional; qualquer exceção deve reverter dados e cursor.

## 3

Timeout pode ser transitório se idempotente; constraint de dado não; deadlock geralmente pode ser repetido desde o início.

## 4

200 parseia; 304 usa cache; 401 interrompe e sinaliza credencial; 429 respeita Retry-After; 503 pode repetir com backoff.

## 5

URLs aparecem em histórico, proxy e logs; use header e transporte TLS.

## 6

Mantenha set de cursores observados e contador máximo; falhe se houver repetição ou excesso.

## 7

Confirme dict, lista, tipos de cada item e `str | None` para cursor antes de persistir.

## 8

Consuma página, valide, abra transação, aplique upserts e checkpoint, commit e só então solicite a próxima.

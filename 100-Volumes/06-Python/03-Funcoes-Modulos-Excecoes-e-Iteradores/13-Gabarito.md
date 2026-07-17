---
title: Gabarito — Funções e Iteradores Python
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, iteradores]
aliases: [Gabarito Funções Python]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

`def total(valores, /, *, ignorar_negativos=False): ...` torna os modos de chamada explícitos.

## 2

A lista é compartilhada entre chamadas. Use `itens=None` e crie uma lista dentro.

## 3

Uma função externa recebe o mínimo e devolve função interna que compara cada valor.

## 4

Domínio não importa CLI; parsing converte formatos para domínio; CLI coordena ambos. Assim, regras permanecem reutilizáveis.

## 5

No `except ValueError as erro`, execute `raise PedidoInvalido(...) from erro`.

## 6

Armazene página atual, retorne `self` em `__iter__` e lance `StopIteration` após n.

## 7

Acumule até o limite, faça `yield tuple(lote)`, limpe e emita o restante no fim.

## 8

Use funções geradoras para parse e validação, callback de quarentena e context manager em torno do consumo pelo sink.

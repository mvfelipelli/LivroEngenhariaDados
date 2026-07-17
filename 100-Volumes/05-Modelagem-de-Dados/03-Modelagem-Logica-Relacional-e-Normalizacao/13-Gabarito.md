---
title: Gabarito
description: "Respostas dos exercícios de normalização."
tags: [modelagem-de-dados, gabarito, normalizacao]
aliases: [Gabarito Normalização]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Se email identifica aluno e `(aluno,turma)` identifica matrícula, `(aluno,turma)` e `(email,turma)` são candidatas; nota não participa da identidade.

## 2

`pedido→cliente,data`; `(pedido,item)→produto,quantidade,preco`; `produto→nome`.

## 3

`A+={A,B,C}`. `D` e `E` não são alcançados sem `D` junto a `C`.

## 4

Dados do cabeçalho determinados só por `pedido_id` dependem de parte da chave `(pedido_id,numero_item)`.

## 5

Separe `CLIENTE(cliente_id,nome)` e `PEDIDO(pedido_id,cliente_id,...)`.

## 6

Use `PROFISSIONAL_IDIOMA` e `PROFISSIONAL_CERTIFICACAO`; não armazene o produto cartesiano.

## 7

A interseção é `B`; como `B→C`, ela determina `R2`, satisfazendo o critério binário de junção sem perda.

## 8

Separe Produto, Categoria recursiva, Fornecedor, Oferta e HistóricoPreço; declare identidades, validade sem sobreposição e referências.

---
title: Gabarito — NumPy e Pandas
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, pandas]
aliases: [Gabarito Processamento Tabular]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Use `np.arange(6, dtype="int64").reshape(2, 3)` e leia os atributos pedidos.

## 2

Crie `view = base[1:3]`, altere `view[0]` e confirme a posição correspondente em `base`.

## 3

Matriz `(linhas, colunas)` vezes vetor `(colunas,)` usa broadcasting por coluna.

## 4

Construa e aplique `astype` aos campos; use `pd.to_datetime(..., utc=True)` para instante.

## 5

Conte `isna` antes e depois; valores novos revelam conversões inválidas e devem ser rejeitados.

## 6

Use `merge(..., validate="many_to_one", indicator=True)` e filtre `_merge != "both"`.

## 7

Ordene ID, versão e instante e aplique `drop_duplicates(id, keep="last")`.

## 8

Filtre atuais aprovados, junte itens, agregue e compare contagem e soma em ambas as camadas.

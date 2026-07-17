---
title: Gabarito — Tipos e Coleções Python
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito, colecoes]
aliases: [Gabarito Tipos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Imprime `[1]`: ambos os nomes referenciam a mesma lista mutável.

## 2

Use `"valor" in registro`; depois compare `registro["valor"] is None`; caso contrário, `== 0` verifica zero.

## 3

`1999` centavos é simples e eficiente; `Decimal("19.99")` preserva escala decimal e oferece regras explícitas, com maior custo.

## 4

`dados = "ação".encode("utf-8")`; então `dados.decode("utf-8") == "ação"` é verdadeiro.

## 5

Lista para ordem e duplicatas; set para IDs únicos; dict para consulta por ID.

## 6

Use `totais[loja] = totais.get(loja, 0) + valor` em um loop.

## 7

`sorted(totais.items(), key=lambda item: (-item[1], item[0]))`.

## 8

Valide tipo e domínio, mantenha `dict[id]` substituindo somente por versão maior, agregue em outro dict e serialize chaves ordenadas.

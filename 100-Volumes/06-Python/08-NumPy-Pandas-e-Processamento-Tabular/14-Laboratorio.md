---
title: Laboratório — Mart Tabular Reconciliado
description: "Deduplicação, joins validados e agregação com Pandas."
tags: [python, laboratorio, numpy, pandas]
aliases: [Laboratório Pandas]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Mart Tabular Reconciliado

## Objetivo

Construir mart de vendas por loja preservando maior versão, cardinalidade e total.

## Pré-requisitos

- Python 3.11 ou superior;
- NumPy 2 e Pandas 3;
- [[07-Acesso-a-Bancos-de-Dados-e-APIs/README|Acesso a Bancos e APIs]].

## Ambiente

Use o ambiente do projeto com NumPy e Pandas e salve a solução como `mart.py`.

## Passos

1. Construa pedidos versionados e itens.
2. Defina dtypes explicitamente.
3. Deduplicate pedidos pela maior versão.
4. Filtre aprovados.
5. Junte itens com pedidos usando many-to-one.
6. Rejeite órfãos via indicador.
7. Agregue por loja e ordene.
8. Reconcilie contagem e soma e repita a transformação.

## Validação

O mart deve conter SP com dois itens e `3700` centavos, RJ com um item e `800`, total `4500`, três itens e resultado determinístico.

## Conclusão

O laboratório transforma DataFrame em produto controlado por grão, cardinalidade e reconciliação.

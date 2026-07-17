---
title: Laboratório — Agregador Determinístico de Pedidos
description: "Deduplicação, validação e agregação com coleções nativas."
tags: [python, laboratorio, colecoes]
aliases: [Laboratório Coleções Python]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Agregador Determinístico de Pedidos

## Objetivo

Consolidar eventos em memória, deduplicando versões e produzindo ranking por loja.

## Pré-requisitos

- Python 3.11 ou superior;
- conceitos do [[01-Fundamentos-Ambiente-e-Ferramentas-Python/README|Módulo 01]];
- nenhuma biblioteca externa.

## Ambiente

Use um ambiente virtual e salve a solução como `agregar.py`.

## Passos

1. Modele eventos como dicionários.
2. Valide ID, loja, versão inteira positiva, status permitido e valor não negativo.
3. Deduplicate por ID, escolhendo a maior versão.
4. Considere somente pedidos `aprovado`.
5. Agregue quantidade e total em centavos por loja.
6. Ordene total decrescente e loja crescente.
7. Confirme que inverter a entrada não altera a saída.

## Validação

A amostra deve produzir duas lojas, três pedidos aprovados e `4500` centavos. A execução com a lista invertida deve ser idêntica.

## Conclusão

Tipos, política de duplicidade e critérios de ordenação compõem o contrato do resultado.

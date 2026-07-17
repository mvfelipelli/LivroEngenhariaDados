---
title: Laboratório — Pipeline Preguiçoso em Lotes
description: "Transformação incremental, quarentena e controle de recursos."
tags: [python, laboratorio, geradores]
aliases: [Laboratório Iteradores Python]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Pipeline Preguiçoso em Lotes

## Objetivo

Processar linhas de pedidos incrementalmente, separar rejeições e formar lotes limitados.

## Pré-requisitos

- Python 3.11 ou superior;
- [[02-Tipos-Controle-de-Fluxo-e-Colecoes/README|Tipos, Controle de Fluxo e Coleções]];
- nenhuma dependência externa.

## Ambiente

Salve a solução como `pipeline.py` e execute no ambiente virtual do projeto.

## Passos

1. Defina `PedidoInvalido`.
2. Converta linhas `id,valor_centavos` sem capturar erros inesperados.
3. Envie falhas de domínio para uma lista de quarentena.
4. Produza lotes imutáveis de tamanho dois.
5. Instrumente a fonte para confirmar seu fechamento.
6. Verifique que o pipeline não consome além da demanda.

## Validação

A amostra deve produzir dois lotes com três pedidos válidos, uma rejeição, total de `4500` centavos e `fonte_fechada=True`.

## Conclusão

O fluxo limita memória, preserva falhas de domínio e encerra recursos na fronteira correta.

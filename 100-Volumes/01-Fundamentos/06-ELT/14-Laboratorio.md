---
title: Laboratório — Raw, Staging e Mart com SQL
aliases: [Laboratório ELT]
tags: [engenharia-de-dados, fundamentos, elt, laboratorio, sql, sqlite]
type: laboratory
order: 14
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Laboratório reproduzível de camadas ELT e testes de dados."
---

# 14 — Laboratório

## Objetivo

Carregar versões brutas em SQLite e transformar por SQL em staging deduplicado e mart de vendas confirmadas.

## Pré-requisitos

- Python 3.11+;
- nenhuma dependência externa.

## Requisitos

1. raw append-only com lote e ingestão;
2. staging com maior versão por chave;
3. mart somente com confirmados;
4. líquido calculado;
5. testes de unicidade, domínio e reconciliação;
6. rebuild idempotente;
7. linhagem registrada.

## Resultado esperado

```text
raw=4
staging=3
mart=2
receita_liquida=230.00
testes=ok
rebuild=ok
linhagem=raw_orders>stg_orders>mart_sales
```

## Próximo Capítulo

➡️ [[14-Solucao|14 — Solução]]

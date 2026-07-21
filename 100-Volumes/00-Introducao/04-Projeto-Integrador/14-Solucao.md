---
title: Solução — Charter do Projeto DataRetail
description: "Modelo resumido para iniciar o projeto."
tags: [projeto-integrador, solucao, planejamento]
aliases: [Solução Charter DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Solução — Charter do Projeto DataRetail

## Problema

Receita divergente e pedidos sem rastreabilidade entre lojas e e-commerce.

## Objetivo

Publicar Pedidos Canônicos e Receita Diária reconciliada até 07:00, com 100% da entrada classificada.

## Primeiro marco

```mermaid
flowchart LR
    S["CSV sintético"] --> V["Validação"]
    V --> Q["Quarentena"]
    V --> P["Pedidos"]
    P --> R["Receita diária"]
```

## Critérios

- seed e entrada versionadas;
- `entrada = válidos + quarentena`;
- chave canônica única;
- soma monetária reconciliada;
- execução repetida sem duplicar;
- testes e README aprovados.

## Riscos

Schema instável, definição de receita ambígua e inclusão de dados reais. Owners: Vendas, Financeiro e Segurança, respectivamente.

---
title: Laboratório — Contrato de Produto em Camadas
description: "Validação reproduzível de schema, camadas e compatibilidade."
tags: [modelagem-de-dados, python, laboratorio, data-product]
aliases: [Laboratório Produto Lakehouse]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Contrato de Produto em Camadas

## Objetivo

Validar eventos Bronze, promover registros válidos para Silver, produzir Gold no grão correto e testar compatibilidade de schema.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Declare contrato v1 com campos obrigatórios e tipos.
2. Receba três eventos Bronze, um inválido.
3. Valide e envie inválido à quarentena.
4. Deduplicate Silver por `evento_id`.
5. Produza Gold por item de pedido.
6. Valide chave única e total.
7. Confirme que v2 adiciona campo opcional de forma compatível.

## Validação esperada

```text
bronze=3
silver=2
quarentena=1
gold_itens=3
total_centavos=4500
chaves_unicas=ok
schema_v2=compativel
produto=ok
```

Consulte [[14-Solucao|Solução]].

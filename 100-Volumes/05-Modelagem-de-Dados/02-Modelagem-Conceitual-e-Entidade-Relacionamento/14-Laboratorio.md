---
title: Laboratório — Modelo Conceitual de Marketplace
description: "Validação executável de entidade associativa e cardinalidades."
tags: [modelagem-de-dados, sqlite, laboratorio, er]
aliases: [Laboratório Modelo ER]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Modelo Conceitual de Marketplace

## Objetivo

Traduzir vendedor, produto, oferta, pedido e item em esquema de validação e provar identidade da associação e referências.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie vendedor, produto e oferta associativa.
2. Faça oferta única por vendedor e código interno.
3. Crie pedido e item dependente do pedido.
4. Preserve preço praticado no item.
5. Insira duas ofertas para o mesmo produto.
6. Confirme rejeição de oferta duplicada e referência inválida.
7. Calcule vendedores, ofertas, itens e total.

## Validação esperada

```text
vendedores=2
produtos=1
ofertas=2
itens=2
total_centavos=5100
oferta_duplicada=rejeitada
referencia_invalida=rejeitada
modelo_er=ok
```

Consulte [[14-Solucao|Solução]].

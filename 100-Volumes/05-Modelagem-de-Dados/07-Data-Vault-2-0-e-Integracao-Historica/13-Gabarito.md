---
title: Gabarito
description: "Respostas dos exercícios de Data Vault."
tags: [modelagem-de-dados, gabarito, data-vault]
aliases: [Gabarito Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Use identificadores reconhecidos no domínio e qualifique fonte quando não forem corporativos.

## 2

Link pedido-cliente conecta dois Hubs; item pode ser Link transacional entre pedido e produto com identificador do item no grão.

## 3

CRM e e-commerce em Satellites distintos; atributos rápidos podem ser separados dos estáveis.

## 4

Tipos e ordem fixos, Unicode normalizado, timezone/precisão definidos, marcador de `NULL` e serialização sem ambiguidade.

## 5

Carregue o mesmo staging duas vezes e confirme contagens e hashes idênticos em Hubs, Links e Satellites.

## 6

Satellite inclui cliente_hk e tipo/posição do telefone como discriminador, além do valor e load timestamp.

## 7

PIT guarda para cada Hub/data as chaves ou timestamps das últimas linhas válidas dos três Satellites.

## 8

Combine Satellites por PIT, aplique survivorship no Business Vault, detecte mudança dos atributos dimensionais e emita versões SCD2.

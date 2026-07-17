---
title: Gabarito
description: "Respostas dos exercícios de modelagem física."
tags: [modelagem-de-dados, gabarito, desempenho]
aliases: [Gabarito Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Centavos inteiros ou decimal exato; timestamp com timezone; `DATE`; texto para código postal, pois zeros e formato importam.

## 2

Sequência é compacta e coordenada; UUID distribui geração; natural deduplica fonte. Uma chave corporativa pode coexistir com `(fonte,id_origem)` única.

## 3

`(cliente_id, criado_em DESC)` e colunas incluídas conforme projeção e suporte do SGBD.

## 4

Faixa mensal permite descarte por partição e pruning; avalie volume para evitar partições pequenas.

## 5

Chave de alta cardinalidade usada em joins, como cliente ou pedido; loja pode gerar skew se uma unidade dominar.

## 6

Atendimento usa row store/indexado; BI usa cópia colunar particionada, mantendo contrato e reconciliação.

## 7

Itens são fonte; total é atualizado transacionalmente ou por projeção idempotente e comparado periodicamente à soma.

## 8

Adicionar UUID, preencher, escrever ambas, criar unicidade e referências paralelas, migrar leitores/escritores, validar e retirar chave antiga.

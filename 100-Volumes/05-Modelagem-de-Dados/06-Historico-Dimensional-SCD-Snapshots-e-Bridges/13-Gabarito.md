---
title: Gabarito
description: "Respostas dos exercícios de histórico dimensional."
tags: [modelagem-de-dados, gabarito, scd]
aliases: [Gabarito Histórico Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Nome corrigido pode ser Tipo 1; segmento real é Tipo 2; data de nascimento tende a Tipo 0, com correção governada.

## 2

Fechar versão anterior em `2026-07-10`, marcar não atual e inserir nova chave substituta válida desde essa data.

## 3

`d.chave=f.chave AND d.desde<=f.tempo AND (d.ate>f.tempo OR d.ate IS NULL)`.

## 4

Uma linha por produto-loja-data, com quantidade final e flags de disponibilidade; saldo não soma no tempo.

## 5

Uma linha por pedido com datas de criação, pagamento, envio e entrega e durações derivadas.

## 6

Bridge com três linhas e pesos, por exemplo 0,5; 0,3; 0,2, verificando soma igual a 1.

## 7

Adjacency é simples para escrita; closure materializa todos os caminhos e acelera ancestrais/descendentes ao custo de manutenção.

## 8

Identificar intervalo afetado, dividir versões, re-resolver fatos no período, reconciliar métricas, preservar lineage e publicar atomicamente.

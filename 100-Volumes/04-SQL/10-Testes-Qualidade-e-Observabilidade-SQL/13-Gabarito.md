---
title: Gabarito
description: "Respostas dos exercícios de qualidade SQL."
tags: [sql, gabarito, qualidade]
aliases: [Gabarito Qualidade SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Inclua conjunto vazio, um pedido, valores iguais, resto de divisão, zero permitido/proibido e `NULL` inválido.

## 2

Use chave primária, `valor_centavos > 0`, `NOT NULL` e `CHECK` sobre estados aceitos.

## 3

```sql
SELECT pedido_id FROM pedidos GROUP BY pedido_id HAVING COUNT(*) > 1;
```

## 4

```sql
SELECT f.cliente_id
FROM fato_pedidos f LEFT JOIN dim_cliente d USING (cliente_id)
WHERE d.cliente_id IS NULL;
```

## 5

Compare contagem, chaves distintas e soma por data/loja; investigue qualquer diferença conforme tolerância financeira definida.

## 6

Capture snapshot, execute o mesmo lote novamente e compare chaves, versões, contagem e somas; nenhum efeito deve mudar.

## 7

SLI: percentual de dias publicado até 06:00. SLO: por exemplo, 99,5% em 90 dias, com calendário e timezone explícitos.

## 8

Alerta segmentado identifica origem e período; runbook verifica chegada, schema, credencial e upstream, bloqueia publicação se necessário e orienta replay idempotente.

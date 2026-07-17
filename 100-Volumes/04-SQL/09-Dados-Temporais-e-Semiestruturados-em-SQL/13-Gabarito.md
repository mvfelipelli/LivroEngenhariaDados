---
title: Gabarito
description: "Respostas dos exercícios de SQL temporal e JSON."
tags: [sql, gabarito, temporal, json]
aliases: [Gabarito SQL Temporal e JSON]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Data identifica dia civil; instante identifica ponto global; duração mede quantidade; intervalo delimita conjunto entre fronteiras.

## 2

Na volta do horário de verão, a mesma hora local pode ocorrer duas vezes com offsets diferentes. É necessário timezone e regra de desambiguação.

## 3

```sql
WHERE valido_desde <= :instante
  AND (valido_ate > :instante OR valido_ate IS NULL)
```

## 4

`a < d AND c < b`. Fins abertos exigem infinito ou tratamento consistente de `NULL`.

## 5

Feche `registrado_ate` da versão conhecida e insira nova versão com intervalo de validade corrigido e novo `registrado_desde`.

## 6

```sql
CREATE TABLE eventos (
    evento_id INTEGER PRIMARY KEY,
    payload TEXT NOT NULL CHECK (json_valid(payload))
);
```

## 7

Expanda e agregue cada array separadamente no grão do documento; só então combine os resultados pela chave pai.

## 8

Introduza `schema_version=2` e `total_centavos`; leitores aceitam v1/v2; novos escritores emitem v2; faça backfill idempotente; reconcilie somas; retire suporte v1 após cobertura e retenção definidas.

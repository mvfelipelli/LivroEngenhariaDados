---
title: Laboratório — Consulta Temporal e Expansão de JSON
description: "Preço as of e itens JSON com SQLite."
tags: [sql, sqlite, laboratorio, temporal, json]
aliases: [Laboratório SQL Temporal e JSON]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Consulta Temporal e Expansão de JSON

## Objetivo

Selecionar o preço válido no instante de cada pedido, expandir itens de payloads JSON e calcular receita sem duplicar o grão.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- SQLite com extensão JSON integrada ao módulo `sqlite3`;
- nenhum serviço externo.

## Passos

1. Crie histórico de preços com intervalos semiabertos.
2. Crie eventos com `CHECK(json_valid(payload))`.
3. Insira pedidos antes e depois de uma mudança de preço.
4. Expanda `$.itens` com `json_each`.
5. Faça join temporal pelo SKU e instante do evento.
6. Agregue quantidades e receita.
7. Confirme que cada item encontra exatamente uma versão.

## Validação esperada

```text
pedidos=2
itens_expandidos=3
quantidade=4
receita_centavos=4000
precos_temporais=corretos
json=valido
resultado=ok
```

Consulte [[14-Solucao|Solução]].

---
title: Laboratório — Composição Relacional sem Fanout
description: "Relatório SQLite com pré-agregação, anti-join e CTE recursiva."
tags: [sql, sqlite, joins, laboratorio]
aliases: [Laboratório Joins e Subconsultas]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Composição Relacional sem Fanout

## Objetivo

Construir um relatório de pedidos sem fanout, detectar ausência de pagamento e percorrer uma hierarquia.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- `sqlite3` da biblioteca padrão;
- nenhuma dependência externa.

## Passos

1. Copie [[14-Solucao|a solução]] para `consultas_compostas.py`.
2. Execute:

```bash
python consultas_compostas.py
```

3. Remova a pré-agregação e observe a soma inflada.
4. Acrescente uma categoria e valide a recursão.

## Resultado esperado

```text
pedidos=3
grao=unico
total_itens=390.00
total_pago=340.00
sem_pagamento=1
hierarquia=3
composicao=ok
```

## Validação

O programa deve terminar com código zero e comprovar uma linha por pedido, totais independentes, anti-join e três níveis hierárquicos.

## Conclusão

O laboratório torna cardinalidade um contrato testável, não uma suposição visual.

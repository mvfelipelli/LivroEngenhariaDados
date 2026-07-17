---
title: Instantes, Datas, Durações, Timezones e Calendários
description: "Conceitos temporais e escolhas de armazenamento."
tags: [sql, timestamp, timezone, calendario]
aliases: [Fundamentos Temporais SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Instantes, Datas, Durações, Timezones e Calendários

Uma **data civil** identifica um dia em calendário; um **instante** identifica um ponto na linha do tempo; uma **duração** mede quantidade de tempo. `2026-07-17 09:00` não é instante completo sem timezone ou offset.

## Práticas

- armazene instantes em tipo consciente de timezone quando disponível;
- normalize comparações e transporte para UTC;
- preserve o timezone de negócio quando a regra depende da hora local;
- use `DATE` para conceitos civis como aniversário;
- não trate mês como quantidade fixa de segundos;
- mantenha tabela calendário para feriados e períodos fiscais.

```sql
-- PostgreSQL: instante convertido para a zona de negócio
SELECT criado_em AT TIME ZONE 'America/Sao_Paulo' AS horario_local
FROM pedidos;
```

Horário de verão produz horas inexistentes ou repetidas. Somar `24 hours` a um instante não equivale necessariamente a “mesmo horário amanhã”. Duração física e regra civil são operações diferentes.

> [!warning]
> Abreviações de timezone podem ser ambíguas. Prefira identificadores IANA, como `America/Sao_Paulo`.

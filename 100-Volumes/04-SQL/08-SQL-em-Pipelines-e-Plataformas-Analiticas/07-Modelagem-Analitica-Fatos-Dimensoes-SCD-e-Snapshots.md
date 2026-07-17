---
title: Modelagem Analítica, Fatos, Dimensões, SCD e Snapshots
description: "Persistência SQL orientada a métricas e histórico."
tags: [sql, dimensional, scd, snapshots]
aliases: [Modelagem Analítica SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Modelagem Analítica, Fatos, Dimensões, SCD e Snapshots

Uma tabela fato registra eventos ou medições em grão explícito. Dimensões fornecem contexto descritivo. Misturar grãos produz fanout e métricas incorretas.

## Mudança de dimensão

- **SCD Tipo 1:** sobrescreve o atributo; não preserva histórico;
- **SCD Tipo 2:** encerra a versão e cria outra com intervalo de validade;
- **snapshot periódico:** registra o estado em intervalos definidos.

```sql
CREATE TABLE dim_cliente (
    cliente_sk BIGINT PRIMARY KEY,
    cliente_id BIGINT NOT NULL,
    segmento TEXT NOT NULL,
    valido_desde TIMESTAMP NOT NULL,
    valido_ate TIMESTAMP,
    atual BOOLEAN NOT NULL,
    UNIQUE (cliente_id, valido_desde)
);
```

O fato deve localizar a versão dimensional válida no instante do evento, não necessariamente a versão atual. Intervalos sobrepostos quebram essa resolução e precisam ser testados.

Snapshots são adequados a saldos e estados, mas exigem calendário, regra para dias ausentes e distinção entre zero e desconhecido.

> [!tip]
> Documente aditividade: receita pode ser somada no tempo; saldo instantâneo normalmente não.

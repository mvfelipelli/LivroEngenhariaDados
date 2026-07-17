---
title: Testes de Transformação, Regressão e Propriedades
description: "Verificação de exemplos, invariantes e compatibilidade histórica."
tags: [sql, regressao, property-testing]
aliases: [Testes de Transformação SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Testes de Transformação, Regressão e Propriedades

Testes por exemplo comparam saída esperada. Testes de propriedade verificam invariantes para várias entradas: total não negativo, uma versão atual por chave, reexecução idempotente ou conservação de soma.

```sql
-- Uma dimensão SCD2 não pode ter mais de uma versão atual
SELECT cliente_id
FROM dim_cliente
WHERE atual
GROUP BY cliente_id
HAVING COUNT(*) <> 1;
```

Testes diferenciais executam implementação antiga e nova sobre a mesma entrada e explicam divergências. Golden datasets preservam casos representativos, mas precisam de revisão quando a regra muda legitimamente.

## Regressões críticas

- `NULL` convertido em zero;
- join que multiplica o grão;
- mudança de timezone na fronteira do dia;
- evento atrasado que regride versão;
- arredondamento inconsistente;
- filtro que remove categoria nova.

> [!tip]
> Prove equivalência semântica antes de comparar desempenho.

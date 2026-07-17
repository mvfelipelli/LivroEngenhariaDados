---
title: Warehouses Distribuídos, Particionamento, Custo e Portabilidade
description: "SQL consciente de arquitetura, movimentação de dados e cobrança."
tags: [sql, warehouse, particionamento, custo]
aliases: [SQL em Warehouses Distribuídos]
created: 2026-07-17
updated: 2026-07-17
---

# Warehouses Distribuídos, Particionamento, Custo e Portabilidade

Em plataformas distribuídas, desempenho depende de bytes lidos, pruning, shuffle, paralelismo, skew e tamanho de intermediários. O SQL declarativo continua igual em princípio, mas o custo físico muda.

## Redução de trabalho

- filtre partições com predicados SARGable;
- projete somente colunas necessárias;
- agregue antes de joins que movimentam grandes volumes;
- evite partições minúsculas em excesso;
- observe chaves enviesadas;
- materialize intermediários apenas com reutilização ou isolamento justificável.

```sql
SELECT loja_id, SUM(valor_centavos) AS receita
FROM analytics.fato_pedidos
WHERE data_pedido >= DATE '2026-07-01'
  AND data_pedido <  DATE '2026-08-01'
GROUP BY loja_id;
```

Aplicar função na coluna de partição pode impedir pruning em alguns mecanismos. Consulte o plano e os bytes estimados antes de executar backfills amplos.

## Portabilidade deliberada

Tipos, `MERGE`, funções de data, arrays, variantes, QUALIFY e DDL divergem. Isole extensões específicas, teste semântica de `NULL` e mantenha núcleo ANSI quando o benefício superar a otimização proprietária.

> [!warning]
> Uma consulta rápida pode ser cara financeiramente; custo por execução, frequência e concorrência fazem parte do SLO.

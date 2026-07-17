---
title: Views Materializadas, Atualização e Consistência
description: "Persistência de resultados derivados e seus compromissos operacionais."
tags: [sql, materialized-view, consistencia]
aliases: [Views Materializadas]
created: 2026-07-17
updated: 2026-07-17
---

# Views Materializadas, Atualização e Consistência

Uma view comum executa sua definição quando consultada. Uma view materializada persiste o resultado, trocando frescor por menor trabalho de leitura. Ela exige estratégia de atualização, observabilidade e propriedade operacional.

| Aspecto | View | View materializada |
|---|---|---|
| Dados persistidos | não | sim |
| Frescor | consulta a origem | depende do refresh |
| Custo de leitura | repete computação | lê resultado preparado |
| Operação | dependências | refresh, espaço e falhas |

```sql
CREATE MATERIALIZED VIEW analytics.mv_receita_mensal AS
SELECT loja_id, DATE_TRUNC('month', criado_em) AS mes, SUM(valor) AS receita
FROM vendas.pedidos
WHERE status = 'pago'
GROUP BY loja_id, DATE_TRUNC('month', criado_em);
```

Atualização total é simples, mas pode ser cara. Atualização incremental depende de chave, capacidade do SGBD ou pipeline próprio. Refresh concorrente pode reduzir indisponibilidade, porém possui pré-requisitos e custos.

## Contrato de frescor

Defina `freshness SLO`, horário do último refresh, atraso da origem, comportamento em falha e reconciliação. Um dashboard rápido com dados silenciosamente atrasados continua incorreto para sua finalidade.

> [!tip]
> Exponha a data de referência e o instante de atualização junto ao produto derivado.

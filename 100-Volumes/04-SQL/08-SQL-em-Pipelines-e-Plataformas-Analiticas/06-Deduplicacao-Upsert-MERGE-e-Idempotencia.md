---
title: Deduplicação, Upsert, MERGE e Idempotência
description: "Convergência do destino diante de repetição e múltiplas versões."
tags: [sql, deduplicacao, merge, idempotencia]
aliases: [Idempotência em Pipelines SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Deduplicação, Upsert, MERGE e Idempotência

Deduplicar exige uma regra de identidade e precedência. “Remover duplicatas” sem definir chave e versão pode descartar informação válida.

```sql
WITH ordenados AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY pedido_id
               ORDER BY atualizado_em DESC, ingerido_em DESC
           ) AS rn
    FROM staging.pedidos
)
SELECT * FROM ordenados WHERE rn = 1;
```

Depois da seleção canônica, upsert ou `MERGE` converge o destino:

```sql
INSERT INTO fato_pedidos (pedido_id, valor_centavos, atualizado_em)
SELECT pedido_id, valor_centavos, atualizado_em
FROM staging_pedidos_canonicos
ON CONFLICT (pedido_id) DO UPDATE
SET valor_centavos = EXCLUDED.valor_centavos,
    atualizado_em = EXCLUDED.atualizado_em
WHERE EXCLUDED.atualizado_em >= fato_pedidos.atualizado_em;
```

A condição evita que um evento antigo sobrescreva estado novo. `MERGE` varia entre SGBDs e pode ter particularidades concorrentes; chave única e transação continuam essenciais.

## Prova de idempotência

Execute o mesmo lote duas vezes e compare contagem, chaves, somas e versões. Resultado igual é evidência melhor que confiar apenas na intenção do código.

> [!warning]
> Idempotência do armazenamento não elimina efeitos externos duplicados, como notificações; coordene-os com padrões como [[09-Retries-Transacoes-Curtas-Outbox-e-Operacao|outbox]].

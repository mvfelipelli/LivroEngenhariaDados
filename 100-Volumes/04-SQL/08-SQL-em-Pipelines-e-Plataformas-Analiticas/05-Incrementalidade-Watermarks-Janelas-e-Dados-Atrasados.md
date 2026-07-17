---
title: Incrementalidade, Watermarks, Janelas e Dados Atrasados
description: "Leitura incremental robusta diante de atraso e reordenação."
tags: [sql, incremental, watermark, late-data]
aliases: [Carga Incremental SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Incrementalidade, Watermarks, Janelas e Dados Atrasados

Watermark registra até onde uma origem foi processada. Usar apenas `criado_em > ultimo_valor` perde linhas com empate, correção ou atraso. Um cursor composto e uma janela de sobreposição são mais seguros.

```sql
SELECT pedido_id, atualizado_em, valor_centavos
FROM raw.pedidos
WHERE atualizado_em >= :watermark_menos_sobreposicao
  AND atualizado_em < :limite_superior_estavel;
```

O limite superior deve ser capturado no início para evitar uma janela móvel. A sobreposição relê dados recentes; o destino idempotente absorve duplicidades. Para cursores sem sobreposição, use tupla ordenada:

```sql
WHERE (atualizado_em, pedido_id) > (:ultimo_instante, :ultimo_id)
ORDER BY atualizado_em, pedido_id;
```

## Tempos diferentes

- **tempo do evento:** quando o fato ocorreu;
- **tempo de ingestão:** quando foi recebido;
- **tempo de processamento:** quando o pipeline tratou;
- **tempo de atualização:** quando a origem modificou o registro.

Correções tardias exigem reprocessamento por chave ou partição. O watermark mede progresso, não garante completude absoluta.

> [!note]
> Defina explicitamente a tolerância a atraso e o procedimento para dados além dessa tolerância.

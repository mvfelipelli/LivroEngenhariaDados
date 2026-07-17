---
title: Reconciliação, Completude, Unicidade e Integridade
description: "Comparação de controles entre origem, transformação e destino."
tags: [sql, reconciliacao, integridade]
aliases: [Reconciliação SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Reconciliação, Completude, Unicidade e Integridade

Contagem total é um controle fraco: uma linha ausente e outra duplicada se anulam. Reconcilie por partição e dimensão relevante, combinando contagem, soma, mínimo, máximo e hash quando apropriado.

```sql
SELECT data_pedido,
       COUNT(*) AS linhas,
       COUNT(DISTINCT pedido_id) AS chaves,
       SUM(valor_centavos) AS total
FROM fato_pedidos
GROUP BY data_pedido;
```

## Dimensões clássicas

- completude: valores obrigatórios presentes;
- unicidade: chave sem duplicatas;
- validade: domínio e formato corretos;
- consistência: regras entre atributos preservadas;
- integridade: referências resolvidas;
- atualidade: atraso dentro do compromisso.

Threshold deve refletir semântica. Uma diferença de um centavo pode ser crítica em reconciliação financeira, enquanto pequeno atraso pode ser tolerável em telemetria.

> [!note]
> Registre denominador e população; “1% inválido” sem volume e período dificulta decisão.

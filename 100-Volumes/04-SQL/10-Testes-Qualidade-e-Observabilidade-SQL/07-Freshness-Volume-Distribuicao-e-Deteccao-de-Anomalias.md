---
title: Freshness, Volume, Distribuição e Detecção de Anomalias
description: "Sinais estatísticos para mudanças inesperadas nos dados."
tags: [sql, freshness, anomalias]
aliases: [Anomalias de Dados SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Freshness, Volume, Distribuição e Detecção de Anomalias

Freshness mede distância entre o dado mais recente esperado e o disponível. Volume e distribuição revelam quedas, picos, categorias novas e deslocamentos que constraints não capturam.

```sql
SELECT MAX(ingerido_em) AS dado_mais_recente,
       COUNT(*) AS linhas,
       AVG(valor_centavos) AS media,
       MIN(valor_centavos) AS minimo,
       MAX(valor_centavos) AS maximo
FROM pedidos
WHERE data_pedido = :data;
```

Limites fixos servem a regras conhecidas; baseline sazonal atende métricas que variam por hora ou dia da semana. Alertas estatísticos não provam defeito: promoções e feriados podem explicar desvios.

Segmentar por origem, região e versão acelera diagnóstico. Agregação global pode esconder que uma loja parou enquanto outra duplicou eventos.

> [!warning]
> Threshold excessivamente sensível gera fadiga; permissivo demais normaliza falhas. Calibre com histórico e impacto.

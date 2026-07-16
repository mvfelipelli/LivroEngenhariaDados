---
title: Dimensões, Métricas e Perfis
aliases: [Dimensões de Qualidade, Data Profiling]
tags: [qualidade, dimensoes, metricas, profiling]
created: 2026-07-16
updated: 2026-07-16
description: "Medição de qualidade e exploração estatística de dados."
---

# Dimensões, Métricas e Perfis

Dimensões organizam propriedades que podem ser medidas. Taxonomias variam; o importante é definir precisamente numerador, denominador, população, janela e tratamento de exceções.

| Dimensão | Pergunta | Exemplo de métrica |
|---|---|---|
| Completude | valores necessários existem? | campos preenchidos / campos esperados |
| Validade | valores respeitam domínio e formato? | registros válidos / avaliados |
| Unicidade | entidades ou eventos estão duplicados? | chaves únicas / registros |
| Consistência | representações concordam? | saldos conciliados / contas |
| Integridade | relacionamentos são válidos? | FKs existentes / referências |
| Atualidade | dados chegam no tempo necessário? | partições no prazo / esperadas |
| Acurácia | representam o mundo corretamente? | valores confirmados / amostra |

## Profiling

Data profiling calcula contagem, nulos, cardinalidade, mínimos, máximos, quantis, frequências e padrões. Ele ajuda a descobrir hipóteses e anomalias, mas não conhece sozinho a intenção do negócio.

```sql
SELECT
    COUNT(*) AS registros,
    COUNT(DISTINCT pedido_id) AS pedidos_unicos,
    SUM(CASE WHEN cliente_id IS NULL THEN 1 ELSE 0 END) AS clientes_nulos,
    MIN(valor) AS menor_valor,
    MAX(valor) AS maior_valor
FROM pedidos;
```

## Baselines e anomalias

Limites estáticos funcionam para invariantes. Baselines históricas ajudam em volume e distribuição sazonais. Anomalia estatística não é automaticamente erro: promoções e feriados alteram padrões legítimos.

> [!tip]
> Compare a métrica com o mesmo contexto temporal e de negócio; média global costuma esconder sazonalidade e segmentos problemáticos.

Métricas derivam de expectativas formalizadas em [[05-Contratos-Schemas-e-Regras-de-Negocio]].

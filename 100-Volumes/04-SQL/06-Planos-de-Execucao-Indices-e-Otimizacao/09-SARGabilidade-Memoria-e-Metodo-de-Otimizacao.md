---
title: SARGabilidade, Memória e Método de Otimização
description: "Antipadrões e processo experimental para reduzir trabalho SQL."
tags: [sql, sargabilidade, memoria, tuning]
aliases: [Método de Otimização SQL]
created: 2026-07-17
updated: 2026-07-17
---

# SARGabilidade, Memória e Método de Otimização

Um predicado é SARGable quando pode orientar um caminho de acesso eficiente. Aplicar uma função à coluna indexada frequentemente impede o uso direto do intervalo.

```sql
-- Evite transformar toda linha para comparar o dia
WHERE DATE(criado_em) = DATE '2026-07-17'

-- Expresse um intervalo sem transformar a coluna
WHERE criado_em >= TIMESTAMP '2026-07-17 00:00:00'
  AND criado_em <  TIMESTAMP '2026-07-18 00:00:00'
```

Conversões implícitas, `LIKE '%sufixo'`, disjunções amplas e tipos incompatíveis também podem degradar o acesso. Índices funcionais são uma alternativa quando a expressão faz parte do contrato e o SGBD os suporta.

## Memória não é solução universal

Sorts, hashes e agregações competem por memória por operador e por sessão. Aumentar o limite global sem estimar concorrência pode trocar spill previsível por exaustão de memória. Primeiro reduza linhas e largura; depois dimensione recursos.

## Método

1. defina SLO e consulta representativa;
2. registre resultado, plano, parâmetros, volume e métricas;
3. localize o operador que concentra trabalho;
4. formule uma hipótese causal;
5. altere predicado, índice, estatística ou modelo de forma isolada;
6. valide equivalência do resultado;
7. compare execução fria, aquecida e concorrente;
8. documente rollback e monitore regressões.

> [!tip]
> Reduzir a quantidade de linhas cedo costuma ser mais robusto que ajustar constantes do otimizador ou forçar planos.

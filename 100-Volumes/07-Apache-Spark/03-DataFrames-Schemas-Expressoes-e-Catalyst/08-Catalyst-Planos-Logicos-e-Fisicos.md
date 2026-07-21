---
title: Catalyst, Planos Lógicos e Físicos
description: "Análise, otimização e seleção da estratégia de execução."
tags: [apache-spark, catalyst, planos]
aliases: [Catalyst Optimizer]
created: 2026-07-20
updated: 2026-07-20
---

# Catalyst, Planos Lógicos e Físicos

Catalyst transforma árvores de expressões. O plano parsed representa a sintaxe; analyzed resolve tabelas, colunas e tipos; optimized aplica regras; physical escolhe operadores executáveis.

```python
resultado.explain(mode="extended")
resultado.explain(mode="cost")
```

Regras comuns incluem predicate pushdown, column pruning, constant folding e simplificação de expressões. Estatísticas permitem decisões baseadas em custo, como estratégia de join.

O plano é evidência, não detalhe acadêmico. Leia scans, filtros, `Exchange`, tipos de join e estimativas antes de alterar configurações.

---
title: Do SQL ao Plano Lógico e Físico
description: "Transformações que convertem uma consulta declarativa em operadores executáveis."
tags: [sql, otimizador, plano-logico, plano-fisico]
aliases: [Plano Lógico e Plano Físico]
created: 2026-07-17
updated: 2026-07-17
---

# Do SQL ao Plano Lógico e Físico

O banco analisa nomes e tipos, produz uma representação lógica e aplica equivalências: empurra filtros, elimina colunas desnecessárias e reorganiza joins quando a semântica permite. Depois, associa operações lógicas a implementações físicas e estima o custo das alternativas.

```mermaid
flowchart LR
    SQL["SELECT declarativo"] --> PARSE["Parse e binding"]
    PARSE --> LOG["Árvore lógica"]
    LOG --> REW["Reescritas equivalentes"]
    REW --> PHY["Alternativas físicas"]
    PHY --> EXE["Plano escolhido"]
```

Para a consulta:

```sql
SELECT c.segmento, SUM(p.valor)
FROM clientes AS c
JOIN pedidos AS p ON p.cliente_id = c.cliente_id
WHERE p.criado_em >= DATE '2026-07-01'
GROUP BY c.segmento;
```

o plano lógico contém seleção, join e agregação. O plano físico precisa decidir acesso a `pedidos`, método de join, ordem de entrada e implementação da agregação. O texto SQL não determina essas escolhas.

## Propriedades importantes

- **Equivalência:** reescritas devem conservar linhas, duplicidades e `NULL`.
- **Ordem de join:** com várias relações, o espaço de alternativas cresce rapidamente.
- **Parâmetros:** valores desconhecidos no planejamento podem induzir planos genéricos.
- **Plano adaptável:** dados e estatísticas mudam; um bom plano hoje não é contrato permanente.

> [!warning]
> A ordem visual das cláusulas SQL não corresponde à ordem física de execução.

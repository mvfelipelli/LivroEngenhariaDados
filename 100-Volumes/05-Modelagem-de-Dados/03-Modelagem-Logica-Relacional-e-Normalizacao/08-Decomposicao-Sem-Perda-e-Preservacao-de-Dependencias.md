---
title: Decomposição sem Perda e Preservação de Dependências
description: "Critérios para dividir relações com segurança."
tags: [decomposicao, lossless-join, dependencias]
aliases: [Decomposição Relacional]
created: 2026-07-17
updated: 2026-07-17
---

# Decomposição sem Perda e Preservação de Dependências

Uma decomposição é sem perda quando a junção das projeções válidas reconstrói exatamente a relação original, sem tuplas espúrias. Para decomposição binária de `R` em `R1` e `R2`, a interseção deve determinar funcionalmente uma das partes.

```text
R(pedido_id, cliente_id, cliente_nome)
R1(pedido_id, cliente_id)
R2(cliente_id, cliente_nome)
```

Como `cliente_id → cliente_nome`, a junção por `cliente_id` é sem perda sob a dependência.

Preservação significa verificar todas as dependências sem juntar relações. 3FN permite síntese que preserva dependências; BCNF pode exigir trade-off. Mesmo quando uma regra não cabe localmente, ela precisa de mecanismo explícito de validação.

> [!important]
> “Consigo fazer JOIN” não prova decomposição sem perda; qualquer tabela pode ser juntada, inclusive produzindo combinações inexistentes.

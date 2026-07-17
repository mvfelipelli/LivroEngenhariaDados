---
title: Dicionários, Conjuntos e Complexidade
description: "Mapeamento, pertinência, unicidade e custo."
tags: [python, dicionarios, conjuntos, complexidade]
aliases: [Dicionários Python]
created: 2026-07-17
updated: 2026-07-17
---

# Dicionários, Conjuntos e Complexidade

Dicionários associam chaves hashable a valores e preservam ordem de inserção. Conjuntos mantêm elementos únicos e oferecem união, interseção e diferença.

```python
totais: dict[str, int] = {}
for loja, valor in [("SP", 10), ("RJ", 20), ("SP", 5)]:
    totais[loja] = totais.get(loja, 0) + valor

assert totais == {"SP": 15, "RJ": 20}
```

Busca média por chave em dict ou set é O(1); busca em lista é O(n). Ordenar n itens custa tipicamente O(n log n).

Chaves precisam ter hash estável durante sua permanência no mapeamento. Listas não podem ser chaves, mas tuplas compostas apenas por valores hashable podem.

> [!warning]
> A ordem observada de um set não constitui contrato. Ordene antes de serializar resultados que precisam ser determinísticos.

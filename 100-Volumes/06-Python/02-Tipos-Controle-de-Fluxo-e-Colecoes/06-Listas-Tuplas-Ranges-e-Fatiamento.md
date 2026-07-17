---
title: Listas, Tuplas, Ranges e Fatiamento
description: "Sequências ordenadas e operações essenciais."
tags: [python, listas, tuplas, sequencias]
aliases: [Sequências Python]
created: 2026-07-17
updated: 2026-07-17
---

# Listas, Tuplas, Ranges e Fatiamento

Listas são sequências mutáveis; tuplas representam registros posicionais ou coleções imutáveis. Ambas preservam ordem e duplicatas.

```python
pedidos = ["P3", "P1", "P2"]
primeiro, *meio, ultimo = pedidos
assert primeiro == "P3" and ultimo == "P2"
```

Índices e slices usam intervalo semiaberto: o início é incluído e o fim é excluído. Slices de listas criam nova lista rasa.

```python
janela = pedidos[0:2]
invertidos = pedidos[::-1]
```

`range` representa progressões inteiras sem materializar todos os números. Use `enumerate` para índice e valor. Inserir ou remover no fim de uma lista costuma ser amortizadamente O(1); operar no início desloca elementos e custa O(n). Para filas, use `collections.deque`.

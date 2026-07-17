---
title: Ordenação, Cópias e Padrões de Transformação
description: "Resultados determinísticos e transformações previsíveis."
tags: [python, ordenacao, copias, transformacao]
aliases: [Ordenação Python]
created: 2026-07-17
updated: 2026-07-17
---

# Ordenação, Cópias e Padrões de Transformação

`sorted()` retorna uma lista nova; `list.sort()` altera a lista e retorna `None`. A ordenação do Python é estável.

```python
ranking = sorted(
    totais.items(),
    key=lambda item: (-item[1], item[0]),
)
```

A chave ordena total decrescente e usa o identificador como desempate crescente. Desempates explícitos tornam saídas e testes determinísticos.

Transformações frequentes incluem filtrar, projetar, indexar, agrupar e reduzir. Para agrupamentos simples, um dict acumulador evita varrer dados repetidamente.

Não altere o tamanho de uma coleção enquanto itera sobre ela. Itere sobre uma cópia das chaves ou construa outra coleção. Prefira transformação sem efeitos quando a etapa alimenta múltiplos consumidores; se mutar por performance, documente ownership e invariantes.

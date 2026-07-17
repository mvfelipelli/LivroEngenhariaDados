---
title: Algoritmos de Join — Nested Loop, Hash e Merge
description: "Características e custos dos principais algoritmos físicos de junção."
tags: [sql, join, nested-loop, hash-join, merge-join]
aliases: [Algoritmos de Join]
created: 2026-07-17
updated: 2026-07-17
---

# Algoritmos de Join — Nested Loop, Hash e Merge

O join lógico não determina sua implementação. O otimizador escolhe conforme cardinalidade, predicados, ordenação, índices e memória.

| Algoritmo | Funcionamento | Bom cenário | Risco |
|---|---|---|---|
| Nested Loop | para cada linha externa, busca a interna | entrada externa pequena e busca indexada | repetir scan grande |
| Hash Join | cria hash de uma entrada e consulta com a outra | igualdade e conjuntos médios/grandes | spill se hash exceder memória |
| Merge Join | avança entradas ordenadas | igualdade/faixa com ordem disponível | sorts prévios caros |

```mermaid
flowchart LR
    A["Entrada menor"] --> H["Construir hash"]
    B["Entrada maior"] --> P["Probe"]
    H --> P
    P --> J["Linhas combinadas"]
```

No nested loop, `loops` revela quantas vezes o filho interno foi executado. Dez microssegundos multiplicados por milhões de loops tornam-se relevantes. No hash join, tamanho do hash, número de lotes e uso de disco indicam pressão de memória. No merge join, verifique se a ordenação já vem de índices ou foi produzida apenas para o join.

> [!example]
> Buscar 20 pedidos recentes e, para cada um, localizar um cliente por chave primária favorece nested loop. Cruzar duas tabelas extensas por igualdade frequentemente favorece hash join.

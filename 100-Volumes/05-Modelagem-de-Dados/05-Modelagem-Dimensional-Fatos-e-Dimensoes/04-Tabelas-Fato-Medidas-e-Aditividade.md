---
title: Tabelas Fato, Medidas e Aditividade
description: "Eventos mensuráveis e regras de agregação."
tags: [fatos, medidas, aditividade]
aliases: [Tabelas Fato]
created: 2026-07-17
updated: 2026-07-17
---

# Tabelas Fato, Medidas e Aditividade

Tabela fato registra eventos ou estados no grão declarado. Contém chaves dimensionais, medidas e, às vezes, identificadores degenerados.

## Tipos

- fato transacional: uma linha por evento;
- snapshot periódico: estado em intervalos regulares;
- snapshot acumulativo: marcos de um processo com começo e fim;
- factless fact: ocorrência ou cobertura sem medida numérica.

Medida aditiva soma em todas as dimensões, como quantidade. Semiaditiva não soma em algum eixo, como saldo no tempo. Não aditiva, como percentual, deve ser recalculada a partir de componentes.

```sql
taxa_conversao = pedidos / sessoes
```

Armazene numerador e denominador, não apenas a taxa. Defina moeda, unidade, sinal e comportamento em cancelamento.

> [!tip]
> Contagem de linhas só é métrica válida quando o grão está correto e não há duplicidades.

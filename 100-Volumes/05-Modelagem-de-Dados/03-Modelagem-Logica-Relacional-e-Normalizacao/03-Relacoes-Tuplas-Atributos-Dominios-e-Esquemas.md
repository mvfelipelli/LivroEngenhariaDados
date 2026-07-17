---
title: Relações, Tuplas, Atributos, Domínios e Esquemas
description: "Elementos formais do modelo relacional lógico."
tags: [relacoes, tuplas, dominios]
aliases: [Elementos do Modelo Relacional]
created: 2026-07-17
updated: 2026-07-17
---

# Relações, Tuplas, Atributos, Domínios e Esquemas

Relação é conjunto de tuplas sobre atributos definidos. Esquema descreve nome, atributos e restrições; estado é o conjunto de tuplas em um instante.

```text
PEDIDO(pedido_id, cliente_id, criado_em, status)
ITEM_PEDIDO(pedido_id, numero_item, produto_id, quantidade, preco)
```

Domínio restringe valores possíveis e carrega semântica: moeda e unidade não devem ser inferidas de `NUMERIC`. A ordem das tuplas não faz parte da relação; duplicatas não pertencem ao modelo matemático, embora SQL possa produzi-las.

Cada atributo deve conter valor no grão da relação. Grupos repetidos e listas concatenadas dificultam domínio, referências e consulta.

> [!note]
> `NULL` representa marcador, não valor comum. Sua semântica deve ser limitada e documentada.

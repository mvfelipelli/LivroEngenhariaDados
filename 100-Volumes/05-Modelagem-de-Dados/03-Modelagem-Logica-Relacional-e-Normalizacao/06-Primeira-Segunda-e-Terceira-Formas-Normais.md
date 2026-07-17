---
title: Primeira, Segunda e Terceira Formas Normais
description: "Eliminação progressiva de grupos e dependências inadequadas."
tags: [1fn, 2fn, 3fn, normalizacao]
aliases: [Formas Normais 1FN 2FN 3FN]
created: 2026-07-17
updated: 2026-07-17
---

# Primeira, Segunda e Terceira Formas Normais

## Primeira Forma Normal

Relações possuem atributos definidos em domínios e uma tupla por ocorrência do grão. Listas em `produto_1`, `produto_2` ou texto separado por vírgula violam o desenho relacional útil.

## Segunda Forma Normal

Em 1FN, nenhum atributo não primo depende de parte própria de uma chave candidata composta. Em `ITEM(pedido_id, numero_item, cliente_nome)`, `cliente_nome` depende do pedido, não do item inteiro.

## Terceira Forma Normal

Para toda dependência não trivial `X → A`, `X` é superchave ou `A` é atributo primo. Isso remove dependência transitiva de atributos não chave.

```mermaid
flowchart LR
    U["PEDIDO com dados do cliente"] --> P["PEDIDO"]
    U --> C["CLIENTE"]
    U --> I["ITEM_PEDIDO"]
```

> [!note]
> 2FN só acrescenta restrição quando existe chave candidata composta.

---
title: Laboratório — Mini Data Vault Idempotente
description: "Carga de Hubs, Link e Satellites com hashes determinísticos."
tags: [modelagem-de-dados, sqlite, laboratorio, data-vault]
aliases: [Laboratório Data Vault]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Mini Data Vault Idempotente

## Objetivo

Carregar cliente, pedido, relação e contexto, repetir o lote e provar que nenhuma linha é duplicada.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulos `sqlite3` e `hashlib` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie Hub Cliente e Hub Pedido.
2. Crie Link Pedido-Cliente.
3. Crie Satellites de cliente e pedido.
4. Gere SHA-256 com canonicalização definida.
5. Carregue duas ocorrências.
6. Repita exatamente o mesmo lote.
7. Valide contagens, record source e idempotência.

## Validação esperada

```text
hub_cliente=2
hub_pedido=2
link_pedido_cliente=2
sat_cliente=2
sat_pedido=2
record_source=preservado
reexecucao=idempotente
data_vault=ok
```

Consulte [[14-Solucao|Solução]].

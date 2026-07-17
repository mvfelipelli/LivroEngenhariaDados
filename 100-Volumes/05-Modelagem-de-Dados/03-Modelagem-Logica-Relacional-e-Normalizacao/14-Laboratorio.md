---
title: Laboratório — Normalização de Vendas
description: "Decomposição e validação de um modelo legado no SQLite."
tags: [modelagem-de-dados, sqlite, laboratorio, normalizacao]
aliases: [Laboratório Normalização]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Normalização de Vendas

## Objetivo

Demonstrar anomalia de atualização no modelo legado, decompor em quatro relações e provar reconstrução sem perda para a amostra.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie `venda_legada` com uma linha por item.
2. Repita cliente e produto em várias linhas.
3. Atualize apenas uma ocorrência e detecte inconsistência.
4. Crie cliente, produto, pedido e item.
5. Migre dados canônicos.
6. Reconstrua a visão pela junção.
7. Compare chaves, contagem e total.

## Validação esperada

```text
anomalia_legada=detectada
clientes=2
produtos=2
pedidos=2
itens=3
total_centavos=5500
reconstrucao=sem_perda
normalizacao=ok
```

Consulte [[14-Solucao|Solução]].

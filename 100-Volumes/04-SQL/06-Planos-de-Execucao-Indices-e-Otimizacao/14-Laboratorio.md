---
title: Laboratório — Plano e Índice no SQLite
description: "Comparação reproduzível de planos antes e depois da indexação."
tags: [sql, sqlite, laboratorio, explain]
aliases: [Laboratório de Plano SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Plano e Índice no SQLite

## Objetivo

Observar uma busca com scan e ordenação temporária, criar um índice alinhado ao filtro e à ordem e comprovar a mudança para busca indexada sem alterar o resultado.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

O banco será criado em memória, com 10.000 pedidos determinísticos.

## Passos

1. Crie `pedidos` com chave, cliente, ordem temporal e valor.
2. Insira 10.000 linhas distribuídas entre 100 clientes.
3. Capture `EXPLAIN QUERY PLAN` para os cinco pedidos recentes do cliente 42.
4. Confirme `SCAN` e uso de B-tree temporária para `ORDER BY`.
5. Crie índice `(cliente_id, criado_em DESC, valor)`.
6. Capture o novo plano e confirme `SEARCH` sem ordenação temporária.
7. Compare os resultados antes e depois.

## Validação esperada

```text
linhas=10000
plano_antes=scan
ordenacao_antes=temporaria
plano_depois=search
ordenacao_depois=indice
resultado=equivalente
otimizacao=ok
```

> [!note]
> O laboratório valida a forma do plano, não promete uma razão de tempo. Em um banco em memória e pequeno, medir apenas milissegundos seria instável.

Consulte a implementação em [[14-Solucao|Solução]].

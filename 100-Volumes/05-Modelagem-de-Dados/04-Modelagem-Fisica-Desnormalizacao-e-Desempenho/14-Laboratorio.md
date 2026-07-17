---
title: Laboratório — Índice e Projeção Desnormalizada
description: "Validação de acesso físico e resumo reconciliável no SQLite."
tags: [modelagem-de-dados, sqlite, laboratorio, desempenho]
aliases: [Laboratório Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Índice e Projeção Desnormalizada

## Objetivo

Comparar plano antes e depois de um índice composto e construir resumo por cliente reconciliado com a fonte normalizada.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- módulo `sqlite3` da biblioteca padrão;
- nenhum serviço externo.

## Passos

1. Crie 10.000 pedidos distribuídos entre 100 clientes.
2. Consulte os cinco pedidos recentes do cliente 42.
3. Capture scan e ordenação temporária.
4. Crie índice `(cliente_id, criado_em DESC)`.
5. Confirme busca indexada sem sort temporário.
6. Materialize resumo por cliente.
7. Reconcilie contagem e valor com a fonte.

## Validação esperada

```text
linhas=10000
plano_antes=scan
plano_depois=search
ordenacao=indice
resumos=100
reconciliacao=ok
modelo_fisico=ok
```

Consulte [[14-Solucao|Solução]].

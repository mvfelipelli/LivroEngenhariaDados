---
title: Exercícios — Fundamentos de SQL
description: "Atividades progressivas sobre modelo relacional e consultas."
tags: [sql, exercicios, relacional]
aliases: [Exercícios Fundamentos SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Exercícios

## Revisão

1. Diferencie schema, relação, tupla, atributo e domínio.
2. Explique DDL, DQL, DML, DCL e TCL.

## Interpretação

3. Por que uma consulta sem `ORDER BY` não possui ordem garantida?
4. Avalie `WHERE email = NULL` e corrija a expressão.
5. Compare `COUNT(*)` com `COUNT(pedido_id)` após um `LEFT JOIN`.

## Aplicação

6. Crie uma tabela `produtos` com chave, nome obrigatório e preço não negativo.
7. Consulte clientes ativos de duas cidades, ordenando por nome e identificador.
8. Classifique pedidos em três faixas de valor com `CASE`.

## Desafio

9. Produza um relatório com todos os clientes, quantidade de pedidos e valor total, incluindo quem nunca comprou.
10. Identifique três pontos de possível incompatibilidade ao portar a consulta entre SQLite e PostgreSQL.

Consulte [[13-Gabarito|o gabarito]] depois de justificar cada decisão.

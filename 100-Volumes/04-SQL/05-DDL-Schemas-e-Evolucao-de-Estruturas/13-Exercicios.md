---
title: Exercícios — DDL e Evolução de Estruturas
description: "Atividades progressivas sobre contratos e migrações."
tags: [sql, exercicios, ddl, migrations]
aliases: [Exercícios Migrações SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Exercícios

## Revisão

1. Diferencie schema, tabela, view, índice e constraint.
2. Explique tipos, defaults e colunas geradas.

## Interpretação

3. Por que `CHECK (preco > 0)` ainda aceita `NULL`?
4. Analise os riscos de `DROP COLUMN ... CASCADE`.
5. Classifique uma mudança como catálogo, scan ou reescrita.

## Aplicação

6. Modele constraints para itens de pedido.
7. Planeje adicionar coluna obrigatória a tabela populada.
8. Crie backfill retomável por chave.

## Desafio

9. Planeje rename de coluna com zero downtime.
10. Defina pipeline de testes e métricas de uma migração grande.

Compare com [[13-Gabarito|o gabarito]] antes do laboratório.

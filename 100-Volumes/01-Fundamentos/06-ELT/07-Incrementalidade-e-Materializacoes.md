---
title: Incrementalidade e Materializações
aliases: [ELT Incremental Models]
tags: [engenharia-de-dados, fundamentos, elt, incremental, materializacao]
type: chapter
order: 07
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Views, tabelas, incrementais, snapshots e reconstrução em ELT."
---

# 07 — Incrementalidade e Materializações

## Escolhas

| Materialização | Vantagem | Custo |
| --- | --- | --- |
| View | sempre derivada | compute em leitura |
| Tabela | leitura rápida | atualização e armazenamento |
| Incremental | processa mudanças | estado e lógica de merge |
| Snapshot | preserva versões | volume e vigência |

## Modelo incremental

Precisa de chave única, filtro de mudanças, tratamento de update/delete, precedência e estratégia de full refresh.

Um filtro por `updated_at` sem sobreposição pode perder atrasados. Reprocessar janela recente e fazer merge idempotente reduz o risco.

## Full refresh

É mecanismo de recuperação e teste. Deve publicar atomicamente e caber em limites de custo. Resultados incremental e completo precisam ser equivalentes.

## Late-arriving data

Fatos podem chegar antes da dimensão ou após o período esperado. Use membro desconhecido controlado, retry ou atualização posterior, mantendo métricas de pendência.

## Próximo Capítulo

➡️ [[08-Testes-Documentacao-e-Linhagem|08 — Testes, Documentação e Linhagem]]

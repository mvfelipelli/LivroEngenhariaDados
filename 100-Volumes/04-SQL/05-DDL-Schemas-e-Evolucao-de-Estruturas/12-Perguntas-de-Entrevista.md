---
title: Perguntas de Entrevista — DDL e Migrações
description: "Questões práticas com respostas fundamentadas."
tags: [sql, entrevista, ddl, migrations]
aliases: [Entrevista Migrações SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. DDL e DML diferem como?

DDL altera estruturas; DML altera os dados contidos nelas.

## 2. Por que nomear constraints?

Melhora diagnóstico, automação e alterações futuras.

## 3. CHECK substitui NOT NULL?

Não; expressão desconhecida pode satisfazer `CHECK`. Use ambos quando necessário.

## 4. Qual o risco de DROP CASCADE?

Remover uma árvore de dependências maior que a pretendida.

## 5. Todo ALTER TABLE é rápido?

Não. Pode validar, reescrever dados ou aguardar lock exclusivo.

## 6. O que é expand-contract?

Adicionar forma compatível, migrar dados e consumidores e só depois remover legado.

## 7. Como fazer backfill seguro?

Em lotes por chave, idempotente, retomável, limitado e observado.

## 8. Renomear coluna é compatível?

Não para consumidores antigos; trate como introdução da nova e remoção posterior da antiga.

## 9. Rollback de código sempre funciona?

Não se schema ou dados deixaram de ser entendidos pela versão antiga.

## 10. Por que não editar migração aplicada?

Ambientes passariam a associar o mesmo identificador a conteúdos diferentes.

## 11. O que testar numa migração?

Banco vazio, upgrade, dados, constraints, dependências, volume e aplicações coexistentes.

## 12. Quais métricas acompanhar?

Lock wait, duração, linhas, erros, lag, espaço e divergências de backfill.

---
title: Perguntas de Entrevista — Bancos e APIs Python
description: "Questões sobre transações e HTTP resiliente."
tags: [python, entrevista, integracao]
aliases: [Entrevista Bancos APIs Python]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Por que parametrizar SQL?

Para separar dados do comando, evitando injeção e delegando conversão ao driver.

## 2. Contexto de conexão sempre fecha a conexão?

Depende do driver; no sqlite3 ele controla commit/rollback, mas não fecha automaticamente.

## 3. Upsert é sempre idempotente?

Não. A chave, valores e política de atualização precisam tornar repetições equivalentes.

## 4. Quando repetir uma transação?

Somente para falhas classificadas como transitórias, com operação reexecutável e tentativas limitadas.

## 5. GET é idempotente?

Pela semântica HTTP, é safe e idempotente, embora servidores defeituosos possam violar o contrato.

## 6. Timeout único é suficiente?

Nem sempre. Conexão, leitura, pool e deadline total podem exigir limites distintos.

## 7. Offset e cursor diferem como?

Offset referencia posição mutável; cursor opaco pode preservar continuidade e snapshot definidos pelo servidor.

## 8. Quando salvar o cursor?

Na mesma transação que confirma os itens da página, após validação completa.

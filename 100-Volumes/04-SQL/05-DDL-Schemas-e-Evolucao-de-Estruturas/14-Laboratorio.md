---
title: Laboratório — Migração Expand-Contract em SQLite
description: "Evolução transacional com backfill e reconstrução de tabela."
tags: [sql, sqlite, migration, laboratorio]
aliases: [Laboratório Evolução de Schema]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Migração Expand-Contract em SQLite

## Objetivo

Migrar `valor` para `valor_centavos`, validar backfill e reconstruir a tabela com contrato final.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- `sqlite3` da biblioteca padrão;
- nenhuma dependência externa.

## Passos

1. Copie [[14-Solucao|a solução]] para `migracao.py`.
2. Execute `python migracao.py`.
3. Inspecione as três fases: expand, backfill e contract.
4. Force divergência e confirme rollback.

## Resultado esperado

```text
versao=3
linhas=3
backfill=ok
constraints=ok
coluna_legada=removida
total_centavos=35990
migracao=ok
```

## Validação

O schema final deve conter somente a nova representação, preservar linhas e rejeitar valor negativo.

## Conclusão

O exercício demonstra que evolução de estrutura combina dados, catálogo, compatibilidade e prova pós-migração.

---
title: Laboratório — Transferência Atômica e Evento Idempotente
description: "Rollback, savepoint, constraint e reprocessamento em SQLite."
tags: [sql, sqlite, transacoes, laboratorio]
aliases: [Laboratório Transações SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Transferência Atômica e Evento Idempotente

## Objetivo

Validar transferência atômica, rollback por constraint e processamento idempotente de evento.

## Pré-requisitos e ambiente

- Python 3.10 ou superior;
- `sqlite3` da biblioteca padrão;
- nenhuma dependência externa.

## Passos

1. Copie [[14-Solucao|a solução]] para `transacoes.py`.
2. Execute:

```bash
python transacoes.py
```

3. Altere o débito para valor superior ao saldo e observe o rollback.
4. Processe o mesmo `evento_id` novamente e confirme ausência de duplicação.

## Resultado esperado

```text
saldo_total=1500.00
transferencia=ok
rollback=ok
eventos=1
idempotencia=ok
outbox=1
transacao=ok
```

## Validação

O total deve permanecer constante, a transferência inválida não pode mudar saldos e evento repetido deve gerar uma única outbox.

## Conclusão

O laboratório demonstra atomicidade e idempotência como invariantes observáveis.

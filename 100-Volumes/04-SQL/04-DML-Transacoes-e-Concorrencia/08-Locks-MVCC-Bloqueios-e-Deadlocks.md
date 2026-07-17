---
title: Locks, MVCC, Bloqueios e Deadlocks
description: "Mecanismos de coordenação e contenção operacional."
tags: [sql, locks, mvcc, deadlock]
aliases: [Locks e MVCC]
created: 2026-07-17
updated: 2026-07-17
---

# Locks, MVCC, Bloqueios e Deadlocks

MVCC mantém versões para que leitores usem snapshots sem bloquear todas as escritas. Locks continuam necessários para proteger linhas, estruturas e operações incompatíveis.

```sql
SELECT saldo
FROM contas
WHERE conta_id = 1
FOR UPDATE;
```

Esse padrão bloqueia modificações conflitantes da linha até o fim da transação em mecanismos que o suportam.

```mermaid
flowchart LR
    T1["T1 segura A"] --> B["espera B"]
    T2["T2 segura B"] --> A["espera A"]
    B --> T2
    A --> T1
```

O ciclo é deadlock. Bancos detectam e abortam uma vítima; a aplicação deve repetir a transação inteira. Adquirir recursos sempre na mesma ordem reduz probabilidade.

Bloqueio longo não é deadlock. Monitore duração, sessão bloqueadora, lock aguardado e consulta. Timeouts evitam espera infinita, mas criam falhas que precisam de tratamento.

SQLite permite leitores simultâneos, mas apenas uma transação de escrita por vez. `BEGIN IMMEDIATE` tenta adquirir capacidade de escrita no início.

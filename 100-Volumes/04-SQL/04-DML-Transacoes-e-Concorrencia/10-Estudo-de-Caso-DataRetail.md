---
title: Estudo de Caso — Pedidos Transacionais da DataRetail
description: "Reserva, pagamento e evento com consistência e idempotência."
tags: [dataretail, sql, transacoes, estudo-de-caso]
aliases: [Caso DataRetail Transações]
created: 2026-07-17
updated: 2026-07-17
---

# Estudo de Caso — DataRetail S.A.

A DataRetail S.A. recebia callbacks duplicados de pagamento e, em falhas raras, marcava pedido como pago sem registrar o evento de integração.

O time introduziu chave única `evento_id`, versão do pedido e outbox. A transação valida o estado, atualiza pedido, registra pagamento e insere evento.

```mermaid
sequenceDiagram
    participant API
    participant DB
    participant PUB as Publicador
    API->>DB: BEGIN + evento_id
    DB->>DB: upsert pagamento
    DB->>DB: atualiza pedido
    DB->>DB: insere outbox
    API->>DB: COMMIT
    PUB->>DB: lê outbox
```

Callbacks repetidos convergem para o mesmo estado. Conflitos transitórios repetem a transação inteira. Estoque é bloqueado por produto em ordem crescente para reduzir deadlocks.

Constraints impedem saldo negativo e transição inválida. Métricas acompanham duplicatas, retries, espera de lock e idade da outbox.

O resultado foi consistência entre estado interno e intenção de publicação sem depender de transação distribuída com o broker.

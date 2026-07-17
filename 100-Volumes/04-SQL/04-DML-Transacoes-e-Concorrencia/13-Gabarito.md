---
title: Gabarito — DML, Transações e Concorrência
description: "Respostas orientadoras dos exercícios."
tags: [sql, gabarito, transacoes]
aliases: [Gabarito Transações SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

1. Tudo ou nada; invariantes; visibilidade concorrente; persistência após commit.
2. Confirmar, desfazer tudo e criar ponto de recuperação parcial.
3. Duas sessões podem observar ausência e tentar inserir; constraint única arbitra atomicamente.
4. Leitura não confirmada; mudança da mesma linha; mudança do conjunto que satisfaz predicado.
5. T1 segura A e espera B, enquanto T2 segura B e espera A.
6. Constraint única e atualização condicionada a `versao_existente < versao_recebida`.
7. Débito e crédito na mesma transação, constraint/validação, locks em ordem e rollback em falha.
8. Repetir a transação completa com limite, backoff, jitter e operação idempotente.
9. `evento_id` único, upsert e transição de estado protegida na mesma transação.
10. Inserir outbox com dado de negócio; publicar com deduplicação e monitorar idade, erros e retries.

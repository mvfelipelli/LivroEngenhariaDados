---
title: Perguntas de Entrevista — DML e Transações
description: "Questões práticas com respostas fundamentadas."
tags: [sql, entrevista, transacoes]
aliases: [Entrevista Transações SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. O que significa ACID?

Atomicidade, consistência, isolamento e durabilidade; propriedades complementares de uma transação.

## 2. Por que consultar antes de inserir não garante unicidade?

Outra transação pode inserir entre as sentenças. Use constraint única e operação atômica.

## 3. O que é idempotência?

Repetir a mesma intenção produz o mesmo estado observável.

## 4. COMMIT e ROLLBACK fazem o quê?

Confirmam ou desfazem a unidade transacional.

## 5. Para que serve SAVEPOINT?

Permite reverter parte da transação sem abortar tudo.

## 6. READ COMMITTED oferece snapshot de quê?

Frequentemente de cada sentença; detalhes dependem do banco.

## 7. O que é write skew?

Transações leem um invariante conjunto e atualizam linhas distintas, tornando o resultado inválido.

## 8. MVCC elimina locks?

Não. Reduz conflitos leitor-escritor, mas escritas e estruturas ainda exigem coordenação.

## 9. Como prevenir deadlocks?

Transações curtas e aquisição de recursos em ordem consistente; ainda trate abortos com retry.

## 10. Quando repetir uma transação?

Em falhas transitórias classificadas, com limite, backoff, jitter e idempotência.

## 11. O que resolve o outbox?

Atomicidade entre mudança no banco e registro da intenção de publicar um evento.

## 12. Por que transações longas são perigosas?

Retêm locks e versões, aumentam contenção, conflitos e custo de recuperação.

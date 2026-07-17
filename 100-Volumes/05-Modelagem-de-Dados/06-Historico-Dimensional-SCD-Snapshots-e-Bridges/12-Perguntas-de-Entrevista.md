---
title: Perguntas de Entrevista
description: "Perguntas sobre SCD, snapshots e bridges."
tags: [modelagem-de-dados, entrevista, scd]
aliases: [Entrevista Histórico Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. SCD1 e SCD2 diferem como?

Tipo 1 sobrescreve; Tipo 2 encerra a versão e insere outra.

## 2. SCD2 exige qual chave?

Chave substituta por versão, além da chave natural que conecta versões.

## 3. Como resolver fato para SCD2?

Pela chave natural e pelo intervalo que contém o tempo do evento.

## 4. Snapshot periódico e acumulativo diferem como?

Periódico captura estado por período; acumulativo atualiza marcos de um processo.

## 5. Quando usar bridge?

Para relação multivalorada ou hierarquia que não cabe em uma chave simples.

## 6. Qual risco de bridge?

Multiplicar medidas ao expandir membros.

## 7. Para que serve peso de alocação?

Distribuir medida sem duplicá-la; pesos devem somar 1 por grupo.

## 8. O que é late arriving fact?

Fato recebido depois, que precisa localizar a versão dimensional do tempo em que ocorreu.

## 9. Como detectar overlap SCD2?

Compare intervalos consecutivos ou faça self-join pelas condições de sobreposição.

## 10. Por que guardar lineage de correção?

Para explicar quem mudou o histórico, por qual origem, motivo e versão.

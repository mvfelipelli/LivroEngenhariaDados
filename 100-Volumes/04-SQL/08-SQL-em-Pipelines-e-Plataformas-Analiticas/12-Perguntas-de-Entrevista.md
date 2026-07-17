---
title: Perguntas de Entrevista
description: "Perguntas e respostas sobre SQL em pipelines analíticos."
tags: [sql, entrevista, pipelines]
aliases: [Entrevista SQL em Pipelines]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. O que transforma um SQL em unidade de pipeline?

Entradas e saídas explícitas, grão, chave, estratégia de escrita, parâmetros, invariantes, versão e comportamento recuperável.

## 2. Para que serve staging?

Para isolar dados recebidos, validar e preparar publicação sem expor estado intermediário.

## 3. Watermark garante que nenhum dado será perdido?

Não. Atraso, empate, correções e falhas da origem exigem cursor estável, sobreposição ou reconciliação.

## 4. Como tratar dados atrasados?

Defina tolerância, releia janela sobreposta, escreva idempotentemente e mantenha caminho de backfill para atrasos maiores.

## 5. Deduplicação e idempotência são iguais?

Não. Deduplicação escolhe uma representação canônica; idempotência garante que repetir a operação não altera o estado final.

## 6. Por que condicionar um upsert à versão?

Para impedir que um evento antigo sobrescreva estado mais recente.

## 7. O que diferencia SCD Tipo 1 e Tipo 2?

Tipo 1 sobrescreve; Tipo 2 cria versões com intervalos de validade e preserva histórico.

## 8. Como testar incrementalidade?

Compare resultado incremental ao full refresh para um conjunto controlado e repita lotes para provar idempotência.

## 9. O que observar em warehouse distribuído?

Bytes lidos, pruning, shuffle, skew, spill, paralelismo, intermediários e custo financeiro.

## 10. Qual deve ser a unidade de retry?

Uma transação ou etapa idempotente cujo estado parcial seja detectável e recuperável.

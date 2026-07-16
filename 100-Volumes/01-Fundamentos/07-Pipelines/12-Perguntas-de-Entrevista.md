---
title: Perguntas de Entrevista sobre Pipelines
aliases: [Entrevista de Pipelines]
tags: [pipelines, entrevista, carreira]
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e critérios de resposta sobre pipelines de dados."
---

# Perguntas de Entrevista

## 1. O que diferencia um pipeline de uma sequência de scripts?

Uma boa resposta menciona dependências explícitas, parâmetros, estado, contratos, observabilidade, políticas de falha e recuperação.

## 2. Por que um DAG não pode conter ciclos?

O ciclo impede uma ordenação topológica completa e deixa indefinido qual tarefa deve concluir primeiro. Iterações devem ser controladas dentro de uma tarefa ou de execuções distintas.

## 3. Quando escolher streaming?

Quando a latência tem valor de negócio suficiente para justificar estado contínuo, tratamento de eventos atrasados e maior maturidade operacional.

## 4. Como tornar um backfill seguro?

Parametrizar intervalos, preservar fontes históricas, versionar código, limitar concorrência, usar tarefas idempotentes e validar antes da publicação.

## 5. Retry resolve qualquer falha?

Não. Ele ajuda em falhas transitórias. Em erros determinísticos, apenas repete custo; sem idempotência, pode duplicar efeitos.

## 6. O que significa exactly-once?

Significa que o efeito lógico é observado uma vez dentro de fronteiras definidas. Exige coordenação entre consumo, estado e saída ou deduplicação idempotente.

## 7. Como monitorar um pipeline que termina com status verde, mas entrega dados ruins?

Com testes e métricas de freshness, completude, volume, distribuição, schema e reconciliação, além do estado técnico.

## 8. Qual é a diferença entre scheduler e sensor?

O scheduler cria ou considera execuções conforme uma regra; o sensor verifica uma condição externa de prontidão.

## 9. Como reduzir a latência de um DAG?

Medir o caminho crítico, remover dependências desnecessárias, paralelizar tarefas independentes e otimizar os gargalos realmente pertencentes a esse caminho.

## 10. Como evoluir um pipeline crítico?

Versionar contratos, avaliar compatibilidade, executar versões em paralelo, reconciliar resultados, migrar consumidores gradualmente e manter rollback.

Transforme as respostas em prática em [[13-Exercicios]].

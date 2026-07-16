---
title: Exercícios de Pipelines de Dados
aliases: [Exercícios do Módulo de Pipelines]
tags: [pipelines, exercicios, modulo-07]
created: 2026-07-16
updated: 2026-07-16
description: "Exercícios progressivos sobre desenho e operação de pipelines."
---

# Exercícios

## Revisão conceitual

1. Diferencie tarefa, job, run e pipeline.
2. Explique por que sucesso operacional não prova qualidade dos dados.
3. Compare dependência de dados e dependência de controle.
4. Diferencie event time e processing time.

## Interpretação

5. Um pipeline diário inicia às 02h mesmo quando o arquivo ainda não chegou. Identifique a fragilidade e proponha um limite melhor.
6. Uma API respondeu com timeout depois de criar uma cobrança. Por que um retry imediato é perigoso?
7. Um DAG possui `A → B`, `B → C` e `C → A`. Qual propriedade foi violada?
8. Um dashboard precisa estar atualizado até 08h em 99,5% dos dias. Proponha um SLI.

## Aplicação prática

9. Modele um DAG para pedidos e clientes que convergem em uma tabela de vendas.
10. Defina políticas de retry, timeout e quarentena para esse DAG.
11. Descreva um backfill de 365 partições sem prejudicar a execução diária.
12. Proponha uma estratégia idempotente para carregar pedidos por chave natural.

## Desafios

13. Explique como publicar uma nova versão sem expor resultados parciais.
14. Desenhe um conjunto mínimo de logs, métricas e metadados para diagnosticar atraso.
15. A DataRetail recebe eventos até 48 horas atrasados. Compare três políticas para tratá-los.
16. Implemente o [[14-Laboratorio]] e acrescente uma tarefa independente que possa executar em paralelo.

Consulte [[13-Gabarito]] somente depois de elaborar suas respostas.

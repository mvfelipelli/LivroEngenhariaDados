---
title: Exercícios de Observabilidade de Dados
aliases: [Exercícios do Módulo de Observabilidade]
tags: [observabilidade, exercicios, modulo-11]
created: 2026-07-16
updated: 2026-07-16
description: "Exercícios progressivos sobre sinais, diagnóstico e operação."
---

# Exercícios

## Revisão conceitual

1. Diferencie telemetria, monitoramento e observabilidade.
2. Compare logs, métricas e traces.
3. Defina SLI, SLO e orçamento de erro.
4. Explique as travessias upstream e downstream da linhagem.

## Interpretação

5. Um pipeline terminou, mas publicou metade dos registros. Quais sinais faltaram?
6. Uma métrica usa `pedido_id` como label. Qual problema pode surgir?
7. Dez alertas downstream têm a mesma causa. Como reduzir ruído?
8. Um runbook manda repetir o job sem reconciliação. Qual é o risco?

## Aplicação prática

9. Defina atributos comuns para correlacionar um pipeline.
10. Proponha três SLIs para um produto financeiro.
11. Desenhe dashboards executivo, operacional e diagnóstico.
12. Crie um runbook para atraso de partição.

## Desafios

13. Modele a linhagem de pedidos até três consumidores.
14. Defina política de retenção e redaction para telemetria.
15. Escreva ações fortes para um postmortem de falha recorrente.
16. Execute o [[14-Laboratorio]] e reduza a transformação a 120 segundos para demonstrar ausência de alerta.

Consulte [[13-Gabarito]] depois de elaborar suas respostas.

---
title: Agregações, Funções de Janela e Análise
description: "Métricas por grupo e cálculos analíticos sem perder o detalhe."
tags: [sql, agregacoes, window-functions, volume-04]
aliases: [Módulo 03 SQL, Análise SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Módulo 03 — Agregações, Funções de Janela e Análise

Agregações reduzem linhas ao grão de um grupo. Funções de janela calculam sobre linhas relacionadas preservando o detalhe. Dominar essa diferença permite construir métricas, rankings, acumulados e comparações temporais corretas.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Agregacao-Grao-e-Funcoes-Fundamentais|Agregação, Grão e Funções Fundamentais]]
4. [[04-GROUP-BY-HAVING-FILTER-e-Agregacao-Condicional|GROUP BY, HAVING, FILTER e Agregação Condicional]]
5. [[05-Agrupamentos-Multinivel-Totais-e-Percentis|Agrupamentos Multinível, Totais e Percentis]]
6. [[06-Funcoes-de-Janela-Particoes-Ordem-e-Peers|Funções de Janela, Partições, Ordem e Peers]]
7. [[07-Ranking-ROW-NUMBER-RANK-e-NTILE|Ranking: ROW_NUMBER, RANK e NTILE]]
8. [[08-LAG-LEAD-Primeiro-Ultimo-e-Comparacoes|LAG, LEAD, Primeiro, Último e Comparações]]
9. [[09-Frames-Acumulados-Medias-Moveis-e-Testes|Frames, Acumulados, Médias Móveis e Testes]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    D["Linhas detalhadas"] --> G["GROUP BY reduz"]
    D --> W["OVER preserva"]
    G --> M["Métrica por grupo"]
    W --> A["Métrica por linha"]
```

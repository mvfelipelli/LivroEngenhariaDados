---
title: Estudo de Caso — Lentidão no Fechamento da DataRetail
description: "Diagnóstico causal de batch com pressão de memória e I/O."
tags: [linux, desempenho, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Performance]
created: 2026-07-16
updated: 2026-07-16
---

# Estudo de Caso — DataRetail S.A.

O fechamento diário da DataRetail S.A. passou de 25 para 70 minutos. CPU média permaneceu em 45%, levando a uma suspeita inicial sobre o banco.

## Evidências

- taxa de registros era 35% maior após nova campanha;
- `vmstat` mostrou swap in/out e run queue baixa;
- PSI de memória subiu durante a fase de ordenação;
- `iostat` mostrou alta latência de escrita no mesmo intervalo;
- o worker excedia memória disponível, pressionava cache e escrevia temporários;
- banco manteve latência estável.

```mermaid
flowchart LR
    C["mais registros"] --> M["working set maior"]
    M --> P["pressão e reclaim"]
    P --> S["swap e I/O temporário"]
    S --> L["batch lento"]
```

## Correção

A equipe particionou a ordenação, limitou concorrência, moveu temporários para volume dimensionado e ajustou memória após teste de carga. O tempo caiu para 31 minutos sem alteração do banco.

## Controles permanentes

- duração e throughput por etapa;
- PSI de CPU, memória e I/O;
- working set, swap e eventos OOM;
- latência e fila do volume temporário;
- projeção de volume e alerta de headroom;
- runbook com comandos somente leitura.

A lição central é que CPU ociosa não significa capacidade livre quando o fluxo espera memória e armazenamento. Reproduza o raciocínio em [[14-Laboratorio]].

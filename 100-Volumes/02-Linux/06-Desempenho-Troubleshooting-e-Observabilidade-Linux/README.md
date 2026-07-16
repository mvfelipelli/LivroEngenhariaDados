---
title: Desempenho, Troubleshooting e Observabilidade Linux
description: "Métodos, métricas e ferramentas para diagnosticar sistemas Linux."
tags: [linux, desempenho, troubleshooting, observabilidade]
aliases: [Módulo 06 Linux, Performance Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Módulo 06 — Desempenho, Troubleshooting e Observabilidade Linux

Desempenho é comportamento observado sob uma carga definida. Troubleshooting transforma sintomas em hipóteses testáveis; observabilidade fornece sinais para explicar o estado interno sem depender de adivinhação.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Metodo-Baselines-USE-e-RED|Método, Baselines, USE e RED]]
4. [[04-CPU-Scheduler-Load-e-Concorrencia|CPU, Scheduler, Load e Concorrência]]
5. [[05-Memoria-Cache-Swap-e-OOM|Memória, Cache, Swap e OOM]]
6. [[06-Armazenamento-I-O-e-Filesystems|Armazenamento, I/O e Filesystems]]
7. [[07-Processos-Servicos-e-Rede|Processos, Serviços e Rede]]
8. [[08-Profiling-Tracing-e-eBPF|Profiling, Tracing e eBPF]]
9. [[09-Observabilidade-Incidentes-Capacidade-e-Tuning|Observabilidade, Incidentes, Capacidade e Tuning]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    S["Sintoma"] --> B["Baseline"]
    B --> H["Hipótese"]
    H --> M["Medição"]
    M --> C["Causa"]
    C --> V["Correção e validação"]
```

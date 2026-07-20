---
title: Benchmarking, Profiling, Memória e Otimização
description: "Medição reproduzível antes de mudanças."
tags: [python, benchmarking, profiling, memoria]
aliases: [Profiling Python]
created: 2026-07-17
updated: 2026-07-17
---

# Benchmarking, Profiling, Memória e Otimização

Benchmark compara alternativas sob carga representativa. Separe aquecimento, repita amostras, use `time.perf_counter`, reporte distribuição e controle ambiente.

`timeit` mede trechos; `cProfile` atribui tempo a chamadas; `tracemalloc` rastreia alocações Python; profilers amostrais observam produção com menor interferência.

Otimize o maior gargalo comprovado:

1. reduza trabalho e I/O;
2. escolha algoritmo e estrutura melhores;
3. processe em lote ou vetorize;
4. evite cópias e materializações;
5. só então adicione concorrência ou código nativo.

Meça tempo de parede, CPU, memória máxima, throughput, p50/p95/p99 e erros. Uma otimização que aumenta complexidade precisa de ganho relevante e teste de regressão de performance, sem comprometer correção.

---
title: Exercícios — Desempenho e Observabilidade Linux
description: "Exercícios progressivos de análise Linux."
tags: [linux, desempenho, exercicios]
aliases: [Exercícios Performance Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Exercícios

## Revisão

1. Aplique USE a CPU, memória, disco e interface de rede.
2. Diferencie métrica gauge, contador e histograma.
3. Explique run queue, load e context switches.
4. Diferencie page cache, memória anônima e swap.

## Interpretação

5. CPU está 40%, load 24 em host de 8 CPUs e muitos processos estão em `D`. Proponha hipótese.
6. Disco apresenta 100% busy e baixa latência. Isso prova gargalo?
7. RSS cresce, mas PSS e `MemAvailable` permanecem estáveis. Explique possibilidades.
8. p99 piorou, média não. Defina próximos cortes de dados.

## Aplicação

9. Crie checklist somente leitura para host lento.
10. Defina sinais RED de uma API e USE do banco.
11. Planeje experimento para alterar concorrência de um worker.
12. Esboce alerta de capacidade com headroom e tempo de ação.

## Desafios

13. Correlacione OOM de contêiner com cgroup e host.
14. Escolha entre `perf`, `strace`, trace distribuído e eBPF para quatro hipóteses.
15. Execute [[14-Laboratorio]] e justifique a classificação produzida.

Consulte [[13-Gabarito]] após registrar suas evidências.

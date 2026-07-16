---
title: CPU, Scheduler, Load e Concorrência
description: "Execução, filas, estados de CPU e contenção."
tags: [linux, desempenho, cpu, scheduler]
aliases: [CPU Linux, Load Average]
created: 2026-07-16
updated: 2026-07-16
---

# CPU, Scheduler, Load e Concorrência

O scheduler escolhe tarefas executáveis para CPUs lógicas. Concorrência acima da capacidade produz espera; paralelismo útil depende de trabalho divisível, locks, memória e I/O.

## Sinais

```bash
mpstat -P ALL 1
pidstat -u -w 1
cat /proc/loadavg
perf stat -p "$PID" sleep 10
```

| Métrica | Interpretação inicial |
| --- | --- |
| user | código em espaço de usuário |
| system | trabalho no kernel |
| iowait | CPU ociosa com I/O pendente, não uso de disco |
| steal | tempo tomado pelo hipervisor |
| run queue | tarefas aptas aguardando CPU |
| context switch | troca entre tarefas; custo depende do padrão |

Load average inclui tarefas executáveis e algumas em espera ininterruptível. Deve ser comparado a CPUs disponíveis e investigado por estado; não é porcentagem.

## CPU alta e baixa

CPU alta com fila e latência pode indicar saturação. CPU baixa com serviço lento pode indicar espera por I/O, lock, rede, quota de cgroup ou dependência. Uma thread única limita um núcleo mesmo quando o total do host parece baixo.

Flame graphs agregam stacks amostradas e mostram onde CPU ou espera se concentra. Frequência, NUMA, cache misses e throttling também influenciam cargas de dados.

> [!warning]
> Aumentar threads pode elevar contenção, memória e trocas de contexto. Faça teste de carga e meça throughput e cauda.

Continue em [[05-Memoria-Cache-Swap-e-OOM]].

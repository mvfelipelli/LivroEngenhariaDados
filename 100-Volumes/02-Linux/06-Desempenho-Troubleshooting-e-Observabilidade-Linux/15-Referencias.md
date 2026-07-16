---
title: Referências — Desempenho e Observabilidade Linux
description: "Documentação oficial e bibliografia de análise de sistemas."
tags: [linux, desempenho, referencias]
aliases: [Referências Performance Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Referências

## Documentação oficial

- Linux Kernel Documentation: PSI, scheduler, memory management, block layer, cgroups e tracing.
- Linux man-pages: `proc(5)`, `perf_event_open(2)`, `sched(7)`, `getrusage(2)` e `strace(1)`.
- perf Wiki e kernel tracing documentation.
- BCC e bpftrace: documentação oficial de ferramentas e referência de linguagem.
- sysstat: manuais de `iostat`, `mpstat`, `pidstat` e `sar`.
- systemd: `systemd.resource-control` e journal.

## Livros e métodos

- GREGG, Brendan. *Systems Performance: Enterprise and the Cloud*.
- GREGG, Brendan. *BPF Performance Tools*.
- BEYER, Betsy et al. *Site Reliability Engineering*.
- BARON, Schwartz. *Systems Performance Methodology* e literatura sobre USE.

> [!tip]
> Métricas e campos variam com kernel, distribuição e ferramenta. Confirme a semântica na versão instalada antes de comparar ambientes.

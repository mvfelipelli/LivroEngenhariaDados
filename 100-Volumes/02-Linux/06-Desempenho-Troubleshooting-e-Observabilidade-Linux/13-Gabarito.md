---
title: Gabarito — Desempenho e Observabilidade Linux
description: "Respostas orientativas dos exercícios."
tags: [linux, desempenho, gabarito]
aliases: [Gabarito Performance Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Gabarito

1. CPU: busy/fila/erros; memória: consumo/pressão/OOM; disco: busy/fila/erros; rede: banda/fila e drops/erros.
2. Gauge representa valor atual; contador cresce; histograma distribui observações em faixas.
3. Run queue é espera por CPU; load inclui executáveis e parte do estado D; context switches são trocas de tarefas.
4. Cache representa arquivo, anônima representa heap/stack e swap armazena páginas fora da RAM.
5. Suspeite espera ininterruptível, possivelmente I/O; identifique `wchan`, latência, filas e kernel logs.
6. Não. Dispositivo pode concluir alta taxa com baixa latência. Verifique fila, SLO e headroom.
7. Pode haver páginas compartilhadas, cache contabilizado por processo ou rotação; use mapas e métricas proporcionais.
8. Corte por endpoint, cliente, status, versão, região, dependência e tamanho, preservando volume de amostra.
9. Inclua uptime, mudanças, processos, CPU, memória, PSI, I/O, filesystem, rede, serviços e logs.
10. API: taxa, erros, duração; banco: CPU, memória, I/O, conexões, filas e erros.
11. Fixe carga, meça baseline, altere uma concorrência, observe throughput, p99, recursos e erros, reverta se necessário.
12. Projete tendência e alerte quando o tempo até o limite for menor que provisionamento mais margem.
13. Compare `memory.events`, limite e working set do cgroup com pressão, capacidade e logs OOM do host.
14. `perf` para CPU; `strace` para syscall; trace para caminho da requisição; eBPF para evento dinâmico do kernel.
15. Pressão de memória e I/O é sustentada por PSI, swap, fila e latência, enquanto CPU não está saturada.

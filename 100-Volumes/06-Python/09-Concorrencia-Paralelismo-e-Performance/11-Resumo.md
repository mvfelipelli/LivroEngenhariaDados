---
title: Resumo — Concorrência, Paralelismo e Performance
description: "Síntese dos modelos de execução e medição."
tags: [python, resumo, concorrencia]
aliases: [Resumo Concorrência Python]
created: 2026-07-17
updated: 2026-07-17
---

# Resumo

- Concorrência intercala progresso; paralelismo executa simultaneamente.
- I/O e CPU pedem modelos diferentes.
- A fração serial limita speedup.
- Threads compartilham memória e exigem sincronização.
- Processos paralelizam CPU com custo de IPC.
- Asyncio requer I/O não bloqueante e await cooperativo.
- Concorrência estruturada controla o ciclo de vida de tasks.
- Cancelamento, timeout e limpeza pertencem ao contrato.
- Filas limitadas propagam backpressure.
- Semáforos limitam concorrência, não taxa.
- Profiling deve preceder otimização.

O próximo módulo integra todo o volume em pipelines observáveis e um projeto final.

---
title: Profiling, Tracing e eBPF
description: "Amostragem, eventos, syscalls e instrumentação dinâmica."
tags: [linux, desempenho, profiling, ebpf]
aliases: [Tracing Linux, eBPF]
created: 2026-07-16
updated: 2026-07-16
---

# Profiling, Tracing e eBPF

Profiling responde onde tempo ou recursos se concentram. Tracing registra eventos e relações ao longo do tempo. Ambos introduzem overhead e precisam de escopo, duração e interpretação.

## Escolha da técnica

| Técnica | Boa pergunta |
| --- | --- |
| sampling profiler | quais stacks consomem CPU? |
| syscall tracing | em quais syscalls o processo espera ou falha? |
| application tracing | qual etapa da requisição demora? |
| kernel tracing | onde ocorre latência no kernel? |
| eBPF | qual evento dinâmico pode ser agregado com baixo overhead? |

```bash
perf top -p "$PID"
perf record -F 99 -g -p "$PID" -- sleep 30
strace -f -tt -T -p "$PID"
bpftrace -e 'tracepoint:syscalls:sys_enter_openat { @[comm] = count(); }'
```

`strace` pode alterar timing e gerar muitos dados. `perf` depende de símbolos e permissões. eBPF executa programas verificados em hooks do kernel, mas não é magicamente gratuito nem sempre permitido.

```mermaid
flowchart TD
    H["Hipótese"] --> E["Evento ou amostra"]
    E --> F["Filtro"]
    F --> A["Agregação"]
    A --> I["Interpretação"]
    I --> V["Validação por outro sinal"]
```

Flame graphs representam frequência de stacks, não uma linha do tempo. Off-CPU profiling ajuda a descobrir locks e espera. Preserve privacidade: argumentos, caminhos e payloads podem conter segredos.

> [!tip]
> Comece pela ferramenta menos invasiva que pode refutar a hipótese e aumente a resolução gradualmente.

Próximo: [[09-Observabilidade-Incidentes-Capacidade-e-Tuning]].

---
title: Solução — Análise USE de um Batch
description: "Implementação validada do laboratório USE."
tags: [linux, desempenho, laboratorio, solucao]
aliases: [Solução Laboratório Performance]
created: 2026-07-16
updated: 2026-07-16
---

# Solução — Análise USE de um Batch

Salve como `analisar_use.py`:

```python
inicio = {
    "cpu_total_s": 10_000,
    "cpu_busy_s": 4_000,
    "swap_in_mb": 100,
    "io_ops": 50_000,
    "io_wait_ms": 500_000,
}

fim = {
    "cpu_total_s": 10_200,
    "cpu_busy_s": 4_090,
    "swap_in_mb": 868,
    "io_ops": 52_000,
    "io_wait_ms": 584_000,
    "run_queue": 2.0,
    "cpus": 8,
    "memory_psi_some_pct": 28.0,
    "io_queue": 12.0,
}


def delta(nome):
    return fim[nome] - inicio[nome]


cpu_util = 100 * delta("cpu_busy_s") / delta("cpu_total_s")
cpu_saturada = fim["run_queue"] > fim["cpus"]
swap_delta = delta("swap_in_mb")
memoria_pressao = fim["memory_psi_some_pct"] >= 20 or swap_delta >= 512
io_latencia = delta("io_wait_ms") / delta("io_ops")
io_saturado = fim["io_queue"] >= 8 and io_latencia >= 20

assert round(cpu_util, 1) == 45.0
assert not cpu_saturada and memoria_pressao and io_saturado

print(f"cpu_utilizacao={cpu_util:.1f}%")
print("cpu_saturacao=" + ("sim" if cpu_saturada else "nao"))
print("memoria_pressao=" + ("sim" if memoria_pressao else "nao"))
print(f"swap_delta_mb={swap_delta}")
print(f"io_fila={fim['io_queue']:.1f}")
print(f"io_latencia_ms={io_latencia:.1f}")
print("recurso_limitante=memoria_e_io")
print("analise=ok")
```

## Leitura da solução

CPU é derivada de deltas no mesmo intervalo. Pressão de memória combina PSI e swap; I/O combina fila e latência. As regras são didáticas e explícitas para não transformar limiar genérico em verdade universal.

> [!warning]
> Em produção, valide unidades, resets de contador, missing data, cardinalidade e intervalo antes de automatizar conclusões.

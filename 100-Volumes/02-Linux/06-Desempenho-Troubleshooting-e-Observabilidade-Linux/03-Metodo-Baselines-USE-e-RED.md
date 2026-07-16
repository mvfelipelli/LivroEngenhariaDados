---
title: Método, Baselines, USE e RED
description: "Estratégias sistemáticas para análise de recursos e serviços."
tags: [linux, desempenho, use, red]
aliases: [Método USE, Método RED]
created: 2026-07-16
updated: 2026-07-16
---

# Método, Baselines, USE e RED

Um método evita escolher a ferramenta favorita antes da pergunta. Comece pelo impacto, construa uma linha do tempo e percorra recursos e serviços sem lacunas.

## USE

Para cada recurso, examine:

- **utilization**: proporção ocupada no intervalo;
- **saturation**: trabalho esperando além da capacidade;
- **errors**: falhas, drops ou operações incompletas.

CPU pode ter utilização e run queue; disco, busy time e fila; rede, banda e drops; memória, consumo e reclaim/OOM. Utilização próxima de 100% só é problema quando viola o objetivo ou cria saturação.

## RED

Para cada serviço, examine taxa de requisições, erros e duração. Use percentis, não apenas média: caudas revelam filas e subconjuntos lentos.

```mermaid
flowchart LR
    R["RED do serviço"] --> D["dependência lenta"]
    D --> U["USE do recurso"]
    U --> H["hipótese causal"]
    H --> E["experimento"]
```

## Baseline e intervalo

Compare mesmo horário, carga, versão e configuração. Contadores cumulativos precisam de delta; gauges exigem contexto; taxas precisam de janela. Métricas muito agregadas ocultam picos, e amostragem curta pode confundir ruído com tendência.

```bash
uptime
vmstat 1 10
pidstat -dur 1 10
iostat -xz 1 10
```

> [!tip]
> Execute primeiro comandos somente leitura e registre versão do kernel, uptime, topologia, limites e alterações recentes.

Próximo: [[04-CPU-Scheduler-Load-e-Concorrencia]].

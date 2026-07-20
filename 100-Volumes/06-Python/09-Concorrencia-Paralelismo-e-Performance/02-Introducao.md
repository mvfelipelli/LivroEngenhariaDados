---
title: Introdução à Concorrência e Performance Python
description: "Capacidade, latência e controle de recursos."
tags: [python, introducao, performance]
aliases: [Introdução Concorrência Python]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Concorrência permite progresso intercalado; paralelismo executa trabalho simultaneamente. Assincronia é um estilo de composição que evita bloquear a thread enquanto espera I/O.

```mermaid
flowchart LR
    F["Fonte"] --> Q["Fila limitada"]
    Q --> W["Workers"]
    W --> S["Sink"]
    S --> M["Métricas"]
    Q -. "backpressure" .-> F
```

Aumentar workers não cria capacidade infinita: banco, API, CPU, memória e rede têm limites. O desenho correto mede throughput e latência, limita trabalho em voo e preserva cancelamento e idempotência.

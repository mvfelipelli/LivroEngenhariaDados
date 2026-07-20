---
title: Filas, Semáforos, Backpressure e Rate Limits
description: "Controle explícito de trabalho em voo."
tags: [python, filas, semaforos, backpressure]
aliases: [Backpressure Python]
created: 2026-07-17
updated: 2026-07-17
---

# Filas, Semáforos, Backpressure e Rate Limits

Fila limitada desacopla produtor e consumidor até uma capacidade definida. Quando cheia, `put` espera e propaga backpressure.

```python
fila: asyncio.Queue[Evento | None] = asyncio.Queue(maxsize=100)
```

Consumidores chamam `task_done` em `finally`; `join` aguarda todos os itens. Sentinelas encerram workers, mas deve haver uma por consumidor ou protocolo equivalente.

Semáforo limita operações simultâneas, como conexões a uma API. Ele controla concorrência, não taxa ao longo do tempo. Rate limit requer token bucket, janela ou respeito aos headers do provedor.

Escolha capacidade pela memória, latência aceitável e capacidade do sink. Uma fila ilimitada converte lentidão downstream em crescimento de memória e eventual indisponibilidade.

---
title: Solução — Coletor Assíncrono Limitado
description: "Implementação de referência do laboratório."
tags: [python, solucao, asyncio]
aliases: [Solução Concorrência Python]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Coletor Assíncrono Limitado

```python
from __future__ import annotations

import asyncio
from dataclasses import dataclass

@dataclass
class Metricas:
    atual: int = 0
    maxima: int = 0
    tentativas: int = 0

async def remoto(identificador: int, tentativa: int, metricas: Metricas) -> tuple[int, int]:
    metricas.atual += 1
    metricas.maxima = max(metricas.maxima, metricas.atual)
    metricas.tentativas += 1
    try:
        atraso = 0.2 if identificador == 3 and tentativa == 1 else 0.005
        await asyncio.sleep(atraso)
        return identificador, identificador * 100
    finally:
        metricas.atual -= 1

async def buscar(identificador: int, semaforo: asyncio.Semaphore, metricas: Metricas) -> tuple[int, int]:
    for tentativa in (1, 2):
        try:
            async with semaforo:
                async with asyncio.timeout(0.1):
                    return await remoto(identificador, tentativa, metricas)
        except TimeoutError:
            if tentativa == 2:
                raise
            await asyncio.sleep(0)
    raise AssertionError("inalcançável")

async def coletar() -> tuple[list[tuple[int, int]], Metricas]:
    semaforo = asyncio.Semaphore(2)
    metricas = Metricas()
    async with asyncio.TaskGroup() as grupo:
        tarefas = [grupo.create_task(buscar(item, semaforo, metricas)) for item in range(1, 7)]
    resultados = sorted(tarefa.result() for tarefa in tarefas)
    return resultados, metricas

async def main() -> None:
    primeira, metricas = await coletar()
    segunda, metricas_2 = await coletar()
    assert primeira == segunda
    assert len(primeira) == 6 and sum(valor for _, valor in primeira) == 2100
    assert metricas.maxima == metricas_2.maxima == 2
    assert metricas.tentativas == metricas_2.tentativas == 7
    assert metricas.atual == metricas_2.atual == 0
    print("resultados=6 total=2100 concorrencia_maxima=2 tentativas=7 timeout_recuperado=ok determinismo=ok")

if __name__ == "__main__":
    asyncio.run(main())
```

O contador fica dentro da coroutine protegida pelo semáforo; o `finally` garante correção mesmo quando o timeout cancela a primeira tentativa.

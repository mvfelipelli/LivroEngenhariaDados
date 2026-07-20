---
title: Asyncio, Coroutines, Tasks e Concorrência Estruturada
description: "I/O cooperativo e ciclo de vida de tarefas."
tags: [python, asyncio, coroutines, tasks]
aliases: [Asyncio Python]
created: 2026-07-17
updated: 2026-07-17
---

# Asyncio, Coroutines, Tasks e Concorrência Estruturada

Uma coroutine progride até `await`, onde cede controle ao event loop. Código bloqueante dentro dela paralisa todas as tarefas daquela thread.

```python
import asyncio

async def coletar(ids: list[str]) -> list[dict]:
    async with asyncio.TaskGroup() as grupo:
        tarefas = [grupo.create_task(buscar(item)) for item in ids]
    return [tarefa.result() for tarefa in tarefas]
```

TaskGroup vincula o ciclo de vida das tarefas ao bloco: falha cancela irmãs e exceções são agrupadas. Isso evita tasks órfãs.

Use bibliotecas async de ponta a ponta. Para uma função bloqueante curta, `asyncio.to_thread` evita bloquear o loop, mas não transforma CPU Python em paralelo eficiente. Não crie um event loop por item; uma aplicação possui fronteira assíncrona clara.

---
title: Threads, GIL, Locks e ThreadPoolExecutor
description: "Concorrência compartilhada para I/O bloqueante."
tags: [python, threads, gil, locks]
aliases: [Threads Python]
created: 2026-07-17
updated: 2026-07-17
---

# Threads, GIL, Locks e ThreadPoolExecutor

Threads compartilham memória e tornam comunicação barata, mas criam races. No CPython tradicional, o GIL permite uma thread executando bytecode por vez; I/O e várias extensões nativas liberam o lock.

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=8) as executor:
    resultados = list(executor.map(buscar, ids))
```

O GIL não torna operações compostas atômicas. Proteja invariantes com `Lock`, use `RLock` apenas quando reentrada for necessária e minimize região crítica. Deadlock surge por aquisição incompatível; imponha ordem global.

Futures propagam resultado ou exceção quando consumidas. Não abandone futures sem observar falhas. Limite submissões: enfileirar milhões de tarefas consome memória mesmo com poucos workers.

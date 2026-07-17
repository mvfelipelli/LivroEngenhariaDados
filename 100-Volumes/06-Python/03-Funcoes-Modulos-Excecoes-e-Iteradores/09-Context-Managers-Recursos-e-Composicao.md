---
title: Context Managers, Recursos e Composição
description: "Aquisição e liberação determinística de recursos."
tags: [python, context-manager, recursos]
aliases: [Context Managers Python]
created: 2026-07-17
updated: 2026-07-17
---

# Context Managers, Recursos e Composição

O protocolo `__enter__` e `__exit__` delimita aquisição e liberação. Arquivos, locks, conexões e transações devem ser fechados mesmo quando ocorre uma exceção.

```python
from contextlib import contextmanager

@contextmanager
def etapa(nome: str):
    print(f"inicio={nome}")
    try:
        yield
    finally:
        print(f"fim={nome}")
```

`contextlib.closing` adapta objetos com `close`; `ExitStack` compõe quantidade dinâmica de contextos e callbacks. O `__exit__` pode suprimir uma exceção retornando verdadeiro, mas isso deve ser raro e explícito.

Separar a vida do recurso da transformação permite testar regras com objetos em memória e integrar recursos reais apenas nas bordas.

---
title: Geradores, Yield e Pipelines Preguiçosos
description: "Produção incremental e backpressure natural."
tags: [python, geradores, yield, pipelines]
aliases: [Geradores Python]
created: 2026-07-17
updated: 2026-07-17
---

# Geradores, Yield e Pipelines Preguiçosos

Uma função com `yield` cria um gerador: seu corpo começa quando o consumidor pede o primeiro item e suspende entre produções.

```python
from collections.abc import Iterable, Iterator

def aprovados(eventos: Iterable[dict]) -> Iterator[dict]:
    for evento in eventos:
        if evento.get("status") == "aprovado":
            yield evento
```

Pipelines preguiçosos reduzem memória e permitem começar a produzir cedo. A demanda do consumidor limita naturalmente o avanço da fonte, embora isso não substitua controle explícito em sistemas distribuídos.

Erros podem surgir durante a iteração, não na criação do gerador. A fronteira de consumo precisa definir rejeição, retry e encerramento. `yield from` delega a outro iterável e preserva o protocolo do gerador.

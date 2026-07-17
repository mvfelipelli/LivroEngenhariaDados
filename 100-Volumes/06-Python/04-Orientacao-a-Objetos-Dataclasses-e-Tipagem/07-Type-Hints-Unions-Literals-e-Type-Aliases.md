---
title: Type Hints, Unions, Literals e Type Aliases
description: "Vocabulário básico da tipagem estática gradual."
tags: [python, type-hints, unions, literals]
aliases: [Type Hints Python]
created: 2026-07-17
updated: 2026-07-17
---

# Type Hints, Unions, Literals e Type Aliases

Anotações descrevem contratos para leitores e ferramentas; o runtime normalmente não as aplica.

```python
from typing import Literal, TypeAlias

Status: TypeAlias = Literal["recebido", "aprovado", "cancelado"]

def publicar(pedido_id: str, status: Status, tentativas: int | None = None) -> bool:
    return bool(pedido_id) and status != "cancelado"
```

`T | None` torna ausência explícita. `Literal` restringe valores conhecidos estaticamente, mas uma string externa ainda precisa ser validada antes de ser tratada como `Status`.

Prefira tipos concretos no retorno e abstrações adequadas na entrada: `Iterable[T]` quando só há iteração, `Sequence[T]` quando ordem e índice são necessários. Isso amplia compatibilidade sem prometer operações não usadas.

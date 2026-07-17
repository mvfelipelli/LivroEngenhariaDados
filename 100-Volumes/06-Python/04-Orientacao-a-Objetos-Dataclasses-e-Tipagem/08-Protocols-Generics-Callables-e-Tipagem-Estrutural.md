---
title: Protocols, Generics, Callables e Tipagem Estrutural
description: "Interfaces por comportamento e abstrações parametrizadas."
tags: [python, protocols, generics, tipagem]
aliases: [Protocols Python]
created: 2026-07-17
updated: 2026-07-17
---

# Protocols, Generics, Callables e Tipagem Estrutural

`Protocol` descreve operações necessárias sem exigir herança nominal.

```python
from typing import Protocol, TypeVar

T = TypeVar("T")

class Repositorio(Protocol[T]):
    def salvar(self, item: T) -> None: ...
    def obter(self, identificador: str) -> T | None: ...
```

Qualquer classe com métodos compatíveis satisfaz o protocolo para o analisador. Isso facilita testar com implementação em memória e usar banco em produção.

Generics preservam relações entre tipos de entrada e saída. `Callable[[Pedido], bool]` descreve callbacks simples; Protocol com `__call__` suporta parâmetros nomeados e atributos adicionais.

Variância determina como subtipos se relacionam dentro de containers genéricos. Tipos mutáveis tendem a ser invariantes, pois leitura e escrita impõem direções opostas.

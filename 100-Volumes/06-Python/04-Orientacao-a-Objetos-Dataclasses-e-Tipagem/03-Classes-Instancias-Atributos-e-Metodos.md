---
title: Classes, Instâncias, Atributos e Métodos
description: "Fundamentos do modelo de classes Python."
tags: [python, classes, metodos]
aliases: [Classes Python]
created: 2026-07-17
updated: 2026-07-17
---

# Classes, Instâncias, Atributos e Métodos

Uma classe é um objeto que cria instâncias. A busca de atributos consulta a instância e depois a classe e seus ancestrais.

```python
class Contador:
    unidade = "registros"

    def __init__(self) -> None:
        self._valor = 0

    def incrementar(self, quantidade: int = 1) -> None:
        if quantidade < 0:
            raise ValueError("quantidade negativa")
        self._valor += quantidade

    @property
    def valor(self) -> int:
        return self._valor
```

Métodos de instância recebem `self`; `@classmethod` recebe a classe e serve a construtores alternativos; `@staticmethod` não recebe contexto automático e deve ser usado quando a operação pertence semanticamente ao namespace.

Atributos mutáveis de classe são compartilhados entre instâncias e raramente representam estado correto.

---
title: Encapsulamento, Propriedades e Invariantes
description: "Proteção de estado válido e evolução da API."
tags: [python, encapsulamento, propriedades]
aliases: [Encapsulamento Python]
created: 2026-07-17
updated: 2026-07-17
---

# Encapsulamento, Propriedades e Invariantes

Python usa convenções, não campos privados absolutos. Um prefixo `_` comunica API interna; dois underscores ativam name mangling, útil para evitar colisões em subclasses, não para segurança.

Propriedades preservam sintaxe de atributo enquanto controlam leitura e escrita:

```python
class Lote:
    def __init__(self, limite: int) -> None:
        if limite <= 0:
            raise ValueError("limite deve ser positivo")
        self._limite = limite

    @property
    def limite(self) -> int:
        return self._limite
```

Uma instância deve nascer válida. Métodos de transição validam pré-condições antes de alterar o estado e evitam mudanças parciais. Validação de tipos externos ainda ocorre na borda: type hints não rejeitam automaticamente um JSON incorreto.

> [!tip]
> Exponha operações do domínio, como `cancelar()`, em vez de permitir que qualquer chamador reescreva `status`.

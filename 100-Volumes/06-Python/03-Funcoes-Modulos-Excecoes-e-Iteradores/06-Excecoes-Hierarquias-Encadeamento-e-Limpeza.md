---
title: Exceções, Hierarquias, Encadeamento e Limpeza
description: "Falhas significativas e preservação de contexto."
tags: [python, excecoes, erros]
aliases: [Exceções Python]
created: 2026-07-17
updated: 2026-07-17
---

# Exceções, Hierarquias, Encadeamento e Limpeza

Exceções representam caminhos anormais que o chamador pode tratar. Capture a classe mais específica possível e limite o bloco `try` à operação que pode falhar.

```python
class EventoInvalido(ValueError):
    pass

def converter(texto: str) -> int:
    try:
        return int(texto)
    except ValueError as erro:
        raise EventoInvalido(f"valor inválido: {texto!r}") from erro
```

`raise ... from erro` preserva a causa. `else` executa após sucesso; `finally` executa mesmo diante de retorno ou falha e serve à limpeza inevitável.

Não capture `BaseException`, pois ela inclui sinais de término. `except Exception` só é apropriado em fronteiras que registram contexto e repropagam ou convertem a falha. Nunca use exceção para fluxo esperado em grandes volumes quando um resultado explícito é mais claro.

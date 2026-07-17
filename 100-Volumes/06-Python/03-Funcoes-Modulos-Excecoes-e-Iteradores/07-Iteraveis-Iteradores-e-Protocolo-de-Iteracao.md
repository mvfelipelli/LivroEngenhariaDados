---
title: Iteráveis, Iteradores e Protocolo de Iteração
description: "Consumo incremental e protocolo iterador."
tags: [python, iteraveis, iteradores]
aliases: [Protocolo de Iteração Python]
created: 2026-07-17
updated: 2026-07-17
---

# Iteráveis, Iteradores e Protocolo de Iteração

Um iterável produz um iterador por `iter()`. Um iterador mantém estado, devolve itens por `next()` e sinaliza término com `StopIteration`.

```python
class Contador:
    def __init__(self, fim: int) -> None:
        self.atual = 0
        self.fim = fim

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.atual >= self.fim:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor
```

Listas são reiteráveis; iteradores normalmente são consumíveis uma vez. Documente essa diferença quando uma API recebe `Iterable`. `itertools` oferece composição preguiçosa, mas funções como `tee` podem manter buffers grandes se consumidores avançarem em ritmos diferentes.

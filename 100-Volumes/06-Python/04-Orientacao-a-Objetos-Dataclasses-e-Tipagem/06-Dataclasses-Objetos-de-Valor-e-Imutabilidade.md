---
title: Dataclasses, Objetos de Valor e Imutabilidade
description: "Registros declarativos e semântica de valor."
tags: [python, dataclasses, imutabilidade]
aliases: [Dataclasses Python]
created: 2026-07-17
updated: 2026-07-17
---

# Dataclasses, Objetos de Valor e Imutabilidade

`@dataclass` gera inicialização, representação e igualdade a partir dos campos. `frozen=True` impede reatribuição normal e permite modelar valores estáveis.

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Dinheiro:
    centavos: int
    moeda: str = "BRL"

    def __post_init__(self) -> None:
        if self.centavos < 0:
            raise ValueError("valor negativo")
```

`default_factory` cria novo valor por instância. `slots=True` reduz armazenamento e impede atributos arbitrários, mas exige atenção com herança.

Frozen é raso: uma lista interna continua mutável. Para imutabilidade efetiva, use campos imutáveis, como tuple e frozenset. Objetos de valor comparam-se pelo conteúdo; entidades normalmente possuem identidade estável e ciclo de vida.

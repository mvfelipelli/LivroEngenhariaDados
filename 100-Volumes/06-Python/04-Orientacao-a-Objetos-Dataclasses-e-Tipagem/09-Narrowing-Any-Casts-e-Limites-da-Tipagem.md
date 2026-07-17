---
title: Narrowing, Any, Casts e Limites da Tipagem
description: "Refinamento seguro e fronteiras dinâmicas."
tags: [python, narrowing, any, cast]
aliases: [Narrowing Python]
created: 2026-07-17
updated: 2026-07-17
---

# Narrowing, Any, Casts e Limites da Tipagem

Narrowing reduz um tipo amplo após uma verificação reconhecida:

```python
def tamanho(valor: str | None) -> int:
    if valor is None:
        return 0
    return len(valor)
```

`isinstance`, comparações com `None`, pattern matching e type guards podem refinar tipos. `assert` é adequado a invariantes internas, não à validação de entrada, pois pode ser removido com otimização.

`Any` desliga verificação e se propaga; restrinja-o à borda e converta cedo. `object` aceita qualquer valor, mas exige narrowing antes do uso, sendo mais seguro.

`cast(T, valor)` informa algo ao analisador e não converte nem valida em runtime. Se o fato não foi provado, o cast apenas esconde um defeito. Tipagem não verifica formatos, limites numéricos, credenciais ou disponibilidade de serviços.

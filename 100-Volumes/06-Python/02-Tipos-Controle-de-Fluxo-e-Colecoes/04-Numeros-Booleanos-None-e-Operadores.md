---
title: Números, Booleanos, None e Operadores
description: "Semântica numérica, ausência e expressões."
tags: [python, numeros, booleanos, none]
aliases: [Números Python]
created: 2026-07-17
updated: 2026-07-17
---

# Números, Booleanos, None e Operadores

`int` possui precisão arbitrária limitada pela memória. `float` segue ponto flutuante binário e não representa exatamente muitos decimais. Para dinheiro, prefira centavos inteiros ou `Decimal` com política explícita de arredondamento.

```python
from decimal import Decimal, ROUND_HALF_UP

valor = Decimal("19.995").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
assert valor == Decimal("20.00")
```

`None` representa ausência, não zero, vazio ou falso. Valores falsy incluem `0`, `""` e coleções vazias; portanto, `if not valor` não distingue essas condições.

Operadores booleanos fazem curto-circuito e retornam um dos operandos. Comparações encadeadas como `0 <= quantidade <= 100` avaliam o termo central uma vez. Divisão `/` retorna float; `//` é divisão pelo piso, inclusive para negativos.

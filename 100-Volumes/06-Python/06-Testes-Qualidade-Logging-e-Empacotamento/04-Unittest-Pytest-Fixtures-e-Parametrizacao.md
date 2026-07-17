---
title: Unittest, Pytest, Fixtures e Parametrização
description: "Estrutura de suítes e preparação controlada."
tags: [python, unittest, pytest, fixtures]
aliases: [Testes Python]
created: 2026-07-17
updated: 2026-07-17
---

# Unittest, Pytest, Fixtures e Parametrização

`unittest` integra a biblioteca padrão e fornece casos, assertions, setup, subtests e mocks. Pytest oferece descoberta concisa, fixtures por injeção e parametrização declarativa.

```python
import unittest

class TesteTotal(unittest.TestCase):
    def test_soma_centavos(self) -> None:
        for valores, esperado in [([], 0), ([100, 200], 300)]:
            with self.subTest(valores=valores):
                self.assertEqual(sum(valores), esperado)
```

Fixtures criam contexto e garantem limpeza. Seu escopo deve ser o menor possível; fixture compartilhada e mutável acopla testes. `TemporaryDirectory` e `tempfile` isolam filesystem.

Parametrização reduz repetição de casos equivalentes, mas não deve esconder a intenção de cenários semanticamente diferentes.

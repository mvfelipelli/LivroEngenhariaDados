---
title: Composição, Herança, Polimorfismo e MRO
description: "Reuso de comportamento e substituição segura."
tags: [python, composicao, heranca, polimorfismo]
aliases: [Composição Python]
created: 2026-07-17
updated: 2026-07-17
---

# Composição, Herança, Polimorfismo e MRO

Composição expressa “tem um”; herança, “é um” substituível. Prefira composição para combinar políticas independentes.

```python
class Processador:
    def __init__(self, validador, destino) -> None:
        self.validador = validador
        self.destino = destino
```

Polimorfismo permite usar objetos diferentes pela mesma interface. Em Python, isso pode ocorrer por duck typing sem ancestral comum.

Herança múltipla segue uma Method Resolution Order calculada por C3. `super()` continua a cadeia da MRO; não significa necessariamente “classe pai imediata”. Mixins pequenos e sem estado podem ser úteis, mas hierarquias profundas tornam inicialização e invariantes difíceis de prever.

Subclasses devem aceitar as expectativas da classe base. Se precisam proibir entradas válidas ou alterar significado do retorno, a relação de substituição está quebrada.

---
title: Expressões Regulares, Grupos e Performance
description: "Parsing textual delimitado e padrões seguros."
tags: [python, regex, parsing]
aliases: [Regex Python]
created: 2026-07-17
updated: 2026-07-17
---

# Expressões Regulares, Grupos e Performance

Regex é apropriada a linguagens textuais regulares e delimitadas, não a JSON, HTML completo ou gramáticas recursivas.

```python
import re

PADRAO_PEDIDO = re.compile(r"^(?P<prefixo>[A-Z]{2})-(?P<numero>[1-9]\d{0,9})$")
casamento = PADRAO_PEDIDO.fullmatch("BR-1042")
if casamento:
    numero = int(casamento.group("numero"))
```

Use strings raw, grupos nomeados e `fullmatch` quando todo o campo deve obedecer ao padrão. Compile padrões reutilizados para comunicar intenção.

Quantificadores aninhados e alternativas ambíguas podem causar backtracking catastrófico. Limite o tamanho da entrada, simplifique o padrão e prefira parser direto quando possível. Regex confirma forma textual, não existência do pedido nem validade de negócio.

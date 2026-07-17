---
title: I/O Textual, Binário, Buffers e Encoding
description: "Streams, codificação e leitura incremental."
tags: [python, io, encoding, buffers]
aliases: [I/O Python]
created: 2026-07-17
updated: 2026-07-17
---

# I/O Textual, Binário, Buffers e Encoding

Modo texto converte bytes em `str` usando encoding e regras de newline. Modo binário entrega bytes sem interpretação.

```python
with open("pedidos.csv", "r", encoding="utf-8", newline="") as arquivo:
    for linha in arquivo:
        processar(linha)
```

Para CSV, `newline=""` permite que o módulo controle finais de linha. Iterar pelo arquivo limita memória; `read()` materializa todo o conteúdo.

Buffers reduzem chamadas ao sistema. `flush()` envia ao buffer do sistema operacional; durabilidade diante de falha de energia pode exigir `os.fsync()`, com custo maior.

Use `with` para fechamento determinístico. Erros de decoding devem produzir rejeição ou falha explícita; substituir caracteres só é correto quando a política de perda é intencional e observável.

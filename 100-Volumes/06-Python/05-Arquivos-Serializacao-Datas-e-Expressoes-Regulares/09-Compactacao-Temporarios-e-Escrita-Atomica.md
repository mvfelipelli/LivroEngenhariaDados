---
title: Compactação, Temporários e Escrita Atômica
description: "Publicação segura e arquivos comprimidos."
tags: [python, compactacao, atomicidade, temporarios]
aliases: [Escrita Atômica Python]
created: 2026-07-17
updated: 2026-07-17
---

# Compactação, Temporários e Escrita Atômica

`gzip`, `bz2`, `lzma` e `zipfile` oferecem compactação na biblioteca padrão. Compactar economiza I/O e armazenamento ao custo de CPU; o formato deve ser escolhido pela interoperabilidade.

Publicação segura escreve em arquivo temporário no mesmo diretório, faz flush, opcionalmente fsync, e substitui o destino:

```python
import os
from pathlib import Path

temporario = Path("saida.csv.tmp")
destino = Path("saida.csv")
with temporario.open("w", encoding="utf-8", newline="") as arquivo:
    arquivo.write("id,valor\n")
    arquivo.flush()
    os.fsync(arquivo.fileno())
temporario.replace(destino)
```

Substituição atômica depende de permanecer no mesmo filesystem. Concorrência entre escritores ainda requer coordenação. Limpe temporários em falhas sem remover arquivos que pertencem a outro processo.

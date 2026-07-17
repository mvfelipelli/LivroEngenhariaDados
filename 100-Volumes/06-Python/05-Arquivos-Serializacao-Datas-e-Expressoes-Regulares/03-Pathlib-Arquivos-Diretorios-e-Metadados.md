---
title: Pathlib, Arquivos, Diretórios e Metadados
description: "Caminhos portáveis e operações do filesystem."
tags: [python, pathlib, filesystem]
aliases: [Pathlib Python]
created: 2026-07-17
updated: 2026-07-17
---

# Pathlib, Arquivos, Diretórios e Metadados

`pathlib.Path` representa caminhos sem concatenar separadores manualmente.

```python
from pathlib import Path

base = Path("dados")
entrada = base / "pedidos.jsonl"
base.mkdir(parents=True, exist_ok=True)
```

`exists()` não distingue tipos; use `is_file()` e `is_dir()` quando o contrato exige. `stat()` expõe tamanho e tempos do filesystem, mas o significado de criação varia por plataforma.

`resolve()` produz caminho absoluto e normaliza componentes; links simbólicos exigem cuidado para não escapar de uma raiz autorizada. Antes de aceitar um caminho externo, resolva a raiz e o destino e verifique a relação de ancestralidade.

Iteração com `iterdir()` e `glob()` não promete ordem de negócio. Ordene explicitamente quando a sequência afetar o resultado.

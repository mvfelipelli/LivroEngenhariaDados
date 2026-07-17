---
title: Instalação, Versões e Portabilidade
description: "Compatibilidade do interpretador entre ambientes."
tags: [python, versoes, portabilidade]
aliases: [Versões Python]
created: 2026-07-17
updated: 2026-07-17
---

# Instalação, Versões e Portabilidade

Projetos devem declarar a menor versão suportada e testá-la. Uma restrição como `>=3.12,<3.14` comunica compatibilidade sem presumir que toda versão futura funcionará.

```bash
python --version
python -c "import sys; print(sys.executable)"
```

Use `sys.executable` para saber qual interpretador está realmente ativo. Em automações, invoque `python -m pip` para associar o instalador ao mesmo runtime.

Portabilidade exige cuidado com separadores de caminho, encoding, finais de linha e shell. A biblioteca `pathlib` reduz diferenças entre Windows e Linux:

```python
from pathlib import Path

entrada = Path("dados") / "pedidos.csv"
print(entrada.resolve())
```

Imagens de contêiner ajudam a estabilizar o sistema operacional, mas ainda exigem versão e dependências fixadas.

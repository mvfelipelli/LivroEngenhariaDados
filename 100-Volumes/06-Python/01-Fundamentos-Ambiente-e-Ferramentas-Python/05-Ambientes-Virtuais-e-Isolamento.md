---
title: Ambientes Virtuais e Isolamento
description: "Isolamento de interpretador e pacotes por projeto."
tags: [python, venv, isolamento]
aliases: [Ambientes Virtuais Python]
created: 2026-07-17
updated: 2026-07-17
---

# Ambientes Virtuais e Isolamento

Um ambiente virtual cria um prefixo isolado para executáveis e pacotes. Ele evita que a atualização de uma biblioteca em um projeto quebre outro.

```bash
python -m venv .venv
```

No Linux ou macOS, a ativação usual é `source .venv/bin/activate`; no PowerShell, `.venv\Scripts\Activate.ps1`. A ativação apenas ajusta o `PATH`: em CI, pode-se chamar diretamente o executável do ambiente.

```bash
python -m pip --version
python -c "import sys; print(sys.prefix != sys.base_prefix)"
```

O diretório `.venv` não deve ser versionado. O que pertence ao Git é a declaração reproduzível das dependências.

> [!info]
> Ambientes virtuais isolam pacotes Python, não bibliotecas nativas do sistema nem serviços externos.

---
title: Configuração, Segredos e Organização de Projetos
description: "Limites entre código, configuração e credenciais."
tags: [python, configuracao, segredos, projetos]
aliases: [Organização de Projetos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Configuração, Segredos e Organização de Projetos

Código descreve comportamento; configuração seleciona o ambiente; segredos concedem acesso. Credenciais nunca devem ser gravadas no código, em exemplos reais ou no histórico Git.

```python
import os

dsn = os.environ.get("DATARETAIL_DSN")
if not dsn:
    raise RuntimeError("DATARETAIL_DSN não configurada")
```

Uma organização inicial adequada é:

```text
projeto/
├── pyproject.toml
├── README.md
├── src/dataretail/
└── tests/
```

O layout `src` reduz imports acidentais do diretório de trabalho. Configurações devem ter defaults seguros, validação no início da execução e precedência documentada.

> [!warning]
> Arquivos `.env` são convenientes localmente, mas o arquivo com valores reais deve ser ignorado; versione somente um exemplo sem credenciais.

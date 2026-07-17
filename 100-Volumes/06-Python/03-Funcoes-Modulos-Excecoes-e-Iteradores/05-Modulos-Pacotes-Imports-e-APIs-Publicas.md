---
title: Módulos, Pacotes, Imports e APIs Públicas
description: "Organização, inicialização e limites de dependência."
tags: [python, modulos, pacotes, imports]
aliases: [Módulos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Módulos, Pacotes, Imports e APIs Públicas

Um módulo é carregado uma vez por processo e armazenado em `sys.modules`. Código no nível superior executa durante a primeira importação; evite abrir conexões ou ler grandes arquivos ali.

```text
src/dataretail/
├── __init__.py
├── dominio.py
├── parsing.py
└── cli.py
```

Pacotes organizam módulos sob um namespace. Imports absolutos tornam dependências visíveis; relativos são úteis dentro de um pacote coeso.

Uma API pública pequena reduz acoplamento. Convenções com `_nome` indicam detalhe interno; `__all__` controla exportações por wildcard, mas documentação e versionamento continuam necessários.

Dependências circulares sinalizam responsabilidades misturadas. Extraia contratos para um módulo mais fundamental ou inverta a dependência.

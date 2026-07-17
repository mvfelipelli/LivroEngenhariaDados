---
title: Linguagem, Runtime e Modelo de Execução
description: "Do código-fonte ao processo Python."
tags: [python, runtime, bytecode]
aliases: [Runtime Python]
created: 2026-07-17
updated: 2026-07-17
---

# Linguagem, Runtime e Modelo de Execução

Python define uma linguagem; CPython é sua implementação de referência mais usada. Ao executar um módulo, CPython analisa o código, compila-o para bytecode e o avalia em uma máquina virtual. Arquivos `.pyc` podem armazenar bytecode em cache, mas não substituem dependências nem garantem portabilidade entre versões.

Cada execução ocorre em um processo com argumentos, ambiente, entrada, saída, erro e código de retorno.

```python
import platform
import sys

print(platform.python_implementation())
print(sys.version_info[:3])
print(sys.argv)
```

O Global Interpreter Lock de CPython afeta threads que executam bytecode intensivo em CPU, tema aprofundado no módulo de concorrência. Ele não impede concorrência de I/O.

> [!note]
> “Interpretada” não significa “sem compilação”: a compilação para bytecode normalmente ocorre de forma transparente.

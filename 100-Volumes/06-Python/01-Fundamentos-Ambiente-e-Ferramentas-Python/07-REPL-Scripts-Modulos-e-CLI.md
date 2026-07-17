---
title: REPL, Scripts, Módulos e CLI
description: "Formas de executar e distribuir código Python."
tags: [python, repl, cli, modulos]
aliases: [Execução Python]
created: 2026-07-17
updated: 2026-07-17
---

# REPL, Scripts, Módulos e CLI

O REPL favorece exploração curta. Scripts automatizam uma tarefa; módulos organizam nomes importáveis; pacotes agrupam módulos. `python -m pacote.modulo` preserva a semântica de importação melhor que executar um arquivo interno diretamente.

```python
import argparse

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--origem", required=True)
    args = parser.parse_args()
    print(f"origem={args.origem}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Uma CLI deve separar parsing, regra de negócio e efeitos externos. Código `0` indica sucesso; códigos não zero comunicam falha à orquestração.

> [!tip]
> Faça `main()` retornar um inteiro: isso simplifica testes e torna o contrato operacional explícito.

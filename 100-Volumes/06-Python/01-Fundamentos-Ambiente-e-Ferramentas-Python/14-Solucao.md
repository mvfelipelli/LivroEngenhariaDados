---
title: Solução — CLI de Inspeção de Pedidos
description: "Implementação de referência do laboratório."
tags: [python, solucao, cli]
aliases: [Solução Fundamentos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — CLI de Inspeção de Pedidos

```python
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

def inspecionar(caminho: Path, limite: int) -> tuple[int, int]:
    if limite <= 0:
        raise ValueError("limite deve ser positivo")

    registros = 0
    total = 0
    with caminho.open(newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        if leitor.fieldnames != ["pedido_id", "valor_centavos"]:
            raise ValueError("cabeçalho inválido")

        for linha_numero, linha in enumerate(leitor, start=2):
            if registros >= limite:
                break
            if not linha["pedido_id"].strip():
                raise ValueError(f"pedido vazio na linha {linha_numero}")
            try:
                valor = int(linha["valor_centavos"])
            except ValueError as erro:
                raise ValueError(f"valor inválido na linha {linha_numero}") from erro
            if valor < 0:
                raise ValueError(f"valor negativo na linha {linha_numero}")
            registros += 1
            total += valor
    return registros, total

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--entrada", type=Path, required=True)
    parser.add_argument("--limite", type=int, default=1000)
    args = parser.parse_args(argv)

    if not args.entrada.is_file():
        print(f"erro=arquivo_inexistente caminho={args.entrada}", file=sys.stderr)
        return 2

    try:
        registros, total = inspecionar(args.entrada, args.limite)
    except (OSError, ValueError) as erro:
        print(f"erro=entrada_invalida detalhe={erro}", file=sys.stderr)
        return 3

    print(f"registros={registros}")
    print(f"total_centavos={total}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Exemplo de entrada:

```csv
pedido_id,valor_centavos
P-1,1200
P-2,800
P-3,2500
```

Saída esperada: três registros e total de `4500` centavos. A função central não conhece `argparse`, o que permite testá-la separadamente.

---
title: Solução — Pipeline Preguiçoso em Lotes
description: "Implementação de referência do laboratório."
tags: [python, solucao, geradores]
aliases: [Solução Iteradores Python]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Pipeline Preguiçoso em Lotes

```python
from __future__ import annotations

from collections.abc import Iterable, Iterator
from contextlib import contextmanager

class PedidoInvalido(ValueError):
    pass

def converter(linha: str) -> tuple[str, int]:
    partes = linha.strip().split(",")
    if len(partes) != 2 or not partes[0]:
        raise PedidoInvalido("formato inválido")
    try:
        valor = int(partes[1])
    except ValueError as erro:
        raise PedidoInvalido("valor não inteiro") from erro
    if valor < 0:
        raise PedidoInvalido("valor negativo")
    return partes[0], valor

def validos(linhas: Iterable[str], rejeitados: list[str]) -> Iterator[tuple[str, int]]:
    for linha in linhas:
        try:
            yield converter(linha)
        except PedidoInvalido:
            rejeitados.append(linha)

def lotes(itens: Iterable[tuple[str, int]], tamanho: int) -> Iterator[tuple[tuple[str, int], ...]]:
    if tamanho <= 0:
        raise ValueError("tamanho deve ser positivo")
    lote: list[tuple[str, int]] = []
    for item in itens:
        lote.append(item)
        if len(lote) == tamanho:
            yield tuple(lote)
            lote.clear()
    if lote:
        yield tuple(lote)

@contextmanager
def fonte(linhas: list[str], estado: dict[str, bool]):
    try:
        yield iter(linhas)
    finally:
        estado["fechada"] = True

if __name__ == "__main__":
    entrada = ["P1,1200", "ruim", "P2,800", "P3,2500"]
    estado = {"fechada": False}
    rejeitados: list[str] = []
    with fonte(entrada, estado) as linhas:
        saida = list(lotes(validos(linhas, rejeitados), 2))

    assert [len(lote) for lote in saida] == [2, 1]
    assert sum(valor for lote in saida for _, valor in lote) == 4500
    assert rejeitados == ["ruim"]
    assert estado["fechada"] is True
    print(f"lotes={len(saida)} validos=3 rejeitados=1 total_centavos=4500 fonte_fechada={estado['fechada']}")
```

A fonte poderia ser um arquivo real; o context manager em memória torna o contrato de fechamento observável sem depender do sistema de arquivos.

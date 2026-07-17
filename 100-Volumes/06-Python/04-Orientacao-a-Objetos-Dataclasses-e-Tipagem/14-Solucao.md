---
title: Solução — Domínio Imutável e Repositório Tipado
description: "Implementação de referência do laboratório."
tags: [python, solucao, dataclasses]
aliases: [Solução Objetos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Domínio Imutável e Repositório Tipado

```python
from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Generic, Literal, Protocol, TypeVar, runtime_checkable

Status = Literal["aprovado", "cancelado"]

@dataclass(frozen=True, slots=True)
class Dinheiro:
    centavos: int

    def __post_init__(self) -> None:
        if type(self.centavos) is not int or self.centavos < 0:
            raise ValueError("centavos inválidos")

@dataclass(frozen=True, slots=True)
class Pedido:
    pedido_id: str
    total: Dinheiro
    status: Status = "aprovado"

    def __post_init__(self) -> None:
        if not self.pedido_id:
            raise ValueError("pedido_id vazio")
        if self.status not in ("aprovado", "cancelado"):
            raise ValueError("status inválido")

    def cancelar(self) -> Pedido:
        if self.status == "cancelado":
            return self
        return replace(self, status="cancelado")

T = TypeVar("T")

@runtime_checkable
class Repositorio(Protocol[T]):
    def salvar(self, identificador: str, item: T) -> None: ...
    def obter(self, identificador: str) -> T | None: ...

class RepositorioMemoria(Generic[T]):
    def __init__(self) -> None:
        self._itens: dict[str, T] = {}

    def salvar(self, identificador: str, item: T) -> None:
        self._itens[identificador] = item

    def obter(self, identificador: str) -> T | None:
        return self._itens.get(identificador)

if __name__ == "__main__":
    repositorio: Repositorio[Pedido] = RepositorioMemoria()
    original = Pedido("P-1", Dinheiro(4500))
    repositorio.salvar(original.pedido_id, original)
    cancelado = original.cancelar()
    repositorio.salvar(cancelado.pedido_id, cancelado)
    atual = repositorio.obter("P-1")
    assert atual is not None
    assert original.status == "aprovado" and atual.status == "cancelado"
    assert isinstance(repositorio, Repositorio)
    print("original=aprovado atual=cancelado total_centavos=4500 imutavel=ok protocolo=ok")
```

`runtime_checkable` confirma apenas a presença estrutural dos membros em runtime; a compatibilidade completa das assinaturas pertence ao analisador estático.

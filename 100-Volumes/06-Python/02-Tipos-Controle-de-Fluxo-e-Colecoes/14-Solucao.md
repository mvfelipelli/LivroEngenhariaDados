---
title: Solução — Agregador Determinístico de Pedidos
description: "Implementação de referência do laboratório."
tags: [python, solucao, colecoes]
aliases: [Solução Coleções Python]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Agregador Determinístico de Pedidos

```python
from __future__ import annotations

from typing import Any

STATUS = {"aprovado", "cancelado"}

def validar(evento: dict[str, Any]) -> None:
    if not isinstance(evento.get("pedido_id"), str) or not evento["pedido_id"]:
        raise ValueError("pedido_id inválido")
    if not isinstance(evento.get("loja"), str) or not evento["loja"]:
        raise ValueError("loja inválida")
    if type(evento.get("versao")) is not int or evento["versao"] <= 0:
        raise ValueError("versão inválida")
    if evento.get("status") not in STATUS:
        raise ValueError("status inválido")
    if type(evento.get("valor_centavos")) is not int or evento["valor_centavos"] < 0:
        raise ValueError("valor inválido")

def agregar(eventos: list[dict[str, Any]]) -> list[dict[str, int | str]]:
    atuais: dict[str, dict[str, Any]] = {}
    for evento in eventos:
        validar(evento)
        identificador = evento["pedido_id"]
        anterior = atuais.get(identificador)
        if anterior is None or evento["versao"] > anterior["versao"]:
            atuais[identificador] = evento.copy()

    totais: dict[str, dict[str, int]] = {}
    for evento in atuais.values():
        if evento["status"] != "aprovado":
            continue
        loja = evento["loja"]
        acumulado = totais.setdefault(loja, {"quantidade": 0, "total_centavos": 0})
        acumulado["quantidade"] += 1
        acumulado["total_centavos"] += evento["valor_centavos"]

    return [
        {"loja": loja, **metricas}
        for loja, metricas in sorted(
            totais.items(),
            key=lambda item: (-item[1]["total_centavos"], item[0]),
        )
    ]

EVENTOS = [
    {"pedido_id": "P1", "loja": "SP", "versao": 1, "status": "aprovado", "valor_centavos": 1000},
    {"pedido_id": "P1", "loja": "SP", "versao": 2, "status": "aprovado", "valor_centavos": 1200},
    {"pedido_id": "P2", "loja": "RJ", "versao": 1, "status": "aprovado", "valor_centavos": 800},
    {"pedido_id": "P3", "loja": "SP", "versao": 1, "status": "aprovado", "valor_centavos": 2500},
    {"pedido_id": "P4", "loja": "RJ", "versao": 1, "status": "cancelado", "valor_centavos": 900},
]

if __name__ == "__main__":
    resultado = agregar(EVENTOS)
    assert resultado == agregar(list(reversed(EVENTOS)))
    assert sum(item["quantidade"] for item in resultado) == 3
    assert sum(item["total_centavos"] for item in resultado) == 4500
    print(resultado)
```

A cópia rasa ao guardar o evento impede que a substituição de chaves externas altere o registro selecionado. Como os valores são escalares, não há estrutura aninhada compartilhada.

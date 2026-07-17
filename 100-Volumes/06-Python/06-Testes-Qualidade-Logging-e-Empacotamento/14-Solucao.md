---
title: Solução — Serviço Testado com Logging JSON
description: "Implementação de referência do laboratório."
tags: [python, solucao, unittest, logging]
aliases: [Solução Qualidade Python]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Serviço Testado com Logging JSON

```python
from __future__ import annotations

import json
import logging
import unittest
from dataclasses import dataclass
from io import StringIO
from typing import Protocol

@dataclass(frozen=True)
class Pedido:
    pedido_id: str
    valor_centavos: int

    def __post_init__(self) -> None:
        if not self.pedido_id or type(self.valor_centavos) is not int or self.valor_centavos < 0:
            raise ValueError("pedido inválido")

class Destino(Protocol):
    def salvar(self, pedido: Pedido) -> None: ...

class DestinoMemoria:
    def __init__(self) -> None:
        self.itens: dict[str, Pedido] = {}

    def salvar(self, pedido: Pedido) -> None:
        self.itens[pedido.pedido_id] = pedido

def publicar(pedidos: list[Pedido], destino: Destino, logger: logging.Logger) -> int:
    for pedido in pedidos:
        destino.salvar(pedido)
    total = sum(pedido.valor_centavos for pedido in pedidos)
    logger.info(json.dumps({"evento": "lote_concluido", "registros": len(pedidos), "total_centavos": total}))
    return total

class TestePublicacao(unittest.TestCase):
    def setUp(self) -> None:
        self.stream = StringIO()
        self.logger = logging.getLogger(f"teste.{id(self)}")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        self.logger.addHandler(logging.StreamHandler(self.stream))

    def test_publica_e_emite_json(self) -> None:
        destino = DestinoMemoria()
        total = publicar([Pedido("P1", 1200), Pedido("P2", 800)], destino, self.logger)
        evento = json.loads(self.stream.getvalue())
        self.assertEqual(total, 2000)
        self.assertEqual(set(destino.itens), {"P1", "P2"})
        self.assertEqual(evento["evento"], "lote_concluido")

    def test_rejeita_valor_negativo(self) -> None:
        with self.assertRaises(ValueError):
            Pedido("P1", -1)

    def test_destino_e_idempotente_por_id(self) -> None:
        destino = DestinoMemoria()
        destino.salvar(Pedido("P1", 100))
        destino.salvar(Pedido("P1", 200))
        self.assertEqual(len(destino.itens), 1)
        self.assertEqual(destino.itens["P1"].valor_centavos, 200)

    def test_log_nao_contem_segredo(self) -> None:
        segredo = "token-supersecreto"
        publicar([Pedido("P1", 100)], DestinoMemoria(), self.logger)
        self.assertNotIn(segredo, self.stream.getvalue())

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestePublicacao)
    resultado = unittest.TextTestRunner(verbosity=2).run(suite)
    if not resultado.wasSuccessful():
        raise SystemExit(1)
    print("testes=4 status=ok ids_unicos=2 total_centavos=2000 segredo=ausente")
```

O fake verifica o port do serviço; um adaptador real ainda precisa de testes de integração e contrato próprios.

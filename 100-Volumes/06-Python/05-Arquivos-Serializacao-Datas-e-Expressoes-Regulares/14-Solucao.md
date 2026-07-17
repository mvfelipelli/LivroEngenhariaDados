---
title: Solução — JSONL para CSV Atômico
description: "Implementação de referência do laboratório."
tags: [python, solucao, jsonl, csv]
aliases: [Solução Serialização Python]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — JSONL para CSV Atômico

```python
from __future__ import annotations

import csv
import json
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ID = re.compile(r"^BR-[1-9]\d{0,9}$")

def normalizar(objeto: object) -> dict[str, str | int]:
    if not isinstance(objeto, dict):
        raise ValueError("evento não é objeto")
    pedido_id = objeto.get("pedido_id")
    valor = objeto.get("valor_centavos")
    instante_texto = objeto.get("instante")
    if not isinstance(pedido_id, str) or ID.fullmatch(pedido_id) is None:
        raise ValueError("pedido_id inválido")
    if type(valor) is not int or valor < 0:
        raise ValueError("valor inválido")
    if not isinstance(instante_texto, str):
        raise ValueError("instante inválido")
    instante = datetime.fromisoformat(instante_texto.replace("Z", "+00:00"))
    if instante.tzinfo is None:
        raise ValueError("instante sem timezone")
    utc = instante.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    return {"pedido_id": pedido_id, "instante_utc": utc, "valor_centavos": valor}

def converter(origem: Path, destino: Path) -> list[tuple[int, str]]:
    registros: list[dict[str, str | int]] = []
    rejeitados: list[tuple[int, str]] = []
    with origem.open(encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, 1):
            try:
                registros.append(normalizar(json.loads(linha)))
            except (json.JSONDecodeError, ValueError) as erro:
                rejeitados.append((numero, str(erro)))

    registros.sort(key=lambda item: (str(item["instante_utc"]), str(item["pedido_id"])))
    temporario = destino.with_suffix(destino.suffix + ".tmp")
    try:
        with temporario.open("w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.DictWriter(
                arquivo,
                fieldnames=["pedido_id", "instante_utc", "valor_centavos"],
                lineterminator="\n",
            )
            escritor.writeheader()
            escritor.writerows(registros)
        temporario.replace(destino)
    finally:
        temporario.unlink(missing_ok=True)
    return rejeitados

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as pasta:
        base = Path(pasta)
        origem, destino = base / "eventos.jsonl", base / "pedidos.csv"
        eventos = [
            {"pedido_id": "BR-2", "instante": "2026-07-17T10:00:00-03:00", "valor_centavos": 800},
            {"pedido_id": "BR-1", "instante": "2026-07-17T12:00:00Z", "valor_centavos": 1200},
            {"pedido_id": "BR-3", "instante": "2026-07-17T11:00:00-03:00", "valor_centavos": 2500},
        ]
        linhas = [json.dumps(item, ensure_ascii=False) for item in eventos] + ["{invalido"]
        origem.write_text("\n".join(linhas) + "\n", encoding="utf-8")
        rejeitados = converter(origem, destino)
        primeira = destino.read_bytes()
        assert converter(origem, destino) == rejeitados
        assert destino.read_bytes() == primeira
        assert len(rejeitados) == 1 and not destino.with_suffix(".csv.tmp").exists()
        assert primeira.count(b"\n") == 4
        print("registros=3 rejeitados=1 total_centavos=4500 utc=ok bytes_estaveis=ok temporario=ausente")
```

Em produção, a política pode falhar o lote acima de um limiar de rejeições e persistir a quarentena em destino protegido.

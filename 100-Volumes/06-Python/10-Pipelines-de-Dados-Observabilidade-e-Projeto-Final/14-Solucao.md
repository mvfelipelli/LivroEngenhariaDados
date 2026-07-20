---
title: Solução — Pipeline Incremental Observável
description: "Implementação de referência do projeto final."
tags: [python, solucao, pipelines, sqlite]
aliases: [Solução Projeto Final Python]
created: 2026-07-20
updated: 2026-07-20
---

# Solução — Pipeline Incremental Observável

```python
from __future__ import annotations

import csv
import json
import sqlite3
import tempfile
import uuid
from pathlib import Path

STATUS = {"recebido", "aprovado", "cancelado"}

def validar(linha: dict[str, str]) -> tuple[str, int, str, int]:
    pedido_id = linha["pedido_id"].strip()
    if not pedido_id:
        raise ValueError("pedido_id vazio")
    try:
        versao = int(linha["versao"])
        valor = int(linha["valor_centavos"])
    except ValueError as erro:
        raise ValueError("número inválido") from erro
    status = linha["status"]
    if versao <= 0 or status not in STATUS or valor < 0:
        raise ValueError("domínio inválido")
    return pedido_id, versao, status, valor

def executar(origem: Path, conexao: sqlite3.Connection) -> dict[str, int | str]:
    run_id = str(uuid.uuid4())
    checkpoint = conexao.execute("SELECT linha FROM checkpoint WHERE id = 1").fetchone()[0]
    metricas: dict[str, int | str] = {
        "evento": "pipeline_concluido",
        "run_id": run_id,
        "lidos": 0,
        "aceitos": 0,
        "rejeitados": 0,
    }
    with origem.open(encoding="utf-8", newline="") as arquivo, conexao:
        leitor = csv.DictReader(arquivo)
        esperado = ["pedido_id", "versao", "status", "valor_centavos"]
        if leitor.fieldnames != esperado:
            raise ValueError("cabeçalho inválido")
        for numero, linha in enumerate(leitor, start=2):
            if numero <= checkpoint:
                continue
            metricas["lidos"] = int(metricas["lidos"]) + 1
            try:
                pedido_id, versao, status, valor = validar(linha)
                conexao.execute(
                    "INSERT INTO pedido VALUES (?, ?, ?, ?) ON CONFLICT(pedido_id) DO UPDATE SET "
                    "versao=excluded.versao, status=excluded.status, valor_centavos=excluded.valor_centavos "
                    "WHERE excluded.versao > pedido.versao",
                    (pedido_id, versao, status, valor),
                )
                metricas["aceitos"] = int(metricas["aceitos"]) + 1
            except ValueError as erro:
                conexao.execute(
                    "INSERT OR REPLACE INTO quarentena(linha, motivo) VALUES (?, ?)",
                    (numero, str(erro)),
                )
                metricas["rejeitados"] = int(metricas["rejeitados"]) + 1
            conexao.execute("UPDATE checkpoint SET linha = ? WHERE id = 1", (numero,))
    assert metricas["lidos"] == int(metricas["aceitos"]) + int(metricas["rejeitados"])
    print(json.dumps(metricas, sort_keys=True))
    return metricas

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as pasta:
        base = Path(pasta)
        origem = base / "pedidos.csv"
        origem.write_text(
            "pedido_id,versao,status,valor_centavos\n"
            "P1,1,recebido,1000\n"
            "P1,2,aprovado,1200\n"
            "P2,1,aprovado,800\n"
            ",1,aprovado,99\n"
            "P3,1,aprovado,2500\n",
            encoding="utf-8",
        )
        conexao = sqlite3.connect(base / "pipeline.db")
        conexao.executescript(
            "CREATE TABLE pedido(pedido_id TEXT PRIMARY KEY, versao INTEGER, status TEXT, valor_centavos INTEGER);"
            "CREATE TABLE quarentena(linha INTEGER PRIMARY KEY, motivo TEXT);"
            "CREATE TABLE checkpoint(id INTEGER PRIMARY KEY, linha INTEGER);"
            "INSERT INTO checkpoint VALUES (1, 1);"
        )
        primeira = executar(origem, conexao)
        estado_1 = conexao.execute("SELECT * FROM pedido ORDER BY pedido_id").fetchall()
        segunda = executar(origem, conexao)
        estado_2 = conexao.execute("SELECT * FROM pedido ORDER BY pedido_id").fetchall()
        total = conexao.execute("SELECT SUM(valor_centavos) FROM pedido WHERE status='aprovado'").fetchone()[0]
        rejeitados = conexao.execute("SELECT COUNT(*) FROM quarentena").fetchone()[0]
        checkpoint = conexao.execute("SELECT linha FROM checkpoint WHERE id=1").fetchone()[0]
        conexao.close()
        assert (primeira["lidos"], primeira["aceitos"], primeira["rejeitados"]) == (5, 4, 1)
        assert segunda["lidos"] == 0 and estado_1 == estado_2
        assert (len(estado_2), total, rejeitados, checkpoint) == (3, 4500, 1, 6)
        print("pedidos=3 total_aprovado=4500 quarentena=1 checkpoint=6 idempotencia=ok reconciliacao=ok")
```

O checkpoint por linha serve ao arquivo append-only do laboratório. Em fontes mutáveis, prefira cursor ou watermark estável fornecido pelo sistema de origem.

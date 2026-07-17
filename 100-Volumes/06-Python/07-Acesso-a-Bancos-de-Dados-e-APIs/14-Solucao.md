---
title: Solução — API Paginada para SQLite
description: "Implementação de referência do laboratório."
tags: [python, solucao, http, sqlite]
aliases: [Solução Bancos APIs Python]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — API Paginada para SQLite

```python
from __future__ import annotations

import json
import sqlite3
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

PAGINAS = {
    "": {"itens": [{"id": "P1", "versao": 1, "preco": 1000}, {"id": "P2", "versao": 1, "preco": 800}], "proximo": "c2"},
    "c2": {"itens": [{"id": "P1", "versao": 2, "preco": 1200}, {"id": "P3", "versao": 1, "preco": 2500}], "proximo": None},
}

class Handler(BaseHTTPRequestHandler):
    chamadas = 0

    def do_GET(self) -> None:
        type(self).chamadas += 1
        cursor = parse_qs(urlparse(self.path).query).get("cursor", [""])[0]
        corpo = json.dumps(PAGINAS[cursor]).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def log_message(self, format: str, *args: object) -> None:
        pass

def buscar(base_url: str, cursor: str) -> dict:
    url = f"{base_url}/produtos?cursor={cursor}"
    with urlopen(Request(url, headers={"Accept": "application/json"}), timeout=2) as resposta:
        if resposta.headers.get_content_type() != "application/json":
            raise ValueError("Content-Type inválido")
        pagina = json.load(resposta)
    if not isinstance(pagina, dict) or not isinstance(pagina.get("itens"), list):
        raise ValueError("página inválida")
    return pagina

def sincronizar(conexao: sqlite3.Connection, base_url: str) -> None:
    cursor = ""
    vistos: set[str] = set()
    while True:
        if cursor in vistos:
            raise RuntimeError("cursor repetido")
        vistos.add(cursor)
        pagina = buscar(base_url, cursor)
        proximo = pagina.get("proximo")
        if proximo is not None and not isinstance(proximo, str):
            raise ValueError("próximo cursor inválido")
        with conexao:
            for item in pagina["itens"]:
                if not isinstance(item, dict):
                    raise ValueError("item inválido")
                produto_id, versao, preco = item.get("id"), item.get("versao"), item.get("preco")
                if not isinstance(produto_id, str) or type(versao) is not int or type(preco) is not int:
                    raise ValueError("tipos inválidos")
                conexao.execute(
                    "INSERT INTO produto VALUES (?, ?, ?) ON CONFLICT(id) DO UPDATE SET "
                    "versao=excluded.versao, preco=excluded.preco WHERE excluded.versao > produto.versao",
                    (produto_id, versao, preco),
                )
            conexao.execute("UPDATE checkpoint SET cursor = ? WHERE id = 1", (proximo,))
        if proximo is None:
            break
        cursor = proximo

if __name__ == "__main__":
    servidor = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=servidor.serve_forever, daemon=True)
    thread.start()
    try:
        with tempfile.TemporaryDirectory() as pasta:
            conexao = sqlite3.connect(Path(pasta) / "catalogo.db")
            conexao.executescript(
                "CREATE TABLE produto(id TEXT PRIMARY KEY, versao INTEGER, preco INTEGER);"
                "CREATE TABLE checkpoint(id INTEGER PRIMARY KEY, cursor TEXT);"
                "INSERT INTO checkpoint VALUES (1, NULL);"
            )
            base_url = f"http://127.0.0.1:{servidor.server_port}"
            sincronizar(conexao, base_url)
            sincronizar(conexao, base_url)
            quantidade, total = conexao.execute("SELECT COUNT(*), SUM(preco) FROM produto").fetchone()
            versao_p1 = conexao.execute("SELECT versao FROM produto WHERE id='P1'").fetchone()[0]
            assert (quantidade, total, versao_p1, Handler.chamadas) == (3, 4500, 2, 4)
            conexao.close()
            print("produtos=3 total_centavos=4500 p1_versao=2 paginas=4 idempotencia=ok")
    finally:
        servidor.shutdown()
        servidor.server_close()
        thread.join()
```

O servidor local elimina dependência externa e exercita HTTP real, parsing, transação e upsert no mesmo teste executável.

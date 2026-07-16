---
title: Solução — Diagnóstico de Serviço em Loopback
description: "Implementação validada do laboratório de redes."
tags: [linux, redes, laboratorio, solucao]
aliases: [Solução Laboratório Redes]
created: 2026-07-16
updated: 2026-07-16
---

# Solução — Diagnóstico de Serviço em Loopback

Salve como `diagnostico_rede.py`:

```python
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import socket
import threading


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        body = b"DataRetail OK"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass


server = ThreadingHTTPServer(("127.0.0.1", 0), HealthHandler)
port = server.server_address[1]
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    addresses = socket.getaddrinfo(
        "localhost", port, family=socket.AF_INET, type=socket.SOCK_STREAM
    )
    address = addresses[0][4][0]
    assert address.startswith("127.")

    with socket.create_connection((address, port), timeout=2) as client:
        request = (
            "GET /health HTTP/1.1\r\n"
            f"Host: localhost:{port}\r\n"
            "Connection: close\r\n\r\n"
        )
        client.sendall(request.encode("ascii"))
        chunks = []
        while chunk := client.recv(4096):
            chunks.append(chunk)

    response = b"".join(chunks)
    headers, body = response.split(b"\r\n\r\n", 1)
    status = int(headers.split(b"\r\n", 1)[0].split()[1])
    assert status == 200
    assert body == b"DataRetail OK"

    print("nome=localhost")
    print("familia=IPv4")
    print("endereco=127.0.0.1")
    print("tcp=conectado")
    print(f"http_status={status}")
    print(f"corpo={body.decode('ascii')}")
    print("camadas=ok")
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=2)
```

## Leitura da solução

`getaddrinfo` reproduz a resolução usada por aplicações. `create_connection` valida transporte. A requisição e a resposta verificam o protocolo HTTP e o conteúdo. Assertions transformam invariantes em falhas observáveis.

> [!tip]
> Loopback elimina roteadores e firewall de perímetro. Ele é adequado ao laboratório, mas não demonstra conectividade entre hosts.

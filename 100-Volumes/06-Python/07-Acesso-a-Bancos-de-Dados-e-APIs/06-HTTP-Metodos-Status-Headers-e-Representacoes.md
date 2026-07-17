---
title: HTTP, Métodos, Status, Headers e Representações
description: "Semântica do protocolo para clientes de dados."
tags: [python, http, api, rest]
aliases: [HTTP Python]
created: 2026-07-17
updated: 2026-07-17
---

# HTTP, Métodos, Status, Headers e Representações

GET recupera representação e deve ser safe; PUT substitui recurso e é idempotente; DELETE é idempotente quanto ao efeito desejado; POST geralmente cria ou aciona operação e pode exigir chave de idempotência.

Status 2xx indica sucesso, 3xx redirecionamento, 4xx problema da requisição e 5xx falha do servidor. O cliente precisa tratar códigos específicos: 401 autenticação, 403 autorização, 404 ausência, 409 conflito, 429 limite e 503 indisponibilidade.

Headers como `Accept`, `Content-Type`, `ETag`, `If-None-Match`, `Retry-After` e `Link` fazem parte do contrato. Verifique tipo de conteúdo antes de parsear.

HTTP não equivale a REST; APIs RPC também usam HTTP. O cliente deve seguir a semântica publicada, limitar tamanho de resposta e não confiar apenas no status para validar o payload.

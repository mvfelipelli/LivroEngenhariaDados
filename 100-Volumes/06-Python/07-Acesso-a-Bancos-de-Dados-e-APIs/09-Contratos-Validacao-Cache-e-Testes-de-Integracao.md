---
title: Contratos, Validação, Cache e Testes de Integração
description: "Compatibilidade e evidência nas fronteiras remotas."
tags: [python, contratos, cache, integracao]
aliases: [Contratos de API Python]
created: 2026-07-17
updated: 2026-07-17
---

# Contratos, Validação, Cache e Testes de Integração

Valide status, Content-Type, tamanho, sintaxe, estrutura e domínio antes de persistir. Mudança aditiva costuma ser compatível quando o cliente ignora campos desconhecidos; remoção ou mudança de tipo exige versão e migração.

ETag com `If-None-Match` evita transferir representação inalterada. Cache deve obedecer `Cache-Control`, variar por autenticação quando necessário e não armazenar conteúdo sensível indevidamente.

Testes unitários exercitam parsing com respostas gravadas e sanitizadas. Servidor fake local testa HTTP e paginação. Teste de contrato verifica schema. Integração contra sandbox confirma autenticação, TLS e comportamento real.

Não use produção como única suíte. Dados de teste precisam de cleanup e namespace isolado. Monitore taxa de sucesso, latência, bytes, páginas, retries, throttling, rejeições e atraso do watermark.

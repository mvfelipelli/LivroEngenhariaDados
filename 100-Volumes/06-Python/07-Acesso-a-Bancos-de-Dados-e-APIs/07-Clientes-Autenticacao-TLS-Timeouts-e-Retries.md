---
title: Clientes, Autenticação, TLS, Timeouts e Retries
description: "Configuração segura e resiliente do cliente HTTP."
tags: [python, http-client, autenticacao, tls]
aliases: [Cliente HTTP Python]
created: 2026-07-17
updated: 2026-07-17
---

# Clientes, Autenticação, TLS, Timeouts e Retries

Um cliente centraliza base URL, headers, autenticação, timeout, parsing e tradução de erros. Credenciais vêm de secret store e nunca entram em URL ou log.

TLS verifica confidencialidade e identidade; não desative validação de certificado para “corrigir” ambientes. Configure autoridades confiáveis e rotação.

Timeout não deve ser infinito. Bibliotecas distinguem conexão, leitura, escrita e pool; defina também deadline total do workflow.

Retry automático considera método, status, exceção e idempotência. Respeite `Retry-After`, aplique backoff com jitter e limite tentativas. Uma desconexão após POST pode ocorrer depois do efeito remoto; use idempotency key ou reconciliação antes de repetir.

Redirecionamentos entre hosts podem vazar Authorization se tratados incorretamente. Restrinja destinos e versões de protocolo conforme o contrato.

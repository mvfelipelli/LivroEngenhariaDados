---
title: Pooling, Lotes, Timeouts, Retries e Observabilidade
description: "Gestão de recursos e falhas transitórias no banco."
tags: [python, pooling, lotes, retries]
aliases: [Resiliência de Banco Python]
created: 2026-07-17
updated: 2026-07-17
---

# Pooling, Lotes, Timeouts, Retries e Observabilidade

Abrir conexão custa autenticação e recursos. Pools reutilizam conexões, mas precisam de limite, timeout de aquisição, validação e descarte de conexões quebradas.

`executemany` reduz round trips, embora drivers possam oferecer caminhos de bulk load superiores. Escolha lote por medição: muito pequeno aumenta overhead; muito grande amplia locks, rollback e memória.

Retries se aplicam somente a falhas transitórias e operações seguras. Use tentativas limitadas, exponential backoff, jitter e orçamento total. Deadlocks podem ser reexecutáveis; erro de constraint por dado inválido, não.

Observe duração de aquisição, tempo de query, linhas lidas/escritas, commits, rollbacks, retries e saturação do pool. Logs usam nome lógico da operação e fingerprint, nunca parâmetros sensíveis.

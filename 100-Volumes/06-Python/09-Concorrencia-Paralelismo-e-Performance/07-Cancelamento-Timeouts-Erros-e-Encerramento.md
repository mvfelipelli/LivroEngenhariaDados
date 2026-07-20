---
title: Cancelamento, Timeouts, Erros e Encerramento
description: "Finalização previsível sob falhas."
tags: [python, cancelamento, timeout, erros]
aliases: [Cancelamento Asyncio]
created: 2026-07-17
updated: 2026-07-17
---

# Cancelamento, Timeouts, Erros e Encerramento

Cancelamento é parte do contrato. `CancelledError` deve normalmente ser repropagado após limpeza; suprimi-lo faz o encerramento parecer travado.

```python
async with asyncio.timeout(10):
    await sincronizar()
```

Timeout converte espera excessiva em falha controlada. Prefira deadline do workflow a timeouts independentes que podem multiplicar o orçamento.

Ao cancelar, pare produtores, sinalize consumidores, aguarde tarefas, finalize itens em voo conforme a política e feche recursos. `asyncio.shield` protege uma await específica do cancelamento externo e deve ser raro, por exemplo para finalizar commit curto já iniciado.

Retries permanecem limitados e idempotentes. Exceções concorrentes podem chegar como ExceptionGroup; trate classes recuperáveis sem esconder falhas independentes.

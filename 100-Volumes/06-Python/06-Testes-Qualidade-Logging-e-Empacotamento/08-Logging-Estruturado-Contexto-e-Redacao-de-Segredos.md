---
title: Logging Estruturado, Contexto e Redação de Segredos
description: "Eventos operacionais consultáveis e seguros."
tags: [python, logging, observabilidade, seguranca]
aliases: [Logging Python]
created: 2026-07-17
updated: 2026-07-17
---

# Logging Estruturado, Contexto e Redação de Segredos

Logs registram eventos discretos. Métricas agregam séries; traces conectam operações. Uma linha estruturada deve conter timestamp, nível, evento e contexto estável.

```python
import logging

logger = logging.getLogger(__name__)
logger.info("lote_concluido", extra={"lote_id": "L-10", "registros": 500})
```

Bibliotecas não configuram handlers globais; aplicações configuram formato e destino. Use parâmetros do logger para evitar interpolação quando o nível está desativado.

Não registre senha, token, DSN completo, payload pessoal ou stack trace para erro esperado. A redação deve ocorrer antes da emissão e usar lista permitida de campos. IDs de correlação ligam etapas; cardinalidade excessiva em labels de métricas deve ser evitada.

`logger.exception` dentro de `except` inclui traceback. Cada falha deve ser registrada uma vez na fronteira responsável, evitando duplicação em todas as camadas.

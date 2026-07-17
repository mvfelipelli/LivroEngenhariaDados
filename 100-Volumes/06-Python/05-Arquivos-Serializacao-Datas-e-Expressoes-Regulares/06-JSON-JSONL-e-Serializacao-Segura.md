---
title: JSON, JSONL e Serialização Segura
description: "Formatos de intercâmbio e validação explícita."
tags: [python, json, jsonl, serializacao]
aliases: [JSON em Python]
created: 2026-07-17
updated: 2026-07-17
---

# JSON, JSONL e Serialização Segura

JSON representa objeto, array, string, número, booleano e null. Não possui datetime, bytes nem Decimal nativos.

```python
import json

evento = json.loads(linha)
saida = json.dumps(evento, ensure_ascii=False, sort_keys=True)
```

JSONL armazena um valor JSON por linha e facilita streaming, particionamento e quarentena localizada. Uma quebra de linha dentro de string deve estar escapada.

Valide estrutura após parsing. `json.loads` aceita números grandes como int, mas floats mantêm limitações binárias; `parse_float=Decimal` pode preservar decimais na leitura, embora a escrita exija conversão definida.

Nunca desserialize dados não confiáveis com `pickle`: o formato pode executar código. Use formatos de dados e schemas explícitos para fronteiras externas.

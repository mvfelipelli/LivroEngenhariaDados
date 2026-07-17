---
title: JSON, Modelagem, Validação, Nulos e Tipos
description: "Uso disciplinado de documentos dentro do banco relacional."
tags: [sql, json, validacao, tipos]
aliases: [Modelagem JSON em SQL]
created: 2026-07-17
updated: 2026-07-17
---

# JSON, Modelagem, Validação, Nulos e Tipos

JSON representa objetos, arrays, strings, números, booleanos e `null`. Um caminho ausente difere de um caminho presente com valor `null`; converter ambos indiscriminadamente perde informação.

```json
{
  "schema_version": 2,
  "canal": "mobile",
  "cupom": null,
  "itens": [{"sku": "A-10", "quantidade": 2}]
}
```

## Quando usar

- atributos esparsos e específicos por categoria;
- envelope de evento preservado;
- integração externa com evolução controlada;
- metadados pouco consultados.

Campos usados em chaves, joins, integridade e filtros frequentes devem ser colunas tipadas. Valide JSON sintático e semanticamente: versão, campos obrigatórios, tipos, limites e valores permitidos.

```sql
-- SQLite
CREATE TABLE eventos (
    evento_id INTEGER PRIMARY KEY,
    payload TEXT NOT NULL CHECK (json_valid(payload))
);
```

> [!warning]
> Guardar tudo em JSON desloca constraints para código, dificulta lineage e torna erros de tipo tardios.

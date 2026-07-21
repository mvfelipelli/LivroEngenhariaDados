---
title: Data Source API e Opções de Leitura
description: "Interface uniforme para fontes batch e streaming."
tags: [apache-spark, data-source-api, leitura]
aliases: [Data Source API]
created: 2026-07-20
updated: 2026-07-20
---

# Data Source API e Opções de Leitura

`DataFrameReader` combina formato, schema, opções e caminho. Opções são específicas do conector e devem ser tratadas como configuração versionada.

```python
pedidos = (spark.read.format("json")
    .schema(schema_pedidos)
    .option("mode", "PERMISSIVE")
    .option("columnNameOfCorruptRecord", "_registro_corrompido")
    .load(entrada))
```

Data Source V2 amplia interfaces para catálogos, pushdown, escrita e streaming. A aplicação deve validar schema efetivo, arquivos encontrados e registros corrompidos. Globs vazios e caminhos errados não podem ser confundidos com lote legítimo sem dados.

---
title: Schemas Explícitos, Inferência e Nulabilidade
description: "Contratos de dados, tipos e validação na leitura."
tags: [apache-spark, schema, qualidade-de-dados]
aliases: [Schema Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Schemas Explícitos, Inferência e Nulabilidade

Inferência lê amostras ou metadados e pode produzir tipos diferentes entre arquivos. Em produção, schema explícito documenta contrato, evita leitura adicional e torna falhas previsíveis.

```python
from pyspark.sql.types import LongType, StringType, StructField, StructType

schema = StructType([
    StructField("pedido_id", StringType(), False),
    StructField("valor_centavos", LongType(), False),
])
```

`nullable=False` expressa intenção, mas não substitui validação em toda fonte ou transformação. Mudanças compatíveis incluem adicionar coluna opcional; trocar significado ou estreitar tipo exige migração e versionamento.

> [!warning]
> `cast` inválido pode produzir `null` em vez de exceção, conforme configuração ANSI. Monitore perdas de conversão.

---
title: Views, Catálogos, Tabelas e Spark SQL
description: "Resolução de nomes e ciclo de vida dos objetos SQL."
tags: [apache-spark, catalogo, views]
aliases: [Catálogo Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Views, Catálogos, Tabelas e Spark SQL

Uma temporary view pertence à sessão; global temporary view vive no banco reservado `global_temp` durante a aplicação. Tabelas registradas persistem metadados no catálogo e podem gerenciar ou apenas referenciar arquivos.

```python
pedidos.createOrReplaceTempView("pedidos_validos")
resumo = spark.sql("""
    SELECT loja_id, COUNT(*) AS pedidos
    FROM pedidos_validos
    GROUP BY loja_id
""")
```

Qualifique catálogo, namespace e tabela em produção. Evite depender de database corrente ou de view criada implicitamente em notebook. O contrato inclui nome, schema, proprietário e ciclo de vida.

---
title: Contratos, Schema e Qualidade de Dados
description: "Invariantes técnicos e semânticos na fronteira do pipeline."
tags: [apache-spark, data-contracts, qualidade-de-dados]
aliases: [Contratos de Dados Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Contratos, Schema e Qualidade de Dados

Contrato define schema, significado, granularidade, chaves, SLA, classificação e política de evolução. Qualidade mede conformidade em dimensões como completude, validade, unicidade, consistência e atualidade.

```python
metricas = df.agg(
    F.count("*").alias("linhas"),
    F.sum(F.col("pedido_id").isNull().cast("int")).alias("ids_nulos"),
    F.countDistinct("pedido_id").alias("ids_distintos"),
)
```

Falhar, colocar em quarentena ou apenas alertar depende do impacto. Limites absolutos devem conviver com baseline histórico para detectar mudanças sutis. Toda exclusão precisa ser contabilizada, amostrada e rastreável.

Evolução compatível não altera retroativamente o significado de um campo existente.

---
title: Arquitetura Testável e Funções de Transformação
description: "Separação entre regras, I/O e inicialização Spark."
tags: [apache-spark, testes, arquitetura]
aliases: [Arquitetura Testável Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Arquitetura Testável e Funções de Transformação

Funções devem receber DataFrames e configuração explícita, retornando DataFrames sem iniciar sessão, ler arquivos ou gravar destinos. O entrypoint coordena infraestrutura.

```python
from pyspark.sql import DataFrame, functions as F

def pedidos_validos(df: DataFrame) -> DataFrame:
    return df.where(
        F.col("pedido_id").isNotNull()
        & (F.col("valor_centavos") >= 0)
    )
```

Essa fronteira permite testar regras em memória, reutilizar planos e trocar conectores. Relógio, data de referência e identificador de execução devem entrar como parâmetros, evitando funções não determinísticas ocultas.

I/O, publicação, métricas e retries pertencem a adapters; regras de negócio permanecem declarativas e pequenas.

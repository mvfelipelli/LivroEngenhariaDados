---
title: Ambiente Local e Primeira Aplicação
description: "Instalação e validação de uma aplicação PySpark."
tags: [pyspark, ambiente, instalacao]
aliases: [Primeira Aplicação Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Ambiente Local e Primeira Aplicação

Confirme Java, Python e `pyspark` antes do job. Fixe versões no projeto.

```bash
java -version
python --version
python -m pip install "pyspark==3.5.3"
```

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[2]").appName("smoke").getOrCreate()
try:
    assert spark.range(10).count() == 10
finally:
    spark.stop()
```

No Windows, `JAVA_HOME` aponta para a raiz do JDK, não para `bin`. Avisos Hadoop nativos não invalidam operações locais em memória; erros de worker exigem conferir permissões e a matriz Java–Python–Spark.

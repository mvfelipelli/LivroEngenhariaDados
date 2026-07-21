---
title: Introdução ao Spark SQL
description: "Relação entre SQL, DataFrames e execução distribuída."
tags: [apache-spark, spark-sql, introducao]
aliases: [Introdução Spark SQL]
created: 2026-07-20
updated: 2026-07-20
---

# Introdução

Spark SQL e DataFrame API produzem planos equivalentes quando expressam a mesma lógica. SQL favorece legibilidade relacional; a API facilita composição programática. Ambos passam pelo Catalyst.

```mermaid
flowchart LR
    SQL["SQL"] --> C["Catalyst"]
    DF["DataFrame API"] --> C
    C --> P["Plano físico"]
    P --> E["Execução"]
```

O custo dominante costuma surgir em joins, agregações e ordenações, pois redistribuem dados. Antes de executar, estime linhas por chave e valide a granularidade de cada relação.

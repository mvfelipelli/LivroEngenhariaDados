---
title: Introdução aos DataFrames
description: "Dados distribuídos com estrutura declarada."
tags: [apache-spark, dataframe, introducao]
aliases: [Introdução DataFrame Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Introdução

Um DataFrame representa uma relação distribuída com colunas nomeadas e tipos conhecidos. Ao usar expressões, o programa informa **o que** calcular; o Spark escolhe **como** executar.

```mermaid
flowchart LR
    API["DataFrame API"] --> LP["Plano lógico"]
    LP --> OP["Plano otimizado"]
    OP --> PP["Plano físico"]
    PP --> EX["Execução distribuída"]
```

Essa separação permite projeção e filtros antecipados, escolha de joins e geração de código. A vantagem diminui quando a lógica é escondida em funções opacas.

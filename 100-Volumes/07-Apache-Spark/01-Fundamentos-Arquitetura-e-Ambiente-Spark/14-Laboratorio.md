---
title: Laboratório — Primeira Aplicação PySpark Observável
description: "Execução local, inspeção de partições e validação."
tags: [pyspark, laboratorio, arquitetura]
aliases: [Laboratório Fundamentos Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Primeira Aplicação PySpark Observável

## Objetivo

Executar uma aplicação local, observar lazy evaluation e validar uma agregação sem coletar o conjunto integral.

## Pré-requisitos

- Java compatível com Spark 3.5;
- Python suportado e `pyspark==3.5.3`;
- ao menos 1 GB de memória.

## Ambiente

Crie `primeiro_job.py`. No Windows, confirme `JAVA_HOME` na raiz do JDK. Use `local[2]`.

## Passos

1. Crie uma sessão `dataretail-primeiro-job`.
2. Gere 100 mil IDs com `spark.range` e quatro partições.
3. Derive `loja_id = id % 10` e `valor_centavos = (id % 5000) + 100`.
4. Filtre IDs pares e imprima o plano formatado.
5. Agregue contagem e soma por loja.
6. Valide total de 50 mil pedidos.
7. Valide que a agregação contém cinco lojas.
8. Como extensão, grave em Parquet se o Windows possuir `HADOOP_HOME` configurado.
9. Encerre a sessão em `finally`.

## Validação

```bash
python primeiro_job.py
```

A saída deve conter `VALIDACAO_OK total=50000 lojas=5`. Duas execuções devem produzir o mesmo resultado lógico. A validação mínima não depende das ferramentas Hadoop nativas do Windows.

## Conclusão

O laboratório conecta código, plano, partições, ação e contrato de saída.

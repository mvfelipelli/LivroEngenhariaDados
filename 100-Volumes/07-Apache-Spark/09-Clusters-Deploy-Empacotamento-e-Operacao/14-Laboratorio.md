---
title: Laboratório — Aplicação Empacotável e Configurável
description: "Contrato de CLI, SparkSession externa e smoke test."
tags: [apache-spark, spark-submit, laboratorio]
aliases: [Laboratório Operação Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Laboratório — Aplicação Empacotável e Configurável

## Objetivo

Construir uma aplicação submetível sem master ou recursos embutidos.

## Pré-requisitos

- PySpark configurado;
- terminal com `spark-submit`.

## Ambiente

Crie pacote `dataretail_spark`, módulo `job.py` e entrypoint `app.py`.

## Passos

1. Defina CLI com `--data-negocio` e `--linhas`.
2. Crie `SparkSession` apenas com nome e timezone.
3. Gere dados com `spark.range(linhas)`.
4. Execute transformação importada do pacote.
5. Registre versão Spark e configuração não sensível.
6. Valide contagem e imprima contrato de saída.
7. Compacte o pacote em ZIP e submeta com `--py-files`.

## Validação

```bash
spark-submit --master local[2] --py-files dist/dataretail_spark.zip app.py --data-negocio 2026-07-20 --linhas 10000
```

A saída deve conter `VALIDACAO_OK data=2026-07-20 linhas=10000`.

## Conclusão

O laboratório separa artefato, configuração Spark e parâmetros de negócio.

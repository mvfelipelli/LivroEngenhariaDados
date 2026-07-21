---
title: Perguntas de Entrevista — I/O no Spark
description: "Questões comentadas sobre fontes e formatos."
tags: [apache-spark, io, entrevista]
aliases: [Entrevista I/O Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## Por que Parquet é adequado a analytics?

Armazena por coluna, preserva schema e estatísticas, comprime bem e permite pruning e pushdown.

## `partitionBy` e `repartition` são iguais?

Não. O primeiro define layout físico na escrita; o segundo redistribui partições de execução.

## Por que muitos arquivos pequenos prejudicam o Spark?

Listagem, abertura, metadados e agendamento dominam o trabalho útil.

## `overwrite` garante atomicidade?

Não. A garantia depende do commit protocol, sistema de arquivos e formato de tabela.

## Como paralelizar JDBC com segurança?

Escolher coluna equilibrada, limites corretos e número de conexões aceito pelo banco.

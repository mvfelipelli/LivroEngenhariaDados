---
title: Gabarito — I/O e Formatos
description: "Respostas dos exercícios do módulo."
tags: [apache-spark, io, gabarito]
aliases: [Gabarito I/O Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Gabarito

1. Schema, delimiter, header, quote/escape, encoding, modo e coluna de corrompido explícitos.
2. Parquet para consumo analítico; JSON/CSV para intercâmbio quando exigido.
3. Eliminam, respectivamente, colunas, blocos/linhas na fonte e diretórios físicos.
4. `numPartitions=8`, coluna equilibrada, limites reais e fetch size validado.
5. Repetição pode apagar escopo indevido ou deixar estado parcial; falta unidade lógica e commit.
6. Data e, se cardinalidade/volume justificarem, região como nível adicional.
7. Contagem, percentis de tamanho, bytes médios e arquivos por partição.
8. Escrever versão temporária, validar manifesto e trocar referência publicada de modo condicional.

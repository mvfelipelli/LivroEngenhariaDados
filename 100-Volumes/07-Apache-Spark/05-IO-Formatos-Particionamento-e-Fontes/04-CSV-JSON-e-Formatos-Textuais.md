---
title: CSV, JSON e Formatos Textuais
description: "Parsing, schemas e qualidade na ingestão de texto."
tags: [apache-spark, csv, json]
aliases: [Formatos Textuais Spark]
created: 2026-07-20
updated: 2026-07-20
---

# CSV, JSON e Formatos Textuais

CSV não carrega tipos nem uma especificação única de dialeto. Delimitador, quote, escape, encoding, cabeçalho, locale e multiline precisam ser definidos. JSON preserva estrutura, mas exige atenção a records por linha e campos aninhados.

Modos `PERMISSIVE`, `DROPMALFORMED` e `FAILFAST` definem reação a registros ruins. Descartar silenciosamente compromete reconciliação; prefira preservar conteúdo corrompido e medir quarentena.

> [!warning]
> Inferência pode interpretar um identificador com zeros à esquerda como número. Schema explícito preserva semântica.

Texto é adequado para intercâmbio e inspeção, mas custa mais CPU e bytes que formatos binários colunares.

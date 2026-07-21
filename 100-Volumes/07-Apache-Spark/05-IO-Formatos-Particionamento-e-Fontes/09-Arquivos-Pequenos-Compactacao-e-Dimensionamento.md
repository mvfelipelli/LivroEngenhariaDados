---
title: Arquivos Pequenos, Compactação e Dimensionamento
description: "Controle da quantidade e do tamanho dos arquivos."
tags: [apache-spark, small-files, compactacao]
aliases: [Problema de Arquivos Pequenos]
created: 2026-07-20
updated: 2026-07-20
---

# Arquivos Pequenos, Compactação e Dimensionamento

Cada arquivo exige listagem, metadados, abertura e planejamento. Milhões de arquivos de poucos quilobytes consomem mais tempo administrativo que leitura útil.

Quantidade de arquivos de saída se relaciona às partições no momento da escrita, multiplicadas pelo layout físico. `coalesce` reduz sem redistribuição ampla; `repartition` equilibra com shuffle. `maxRecordsPerFile` limita arquivos grandes, mas não consolida pequenos.

Compactação lê vários arquivos e publica menos arquivos maiores, preservando partições lógicas. Deve ser idempotente, isolada de escritores concorrentes e acompanhada por manifesto e métricas de bytes/arquivo.

Não existe tamanho universal; meça throughput, paralelismo e características do armazenamento.

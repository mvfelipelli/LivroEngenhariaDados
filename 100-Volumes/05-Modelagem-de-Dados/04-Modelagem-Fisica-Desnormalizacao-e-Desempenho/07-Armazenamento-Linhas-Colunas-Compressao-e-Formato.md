---
title: Armazenamento em Linhas e Colunas, Compressão e Formato
description: "Layout físico conforme o padrão de leitura e escrita."
tags: [row-store, column-store, compressao, formatos]
aliases: [Layout de Armazenamento]
created: 2026-07-17
updated: 2026-07-17
---

# Armazenamento em Linhas e Colunas, Compressão e Formato

Row stores mantêm atributos da tupla próximos e favorecem escrita pontual e leitura de registros completos. Column stores agrupam valores por coluna, favorecendo projeções, agregações, vetorização e compressão.

| Workload | Layout provável |
|---|---|
| transação por chave | linhas |
| scan de poucas colunas | colunas |
| atualização frequente | linhas |
| analytics append-only | colunas |

Compressão explora repetição, ordem e encoding. Ordenar por colunas correlacionadas melhora compressão e pruning, mas o benefício depende das consultas.

Em data lakes, tamanho de arquivo, row groups, estatísticas e schema embutido afetam desempenho. Muitos arquivos pequenos aumentam planejamento e chamadas ao storage.

> [!tip]
> Modele o layout junto com tamanho médio, cardinalidade, taxa de mudança e colunas consultadas.

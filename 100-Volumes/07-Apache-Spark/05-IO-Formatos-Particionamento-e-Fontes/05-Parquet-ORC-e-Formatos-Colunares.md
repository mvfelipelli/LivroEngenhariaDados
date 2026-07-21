---
title: Parquet, ORC e Formatos Colunares
description: "Armazenamento analítico, compressão e pushdown."
tags: [apache-spark, parquet, orc]
aliases: [Formatos Colunares Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Parquet, ORC e Formatos Colunares

Parquet e ORC armazenam valores por coluna em grupos, com schema, estatísticas e compressão. Consultas que leem poucas colunas evitam carregar o restante; filtros compatíveis podem eliminar grupos pela estatística.

Column pruning reduz colunas; predicate pushdown leva filtros à fonte; partition pruning elimina diretórios. São mecanismos distintos e devem ser verificados no plano.

Compressões como Snappy favorecem velocidade; Zstandard tende a reduzir mais bytes com CPU adicional. A escolha depende de custo de armazenamento, rede e SLA.

Evolução de schema deve ser deliberada. Mesclar schemas de muitos arquivos adiciona custo e pode esconder produtores inconsistentes.

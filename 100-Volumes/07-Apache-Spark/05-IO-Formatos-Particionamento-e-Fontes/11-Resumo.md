---
title: Resumo — I/O e Formatos
description: "Síntese do contrato físico de dados."
tags: [apache-spark, io, resumo]
aliases: [Resumo I/O Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Resumo

- Data Source API unifica configuração de leitura e escrita.
- Schemas explícitos protegem ingestões textuais.
- Parquet e ORC habilitam leitura colunar e pushdown.
- JDBC precisa respeitar capacidade do sistema fonte.
- Modo de escrita não equivale a transação ou idempotência.
- Particionamento físico deve acompanhar filtros e cardinalidade.
- Arquivos pequenos elevam custo de metadados e planejamento.
- Publicação requer reconciliação e fronteira de commit.

O próximo módulo examina shuffles, memória e otimização da execução.

---
title: Data Warehouse, Data Lake e Lakehouse
description: "Modelos de armazenamento, processamento e consumo analítico."
tags: [data-warehouse, data-lake, lakehouse]
aliases: [Warehouse Lake Lakehouse]
created: 2026-07-21
updated: 2026-07-21
---

# Data Warehouse, Data Lake e Lakehouse

Data Warehouse integra dados estruturados para análise governada, geralmente com schema e engine acoplados. Data Lake armazena objetos em formatos abertos com flexibilidade, mas exige disciplina para evitar dados opacos. Lakehouse adiciona metadados transacionais e gestão de tabelas sobre armazenamento de objetos.

| Critério | Warehouse | Lake | Lakehouse |
|---|---|---|---|
| Foco | Analytics governado | Armazenamento flexível | Tabelas abertas no Lake |
| Schema | Forte | Variável | Gerenciado por tabela |
| Transações | Nativas | Não por arquivo | Pelo formato de tabela |

Os estilos podem coexistir. A escolha depende de consumidores, operações, habilidades e custo total, não de uma promessa universal de unificação.

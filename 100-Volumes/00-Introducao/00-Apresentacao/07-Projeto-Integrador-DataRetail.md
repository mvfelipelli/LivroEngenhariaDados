---
title: Projeto Integrador DataRetail
description: "Empresa fictícia e continuidade prática da formação."
tags: [dataretail, projeto-integrador, academia]
aliases: [DataRetail S.A.]
created: 2026-07-21
updated: 2026-07-21
---

# Projeto Integrador DataRetail

A DataRetail S.A. é uma varejista fictícia com lojas, e-commerce, clientes, pedidos, estoque, pagamentos e logística. O cenário fornece continuidade sem depender de dados empresariais reais.

Ao longo dos volumes, a empresa evolui de arquivos e banco transacional para pipelines, Lakehouse, consumo analítico, qualidade e observabilidade.

```mermaid
flowchart LR
    ERP["ERP"] --> DP["Plataforma de dados"]
    CRM["CRM"] --> DP
    WEB["E-commerce"] --> DP
    IOT["Eventos"] --> DP
    DP --> BI["Analytics"]
    DP --> ML["Ciência de Dados"]
    DP --> OP["Operação"]
```

Cada estudo de caso deve declarar requisito, decisão, trade-off e validação. A empresa é um fio pedagógico, não uma desculpa para exemplos irreais.

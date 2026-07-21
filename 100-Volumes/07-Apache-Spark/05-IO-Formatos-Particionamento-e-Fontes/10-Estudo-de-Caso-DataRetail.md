---
title: Estudo de Caso — Camada Curada da DataRetail
description: "Conversão de eventos JSON em dados colunares particionados."
tags: [apache-spark, io, dataretail]
aliases: [Caso DataRetail I/O]
created: 2026-07-20
updated: 2026-07-20
---

# Estudo de Caso — Camada Curada

A DataRetail recebe JSON por hora e publica pedidos em Parquet. O schema explícito captura registros corrompidos; dados válidos são normalizados e particionados por `data_negocio`, enquanto quarentena preserva payload e motivo.

```mermaid
flowchart LR
    J["JSON horário"] --> V["Schema e validação"]
    V --> Q["Quarentena"]
    V --> R["Repartition por data"]
    R --> P["Parquet curado"]
    P --> C["Compactação"]
```

Cada lote grava em área temporária, valida contagem e soma em centavos, e só então publica. Uma rotina compacta partições fechadas. Métricas incluem arquivos, bytes médios, registros ruins e tempo de listagem.

---
title: Modelagem de Dados
description: "Representação de domínios, relações, histórico e produtos analíticos."
tags: [modelagem-de-dados, engenharia-de-dados, volume-05]
aliases: [Volume Modelagem de Dados]
type: volume
status: em-desenvolvimento
created: 2026-07-17
updated: 2026-07-17
---

# Volume 05 — Modelagem de Dados

Este volume desenvolve a capacidade de transformar linguagem de negócio em modelos conceituais, lógicos, físicos e analíticos governados.

## Módulos

1. [[01-Fundamentos-e-Niveis-de-Modelagem/README|Fundamentos e Níveis de Modelagem]] — concluído.
2. [[02-Modelagem-Conceitual-e-Entidade-Relacionamento/README|Modelagem Conceitual e Entidade-Relacionamento]] — concluído.
3. [[03-Modelagem-Logica-Relacional-e-Normalizacao/README|Modelagem Lógica Relacional e Normalização]] — concluído.
4. [[04-Modelagem-Fisica-Desnormalizacao-e-Desempenho/README|Modelagem Física, Desnormalização e Desempenho]] — concluído.
5. [[05-Modelagem-Dimensional-Fatos-e-Dimensoes/README|Modelagem Dimensional, Fatos e Dimensões]] — concluído.
6. [[06-Historico-Dimensional-SCD-Snapshots-e-Bridges/README|Histórico Dimensional, SCD, Snapshots e Bridges]] — concluído.
7. Data Vault 2.0 e Integração Histórica — planejado.
8. Modelagem para Data Lake, Lakehouse e Produtos de Dados — planejado.

```mermaid
flowchart LR
    N["Necessidade do negócio"] --> C["Modelo conceitual"]
    C --> L["Modelo lógico"]
    L --> F["Modelo físico"]
    F --> P["Produto operacional ou analítico"]
```

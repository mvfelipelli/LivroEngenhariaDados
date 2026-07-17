---
title: Introdução à Evolução de Schema
description: "Por que estruturas persistentes precisam mudar sem quebrar consumidores."
tags: [sql, schema-evolution, introducao]
aliases: [Introdução Evolução de Schema]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

Schemas codificam contratos entre produtores, consumidores e o banco. Renomear uma coluna ou estreitar um tipo afeta aplicações, consultas, views, cargas e réplicas.

```mermaid
flowchart TD
    D["Mudança de domínio"] --> A["Análise de dependências"]
    A --> P["Plano compatível"]
    P --> X["Execução"]
    X --> V["Validação"]
    V --> O["Observação e limpeza"]
```

Uma sentença rápida em desenvolvimento pode bloquear uma tabela grande ou validar milhões de linhas em produção. O plano deve distinguir mudança de catálogo, scan, reescrita e construção de índice.

Expand-contract separa a mudança incompatível em fases compatíveis. Durante a transição, duas versões da aplicação podem coexistir.

> [!warning]
> DDL é frequentemente transacional, mas limites e comportamento variam por mecanismo e operação. Teste no mesmo produto e versão do destino.

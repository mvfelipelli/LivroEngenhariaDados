---
title: Estudo de Caso — O Problema de Dados da DataRetail
description: "Diagnóstico inicial que justifica a Engenharia de Dados."
tags: [engenharia-de-dados, estudo-de-caso, dataretail]
aliases: [Caso DataRetail Engenharia de Dados]
created: 2026-07-21
updated: 2026-07-21
---

# Estudo de Caso — O Problema de Dados da DataRetail

A DataRetail cresceu por aquisições. Lojas usam versões diferentes do ERP, o e-commerce publica eventos e o CRM exporta arquivos diários. Financeiro e Comercial calculam receita com regras distintas.

O problema não é falta de dashboards. Faltam contratos, integração, histórico, qualidade, responsabilidade e uma plataforma que torne dados confiáveis disponíveis aos consumidores.

```mermaid
flowchart LR
    ERP["ERPs"] --> M["Processos manuais"]
    WEB["E-commerce"] --> M
    CRM["CRM"] --> M
    M --> D1["Relatório Financeiro"]
    M --> D2["Relatório Comercial"]
    D1 -. "diverge" .-> D2
```

A Engenharia de Dados assume a construção do fluxo, enquanto áreas de negócio definem semântica e critérios de aceite. A primeira entrega será uma receita diária reconciliada por loja.

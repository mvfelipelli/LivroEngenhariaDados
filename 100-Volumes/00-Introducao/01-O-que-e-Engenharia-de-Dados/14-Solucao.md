---
title: Solução — Mapeamento de um Fluxo de Dados
description: "Referência conceitual para receita diária da DataRetail."
tags: [engenharia-de-dados, solucao, dataretail]
aliases: [Solução Fluxo de Dados]
created: 2026-07-21
updated: 2026-07-21
---

# Solução — Mapeamento de um Fluxo de Dados

```mermaid
flowchart LR
    ERP["ERP lojas"] --> I["Captura"]
    WEB["E-commerce"] --> I
    PAY["Pagamentos"] --> I
    I --> V["Validação e quarentena"]
    V --> T["Padronização de pedidos"]
    T --> R["Receita diária"]
    R --> BI["Financeiro e Comercial"]
    V --> M["Métricas"]
    T --> M
    R --> M
```

| Etapa | Owner | Critério |
|---|---|---|
| Captura | Plataforma | Arquivos/eventos contabilizados |
| Validação | Engenharia de Dados | Válidos + quarentena = entrada |
| Padronização | Produto de Pedidos | Chave única e schema válido |
| Receita | Financeiro | Soma reconciliada por data/loja |

Falhas de fonte geram atraso alertado; schema desconhecido interrompe publicação; divergência monetária preserva a versão anterior.

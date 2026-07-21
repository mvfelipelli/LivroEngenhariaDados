---
title: Governança, Metadados, Lineage e Catálogo
description: "Descoberta, responsabilidade e análise de impacto."
tags: [governanca-de-dados, metadados, lineage]
aliases: [Catálogo de Dados]
created: 2026-07-21
updated: 2026-07-21
---

# Governança, Metadados, Lineage e Catálogo

Governança define direitos de decisão e controles para que dados sejam utilizáveis e protegidos. Metadados técnicos descrevem schema, formato e execução; metadados de negócio registram conceito, owner e finalidade; metadados operacionais incluem freshness e qualidade.

Catálogo torna ativos pesquisáveis. Lineage liga fontes, transformações e consumidores, apoiando análise de impacto e auditoria.

```mermaid
flowchart LR
    S["Fonte"] --> T["Transformação"]
    T --> D["Dataset"]
    D --> C["Dashboard"]
    D --> M["Modelo"]
    CAT["Catálogo"] --> S
    CAT --> T
    CAT --> D
```

Coletar metadados sem processo de manutenção gera catálogo desatualizado. Automação e ownership precisam caminhar juntos.

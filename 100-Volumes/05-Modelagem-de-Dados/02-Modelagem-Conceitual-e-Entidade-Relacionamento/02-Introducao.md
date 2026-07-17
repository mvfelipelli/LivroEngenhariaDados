---
title: Introdução
description: "O modelo ER como linguagem de descoberta."
tags: [modelagem-de-dados, introducao, er]
aliases: [Introdução ao Modelo ER]
created: 2026-07-17
updated: 2026-07-17
---

# Introdução

O modelo Entidade-Relacionamento, proposto por Peter Chen, descreve conjuntos de coisas distinguíveis, suas propriedades e associações. Seu valor não está em produzir um desenho bonito, mas em expor decisões que frases vagas escondem.

```mermaid
flowchart LR
    F["Falas e exemplos"] --> E["Entidades"]
    F --> R["Relacionamentos"]
    F --> C["Cardinalidades"]
    E --> M["Modelo conceitual"]
    R --> M
    C --> M
    M --> V["Validação com o negócio"]
```

O diagrama é acompanhado por glossário e regras textuais. Nem toda regra cabe visualmente, e sobrecarregar a figura reduz sua utilidade.

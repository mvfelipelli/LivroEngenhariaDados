---
title: Dimensões, Atributos, Hierarquias e Conformidade
description: "Contexto descritivo para filtros e agrupamentos."
tags: [dimensoes, hierarquias, conformidade]
aliases: [Dimensões Conformadas]
created: 2026-07-17
updated: 2026-07-17
---

# Dimensões, Atributos, Hierarquias e Conformidade

Dimensões respondem quem, o quê, onde, quando, como e por quê. Devem oferecer descrições legíveis, classificações e hierarquias para navegação.

Dimensão Data inclui dia, semana, mês, trimestre, feriado e calendário fiscal. Hierarquias podem ser estritas ou permitir múltiplos caminhos; isso afeta agregação.

Dimensão conformada possui significado e valores compatíveis entre processos. Produto e Loja conformados permitem comparar venda e estoque sem remapeamento ad hoc.

```mermaid
flowchart LR
    P["Produto"] --> C["Categoria"]
    C --> D["Departamento"]
```

Atributos devem preservar descrições históricas conforme a política de mudança. Código operacional e chave substituta possuem finalidades diferentes.

> [!note]
> Conformidade é contrato organizacional, não apenas nomes de colunas iguais.

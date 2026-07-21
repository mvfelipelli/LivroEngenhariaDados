---
title: Estrutura do Vault e Navegação
description: "Organização física, índices e Wikilinks do material."
tags: [obsidian, vault, navegacao]
aliases: [Navegação da Academia]
created: 2026-07-21
updated: 2026-07-21
---

# Estrutura do Vault e Navegação

Os diretórios numerados expressam função e ordem. `100-Volumes` contém a formação; `020-Laboratorios` reúne práticas transversais; `030-Projetos` concentra entregas; Atlas, Wiki e Biblioteca apoiam descoberta.

Cada volume possui README, sumário e changelog. Cada módulo possui navegação própria e componentes padronizados. Wikilinks conectam conceitos sem acoplar a navegação a caminhos externos.

```mermaid
flowchart TB
    V["Vault"] --> A["Atlas e Dashboard"]
    V --> W["Wiki e Biblioteca"]
    V --> L["Laboratórios e Projetos"]
    V --> VO["Volumes"]
    VO --> M["Módulos"]
    M --> C["Capítulos"]
```

Use busca, backlinks e grafo como apoio; o sumário continua sendo a fonte da sequência pedagógica.

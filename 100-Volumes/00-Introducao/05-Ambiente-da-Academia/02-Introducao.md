---
title: Introdução ao Ambiente da Academia
description: "Ambiente como sistema reproduzível, não coleção de instalações."
tags: [ambiente, introducao, reproducibilidade]
aliases: [Introdução Ambiente da Academia]
created: 2026-07-21
updated: 2026-07-21
---

# Introdução

Um ambiente de aprendizagem deve permitir executar, modificar, testar e explicar exemplos. Instalar ferramentas sem conhecer versões, caminhos e dependências cria falhas difíceis de reproduzir.

```mermaid
flowchart TB
    HW["Hardware"] --> OS["Sistema operacional"]
    OS --> SH["Shell"]
    OS --> RT["Runtimes"]
    OS --> CT["Containers"]
    SH --> G["Git e automação"]
    RT --> P["Projetos"]
    CT --> P
    ED["Editor + Obsidian"] --> P
```

O ambiente será incremental: comece com editor, Git e runtime básico; adicione serviços quando um laboratório exigir. A preparação prática ocorrerá no Módulo 08.

---
title: Introdução ao ELT
aliases: [ELT Introduction]
tags: [engenharia-de-dados, fundamentos, elt, introducao]
type: chapter
order: 02
parent: "[[README]]"
created: 2026-07-16
updated: 2026-07-16
description: "Motivação e contexto arquitetural do ELT."
---

# 02 — Introdução

Plataformas analíticas modernas armazenam grandes volumes e executam transformações paralelas. ELT usa essa capacidade: primeiro preserva os dados carregados, depois cria representações de consumo dentro da plataforma.

Isso separa ingestão e transformação, permite múltiplos produtos derivados e facilita reprocessamento. Também amplia o risco de expor dados brutos, duplicar lógica e consumir recursos sem controle.

```mermaid
flowchart TD
    A[Raw compartilhado] --> B[Modelo financeiro]
    A --> C[Modelo de marketing]
    A --> D[Modelo de operações]
```

## Questões orientadoras

- quais dados podem entrar na zona raw?
- quem pode acessá-los?
- qual contrato separa raw, staging e mart?
- como dependências são ordenadas?
- quando reconstruir ou processar incrementalmente?
- como testar sem copiar lógica entre modelos?
- como atribuir custo e responsabilidade?

## Próximo Capítulo

➡️ [[03-O-que-e-ELT|03 — O que é ELT]]

---
title: Arquitetura de Pipelines, Ports, Adapters e Configuração
description: "Separação entre regras e infraestrutura."
tags: [python, arquitetura, ports-adapters]
aliases: [Arquitetura de Pipelines Python]
created: 2026-07-20
updated: 2026-07-20
---

# Arquitetura de Pipelines, Ports, Adapters e Configuração

O núcleo transforma objetos de domínio. Ports descrevem fonte, sink, checkpoint e relógio. Adapters implementam CSV, HTTP, SQLite ou cloud.

```text
src/pipeline/
├── dominio.py
├── aplicacao.py
├── ports.py
├── adapters/
└── cli.py
```

Dependências apontam da infraestrutura para o núcleo. A aplicação coordena transação e políticas, sem conhecer detalhes do driver.

Configuração seleciona adapters, limites e caminhos. Ela é validada no startup, possui defaults seguros e não contém segredo versionado. O composition root cria dependências uma vez; importação não abre conexões nem executa pipeline.

Uma API pequena permite testar o núcleo em memória e substituir tecnologia sem reescrever regras.

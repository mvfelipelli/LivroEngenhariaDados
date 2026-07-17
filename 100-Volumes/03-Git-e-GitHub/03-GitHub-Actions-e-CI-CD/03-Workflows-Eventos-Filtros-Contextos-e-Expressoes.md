---
title: Workflows, Eventos, Filtros, Contextos e Expressões
description: "Sintaxe e superfície de execução de workflows."
tags: [github-actions, workflows, eventos]
aliases: [Workflow Syntax, Eventos Actions]
created: 2026-07-17
updated: 2026-07-17
---

# Workflows, Eventos, Filtros, Contextos e Expressões

Arquivos YAML em `.github/workflows` definem nome, eventos, permissões, concorrência e jobs. Filtros de branch e caminho evitam custo, mas required checks precisam permanecer coerentes.

```yaml
name: ci
on:
  pull_request:
    branches: [main]
    paths: ['src/**', 'tests/**']
  workflow_dispatch:

permissions:
  contents: read
```

Contextos como `github`, `inputs`, `vars`, `secrets`, `needs` e `matrix` têm disponibilidade e confiança diferentes. Dados de issue, branch e PR são entrada não confiável: não concatene diretamente em shell.

```yaml
- name: Validar referência
  env:
    REF_SEGURA: ${{ github.ref_name }}
  run: printf '%s\n' "$REF_SEGURA"
```

Expressões controlam `if`, nomes e inputs. Eventos `pull_request` e `pull_request_target` possuem contextos de segurança distintos; o segundo não deve executar código do fork com privilégios da base.

> [!tip]
> Defina `workflow_dispatch` com inputs tipados para operações manuais auditáveis.

Próximo: [[04-Jobs-Steps-Runners-Matrizes-e-Servicos]].

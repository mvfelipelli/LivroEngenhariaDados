---
title: Jobs, Steps, Runners, Matrizes e Serviços
description: "Unidades de execução, DAG e ambientes de runner."
tags: [github-actions, runners, matrix]
aliases: [Jobs GitHub Actions, Runners]
created: 2026-07-17
updated: 2026-07-17
---

# Jobs, Steps, Runners, Matrizes e Serviços

Steps compartilham workspace dentro do job; jobs executam em runners separados e trocam dados por outputs ou artefatos. `needs` cria DAG explícito.

```yaml
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        python: ['3.11', '3.12']
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@COMMIT_SHA_COMPLETO
      - run: python -m pytest
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: ./build.sh
```

Matriz cobre compatibilidade, mas multiplica custo. Services fornecem bancos ou brokers temporários ao job. Health checks evitam corrida de inicialização.

Runners hospedados começam limpos; self-hosted preservam risco de estado, rede e credenciais. Prefira efêmeros, segmentados e sem workloads não confiáveis.

> [!note]
> Imagem de runner muda ao longo do tempo. Fixe versões de toolchain e registre ambiente para reprodutibilidade.

Continue em [[05-Dependencias-Cache-Artefatos-e-Reprodutibilidade]].

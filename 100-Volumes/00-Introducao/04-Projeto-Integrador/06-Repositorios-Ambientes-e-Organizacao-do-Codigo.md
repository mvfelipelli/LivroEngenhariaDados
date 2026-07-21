---
title: Repositórios, Ambientes e Organização do Código
description: "Estrutura reprodutível para artefatos do projeto."
tags: [repositorio, ambientes, organizacao]
aliases: [Organização Projeto DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Repositórios, Ambientes e Organização do Código

O Vault documenta a formação; implementações podem viver em `030-Projetos` ou repositório dedicado. Código, configuração de exemplo, contratos e testes são versionados. Dados gerados e segredos permanecem fora do Git.

```text
projeto-dataretail/
├── src/
├── tests/
├── contracts/
├── data/sample/
├── docs/
├── infra/
├── pyproject.toml
└── README.md
```

Ambientes local, teste e produção usam o mesmo artefato com configurações distintas. Versões de runtime e dependências são fixadas. Comandos principais ficam em scripts ou task runner, reduzindo conhecimento tribal.

Decisões arquiteturais, runbooks e changelog acompanham o código.

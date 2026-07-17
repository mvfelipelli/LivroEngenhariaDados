---
title: Pyproject, Build, Wheels, Versionamento e Publicação
description: "Do código-fonte ao artefato instalável."
tags: [python, pyproject, wheel, versionamento]
aliases: [Empacotamento Python]
created: 2026-07-17
updated: 2026-07-17
---

# Pyproject, Build, Wheels, Versionamento e Publicação

`pyproject.toml` declara backend de build, metadados, versão Python, dependências e scripts.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "dataretail-pipeline"
version = "1.2.0"
requires-python = ">=3.12"

[project.scripts]
dataretail-pipeline = "dataretail.cli:main"
```

Sdist contém fontes para build; wheel é artefato pronto para instalação, podendo ser puro ou específico de plataforma. Teste o wheel em ambiente limpo: executar apenas do checkout pode mascarar arquivos ausentes.

Versão comunica compatibilidade conforme a política adotada. Builds devem partir de commit identificado, produzir artefatos imutáveis, gerar hashes e, idealmente, proveniência e SBOM. Publique uma vez; não sobrescreva uma versão existente.

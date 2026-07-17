---
title: Dependências, Pacotes e Reprodutibilidade
description: "Declaração, resolução e fixação de dependências."
tags: [python, dependencias, pyproject]
aliases: [Dependências Python]
created: 2026-07-17
updated: 2026-07-17
---

# Dependências, Pacotes e Reprodutibilidade

Uma distribuição é o artefato instalado; um pacote é uma unidade importável. O nome publicado pode diferir do nome usado em `import`.

O `pyproject.toml` centraliza metadados e configuração de ferramentas:

```toml
[project]
name = "dataretail-carga"
version = "0.1.0"
requires-python = ">=3.12,<3.14"
dependencies = []
```

Restrições amplas expressam compatibilidade; um lock reproduz a resolução exata. Aplicações normalmente fixam o ambiente de implantação, enquanto bibliotecas evitam limitar dependências transitivas além do necessário.

```bash
python -m pip install --require-hashes -r requirements.txt
```

Hashes protegem a integridade dos artefatos. Dependências devem ser atualizadas deliberadamente, com testes e revisão de vulnerabilidades e licenças.

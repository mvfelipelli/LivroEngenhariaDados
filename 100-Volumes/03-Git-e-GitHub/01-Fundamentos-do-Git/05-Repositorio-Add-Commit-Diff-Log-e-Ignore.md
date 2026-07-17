---
title: Repositório, Add, Commit, Diff, Log e Ignore
description: "Fluxo diário para construir e inspecionar commits."
tags: [git, commit, diff, log]
aliases: [Fluxo Básico Git, Git Add]
created: 2026-07-17
updated: 2026-07-17
---

# Repositório, Add, Commit, Diff, Log e Ignore

Configure identidade conscientemente; ela entra na metadata, não autentica por si só.

```bash
git init -b main projeto
git config user.name 'Ana Dados'
git config user.email 'ana@example.test'
git status
```

## Construção do commit

```bash
git diff -- pipeline.py
git add -p pipeline.py
git diff --staged --check
git commit -m 'feat: valida schema de pedidos'
```

`git add` copia a versão atual para o index; editar depois não atualiza automaticamente o staged. `git add -p` permite selecionar hunks. Um bom commit é coeso, testado e explica intenção.

## Inspeção

```bash
git log --graph --decorate --oneline --all
git show --stat HEAD
git diff main...feature
git blame -L 10,20 pipeline.py
```

Dois pontos comparam endpoints; três pontos comparam uma ponta ao merge-base, útil para revisar branch. `blame` mostra último commit por linha, não culpado nem origem conceitual.

## Ignore

Use `.gitignore` para artefatos do projeto, `.git/info/exclude` para exclusões locais e configuração global para arquivos pessoais. Não ignore migrations ou lockfiles sem decisão técnica.

```gitignore
.venv/
__pycache__/
*.log
.env
dados/entrada/*.csv
```

> [!warning]
> Revise `git diff --staged` antes do commit para evitar segredos, dumps e mudanças acidentais.

Próximo: [[06-Branches-Merges-Conflitos-e-Integracao]].

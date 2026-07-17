---
title: Solução — Fluxo Git Completo
description: "Implementação validada do laboratório Git."
tags: [git, laboratorio, solucao, bash]
aliases: [Solução Laboratório Git]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Fluxo Git Completo

Salve como `fluxo_git.sh`:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

raiz=$(mktemp -d)
trap 'rm -rf -- "$raiz"' EXIT
cd "$raiz"

git init -q -b main
git config user.name 'DataRetail Bot'
git config user.email 'bot@dataretail.example'

export GIT_AUTHOR_DATE='2026-01-01T00:00:00Z'
export GIT_COMMITTER_DATE='2026-01-01T00:00:00Z'

printf '# Pipeline de pedidos\n' >README.md
git add README.md
git commit -q -m 'docs: cria projeto'
base=$(git rev-parse HEAD)

git switch -q -c feature/pedidos
printf 'status=validado\n' >pipeline.conf
git add pipeline.conf
git commit -q -m 'feat: adiciona pipeline'
feature=$(git rev-parse HEAD)

git switch -q main
GIT_AUTHOR_DATE='2026-01-01T00:02:00Z' \
GIT_COMMITTER_DATE='2026-01-01T00:02:00Z' \
  git merge -q --no-ff feature/pedidos -m 'merge: integra pipeline'

commits=$(git rev-list --count HEAD)
branches=$(git branch --format='%(refname:short)' | wc -l | tr -d ' ')
[[ -z $(git status --porcelain) ]]
git merge-base --is-ancestor "$base" HEAD
git merge-base --is-ancestor "$feature" HEAD
[[ $(cat pipeline.conf) == 'status=validado' ]]

printf 'commits=%s\n' "$commits"
printf 'branches=%s\n' "$branches"
printf 'working_tree=limpa\n'
printf 'feature_integrada=sim\n'
printf 'ancestralidade=ok\n'
printf 'git=ok\n'
```

## Leitura da solução

Datas e identidade fixas tornam commits reproduzíveis. `--no-ff` cria merge mesmo quando fast-forward seria possível. `merge-base --is-ancestor` valida o grafo sem depender da aparência do log.

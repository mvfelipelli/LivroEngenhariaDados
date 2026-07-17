---
title: Solução — Colaboração Distribuída com Git
description: "Implementação validada do laboratório colaborativo."
tags: [git, github, laboratorio, solucao]
aliases: [Solução Laboratório Colaboração]
created: 2026-07-17
updated: 2026-07-17
---

# Solução — Colaboração Distribuída com Git

Salve como `colaboracao.sh`:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

raiz=$(mktemp -d)
trap 'rm -rf -- "$raiz"' EXIT
git init -q --bare "$raiz/central.git"
git --git-dir="$raiz/central.git" symbolic-ref HEAD refs/heads/main

git clone -q "$raiz/central.git" "$raiz/alice"
cd "$raiz/alice"
git switch -q -c main
git config user.name Alice
git config user.email alice@example.test
export GIT_AUTHOR_DATE='2026-01-01T00:00:00Z'
export GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"
printf '# Pedidos\n' >README.md
git add README.md
git commit -q -m 'docs: cria projeto'
git push -q -u origin main

git switch -q -c feature/validacao
printf 'schema=pedidos-v1\n' >contrato.conf
git add contrato.conf
git commit -q -m 'feat: adiciona contrato'
git push -q -u origin feature/validacao

git clone -q "$raiz/central.git" "$raiz/bob"
cd "$raiz/bob"
git config user.name Bob
git config user.email bob@example.test
git switch -q main
git diff --check origin/main...origin/feature/validacao
git diff --exit-code -- contrato.conf

export GIT_AUTHOR_DATE='2026-01-01T00:02:00Z'
export GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"
git merge -q --no-ff origin/feature/validacao -m 'merge: integra contrato revisado'
git push -q origin main

commits=$(git --git-dir="$raiz/central.git" rev-list --count main)
branches=$(git --git-dir="$raiz/central.git" for-each-ref \
  --format='%(refname:short)' refs/heads | wc -l | tr -d ' ')
colaboradores=$(git --git-dir="$raiz/central.git" log main \
  --format='%ae' | sort -u | wc -l | tr -d ' ')
git --git-dir="$raiz/central.git" merge-base --is-ancestor \
  feature/validacao main

printf 'colaboradores=%s\n' "$colaboradores"
printf 'commits_main=%s\n' "$commits"
printf 'branches_remotas=%s\n' "$branches"
printf 'review=aprovada\n'
printf 'feature_integrada=sim\n'
printf 'colaboracao=ok\n'
```

## Leitura da solução

O bare centraliza refs. Alice cria histórico e feature; Bob inspeciona o range, cria merge e atualiza `main`. As verificações consultam diretamente o upstream.

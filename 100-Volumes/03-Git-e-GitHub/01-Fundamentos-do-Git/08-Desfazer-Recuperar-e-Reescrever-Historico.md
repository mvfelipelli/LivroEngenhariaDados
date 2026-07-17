---
title: Desfazer, Recuperar e Reescrever Histórico
description: "Escolha segura entre restore, reset, revert e reflog."
tags: [git, recuperacao, reset, revert]
aliases: [Desfazer no Git, Git Reflog]
created: 2026-07-17
updated: 2026-07-17
---

# Desfazer, Recuperar e Reescrever Histórico

Antes de desfazer, identifique área e publicação. Mudança não commitada existe apenas no working tree ou index; commit publicado pode estar em clones de terceiros.

| Objetivo | Ferramenta típica |
| --- | --- |
| descartar arquivo não staged | `git restore arquivo` |
| remover do index, manter arquivo | `git restore --staged arquivo` |
| criar inversão auditável | `git revert commit` |
| mover branch local | `git reset` |
| recuperar referência recente | `git reflog` |

`reset --soft` move ref e mantém index; mixed redefine index; hard também redefine working tree e pode destruir mudanças. Faça branch de segurança antes de operação incerta.

```bash
git branch backup/antes-da-correcao
git reflog
git branch recuperacao HEAD@{2}
git revert --no-edit abc123
```

Reflog registra movimentos de refs localmente por tempo limitado; não é backup remoto. Objetos inalcançáveis podem ser removidos por garbage collection.

## Histórico publicado

Prefira revert para preservar auditoria. Rebase interativo e amend são úteis antes da publicação, mas mudam hashes de commits e descendentes. Após vazamento de segredo, revogue primeiro; depois coordene reescrita e limpeza de caches.

> [!warning]
> `git reset --hard` e `git clean` são destrutivos para trabalho não commitado. Inspecione e use dry-run quando disponível.

Continue em [[09-Workflows-Qualidade-Seguranca-e-Arquivos-Grandes]].

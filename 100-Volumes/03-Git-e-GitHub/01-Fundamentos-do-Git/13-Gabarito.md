---
title: Gabarito — Fundamentos do Git
description: "Respostas orientativas dos exercícios de Git."
tags: [git, gabarito]
aliases: [Gabarito Git]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

1. Blob guarda bytes; tree nomes e modos; commit snapshot e pais; ref nomeia objeto.
2. Working tree é edição, index é próximo snapshot e HEAD identifica estado atual.
3. Branch move com commits; tag normalmente permanece em uma versão.
4. Fetch recebe, pull recebe e integra, push propõe atualização remota.
5. Use `git diff` e `git diff --staged`; `git status` resume estados.
6. Crie branch ou tag apontando para o commit antes que se torne inalcançável.
7. Fetch, inspecione divergência, integre por merge/rebase conforme política, teste e push.
8. Revogue, investigue, remova da origem, coordene reescrita e limpeza; trocar arquivo atual não basta.
9. Cada commit deve ser testável e explicar uma intenção; dependências determinam ordem.
10. Altere mesma região em duas branches, faça merge, resolva marcadores, add, teste e continue.
11. Localize hash no `git reflog` e crie `git branch recuperada <hash>`.
12. Ignore ambiente, cache, logs, `.env`, artefatos e dados locais; mantenha código, lockfiles e migrations.
13. Merge preserva topologia; squash consolida; rebase lineariza criando commits novos.
14. Use expand-contract, revisão, testes, ordem imutável e compatibilidade com rollback de aplicação.
15. O grafo contém base, commit da feature e merge com dois pais; ambas as branches permanecem.

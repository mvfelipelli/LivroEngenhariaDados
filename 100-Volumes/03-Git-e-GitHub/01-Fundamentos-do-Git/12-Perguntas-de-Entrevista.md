---
title: Perguntas de Entrevista — Fundamentos do Git
description: "Perguntas progressivas com respostas fundamentadas."
tags: [git, entrevista]
aliases: [Entrevista Git]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Git armazena diffs?

Seu modelo lógico armazena snapshots por trees e blobs; compressão interna pode usar deltas.

## 2. Working tree e index diferem em quê?

Working tree é edição atual; index é o snapshot preparado para o próximo commit.

## 3. O que é commit?

Objeto que referencia tree, pais, autor, committer e mensagem.

## 4. Branch é cópia do projeto?

Não. É uma referência móvel para commit.

## 5. O que é detached HEAD?

HEAD aponta diretamente para commit, não para branch; novos commits precisam de ref para não ficarem inalcançáveis.

## 6. Fast-forward e merge commit diferem em quê?

Fast-forward apenas move a ref; merge commit une histórias com múltiplos pais.

## 7. Fetch e pull diferem em quê?

Fetch baixa e atualiza refs remotas; pull também integra por merge ou rebase.

## 8. `origin/main` é a branch do servidor em tempo real?

Não. É ref local atualizada pelo último fetch ou operação relacionada.

## 9. Reset e revert diferem em quê?

Reset move refs e pode alterar index/working tree; revert cria commit inverso auditável.

## 10. Para que serve reflog?

Registra movimentos locais de refs e ajuda a recuperar commits recentes.

## 11. Por que rebase muda hashes?

Ele cria novos commits com pais e metadata diferentes, mesmo que o patch seja equivalente.

## 12. Como resolver conflito?

Entenda base e intenções, edite resultado, marque no index, teste e continue a integração.

## 13. Como remover segredo publicado?

Revogue primeiro, investigue uso, reescreva sob coordenação e limpe clones/caches quando necessário.

## 14. Quando usar Git LFS?

Para binários grandes que precisam de versionamento por ponteiros, não como substituto geral de storage de dados.

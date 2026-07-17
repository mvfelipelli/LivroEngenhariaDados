---
title: Perguntas de Entrevista — Colaboração e GitHub
description: "Perguntas progressivas com respostas fundamentadas."
tags: [git, github, entrevista]
aliases: [Entrevista GitHub]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Fork e branch no mesmo repositório diferem em quê?

Fork é outro repositório; branch é ref no mesmo repositório. Permissões e confiança do CI mudam.

## 2. O que uma PR representa?

Proposta e discussão para integrar diferenças entre branches, com eventos, revisões e checks.

## 3. Aprovação prova correção?

Não. Registra julgamento sob evidências; testes, políticas e operação complementam.

## 4. Merge e squash diferem em quê?

Merge preserva topologia e commits; squash cria um commit consolidado na base.

## 5. Quando rebase é adequado?

Para atualizar e organizar branch privada; em história compartilhada exige coordenação por reescrever commits.

## 6. O que CODEOWNERS faz?

Solicita owners conforme padrões; torna-se gate quando regra exige revisão deles.

## 7. Branch protection e ruleset diferem em quê?

Ambos aplicam regras; rulesets permitem composição, targeting e avaliação mais ampla conforme recursos disponíveis.

## 8. Para que serve merge queue?

Testa e integra PRs considerando a base e combinações mais recentes, reduzindo falhas entre mudanças concorrentes.

## 9. Por que invalidar aprovação após novo commit?

Porque a aprovação anterior pode não cobrir o conteúdo atualizado.

## 10. Qual risco de `pull_request_target`?

Executa com contexto da base; checkout e execução de código não confiável podem expor segredos ou escrita.

## 11. Por que fixar Actions por SHA?

Tags podem mudar; SHA completo referencia conteúdo imutável, desde que validado no repositório correto.

## 12. Como proteger self-hosted runner?

Isole rede e credenciais, use runners efêmeros, controle origens, limpe estado e monitore.

## 13. Como governar bypass?

Poucos atores, justificativa, auditoria, expiração e revisão posterior.

## 14. Como versionar migrations colaborativamente?

Ordem imutável, owners, testes de compatibilidade, expand-contract e ligação ao deploy.

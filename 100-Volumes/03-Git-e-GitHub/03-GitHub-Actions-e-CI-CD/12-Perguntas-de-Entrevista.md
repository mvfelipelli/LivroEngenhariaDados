---
title: Perguntas de Entrevista — GitHub Actions e CI/CD
description: "Perguntas com respostas fundamentadas."
tags: [github-actions, ci-cd, entrevista]
aliases: [Entrevista GitHub Actions]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Workflow, job e step diferem em quê?

Workflow responde a evento; jobs formam DAG; steps compartilham runner dentro do job.

## 2. Cache e artefato diferem em quê?

Cache acelera conteúdo regenerável; artefato preserva ou transfere resultado da execução.

## 3. O que `needs` faz?

Cria dependência e disponibiliza resultados do job anterior.

## 4. Por que declarar permissions?

Para reduzir capacidades do `GITHUB_TOKEN` ao mínimo por workflow ou job.

## 5. Por que OIDC?

Troca identidade verificável e curta por credencial cloud, evitando chave estática.

## 6. Qual risco de self-hosted runner?

Persistência de estado, credenciais e acesso à rede; código não confiável pode comprometer o ambiente.

## 7. O que environment protege?

Deployment, aprovações/regras, variáveis e segredos conforme disponibilidade do plano.

## 8. Para que serve concurrency?

Agrupa runs ou jobs para limitar sobreposição; política de cancelamento depende do processo.

## 9. Por que build único?

Garante que staging e produção recebam os mesmos bytes identificados.

## 10. Por que SHA completo em Actions?

É referência imutável; tags podem mudar.

## 11. Reusable workflow e composite action diferem em quê?

O primeiro reutiliza workflows/jobs; o segundo agrupa steps dentro de job.

## 12. Como proteger PR de fork?

Sem segredos/escrita, permissões mínimas e sem executar código não confiável em contexto privilegiado.

## 13. Como reduzir flaky CI?

Isolar estado, fixar dependências, controlar relógio/rede, medir e corrigir causa.

## 14. Como fazer rollback com migration?

Compatibilidade expand-contract, backup e estratégia de roll-forward/rollback testada.

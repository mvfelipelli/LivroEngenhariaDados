---
title: Fundamentos do Git
description: "Modelo de dados, estados, branches, remotos e recuperação no Git."
tags: [git, versionamento, volume-03]
aliases: [Módulo 01 Git, Git Fundamentals]
created: 2026-07-17
updated: 2026-07-17
---

# Módulo 01 — Fundamentos do Git

Git registra snapshots endereçados por conteúdo e conecta commits em um grafo. Compreender objetos, referências e áreas de estado torna comandos previsíveis e reduz perdas.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Versionamento-Distribuido-e-Estados-do-Git|Versionamento Distribuído e Estados do Git]]
4. [[04-Objetos-Commits-Arvores-Refs-e-HEAD|Objetos, Commits, Árvores, Refs e HEAD]]
5. [[05-Repositorio-Add-Commit-Diff-Log-e-Ignore|Repositório, Add, Commit, Diff, Log e Ignore]]
6. [[06-Branches-Merges-Conflitos-e-Integracao|Branches, Merges, Conflitos e Integração]]
7. [[07-Remotos-Fetch-Pull-Push-e-Tracking|Remotos, Fetch, Pull, Push e Tracking]]
8. [[08-Desfazer-Recuperar-e-Reescrever-Historico|Desfazer, Recuperar e Reescrever Histórico]]
9. [[09-Workflows-Qualidade-Seguranca-e-Arquivos-Grandes|Workflows, Qualidade, Segurança e Arquivos Grandes]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    W["Working tree"] --> I["Index"]
    I --> C["Commit"]
    C --> R["Repositório remoto"]
    R --> C
```

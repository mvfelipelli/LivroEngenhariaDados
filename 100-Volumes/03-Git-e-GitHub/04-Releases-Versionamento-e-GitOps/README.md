---
title: Releases, Versionamento e GitOps
description: "Da intenção de mudança à promoção declarativa, rastreável e reconciliada."
tags: [releases, versionamento, gitops, volume-03]
aliases: [Módulo 04 Git, Releases e GitOps]
created: 2026-07-17
updated: 2026-07-17
---

# Módulo 04 — Releases, Versionamento e GitOps

Uma release torna uma mudança consumível; GitOps torna o estado promovido verificável e continuamente reconciliado. O elo entre ambos é uma identidade imutável, acompanhada por evidências e política.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Versoes-Compatibilidade-e-SemVer|Versões, Compatibilidade e SemVer]]
4. [[04-Tags-Releases-Changelog-e-Notas|Tags, Releases, Changelog e Notas]]
5. [[05-Artefatos-Imutabilidade-Proveniencia-e-SBOM|Artefatos, Imutabilidade, Proveniência e SBOM]]
6. [[06-Estrategias-de-Release-Promocao-e-Rollback|Estratégias de Release, Promoção e Rollback]]
7. [[07-Fundamentos-e-Arquitetura-GitOps|Fundamentos e Arquitetura GitOps]]
8. [[08-Reconciliacao-Drift-Ambientes-e-Segredos|Reconciliação, Drift, Ambientes e Segredos]]
9. [[09-Governanca-Metricas-Seguranca-e-Adocao|Governança, Métricas, Segurança e Adoção]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    C["Commit aprovado"] --> R["Release imutável"]
    R --> P["Promoção declarativa"]
    P --> A["Agente GitOps"]
    A --> S["Estado reconciliado"]
```

---
title: Modelagem Lógica Relacional e Normalização
description: "Relações, dependências e decomposição orientada à integridade."
tags: [modelagem-de-dados, relacional, normalizacao, volume-05]
aliases: [Módulo 03 Modelagem de Dados, Normalização]
created: 2026-07-17
updated: 2026-07-17
---

# Módulo 03 — Modelagem Lógica Relacional e Normalização

O modelo lógico traduz conceitos em relações, atributos, chaves e restrições independentes de um produto específico. A normalização usa dependências para reduzir redundância e anomalias sem perder informação.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Relacoes-Tuplas-Atributos-Dominios-e-Esquemas|Relações, Tuplas, Atributos, Domínios e Esquemas]]
4. [[04-Superchaves-Chaves-Candidatas-Primarias-e-Estrangeiras|Superchaves, Chaves Candidatas, Primárias e Estrangeiras]]
5. [[05-Dependencias-Funcionais-Fecho-e-Cobertura-Minima|Dependências Funcionais, Fecho e Cobertura Mínima]]
6. [[06-Primeira-Segunda-e-Terceira-Formas-Normais|Primeira, Segunda e Terceira Formas Normais]]
7. [[07-BCNF-Quarta-e-Quinta-Formas-Normais|BCNF, Quarta e Quinta Formas Normais]]
8. [[08-Decomposicao-Sem-Perda-e-Preservacao-de-Dependencias|Decomposição sem Perda e Preservação de Dependências]]
9. [[09-Anomalias-Trade-offs-e-Processo-de-Normalizacao|Anomalias, Trade-offs e Processo de Normalização]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    R["Relação com redundância"] --> D["Dependências"]
    D --> N["Decomposição"]
    N --> L["Junção sem perda"]
    N --> I["Integridade preservada"]
```

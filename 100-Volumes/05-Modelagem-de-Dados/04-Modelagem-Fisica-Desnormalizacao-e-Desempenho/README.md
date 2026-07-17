---
title: Modelagem Física, Desnormalização e Desempenho
description: "Implementação orientada a acesso, armazenamento e operação."
tags: [modelagem-de-dados, modelagem-fisica, desempenho, volume-05]
aliases: [Módulo 04 Modelagem de Dados]
created: 2026-07-17
updated: 2026-07-17
---

# Módulo 04 — Modelagem Física, Desnormalização e Desempenho

O modelo físico adapta o modelo lógico a um mecanismo e a uma carga reais. Tipos, índices, layout, particionamento e redundância controlada devem reduzir custo sem enfraquecer identidade e integridade.

## Percurso

1. [[01-Objetivos|Objetivos]]
2. [[02-Introducao|Introdução]]
3. [[03-Tipos-Fisicos-Precisao-Nulabilidade-e-Defaults|Tipos Físicos, Precisão, Nulabilidade e Defaults]]
4. [[04-Chaves-Identidade-Referencias-e-Localidade|Chaves, Identidade, Referências e Localidade]]
5. [[05-Indices-Clustering-Cobertura-e-Custo-de-Escrita|Índices, Clustering, Cobertura e Custo de Escrita]]
6. [[06-Particionamento-Distribuicao-Pruning-e-Skew|Particionamento, Distribuição, Pruning e Skew]]
7. [[07-Armazenamento-Linhas-Colunas-Compressao-e-Formato|Armazenamento em Linhas e Colunas, Compressão e Formato]]
8. [[08-Desnormalizacao-Projecoes-Materializadas-e-Consistencia|Desnormalização, Projeções Materializadas e Consistência]]
9. [[09-Workload-Medicao-Evolucao-e-Governanca-Fisica|Workload, Medição, Evolução e Governança Física]]
10. [[10-Estudo-de-Caso-DataRetail|Estudo de Caso — DataRetail S.A.]]
11. [[11-Resumo|Resumo]]
12. [[12-Perguntas-de-Entrevista|Perguntas de Entrevista]]
13. [[13-Exercicios|Exercícios]] e [[13-Gabarito|Gabarito]]
14. [[14-Laboratorio|Laboratório]] e [[14-Solucao|Solução]]
15. [[15-Referencias|Referências]]

```mermaid
flowchart LR
    L["Modelo lógico"] --> W["Workload e SLO"]
    W --> F["Modelo físico"]
    F --> M["Medição"]
    M --> F
```

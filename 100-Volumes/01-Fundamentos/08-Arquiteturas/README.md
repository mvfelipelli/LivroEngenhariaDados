---
title: Arquiteturas de Dados
aliases: [Arquitetura de Dados, Data Architecture]
tags: [engenharia-de-dados, fundamentos, arquitetura, volume-01, modulo-08]
type: modulo
status: concluido
created: 2026-07-16
updated: 2026-07-16
description: "Fundamentos para projetar e evoluir arquiteturas de dados orientadas por requisitos."
---

# Módulo 08 — Arquiteturas de Dados

> [!abstract]
> Arquitetura de dados é o conjunto de decisões estruturais que conecta necessidades do negócio, fluxos de informação, componentes e atributos de qualidade. Não existe arquitetura universal: existem escolhas justificadas e verificáveis.

## Estrutura

- [[01-Objetivos]]
- [[02-Introducao]]
- [[03-O-que-e-Arquitetura-de-Dados]]
- [[04-Principios-Requisitos-e-Trade-offs]]
- [[05-Estilos-Camadas-e-Componentes]]
- [[06-Arquiteturas-Batch-Streaming-e-Orientadas-a-Eventos]]
- [[07-Arquiteturas-Analiticas-Warehouse-Lake-e-Lakehouse]]
- [[08-Descentralizacao-Data-Mesh-e-Data-Fabric]]
- [[09-Decisoes-Arquiteturais-Evolucao-e-Governanca]]
- [[10-Estudo-de-Caso-DataRetail]]
- [[11-Resumo]]
- [[12-Perguntas-de-Entrevista]]
- [[13-Exercicios]]
- [[13-Gabarito]]
- [[14-Laboratorio]]
- [[14-Solucao]]
- [[15-Referencias]]

```mermaid
flowchart LR
    A[Objetivos de negócio] --> B[Requisitos]
    B --> C[Decisões arquiteturais]
    C --> D[Componentes e fluxos]
    D --> E[Atributos de qualidade]
    E --> F[Métricas e evolução]
    F -. aprendizado .-> B
```

## Projeto integrador

A DataRetail S.A. comparará alternativas arquiteturais, registrará a decisão e aplicará testes automatizados às propriedades escolhidas.

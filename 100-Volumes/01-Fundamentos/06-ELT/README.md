---
title: ELT
aliases: [Extract Load Transform, Extração Carga e Transformação]
tags: [engenharia-de-dados, fundamentos, elt, volume-01, modulo-06]
type: modulo
status: concluido
created: 2026-07-16
updated: 2026-07-16
description: "Fundamentos de carga antecipada e transformação governada dentro da plataforma de dados."
---

# Módulo 06 — ELT

> [!abstract]
> ELT carrega dados no destino antes das transformações de consumo, aproveitando sua capacidade computacional e preservando uma base reprocessável. Flexibilidade exige contratos, camadas, testes, segurança e controle de custo.

## Estrutura

- [[01-Objetivos]]
- [[02-Introducao]]
- [[03-O-que-e-ELT]]
- [[04-Extracao-e-Carga-na-Plataforma]]
- [[05-Transformacoes-no-Destino]]
- [[06-Camadas-Modelos-e-Produtos]]
- [[07-Incrementalidade-e-Materializacoes]]
- [[08-Testes-Documentacao-e-Linhagem]]
- [[09-Governanca-Seguranca-Custo-e-Desempenho]]
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
    A[Fontes] --> B[Extract]
    B --> C[Load raw]
    C --> D[Transform staging]
    D --> E[Transform marts]
    E --> F[Produtos de dados]
```

## Projeto Integrador

A DataRetail S.A. carregará eventos brutos em uma plataforma analítica e publicará modelos SQL testados, documentados e reconciliados.

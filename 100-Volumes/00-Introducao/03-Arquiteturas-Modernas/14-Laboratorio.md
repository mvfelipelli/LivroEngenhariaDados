---
title: Laboratório — Decisão Arquitetural da DataRetail
description: "Comparação de alternativas por requisitos e trade-offs."
tags: [arquitetura-de-dados, laboratorio, dataretail]
aliases: [Laboratório Arquitetura DataRetail]
created: 2026-07-21
updated: 2026-07-21
---

# Laboratório — Decisão Arquitetural da DataRetail

## Objetivo

Propor arquitetura inicial para receita diária e fraude em tempo quase real.

## Pré-requisitos

- conceitos deste módulo;
- editor com Mermaid.

## Ambiente

Produza um ADR e um diagrama conceitual, sem escolher produtos comerciais.

## Passos

1. Defina volume, latência, retenção e SLOs.
2. Separe receita diária e fraude.
3. Compare batch único, Lambda e abordagem híbrida com log.
4. Defina camadas e contratos.
5. Registre segurança, qualidade e operação.
6. Estime custos relativos e riscos.
7. Escolha uma alternativa e seus gatilhos de revisão.

## Validação

A decisão deve ligar cada componente a um requisito, declarar ao menos três trade-offs e prever replay/reconciliação.

## Conclusão

O laboratório avalia raciocínio arquitetural, não familiaridade com marcas.

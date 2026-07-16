---
title: Laboratório — Prontidão de Produtos de Dados
aliases: [Laboratório de Conceitos Modernos]
tags: [conceitos-modernos, laboratorio, python, sqlite]
created: 2026-07-16
updated: 2026-07-16
description: "Avaliação executável de contratos e capacidades mínimas de produtos."
---

# Laboratório — Prontidão de Produtos de Dados

## Objetivo

Avaliar três candidatos a produto da DataRetail S.A. por oito critérios e persistir bloqueios de forma idempotente.

## Pré-requisitos

- Python 3.10 ou superior;
- biblioteca padrão;
- conceitos de produto, contrato e guardrails.

## Passo a passo

1. Modele owner, consumidores, schema, SLO, qualidade, acesso, linhagem e custo.
2. Considere pronto somente o produto com todos os critérios.
3. Registre uma violação para cada critério ausente.
4. Calcule percentual de produtos prontos.
5. Persista duas vezes usando chaves estáveis.

## Resultado esperado

```text
produtos=3
checks=24
prontos=1
bloqueados=2
violacoes=4
readiness=33.33
violacoes_persistidas=4
segunda_execucao=sem_duplicacao
produtos_de_dados=ok
```

## Conclusão

O laboratório transforma “dados como produto” em requisitos verificáveis. Critérios reais devem ser proporcionais à criticidade e integrados ao golden path da plataforma.

Compare com [[14-Solucao]].

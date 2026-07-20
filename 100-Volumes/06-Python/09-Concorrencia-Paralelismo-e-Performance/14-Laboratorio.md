---
title: Laboratório — Coletor Assíncrono Limitado
description: "Concorrência, timeout, retry e determinismo com asyncio."
tags: [python, laboratorio, asyncio]
aliases: [Laboratório Concorrência Python]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Coletor Assíncrono Limitado

## Objetivo

Coletar seis fontes simuladas sem ultrapassar duas operações simultâneas.

## Pré-requisitos

- Python 3.11 ou superior;
- [[08-NumPy-Pandas-e-Processamento-Tabular/README|NumPy, Pandas e Processamento Tabular]];
- nenhuma dependência externa.

## Ambiente

Salve a solução como `coletor.py` e execute no ambiente virtual.

## Passos

1. Modele uma operação remota assíncrona.
2. Instrumente concorrência atual e máxima.
3. Use Semaphore com limite dois.
4. Aplique timeout por tentativa.
5. Faça uma única repetição para timeout transitório.
6. Use TaskGroup para ciclo de vida estruturado.
7. Ordene resultados pela chave.
8. Execute duas vezes e compare.

## Validação

Devem existir seis resultados, total `2100`, máximo de duas operações, sete tentativas e saída idêntica nas duas execuções.

## Conclusão

O laboratório demonstra que concorrência controlada não precisa sacrificar determinismo nem rastreabilidade.

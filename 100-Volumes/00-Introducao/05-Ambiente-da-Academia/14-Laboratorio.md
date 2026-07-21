---
title: Laboratório — Inventário Reproduzível do Ambiente
description: "Coleta não sensível de versões e capacidades."
tags: [ambiente, laboratorio, diagnostico]
aliases: [Laboratório Inventário do Ambiente]
created: 2026-07-21
updated: 2026-07-21
---

# Laboratório — Inventário Reproduzível do Ambiente

## Objetivo

Criar um relatório do ambiente que ajude a reproduzir e diagnosticar laboratórios.

## Pré-requisitos

- terminal;
- Git e editor, se já instalados.

## Ambiente

Execute somente comandos de leitura. Não inclua usuário, tokens, IP público ou valores de segredos.

## Passos

1. Registre sistema e arquitetura.
2. Registre CPU, memória e espaço livre.
3. Identifique shell atual.
4. Consulte versões de Git, Python, Java e container runtime quando disponíveis.
5. Registre editor e Obsidian manualmente.
6. Liste limitações conhecidas.
7. Salve um relatório sanitizado.

## Validação

O relatório deve permitir comparar requisitos de um laboratório sem expor informação sensível.

## Conclusão

Inventário objetivo reduz tentativas aleatórias durante troubleshooting.

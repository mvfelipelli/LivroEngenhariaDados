---
title: Laboratório — Fluxo Git Completo
description: "Repositório reproduzível com branch, commits e merge."
tags: [git, laboratorio, bash]
aliases: [Laboratório Git]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Fluxo Git Completo

## Objetivo

Criar repositório temporário, preparar commits, desenvolver em branch, integrar com merge e validar invariantes do grafo.

## Pré-requisitos

- Git 2.28 ou superior;
- Bash;
- diretório temporário gravável.

## Ambiente

O script configura identidade apenas no repositório, fixa datas para repetibilidade e remove o diretório ao terminar. Não usa rede.

## Passos

1. Salve [[14-Solucao|a solução]] como `fluxo_git.sh`.
2. Execute `bash -n fluxo_git.sh`.
3. Execute `bash fluxo_git.sh`.
4. Confirme três commits e duas branches.
5. Execute novamente e compare a saída.

## Resultado esperado

```text
commits=3
branches=2
working_tree=limpa
feature_integrada=sim
ancestralidade=ok
git=ok
```

## Validação

As seis linhas devem se repetir e o status ser zero.

## Conclusão

O exercício demonstra que branch é referência, commit nasce do index e merge registra a relação entre históricos.

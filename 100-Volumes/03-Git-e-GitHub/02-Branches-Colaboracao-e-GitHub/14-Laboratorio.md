---
title: Laboratório — Colaboração Distribuída com Git
description: "Simulação local de upstream, autora, revisão e integração."
tags: [git, github, laboratorio, bash]
aliases: [Laboratório Colaboração Git]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Colaboração Distribuída com Git

## Objetivo

Simular um repositório central e dois colaboradores: Alice propõe uma feature; Bob revisa o diff, integra e publica a branch principal.

## Pré-requisitos

- Git 2.28 ou superior;
- Bash;
- nenhum acesso de rede.

## Ambiente

O script usa repositório bare e clones temporários, identidades locais e datas fixas.

## Passos

1. Salve [[14-Solucao|a solução]] como `colaboracao.sh`.
2. Execute `bash -n colaboracao.sh`.
3. Execute `bash colaboracao.sh`.
4. Confirme duas identidades, três commits e duas branches remotas.
5. Execute novamente e compare a saída.

## Resultado esperado

```text
colaboradores=2
commits_main=3
branches_remotas=2
review=aprovada
feature_integrada=sim
colaboracao=ok
```

## Validação

As seis linhas devem se repetir e o status ser zero.

## Conclusão

O laboratório separa proposta, revisão e integração. GitHub acrescentaria PR, checks, identidade e enforcement ao mesmo grafo Git.

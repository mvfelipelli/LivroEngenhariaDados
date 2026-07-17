---
title: Laboratório — Validação de Pipeline CI/CD
description: "Análise reproduzível de DAG, permissões e gates."
tags: [github-actions, ci-cd, laboratorio, python]
aliases: [Laboratório CI CD]
created: 2026-07-17
updated: 2026-07-17
---

# Laboratório — Validação de Pipeline CI/CD

## Objetivo

Validar DAG de três jobs, permissões mínimas, artefato único, ambiente protegido e concurrency.

## Pré-requisitos

- Python 3.10 ou superior;
- somente biblioteca padrão;
- nenhum acesso ao GitHub.

## Passos

1. Salve [[14-Solucao|a solução]] como `validar_pipeline.py`.
2. Execute duas vezes.
3. Altere `deploy.needs` para `deploy` e confirme ciclo.

## Resultado esperado

```text
jobs=3
ordem=test,build,deploy
permissoes=minimas
artefato=unico
ambiente=protegido
concurrency=ativa
pipeline=ok
```

## Validação

As sete linhas devem se repetir e o status ser zero.

## Conclusão

Política estrutural complementa a execução real e impede configurações perigosas antes do merge.

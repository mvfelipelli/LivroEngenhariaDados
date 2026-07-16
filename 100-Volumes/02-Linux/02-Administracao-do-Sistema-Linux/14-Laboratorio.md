---
title: Laboratório — Auditoria de Prontidão Linux
aliases: [Laboratório Administração Linux]
tags: [linux, administracao, laboratorio, bash]
created: 2026-07-16
updated: 2026-07-16
description: "Auditoria idempotente de configuração, mounts e backup."
---

# Laboratório — Auditoria de Prontidão Linux

## Objetivo

Criar e auditar uma configuração temporária da DataRetail S.A. sem privilégios, validando oito controles operacionais.

## Pré-requisitos

- Bash 4 ou superior;
- `find`, `stat` e `sha256sum`;
- ambiente descartável ou Git Bash.

## Passos

1. Crie workspace com `mktemp -d` e `umask 027`.
2. Gere configuração do serviço e inventário de dois mounts.
3. Crie backup e hash de integridade.
4. Valide owner lógico, ambiente, dois mounts, opções seguras, backup, hash, permissões e espaço reservado.
5. Gere relatório determinístico.
6. Repita e compare o relatório.

## Resultado esperado

```text
checks=8
aprovados=8
servicos=1
mounts=2
backup=ok
permissao_config=640
segunda_execucao=sem_alteracoes
administracao=ok
```

> [!note]
> A solução usa fixtures para permanecer segura e reproduzível. Adapte os checks para `systemctl`, `findmnt` e sua ferramenta de backup em um host de laboratório.

Compare com [[14-Solucao]].

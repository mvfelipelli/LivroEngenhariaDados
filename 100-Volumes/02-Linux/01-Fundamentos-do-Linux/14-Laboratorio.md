---
title: Laboratório — Workspace Seguro de Ingestão
aliases: [Laboratório Linux]
tags: [linux, laboratorio, bash, seguranca]
created: 2026-07-16
updated: 2026-07-16
description: "Criação idempotente de workspace com permissões e integridade."
---

# Laboratório — Workspace Seguro de Ingestão

## Objetivo

Criar um workspace temporário para ingestão da DataRetail S.A., aplicar permissões, gerar manifesto SHA-256 e provar idempotência.

## Pré-requisitos

- Linux ou ambiente compatível;
- Bash 4 ou superior;
- utilitários `find`, `stat` e `sha256sum`.

## Ambiente e passos

1. Crie diretório temporário com `mktemp -d`.
2. Configure `umask 027`.
3. Crie cinco diretórios operacionais.
4. Gere um arquivo de pedidos somente se estiver ausente.
5. Aplique `750` aos diretórios e `640` aos arquivos.
6. Gere manifesto de integridade.
7. Execute a função novamente e compare snapshots.
8. Remova o workspace automaticamente ao sair.

## Resultado esperado

```text
workspace=ok
diretorios=5
arquivos=2
permissao_diretorio=750
entradas_manifesto=1
segunda_execucao=sem_alteracoes
linux=ok
```

> [!warning]
> O laboratório usa um diretório criado por `mktemp`. Não substitua por caminho do sistema sem revisar as operações de limpeza.

Compare com [[14-Solucao]].

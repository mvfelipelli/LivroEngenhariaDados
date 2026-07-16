---
title: Fundamentos do Linux
aliases: [Introdução ao Linux]
tags: [linux, fundamentos, volume-02, modulo-01]
type: modulo
status: concluido
created: 2026-07-16
updated: 2026-07-16
description: "Fundamentos do sistema Linux e de sua operação segura no terminal."
---

# Módulo 01 — Fundamentos do Linux

> [!abstract]
> Linux é a base operacional de grande parte das plataformas de dados. Compreender kernel, shell, filesystem, permissões, processos e fluxos de texto permite operar e diagnosticar sistemas com segurança.

## Estrutura

- [[01-Objetivos]]
- [[02-Introducao]]
- [[03-Linux-e-o-Papel-na-Engenharia-de-Dados]]
- [[04-Arquitetura-Kernel-Shell-e-Distribuicoes]]
- [[05-Sistema-de-Arquivos-Caminhos-e-Tipos]]
- [[06-Usuarios-Grupos-Permissoes-e-Sudo]]
- [[07-Processos-Sinais-Servicos-e-Recursos]]
- [[08-Terminal-Comandos-Documentacao-e-Pipes]]
- [[09-Seguranca-Ambientes-e-Boas-Praticas]]
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
    A[Usuário] --> B[Shell e utilitários]
    B --> C[Chamadas de sistema]
    C --> D[Kernel Linux]
    D --> E[CPU, memória, discos e rede]
```

## Projeto integrador

A DataRetail S.A. preparará e validará um workspace seguro para recepção de arquivos de pedidos.

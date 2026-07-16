---
title: Exercícios de Fundamentos do Linux
aliases: [Exercícios do Módulo Linux]
tags: [linux, exercicios, modulo-01]
created: 2026-07-16
updated: 2026-07-16
description: "Exercícios progressivos sobre Linux e terminal."
---

# Exercícios

## Revisão

1. Diferencie kernel, shell e distribuição.
2. Explique caminho absoluto, relativo, `.` e `..`.
3. Interprete `-rw-r-----`.
4. Diferencie processo, programa e serviço.

## Interpretação

5. Um diretório tem leitura sem execução. O que o usuário consegue fazer?
6. Um processo ignora SIGTERM. Qual deve ser a sequência de resposta?
7. Um pipeline perde mensagens de erro ao redirecionar stdout. Explique.
8. Uma variável de caminho é usada sem aspas em `rm`. Qual risco existe?

## Aplicação

9. Crie árvore `incoming`, `processing`, `quarantine`, `archive` e `logs`.
10. Defina permissões para owner completo, grupo leitura/execução e nenhum acesso externo.
11. Conte status de um arquivo usando `cut`, `sort` e `uniq`.
12. Inspecione processos, memória, filesystem e consumo de um diretório.

## Desafios

13. Escreva script idempotente para preparar um workspace.
14. Adicione `trap` para limpar temporários.
15. Produza manifesto SHA-256 dos arquivos recebidos.
16. Execute o [[14-Laboratorio]] e acrescente validação de `umask`.

Consulte [[13-Gabarito]] depois de elaborar as respostas.

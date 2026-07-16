---
title: Referências — Shell Script e Automação
aliases: [Referências Bash]
tags: [linux, bash, referencias]
created: 2026-07-16
updated: 2026-07-16
description: "Documentação oficial, padrões e bibliografia do módulo."
---

# Referências

## Documentação oficial e padrões

- GNU Project. *Bash Reference Manual*. Sintaxe, expansões, builtins, arrays, traps e execução.
- GNU Project. *Bash Manual — Shell Parameter Expansion*.
- GNU Project. *Coreutils Manual*. `sort`, `mktemp`, `mv`, `sha256sum` e demais utilitários.
- POSIX.1-2024. *Shell Command Language*. Contrato portátil de `sh` e utilitários.
- Linux man-pages project. `execve(2)`, `signal(7)`, `flock(2)` e `cron(8)`.
- systemd. *systemd.service* e *systemd.timer*.
- ShellCheck. *ShellCheck Wiki*. Diagnósticos e justificativas de análise estática.

## Livros

- COOPER, Mendel. *Advanced Bash-Scripting Guide*.
- NEWMAN, Chris; ROSENBLATT, Bill. *Learning the bash Shell*. O'Reilly.
- ROBBINS, Arnold; BEEBE, Nelson H. F. *Classic Shell Scripting*. O'Reilly.
- SHOTTS, William. *The Linux Command Line*. No Starch Press.

## Prática recomendada

Consulte primeiro o manual da versão instalada (`help`, `man bash`, `info coreutils`) e teste no interpretador mínimo declarado. Para segurança, valide também as políticas da distribuição e do ambiente de execução.

> [!tip]
> Documentação de ferramenta explica mecanismos; combine-a com os fundamentos de [[06-Erros-Sinais-Traps-e-Idempotencia]] e os controles de [[09-Seguranca-Portabilidade-Agendamento-e-Operacao]].

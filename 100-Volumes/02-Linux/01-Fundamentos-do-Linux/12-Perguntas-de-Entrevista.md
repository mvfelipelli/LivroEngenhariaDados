---
title: Perguntas de Entrevista sobre Fundamentos do Linux
aliases: [Entrevista Linux]
tags: [linux, entrevista, carreira]
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e respostas fundamentais sobre Linux."
---

# Perguntas de Entrevista

## 1. Kernel e shell são a mesma coisa?

Não. Kernel gerencia hardware e recursos; shell interpreta comandos e inicia programas.

## 2. Caminho absoluto e relativo diferem como?

O absoluto começa em `/`; o relativo é resolvido a partir do diretório atual.

## 3. O que significa `chmod 750`?

Owner lê, escreve e executa; grupo lê e executa; outros não possuem permissão.

## 4. Por que `x` importa em diretórios?

Permite atravessar e acessar entradas conhecidas; `r` permite listar nomes.

## 5. SIGTERM e SIGKILL diferem como?

SIGTERM pode ser tratado para limpeza; SIGKILL é imposto pelo kernel e não pode ser capturado.

## 6. O que é um pipe?

Conexão do stdout de um processo ao stdin do seguinte.

## 7. Para que serve stderr?

Separar diagnósticos e erros da saída de dados.

## 8. O que é inode?

Estrutura que guarda metadados e referências aos blocos de um arquivo.

## 9. Como investigar disco aparentemente livre?

Verificar blocos, inodes, arquivos abertos removidos, mounts e consumo por diretório.

## 10. Como escrever script mais seguro?

Validar entradas, usar aspas, menor privilégio, caminhos controlados, `set -Eeuo pipefail`, logs e idempotência.

Pratique em [[13-Exercicios]].

---
title: Gabarito — Fundamentos Python
description: "Respostas dos exercícios do módulo."
tags: [python, gabarito]
aliases: [Gabarito Fundamentos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Gabarito

## 1

Python é a especificação da linguagem; CPython é uma implementação; bytecode é a representação intermediária avaliada pela máquina virtual.

## 2

Executar `python -c "import sys; print(sys.executable)"` e `python -m pip --version`. Ambos devem apontar para o ambiente esperado.

## 3

`Path("dados") / nome`. A API representa caminhos semanticamente e adapta separadores ao sistema.

## 4

Por exemplo: `0` sucesso, `2` uso ou entrada ausente e `3` conteúdo inválido. O essencial é documentar e manter estabilidade.

## 5

A faixa permite várias versões compatíveis; o lock registra a seleção exata usada para reconstruir uma aplicação.

## 6

Localmente, variável de ambiente ou cofre de desenvolvimento; no CI, secret store com injeção temporária e mascaramento de logs.

## 7

Use `argparse`, converta para `Path`, teste `is_file()`, escreva erros em `stderr` e retorne código não zero.

## 8

Formatar estabiliza estilo; lint detecta padrões; tipos verificam contratos; testes confirmam comportamento. O CI executa os mesmos comandos e bloqueia integração diante de falha.

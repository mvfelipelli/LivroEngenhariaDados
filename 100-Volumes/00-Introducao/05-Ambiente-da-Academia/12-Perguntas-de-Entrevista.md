---
title: Perguntas de Entrevista — Ambiente Técnico
description: "Questões comentadas sobre reprodutibilidade e ferramentas."
tags: [ambiente, entrevista, reproducibilidade]
aliases: [Entrevista Ambiente Técnico]
created: 2026-07-21
updated: 2026-07-21
---

# Perguntas de Entrevista

## Terminal e shell são iguais?

Não. Terminal fornece interface; shell interpreta comandos e possui sintaxe própria.

## Por que usar ambiente virtual?

Para isolar dependências do projeto e reduzir conflito com instalação global.

## Container é uma máquina virtual?

Não. Containers compartilham kernel e isolam processos; VMs virtualizam um sistema completo.

## O que deve entrar no Git?

Código, contratos, testes e configuração não sensível; nunca segredos ou grandes artefatos regeneráveis.

## Como diagnosticar “comando não encontrado”?

Confirmar instalação, executável, PATH, shell, versão e contexto antes de reinstalar.

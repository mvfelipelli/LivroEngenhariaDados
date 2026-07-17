---
title: Perguntas de Entrevista — Arquivos e Serialização Python
description: "Questões sobre formatos, tempo e regex."
tags: [python, entrevista, arquivos]
aliases: [Entrevista Arquivos Python]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Por que usar `pathlib`?

Para representar e operar caminhos semanticamente, com separadores e APIs portáveis.

## 2. Texto e binário diferem como?

Texto decodifica bytes em str e trata newlines; binário entrega bytes sem conversão.

## 3. Por que `newline=""` com CSV?

Para que o módulo csv controle corretamente convenções de fim de linha.

## 4. JSON valida schema?

Não. O parser confirma sintaxe; estrutura e domínio exigem validação separada.

## 5. Por que evitar pickle externo?

Desserializar pode executar código arbitrário e o formato não é adequado a dados não confiáveis.

## 6. Datetime naive é UTC?

Não. Ele não possui timezone; interpretá-lo como UTC sem contrato é uma suposição.

## 7. Quando usar `fullmatch`?

Quando todo o texto deve obedecer ao padrão, evitando aceitação parcial.

## 8. Rename é sempre atômico?

Não. As garantias dependem do sistema e normalmente exigem origem e destino no mesmo filesystem.

---
title: Perguntas de Entrevista
description: "Perguntas sobre modelagem dimensional."
tags: [modelagem-de-dados, entrevista, dimensional]
aliases: [Entrevista Modelagem Dimensional]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Qual o primeiro passo dimensional?

Selecionar processo de negócio; em seguida declarar o grão.

## 2. O que é bus matrix?

Matriz que cruza processos de negócio e dimensões conformadas.

## 3. Fato transacional e snapshot diferem como?

O primeiro registra evento atômico; o segundo registra estado em período.

## 4. Saldo é aditivo?

Geralmente semiaditivo: soma entre contas, mas não entre instantes.

## 5. O que é dimensão conformada?

Dimensão com semântica e conteúdo compatíveis compartilhados por processos.

## 6. Para que serve chave substituta?

Identificar versões dimensionais e desacoplar fatos das chaves operacionais.

## 7. O que é dimensão degenerada?

Identificador dimensional guardado na fato sem tabela própria, como número de pedido.

## 8. Estrela e snowflake diferem como?

Estrela desnormaliza dimensões; snowflake separa hierarquias em relações adicionais.

## 9. Como tratar late arriving dimension?

Unknown, membro inferido, quarentena ou retry, conforme impacto e SLO.

## 10. Como evitar fanout entre fatos?

Agregue cada fato ao mesmo grão dimensional antes de juntá-las.

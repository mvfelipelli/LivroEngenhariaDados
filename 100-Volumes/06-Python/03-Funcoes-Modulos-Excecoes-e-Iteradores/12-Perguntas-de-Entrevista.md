---
title: Perguntas de Entrevista — Funções e Iteradores Python
description: "Questões sobre abstrações, erros e lazy evaluation."
tags: [python, entrevista, iteradores]
aliases: [Entrevista Funções Python]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Quando defaults são avaliados?

Uma vez, durante a execução da definição da função. Objetos mutáveis podem acumular estado.

## 2. O que é closure?

Função que mantém referências aos nomes livres do escopo lexical em que foi criada.

## 3. Por que usar `functools.wraps`?

Para preservar nome, documentação e outros metadados da função decorada.

## 4. O que ocorre na primeira importação?

O módulo é criado, seu código de nível superior executa e o objeto fica em `sys.modules`.

## 5. Quando criar uma exceção própria?

Quando o chamador precisa distinguir semanticamente uma falha do domínio ou da camada.

## 6. Iterável e iterador são iguais?

Não. Iterável fornece iterador; iterador mantém estado e produz itens até `StopIteration`.

## 7. Qual a vantagem de geradores?

Produção sob demanda, composição e uso de memória proporcional ao estado ativo.

## 8. O que um context manager garante?

Que a etapa de saída seja executada ao deixar o bloco, inclusive diante de exceção.

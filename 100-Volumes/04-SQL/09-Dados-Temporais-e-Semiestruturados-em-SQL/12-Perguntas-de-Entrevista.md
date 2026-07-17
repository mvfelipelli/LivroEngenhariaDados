---
title: Perguntas de Entrevista
description: "Perguntas e respostas sobre tempo e JSON em SQL."
tags: [sql, entrevista, temporal, json]
aliases: [Entrevista SQL Temporal e JSON]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Data e instante são iguais?

Não. Data é conceito civil; instante é ponto global na linha do tempo.

## 2. Por que usar intervalos `[início, fim)`?

Eles permitem versões adjacentes sem sobreposição e predicados consistentes nas fronteiras.

## 3. O que é uma consulta as of?

Consulta que retorna a versão válida em um instante especificado.

## 4. Tempo de evento e tempo de sistema diferem como?

O primeiro representa quando o fato ocorreu; o segundo, quando o banco conhecia determinada versão.

## 5. O que é bitemporalidade?

Preservação simultânea dos intervalos de validade do negócio e registro no sistema.

## 6. Campo ausente e JSON null são iguais?

Não. Ausente significa que o caminho não existe; `null` é valor explicitamente presente.

## 7. Quando normalizar um array JSON?

Quando seus elementos exigem joins, constraints, indexação ou análise frequente.

## 8. Qual risco existe ao expandir dois arrays?

Produto cartesiano e duplicação de métricas se cada coleção tiver vários elementos.

## 9. Como indexar atributo JSON frequente?

Com índice de expressão ou coluna gerada; índices invertidos servem a consultas mais variadas conforme o SGBD.

## 10. Como evoluir um payload?

Versione, mantenha leitores compatíveis, valide ambos os formatos, migre histórico se necessário e retire o legado após observação.

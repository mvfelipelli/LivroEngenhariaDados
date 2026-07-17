---
title: Perguntas de Entrevista
description: "Perguntas sobre modelagem física e desempenho."
tags: [modelagem-de-dados, entrevista, desempenho]
aliases: [Entrevista Modelagem Física]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Modelo lógico e físico diferem como?

O lógico organiza relações e regras; o físico escolhe tipos, índices, layout e recursos de um mecanismo.

## 2. Qual risco de default zero?

Ele pode converter valor desconhecido em medida legítima e corromper semântica.

## 3. UUID aleatório tem qual trade-off?

Geração distribuída simples, mas chave larga e inserções dispersas em estruturas ordenadas.

## 4. Como ordenar colunas de índice composto?

Pelos predicados e ordem do workload, considerando igualdade, faixa, seletividade e cobertura.

## 5. Particionamento substitui índice?

Não. Partição reduz conjunto por pruning; índice localiza linhas dentro do conjunto.

## 6. O que é skew?

Distribuição desigual que concentra armazenamento ou processamento em poucas partições.

## 7. Row store e column store atendem quais usos?

Linhas favorecem registros completos e escrita pontual; colunas favorecem scans analíticos de poucas colunas.

## 8. O que é desnormalização controlada?

Redundância intencional com fonte canônica, atualização, tolerância a atraso e reconciliação.

## 9. Como justificar índice?

Com consulta, plano, frequência, ganho medido e custo de escrita/espaço.

## 10. Como evoluir desenho físico?

Criar estrutura paralela, backfill, validar, migrar tráfego, observar e remover legado depois.

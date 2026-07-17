---
title: Perguntas de Entrevista
description: "Perguntas sobre lakehouse e produtos de dados."
tags: [modelagem-de-dados, entrevista, lakehouse]
aliases: [Entrevista Modelagem Lakehouse]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Bronze, Silver e Gold diferem como?

Recepção rastreável, dado canônico validado e modelo orientado ao consumo.

## 2. Parquet e Avro atendem quais padrões?

Parquet favorece analytics colunar; Avro favorece registros e intercâmbio.

## 3. O que tabela lakehouse adiciona?

Metadados de snapshots, transações, evolução e planejamento sobre arquivos.

## 4. Time travel é backup?

Não. Snapshots podem expirar e compartilhar arquivos; backup tem política independente.

## 5. O que causa small files?

Microbatches, alta cardinalidade de partição e writers paralelos com pouco volume.

## 6. Schema-on-read elimina contrato?

Não. Apenas posterga interpretação; consumidores ainda precisam de tipos e semântica.

## 7. O que é produto de dados?

Interface mantida para consumidores, com owner, contrato, qualidade e suporte.

## 8. O que é mudança backward compatible?

Novo leitor continua processando dados produzidos pelo schema anterior.

## 9. Como escolher partição?

Por filtros, volume, cardinalidade e unidade de manutenção.

## 10. O que governança federada resolve?

Alinha domínios autônomos em padrões de identidade, segurança, contrato e interoperabilidade.

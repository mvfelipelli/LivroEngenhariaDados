---
title: Perguntas de Entrevista — Pipelines Python
description: "Questões sobre incrementalidade, idempotência e observabilidade."
tags: [python, entrevista, pipelines]
aliases: [Entrevista Projeto Final Python]
created: 2026-07-20
updated: 2026-07-20
---

# Perguntas de Entrevista

## 1. O que pertence ao núcleo do pipeline?

Regras e contratos do domínio, sem detalhes de arquivo, banco, rede ou framework.

## 2. Erro de dado e falha sistêmica diferem como?

O primeiro é um registro conhecido que viola contrato; a segunda compromete a execução e normalmente interrompe o lote.

## 3. Quando avançar o watermark?

Depois que os dados correspondentes estiverem confirmados, idealmente na mesma transação.

## 4. Retry garante exactly-once?

Não. Sem idempotência, repetição pode duplicar efeitos; exactly-once depende do protocolo completo.

## 5. Como executar backfill com segurança?

Isole intervalo e estado, limite capacidade, use sink idempotente e reconcilie antes da promoção.

## 6. Quais métricas devem reconciliar?

Por exemplo, lidos igual a aceitos mais rejeitados, além de totais da fonte e do destino.

## 7. O que um SLO de pipeline mede?

Disponibilidade, pontualidade, freshness ou qualidade percebida pelo consumidor dentro de uma janela.

## 8. O que torna um deploy reproduzível?

Artefato imutável, dependências fixadas, configuração externa, ambiente limpo e smoke test.

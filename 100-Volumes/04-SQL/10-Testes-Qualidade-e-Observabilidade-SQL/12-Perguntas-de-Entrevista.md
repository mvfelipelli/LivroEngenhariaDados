---
title: Perguntas de Entrevista
description: "Perguntas e respostas sobre qualidade e observabilidade SQL."
tags: [sql, entrevista, qualidade]
aliases: [Entrevista Qualidade SQL]
created: 2026-07-17
updated: 2026-07-17
---

# Perguntas de Entrevista

## 1. Teste e observabilidade diferem como?

Teste verifica expectativa definida; observabilidade permite explicar comportamento durante a operação.

## 2. O que torna uma fixture útil?

Ser pequena, determinística, legível e cobrir fronteiras relevantes.

## 3. Constraint substitui teste de dados?

Não. Ela protege regras locais; reconciliação e regras entre conjuntos exigem testes adicionais.

## 4. Por que contagem total é insuficiente?

Perdas e duplicações podem se compensar. É preciso segmentar e comparar chaves e valores.

## 5. O que é teste de propriedade?

Verificação de invariante que deve valer para muitas entradas, como idempotência ou unicidade.

## 6. Como medir freshness?

Compare o dado mais recente disponível ao instante esperado, considerando origem e calendário.

## 7. Quais metadados registrar por execução?

Run ID, versão, parâmetros, janela, contagens, duração, watermark e testes.

## 8. SLI e SLO diferem como?

SLI é a medida; SLO é o alvo definido para essa medida.

## 9. O que torna um alerta acionável?

Impacto claro, owner, severidade, contexto, runbook e critério de recuperação.

## 10. Como evitar recorrência?

Transforme a causa e fatores contribuintes em testes, limites, automação ou desenho mais seguro.

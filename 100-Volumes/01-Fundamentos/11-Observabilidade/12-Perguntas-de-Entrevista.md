---
title: Perguntas de Entrevista sobre Observabilidade
aliases: [Entrevista de Observabilidade de Dados]
tags: [observabilidade, entrevista, carreira]
created: 2026-07-16
updated: 2026-07-16
description: "Perguntas e respostas fundamentadas sobre observabilidade de dados."
---

# Perguntas de Entrevista

## 1. Monitoramento e observabilidade são iguais?

Não. Monitoramento verifica condições previstas; observabilidade permite inferir estados e investigar comportamentos não antecipados.

## 2. Quais são os sinais clássicos?

Logs, métricas e traces, complementados por perfis e, em dados, qualidade, schema, freshness e linhagem.

## 3. Por que correlação é importante?

Porque conecta evidências de sistemas diferentes à mesma run, partição, versão e jornada.

## 4. O que é alta cardinalidade?

Grande número de combinações de labels, que aumenta armazenamento e custo de consulta de métricas.

## 5. Como observar um pipeline verde com dados ruins?

Instrumentando contratos, volume, completude, distribuição, schema, freshness e reconciliação.

## 6. Qual o papel da linhagem?

Localizar causas upstream, consumidores downstream e escopo temporal do impacto.

## 7. O que torna um alerta acionável?

Sintoma relevante, impacto, severidade, contexto, owner e runbook.

## 8. SLI, SLO e SLA diferem como?

SLI mede; SLO define meta; SLA formaliza compromisso e possíveis consequências.

## 9. O que deve existir em um postmortem?

Impacto, linha do tempo, detecção, fatores contribuintes, resposta, aprendizados e ações verificáveis.

## 10. Como controlar custo de telemetria?

Gerenciar cardinalidade, amostragem, retenção, agregação, indexação e cobertura por criticidade.

Pratique em [[13-Exercicios]].

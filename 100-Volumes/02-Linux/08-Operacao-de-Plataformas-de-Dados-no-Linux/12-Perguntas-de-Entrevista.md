---
title: Perguntas de Entrevista — Operação de Plataformas de Dados
description: "Perguntas progressivas com respostas fundamentadas."
tags: [linux, operacao, entrevista]
aliases: [Entrevista Operação Linux]
created: 2026-07-16
updated: 2026-07-16
---

# Perguntas de Entrevista

## 1. SLI, SLO e SLA diferem em quê?

SLI é medida, SLO é alvo interno e SLA é compromisso com consequências definidas.

## 2. O que é failure domain?

Conjunto de componentes que podem falhar juntos, como host, rack, zona, conta ou sistema de identidade.

## 3. RPO e RTO significam quê?

RPO limita perda de dados aceitável; RTO limita tempo para restaurar capacidade.

## 4. Replicação substitui backup?

Não. Pode propagar corrupção ou exclusão e compartilha falhas; backup preserva versões recuperáveis.

## 5. O que torna uma automação operável?

Entradas validadas, idempotência, lock, timeout, retry classificado, logs, métricas, estado e código de saída.

## 6. Health check deve testar dependências?

Depende do propósito. Readiness pode refletir dependência essencial; liveness não deve reiniciar por falha externa indiscriminada.

## 7. O que é error budget?

Quantidade de falha permitida pelo SLO na janela, usada para equilibrar confiabilidade e mudança.

## 8. Como evitar rollback impossível?

Use mudanças de schema compatíveis, expand-contract, artefato preservado, configuração versionada e teste real.

## 9. O que um runbook deve conter?

Escopo, risco, pré-requisitos, diagnóstico, ações, rollback, validação, escalonamento e referências.

## 10. Quando declarar desastre?

Segundo critérios e autoridade pré-definidos, quando recuperação normal não atende objetivo e DR é justificado.

## 11. Como medir frescor de dados?

Compare timestamp ou watermark confiável do dado publicado com expectativa, distinguindo ausência, atraso e relógio.

## 12. Como planejar capacidade?

Projete crescimento, picos, retenção, replicação, backfill, falha e lead time, mantendo headroom.

## 13. O que é toil?

Trabalho manual, repetitivo, automatizável e sem valor duradouro que cresce com o serviço.

## 14. O que é production readiness review?

Gate multidisciplinar que verifica se serviço possui contratos, segurança, operação, recuperação e responsabilidade suficientes.

---
title: Event Time, Processing Time e Atrasos
description: "Semântica temporal e eventos fora de ordem."
tags: [apache-spark, event-time, streaming]
aliases: [Event Time Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Event Time, Processing Time e Atrasos

Event time é quando o evento ocorreu no domínio; processing time é quando o Spark o processa; ingestion time é quando entrou na plataforma. Redes, dispositivos offline e retries fazem eventos chegarem fora de ordem.

Janelas por processing time mudam com indisponibilidade e backlog. Métricas de negócio geralmente exigem event time, timezone explícito e política para eventos atrasados.

O atraso observado é `processing_time - event_time`, mas relógios incorretos e eventos futuros precisam de validação. Analise a distribuição de atraso por fonte e período antes de escolher watermark.

> [!note]
> Watermark não é SLA de chegada; é uma fronteira de retenção de estado baseada no progresso temporal observado.

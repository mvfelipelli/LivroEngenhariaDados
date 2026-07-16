---
title: Referências de Pipelines de Dados
aliases: [Bibliografia de Pipelines]
tags: [pipelines, referencias, bibliografia]
created: 2026-07-16
updated: 2026-07-16
description: "Documentação oficial e livros para aprofundar pipelines de dados."
---

# Referências

## Livros

- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. O'Reilly Media, 2017.
- REIS, Joe; HOUSLEY, Matt. *Fundamentals of Data Engineering*. O'Reilly Media, 2022.
- AKIDZA, James et al. *Streaming Systems*. O'Reilly Media, 2018.
- BEYER, Betsy et al. *Site Reliability Engineering*. O'Reilly Media, 2016.

## Documentação oficial

- Apache Airflow. *Core Concepts — DAGs, Tasks and Backfill*.
- Apache Beam. *Programming Guide — Windowing, Watermarks and Triggers*.
- Apache Flink. *Documentation — Stateful Stream Processing and Checkpoints*.
- Apache Kafka. *Design — Delivery Semantics*.
- PostgreSQL. *INSERT — ON CONFLICT Clause*.
- SQLite. *UPSERT and Transaction Documentation*.

## Padrões e especificações

- OpenTelemetry. *Logs, Metrics and Traces*.
- OpenLineage. *Open Standard for Lineage Metadata Collection*.
- Cloud Native Computing Foundation. *CloudEvents Specification*.

## Roteiro de aprofundamento

1. reveja [[04-Componentes-Dependencias-e-DAGs]] antes de estudar um orquestrador;
2. conecte checkpoints e entrega a [[07-Estado-Confiabilidade-e-Idempotencia]];
3. transforme expectativas de consumo em SLOs usando [[08-Observabilidade-Qualidade-e-SLOs]];
4. implemente novamente o [[14-Laboratorio]] com uma ferramenta de orquestração de sua escolha.

Retorne ao índice em [[README|Módulo 07 — Pipelines de Dados]].

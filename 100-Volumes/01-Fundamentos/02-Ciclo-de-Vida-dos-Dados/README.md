---
title: Ciclo de Vida dos Dados
aliases:
  - Data Lifecycle
  - Data Life Cycle
tags:
  - engenharia-de-dados
  - fundamentos
  - ciclo-de-vida
  - data-lifecycle
  - volume-01
  - modulo-02
type: modulo
status: em-desenvolvimento
created: 2026-07-14
updated: 2026-07-16
description: "Visão geral, objetivos e navegação de Ciclo de Vida dos Dados."
---

# Módulo 02 — Ciclo de Vida dos Dados

> [!abstract]
> Neste módulo estudaremos como os dados percorrem todas as etapas de sua existência dentro de uma organização, desde sua geração até seu descarte. O entendimento desse ciclo é um dos pilares da Engenharia de Dados e servirá de base para praticamente todos os módulos seguintes desta formação.

---

## Objetivos do módulo

Ao concluir este módulo você será capaz de:

- compreender o conceito de Ciclo de Vida dos Dados;
- identificar todas as fases pelas quais um dado pode passar;
- diferenciar geração, ingestão, armazenamento, processamento e consumo;
- compreender a importância da governança durante todo o ciclo;
- entender como diferentes profissionais atuam em cada etapa;
- reconhecer riscos associados à má gestão do ciclo de vida;
- relacionar o ciclo de vida com arquiteturas modernas de dados;
- aplicar esses conceitos em ambientes reais.

---

## Por que estudar o Ciclo de Vida dos Dados?

Uma organização não trabalha apenas com bancos de dados.

Ela trabalha com **dados em movimento**.

Todos os dias novos dados são produzidos, coletados, armazenados, transformados, analisados, compartilhados, arquivados e eventualmente eliminados.

Cada uma dessas etapas possui desafios técnicos, requisitos legais, necessidades de qualidade e responsabilidades específicas.

A Engenharia de Dados existe justamente para garantir que esse fluxo aconteça de forma eficiente, segura, confiável e escalável.

Antes de aprender tecnologias como:

- PostgreSQL
- Spark
- Kafka
- Airflow
- Hive
- Trino
- Iceberg
- Delta Lake
- Data Warehouse
- Data Lake

é fundamental compreender **como os dados se movimentam dentro de uma organização**.

Esse entendimento permitirá enxergar cada ferramenta como parte de um processo muito maior.

---

## Estrutura do módulo

Este módulo está organizado em uma sequência lógica.

### Parte Conceitual

- [[01-Objetivos]]
- [[02-Introducao]]

---

### Fundamentos

- [[03-O-que-e-o-Ciclo-de-Vida-dos-Dados]]
- [[04-Geracao-e-Coleta-de-Dados]]
- [[05-Ingestao-de-Dados]]
- [[06-Armazenamento-de-Dados]]
- [[07-Processamento-de-Dados]]
- [[08-Consumo-e-Compartilhamento]]
- 09-Arquivamento-e-Descarte

---

### Aplicação

- 10-Estudo-de-Caso-DataRetail

---

### Revisão

- [[11-Resumo]]
- [[12-Perguntas-de-Entrevista]]
- [[13-Exercicios]]
- [[13-Gabarito]]
- [[14-Laboratorio]]
- [[14-Solucao]]
- [[15-Referencias]]

---

## O ciclo de vida em uma visão geral

```mermaid
flowchart LR

A[Geração]
--> B[Coleta]

B --> C[Ingestão]

C --> D[Armazenamento]

D --> E[Processamento]

E --> F[Consumo]

F --> G[Arquivamento]

G --> H[Descarte Seguro]
```

Embora apresentado como uma sequência linear, na prática esse processo é contínuo.

Os dados podem retornar para etapas anteriores, ser reprocessados, enriquecidos ou reutilizados diversas vezes durante sua existência.

---

## Relação com os próximos módulos

Este módulo prepara o terreno para diversos assuntos que serão aprofundados posteriormente.

| Módulo | Relação |
|----------|----------|
| Modelagem de Dados | Organização dos dados durante o armazenamento |
| Armazenamento de Dados | Tecnologias utilizadas na persistência |
| Processamento de Dados | ETL, ELT, Batch e Streaming |
| Integração de Dados | Movimentação entre sistemas |
| Governança | Controle durante todo o ciclo |
| Arquiteturas | Como as arquiteturas suportam o ciclo completo |

---

## Projeto Integrador

Durante este módulo continuaremos utilizando a empresa fictícia **DataRetail S.A.**

Ao longo dos capítulos acompanharemos o caminho percorrido pelos dados produzidos pelas operações da empresa, observando como eles transitam entre sistemas operacionais, pipelines de engenharia, plataformas analíticas e aplicações de negócio.

Essa abordagem permitirá conectar todos os conceitos apresentados com situações próximas da realidade encontrada em ambientes corporativos.

---

## Ao final deste módulo

Você compreenderá que a Engenharia de Dados não consiste apenas em construir pipelines ou bancos de dados.

Ela consiste em administrar toda a jornada dos dados, garantindo que eles sejam produzidos, transportados, armazenados, processados e disponibilizados de maneira confiável durante todo o seu ciclo de vida.

Nos próximos capítulos iniciaremos essa jornada entendendo, em detalhes, o que realmente significa o **Ciclo de Vida dos Dados**.

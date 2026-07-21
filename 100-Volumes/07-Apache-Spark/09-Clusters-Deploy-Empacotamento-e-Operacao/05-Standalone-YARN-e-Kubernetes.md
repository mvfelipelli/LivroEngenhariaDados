---
title: Standalone, YARN e Kubernetes
description: "Modelos de cluster manager e integração operacional."
tags: [apache-spark, yarn, kubernetes]
aliases: [Cluster Managers Spark]
created: 2026-07-20
updated: 2026-07-20
---

# Standalone, YARN e Kubernetes

Standalone é o gerenciador próprio do Spark e simplifica clusters dedicados. YARN integra recursos, filas e segurança do ecossistema Hadoop. Kubernetes cria driver e executors como pods e usa imagens, service accounts, quotas e políticas de rede.

| Critério | Standalone | YARN | Kubernetes |
|---|---|---|---|
| Ecossistema | Spark | Hadoop | Containers |
| Isolamento | Processos | Containers YARN | Pods/namespaces |
| Artefato típico | Pacote/JAR | Pacote/JAR | Imagem + pacote |

A escolha depende da plataforma existente, não só de desempenho. Logs, volumes, identidade, DNS, autoscaling e atualização precisam de integração específica.
